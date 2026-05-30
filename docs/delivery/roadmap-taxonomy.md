# Roadmap Taxonomy

Ariad uses a delivery taxonomy to keep roadmap work meaningful without turning every task into roadmap structure.

The default hierarchy is:

```text
Value / CV -> Epic -> Delivery Story -> Task
```

Maintenance work sits beside the hierarchy. It is real work, but it should not be inflated into Value, Epic, or Delivery Story unless it changes a meaningful product, project, or process capability.

## Value

A **Value** is a major delivery stage with clear impact for the people or community the project serves.

A Value names why a coherent arc matters. It is larger than a feature group. It changes what the project can do, who it can serve, how ready it is, or what capability it exposes.

Ariad's default concrete form is **Capability Value**, abbreviated **CV**.

```text
CV
  Capability Value
  a major delivery stage with clear user-visible, contributor-visible, operator-visible, community-visible, or business-visible impact
```

Projects may adapt the V in CV when their domain needs a sharper value lens, such as Community Value or Business Value. Ariad's default remains Capability Value because it works across product, platform, process, and tooling projects.

## Epic

An **Epic** is a cohesive block of work inside a Value.

An Epic has a done condition. It is too large to deliver as one Delivery Story, but coherent enough to be recognized as one arc. If an Epic closes, the project should be able to say what capability, product behavior, operational state, or process maturity emerged.

An Epic may suggest a release boundary when it closes, especially when it changes product behavior, public documentation, runtime reliability, or operational capability.

## Delivery Story

A **Delivery Story** is an atomic delivery that can be verified end to end.

A Delivery Story should add behavior or capability that can be validated. In user-facing work, the Navigator should be able to inspect the behavior through a manual validation route. In process, documentation, tooling, or technical work, the validation route may inspect commands, dry-runs, generated output, docs, runtime state, tests, diagnostics, operation evidence, or operational behavior.

A Delivery Story should not be reduced to an internal implementation slice. If no observable behavior or capability can be named, either expose one through a validation route or treat the work as a Technical Story inside an Epic that leads toward a later behavior-visible checkpoint.

A Delivery Story is the normal unit of implementation. It is small enough to plan, implement, validate, document, review, check for coherence, and record in history.

## Technical Story

A **Technical Story** is a Delivery Story whose immediate behavior is internal rather than directly visible to the Navigator.

Technical Stories are valid when they create necessary internal capability, safety, migration, infrastructure, instrumentation, test support, or operational substrate. They should still be verifiable. They may not justify a Navigator behavior checkpoint by themselves, but inside an Epic they should lead toward a later behavior-visible checkpoint.

## Task

A **Task** is concrete work inside a Delivery Story.

Tasks help the Driver execute. They are not normally roadmap items. A task may edit a file, add a test, rename a function, update a command, or adjust a document section. Tasks should not be used to create a false sense of roadmap progress.

## Maintenance

**Maintenance** is legitimate work that may not belong in the roadmap hierarchy.

Examples include typo fixes, dependency updates, CI adjustments, documentation reconciliation, internal cleanup, small process corrections, and low-risk operational upkeep.

Maintenance may produce:

- no release, when it changes only internal project state;
- a patch release, when it changes observable behavior, public documentation, packaging, runtime reliability, or user-facing operation.

Do not inflate maintenance into a Value, Epic, or Delivery Story just to make it visible. Record it in the worklog when meaningful.

## Expand and collapse in the roadmap

The roadmap expands and collapses.

```text
Value / CV expands into Epics.
Epic expands into Delivery Stories.
Delivery Story expands into Tasks.
```

The reverse direction is collapse:

```text
completed Tasks close a Delivery Story
completed Delivery Stories close an Epic
completed Epics close a Value / CV
```

Every collapse should name the emergent value of the whole. An Epic is not done merely because its stories are checked off. It is done when those stories produce a coherent capability or outcome. A Value is not done merely because its Epics are closed. It is done when the project reaches the value boundary the CV named.

## When to expand

Expand when the work is too ambiguous or too large to validate coherently.

Common signals:

- the proposed Delivery Story needs multiple behavior checkpoints;
- the Navigator cannot validate the result in one coherent route;
- technical prerequisites hide the user-facing behavior;
- the scope mixes product, process, project, and release concerns;
- the work has more than one done condition.

In those cases, the Driver should propose an Epic or Value expansion rather than hide complexity inside one story.

## When to collapse

Collapse when the parts have produced a new whole.

Common signals:

- the last Delivery Story in an Epic has been validated;
- roadmap, docs, tests, decisions, and worklog now describe the same state;
- release notes can name the arc clearly;
- the Navigator can recognize the outcome without reading every implementation detail.

Collapse should produce recognition: story done, Epic done, Value done, release candidate, or next coherent horizon.
