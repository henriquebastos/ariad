# Project Templates

These templates are copied into a project that wants to use Ariad.

They are intentionally small. The method should become operational before it becomes elaborate.

`AGENTS.md` remains project-owned and provides a minimal, stable route to `docs/ariad/index.md`. The Ariad router then loads the installed skill and progressively directs agents into local project context.

Ariad works as a canonical method plus a local instance:

- **Ariad canonical method**: the general method maintained in this repository.
- **Local Ariad instance**: the project-specific docs copied or adapted into the target project.
- **Local development guide**: `docs/process/development-guide/index.md` and its focused current-policy documents, the project-specific operating contract.
- **AGENTS.md**: the project-owned entry point that routes to `docs/ariad/index.md` without embedding the whole method contract.
- **Ariad router**: the stable bridge between the installed skill and project-owned documentation.

The installed skill contains a pinned snapshot of canonical Ariad docs. Project templates are adopted separately and become project-owned adaptations. Agents install and upgrade these surfaces under Navigator review; optional runtime extensions may add convenience without becoming Ariad's authority.

The documentation templates create the minimum memory surface required for coherent work:

- **Project briefing**: focused current project context under `docs/project/briefing/` that should not be re-explained every session.
- **Decisions**: one decision record per file in `docs/project/decisions/records/`, with `status` distinguishing open, decided, superseded, and dropped records.
- **Roadmap**: meaningful progress as item files or folders whose own metadata carries lifecycle state.
- **Technical Debt Ledger**: structural cost consciously carried by the project, stored as one debt item per file in `docs/project/debt/items/`, with revisit triggers and closure conditions.
- **Local development guide**: focused project-specific commands, validation, workflow, documentation, preferences, exceptions, and release rules.
- **Worklog**: one milestone entry per file in `docs/process/worklog/entries/`.
- **Product principles**: bounded current product behavior guidance under `docs/product/principles/` that should influence trade-offs.

Index files explain structure, naming, and templates. They should not become central mutable lists unless a project explicitly accepts that coordination cost.

Copy the templates, then adapt them. Do not try to perfect every section before the first agent session. A useful first draft is better than an empty method.
