# Optional Mirror Adapter: Maestro

Maestro is an optional Mirror Mind adapter that consumes the same versioned `using-ariad` package as any other runtime. Ariad remains the runtime-independent method and canonical editable repository; Maestro does not own discovery, templates, or a second method copy.

## Surfaces

Keep three surfaces separate:

**Ariad repository.** Human-authored canonical docs plus the sources used to generate the versioned skill package.

**Mirror runtime and Maestro.** Optional journeys, project paths, identity, memory, Builder Mode, extension dispatch, and convenience commands.

**Target project.** Its installed skill snapshot and adapted local `AGENTS.md`, development guide, briefing, decisions, roadmap, debt ledger, worklog, and product principles.

Maestro can bridge Mirror to the package; it is not a distribution authority.

## Command surface

Where the installed Maestro version provides these commands, Mirror dispatch uses:

```bash
uv run python -m memory ext maestro <command> [args]
```

The adapter may resolve a target from `--project-path` or `--journey <slug>`. Its source must be the selected installed `using-ariad` package, rather than a separately discovered canonical template tree.

### `maestro doctor`

Reports whether the project has an Ariad-integrated `AGENTS.md` and the expected briefing, development-guide, worklog, decisions, debt, roadmap, and principles indexes. A readiness report may suggest previewing adoption; it must not claim that different local content is invalid merely because it differs from pristine assets.

```text
Check whether this project is ready for Builder Mode.
```

### `maestro init`

If supported, prepares a new target and invokes the same package adoption semantics. A preview writes nothing and existing files remain untouched. Project-specific content still requires Driver interpretation and Navigator review.

```text
Start a new Ariad project at ~/Code/my-project.
```

### `maestro adopt`

Invokes or faithfully wraps `using-ariad/scripts/adopt.py`: preflight first, create only missing files, count an Ariad-integrated custom `AGENTS.md` as present, return a distinct manual-integration result for an unintegrated doorway, and never overwrite or merge any existing file.

```text
Adopt Ariad in this project.
```

### `maestro update`

Where provided, this is report-only comparison between the installed package snapshot and its pristine assets. It may identify missing, differing, and matching paths. It does not fetch silently, overwrite, merge, or treat skill replacement as migration of adapted local templates.

```text
Show how this project's Ariad templates differ from its installed package.
```

These descriptions define safe integration semantics, not a claim that every Maestro release implements every command.

## Deterministic and judgment responsibilities

Deterministic tooling can verify package identity, inventory expected paths, preflight collisions, copy missing bytes, and report differences. The Driver remains responsible for reading the project, distinguishing inference from uncertainty, drafting local documentation, proposing reconciliation, and selecting a small first pull. The Navigator reviews truth, trade-offs, and acceptance. Automation must not turn a byte difference into permission to replace local knowledge.

## Skill surface

An optional Maestro skill may guide natural-language Mirror workflows, but it should route to the installed `using-ariad/SKILL.md` and package references rather than duplicate them. Command code owns deterministic checks; skills guide judgment-shaped work.

## Installation

For a Mirror environment and extension checkout that provide Maestro:

```bash
git clone https://github.com/mirror-mind-ai/extensions ~/Code/mirror-extensions

uv run python -m memory extensions install maestro \
  --extensions-root ~/Code/mirror-extensions
```

Mirror-specific environment resolution and supported commands belong to that extension's documentation. Ariad itself requires no Mirror process, MCP service, daemon, credentials, or network access.

## Out of scope

The safe adapter boundary excludes a hosted Ariad registry, automatic background sync, destructive overwrite, automatic reconciliation of divergent local files, and semantic migration of project adaptations. Runtime-agnostic distribution already belongs to the `using-ariad` Agent Skill; Maestro only adds optional Mirror integration around it.
