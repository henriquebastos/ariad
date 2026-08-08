from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADOPT = ROOT / "skills/using-ariad/scripts/adopt.py"
ASSETS = ROOT / "skills/using-ariad/assets/project-templates"
MARKER = "<!-- ariad-entrypoint: docs/ariad/index.md -->"
DIRECTIVE = "@docs/ariad/index.md"

class AdoptTests(unittest.TestCase):
    def run_adopt(self, target: Path, apply: bool = False):
        command = [sys.executable, str(ADOPT), str(target)]
        if apply: command.append("--apply")
        return subprocess.run(command, text=True, capture_output=True)

    def test_adoption_guarantees(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = self.run_adopt(target)
            self.assertEqual(result.returncode, 0)
            self.assertIn("ready", result.stdout)
            self.assertEqual(list(target.iterdir()), [])
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 0)
            expected = {p.relative_to(ASSETS) for p in ASSETS.rglob("*") if p.is_file()}
            actual = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
            self.assertEqual(actual, expected)
            self.assertFalse((target / "index.md").exists())
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 0)
            self.assertIn("already adopted", result.stdout)

    def test_unintegrated_agents_stops_all_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); (target / "AGENTS.md").write_text("# Local rules\n")
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 3)
            self.assertIn("manual integration required", result.stderr)
            self.assertEqual([p.name for p in target.iterdir()], ["AGENTS.md"])

    def test_custom_integrated_agents_is_preserved_and_templates_are_installed(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            agents = target / "AGENTS.md"
            custom = f"# Local rules\n\n{MARKER}\n{DIRECTIVE}\nLocal policy remains.\n"
            agents.write_text(custom)
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 0)
            self.assertIn("1 already present", result.stdout)
            self.assertEqual(agents.read_text(), custom)
            self.assertTrue((target / "docs/project/briefing/index.md").is_file())
            self.assertFalse((target / "index.md").exists())

    def test_negative_agents_mention_requires_manual_integration(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "AGENTS.md").write_text("Do not use using-ariad.\n")
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 3)
            self.assertIn(MARKER, result.stderr)
            self.assertEqual([p.name for p in target.iterdir()], ["AGENTS.md"])

    def test_marker_without_standalone_directive_requires_manual_integration(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "AGENTS.md").write_text(f"{MARKER}\nUse {DIRECTIVE} when possible.\n")
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 3)
            self.assertFalse((target / "docs").exists())

    def test_dangling_destination_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            target = Path(tmp); external = Path(outside) / "absent.md"
            (target / "AGENTS.md").symlink_to(external)
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 4)
            self.assertFalse(external.exists())
            self.assertTrue((target / "AGENTS.md").is_symlink())

    def test_existing_nested_symlink_parent_stops_all_writes(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            target = Path(tmp)
            (target / "docs").symlink_to(Path(outside), target_is_directory=True)
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 4)
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_exclusive_helper_does_not_truncate(self):
        spec = importlib.util.spec_from_file_location("adopt", ADOPT)
        module = importlib.util.module_from_spec(spec)
        previous = sys.dont_write_bytecode
        try:
            sys.dont_write_bytecode = True
            spec.loader.exec_module(module)
        finally:
            sys.dont_write_bytecode = previous
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "existing"
            destination.write_bytes(b"original")
            with self.assertRaises(FileExistsError):
                module.create_exclusive(destination, b"replacement")
            self.assertEqual(destination.read_bytes(), b"original")

    def test_nested_collision_stops_all_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp); collision = target / "docs/project/roadmap/index.md"
            collision.parent.mkdir(parents=True); collision.write_text("different\n")
            result = self.run_adopt(target, True)
            self.assertEqual(result.returncode, 4)
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertEqual(collision.read_text(), "different\n")

    def test_manual_skill_path_is_readable(self):
        skill = ROOT / "skills/using-ariad/SKILL.md"
        self.assertIn("name: using-ariad", skill.read_text())

if __name__ == "__main__":
    unittest.main()
