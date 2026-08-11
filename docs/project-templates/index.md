# Project Templates

These templates are copied into a project that wants to use Ariad.

They are intentionally small. The method should become operational before it becomes elaborate.

The most important file is `AGENTS.md`. It is the operational doorway for coding agents. It tells the agent that the project uses Ariad, which local docs to read, and how to preserve coherence during work.

Ariad works as a canonical method plus a local instance:

- **Ariad canonical method**: the general method maintained in this repository.
- **Local Ariad instance**: the project-specific docs copied or adapted into the target project.
- **Local development guide**: `docs/process/development-guide/index.md` and its focused current-policy documents, the project-specific operating contract.
- **AGENTS.md**: the agent-facing entry point that connects the canonical method to the local project docs.

The canonical Ariad docs are not vendored into target projects during manual adoption. Target projects receive a local instance of the method. The future Mirror extension will own canonical source discovery, version awareness, updates, and canonical context injection when needed.

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
