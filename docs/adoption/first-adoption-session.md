# First Adoption Session

The first adoption session proves Ariad is operational. Do not adopt the method abstractly: prepare one real project and run one small change through it.

## Before the session

Install a pinned `using-ariad` snapshot, preview and apply template adoption, and use [Agent-Assisted Initialization](agent-assisted-initialization.md) to draft local truth for Navigator review. Confirm your agent discovers the skill or explicitly ask it to open `using-ariad/SKILL.md`.

Check the target repository before editing:

```bash
cd /path/to/project
git status
```

Identify its setup, test, and verification commands. If useful, inspect the Ariad docs locally with `uv run mkdocs serve`, but the installed skill is the method source for the session. Do not automatically migrate older templates.

## Optional: Mirror setup

Mirror users may connect a journey to the same prepared project:

```bash
uv run python -m memory journey set-path <journey-slug> /path/to/project
```

```text
/mm-build <journey-slug>
```

This adds journey continuity; it does not replace or redefine `using-ariad`.

## The first pull

The Driver should read context, identify Exploration, Delivery, or Refinement, and propose a small pull. Good examples include:

- document the current setup and verification command,
- add one small missing test,
- fix one visible bug,
- clarify one README section,
- add one small feature with clear validation.

Avoid “refactor the project,” “improve architecture,” or “make it production-ready.” Expand oversized delivery into a smaller User Story or Technical Story; keep ambiguous work in Exploration until it can collapse into a candidate. The first pull tests continuity, not endurance.

## Expected session shape

A successful session includes context reading, a short plan, Navigator confirmation, focused implementation, automated or manual validation, documentation when project state changes, review and coherence checking, and a proposed commit message. The evidence is not file count: it is a coherent path the Navigator can see and judge.

## After the session

If the session produced a meaningful milestone, add a worklog entry under `docs/process/worklog/entries/`. Record adoption friction in the appropriate roadmap, worklog, or Exploration surface without silently expanding the first change. With an optional runtime journey, relevant continuity may also be recorded there.
