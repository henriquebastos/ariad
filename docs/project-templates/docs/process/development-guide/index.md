# Local Development Guide

This directory is the project-specific operating contract for agentic development.

Ariad is the canonical method. These focused documents are the local instance of that method for this repository. When Ariad and this guide differ, follow the local rule for project work and surface the difference during the coherence check.

The agent is the **Driver**: it reads context, proposes plans, changes files, runs checks, prepares validation routes, updates documentation, and stops at checkpoints. The human is the **Navigator** and holds intent, trade-offs, product judgment, and acceptance.

## How to Read This Guide

Read this index first, then only the documents relevant to the current work:

- [Commands and verification](commands-and-verification.md) — setup, execution, automated checks, and acceptance evidence.
- [Documentation and project memory](documentation-and-memory.md) — documentation responsibilities and conflict-resistant records.
- [Workflow and checkpoints](workflow-and-checkpoints.md) — roadmap taxonomy, lifecycle, debt review, and confirmation boundaries.
- [Navigator preferences](navigator-preferences.md) — explicit local choices about how work is conducted.
- [Release and history](release-and-history.md) — branches, commits, pushes, pull requests, versions, and releases.
- [Local exceptions](local-exceptions.md) — deliberate deviations from Ariad or normal engineering practice.

Keep current truth in the focused document that owns it. Record rationale for consequential changes in `docs/project/decisions/records/`; rely on Git for ordinary textual history. Do not append policy history here or create version-suffixed policy files.
