# Ariad

Ariad is the thread through the labyrinth of agentic software work.

It is a method for integral agentic development: human-agent development that keeps the work whole over time, from the first weak signal to verified delivery.

It starts from a simple observation: coding agents can move faster than a project can remember. They can edit files, generate tests, refactor modules, and draft documentation in minutes. But if the work is not held by a coherent process, speed turns into fragmentation. The code changes, but the reason for the change gets lost. Decisions happen, but future sessions cannot see them. Documentation exists, but no longer describes the product. The agent helps, but the project slowly forgets itself.

The method exists to prevent that forgetting.

Ariad distinguishes three kinds of agentic software work: **Exploratory Work**, **Delivery Work**, and **Refinement Work**.

**Exploration** preserves and thickens signals before commitment. It is where Ariad holds material that is real enough to preserve but not yet formed enough to deliver.

**Delivery** turns formed intent into verified change. It is where Ariad uses stories, checkpoints, validation, documentation, coherence checks, and intentional history to make change trustworthy.

**Refinement** cares for existing capability. It is where Ariad holds requested adjustments, bug fixes, polish, test gaps, documentation corrections, and small structural care without inflating them into roadmap promises.

Runtimes may implement these areas as modes or lanes. Ariad defines them as methodological work areas. Maestro, the Mirror extension, may speak of modes because it executes and renders Ariad inside a runtime.

Ariad gives the agent an operating model and gives the human a clear place to exercise judgment. The agent becomes the Driver: reading, proposing, implementing, validating, documenting, and checking coherence. The human remains the Navigator: holding intention, product sense, trade-offs, and final validation.

Ariad is runtime-independent. The standard `using-ariad` Agent Skill packages the method for portable use; skill discovery and installation locations vary by runtime. Mirror Mind and Maestro are optional adapters that consume the same package.

The promise is not more ceremony. The promise is coherent progress.

## Start here

- [Method overview](method/overview.md) explains the operating model.
- [Work Areas](method/work-areas.md) explains the method-level distinction between Exploration, Delivery, and Refinement.
- [Expand and Collapse](method/expand-collapse.md) explains the rhythm by which work differentiates and reintegrates.
- [Exploration](exploration/index.md) holds pre-roadmap signals, inquiries, hypotheses, experiments, and candidates before they become delivery work.
- [Delivery](delivery/index.md) explains how formed intent becomes verified change.
- [Refinement](refinement/index.md) explains how requested changes to existing capability move through Workbench, Change Requests, and Refinement Stories.
- [Roadmap Taxonomy](delivery/roadmap-taxonomy.md) defines Value/CV, Delivery Story, User Story, Technical Story, Task, and Maintenance.
- [Release Management](delivery/release-management.md) defines release boundaries, release intent, release notes, and default versioning policy.
- [Driver and Navigator](method/driver-navigator.md) defines the human-agent collaboration roles.
- [Process, Project, Product](method/triad.md) names the three dimensions of coherent work.
- [User and Technical Story Lifecycle](delivery/story-lifecycle.md) describes the delivery rhythm for bounded change.
- [Checkpoints](delivery/checkpoints.md) names the pauses where Navigator judgment re-enters delivery work.
- [Contracts and Preferences](method/contracts-and-preferences.md) separates Ariad's invariants from configurable Navigator preference defaults.
- [Explicit Policies](method/explicit-policies.md) defines recurring operating policies, starting with coherent updates.
- [Methodological Roots](method/methodological-roots.md) names the different roots behind Exploration, Delivery, and Refinement.
- [Install in a Project](adoption/install-in-a-project.md) shows how to adopt the method in a repository.
- [Using Ariad Skill](skill/index.md) explains the portable package, versioning, and validation.
- [Builder Mode Guide](adoption/builder-mode-guide.md) explains how to use the method with an agentic coding runtime.
- [Mirror Extension (Maestro)](extension/index.md) describes the durable implementation path for Ariad inside Mirror Mind.
