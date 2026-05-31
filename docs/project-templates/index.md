# Project Templates

These templates are copied into a project that wants to use Ariad.

They are intentionally small. The method should become operational before it becomes elaborate.

The most important file is `AGENTS.md`. It is the operational doorway for coding agents. It tells the agent that the project uses Ariad, which local docs to read, and how to preserve coherence during work.

Ariad works as a canonical method plus a local instance:

- **Ariad canonical method**: the general method maintained in this repository.
- **Local Ariad instance**: the project-specific docs copied or adapted into the target project.
- **Local development guide**: `docs/process/development-guide.md`, the project-specific operating contract.
- **AGENTS.md**: the agent-facing entry point that connects the canonical method to the local project docs.

The canonical Ariad docs are not vendored into target projects during manual adoption. Target projects receive a local instance of the method. The future Mirror extension will own canonical source discovery, version awareness, updates, and canonical context injection when needed.

The documentation templates create the minimum memory surface required for coherent work:

- **Project briefing**: stable project context that should not be re-explained every session.
- **Decisions**: choices and open discussions that should shape future work.
- **Roadmap**: meaningful progress, active focus, planned work, and radar.
- **Technical Debt Ledger**: structural cost consciously carried by the project, with revisit triggers.
- **Local development guide**: project-specific commands, validation, documentation, and release rules.
- **Worklog**: completed milestones and verification notes.
- **Product principles**: product behavior guidance that should influence trade-offs.

Copy the templates, then adapt them. Do not try to perfect every section before the first agent session. A useful first draft is better than an empty method.
