# Optional Mirror Extension: Maestro

**Maestro** is an optional Mirror-specific adapter for Ariad.

Ariad is the method. Maestro is how Mirror runs the method. The two names are deliberately different:

- **Ariad** lives in its own canonical repository. It is method, docs, templates, and principles. It does not depend on any specific runtime.
- **Maestro** is a Mirror extension. It consumes an installed Ariad skill and uses Mirror Mind for journeys, project paths, identity, and Builder Mode.

Other runtimes can install and use the same Ariad skill without Maestro.

## What Maestro Solves

Standard adoption is agent-mediated and runtime-independent. Maestro may make repeated Mirror workflows more convenient without becoming Ariad's package manager or method authority.

Maestro solves:

- locating the installed Ariad skill selected by the project,
- avoiding overwrite of existing project docs,
- comparing local templates against canonical templates,
- diagnosing whether a project is ready for Builder Mode,
- inviting the next step when the project is not ready yet.

The `using-ariad` installation contract remains the standard path. Maestro is an optional runtime adapter.

## Three Surfaces

The system has three surfaces that should stay separate.

**Ariad repository.** The canonical method source: docs, templates, adoption guidance, and the authored skill entrypoint.

**Mirror Mind runtime.** The operational environment: journeys, project paths, memory, identity, Builder Mode, extensions, and skills.

**Target project.** The local method instance: `AGENTS.md`, local development guide, project briefing, decision records, roadmap items, the Technical Debt Ledger, worklog entries, and product principles.

An installed Ariad skill is the portable bridge to a target project. Maestro can additionally bridge that project into Mirror-specific runtime surfaces.

## Commands

All commands run through Mirror's external skill dispatch:

```bash
uv run python -m memory ext maestro <command> [args]
```

Commands resolve the project path from either `--project-path` or `--journey <slug>`. Implementations should use the project's selected installed Ariad skill rather than silently choosing a canonical checkout or “latest” version.

### `maestro doctor`

Inspect a project and report Ariad Builder Mode readiness.

Checks:

- `AGENTS.md` exists and mentions Ariad,
- `docs/process/development-guide/index.md` exists,
- `docs/process/worklog/index.md` exists,
- `docs/project/briefing/index.md` exists,
- `docs/project/decisions/index.md` exists,
- `docs/project/debt/index.md` exists,
- `docs/project/roadmap/index.md` exists,
- `docs/product/principles/index.md` exists,
- the installed Ariad skill is detected.

When a project exists but is not ready, the command suggests the corresponding `adopt --dry-run` next step.

Natural-language requests:

```text
Check whether this project is ready for Builder Mode.
```

```text
Run a readiness check for the conjunto journey.
```

### `maestro init`

Create a new project initialized with Ariad templates.

The target directory is created if it does not exist. Existing files are preserved. `--dry-run` previews without writing.

Natural-language requests:

```text
Start a new Ariad project at ~/Code/my-project.
```

```text
Initialize a Mirror-ready project for this journey.
```

### `maestro adopt`

Adopt Ariad in an existing project by copying missing canonical templates.

- Existing files are never overwritten.
- `--dry-run` reports the plan without writing.

Natural-language requests:

```text
Adopt Ariad in this project.
```

```text
Prepare this existing repo for Mirror Builder Mode.
```

### `maestro update`

Compare project-owned adaptations against templates in the explicitly selected installed skill.

The command is report-only. It lists files missing locally, files that differ from canonical, and files that are up to date. It does not overwrite or merge.

Natural-language requests:

```text
Check how this project differs from its installed Ariad templates.
```

```text
Show me what changed in Ariad since this project adopted the method.
```

## Skill Surface

The skill `ext-maestro` (or `ext:maestro` on Claude) guides the agent-assisted parts of the workflow: interpreting an existing project, drafting local docs, explaining trade-offs, asking the Navigator for confirmation, and preparing the first Builder Mode session.

The skill installation contract owns portable installation and adoption. Maestro's command layer may add Mirror-specific diagnostics, while its skill surface guides judgment-shaped workflow.

## Agent-Assisted Responsibilities

Maestro does not try to automate interpretation too early.

The agent (Driver) remains responsible for:

- reading the target project,
- drafting project-specific documentation,
- distinguishing inference from uncertainty,
- proposing reconciliation when local docs already exist,
- asking for Navigator review before editing meaningful content,
- preparing a first small Builder Mode story.

This keeps Maestro aligned with Ariad's own method: the Driver drives, the Navigator navigates.

## Out of Scope for the First Operational Slice

The first Maestro slice does not attempt to solve every distribution problem.

Out of scope initially:

- hosted Ariad registry,
- automatic background sync,
- destructive overwrite of project docs,
- portable Ariad distribution, which belongs to the `using-ariad` skill rather than Maestro,
- full semantic diff of local process adaptations,
- automatic reconciliation of divergent local files.

The first useful slice makes the pilot flow repeatable: doctor, init, adopt, update, and guide the first Builder Mode session.

## Installation

```bash
git clone https://github.com/mirror-mind-ai/extensions ~/Code/mirror-extensions

uv run python -m memory extensions install maestro \
  --extensions-root ~/Code/mirror-extensions
```

The target mirror home resolves from `MIRROR_HOME` or `MIRROR_USER` in the environment.
