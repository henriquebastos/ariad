# Exploratory Mode Conceptual Model

This document captures the current conceptual shape of Ariad Exploratory Mode. It is a working artifact, not a final specification.

Exploratory Mode is being shaped around one core idea: exploratory work is narrative before it is procedural. It begins with thin signals and gains form through narrative thickening.

## Core distinction

Ariad has two working modes:

```text
Delivery Mode
  work has enough form to become verified delivery

Exploratory Mode
  signals are being captured and options are being explored before there is enough form for delivery
```

Delivery Mode is centered on an Agile-like User Story. Exploratory Mode is centered on an Exploratory Story.

User Story is for delivery; Exploratory Story is for sensemaking.

An Exploratory Story is a narrative thread opened by one or more signals. It thickens as facts, tensions, hypotheses, experiments, and interpretations accumulate. It ends by becoming a candidate for Delivery Mode or by being archived.

## Central questions

```text
Delivery Mode
  What are we delivering?

Exploratory Mode
  What is being captured, and what is it becoming?
```

## Progress semantics

Delivery Mode treats progress as movement toward verified delivery.

Exploratory Mode treats progress as transformation of form. A signal is not merely advanced through steps. It changes nature as it is held, related, questioned, experimented, and shaped.

This gives the two modes different teleologies:

```text
Delivery Mode
  formative teleology
  the work moves toward a known or chosen form
  progress means the intended delivery is becoming complete

Exploratory Mode
  transformative teleology
  the work discovers what form it wants to take
  progress means the material is changing into something more intelligible
```

Progress in exploration is not completion of a target. It is condensation of meaning.

Meaning condenses when thin signals become thicker narratives. A captured signal is only a perceived phenomenon. As it gathers context, connects to other signals, clusters, resonates, attracts interpretation, meets hypotheses, and survives experiments, it gains relation, direction, and interpretive weight.

## Narrative thickening

Exploration begins with thin signals: small captured narratives that are worth preserving but not yet meaningful enough to guide delivery.

!!! note "Signal"

    Users abandon checkout after the address step, but we do not know why.

A signal may open an Exploratory Story. A story thickens through assemblage: it gathers facts, related signals, logs, user reports, contradictions, hypotheses, experiments, constraints, feelings, decisions, and contextual interpretation.

!!! abstract "Assemblage"

    Users abandon checkout after the address step, but the reason is still unclear.
    At first, the only additional clue comes from support tickets: people mention
    confusing address errors. A few days later, analytics gives the story a sharper
    contour. The drop-off is heavier on mobile. Someone checks the frontend logs and
    finds validation_error events around the same step, but the logs do not say which
    field failed or what shape was rejected. When QA tries to reproduce the issue on
    desktop, the path does not fail consistently.

As related signals cluster and resonate, some clusters may become attractors. An attractor is a pattern with enough gravity to pull attention, interpretation, or action.

!!! tip "Emergent Attractor"

    **Mobile address validation and recovery feedback.**

    The checkout problem is no longer a generic drop-off. The material is clustering
    around mobile address validation and recovery feedback. The rewrite-the-whole-checkout
    story is also present, but it may be a misleading attractor.

A candidate forms when a thickened Exploratory Story has enough meaning and direction to invite Delivery Mode. A story may also be archived when it loses relevance, is absorbed elsewhere, or becomes a misleading attractor.

!!! success "Candidate"

    Track where address validation fails so the team can decide whether to fix mobile
    input, error messages, or the broader checkout flow.

## A Mirror Mind Story

The same kind of thickening happened as the Ariad method was expanded to support exploratory work.

!!! note "Signal"

    Problems, situations, and exploratory questions in Mirror do not fit well in the
    roadmap or in the current task system.

The story begins as a signal about work that is real enough to preserve, but not yet formed enough for Delivery Mode.

!!! abstract "Early Assemblage"

    At first, the problem looks like a missing place for unresolved work. A Radar
    extension seems plausible: a dedicated surface to capture issues, tensions, and
    exploratory material that would otherwise disappear.

    As the conversation continues, the shape changes. Radar starts to look less like
    a separate product and more like a capability Maestro may need, because Ariad
    remains the underlying method.

The story thickens as method, runtime, and experience concerns join the same field.

!!! abstract "Method, product, and runtime assemblage"

    The method question then becomes clearer. Ariad may need an Exploratory Mode
    before Delivery Mode. Maestro may need to execute both modes: Delivery Mode for
    verified delivery, Exploratory Mode for signal capture and sensemaking.

    The product surface enters the story next. If this field only exists in CLI or
    conversation, it will stay hidden. The web app needs to show it.

    Then the runtime dimension joins the assemblage. Mirror should become aware of
    the exploratory field during conversation, so it can capture signals naturally
    and without bureaucracy instead of forcing the user to manage a task list.

The story gains more weight when visual exploration changes the conceptual model.

!!! tip "Visual attractor"

    The visual exploration adds another layer. Squares feel too close to delivery
    work. Circles feel too close to generic markers. Triangles begin to resonate
    because they evoke antenna, direction, signal, and tension.

    That visual discovery creates a new methodological constraint: visual language
    can help discover the concept, but it cannot define it. The concept must survive
    multiple renderings.

A later conversation brings a stronger sensemaking frame.

!!! abstract "Sensemaking frame"

    A later conversation brings a stronger sensemaking frame. Exploration is not
    only signal -> inquiry -> candidate. It is narrative thickening.

    The current work itself demonstrates the idea: a thin signal becomes a thicker
    narrative through assemblage, clustering, resonance, attractors, hypotheses, and
    experiments.

    The distinction finally becomes nameable: User Story is for delivery;
    Exploratory Story is for sensemaking.

The current candidate is now visible.

!!! success "Candidate"

    Extend Ariad with Exploratory Mode and expand Maestro with an Exploratory Mode
    that can capture signals, thicken Exploratory Stories, and promote mature
    candidates into Delivery Mode.

Some material also reaches archive.

!!! note "Archived for now"

    Radar as a separate extension. The stronger current hypothesis is to expand
    Maestro rather than create a separate lifecycle.

## Entities

### Signal

A signal is a thin narrative that deserves not to be lost.

It may come from a conversation, a runtime failure, repeated friction, product discomfort, architectural suspicion, user feedback, operational incident, methodological gap, or unresolved question.

A signal does not need a solution. It does not need a planned action. It only needs enough relevance to be preserved.

Example:

> Several users abandon checkout after the shipping address step, but the team
> does not yet know whether the cause is UX, validation, mobile autofill, or a
> backend contract problem.

Possible attributes:

```text
id
journey
summary
source
captured_at
resonance
maturity
links
notes
```

Filled example:

```text
id: SIG-042
journey: checkout-conversion
summary: Users abandon checkout after the shipping address step, with unclear cause across UX, validation, mobile autofill, or backend contract.
source: support tickets, analytics review, frontend error logs
captured_at: 2026-05-28T14:30:00Z
resonance: high
maturity: captured
links:
  - support: tickets #1832, #1841, #1847
  - analytics: checkout funnel drop-off, address step
  - logs: validation_error events from mobile browsers
notes: Preserve as exploratory. Do not create a fix story until the failure mode is better understood.
```

Mirror Mind example:

```text
id: SIG-001
journey: mirror-mind
summary: Problems, situations, and exploratory questions in Mirror do not fit well in the roadmap or in the current task system.
source: conversation during Mirror Mind Builder session
captured_at: 2026-05-28T15:10:00Z
resonance: high
maturity: captured
links:
  - Ariad docs: docs/exploration/ideation.md
  - Ariad docs: docs/exploration/conceptual-model.md
  - Ariad docs: docs/exploration/visual-grammar.md
notes: Preserve as exploratory. The signal may point to Maestro Exploratory Mode rather than a separate extension.
```

### Exploratory Story

An Exploratory Story is a narrative thread opened by one or more signals. It thickens as facts, tensions, hypotheses, experiments, and interpretations accumulate. It ends by becoming a candidate for Delivery Mode or by being archived.

The story begins as a short story of tension. It thickens as new material joins it. The story does not have to move linearly. It can branch, loop, absorb contradictions, weaken hypotheses, form clusters, generate experiments, or end without delivery.

Example:

Initial story:

> Users abandon checkout after the address step, but we do not know why.

Thickened story:

> At first, the team only knows that users are leaving after the address step.
> Then support tickets start describing confusing address errors. A few days later,
> analytics show that the drop-off is heavier on mobile. Someone checks the
> frontend logs and finds validation_error events around the same step, but the
> logs do not say which field failed or what shape was rejected. When QA tries to
> reproduce the issue on desktop, the path does not fail consistently.

Mirror Mind example:

Initial story:

> Exploratory issues in Mirror do not fit the roadmap or the current task system.

Thickened story:

> At first, the idea appears as a possible separate extension: maybe Mirror needs
> a Radar-like place to hold what does not fit the roadmap. As the conversation
> unfolds, that interpretation starts to shift. If Ariad is still the method
> underneath, maybe Maestro should expand instead of creating a separate lifecycle.
>
> The story then gathers more material. Ariad may need an Exploratory Mode before
> Delivery Mode. Signal capture should feel fluid rather than bureaucratic. The
> web app should make the field visible. The runtime should be aware enough to
> capture signals naturally in conversation.
>
> Visual exploration adds another turn. Squares feel too close to delivery work,
> circles feel too generic, and triangles begin to resonate as antenna, direction,
> signal, and tension. But that discovery creates a boundary: visual grammar and
> conceptual model must remain separate.
>
> Later, Cynefin-style thickening gives the exploration a stronger sensemaking
> frame. The work is not just signal -> inquiry -> candidate. Thin signals become
> thicker narratives through assemblage, clustering, resonance, attractors,
> hypotheses, and experiments. Delivery Mode becomes the counterpart to
> Exploratory Mode, and User Story becomes the delivery-side mirror of
> Exploratory Story.

### Assemblage

Assemblage is the process by which an Exploratory Story gains body by absorbing heterogeneous material from its environment.

The story thickens not only by reflection, but by incorporation: logs, conversations, analytics, decisions, feelings, failures, constraints, terminology, visual sketches, and experiments can all become part of the assemblage.

Example:

```text
Checkout address assemblage:
  support tickets
  mobile analytics
  validation logs
  QA reproduction failure
  backend contract suspicion
  user frustration
```

Mirror Mind example:

```text
Exploratory Mode assemblage:
  Ariad method gap
  Maestro execution model
  web visibility need
  conversation awareness
  visual grammar
  Delivery Mode naming
  Cynefin thickening insight
```

### Cluster

A cluster is a meaningful grouping of related signals.

The constellation metaphor is useful here. Stars are separate points, but a constellation appears when relation gives them a recognizable figure. A cluster does not claim that the figure is final or objective. It says that several signals can currently be read together as a pattern.

A cluster reveals recurrence, pattern, tension, or a field of attention. It may emerge manually or through later assistance, but its purpose is conceptual: it says that several signals are pointing at something shared.

Example:

```text
Cluster: checkout address friction
Signals:
  users abandon checkout after the shipping address step
  support tickets mention confusing address errors
  analytics show a mobile-heavy drop-off at the same step
  frontend logs contain validation_error events without field-level clarity
  QA cannot reproduce the issue consistently on desktop
```

Mirror Mind example:

```text
Cluster: pre-roadmap exploration gap
Signals:
  task management does not fit exploratory work
  roadmap is too committed for early questions
  issues disappear when they remain only in conversation
  Mirror needs session-start visibility of unresolved tensions
  Ariad may need an Exploratory Mode before Delivery Mode
```

### Resonance

Resonance is the felt or observed amplification of a signal, cluster, inquiry, or story.

A signal resonates when it returns, echoes across sources, attracts attention, or keeps explaining more than its initial scope. Resonance may be supported by evidence, recurrence, user emotion, operational cost, strategic relevance, or repeated appearance in conversation.

Resonance is a quality of the field, not only a state of one item.

Example:

```text
Checkout address friction resonates because analytics, support tickets, and logs all point toward the same step.
```

Mirror Mind example:

```text
The pre-roadmap exploration gap resonates because it touches task management, roadmap discipline, Builder session orientation, web visibility, Ariad method, and Maestro execution.
```

### Attractor

An attractor is a cluster or story with enough gravity to pull interpretation, attention, or action.

Attractors can be useful or misleading. A useful attractor helps the team see a real pattern. A misleading attractor over-explains events and can distort the field.

Example:

```text
Useful attractor:
The checkout problem may be mobile address validation and recovery feedback.

Misleading attractor:
The entire checkout needs to be rewritten.
```

Mirror Mind example:

```text
Useful attractor:
Maestro may need an Exploratory Mode.

Misleading attractor:
Every unresolved idea needs a new extension.
```

### Inquiry

An inquiry is an exploratory question formed around one or more signals, clusters, or attractors.

An inquiry is not a demand. It is not yet a story. It gives the exploration a center without forcing delivery.

A good inquiry names the uncertainty rather than hiding it.

Example:

```text
What is causing checkout failure around the shipping address step, and is the primary problem UX feedback, client-side normalization, mobile autofill, or the backend validation contract?
```

Mirror Mind example:

```text
What would an integrated Mirror experience look like where signals with the potential to become concrete implementation demands are captured intelligently, fluidly, and without bureaucracy?
```

### Hypothesis

A hypothesis is a possible interpretation, direction, or solution inside an inquiry.

Hypotheses are allowed to compete. They are working shapes, not decisions.

Checkout working hypotheses:

```text
Problem hypotheses

H-P1
The checkout drop-off is caused by address validation failures rather than payment, pricing, or account friction.

H-P2
The failure is concentrated on mobile browsers because mobile autofill sends address, postal code, or phone values in shapes the system does not normalize well.

H-P3
Users can recover when validation is field-specific, but currently the UI shows an ambiguous error or no useful recovery path.

Technical hypotheses

H-T1
The frontend and backend disagree on the address validation contract for at least one mobile-autofilled field.

H-T2
Frontend logs are too coarse to identify the rejected field and raw rejected shape.

H-T3
A tolerant normalization layer can reduce false rejections without weakening backend validation.

Experience hypotheses

H-X1
Users abandon because they do not know which field is wrong or how to correct it.

H-X2
Showing field-level recovery messages at the address step will reduce abandonment more than moving the step later in the checkout.

Delivery hypotheses

H-D1
The first delivery should be instrumentation and diagnosis, not a full checkout rewrite.

H-D2
If the experiment confirms mobile autofill shape mismatch, the delivery candidate should combine normalization and field-level feedback.
```

Mirror Mind working hypotheses:

```text
Method hypotheses

H-M1
Ariad should extend its methodological conceptualization to include exploratory work before delivery.

H-M2
Exploratory work has a different teleology from delivery work: delivery is formative, exploration is transformative.

H-M3
Exploratory progress should be understood as condensation of meaning, not completion of a target.

H-M4
The core exploratory entities are signal, Exploratory Story, assemblage, cluster, resonance, attractor, inquiry, hypothesis, experiment, candidate, and archive.

Execution hypotheses

H-E1
Maestro should execute both Ariad Delivery Mode and Ariad Exploratory Mode.

H-E2
Exploratory Mode should initially live inside Maestro rather than as a separate extension.

H-E3
Maestro should infer lightweight signal capture more often than it asks explicit permission, while requiring Navigator consent for promotion into Delivery Mode.

H-E4
Exploratory events such as signal_captured, exploratory_story_thickened, inquiry_opened, experiment_started, experiment_completed, candidate_formed, and candidate_promoted are useful runtime primitives.

Experience hypotheses

H-X1
Signal capture should feel fluid and non-bureaucratic, not like task creation.

H-X2
A Capture Flash should confirm preservation, show that no commitment was created, and orient the user toward possible next movement.

H-X3
Exploratory visual grammar should differ clearly from kanban/task grammar.

H-X4
Triangles are a promising primary visual shape for exploration because they evoke antenna, signal, direction, and tension.

Implementation hypotheses

H-I1
Exploratory state should be persisted per journey.

H-I2
Builder/session orientation should surface active exploratory material alongside delivery roadmap state.

H-I3
The web app should expose exploratory surfaces, not only CLI commands.

H-I4
The conceptual model and visual grammar should remain separate artifacts.
```

### Experiment

An experiment is a safe-to-learn intervention that introduces new material into the field and observes how the Exploratory Story changes.

Experiments are not delivery work by default. They are learning moves inside exploration. They may involve a prototype, a document sketch, a visual mockup, a code spike, a manual check, instrumentation, or a comparison between alternatives.

An experiment should have a learning intent rather than a delivery promise.

Example:

```text
Instrument address validation failures by field, browser, and raw rejected shape for 48 hours, then replay representative failing payloads in staging.
```

Mirror Mind example:

```text
Create a draft Capture Flash and Signal Flow visual grammar to learn whether signal capture needs immediate flow orientation.
```

### Candidate

A candidate is a thickened Exploratory Story, inquiry, hypothesis, or experiment result mature enough to be considered for Delivery Mode.

A candidate may become:

```text
story
epic
roadmap item
decision record
documentation change
explicit policy
archive
```

Promotion is a Navigator decision. The Driver may suggest promotion, but it should not silently convert exploration into delivery.

Example:

```text
Add tolerant normalization for mobile autofill address fields and show field-level recovery messages when backend validation rejects the address.
```

Mirror Mind example:

```text
Create an Ariad documentation area for Exploratory Mode, with separate conceptual and visual artifacts.
```

### Archive

Archive is the non-active resting place for exploratory material.

Archived material is not necessarily wrong or useless. It may be resolved, duplicated, incorporated elsewhere, intentionally deferred, no longer alive in the current field, or identified as a misleading attractor.

Example:

```text
Archive the hypothesis that a full checkout rewrite is needed because the experiment showed a narrower validation and feedback problem.
```

Mirror Mind example:

```text
Archive Radar as a separate extension for now because the stronger current hypothesis is to expand Maestro with an Exploratory Mode.
```

## States

The state names are provisional.

```text
captured
  the signal has been preserved

thickening
  the story is gaining body through assemblage, relation, resonance, or new context

clustered
  signals have been connected into a pattern or constellation

resonating
  the signal, cluster, inquiry, or story is echoing across sources or returning with force

attracting
  a cluster or story is pulling interpretation, attention, or action

inquiring
  the material has gained a guiding question

experimenting
  a deliberate learning move is underway

maturing
  hypotheses, boundaries, experiment results, or possible directions are taking shape

promotable
  the material has enough form to be considered for Delivery Mode

promoted
  the material crossed into a delivery artifact or durable decision

archived
  the material is no longer active
```

These states describe gain or transformation of form, not task completion.

## Exploratory moves

Exploratory Mode is operated through moves rather than delivery steps.

```text
capture
  preserve a signal before it disappears

thicken
  add context, facts, relations, contradictions, or observations to an Exploratory Story

relate
  connect signals into a cluster or constellation

tune
  notice resonance, weak signals, amplification, or loss of energy

inquire
  form a guiding question from signal material

experiment
  step outside the conversational flow to learn something specific

mature
  clarify hypotheses, tensions, boundaries, experiment results, and possible paths

promote
  offer mature material to Delivery Mode or another durable project artifact

archive
  remove material from the active field without erasing its history
```

## Events

Exploratory Mode can be understood through events. Events are moments where the method recognizes that something changed in the exploratory field.

Events are not visual components. They may produce visual feedback, conversation feedback, stored records, or later automation, depending on the runtime.

### signal_captured

A `signal_captured` event occurs when the Driver recognizes and preserves a signal in a journey.

The event should be lightweight and reversible. Capturing a signal does not create a task, does not modify the roadmap, and does not create a delivery commitment.

Conceptual payload:

```text
journey
summary
source
state: captured
commitment: none
```

The recommended user experience is natural-language acknowledgement, not a form. The Driver may infer more and ask less at this stage because capture is low-risk and reversible.

### exploratory_story_thickened

An `exploratory_story_thickened` event occurs when an Exploratory Story gains new material that changes its meaning, weight, or direction.

Conceptual payload:

```text
journey
story
added_material
material_kind
observed_effect
```

### cluster_formed

A `cluster_formed` event occurs when related signals can be read together as a pattern.

### resonance_detected

A `resonance_detected` event occurs when a signal, cluster, inquiry, or story begins echoing across sources, returning in conversation, or gaining interpretive weight.

### attractor_detected

An `attractor_detected` event occurs when a cluster or story starts pulling interpretation, attention, or action.

Attractor detection should remain provisional. The Driver should treat attractors as readings of a complex field, not as objective truth.

### inquiry_opened

An `inquiry_opened` event occurs when one or more signals gain a guiding question.

The inquiry gives the exploration a center. It still does not create delivery commitment.

### experiment_started

An `experiment_started` event occurs when exploration deliberately leaves the conversational flow to learn something specific.

The event should preserve the experiment's learning intent.

Conceptual payload:

```text
journey
inquiry
learning_intent
method
commitment: learning, not delivery
```

### experiment_completed

An `experiment_completed` event occurs when an experiment produces an observation, artifact, or result that changes the exploratory field.

The result may strengthen a hypothesis, weaken it, open a new inquiry, reveal an attractor, or form a candidate.

### candidate_formed

A `candidate_formed` event occurs when a thickened Exploratory Story, inquiry, hypothesis, or experiment result has enough form to be considered for Delivery Mode.

This is the first point where the Driver should become more explicit, because promotion may affect roadmap, documentation, or implementation direction.

### candidate_promoted

A `candidate_promoted` event occurs when the Navigator accepts a candidate into a delivery artifact such as a story, epic, roadmap item, decision record, documentation change, or explicit policy.

Promotion requires Navigator consent.

### signal_archived

A `signal_archived` event occurs when exploratory material leaves the active field without being erased.

Archiving can mean resolved, duplicated, incorporated elsewhere, deferred, no longer alive in the current field, or identified as a misleading attractor.

## Boundary with Delivery Mode

Exploratory Mode does not execute stories. It prepares the passage into delivery when enough form has emerged.

A possible passage is:

```text
thin signal -> Exploratory Story -> assemblage -> cluster -> attractor -> inquiry -> hypothesis -> experiment -> candidate -> delivery artifact
```

A shorter passage is valid when the material is clear:

```text
signal -> candidate -> story
```

A longer passage is valid when the field remains uncertain.

The passage is not a required linear pipeline. It is a way to describe how exploration may thicken until it becomes promotable.

## Conversation awareness

When Exploratory Mode is active for a journey, the runtime may become aware of it in conversation.

The first safe behavior should be natural acknowledgement, not form-like interruption. Because capture is lightweight and reversible, the Driver may infer a signal and record it while making the action visible in conversation.

For example, the Driver can say that it is capturing a signal in the journey's exploratory field and that no commitment has been created.

Open policy question:

```text
Which exploratory events are safe for inference, and which require explicit Navigator consent?
```

## Relationship with Maestro

Maestro remains the executor of Ariad inside Mirror Mind.

The emerging shape is:

```text
Maestro Delivery Mode
  executes Ariad verified delivery

Maestro Exploratory Mode
  executes Ariad exploratory work
```

A separate extension is not assumed. Exploratory Mode may be a new Maestro capability unless future pressure shows that it needs a separate lifecycle.

## Relationship with visual grammar

Visual design can help discover the method, but it does not define it.

Examples:

```text
Signal -> rendered as a triangle, card, row, voice prompt, or API object
resonance -> rendered as color, ordering, icon, weight, or summary
maturity -> rendered as flow position, state badge, progression, or grouping
Exploratory Story thickening -> rendered as timeline, stack, assemblage map, or narrative card
attractor -> rendered as gravity, weight, cluster center, or visual emphasis
```

The conceptual model must survive multiple renderings.

## Open questions

- What are the minimal attributes of a signal?
- Is resonance a single value, a derived reading, or a set of reasons?
- Are cluster and attractor distinct entities, or is attractor a quality of some clusters?
- Is assemblage an entity, an event, or a process description?
- What criteria make something promotable?
- When is an exploratory experiment still exploration, and when does it become delivery work?
- What is the exact Navigator confirmation policy for capture, experiments, and promotion?
- How should exploratory material appear in Builder Mode session orientation?
- Which parts belong to Ariad method, Maestro execution, Mirror runtime hooks, and web presentation?
