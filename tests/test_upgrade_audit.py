from __future__ import annotations
import hashlib, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "skills/upgrading-ariad/scripts/audit.py"

def tree_digest(root: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(x for x in root.rglob("*") if x.is_file() and ".git" not in x.parts):
        h.update(p.relative_to(root).as_posix().encode()); h.update(p.read_bytes())
    return h.hexdigest()

class UpgradeAuditTests(unittest.TestCase):
    def run_audit(self, target: Path, candidate: Path = ROOT, *extra: str):
        return subprocess.run([sys.executable, str(AUDIT), str(target), "--candidate", str(candidate), *extra, "--json"], text=True, capture_output=True, check=True)

    def test_mature_inventory_and_no_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); (target / "docs/project/roadmap/history").mkdir(parents=True)
            (target / "docs/process").mkdir(parents=True); (target / "docs/product").mkdir(parents=True)
            (target / "AGENTS.md").write_text("# Valuable custom rules\n")
            (target / "nested").mkdir(); (target / "nested/AGENTS.md").write_text("# Scope\n")
            (target / "docs/process/engineering-conventions.md").write_text("project owned\n")
            for p in ("docs/project/briefing.md", "docs/process/development-guide.md", "docs/product/principles.md"):
                (target / p).write_text("legacy\n")
            (target / "docs/project/roadmap/history/item.md").write_text("see docs/project/briefing.md\n")
            before = tree_digest(target); data = json.loads(self.run_audit(target).stdout)
            self.assertEqual(before, tree_digest(target))
            self.assertEqual(data["agents_scopes"], ["AGENTS.md", "nested/AGENTS.md"])
            self.assertIn("add exact entrypoint block to project-owned AGENTS.md", data["operations"]["manual_integration"])
            self.assertIn("no package found in probed locations; select installation destination manually", data["operations"]["manual_integration"])
            self.assertTrue(data["documents"]["briefing"]["legacy"])
            self.assertIn("docs/project/roadmap", data["project_memory"])
            self.assertIn("docs/process/engineering-conventions.md", data["adjacent_project_docs"])
            self.assertIn("docs/process/engineering-conventions.md", data["operations"]["retain_unchanged"])
            self.assertEqual(data["schema_version"], 1)

    def test_current_and_old_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); (target / "docs/ariad").mkdir(parents=True)
            (target / "AGENTS.md").write_text("<!-- ariad-entrypoint: docs/ariad/index.md -->\n@docs/ariad/index.md\n")
            (target / "docs/ariad/index.md").write_text("router\n")
            skill = target / ".agents/skills/using-ariad"; skill.mkdir(parents=True); (skill / "SKILL.md").write_text("skill\n")
            data = json.loads(self.run_audit(target).stdout)
            self.assertTrue(data["integration"]["marker"] and data["integration"]["directive"])
            self.assertTrue(data["installed_packages"][0]["present"])
            (target / "AGENTS.md").write_text("<!-- ariad-skill: using-ariad -->\n")
            self.assertTrue(json.loads(self.run_audit(target).stdout)["integration"]["old_marker"])

    def test_dirty_staged_and_url_sanitization(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); subprocess.run(["git", "init", "-q", str(target)], check=True)
            (target / "x").write_text("x"); subprocess.run(["git", "-C", str(target), "add", "x"], check=True)
            data = json.loads(self.run_audit(target).stdout); self.assertTrue(data["git"]["dirty"]); self.assertTrue(data["git"]["staged"])
        spec = importlib.util.spec_from_file_location("audit", AUDIT); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        self.assertEqual(module.sanitize_url("https://user:secret@example.com/repo.git"), "https://example.com/repo.git")
        self.assertEqual(module.sanitize_url("https://example.com/repo.git?token=secret#fragment"), "https://example.com/repo.git")
        self.assertEqual(module.sanitize_url("git@github.com:owner/repo.git"), "github.com:owner/repo.git")
        self.assertEqual(module.sanitize_url("ftp://u%40x:p@example.com/a?q#f"), "ftp://example.com/a")
        self.assertEqual(module.sanitize_url("weird://user:pw@example.com/a?q"), "weird://example.com/a")
        self.assertEqual(module.sanitize_url("scheme:opaque-secret"), "<redacted-unrecognized-url>")
        self.assertEqual(module.sanitize_url("https://user:pw@[broken/repo"), "<redacted-unrecognized-url>")
        self.assertEqual(module.sanitize_url("../repo?token=x"), "<redacted-unrecognized-url>")

    def test_manifest_is_closed_and_untrusted(self):
        spec = importlib.util.spec_from_file_location("audit", AUDIT); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp); content = b"skill\n"; (package / "SKILL.md").write_bytes(content)
            def write_manifest(destination="SKILL.md", package_digest=None):
                payload_digest = hashlib.sha256(destination.encode() + b"\0" + content + b"\0").hexdigest()
                (package / "manifest.json").write_text(json.dumps({"package": "using-ariad", "package_version": "1", "package_digest": package_digest or payload_digest, "files": [{"destination": destination, "sha256": hashlib.sha256(content).hexdigest()}]}))
            write_manifest("../outside")
            self.assertIn("invalid destination: ../outside", module.package(package, package.parent)["manifest"]["invalid_reasons"])
            write_manifest("..\\outside")
            self.assertIn("invalid destination: ..\\outside", module.package(package, package.parent)["manifest"]["invalid_reasons"])
            write_manifest(package_digest="0" * 64)
            self.assertIn("package digest mismatch", module.package(package, package.parent)["manifest"]["invalid_reasons"])
            write_manifest(); (package / "extra.txt").write_text("unexpected")
            self.assertIn("unexpected inventory file: extra.txt", module.package(package, package.parent)["manifest"]["invalid_reasons"])
            (package / "extra.txt").unlink()
            external = package.parent / "external-skill"
            external.write_bytes(content); (package / "SKILL.md").unlink()
            try:
                (package / "SKILL.md").symlink_to(external)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            self.assertIn("destination missing or unsafe: SKILL.md", module.package(package, package.parent)["manifest"]["invalid_reasons"])

    def test_unexpected_symlink_directory_is_in_closed_inventory(self):
        spec = importlib.util.spec_from_file_location("audit", AUDIT); module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            package = Path(tmp); content = b"skill\n"; (package / "SKILL.md").write_bytes(content)
            package_digest = hashlib.sha256(b"SKILL.md\0" + content + b"\0").hexdigest()
            (package / "manifest.json").write_text(json.dumps({"format_version":"1","package":"using-ariad","source_path":"skills/using-ariad","package_version":"1","method_digest":"0"*64,"package_digest":package_digest,"files":[{"destination":"SKILL.md","sha256":hashlib.sha256(content).hexdigest()}]}))
            try:
                (package / "unexpected-dir").symlink_to(Path(outside), target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            self.assertIn("unexpected inventory file: unexpected-dir", module.package(package, package.parent)["manifest"]["invalid_reasons"])

    def test_fresh_and_existing_operation_classification(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            data = json.loads(self.run_audit(target).stdout)
            self.assertIn("add minimal root AGENTS.md entrypoint", data["operations"]["safe_additive"])
            self.assertIn("add docs/ariad/index.md router", data["operations"]["safe_additive"])
            data = json.loads(self.run_audit(target, ROOT, "--skill-destination", ".agents/skills/using-ariad").stdout)
            self.assertTrue(any(x.startswith("install complete") for x in data["operations"]["safe_additive"]))
            (target / "AGENTS.md").write_text("custom\n")
            (target / "docs/project").mkdir(parents=True)
            data = json.loads(self.run_audit(target).stdout)
            self.assertIn("add exact entrypoint block to project-owned AGENTS.md", data["operations"]["manual_integration"])
            self.assertIn("add docs/ariad/index.md router", data["operations"]["manual_integration"])

    def test_target_symlinks_are_not_followed(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            target, external = Path(tmp), Path(outside)
            (external / "AGENTS.md").write_text("outside")
            (external / "leak.md").write_text("docs/project/briefing.md")
            try:
                (target / "linked").symlink_to(external, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            before = tree_digest(external); data = json.loads(self.run_audit(target).stdout)
            self.assertEqual(before, tree_digest(external))
            self.assertEqual(data["agents_scopes"], [])
            self.assertEqual(data["legacy_inbound_references"]["docs/project/briefing.md"], [])

    def test_git_index_and_worktree_are_byte_for_byte_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); subprocess.run(["git", "init", "-q", str(target)], check=True)
            subprocess.run(["git", "-C", str(target), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(target), "config", "user.name", "Test"], check=True)
            (target / "fixture.txt").write_text("committed\n")
            subprocess.run(["git", "-C", str(target), "add", "fixture.txt"], check=True)
            subprocess.run(["git", "-C", str(target), "commit", "-qm", "fixture"], check=True)
            index = target / ".git/index"; before = (index.read_bytes(), index.stat().st_mode, index.stat().st_size, tree_digest(target))
            self.run_audit(target)
            after = (index.read_bytes(), index.stat().st_mode, index.stat().st_size, tree_digest(target))
            self.assertEqual(before, after)

    def test_intermediate_symlinks_are_collisions_and_external_trees_are_unread(self):
        for relative in (".agents", "docs"):
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
                target, external = Path(tmp), Path(outside); (external / "secret").write_text("do-not-read")
                (target / relative).symlink_to(external, target_is_directory=True)
                data = json.loads(self.run_audit(target).stdout)
                self.assertNotIn("secret", json.dumps(data)); self.assertEqual((external / "secret").read_text(), "do-not-read")
        for relative in ("skills", "docs"):
            with self.subTest(candidate=relative), tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside, tempfile.TemporaryDirectory() as target_tmp:
                candidate, external = Path(tmp), Path(outside); (external / "secret").write_text("do-not-read")
                (candidate / relative).symlink_to(external, target_is_directory=True)
                data = json.loads(self.run_audit(Path(target_tmp), candidate).stdout)
                self.assertFalse(data["candidate"]["package_valid"]); self.assertNotIn("do-not-read", json.dumps(data))

    def test_empty_unrelated_candidate_denies_candidate_operations(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as target_tmp:
            candidate, target = Path(tmp), Path(target_tmp); (candidate / "README").write_text("unrelated")
            data = json.loads(self.run_audit(target, candidate, "--skill-destination", ".agents/skills/using-ariad").stdout)
            self.assertFalse(data["candidate"]["package_valid"])
            self.assertFalse(data["operations"]["safe_additive"])
            self.assertTrue(data["operations"]["destructive_ambiguous_denied"])

    def test_unsafe_cli_paths_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            for value in ("/absolute", "../escape", "a\\b", "a/./b"):
                result = subprocess.run([sys.executable, str(AUDIT), tmp, "--candidate", str(ROOT), "--skill-destination", value], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)

if __name__ == "__main__": unittest.main()
