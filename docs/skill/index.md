# The `using-ariad` Agent Skill

`skills/using-ariad/` is Ariad's standard, self-contained distribution. Agent Skills is the portable package format; Ariad itself is runtime-independent. The package contains a thin activation guide, generated canonical method references, project-template assets, a safe adopter, an MIT license, and a deterministic manifest.

Canonical human documentation under `docs/` remains the sole editable method authority. Maintainers run `python scripts/package_skill.py` to regenerate the package and `python scripts/package_skill.py --check` to detect drift. Generated references and assets must not be edited directly.

## Install in a project

Copy a released `skills/using-ariad/` directory, intact, into a skill directory supported by the target runtime. `.agents/skills/using-ariad/` is a preferred conventional project-local location, not a universal one. A runtime-native installer may place the same package elsewhere. If automatic discovery is unavailable, read its `SKILL.md` manually.

Treat the installed directory as a vendored snapshot. Pin it by release/package version and `manifest.json` package digest. The **method digest** identifies only canonical method-reference inputs; the **package digest** identifies every packaged payload path and byte except the manifest itself. Manifest file entries include authored `SKILL.md` and `scripts/adopt.py` as well as generated references, assets, and license. No generic automatic update mechanism is implied.

The package records repository-relative source paths rather than a fixed GitHub repository. The same package can therefore be built and distributed from upstream or a fork without changing its bytes. Record the actual repository URL and Git revision used to obtain a snapshot in the adopting project's dependency or decision history.

Replacing the skill snapshot and migrating already-adapted local templates are separate operations. Replace the package deliberately after reviewing release metadata. Do not automatically overwrite, merge, or migrate local project documentation.

## Adopt templates

From the installed skill, preview template adoption:

```bash
python path/to/using-ariad/scripts/adopt.py /path/to/project
```

Apply only after reviewing the plan:

```bash
python path/to/using-ariad/scripts/adopt.py /path/to/project --apply
```

The adopter preflights every destination and never overwrites or merges. It rejects destination and parent symlinks, rechecks before creation, and uses exclusive file creation. This is cooperative local-CLI race hardening and does not protect against hostile concurrent ancestor swaps. Existing project-owned `AGENTS.md` is integrated only when it contains exact standalone `<!-- ariad-entrypoint: docs/ariad/index.md -->` and `@docs/ariad/index.md` lines; otherwise it returns a ready-to-copy block without writing. Ariad integrates with this file but does not own it. Because `@path` is not universal, preserve the direct-read fallback. This installs templates only—it does not migrate or update the installed skill. See [Upgrading Ariad](upgrading.md) for report-only inventory.
