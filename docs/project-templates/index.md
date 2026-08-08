# Project Templates

These templates are copied into a project that wants to use Ariad.

They are intentionally small. The method should become operational before it becomes elaborate.

`AGENTS.md` is the operational doorway, but Ariad integrates with it and does not own it. The minimal template carries an exact marker, standalone `@docs/ariad/index.md`, and a direct-read fallback for runtimes that do not expand `@path`. The local router owns Ariad orientation while project instructions remain project-owned.

Ariad works as a canonical method plus a local instance:

- **Ariad canonical method**: the general method maintained in this repository.
- **Local Ariad instance**: the project-specific docs copied or adapted into the target project.
- **Local development guide**: `docs/process/development-guide/index.md` and its focused current-policy documents, the project-specific operating contract.
- **AGENTS.md**: a stable pointer in project-owned agent instructions.
- **docs/ariad/index.md**: the thin router connecting the canonical method to local project docs.

The `using-ariad` Agent Skill is the self-contained, portable method package. Install a vendored snapshot in a runtime-supported project-local skill directory; `.agents/skills/using-ariad/` is conventional but not universal. Mirror and Maestro are optional consumers of the same package.

The documentation templates create the minimum memory surface required for coherent work:

- **Project briefing**: focused current project context under `docs/project/briefing/` that should not be re-explained every session.
- **Decisions**: one decision record per file in `docs/project/decisions/records/`, with `status` distinguishing open, decided, superseded, and dropped records.
- **Roadmap**: meaningful progress as item files or folders whose own metadata carries lifecycle state.
- **Technical Debt Ledger**: structural cost consciously carried by the project, stored as one debt item per file in `docs/project/debt/items/`, with revisit triggers and closure conditions.
- **Local development guide**: focused project-specific commands, validation, workflow, documentation, preferences, exceptions, and release rules.
- **Worklog**: one milestone entry per file in `docs/process/worklog/entries/`.
- **Product principles**: bounded current product behavior guidance under `docs/product/principles/` that should influence trade-offs.

Index files explain local structure, naming, and templates. Untouched local method-policy slots inherit the installed skill's current canonical guidance instead of freezing a copy of old defaults. They should not become central mutable lists unless a project explicitly accepts that coordination cost.

Copy the templates, then adapt them. Do not try to perfect every section before the first agent session. A useful first draft is better than an empty method.
