# Adoption

A project adopts Ariad by giving agents a small, explicit memory surface and a clear operating contract.

The standard adoption path is agent-mediated and runtime-independent. From an exact Ariad checkout or release selected by the Navigator, the Driver installs a pinned `using-ariad` skill snapshot, inspects the target project, and integrates the smallest useful project documentation surface.

The agent performs the filesystem work, but installation remains explicit and reviewable. It previews destinations, preserves existing project-owned files, adapts templates to real context, and stops for Navigator judgment where integration is ambiguous.

The installed skill contains a copied snapshot of canonical documentation so it remains pinned and usable offline. This repository keeps only one maintained copy under `docs/`; the installation boundary creates the consumer's snapshot. [Maestro](../extension/index.md) may provide optional Mirror-specific integration, but it is not required for installation or adoption.

## Adoption Goal

The goal is not to create perfect documentation before work begins.

The goal is for the next agent session to know:

- what the project is,
- what matters about the product,
- what decisions should be preserved,
- what work is active,
- how the Driver and Navigator should collaborate.

## Start Here

Use [Install in a Project](install-in-a-project.md) to have the Driver install the skill and integrate the templates into a repository.

Then use [Agent-Assisted Initialization](agent-assisted-initialization.md) to have the Driver inspect the project and draft the first project-specific documentation for Navigator review.

Use [Builder Mode Guide](builder-mode-guide.md) when connecting the project to an optional Mirror journey.

Use [First Adoption Session](first-adoption-session.md) to run the first real Builder session without turning adoption into an abstract documentation exercise.
