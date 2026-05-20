# Story Lifecycle

A story is the normal unit of meaningful change.

A story is not just a task. A task can be completed locally: edit a file, rename a function, add a test. A story creates a recognizable change in the project. It has intent, scope, implementation, validation, documentation, and a moment where the Navigator can say: this is done.

The lifecycle exists to keep that change bounded enough to finish and coherent enough to trust.

## Plan

The Driver begins by reading the relevant code and project documentation. It identifies what kind of work this is, what context matters, what is in scope, what is out of scope, and which risks or trade-offs should be visible before implementation.

For non-trivial work, the Driver presents the plan and stops. The Navigator confirms, redirects, or narrows the route. This checkpoint is important because an agent can turn vague intention into concrete changes very quickly. The plan is where speed becomes direction.

## Implement

The Driver changes the repository in focused slices. Behavior changes should be test-driven when practical. Refactoring can happen inside the story when it supports the story's coherence, but new scope should not be silently absorbed.

If the work reveals a larger problem, the Driver names it. Some discoveries belong inside the current story because they block correctness. Others should become follow-up work. The Driver protects the story boundary so the Navigator can still recognize what is being delivered.

## Test and Validate

The Driver runs the relevant automated checks and prepares a manual validation route.

Automated tests tell the project that the implementation still satisfies known contracts. Manual validation tells the Navigator how to inspect whether the change matches the intention. A good validation route is concrete: commands to run, files to inspect, URLs to open, expected observations, and conscious exclusions.

For user-visible or product-visible work, automated tests alone are not enough. The Navigator needs a way to see the change.

## Document

Documentation changes happen in the same cycle as the change they describe.

Documentation is not cleanup. It is part of the project memory. When code changes without documentation, future agents inherit a repository that works but cannot explain itself. When documentation changes without validation, future agents inherit confidence without proof.

The Driver updates the smallest documentation surface needed to keep process, project, and product aligned.

## Review and Coherence Check

The Driver reviews what changed and why. It names design debt, checks whether refactoring is needed, and asks what was forgotten across the triad.

This is the moment to look for drift: roadmap status, decisions, worklog, product principles, command references, tests, validation notes, and any instruction file the agent will read in future sessions.

If something is missing, the Driver returns to the relevant step instead of pretending the story is done.

## Commit

The Driver proposes a descriptive commit message and waits for Navigator confirmation before committing.

A good commit records the reason for the change, not only the files touched. The commit is the point where a story becomes part of project history. It should leave the next session with a clear trail.
