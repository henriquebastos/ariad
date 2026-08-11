---
name: upgrading-ariad
description: Audits and plans an upgrade of an Ariad-adopted project against an explicitly selected Ariad source. Use when replacing an installed Ariad skill or migrating project-owned Ariad documents.
license: MIT
---

# Upgrading Ariad

Treat the Ariad checkout or immutable release containing this skill as the candidate. Never infer “latest,” fetch another version automatically, or mutate the target while auditing it.

## Inspect

Read the target project's instructions and Ariad router, then identify:

- repository, branch, HEAD, and staged, unstaged, and untracked changes;
- the installed `using-ariad` location and any recorded source revision;
- the candidate repository, resolved commit or immutable release identifier, and staged, unstaged, and untracked state;
- candidate `skills/using-ariad/SKILL.md`, `INSTALL.md`, `LICENSE`, and canonical `docs/`;
- project-owned Ariad documents, local adaptations, legacy paths, and instruction scopes;
- symlinks, collisions, or runtime-specific installation constraints.

Do not follow links or symlinks outside the target or candidate roots when inventorying files. Do not treat project-owned adaptations as package drift.

## Compare and Classify

Compare the complete installed skill snapshot with the complete candidate snapshot that installation would materialize. Separately compare candidate project templates with project-owned documents semantically; template differences do not authorize replacement.

Classify every proposed operation as one of:

- **safe additive** — creates an absent path without changing project-owned content;
- **manual integration** — requires reconciling canonical guidance with local truth;
- **whole-snapshot replacement — blocked pending explicit Navigator approval** — replaces one verified installed package snapshot with another while preserving package/project ownership boundaries;
- **destructive or ambiguous — denied** — would overwrite, partially replace, follow an unsafe path, or discard intent;
- **retain unchanged** — local content already owns the intended behavior or deliberately differs.

Report evidence, uncertainty, and a proposed sequence. Stop for Navigator approval before writing.

## Apply Only the Approved Plan

Before applying, verify that the candidate identity and dirty state still match the audited candidate. Replace an installed `using-ariad` skill only as one complete snapshot from that selected candidate. Stage it outside the destination, verify required files and references, then replace the old skill as a single approved operation. Never merge package files in place or leave content from two revisions.

Migrate project-owned documents separately. Preserve local facts, decisions, policies, history, and adaptations; use the candidate templates as guidance rather than replacement content. Update the project-owned provenance record with the actual installed path, candidate repository, and resolved commit or immutable release identifier as a separately approved semantic edit. Show the resulting diff and re-run project and documentation verification before asking the Navigator to accept the upgrade.
