# Roadmap

The roadmap describes meaningful progress, not every task.

This index explains roadmap structure and conventions. Do not use it as the mutable source of truth for every roadmap item. Roadmap items should live in their own files or folders, and each item should carry its own `status` metadata.

## Taxonomy

Use the simplest hierarchy that fits the project. Ariad's default delivery taxonomy is:

- **Value / CV**: a major delivery stage with clear impact. Ariad's default CV means Capability Value.
- **Delivery Story**: a coherent delivery arc inside a Value / CV, with a done condition.
- **User Story**: an atomic delivery that can be verified end to end through observable behavior or capability.
- **Technical Story**: internal capability needed by a Delivery Story, still verified but not necessarily Navigator-visible by itself.
- **Task**: concrete work inside a User Story or Technical Story.
- **Maintenance**: legitimate work that may sit outside the roadmap hierarchy.

Do not inflate maintenance work into roadmap structure just to make it visible. Use the worklog for meaningful operational progress and Exploration records for future possibilities that are not ready for Delivery.

## Codes and Folders

Recommended codes:

```text
CV<N>  Value / Capability Value
DS<N>  Delivery Story
US<N>  User Story
TS<N>  Technical Story
```

Recommended folder pattern:

```text
docs/project/roadmap/
  index.md
  cv<N>-<value-slug>/
    index.md
    cv<N>-ds<M>-<delivery-story-slug>/
      index.md
      exploration-summary.md
      cv<N>-ds<M>-us<K>-<user-story-slug>/
        index.md
        plan.md
        test-guide.md
      cv<N>-ds<M>-ts<K>-<technical-story-slug>/
        index.md
        plan.md
        test-guide.md
```

Legacy projects may keep old codes for old work, but new Ariad delivery work should use `DS`, `US`, and `TS`.

## State Representation

Use Ariad's default roadmap states unless this project explicitly adapts them:

```text
Planned
Active
Blocked
Validated
Done
Deferred
Dropped
```

Put lifecycle state in each roadmap item's frontmatter or status section.

```yaml
---
status: Active
status_reason: pulled for current Delivery Work
updated: YYYY-MM-DD
---
```

Do not use directory moves as the primary state mechanism. Directory moves make paths unstable, can break links, and hide the reason for a transition. Moving a file or folder is acceptable for coarse archival or a deliberate structural reorganization, but the current lifecycle state should remain explicit in the item metadata.

When work cannot proceed, prefer `Blocked` with a reason over runtime warning labels such as `Attention`.

## How to Find Work

- Find active work by searching for `status: Active`.
- Find blocked work by searching for `status: Blocked`.
- Find completed work by searching for `status: Done`.
- Find recent roadmap changes by listing files by modification time or reading linked worklog entries.
- Do not maintain a complete active/planned/done table in this index unless the project deliberately accepts that coordination cost.

## Item Template

Use this shape for a Value, Delivery Story, User Story, Technical Story, or Maintenance record. Adjust fields to the level of work.

```markdown
---
code: CVX.DSY.USZ
level: Value | Delivery Story | User Story | Technical Story | Maintenance
status: Planned
status_reason:
updated: YYYY-MM-DD
related:
  - decision-or-worklog-link
---

# Item title

## Intent

Describe the outcome this item exists to create.

## Scope

Name what belongs inside this item.

## Acceptance / Done Condition

For User Stories, prefer lightweight BDD form:

Given <relevant starting state>
When <the user, operator, command, or runtime action happens>
Then <observable behavior or capability is visible>
And <important constraint or protection still holds>

For Delivery Stories or Values, name the emergent capability or boundary that closes the parent.

## Validation Route

Describe how the Driver and Navigator can verify this item.

## Out of Scope

Name related work that should not be silently absorbed.

## Notes

Add links to Exploration summaries, decisions, debt items, worklog entries, or follow-up work.
```
