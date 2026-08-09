from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/package_skill.py"
SPEC = importlib.util.spec_from_file_location("package_skill", SCRIPT)
PACKAGE_SKILL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE_SKILL)


class PackageSkillTests(unittest.TestCase):
    def test_digest_is_deterministic_and_path_sensitive(self):
        first = PACKAGE_SKILL.digest_payload({"b": b"two", "a": b"one"})
        self.assertEqual(first, PACKAGE_SKILL.digest_payload({"a": b"one", "b": b"two"}))
        self.assertNotEqual(first, PACKAGE_SKILL.digest_payload({"a": b"two", "b": b"one"}))

    def test_closed_inventory_includes_authored_and_rejects_arbitrary_payload(self):
        allowed = PACKAGE_SKILL.expected_inventory({"manifest.json", "LICENSE.txt"})
        self.assertIn("SKILL.md", allowed)
        self.assertIn("scripts/adopt.py", allowed)
        self.assertNotIn("scripts/extra.py", allowed)

    def test_manifest_represents_authored_payload(self):
        generated, _ = PACKAGE_SKILL.expected_generated()
        manifest = __import__("json").loads(generated["manifest.json"])
        destinations = {entry["destination"] for entry in manifest["files"]}
        self.assertIn("SKILL.md", destinations)
        self.assertIn("scripts/adopt.py", destinations)
        self.assertIn("package_digest", manifest)
        self.assertEqual(manifest["source_path"], "skills/using-ariad")
        self.assertNotIn("source", manifest)

    def test_memory_closure_is_canonical_packaged_and_routed(self):
        generated, _ = PACKAGE_SKILL.expected_generated()
        destination = "references/method/memory-closure.md"
        self.assertIn(destination, generated)
        source = (ROOT / "docs/method/memory-closure.md").read_bytes()
        self.assertEqual(generated[destination], source)
        skill = (ROOT / "skills/using-ariad/SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"]({destination})", skill)
        text = source.decode()
        for heading in ("## Triggers", "## Promotion Test", "## Protocol", "## Context-Release Condition", "## Progressive Resume", "## Anti-Bloat Invariants"):
            self.assertIn(heading, text)
        self.assertIn("Do not create a second closure ceremony", text)
        self.assertIn("absent push authorization never prevents an otherwise authorized local commit", text)
        self.assertIn("Never treat an uncommitted working tree as transferable long-term memory", text)


if __name__ == "__main__":
    unittest.main()
