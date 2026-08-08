# Mirror Extension: Maestro

The durable Ariad implementation target inside Mirror Mind is a Mirror extension called **Maestro**.

Ariad is the method. Maestro is how Mirror runs the method. The two names are deliberately different:

- **Ariad** lives in its own canonical repository. It is method, docs, templates, and principles. It does not depend on any specific runtime.
- **Maestro** is a Mirror extension. It depends on Ariad as the source of truth for templates and on Mirror Mind for journeys, project paths, identity, and Builder Mode.

Other runtimes could implement their own Ariad executors in the future. Maestro is the first one, and the reference one.

## What Maestro Solves

Manual adoption is useful for pilots because it keeps the method visible. It is not enough for repeated use across multiple users and projects. Without an extension, each project has to discover the canonical Ariad source manually, copy templates by hand, track version drift informally, and ask the Navigator where the method lives whenever canonical context is needed.

Maestro solves:

- discovering the canonical Ariad source,
- installing a local Ariad instance into a project,
- avoiding overwrite of existing project docs,
- comparing local templates against canonical templates,
- diagnosing whether a project is ready for Builder Mode,
- inviting the next step when the project is not ready yet.

Manual adoption remains the learning path. Maestro is the durable product path.

## Three Surfaces

The system has three surfaces that should stay separate.

**Ariad repository.** The canonical method source: docs, templates, adoption guidance, and versioned method assets.

**Mirror Mind runtime.** The operational environment: journeys, project paths, memory, identity, Builder Mode, extensions, and skills.

**Target project.** The local method instance: `AGENTS.md`, local development guide, project briefing, decision records, roadmap items, the Technical Debt Ledger, worklog entries, and product principles.

Maestro is the bridge between those surfaces.

## Commands

All commands run through Mirror's external skill dispatch:

```bash
uv run python -m memory ext maestro <command> [args]
```

Commands resolve the project path from either `--project-path` or `--journey <slug>`. The canonical Ariad repository is resolved from `--ariad-root`, `ARIAD_ROOT`, or `~/ariad`.

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
- canonical Ariad repository is detected (and treated as such).

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

Compare a local Ariad instance against the canonical templates.

The command is report-only. It lists files missing locally, files that differ from canonical, and files that are up to date. It does not overwrite or merge.

Natural-language requests:

```text
Check whether this project is out of date relative to canonical Ariad.
```

```text
Show me what changed in Ariad since this project adopted the method.
```

## Skill Surface

The skill `ext-maestro` (or `ext:maestro` on Claude) guides the agent-assisted parts of the workflow: interpreting an existing project, drafting local docs, explaining trade-offs, asking the Navigator for confirmation, and preparing the first Builder Mode session.

The command layer owns deterministic operations. The skill surface owns judgment-shaped workflow. Maestro needs both.

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
- runtime-agnostic distribution (Maestro is Mirror-specific),
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
