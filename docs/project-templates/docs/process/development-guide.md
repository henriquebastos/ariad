# Local Development Guide

This is the project-specific operating contract for agentic development.

Ariad is the canonical method. This file is the local instance of that method for this repository. It explains how the Driver and Navigator should work here, which commands matter, what validation means, and which project-specific rules override generic guidance.

Keep this file practical. It should help a future agent work correctly in this project without asking the Navigator to repeat the same context every session.

## Relationship to Ariad

This project uses Ariad as its human-agent development method.

When Ariad and this local guide differ, follow this local guide for project-specific work and surface the difference during the coherence check.

## Driver and Navigator

The agent is the **Driver**. The human is the **Navigator**.

The Driver reads context, proposes plans, changes files, runs checks, prepares validation routes, updates documentation, and stops at checkpoints.

The Navigator holds intent, trade-offs, product judgment, and acceptance.

## Project Commands

List the commands the Driver should use in this project.

```bash
# install dependencies

# run tests

# run lint or formatting checks

# run the app locally
```

## Verification

Describe what counts as verified work in this project.

Include automated checks, manual validation routes, smoke tests, screenshots, local URLs, database safety rules, or any project-specific acceptance expectations.

## Documentation Rules

Describe when documentation must be updated.

Common documentation surfaces:

- `README.md`
- `docs/project/briefing.md`
- `docs/project/decisions.md`
- `docs/project/roadmap/index.md`
- `docs/project/debt.md`
- `docs/process/worklog.md`
- `docs/product/principles.md`

## Roadmap Taxonomy

Use Ariad's default taxonomy unless this project explicitly adapts it:

- Value / CV: major delivery stage with clear impact.
- Delivery Story: coherent delivery arc inside a Value / CV.
- User Story: atomic user-observable delivery that can be verified end to end through observable behavior or capability. For non-UI work, the validation route may be a dry-run, diagnostic, operation report, generated artifact, documented policy, runtime state, or other inspectable output.
- Technical Story: internal capability needed by a Delivery Story, still verified but not necessarily Navigator-visible by itself.
- Task: concrete work inside a User Story or Technical Story.
- Maintenance: legitimate work that may sit outside roadmap structure.

Do not inflate maintenance into the roadmap just to make it visible.

Use Ariad's default new-work codes unless this project explicitly adapts them: `CV<N>` for Values, `DS<N>` for Delivery Stories, `US<N>` for User Stories, and `TS<N>` for Technical Stories. Roadmap folders should use lowercase slugs such as `cv9-ds7-conversation-metadata-lifecycle` and child folders such as `cv9-ds7-us1-dry-run-metadata-lifecycle-decision-path`.

Use Ariad's default roadmap states unless this project explicitly adapts them: `Planned`, `Active`, `Blocked`, `Validated`, `Done`, `Deferred`, and `Dropped`. When work cannot proceed, prefer `Blocked` with a reason over runtime warning labels such as `Attention`.

## Expand and Collapse

Use expand when work is blocked by ambiguity: separate concerns, name options, clarify scope, or expand a Delivery Story into User Stories.

Use collapse when work is lost in fragments: relate parts, update status, name emergent value, close a User Story or Technical Story, close a Delivery Story, or prepare a release boundary.

## User and Technical Story Lifecycle

For non-trivial work, follow the Ariad lifecycle:

- plan,
- name User Story acceptance behavior, preferably as Given / When / Then / And,
- implement,
- test and validate,
- document,
- review and coherence check,
- record project history according to the configured commit policy.

Add any project-specific story rules here.

## Technical Debt Tracking

Use `docs/project/debt.md` when debt should outlive one story's review notes.

During Review, name:

- debt paid;
- new debt introduced;
- debt carried forward;
- revisit trigger;
- whether a Debt Ledger entry should be created or updated.

Small local debt can be captured as follow-up. Debt that may affect future delivery, safety, maintainability, validation, operation, or product coherence should enter the ledger.

## Checkpoints

Stop for Navigator confirmation:

- after the Plan Checkpoint surface is shown; creating `plan.md` does not replace the visible checkpoint,
- after automated checks, with a concrete Navigator validation route that includes expected observations, pass condition, and fail condition,
- after review and refactoring assessment,
- before recording project history unless the local commit policy says otherwise.

Add any project-specific checkpoint rules here.

## Navigator Preferences

Ariad ships with opinionated defaults. Override them here when this project or Navigator has a better local answer.

- **Commit policy:** default is to commit after a coherent story or meaningful change is validated and accepted.
- **Push policy:** default is to ask before pushing to a shared remote.
- **Checkpoint compression:** default is full checkpoints for non-trivial work, compressed checkpoints only for trivial low-risk changes.
- **Documentation detail:** default is the smallest documentation update that keeps the project coherent.
- **Worklog policy:** default is to record meaningful milestones, not every edit.
- **Branch/PR habits:** describe local branch, pull request, review, or merge expectations.

## Commit and Release Rules

Describe branch, commit, push, pull request, versioning, and release expectations for this project.

If the work creates a release boundary, name the likely boundary explicitly: Value / CV, Delivery Story, User Story, Technical Story, or Maintenance.

## Local Exceptions

Record deliberate deviations from Ariad or from common engineering habits.

Each exception should explain why it exists and when it should be revisited.
