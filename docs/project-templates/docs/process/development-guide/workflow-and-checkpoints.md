# Workflow and Checkpoints

## Roadmap Taxonomy

Use Ariad's default taxonomy unless this project explicitly adapts it:

- **Value / CV:** major delivery stage with clear impact.
- **Delivery Story:** coherent delivery arc inside a Value / CV.
- **User Story:** atomic user-observable delivery verified end to end through behavior or another inspectable output.
- **Technical Story:** verified internal capability needed by a Delivery Story.
- **Task:** concrete work inside a User Story or Technical Story.
- **Maintenance:** legitimate work that may sit outside roadmap structure.

Do not inflate maintenance into the roadmap merely to make it visible.

Default new-work codes are `CV<N>`, `DS<N>`, `US<N>`, and `TS<N>`. Use lowercase roadmap slugs such as `cv9-ds7-conversation-metadata-lifecycle` and `cv9-ds7-us1-dry-run-metadata-lifecycle-decision-path`.

Default states are `Planned`, `Active`, `Blocked`, `Validated`, `Done`, `Deferred`, and `Dropped`. Store state on the item. Prefer `Blocked` with a reason over runtime labels such as `Attention`.

## Expand and Collapse

Expand when ambiguity blocks work: separate concerns, name options, clarify scope, or divide a Delivery Story into User Stories. Collapse when fragments obscure progress: relate parts, update status, name emergent value, close work, or prepare a release boundary.

## Story Lifecycle

For non-trivial work: plan; name acceptance behavior, preferably as Given / When / Then / And; implement; test and validate; review and assess refactoring; document and run a coherence check; then record project history according to local policy.

During review, name debt paid, introduced, and carried forward; its revisit trigger; and whether `docs/project/debt/items/` needs a durable item. Small local debt may remain follow-up work, but debt affecting future delivery, safety, maintainability, validation, operation, or product coherence belongs in the ledger.

## Refinement State Owner

- Not configured. Before active Refinement begins, replace this line with one authorized owner: a repository Workbench path, an external issue tracker/project surface, or another project-owned system. Without that owner, Memory Closure must mark context release not safe when active Refinement state would otherwise exist only in conversation.

## Checkpoints

Stop for Navigator confirmation:

- after showing the Plan Checkpoint surface;
- after automated checks, with a concrete validation route and pass/fail conditions;
- after review and refactoring assessment;
- before recording project history, unless local policy says otherwise.

A confirmation releases work only until the next checkpoint. Add project-specific lifecycle or checkpoint rules here.
