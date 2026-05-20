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
- `docs/process/worklog.md`
- `docs/product/principles.md`

## Story Lifecycle

For non-trivial work, follow the Ariad lifecycle:

- plan,
- implement,
- test and validate,
- document,
- review and coherence check,
- commit after Navigator confirmation.

Add any project-specific story rules here.

## Checkpoints

Stop for Navigator confirmation:

- after the plan,
- after tests and the validation route,
- after review and refactoring assessment,
- before commit and push.

Add any project-specific checkpoint rules here.

## Commit and Release Rules

Describe branch, commit, push, pull request, versioning, and release expectations for this project.

## Local Exceptions

Record deliberate deviations from Ariad or from common engineering habits.

Each exception should explain why it exists and when it should be revisited.
