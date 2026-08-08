# Install in a Project

This is the manual pilot installation flow.

The reference installation path assumes Mirror Mind Builder Mode as the runtime. The target project receives a local Ariad instance, and a Mirror journey points Builder Mode to that project.

Manual adoption does not vendor the full canonical Ariad documentation into the target project. The canonical source remains the Ariad repository. The project receives local operating docs that tell agents how to work in that project.

Manual installation is intentional at this stage. It makes the method visible, keeps the project owner involved in the initial framing, and avoids hiding adoption behind tooling before the method has been tested in enough real contexts.

## Copy the Templates

From the method repository, copy the templates into the target project.

```bash
cp docs/project-templates/AGENTS.md /path/to/project/AGENTS.md
mkdir -p /path/to/project/docs/project/roadmap \
  /path/to/project/docs/project/decisions/records \
  /path/to/project/docs/project/exploration \
  /path/to/project/docs/project/debt/items \
  /path/to/project/docs/process/worklog/entries \
  /path/to/project/docs/product
cp -R docs/project-templates/docs/project/briefing /path/to/project/docs/project/
cp docs/project-templates/docs/project/decisions/index.md /path/to/project/docs/project/decisions/index.md
cp docs/project-templates/docs/project/exploration/index.md /path/to/project/docs/project/exploration/index.md
cp docs/project-templates/docs/project/roadmap/index.md /path/to/project/docs/project/roadmap/index.md
cp docs/project-templates/docs/project/debt/index.md /path/to/project/docs/project/debt/index.md
cp -R docs/project-templates/docs/process/development-guide /path/to/project/docs/process/
cp docs/project-templates/docs/process/worklog/index.md /path/to/project/docs/process/worklog/index.md
cp -R docs/project-templates/docs/product/principles /path/to/project/docs/product/
touch /path/to/project/docs/project/decisions/records/.gitkeep \
  /path/to/project/docs/project/debt/items/.gitkeep \
  /path/to/project/docs/process/worklog/entries/.gitkeep
```

## Adapt the Project Context

Start with the smallest useful version.

You can fill the templates manually, but the recommended pilot flow is agent-assisted. Use [Agent-Assisted Initialization](agent-assisted-initialization.md) to ask the Driver to inspect the project and draft the first version for Navigator review.

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

## Connect Mirror Builder Mode

Create or choose the Mirror journey that represents this project, then set its project path:

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
