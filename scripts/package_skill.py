#!/usr/bin/env python3
"""Build and verify the self-contained using-ariad Agent Skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/using-ariad"
VERSION = "0.1.0"
SOURCE = "https://github.com/mirror-mind-ai/ariad"
SIZE_BUDGET = 750_000

# Method authority is intentionally explicit. Adding a canonical page requires review here.
REFERENCE_SOURCES = (
    "docs/method/index.md", "docs/method/overview.md", "docs/method/work-areas.md",
    "docs/method/expand-collapse.md", "docs/method/driver-navigator.md",
    "docs/method/triad.md", "docs/method/contracts-and-preferences.md",
    "docs/method/explicit-policies.md", "docs/method/methodological-roots.md",
    "docs/exploration/index.md", "docs/exploration/conceptual-model.md",
    "docs/exploration/flow.md", "docs/exploration/visual-grammar.md",
    "docs/delivery/index.md", "docs/delivery/roadmap-taxonomy.md",
    "docs/delivery/conceptual-model.md", "docs/delivery/flow.md",
    "docs/delivery/visual-grammar.md", "docs/delivery/cadences.md",
    "docs/delivery/release-management.md", "docs/delivery/story-lifecycle.md",
    "docs/delivery/checkpoints.md", "docs/refinement/index.md",
    "docs/refinement/conceptual-model.md", "docs/refinement/flow.md",
)

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def digest_payload(payload: dict[str, bytes]) -> str:
    """Hash package-relative destination names and bytes, excluding the manifest."""
    return sha(b"".join(
        path.encode() + b"\0" + payload[path] + b"\0"
        for path in sorted(payload) if path != "manifest.json"
    ))

def expected_inventory(generated: set[str]) -> set[str]:
    return generated | {"SKILL.md", "scripts/adopt.py"}

def source_map() -> dict[str, str]:
    result = {p: f"references/{p.removeprefix('docs/')}" for p in REFERENCE_SOURCES}
    for path in sorted((ROOT / "docs/project-templates").rglob("*")):
        # This is the documentation-site overview, not a file installed in projects.
        if path.is_file() and path != ROOT / "docs/project-templates/index.md":
            rel = path.relative_to(ROOT).as_posix()
            result[rel] = "assets/project-templates/" + path.relative_to(ROOT / "docs/project-templates").as_posix()
    result["LICENSE"] = "LICENSE.txt"
    return result

def expected_generated() -> tuple[dict[str, bytes], str]:
    mapping = source_map()
    output = {dest: (ROOT / src).read_bytes() for src, dest in mapping.items()}
    method_digest = sha(b"".join(
        src.encode() + b"\0" + (ROOT / src).read_bytes() + b"\0"
        for src in REFERENCE_SOURCES
    ))
    payload = dict(output)
    payload["SKILL.md"] = (PACKAGE / "SKILL.md").read_bytes()
    payload["scripts/adopt.py"] = (PACKAGE / "scripts/adopt.py").read_bytes()
    entries = [
        {"source": src, "destination": dest, "sha256": sha(output[dest])}
        for src, dest in sorted(mapping.items())
    ]
    entries.extend(
        {"source": "authored:" + dest, "destination": dest, "sha256": sha(payload[dest])}
        for dest in ("SKILL.md", "scripts/adopt.py")
    )
    manifest = {
        "format_version": "1",
        "package": "using-ariad",
        "package_version": VERSION,
        "source": SOURCE,
        "method_digest": method_digest,
        "package_digest": digest_payload(payload),
        "files": entries,
    }
    output["manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    return output, method_digest

def package_files() -> set[str]:
    return {p.relative_to(PACKAGE).as_posix() for p in PACKAGE.rglob("*") if p.is_file()}

def heading_ids(text: str) -> set[str]:
    ids: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            value = re.sub(r"[^\w\- ]", "", match.group(1).lower(), flags=re.UNICODE)
            ids.add(re.sub(r"[\s\-]+", "-", value).strip("-"))
    return ids

def check_links(errors: list[str]) -> None:
    link_re = re.compile(r"(?<!!)\[[^]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
    for path in sorted((PACKAGE / "references").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw in link_re.findall(text):
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc or raw.startswith(("mailto:", "/")):
                continue
            target = path if not parts.path else (path.parent / unquote(parts.path)).resolve()
            try:
                target.relative_to(PACKAGE / "references")
            except ValueError:
                errors.append(f"link escapes references: {path.relative_to(PACKAGE)} -> {raw}")
                continue
            if not target.is_file():
                errors.append(f"missing link target: {path.relative_to(PACKAGE)} -> {raw}")
            elif parts.fragment and target.suffix == ".md":
                if unquote(parts.fragment) not in heading_ids(target.read_text(encoding="utf-8")):
                    errors.append(f"missing fragment: {path.relative_to(PACKAGE)} -> {raw}")

def check_authored(method_digest: str, errors: list[str]) -> None:
    skill = (PACKAGE / "SKILL.md").read_text(encoding="utf-8") if (PACKAGE / "SKILL.md").is_file() else ""
    required = ("name: using-ariad", "license: MIT", f'version: "{VERSION}"',
                f'source: "{SOURCE}"', f'method-digest: "sha256:{method_digest}"')
    for value in required:
        if value not in skill:
            errors.append(f"SKILL.md missing or inconsistent metadata: {value}")
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    if not re.search(r'^version = "' + re.escape(VERSION) + r'"$', pyproject, re.MULTILINE):
        errors.append("package version does not match pyproject.toml")
    if not (PACKAGE / "scripts/adopt.py").is_file():
        errors.append("missing authored adopter scripts/adopt.py")

def check() -> int:
    expected, digest = expected_generated()
    errors: list[str] = []
    actual = package_files()
    allowed = expected_inventory(set(expected))
    if actual != allowed:
        for path in sorted(allowed - actual): errors.append(f"missing package file: {path}")
        for path in sorted(actual - allowed): errors.append(f"unexpected package file: {path}")
    for rel, data in expected.items():
        path = PACKAGE / rel
        if path.is_file() and path.read_bytes() != data:
            errors.append(f"generated bytes differ: {rel}")
    check_authored(digest, errors)
    check_links(errors)
    total = sum(p.stat().st_size for p in PACKAGE.rglob("*") if p.is_file())
    if total > SIZE_BUDGET:
        errors.append(f"package size {total} exceeds budget {SIZE_BUDGET}")
    if errors:
        print("Skill package check failed:\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1
    print(f"Skill package is current ({len(expected)} generated files, {total} bytes, sha256:{digest}).")
    return 0

def generate() -> None:
    expected, _ = expected_generated()
    for name in ("references", "assets"):
        shutil.rmtree(PACKAGE / name, ignore_errors=True)
    for name in ("LICENSE.txt", "manifest.json"):
        (PACKAGE / name).unlink(missing_ok=True)
    for rel, data in expected.items():
        path = PACKAGE / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify without writing")
    args = parser.parse_args()
    if not args.check:
        generate()
    return check()

if __name__ == "__main__":
    raise SystemExit(main())
