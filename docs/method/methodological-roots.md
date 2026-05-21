# Methodological Roots

Ariad is not a collage of existing methods. It is a method for human-agent software work.

Still, it has roots. Naming those roots matters because it keeps Ariad honest about what it inherits and what it transforms.

The strongest methodological roots in Ariad are **Extreme Programming** and **Kanban**.

## From Extreme Programming

Ariad inherits XP's bias toward small, verified, continuously integrated work.

The story lifecycle echoes XP's discipline of moving in small slices: clarify intention, implement narrowly, validate, refactor when needed, and leave the system better understood than before.

XP also informs Ariad's view of feedback. A change is not done because the Driver produced code. It is done when the project can verify it and the Navigator can judge whether it fits the intention.

Important XP resonances:

- small coherent stories;
- fast feedback;
- tests when practical;
- refactoring as part of the work, not a separate virtue signal;
- simple design;
- shared understanding between collaborators;
- readable project history;
- discipline around what enters the codebase.

Ariad adapts these ideas to a human-agent pair. The Driver is not a pair programmer in the human sense, but the Driver/Navigator relationship borrows XP's insight that software work improves when thinking is shared, feedback is frequent, and decisions stay close to the code.

## From Kanban

Ariad inherits Kanban's respect for flow, visibility, and explicit policies.

Kanban teaches that work should be visible and that policies should be explicit enough for people to know how decisions are made. Ariad applies that lesson to agentic work: the Driver must make its state visible to the Navigator, and the project must write down the policies that shape future agent behavior.

Ariad makes work visible through:

- the Driver's orientation, plan, validation route, review, and coherence check;
- project documentation that records decisions, roadmap movement, worklog milestones, product principles, and local process rules;
- checkpoints where the Navigator can see and steer the work before it silently drifts.

Ariad uses explicit policies for decisions that should not be improvised every session. Examples include:

- how technical debt is handled;
- when documentation must change;
- what counts as validation;
- how checkpoint compression works;
- commit and push policies;
- how new scope is captured;
- how follow-up work is recorded.

Ariad also borrows from the spirit of WIP limits, but translates it for agentic development.

The Driver should avoid expanding scope before the current work has collapsed into a coherent state. A story may expand during discovery, but that expansion needs judgment. If new work blocks correctness, it may enter the current story. If it is adjacent, valuable, or merely tempting, the Driver should capture it as follow-up instead of silently increasing work in progress.

This is Ariad's version of limiting WIP: protect the current story until it reaches a coherent collapse: implemented, validated, reviewed, documented, and ready to enter project history.

## What Ariad Changes

XP and Kanban were designed for human teams. Ariad is designed for human-agent collaboration.

The agent introduces a new failure mode: it can produce movement faster than the human can notice that direction has shifted. Ariad's checkpoints, Driver/Navigator roles, and coherence checks exist to protect human judgment inside that acceleration.

Ariad also treats documentation as an active memory surface for future agents. Documentation is not only communication between humans. It is part of the runtime environment in which the next Driver session will think.

## What Ariad Does Not Claim

Ariad does not require a team to practice XP.

Ariad does not require a Kanban board.

Ariad does not import every XP or Kanban practice.

It borrows the parts that protect coherence in agentic software work: small verified change, fast feedback, visible work, explicit policies, and limits against uncontrolled scope expansion.
