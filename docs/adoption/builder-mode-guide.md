# Builder Mode Guide

Mirror Mind Builder Mode is the reference runtime for Ariad.

Ariad can be read as a general method for human-agent software work, but its first concrete implementation assumes Mirror Mind. Mirror provides the runtime continuity: journeys, project paths, memory, identity, skills, and context loading. Ariad provides the operating method: Driver/Navigator roles, project documentation, Exploration, Delivery, and Refinement work areas, roadmap taxonomy, Workbench, Delivery Story lifecycle, Refinement Story flow, checkpoints, coherence checks, release handoff, and opinionated Navigator preference defaults.

## How the Pieces Fit

A Mirror **journey** carries the broader context of an ongoing area of work.

A journey **project path** points Builder Mode to the repository where the work happens.

The target repository contains Ariad's project documentation surface: `AGENTS.md`, project briefing, decision records, roadmap items, the Technical Debt Ledger, worklog entries, and product principles.

Builder Mode loads the journey context, then the agent reads the project documentation and operates as the Driver.

The human remains the Navigator.

## Prepare the Project

Install the project templates into the target repository and adapt the smallest useful context:

- `AGENTS.md`
- `docs/project/briefing.md`
- `docs/project/roadmap/index.md`
- `docs/project/decisions/index.md`
- `docs/project/debt/index.md`
- `docs/process/development-guide.md`
- `docs/process/worklog/index.md`
- `docs/product/principles.md`

Use [Agent-Assisted Initialization](agent-assisted-initialization.md) when possible. The Driver can inspect the repository and draft these files; the Navigator reviews and corrects the drafts.

The decision records, debt items, and worklog entry directories can start mostly empty. Their indexes should exist because they explain naming, status, and templates.

## Connect the Journey

Create or choose the Mirror Mind journey that represents the project or ongoing work.

Set the journey project path:

```bash
uv run python -m memory journey set-path <journey-slug> /path/to/project
```

Then activate Builder Mode:

```text
/mm-build <journey-slug>
```

The agent should load the journey context, read the project documentation, apply the Driver/Navigator roles, show the situated work fields when choosing work, and follow the relevant Ariad path: Exploration for unclear signals, Delivery for pulled Value/CV, Delivery Story, User Story, Technical Story, Task, or Maintenance work, and Refinement for pulled Workbench / Refinement Story work. In Refinement, the runtime may choose its own storage model, status names, and surface layout, but the Navigator must be able to see the active field, CR phase, mutation boundary, outcome evidence, and RS closure conditions. If the project defines Navigator preferences, such as commit frequency or push policy, the agent should follow them. If not, it should use Ariad defaults.

## First Builder Session

The first Builder session should be small and real.

A good first session usually does four things:

- reads the journey and project documentation,
- identifies whether the current work belongs in Exploration, Delivery, or Refinement,
- proposes a small first Delivery Story, Refinement Story, or maintenance change,
- moves that change through validation and documentation.

Avoid starting with a broad refactor or a vague product ambition. The first session is a test of continuity. It should prove that the agent can work inside the method without the Navigator having to restate the method manually.

## Expected Behavior

When the method is working, the Driver should:

- read context before editing,
- propose a plan before non-trivial implementation,
- stop at checkpoints,
- provide concrete validation steps,
- update documentation when the project state changes,
- name follow-up work instead of absorbing it silently,
- expand oversized delivery work into User Stories and Technical Stories,
- route existing-capability care through Workbench, Change Requests, and Refinement Stories,
- name release intent when a delivery arc creates a release boundary,
- propose a commit message before committing unless the local commit policy says otherwise.

If the Driver skips these behaviors, update `AGENTS.md` or the project docs before adding more tooling. The first correction should be clarity, not automation.
