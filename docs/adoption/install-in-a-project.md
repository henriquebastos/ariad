# Install in a Project

Keep three operations distinct: **first adoption** installs missing templates without overwriting files; **skill replacement** updates the complete vendored package but not project docs; **manual template migration** reconciles older or locally adapted docs with human review.

## First adoption: install the method package

Copy a released `skills/using-ariad/` directory intact into a project-local skill location supported by your runtime:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R /path/to/ariad/skills/using-ariad /path/to/project/.agents/skills/
```

`.agents/skills/` is conventional, not universal. Runtime-native installation is valid, or open `using-ariad/SKILL.md` manually. Record the package version and manifest `package_digest` to pin the complete snapshot; `method_digest` identifies canonical reference inputs only.

Preview, then explicitly apply template adoption:

```bash
python /path/to/project/.agents/skills/using-ariad/scripts/adopt.py /path/to/project
python /path/to/project/.agents/skills/using-ariad/scripts/adopt.py /path/to/project --apply
```

The adopter preflights every destination before normal writes. Exact files and a custom `AGENTS.md` containing the exact marker `<!-- ariad-skill: using-ariad -->` count as present. The custom file must also positively instruct agents to read the installed `using-ariad/SKILL.md`; a mere mention does not integrate it. An unmarked `AGENTS.md` returns a distinct manual-integration result and a ready-to-copy snippet. Any other differing destination or destination/parent symlink stops all writes. Creation is exclusive and never truncates or merges. This is cooperative local-CLI collision safety, not a guarantee against hostile concurrent filesystem races. If it cannot run, copy from `assets/project-templates/` with the same relative paths and no-overwrite rule.

## Adapt the modular project context

Use [Agent-Assisted Initialization](agent-assisted-initialization.md) or edit manually. Start with the smallest useful truth:

- Read `docs/project/briefing/index.md`, then capture identity and purpose, current state, and constraints in their focused documents.
- Read `docs/product/principles/index.md`, then put principles that should govern trade-offs in `current-principles.md`.
- Keep roadmap structure and state conventions in `docs/project/roadmap/index.md`; put active or planned work in separate items with explicit `status` metadata rather than making the index a ledger.
- Read `docs/process/development-guide/index.md`, then capture current commands and verification, documentation and memory, workflow and checkpoints, Navigator preferences, release and history, and local exceptions in the focused policy documents.

Decision records, debt items, and worklog entries may remain empty until real material exists. Keep their indexes because those explain naming, status, and templates. Preserve consequential rationale in decision records; use Git, not policy-history sections, for ordinary history.

## Skill replacement

Replace the installed `using-ariad` directory only as one complete, versioned package and verify its manifest. Review release differences first. Replacement updates packaged references, scripts, and pristine assets; it does **not** migrate or reconcile the target project's adapted files.

## Manual template migration

For former monolithic templates, start with a clean worktree and retain temporary in-repository migration sources:

```bash
cd /path/to/project
mkdir -p docs/process/development-guide docs/project/briefing docs/product/principles
git mv docs/process/development-guide.md docs/process/development-guide/migration-source.md
git mv docs/project/briefing.md docs/project/briefing/migration-source.md
git mv docs/product/principles.md docs/product/principles/migration-source.md

cp -n /path/to/ariad/docs/project-templates/docs/process/development-guide/*.md docs/process/development-guide/
cp -n /path/to/ariad/docs/project-templates/docs/project/briefing/*.md docs/project/briefing/
cp -n /path/to/ariad/docs/project-templates/docs/product/principles/*.md docs/product/principles/
```

Move every real current premise, rule, and principle from the three `migration-source.md` files into the focused documents that now own it. Compare and retain local rules instead of replacing them with defaults. Preserve consequential rationale in decision records, update `AGENTS.md` and local links to each directory's `index.md`, then delete the migration sources. Review `git diff` before committing to confirm no local knowledge was lost. The adopter intentionally does not perform this judgment-heavy migration.

## Run one small change

Adoption becomes real only when used. Choose a change small enough to complete but real enough to exercise planning, implementation, validation, documentation, review, and the local commit policy.
