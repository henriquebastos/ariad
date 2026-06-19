# Exploration

Exploration preserves material that is real enough to remember, but not yet formed enough to become Delivery.

Use this area for Exploratory Stories: narrative threads opened by signals, thickened by facts, tensions, hypotheses, experiments, Carry Forward Notes, and interpretations. An Exploratory Story may become a candidate for Delivery, pause, or archive.

This index explains the structure and template. Do not use it as the mutable state surface for active Exploratory Stories. Each Exploratory Story owns its state in its own directory.

## Structure

```text
docs/project/exploration/
  index.md
  es<N>-<story-slug>/
    index.md
    experiments/
      YYYY-MM-DDTHHMMZ-<experiment-slug>.md
    artifacts/
      <supporting-artifact>.md
```

Create the `experiments/` and `artifacts/` directories only when the Exploratory Story needs them. Small stories can live entirely in their own `index.md`.

## Status Values

Use these values in the Exploratory Story `index.md` frontmatter unless the project explicitly adapts them:

```text
Thickening  active sensemaking; material is still gaining form
Paused      meaningful but not active right now
Candidate   enough form to consider for Delivery, awaiting Navigator decision
Promoted    accepted into Delivery with a Delivery handoff or roadmap placement
Archived    preserved but no longer active
```

State belongs in the Exploratory Story metadata, not in the top-level Exploration index and not primarily in the directory path.

## How to Use

- Create one directory per Exploratory Story under `docs/project/exploration/`.
- Use the story directory's `index.md` as the durable story anchor.
- Keep the top-level `docs/project/exploration/index.md` as this guide and template.
- Find active Exploration by searching story indexes for `status: Thickening`, `status: Paused`, or `status: Candidate`.
- Link promoted stories to the Delivery Story or child story that received the handoff.
- Put the concise Delivery summary beside the Delivery Story; keep the full Exploration Documentation in the story directory.

## Exploratory Story Template

Create a new directory such as `es-001-short-slug/`, then copy this template into that directory's `index.md`.

```markdown
---
id: ES-001
status: Thickening
opened: YYYY-MM-DD
updated: YYYY-MM-DD
source:
  - signal-or-context
attractor:
promoted_to:
related:
  - decision-or-roadmap-link
---

# Exploratory Story title

## Current Story

Describe the current thickened story. This should read as the accumulated narrative, not only the latest note.

## Initial Signal

Describe the signal or signals that opened the Exploratory Story.

## Thickening Timeline

Add meaningful changes to the story as dated notes. Do not record every turn; record material that changes meaning, weight, or direction.

### YYYY-MM-DD — Short note title

What changed in the story?

Why does it matter?

## Attractors and Tensions

Name confirmed attractors, rejected attractors, contradictions, or tensions that shape the story.

## Experiments

Link experiments when they exist. If an experiment is small, summarize it here. If it needs detail, create a file under `experiments/` and link it.

## Carry Forward Notes

Preserve implementation-relevant findings only when the Navigator accepts carrying them forward.

## Candidate / Promotion

Describe candidate readiness, Navigator decision, Delivery handoff, roadmap placement, validation seeds, and links to Delivery summaries when relevant.

## Kept-for-Later Signals

Link nearby signals that remain outside this story's scope.

## Archive Notes

If archived, explain why the story is preserved but inactive.
```
