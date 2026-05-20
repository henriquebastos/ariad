# Agent-Assisted Initialization

Manual template filling can become adoption friction.

Ariad assumes the project is being prepared inside an agentic environment. The Navigator should not need to fill every document from a blank page. The Driver can inspect the project, draft the initial documentation, and ask the Navigator to review and correct it.

This keeps adoption aligned with the method: the agent drives the repository work; the human navigates meaning, trade-offs, and acceptance.

## When to Use

Use agent-assisted initialization after copying the Ariad project templates into a repository and before the first meaningful Builder Mode cycle.

It works for existing projects and for new projects that already have enough context to describe purpose, product direction, and first work.

## Initialization Prompt

Use this prompt with the coding agent inside the target project:

```text
This project uses Ariad.

Act as the Driver. I am the Navigator.

Inspect this repository and draft the initial Ariad project documentation. Read the files that exist, especially README, package or project metadata, existing docs, tests, and any agent instruction files.

Do not overwrite files without showing me the proposed content first.

Prepare drafts for:

- docs/project/briefing.md
- docs/product/principles.md
- docs/project/roadmap/index.md
- docs/process/development-guide.md
- docs/project/decisions.md, only if you find real decisions worth preserving
- docs/process/worklog.md, only if there is meaningful completed work to record
- AGENTS.md, if it needs project-specific adjustments

For each draft, distinguish what you inferred from the repository from what you need me to confirm.

Keep the first version concise. The goal is not perfect documentation. The goal is enough project memory for Builder Mode to stop starting from zero.

After presenting the drafts, stop for my review before editing files.
```

## Review Guidance

The Navigator should review the drafts for truth, not polish.

Correct wrong assumptions, add missing constraints, remove invented certainty, and clarify the current focus. The first version can be imperfect if it gives future sessions a trustworthy starting point.

## What Good Looks Like

A good initialization produces:

- a briefing that explains what the project is and how work should happen,
- product principles that guide trade-offs,
- a roadmap with a current focus,
- a local development guide with commands, validation, documentation, and release rules,
- decisions only when there are real decisions to preserve,
- a worklog only when there is meaningful completed work,
- an `AGENTS.md` that tells future agents how to operate in this project.

The result should make the first Builder Mode session easier, not heavier.
