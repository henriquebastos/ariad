# Runtime Integration Guide

Ariad is runtime-independent. Agent Skills is its portable package format; each coding-agent runtime chooses discovery and installation locations. Runtime journeys, memory, identity, and rendering may add continuity, but do not own canonical method access.

## Project surface

Install `using-ariad`, adopt the templates, and adapt the smallest useful context:

- `AGENTS.md`
- `docs/project/briefing/index.md`
- `docs/project/roadmap/index.md`
- `docs/project/decisions/index.md`
- `docs/project/debt/index.md`
- `docs/process/development-guide/index.md`
- `docs/process/worklog/index.md`
- `docs/product/principles/index.md`

The runtime should load `SKILL.md`; without automatic discovery, point it there manually. The Driver reads modular indexes before relevant focused records. Project-local instructions and explicit Navigator direction take precedence. Decision, debt-item, and worklog directories can start mostly empty, but their indexes explain their contracts.

## Expected Driver behavior

The runtime should let the Driver:

- read context before editing and propose a plan before non-trivial work;
- route unclear signals through Exploration, new value through Delivery, and existing-capability care through Refinement;
- show the situated work fields and stop at checkpoints for Navigator judgment;
- provide concrete validation and update documentation when project state changes;
- expand oversized delivery work instead of hiding scope;
- make Refinement's active field, CR phase, mutation boundary, evidence, and closure conditions visible;
- name follow-up work rather than absorb it silently;
- follow local Navigator preferences, otherwise Ariad defaults;
- name release intent at a release boundary and propose a commit message before committing unless local policy differs.

Test this with a small real change. If behavior is weak, clarify `AGENTS.md` or project docs before adding automation.

## Optional Mirror Builder Mode

Mirror Mind Builder Mode is one adapter, not the reference or required runtime. A Mirror journey carries broader continuity and its project path points to the repository containing the same Ariad surface.

Set that path and activate Builder Mode:

```bash
uv run python -m memory journey set-path <journey-slug> /path/to/project
```

```text
/mm-build <journey-slug>
```

Builder Mode should load journey context, then `using-ariad` and project-local docs, show the roadmap/work surface, and propose a small Delivery Story, Refinement Story, or maintenance pull. If useful work is unclear, it should name Exploration rather than force delivery. Maestro may provide additional Mirror conveniences while consuming the identical versioned package and honoring its no-overwrite boundary.
