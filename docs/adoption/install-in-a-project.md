# Install in a Project

The standard installation flow is performed by an agent under Navigator review. Start from an exact Ariad checkout, tag, commit, or release selected by the Navigator; never infer “latest.”

Installation has two distinct operations:

1. Install the runtime-independent `using-ariad` skill as a pinned snapshot.
2. Adopt and adapt project templates as project-owned documentation.

The detailed agent contract lives at `skills/using-ariad/INSTALL.md` in the selected Ariad source and is copied alongside the installed skill. The Navigator chooses the source and reviews integration; the Driver inspects, copies, adapts, and verifies.

## Install the Skill

The Driver first inspects existing instructions, documentation, and installed skills. It identifies the runtime's supported project-local skill location and previews all destinations. If the destination `using-ariad` directory already exists, it stops for Navigator direction rather than copying into it; updating or replacing a complete snapshot is a separate operation. It must not partially replace an existing skill or overwrite project-owned files.

From the selected Ariad source, it creates the `using-ariad` skill directory and copies the authored `SKILL.md` and `INSTALL.md`, the repository `LICENSE`, and the complete canonical `docs/` tree as `references/`, preserving its structure.

Canonical material has one maintained copy under `docs/` in this repository. The installed `references/` directory is a deliberate consumer snapshot: it keeps the selected method revision self-contained, pinned, and available without runtime downloads. Record the actual source repository and resolved commit or immutable release identifier in the target project's chosen dependency or decision history.

## Adopt the Templates

The Driver then inspects `references/project-templates/` against the target project. It proposes the smallest useful set of files, copies only absent files that fit, and integrates Ariad routing into existing agent instructions rather than replacing them.

When a destination already exists, preserve it. The Driver should explain the difference and propose a semantic reconciliation for Navigator review instead of applying a generic merge. Adopted documents become project-owned adaptations; they are not package files to overwrite during a later skill update.

## Adapt the Project Context

Start with the smallest useful version.

Use [Agent-Assisted Initialization](agent-assisted-initialization.md) to ask the Driver to inspect the project and draft the first version for Navigator review.

Read `docs/project/briefing/index.md`, then capture identity and purpose, current state, and constraints or environment in their focused documents.

Read `docs/product/principles/index.md`, then capture what the product should preserve when trade-offs appear in `current-principles.md`.

In `docs/project/roadmap/index.md`, keep the roadmap structure and state conventions clear. Put active or planned roadmap work in its own item files or folders with explicit `status` metadata instead of turning the index into a central ledger.

Read `docs/process/development-guide/index.md`, then capture the local operating contract in the focused current-policy documents for commands and verification, documentation and memory, workflow and checkpoints, Navigator preferences, release and history, and local exceptions.

Leave the artifact directories mostly empty if there are no decisions, debt items, or milestones yet:

- `docs/project/decisions/records/`
- `docs/project/debt/items/`
- `docs/process/worklog/entries/`

The index files should remain present because they explain naming, status, and templates.

## Migrate an Existing Local Instance

If a project already has the former single-file templates, preserve their content while moving to the directory structure. Start from a clean worktree and use temporary in-repository migration files so nothing is lost between commands:

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

Move each project's real current content from the three `migration-source.md` files into the focused documents that now own it. Preserve consequential rationale in decision records, not in policy-history sections; rely on Git for ordinary history. Compare and retain local rules rather than replacing them with template defaults. Update `AGENTS.md` and any project-local links to point to each directory's `index.md`, then delete the three migration-source files before committing. Review `git diff` to confirm every local premise, rule, and principle has a current home.

## Verify the Installation

Before acceptance, the Driver shows the resulting diff and verifies that:

- the runtime can discover the skill or its manual-loading fallback is documented;
- `SKILL.md` routes to the installed `references/` snapshot;
- existing project instructions and files were preserved;
- copied templates describe real project truth or clearly mark Navigator questions;
- the selected Ariad source and revision are recorded.

## Optional: Connect Mirror Builder Mode

When Mirror is the selected runtime, create or choose the journey that represents this project, then set its project path:

```bash
uv run python -m memory journey set-path <journey-slug> /path/to/project
```

Start Builder Mode from the journey:

```text
/mm-build <journey-slug>
```

## Run One Small Change

Adoption becomes real only when the method is used.

Pick a small change that can move through the full lifecycle: plan, implementation, validation, documentation, review, and commit. The change should be small enough to finish, but real enough to test whether the agent actually follows the method.

The goal is not to fill every section perfectly. The goal is to give the agent enough context to stop starting from zero.
