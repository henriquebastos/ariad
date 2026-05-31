# Roadmap

The roadmap describes meaningful progress, not every task.

Use the simplest hierarchy that fits the project. Ariad's default delivery taxonomy is:

- **Value / CV**: a major delivery stage with clear impact. Ariad's default CV means Capability Value.
- **Delivery Story**: a coherent delivery arc inside a Value / CV, with a done condition.
- **User Story**: an atomic delivery that can be verified end to end through observable behavior or capability.
- **Technical Story**: internal capability needed by a Delivery Story, still verified but not necessarily Navigator-visible by itself.
- **Task**: concrete work inside a User Story or Technical Story.
- **Maintenance**: legitimate work that may sit outside the roadmap hierarchy.

Do not inflate maintenance work into roadmap structure just to make it visible. Use the worklog for meaningful operational progress and the radar for future possibilities.

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
  cv<N>-<value-slug>/
    cv<N>-ds<M>-<delivery-story-slug>/
      cv<N>-ds<M>-us<K>-<user-story-slug>/
      cv<N>-ds<M>-ts<K>-<technical-story-slug>/
```

Legacy projects may keep old codes for old work, but new Ariad delivery work should use `DS`, `US`, and `TS`.

## States

Recommended roadmap states:

```text
Planned
Active
Blocked
Validated
Done
Deferred
Dropped
```

Use a reason when the state is `Blocked`, `Deferred`, or `Dropped`, for example: `Active; blocked by TS1 policy refinement`. Avoid using runtime warning words such as `Attention` as roadmap states; name the actual lifecycle condition instead.

## Current Focus

Describe the current delivery focus.

Include the outcome being pursued, why it matters now, and what would make this focus complete.

## Active Work

List active values, delivery stories, user stories, technical stories, or maintenance work.

| Item | Status | Notes |
|------|--------|-------|
| Example | Planned | Replace with real work. |

## Planned Work

List known work that is not active yet.

## Done

List recently completed roadmap-level work, or link to a more detailed worklog entry.

## Radar

Capture relevant future work that is visible but not planned.

A radar item should name the problem, not only the solution. Include evidence or a trigger that would make the work worth planning.
