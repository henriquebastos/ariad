# Delivery Visual Grammar

This document captures the emerging visual language for Maestro's delivery behavior.

It is separate from the [Conceptual Model](conceptual-model.md). The method defines concepts, events, checkpoints, and criteria. The visual grammar chooses how those concepts appear in a specific interface.

## Design boundary

Visual components may help operate Delivery, but they do not define it.

A Delivery Story is a Delivery Story whether it appears as a terminal card, web task, compact checkpoint, roadmap row, commit proposal, or conversation summary. A checkpoint is a methodological pause before it is a visual component.

## Visual direction

Delivery can use block-like cards because its central structure is the roadmap taxonomy: Value / CV, Epic, Delivery Story, Task, and Maintenance. Its central implementation object is the Delivery Story: something bounded enough to become verified change.

Exploration uses triangles to express capture, tension, and emergence. Delivery uses squares and blocks to express bounded commitment, verification, and closure.

```text
triangle exploratory capture, tension, direction, antenna
square   delivery commitment, bounded change, verified artifact
```

The square should not imply rigidity. It means the work has enough boundary to be planned, implemented, validated, documented, and recorded.

## Provisional symbol set

```text
🟪 Value / CV
▣ Epic
■ Delivery Story / delivery artifact
◼ technical story
◫ context loaded
🧭 plan checkpoint
✅ validation checkpoint
◨ documentation update
🔎 review checkpoint
◉ coherence check
🟩■ closed delivery
↳ follow-up captured
```

These symbols are provisional render choices. They should remain replaceable.

## Visual primitives

Delivery visuals should combine shape, icon, color, and state instead of rendering every component as a plain text rectangle.

Ariad defines the semantic mapping. The runtime chooses exact rendering.

### Shape language

```text
■ square card
  bounded delivery commitment

▣ framed square
  parent delivery arc, usually Epic

🟪 colored block
  Value / CV taxonomy card

🟦 colored block
  Epic taxonomy card

🟨 colored block
  Delivery Story taxonomy card

◼ compact filled block
  technical story or internal capability

◉ circle
  current focus, coherence point, or active method state

○ hollow circle
  pending or not-yet-started method state

✓ check
  accepted, validated, or done

✕ cross
  blocked, failed, or rejected

↳ hook
  follow-up or adjacent work captured outside current boundary

⇄ transition
  movement from closed work into parent structure or next coherent pull

🚢 release marker
  release intent, release candidate, or release handoff
```

### Card anatomy

A rich Delivery card should make its visual role visible before the reader parses the prose.

```text
[color/shape][code]  title                       state marker
  level: Value / Epic / Delivery Story / Task
  role: why this card exists in the current surface
  evidence or next movement
```

Examples:

```text
🟪[CV2]  Checkout Recovery                         ◉ active
  value: reduce checkout abandonment without broad redesign
  progress: 2/3 Epics

🟦[E3]   Mobile validation recovery                ◉ current
  epic: recover from address validation failures
  stories: 2/3 done

🟨[S2]   Show field-level recovery guidance         ✓ done
  behavior: mobile users see actionable field-level guidance
  validated: Navigator behavior checkpoint passed

◼[S1]   Classify mobile autofill failures          ✓ verified
  technical: internal classifier and diagnostics
  behavior checkpoint: not yet, continues to S2

↳       Review postal normalization                ○ captured
  follow-up: adjacent, not blocking current story
```

### Surface composition

A surface may use a shell, but the shell should contain cards, markers, and visual relations when roadmap structure matters.

```text
🟪[CV2] Checkout Recovery ◉
  └─ 🟦[E3] Mobile validation recovery ◉
       ├─ 🟨[S1] Classify autofill failures ✓
       ├─ 🟨[S2] Show recovery guidance ◉
       └─ 🟨[S3] Record validation guidance ○
```

The goal is orientation before reading: the Navigator should see level, state, and movement at a glance.

## Provisional color semantics

Taxonomy level and method state should remain visually distinct.

Taxonomy examples:

```text
🟪[CV2]  Capability Value
🟦[E3]   Epic
🟨[S4]   Delivery Story
```

Method state examples:

```text
✓ done
◉ current
○ pending
✕ blocked
```

Color may support delivery posture, but it should not confuse roadmap level with lifecycle state.

```text
gray    context, documentation, or neutral project memory
blue    implementation in progress
green   validated, coherent, or closed delivery
yellow  attention, risk, or pending Navigator judgment
red     blocked validation or incoherent Delivery Story
black   abandoned or superseded delivery work
```

The exact palette belongs to the runtime or UI implementation.

## Core delivery surfaces

Maestro currently uses structured checkpoint surfaces for Delivery:

```text
Roadmap Snapshot
  What delivery work is available to pull?

Pull Recommendation
  What should be pulled next, and why?

Plan Checkpoint
  Is the route right before implementation begins?

Epic Expansion
  Should this work become multiple Delivery Stories?

Implementation Orientation
  What is being changed inside the Delivery Story boundary?

Validation Checkpoint
  What passed, what needs manual inspection, and what remains uncertain?

Review Checkpoint
  What changed, what debt remains, and what documentation or refactoring is needed?

Coherence Checkpoint
  Do Process, Project, and Product still agree?

History Checkpoint
  Is the Delivery Story coherent enough to enter project history?

Transition View
  What closed, where was it absorbed, what did it unlock, and what moves next?

Epic Closure
  Is the Epic complete enough to suggest release management?

Release Intent
  Is there a release boundary now?

Operation Execution
  What controlled operation ran, what state did it reach, and what evidence did it produce?
```

These surfaces are introduced in [Delivery Flow](flow.md). Operation Execution is included here as a visual schema because it often supports technical validation, release checks, runtime operations, and web-console evidence, but the exact web layout belongs to the implementing runtime.

## Surface Shell

A `Surface Shell` is a reusable information structure for rich Delivery surfaces.

It is inspired by web-console and runtime-operation surfaces, but it is not a CSS or layout contract. Ariad defines the information architecture. The runtime chooses whether it appears as tabs, terminal panels, web cards, tables, collapsible sections, or conversation prose.

Use a Surface Shell when a surface needs more than a compact checkpoint card.

Schema:

```text
Surface Shell
  label:
    uppercase surface family or execution category
  title:
    human-readable surface title
  description:
    one sentence explaining what the surface shows or what limitation applies
  tabs or panels:
    optional named views such as Overview, Backlog, Details, Timeline, Result details
  status line:
    compact state sentence, often "result of <surface-id> — <state>"
  primary panel:
    structured human-readable evidence or current state
  secondary evidence:
    optional raw payload, details, links, or audit trail
```

Example shape:

```text
SURFACE LABEL
Surface title

Short explanation of what this surface shows.

Tabs
  Overview | Details

result of surface-id      state

╭────────────────────────────────────────────────────────╮
│ Key:        value                                      │
│ Key:        value                                      │
│                                                        │
│ Evidence or current state                              │
╰────────────────────────────────────────────────────────╯
```

Boundary:

- Ariad owns the shell semantics: label, title, description, panels, status line, evidence.
- The runtime owns typography, spacing, colors, tab implementation, streaming, polling, and collapsible behavior.
- A surface may omit shell parts when the compact form is clearer.

## Operation Execution

An `Operation Execution` surface appears when Delivery runs a controlled operation and needs to preserve visible evidence.

It should show the operation category, operation title, execution mode, state, primary result, and detailed evidence. It may include tabs or panels when the runtime separates live or polled output from structured result details.

Schema:

```text
Operation Execution
  category: operation class or execution domain
  title: human-readable operation name
  description: what this surface is showing or what limitation applies
  primary panels:
    polled console | result details | timeline | approvals
  status line:
    result of <operation-id> — <state>
  result card:
    structured evidence as readable key-value data
  raw evidence:
    optional collapsed machine-readable payload
```

Example:

```text
OPERATION EXECUTION
Runtime health diagnosis

This surface updates from durable run state. True streaming remains future work.

Tabs
  Polled console | Result details

Console
╭────────────────────────────────────────────────────────╮
│ result of runtime-health      attention needed         │
│                                                        │
│  Runtime status: attention needed                      │
│  Version: 0.15.0                                       │
│  Git branch: cv13/v2-agentic-web-console               │
│  Mirror home: /Users/example/.mirror-minds/example     │
│  Database: present                                     │
╰────────────────────────────────────────────────────────╯
```

Use when:

- a technical story is verified through an operation run;
- a release candidate needs runtime health, backup, migration, or smoke evidence;
- a web or runtime surface executes allowlisted operations and preserves audit evidence;
- the Navigator needs to inspect operation state without reading raw JSON first.

Boundary:

- Ariad owns the requirement that controlled operations expose state and evidence when they are used for validation.
- The runtime owns polling, streaming, tabs, colors, typography, raw payload shape, and operation-specific rendering.
- Unknown, attention, blocked, failed, cancelled, and approval-required states should be represented honestly rather than flattened into pass/fail.

## Roadmap Snapshot

A `Roadmap Snapshot` component appears when the Navigator asks to see the delivery field before pulling work.

It should show Value / CV, Epic, Delivery Story backlog, recently promoted candidates from Exploration, active constraints, and enough context for an intentional pull. It should not silently choose the next story.

Roadmap Snapshot may use the reusable [Surface Shell](#surface-shell) when it needs to feel closer to a web-console or operation surface.

Schema:

```text
Roadmap Snapshot
  label: ROADMAP SNAPSHOT
  title: Delivery field overview
  description: source and limits of the roadmap state
  tabs or panels: Overview | Backlog | Promoted | Details
  status line: result of roadmap-snapshot — ready to pull | attention | unknown
  primary panel: current Value / CV, active Epic, backlog, promoted candidates, constraints
  secondary evidence: roadmap links, counts, progress bars, unknowns, stale-state warnings
```

Example:

```text
ROADMAP SNAPSHOT
Delivery field overview

This surface reads project roadmap state and recently promoted Exploration candidates.

Tabs
  Overview | Backlog | Promoted | Details

result of roadmap-snapshot      ready to pull

╭────────────────────────────────────────────────────────╮
│ 🟪[CV2]  Checkout Recovery                      ◉ active │
│          value: reduce abandonment without redesign     │
│                                                        │
│   └─ 🟦[E3] Reduce checkout abandonment          ◉ current│
│      progress: 1/4 Delivery Stories done               │
│                                                        │
│      Backlog                                           │
│      ○ 🟨[S4] Add saved-address editing                 │
│      ○ 🟨[S5] Improve checkout loading feedback         │
│      ○ 🟨[S6] Review postal code normalization          │
│                                                        │
│      Recently promoted from Exploration                │
│      ◉ 🟨[S3] Improve mobile validation recovery        │
│                                                        │
│      Active constraints                                │
│      ✕ broad checkout redesign                         │
│      ✓ preserve validation rule behavior               │
╰────────────────────────────────────────────────────────╯
```

Compact runtimes may render the same information as a smaller checkpoint card instead of the full shell.

## Pull Recommendation

A `Pull Recommendation` component or response appears after the roadmap snapshot.

It should balance normal backlog priority with newly promoted exploratory learning. The Driver may recommend a promoted candidate over the next backlog item, but it must make the trade-off explicit and leave the pull decision with the Navigator.

Preferred response shape:

```text
The next backlog item would normally be **Add saved-address editing** because it is the highest planned item in CV2.E3. However, **Improve mobile address validation recovery** was just promoted from Exploration and sits directly inside the active Epic: reducing checkout abandonment without redesigning checkout. I recommend pulling the promoted Delivery Story now, then returning to saved-address editing. That keeps the roadmap order visible, but lets recent learning influence the next commitment instead of aging in the backlog.
```

## Delivery Story Identified

A `Delivery Story Identified` component appears when the Navigator intentionally pulls work into Delivery.

It should show the story title, source, roadmap placement, intent, commitment state, and current story. If the source is a promoted Exploration candidate, the exploration source should be visible.

Schema:

```text
Delivery Story Identified
  title
  source:
    roadmap backlog | promoted Exploration candidate | maintenance | pulled Epic expansion
  roadmap placement:
    Value / CV -> Epic -> Delivery Story
  intent
  commitment
  current story
  exploration source, when promoted from Exploration:
    source Exploratory Story
    full Exploration document
    Delivery Story exploration summary
    Carry Forward Notes status
```

Example:

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🟪■  DELIVERY STORY IDENTIFIED                  │
│                                                        │
│  Improve mobile address validation recovery.           │
│                                                        │
│  source                                                │
│  promoted Exploration candidate                        │
│                                                        │
│  promoted from                                         │
│  ES-042 Checkout address-step abandonment              │
│                                                        │
│  roadmap placement                                     │
│  🟪[CV2] Checkout Recovery                             │
│    └─ 🟦[E3] Reduce checkout abandonment               │
│         └─ 🟨[S4] Mobile validation recovery           │
│                                                        │
│  intent                                                │
│  help mobile users recover from address errors         │
│                                                        │
│  exploration source                                    │
│  full doc: docs/project/exploration/es-042...md        │
│  summary: roadmap/.../exploration-summary.md           │
│  carry forward notes: preserved                        │
│                                                        │
│  commitment                                            │
│  delivery pending plan confirmation                    │
│                                                        │
│  current story                                         │
│  Mobile autofill values are rejected without useful    │
│  field-level recovery guidance.                        │
╰────────────────────────────────────────────────────────╯
```

## Plan Checkpoint

A `Plan Checkpoint` component appears before implementation for non-trivial Delivery Work.

It should show the scope, out-of-scope boundaries, validation route, documentation impact, and risks. It should make clear that Navigator confirmation is required before implementation begins.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🧭  PLAN CHECKPOINT                             │
│                                                        │
│  Improve mobile address validation recovery.           │
│                                                        │
│  scope                                                 │
│  add field-level recovery guidance for rejected        │
│  mobile autofill values                                │
│                                                        │
│  out of scope                                          │
│  checkout redesign                                     │
│  address validation rule redesign                      │
│                                                        │
│  validation                                            │
│  automated tests for mobile autofill-shaped values     │
│  manual checkout check on mobile viewport              │
│                                                        │
│  risk                                                  │
│  validation rules may be coupled to generic errors     │
╰────────────────────────────────────────────────────────╯
```

## Epic Expansion

An `Epic Expansion` component appears when planning reveals that the pulled work is too large for one Delivery Story.

It should show why the work is an Epic and propose smaller Delivery Stories with behavior validation boundaries. It should prevent large work from being hidden behind one story-level validation moment.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🧩  EPIC EXPANSION                              │
│                                                        │
│  epic                                                  │
│  Improve mobile address validation recovery            │
│                                                        │
│  reason                                                │
│  The work contains multiple behavior and technical     │
│  steps that should not be hidden inside one story.     │
│                                                        │
│  proposed Delivery Stories                             │
│  1. Classify mobile autofill validation failures       │
│     type: technical                                    │
│     validation: automated and diagnostic               │
│                                                        │
│  2. Show field-level recovery guidance                 │
│     type: behavior-visible                            │
│     validation: Navigator behavior checkpoint          │
│                                                        │
│  3. Record validation guidance in project docs         │
│     type: documentation-visible                        │
│     validation: documentation review                   │
╰────────────────────────────────────────────────────────╯
```

## Delivery Story Implemented

A `Delivery Story Implemented` component appears when a Delivery Story has created behavior or capability ready for verification.

It should show what changed and what behavior was created. It should not represent a private implementation chunk inside a larger hidden story.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ◼  DELIVERY STORY IMPLEMENTED                  │
│                                                        │
│  story                                                │
│  Show field-level recovery guidance                   │
│                                                        │
│  changed                                               │
│  address error classifier                              │
│  field-level recovery message                          │
│  mobile autofill regression test                       │
│                                                        │
│  behavior created                                      │
│  rejected mobile autofill values now show field-level  │
│  recovery guidance instead of generic failure          │
╰────────────────────────────────────────────────────────╯
```

## Technical Story Verified

A `Technical Story Verified` component appears when a technical story inside an Epic creates internal capability without producing Navigator-visible behavior yet.

It should show internal verification and the next behavior-visible story. It should make clear that the Driver may continue until a behavior checkpoint is reached, unless risk or project policy requires a stop.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ◼  TECHNICAL STORY VERIFIED                    │
│                                                        │
│  story                                                │
│  Classify mobile autofill validation failures          │
│                                                        │
│  verification                                          │
│  classifier tests passed                               │
│  diagnostic output identifies rejected autofill shape  │
│                                                        │
│  Navigator behavior checkpoint                         │
│  not yet                                               │
│                                                        │
│  next story                                            │
│  Show field-level recovery guidance                    │
╰────────────────────────────────────────────────────────╯
```

## Validation Checkpoint

A `Validation Checkpoint` component appears after automated checks and manual validation route preparation.

It should show automated evidence, manual route, exclusions, and any blocker or uncertainty. For product-visible work, it should never rely on automated checks alone.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ✅  VALIDATION CHECKPOINT                       │
│                                                        │
│  story: Improve mobile address validation recovery     │
│                                                        │
│  automated                                             │
│  address validation tests passed                       │
│  checkout form tests passed                            │
│  build passed                                          │
│                                                        │
│  manual route                                          │
│  open checkout in mobile viewport                      │
│  enter autofill-shaped address values                  │
│  expect field-level recovery guidance                  │
│                                                        │
│  conscious exclusions                                  │
│  no desktop visual redesign                            │
│  no validation rule changes                            │
╰────────────────────────────────────────────────────────╯
```

## Documentation Updated

A `Documentation Updated` component appears when project memory changes as part of the story.

It should show what was updated, why it changed, and what was intentionally left unchanged.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ◨  DOCUMENTATION UPDATED                        │
│                                                        │
│  updated                                               │
│  checkout validation notes                             │
│  roadmap Delivery Story status                         │
│                                                        │
│  reason                                                │
│  mobile address errors now expose field-level          │
│  recovery guidance instead of generic failure          │
│                                                        │
│  not updated                                           │
│  architecture overview, because no rule architecture   │
│  changed                                               │
╰────────────────────────────────────────────────────────╯
```

## Review Checkpoint

A `Review Checkpoint` component appears when the Driver has inspected the changed surface.

It should show what changed, what refactoring happened, what debt remains, and what follow-up was captured.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🔎  REVIEW CHECKPOINT                           │
│                                                        │
│  changed                                               │
│  mobile autofill validation failures now map to        │
│  field-level recovery guidance                         │
│                                                        │
│  refactoring                                           │
│  extracted error classifier branch for readability     │
│                                                        │
│  design debt                                           │
│  country-specific postal normalization remains uneven  │
│                                                        │
│  follow-up                                             │
│  Review country-specific postal code normalization     │
╰────────────────────────────────────────────────────────╯
```

## Coherence Check

A `Coherence Check` component appears when the Driver verifies alignment across Process, Project, and Product.

It should show the three dimensions and a clear result. If one dimension is not coherent, the story should return to the relevant step.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ◉  COHERENCE CHECK                              │
│                                                        │
│  Process                                               │
│  story stayed inside confirmed scope                   │
│  validation route prepared                             │
│                                                        │
│  Project                                               │
│  roadmap and validation notes updated                  │
│  follow-up captured                                    │
│                                                        │
│  Product                                               │
│  user now receives field-level recovery guidance       │
│  checkout redesign avoided                             │
│                                                        │
│  result                                                │
│  coherent                                              │
╰────────────────────────────────────────────────────────╯
```

## History Checkpoint

A `History Checkpoint` component appears before recording the change according to the configured commit policy.

It should show the proposed message, the reason for the change, and the closure evidence.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🟩■  HISTORY CHECKPOINT                         │
│                                                        │
│  story: Improve mobile address validation recovery     │
│                                                        │
│  proposed message                                      │
│  Improve recovery guidance for mobile address errors   │
│                                                        │
│  why                                                   │
│  Mobile autofill values were rejected with generic     │
│  feedback. Field-level guidance now helps users        │
│  recover without broad checkout redesign.              │
│                                                        │
│  ready to close                                        │
│  tests passed                                          │
│  manual validation route prepared                      │
│  documentation updated                                 │
│  coherence checked                                     │
╰────────────────────────────────────────────────────────╯
```

## Transition View

A `Transition View` appears when a Delivery Story, Epic, or Value closes and the Driver needs to show how the completed work changes the larger roadmap.

It should show what completed, where it was absorbed, what it unlocked, what remains, and why the next movement is coherent.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ⇄  TRANSITION VIEW                              │
│                                                        │
│  completed                                             │
│  S2 Show field-level recovery guidance                 │
│                                                        │
│  absorbed into                                         │
│  E3 Improve mobile address validation recovery         │
│                                                        │
│  unlocked                                              │
│  Navigator can validate recovery behavior on mobile    │
│                                                        │
│  remaining in Epic                                     │
│  S3 Record validation guidance in project docs         │
│                                                        │
│  next coherent movement                                │
│  Pull S3, then collapse the Epic if validation and     │
│  documentation remain coherent.                        │
╰────────────────────────────────────────────────────────╯
```

## Epic Closure

An `Epic Closure` component appears when completed Delivery Stories collapse into an Epic.

It should name the completed stories, the emergent capability, and whether release management is suggested.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🟩▣  EPIC CLOSED                                │
│                                                        │
│  epic                                                  │
│  Improve mobile address validation recovery            │
│                                                        │
│  completed Delivery Stories                            │
│  ✓ Classify mobile autofill validation failures        │
│  ✓ Show field-level recovery guidance                  │
│  ✓ Record validation guidance in project docs          │
│                                                        │
│  result                                                │
│  mobile users can recover from address validation      │
│  failures without broad checkout redesign              │
│                                                        │
│  suggested next process                                │
│  release management                                    │
│                                                        │
│  likely release boundary                               │
│  Epic close suggests a MINOR release by Ariad default  │
╰────────────────────────────────────────────────────────╯
```

## Release Intent

A `Release Intent` component appears when release context is known or emerges from closure.

It should show whether the release is known or emergent, the likely boundary, required release work, and the Navigator decision.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🚢  RELEASE INTENT                              │
│                                                        │
│  state                                                 │
│  emergent                                              │
│                                                        │
│  likely boundary                                       │
│  MINOR, because an Epic closed without closing CV2     │
│                                                        │
│  release candidate                                     │
│  Checkout Recovery: mobile validation guidance         │
│                                                        │
│  required before release                               │
│  release note                                          │
│  version or package decision                           │
│  release-specific smoke validation                     │
│                                                        │
│  Navigator decision                                    │
│  enter release management now, defer it, or record     │
│  that no release is needed                             │
╰────────────────────────────────────────────────────────╯
```

## Story Flow Map

`Story Flow Map` is the compact map of Delivery movement.

It should not imply that every story moves linearly without returns. Validation failure, review findings, and coherence gaps can send the story back to implementation, documentation, or planning.

```text
🗺️ roadmap snapshot
      │
      ▼
⇢ pull recommendation ───▶ Navigator chooses what to pull
      │ pulled
      ▼
🟪■ Delivery Story identified
      │
      ▼
◫ context loaded
      │
      ▼
🧭 plan checkpoint ──────▶ Navigator redirects or narrows
      │ confirmed
      ▼
🧩 epic expansion ───────▶ expands if too large
      │ story-sized
      ▼
◼ Delivery Story ────────▶ ↳ follow-up captured
      │
      ▼
✅ behavior checkpoint ──▶ returns if validation fails
      │
      ▼
◨ documentation updated
      │
      ▼
🔎 review checkpoint ─────▶ returns if refactoring is needed
      │
      ▼
◉ coherence check ───────▶ returns if Process, Project, Product drift
      │
      ▼
🟩■ history checkpoint ───▶ Delivery Story closed
      │
      ▼
⇄ transition view ───────▶ next story, Epic closure, or release intent
```

Conceptual mapping:

```text
roadmap snapshot
  current focus, backlog, promoted candidates, and constraints are visible

pull recommendation
  the Driver recommends what to pull by balancing backlog order and recent Exploration learning

Delivery Story identified
  the Navigator has intentionally pulled work into Delivery

context loaded
  project memory and relevant code are read before action

plan checkpoint
  the Navigator confirms direction before implementation

epic expansion
  large work becomes multiple Delivery Stories instead of one oversized story

Delivery Story
  implementation creates verifiable behavior or capability

behavior checkpoint
  automated evidence and Navigator-visible validation route are ready when behavior is inspectable

documentation updated
  project memory changes with the story

review checkpoint
  changed surfaces, debt, and follow-up are named

coherence check
  Process, Project, and Product are reconciled

history checkpoint
  the Delivery Story is ready to enter project history

transition view
  closed work is absorbed into its parent and the next coherent movement is named

epic closure
  completed Delivery Stories collapse into an Epic

release intent
  the completed arc may suggest release management
```

## Language tone

The visual component should make delivery state legible without pretending certainty.

Preferred language:

```text
Here is the route before implementation. Confirm, narrow, or redirect it.
```

```text
Automated checks passed. Here is the manual route to inspect the intended change.
```

```text
This Delivery Story is coherent enough to enter history if you accept the closure.
```

Avoid language that collapses judgment too early:

```text
Done.
```

```text
All good.
```

```text
Ready because tests passed.
```

Delivery visuals should preserve the Navigator's authority. They show evidence, boundary, and state. They do not declare acceptance on the Navigator's behalf.

## Open questions

- Should technical stories always render a component, or only when they occur inside an Epic?
- Should Delivery use one compact card per checkpoint or a single story card that changes state?
- How should follow-up capture appear without becoming a distracting task board?
- Should the Story Flow Map appear in validation and review checkpoints, or only in documentation and teaching surfaces?
- How should Delivery visuals show a story that returns from validation to implementation?
- How should commit policy differences appear without making the history checkpoint noisy?
