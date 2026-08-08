---
name: upgrading-ariad
description: Audit and plan an upgrade of an Ariad-adopted project against an explicitly selected Ariad checkout or ref, without changing the target project.
license: MIT
metadata:
  version: "0.1.1"
---

# Upgrading Ariad

This is an operational specialization of Ariad, not a second method. The target version is the Ariad checkout/ref containing this skill: never assume remote `main`, “latest,” or fetch automatically.

Run `python scripts/audit.py /path/to/project --candidate /path/to/this/ariad/checkout --skill-destination .agents/skills/using-ariad` first. Use repeatable `--installed-package TARGET_RELATIVE_PATH` for runtime-native existing locations and choose a different safe target-relative `--skill-destination` when appropriate. Report mode makes no changes. It maps legacy references across project text, inventories harness support, records semantic Ariad evidence, and summarizes project-memory status vocabulary and possible intentional absences. Review the concise evidence and classify every proposed operation as **safe additive**, **manual integration**, **destructive/ambiguous denied**, or **retain unchanged**. Present a plan and checkpoint before action.

Project-owned instructions, memory, statuses, and adaptations are not package drift. Semantic migration requires Driver investigation and Navigator judgment. Never overwrite a root or nested `AGENTS.md`, old monolith, history, or custom memory; never partially edit an installed skill. Package replacement and local-document migration are separate, deliberate operations.
