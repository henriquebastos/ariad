# Builder Mode Guide

Mirror Mind Builder Mode is the reference runtime for Ariad.

Ariad can be read as a general method for human-agent software work, but its first concrete implementation assumes Mirror Mind. Mirror provides the runtime continuity: journeys, project paths, memory, identity, skills, and context loading. Ariad provides the operating method: Driver/Navigator roles, project documentation, story lifecycle, checkpoints, coherence checks, and opinionated Navigator preference defaults.

## How the Pieces Fit

A Mirror **journey** carries the broader context of an ongoing area of work.

A journey **project path** points Builder Mode to the repository where the work happens.

The target repository contains Ariad's project documentation surface: `AGENTS.md`, project briefing, decisions, roadmap, worklog, and product principles.

Builder Mode loads the journey context, then the agent reads the project documentation and operates as the Driver.

The human remains the Navigator.

## Prepare the Project

Install the project templates into the target repository and adapt the smallest useful context:

- `AGENTS.md`
- `docs/project/briefing.md`
- `docs/project/roadmap/index.md`
- `docs/process/development-guide.md`
- `docs/product/principles.md`

Use [Agent-Assisted Initialization](agent-assisted-initialization.md) when possible. The Driver can inspect the repository and draft these files; the Navigator reviews and corrects the drafts.

The decisions and worklog files can start mostly empty. They become valuable as work happens.

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

The agent should load the journey context, read the project documentation, apply the Driver/Navigator roles, and follow the story lifecycle and checkpoints. If the project defines Navigator preferences, such as commit frequency or push policy, the agent should follow them. If not, it should use Ariad defaults.

## First Builder Session

The first Builder session should be small and real.

A good first session usually does four things:

- reads the journey and project documentation,
- identifies whether the current work is clear enough to plan,
- proposes a small first story or maintenance change,
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
- propose a commit message before committing unless the local commit policy says otherwise.

If the Driver skips these behaviors, update `AGENTS.md` or the project docs before adding more tooling. The first correction should be clarity, not automation.
