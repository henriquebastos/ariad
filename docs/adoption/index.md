# Adoption

A project adopts Ariad by giving agents a small, explicit memory surface and a clear operating contract. The generic path has two independent layers: install the runtime-independent [`using-ariad` Agent Skill](../skill/index.md), then adopt and adapt its project memory templates.

Agent Skills is the portable package format. Discovery locations vary; `.agents/skills/using-ariad/` is conventional, not required, and opening `SKILL.md` manually is always valid. Mirror Mind and Maestro are optional adapters consuming the same package.

The first adoption should stay visible: preview the no-overwrite adopter, install missing templates, adapt them to the real project, and run one small change. Template migration and later skill replacement are separate operations; neither silently rewrites local project knowledge.

## Adoption Goal

The goal is not perfect documentation before work begins. The goal is for the next agent session to know:

- what the project is,
- what matters about the product,
- what decisions should be preserved,
- what work is active,
- how the Driver and Navigator should collaborate.

## Start Here

Use [Install in a Project](install-in-a-project.md) to install the skill and adopt templates. Then use [Agent-Assisted Initialization](agent-assisted-initialization.md) so the Driver can inspect the project and draft project-specific documentation for Navigator review.

[Runtime Integration Guide](builder-mode-guide.md) explains the expected runtime and Driver behavior, including an optional Mirror Builder Mode path. [First Adoption Session](first-adoption-session.md) takes one real change through the method instead of turning adoption into an abstract documentation exercise.
