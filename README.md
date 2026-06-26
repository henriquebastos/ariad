# Ariad

**Ariad is the thread through the labyrinth of agentic software work.**

It is a method for integral agentic development: human-agent development that keeps the work whole over time, from the first weak signal to verified delivery.

## Why Ariad exists

Coding agents can move faster than a project can remember. They edit files, generate tests, refactor modules, and draft documentation in minutes. But if the work is not held by a coherent process, speed turns into fragmentation. Decisions happen, but future sessions cannot see them. Documentation exists, but no longer describes the product. The agent helps, but the project slowly forgets itself.

The [method](docs/method/overview.md) exists to prevent that forgetting.

## The shape of the method

Ariad distinguishes three kinds of agentic software work: **Exploratory Work**, **Delivery Work**, and **Refinement Work**.

[**Exploration**](docs/exploration/index.md) preserves and thickens signals before commitment. It holds bugs that are noticed but not understood, product discomforts that keep returning, methodological gaps that are felt before they can become proposals, and patterns that need attention before they deserve roadmap or Workbench weight.

[**Delivery**](docs/delivery/index.md) turns formed intent into verified change. It uses stories, checkpoints, validation, documentation, coherence checks, and intentional history to keep bounded change legible and trustworthy.

[**Refinement**](docs/refinement/index.md) cares for existing capability. It holds requested adjustments, bug fixes, polish, test gaps, documentation corrections, and small structural care without inflating them into roadmap promises.

The [work areas](docs/method/work-areas.md) page explains the boundary and passage between Exploration, Delivery, and Refinement. [Expand and Collapse](docs/method/expand-collapse.md) explains the operating rhythm, while [Roadmap Taxonomy](docs/delivery/roadmap-taxonomy.md) and [Release Management](docs/delivery/release-management.md) define how delivery arcs become recognized value and releases.

Runtimes may implement these areas as modes or lanes. Ariad defines them as methodological work areas. Maestro, the Mirror extension, may speak of Exploratory Mode, Builder Mode, or Refinement lanes because it executes and renders the method inside a runtime.

Ariad is built on a small set of load-bearing ideas. They are simple enough to internalize and complete enough to operate.

**Two roles.** The agent is the [Driver](docs/method/driver-navigator.md). The human is the Navigator. The Driver reads, proposes, implements, validates, documents, and watches for drift. The Navigator holds intent, trade-offs, product judgment, and final validation. Neither replaces the other.

**Three dimensions.** Every change moves through the [triad](docs/method/triad.md) of **Process**, **Project**, and **Product**: how the work is done, what is being built and why, and how the thing behaves for the people it serves. Coherent work keeps the three in alignment.

**One passage.** Work can begin as exploration and later cross into delivery or refinement. A signal becomes an Exploratory Story; an Exploratory Story may thicken into a candidate; a candidate may become a Delivery Story or a requested change when the Navigator accepts it. Ariad protects that passage so discovery does not prematurely become commitment, and committed work does not lose the inquiry that shaped it.

**Opinionated defaults.** Ariad has a [method contract and Navigator preference defaults](docs/method/contracts-and-preferences.md). The contract protects coherence. The defaults give new users a complete starting posture. Advanced Navigators and projects can override preferences such as commit frequency, push policy, checkpoint compression, and documentation detail.

**Explicit policies.** Ariad makes recurring operational decisions visible through [explicit policies](docs/method/explicit-policies.md), starting with coherent updates to runtimes, methods, migrations, templates, and installed tooling.

**Methodological roots.** Ariad's [roots](docs/method/methodological-roots.md) differ by work area. Delivery draws most strongly from XP and Kanban. Exploration draws from Complexity Theory, Cynefin, sensemaking, inquiry, discovery work, and reflective practice. Refinement draws from maintenance, continuous improvement, technical stewardship, and product care.

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
