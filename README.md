# Ariad

**Ariad is the thread through the labyrinth of agentic software work.**

It is a method for integral agentic development: human-agent development that keeps the work whole over time.

## Why Ariad exists

Coding agents can move faster than a project can remember. They edit files, generate tests, refactor modules, and draft documentation in minutes. But if the work is not held by a coherent process, speed turns into fragmentation. Decisions happen, but future sessions cannot see them. Documentation exists, but no longer describes the product. The agent helps, but the project slowly forgets itself.

The [method](docs/method/overview.md) exists to prevent that forgetting.

## The shape of the method

Ariad is built on three load-bearing ideas. They are small enough to internalize and complete enough to operate.

**Two roles.** The agent is the [Driver](docs/method/driver-navigator.md). The human is the Navigator. The Driver reads, proposes, implements, validates, documents, and watches for drift. The Navigator holds intent, trade-offs, product judgment, and final validation. Neither replaces the other.

**Three dimensions.** Every change moves through the [triad](docs/method/triad.md) of **Process**, **Project**, and **Product** — how the work is done, what is being built and why, and how the thing behaves for the people it serves. Coherent work keeps the three in alignment.

**One rhythm.** Work flows through the [story lifecycle](docs/method/story-lifecycle.md): read and orient, plan, implement, test and validate, review, document, record history. The Driver self-conducts through the cycle, but [checkpoints](docs/method/checkpoints.md) pause the work for the Navigator at four deliberate moments.

**Opinionated defaults.** Ariad has a [method contract and Navigator preference defaults](docs/method/contracts-and-preferences.md). The contract protects coherence. The defaults give new users a complete starting posture. Advanced Navigators and projects can override preferences such as commit frequency, push policy, checkpoint compression, and documentation detail.

Together these are the thread. Pull on any one and the others come with it.

## Adopting Ariad

A project adopts Ariad by giving its agents a small, explicit memory surface and a clear operating contract. The [adoption guide](docs/adoption/index.md) walks through the path.

The shortest version:

- [Install the method in a repository](docs/adoption/install-in-a-project.md). Copy the [project templates](docs/project-templates/index.md) and adapt them to the real context.
- Let the agent help: [agent-assisted initialization](docs/adoption/agent-assisted-initialization.md) explains how to have the Driver inspect the project and draft the first project-specific documentation for Navigator review.
- Run [the first adoption session](docs/adoption/first-adoption-session.md) to ground the method in a real, small change instead of an abstract documentation exercise.
- Connect the project to an agentic coding runtime with the [Builder Mode guide](docs/adoption/builder-mode-guide.md).

The reference runtime is **Mirror Mind**. The [Mirror extension Maestro](docs/extension/index.md) automates discovery, readiness checks, initialization, and updates of a local Ariad instance inside a Mirror Mind home.

## Documentation site

The full method site is built with MkDocs. To browse locally:

```bash
uv sync
uv run mkdocs serve
```

Then open `http://127.0.0.1:8000`.

## Status

This repository is in an early pilot stage. The current goal is to make the method concrete enough to adopt in real projects while keeping it small enough to understand quickly. Feedback from real adoption shapes what gets added; ceremony for its own sake does not.

## License

Ariad is released under the [MIT License](LICENSE).

### Using the templates

The files in `docs/project-templates/` are designed to be copied into consumer projects and adapted to their context. When you copy a template into your own project, you do not need to preserve the Ariad copyright notice or carry the license text inside that project. The templates exist to be used; attribution is welcome but not required for files copied out as project scaffolding.

The rest of the repository (canonical method docs, site configuration, and any future tooling) remains under the standard MIT terms: keep the copyright notice when redistributing.
