# Mirror Extension

The durable Ariad implementation target is a Mirror extension with a skill surface.

Manual adoption is useful for pilots because it keeps the method visible. It is not enough for repeated use across multiple users and projects. Without an extension, each project has to discover the canonical Ariad source manually, copy templates by hand, track version drift informally, and ask the Navigator where the method lives whenever canonical context is needed.

The extension turns Ariad from documentation into an operational capability inside Mirror Mind.

## What the Extension Solves

The extension should solve the problems manual adoption leaves open:

- discover the canonical Ariad source,
- know which Ariad version a project is using,
- install a local Ariad instance into a project,
- reconcile existing project docs without overwriting them blindly,
- update local Ariad templates when the canonical method changes,
- diagnose whether a project is ready for Builder Mode,
- inject canonical Ariad context when the method itself needs to be inspected.

Manual adoption remains the learning path. The extension is the durable product path.

## Three Surfaces

Ariad has three surfaces that should stay separate.

**Ariad repository.** The canonical method source: docs, templates, adoption guidance, and versioned method assets.

**Mirror Mind runtime.** The operational environment: journeys, project paths, memory, identity, Builder Mode, extensions, and skills.

**Target project.** The local method instance: `AGENTS.md`, local development guide, project briefing, decisions, roadmap, worklog, and product principles.

The extension is the bridge between those surfaces.

## Command Shape and Natural-Language Surface

The first command set can stay small, but commands are not the primary user experience.

A Mirror principle matters here: the user should be able to operate the system in natural language. Commands provide reliable internal operations. The skill surface translates user intent into the right command path, asks for missing information, and stops for Navigator review when judgment is needed.

### `ariad init`

Create a new project prepared for Ariad.

Natural-language requests:

```text
I want to create a new project using Ariad.
```

```text
Prepare a new Builder project with Ariad in ~/Code/my-project.
```

```text
Start a new Mirror journey and project using Ariad.
```

Expected responsibilities:

- create or validate the target directory,
- copy the local Ariad templates,
- initialize the local documentation surface,
- optionally initialize Git,
- configure or suggest a Mirror journey and project path,
- report what still needs Navigator review.

### `ariad adopt`

Adopt Ariad in an existing project.

Natural-language requests:

```text
Adopt Ariad in this project.
```

```text
Prepare this existing repo for Mirror Builder Mode with Ariad.
```

```text
Inspect this project and reconcile it with Ariad without overwriting existing docs.
```

Expected responsibilities:

- inspect whether `AGENTS.md` and expected docs already exist,
- avoid overwriting existing files without confirmation,
- copy missing templates,
- detect mature local docs and prefer reconciliation over replacement,
- produce an adoption report.

### `ariad doctor`

Inspect a project and report Ariad readiness.

Natural-language requests:

```text
Check whether this project is ready for Ariad Builder Mode.
```

```text
Run an Ariad readiness check for this journey.
```

```text
Tell me what is missing before this project can use Ariad well.
```

Expected checks:

- `AGENTS.md` exists and mentions Ariad,
- local development guide exists,
- project briefing exists,
- roadmap exists,
- product principles exist,
- Mirror journey has a project path,
- local docs distinguish local instance from canonical Ariad when relevant.

### `ariad update`

Update a project's local Ariad instance from the canonical source.

Natural-language requests:

```text
Update this project's Ariad files from the canonical method.
```

```text
Check whether this local Ariad instance is out of date.
```

```text
Show me what changed in Ariad and what we should reconcile here.
```

Expected responsibilities:

- compare local template versions against canonical versions,
- show proposed changes,
- avoid blind overwrite,
- preserve project-specific local content,
- produce follow-up instructions when manual reconciliation is needed.

## Skill Surface

The extension should expose a skill surface such as `/mm-ariad`.

The command layer should own deterministic operations: copying templates, checking files, reading extension metadata, comparing versions, and reporting readiness.

The skill surface should guide the agent-assisted parts of the workflow: interpreting an existing project, drafting local docs, explaining trade-offs, asking the Navigator for confirmation, and preparing the first Builder Mode session.

Ariad needs both. Commands give reliability. Skills give judgment-shaped workflow.

## Agent-Assisted Responsibilities

The extension should not try to automate interpretation too early.

The agent should remain responsible for:

- reading the target project,
- drafting project-specific documentation,
- distinguishing inference from uncertainty,
- proposing reconciliation when local docs already exist,
- asking for Navigator review before editing meaningful content,
- preparing a first small Builder Mode story.

This keeps Ariad aligned with its own method: the Driver drives, the Navigator navigates.

## Out of Scope for the First Extension

The first extension should not attempt to solve every distribution problem.

Out of scope initially:

- hosted Ariad registry,
- automatic background sync,
- destructive overwrite of project docs,
- broad runtime-agnostic support,
- full semantic diff of local process adaptations,
- migration across multiple Ariad major versions.

The first useful extension should make the pilot flow repeatable: install, adopt, inspect, and guide the first Builder Mode session.
