# First Adoption Session

The first adoption session proves that Ariad is operational.

Do not try to adopt the entire method abstractly. Prepare one real project, connect it to Mirror Mind Builder Mode, and run one small change through the method.

## Before the Session

Make sure the local environment can run Mirror Mind and the target project.

Open the Ariad documentation site:

```bash
cd /path/to/ariad
uv run mkdocs serve
```

Open the target project in another terminal and confirm its current state:

```bash
cd /path/to/project
git status
```

If the project has tests or a local verification command, identify it before changing files.

## Adoption Route

Start by copying the Ariad project templates into the target project:

```bash
cd /path/to/ariad
cp docs/project-templates/AGENTS.md /path/to/project/AGENTS.md
mkdir -p /path/to/project/docs/project/roadmap \
  /path/to/project/docs/process \
  /path/to/project/docs/product
cp docs/project-templates/docs/project/briefing.md /path/to/project/docs/project/briefing.md
cp docs/project-templates/docs/project/decisions.md /path/to/project/docs/project/decisions.md
cp docs/project-templates/docs/project/roadmap/index.md /path/to/project/docs/project/roadmap/index.md
cp docs/project-templates/docs/process/worklog.md /path/to/project/docs/process/worklog.md
cp docs/project-templates/docs/product/principles.md /path/to/project/docs/product/principles.md
```

Then use [Agent-Assisted Initialization](agent-assisted-initialization.md) inside the target project. The Driver drafts the project-specific docs; the Navigator reviews for truth.

## Mirror Setup

Create or choose the Mirror journey that represents the target project.

Set the project path:

```bash
uv run python -m memory journey set-path <journey-slug> /path/to/project
```

Activate Builder Mode:

```text
/mm-build <journey-slug>
```

The Driver should load the journey context, read the Ariad project docs, and propose a first small story.

## The First Story

Choose something small enough to complete in one session.

Good first stories usually improve confidence without requiring broad architecture changes. Examples:

- document the current setup and verification command,
- add one small missing test,
- fix one visible bug,
- clarify one README section,
- add one small feature with clear validation.

Avoid vague goals such as "refactor the project", "improve architecture", or "make it production-ready". The first story should test the method, not exhaust it.

## Expected Session Shape

A successful first session should include:

- context reading,
- a short plan,
- Navigator confirmation,
- focused implementation,
- automated or manual validation,
- documentation update if project state changed,
- review and coherence check,
- proposed commit message.

The main evidence is not that many files changed. The evidence is that the Driver worked inside a coherent path and the Navigator could see and validate the work.

## After the Session

Record what happened in the target project's worklog if the session produced a meaningful milestone.

If the adoption flow revealed friction, record it in the Ariad journey or roadmap. Early adoption is not only delivery; it is method discovery.
