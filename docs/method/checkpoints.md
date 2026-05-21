# Checkpoints

Checkpoints are moments where the Driver stops and the Navigator exercises judgment.

They exist because coding agents can convert ambiguity into motion faster than humans can notice the drift. A checkpoint does not slow the work for its own sake. It gives direction a place to re-enter the work before the next slice begins.

## Mandatory checkpoints

For non-trivial work, the Driver stops:

- after the plan,
- after tests and the manual validation route,
- after review and refactoring assessment,
- before recording the change in project history according to the configured commit policy.

Between checkpoints, the Driver may operate without asking permission for every file. At checkpoints, the Driver stops for real. A confirmation releases the work until the next checkpoint, not through the entire lifecycle.

Ariad's default is conservative: propose the commit message, wait for Navigator confirmation, then commit. Pushing to a shared remote is not a method invariant; it is a project contract or Navigator preference. When no preference is configured, ask before pushing.

## After the plan

The Driver presents the route before implementation. The Navigator confirms that the work is framed correctly, that scope is right-sized, and that the proposed path matches the actual intention.

This prevents the agent from building the wrong thing well.

## After tests and validation route

The Driver reports automated checks and gives the Navigator a concrete way to inspect the change.

This prevents the story from being treated as done merely because the agent says it is done.

## After review and refactoring assessment

The Driver reviews the changed surface, names design debt, and says what was cleaned up or deferred.

This prevents the project from accumulating hidden structural cost while each individual story appears successful.

## Before recording history

The Driver proposes the commit message or history action and waits according to the configured commit policy.

This gives the Navigator one final moment to check whether the story is coherent enough to enter project history. Ariad requires intentional history; the exact commit and push rhythm belongs to Navigator preferences or the project contract.

## Why checkpoints matter

The point is not ceremony. The point is preserving agency where it belongs. The agent can drive, but it should not silently own direction. Product judgment remains human, and checkpoints are how the method protects that judgment without requiring constant micromanagement.
