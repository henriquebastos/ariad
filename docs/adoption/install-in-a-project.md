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
cp docs/project-templates/docs/project/briefing.md /path/to/project/docs/project/briefing.md
cp docs/project-templates/docs/project/decisions/index.md /path/to/project/docs/project/decisions/index.md
cp docs/project-templates/docs/project/exploration/index.md /path/to/project/docs/project/exploration/index.md
cp docs/project-templates/docs/project/roadmap/index.md /path/to/project/docs/project/roadmap/index.md
cp docs/project-templates/docs/project/debt/index.md /path/to/project/docs/project/debt/index.md
cp docs/project-templates/docs/process/development-guide.md /path/to/project/docs/process/development-guide.md
cp docs/project-templates/docs/process/worklog/index.md /path/to/project/docs/process/worklog/index.md
cp docs/project-templates/docs/product/principles.md /path/to/project/docs/product/principles.md
touch /path/to/project/docs/project/decisions/records/.gitkeep \
  /path/to/project/docs/project/debt/items/.gitkeep \
  /path/to/project/docs/process/worklog/entries/.gitkeep
```

## Adapt the Project Context

Start with the smallest useful version.

You can fill the templates manually, but the recommended pilot flow is agent-assisted. Use [Agent-Assisted Initialization](agent-assisted-initialization.md) to ask the Driver to inspect the project and draft the first version for Navigator review.

In `docs/project/briefing.md`, capture what the project is, where it is now, what constraints matter, and how work should be validated.

In `docs/product/principles.md`, capture what the product should preserve when trade-offs appear.

In `docs/project/roadmap/index.md`, keep the roadmap structure and state conventions clear. Put active or planned roadmap work in its own item files or folders with explicit `status` metadata instead of turning the index into a central ledger.

In `docs/process/development-guide.md`, capture the local operating contract: commands, validation rules, documentation expectations, release habits, and any project-specific exceptions to Ariad.

Leave the artifact directories mostly empty if there are no decisions, debt items, or milestones yet:

- `docs/project/decisions/records/`
- `docs/project/debt/items/`
- `docs/process/worklog/entries/`

The index files should remain present because they explain naming, status, and templates.

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
