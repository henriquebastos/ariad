# Delivery Conceptual Model

This document names the conceptual elements of Ariad Delivery.

It does not explain the practical flow. The step-by-step sequence, examples, checkpoints, and visual feedback live in [Delivery Flow](flow.md).

For the method-level distinction between Exploration and Delivery, see [Work Areas](../method/work-areas.md). For the hierarchy that organizes Delivery, see [Roadmap Taxonomy](roadmap-taxonomy.md).

## Progress semantics

Delivery treats progress as movement toward verified change. A Delivery Story is not merely advanced through tasks. It becomes trustworthy as intent, implementation, validation, documentation, review, coherence, and history converge.

This gives Delivery a formative teleology:

```text
Delivery
  formative teleology
  the work moves toward a known or chosen form
  progress means the intended delivery is becoming complete, verified, and recorded
```

Progress in Delivery is not activity. It is coherent collapse.

A Delivery Story collapses coherently when the Driver and Navigator can say what behavior or project capability changed, why it changed, how it was validated, where the project memory was updated, what risks remain, and how the change entered history. An Epic collapses coherently when its Delivery Stories have produced the intended behavior arc and the Navigator can accept the whole as complete.

## Concepts

### Intentional Pull

An intentional pull is the Navigator's act of selecting work for active Delivery.

The Driver may show the roadmap, identify the next backlog item, and recommend a promoted candidate when recent Exploration changes the delivery field. The Navigator still pulls the work. This keeps prioritization explicit and prevents the Driver from silently turning availability into commitment.

### Value / CV

A Value is a major delivery stage with clear impact. Ariad's default concrete form is Capability Value, abbreviated CV.

A Value / CV expands into Epics and collapses when those Epics produce the intended value boundary. A closed Value / CV may suggest a major release or public milestone.

### Epic

An Epic is a coherent delivery arc inside a Value / CV that is too large to implement as one Delivery Story.

If planning reveals that a proposed Delivery Story needs multiple behavior changes, multiple validation moments, or a sequence of dependent technical work before the Navigator can judge the result, the Driver should name it as an Epic and expand it into smaller Delivery Stories.

An Epic is not a dumping ground for unrelated tasks. It holds a meaningful product, project, or process outcome that requires more than one story to deliver responsibly.

### Delivery Story

A Delivery Story is a bounded unit of meaningful change.

It is larger than a task and smaller than an Epic. It creates a recognizable change in the project and gives the Navigator a concrete moment to accept, redirect, or reject the result.

A Delivery Story may come from a direct Navigator request, roadmap item, known bug, explicit project need, rare story-sized candidate promoted from Exploration, or Epic expansion.

Most promoted Exploration candidates should become an Epic or trigger Epic Expansion before implementation, because Exploration tends to discover an arc rather than one story-sized behavior. Direct promotion to a Delivery Story should be justified during planning.

A Delivery Story should add behavior or capability that can be verified. In user-facing work, that behavior should be visible to the Navigator through a manual validation route. In technical, tooling, documentation, or operational work, the behavior may be a command output, dry-run report, generated document, diagnostic result, runtime state, testable policy, or operation evidence. It should still be observable enough for the Navigator to understand what changed.

A Delivery Story should not close on private implementation alone. If the work has no observable behavior or capability yet, it should either become a Technical Story inside an Epic that leads to a later visible behavior checkpoint, or the plan should expose an observable validation route such as a dry-run, diagnostic, generated artifact, or operation report.

### Intent

Intent is the reason the story exists.

Intent names the change the project is trying to make, not just the files the Driver expects to edit. Without intent, the story becomes a task list. With intent, implementation, validation, and documentation can stay aligned.

### Scope

Scope is the boundary of the story.

It names what belongs inside the current delivery and what should remain outside. Scope can change when correctness requires it, but it should not expand silently.

### Plan

A plan is the Driver's proposed route through the story.

It includes relevant context, affected surfaces, implementation approach, validation route, documentation impact, known risks, and conscious exclusions. A plan is not a guarantee. It is a checkpoint where speed becomes direction.

### Technical Story

A Technical Story is a Delivery Story whose immediate behavior is not directly visible to the Navigator.

Technical Stories are valid when they create necessary internal capability, safety, migration, infrastructure, or test support for an Epic. They still require verification, but they may not justify a Navigator behavior-validation checkpoint by themselves.

When an Epic contains technical stories, the Driver may continue through subsequent stories until a Navigator-visible behavior checkpoint is reached, unless risk, project policy, or Navigator preference requires an earlier stop.

### Behavior Checkpoint

A Behavior Checkpoint is the moment where the Navigator validates newly created behavior.

For visible Delivery Stories, the Behavior Checkpoint normally happens after implementation and validation route preparation. For technical stories inside an Epic, the Driver records internal verification and continues until the next story that exposes behavior the Navigator can inspect.

### Operation Evidence

Operation evidence is structured proof produced by a controlled operation.

It may come from runtime health checks, backups, migrations, release doctors, smoke commands, web operation runs, approval flows, or other allowlisted project operations. Operation evidence should expose state and relevant details in a form the Navigator can inspect before falling back to raw machine payloads.

Operation evidence is especially important for technical stories, release candidates, and operational updates where the behavior is not a simple user-interface change.

### Validation Route

A validation route is the concrete path by which the project and Navigator can inspect the change.

It includes automated checks when available and manual inspection steps when the change is user-visible, product-visible, process-visible, or documentation-visible.

### Documentation Surface

A documentation surface is any project memory that must change for future Drivers and humans to understand the new truth.

It may include README files, architecture notes, roadmap status, decision records, development guides, product principles, command references, worklogs, or local agent instructions.

### Review

Review is the Driver's inspection of what changed and what the change implies.

It names design debt, checks whether refactoring is needed, distinguishes cleanup from new scope, and prepares the coherence check.

### Coherence Check

A coherence check asks whether Process, Project, and Product still agree after the change.

It looks for drift between implementation, tests, documentation, roadmap, decisions, validation notes, and any instruction surface future agents will read.

### Release Intent

Release intent names whether the current Delivery arc is expected to become a release.

It may be known during planning or emerge when a Delivery Story, Epic, or Value collapses. The Driver should surface release intent when the work changes behavior, public documentation, runtime operation, packaging, or user-facing capability enough to warrant release management.

### History Entry

A history entry records the change according to the configured commit or recording policy.

It should preserve why the change happened, not only what files changed. Ariad requires intentional, legible project history. The exact commit and push rhythm belongs to the project contract or Navigator preferences.

## Events

Delivery can be understood through events. Events are moments where the method recognizes that something changed in the delivery field.

Events are not visual components. They may produce visual feedback, conversation feedback, stored records, or later automation, depending on the runtime.

```text
roadmap_requested
  the Navigator asks to see the delivery field before pulling work

roadmap_presented
  the Driver renders current focus, backlog, promoted candidates, and constraints

delivery_item_recommended
  the Driver recommends what to pull next by balancing backlog order, current focus, and newly promoted Exploration candidates

delivery_story_pulled
  the Navigator intentionally selects a backlog item or promoted candidate for active Delivery Work

story_identified
  the Driver recognizes a bounded Delivery Story from the pulled item

epic_identified
  planning reveals that the pulled item is too large for one Delivery Story

epic_expanded
  the Driver proposes smaller Delivery Stories that preserve behavior validation boundaries

context_loaded
  relevant code, documentation, roadmap, decisions, and project instructions are read

plan_presented
  the Driver proposes scope, route, risks, validation, and documentation impact

plan_confirmed
  the Navigator accepts, redirects, or narrows the delivery route

implementation_started
  the Driver begins focused repository changes inside the confirmed Delivery Story boundary

technical_story_verified
  a technical story inside an Epic passes its internal verification without requiring a behavior checkpoint

behavior_checkpoint_reached
  a Delivery Story creates behavior visible enough for Navigator validation

automated_checks_run
  tests, builds, linters, or other automated checks are executed when relevant

validation_route_prepared
  the Driver gives the Navigator a concrete route to inspect the change

operation_evidence_recorded
  a controlled operation produces structured evidence for validation, release, or operational review

documentation_updated
  the smallest necessary project memory surface is updated

review_completed
  the Driver reviews changed surfaces and names refactoring or design debt

coherence_checked
  the Driver checks alignment across Process, Project, and Product

history_proposed
  the Driver proposes the commit message or history action

story_closed
  the Navigator accepts the Delivery Story and the work enters project history or another configured record

epic_closed
  all Delivery Stories in the Epic have reached their validation and coherence criteria

release_candidate_suggested
  Epic closure suggests that release management may begin

follow_up_captured
  adjacent work is preserved without silently entering the current story
```

## Delivery surfaces

A runtime may render Delivery through different surfaces. Maestro currently uses structured checkpoints for delivery work.

```text
Roadmap Snapshot
  What delivery work is available to pull?

Pull Recommendation
  What should be pulled next, and why?

Plan Checkpoint
  Is the route right before implementation begins?

Epic Expansion
  Should this work become multiple Delivery Stories?

Implementation Orientation
  What is being changed inside the Delivery Story boundary?

Validation Checkpoint
  What passed, what needs manual inspection, and what remains uncertain?

Operation Execution
  What controlled operation ran, what state did it reach, and what evidence did it produce?

Review Checkpoint
  What changed, what debt remains, and what documentation or refactoring is needed?

Coherence Checkpoint
  Do Process, Project, and Product still agree?

History Checkpoint
  Is the Delivery Story coherent enough to enter project history?

Epic Closure
  Is the Epic complete enough to suggest release management?
```

These surfaces support the method, but they do not define it. A Delivery Story remains a Delivery Story whether it appears as a checkpoint card, a terminal panel, a web task, a commit proposal, or a conversation summary. An Epic remains an Epic whether it appears as a roadmap group, milestone, release candidate, or expanded set of Delivery Stories.
