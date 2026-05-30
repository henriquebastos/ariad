# Delivery Flow

This document explains Ariad Delivery through a practical sequence.

The [Conceptual Model](conceptual-model.md) names the concepts. [Roadmap Taxonomy](roadmap-taxonomy.md) defines Value/CV, Epic, Delivery Story, Task, and Maintenance. This page shows how those concepts appear in use: events, checkpoints, validation, review, coherence, and history.

The flow is not a rigid bureaucracy. Delivery work can discover new information, require refactoring, or return to an earlier step. The sequence below is a teaching path.

## Step 1. Navigator Pulls from the Roadmap

Delivery begins with an intentional pull.

The Navigator asks for the delivery field before choosing what to work on:

> Show me the roadmap and recommend what we should pull next.

The Driver reads the roadmap, active focus, planned work, and any recently promoted candidates from Exploration. A promoted candidate should already have a Delivery handoff: suggested Value / CV, Epic seed, candidate Delivery Stories, validation seeds, pull state, and an exploration source. The exploration source should include a concise summary near the roadmap Epic or Story and a link to the full Exploration document. The Driver then renders the delivery field before recommending a next item.

Promoted Exploration candidates normally enter Delivery as an Epic or Epic Expansion. Direct pull as one Delivery Story is reserved for candidates that are already story-sized.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        🗺️  ROADMAP SNAPSHOT                            │
│                                                        │
│  current Value / CV                                    │
│  CV2 Checkout Recovery                                 │
│                                                        │
│  active Epic                                           │
│  E3 Reduce checkout abandonment without redesign       │
│                                                        │
│  backlog                                               │
│  1. Add saved-address editing                          │
│  2. Improve checkout loading feedback                  │
│  3. Review country-specific postal code normalization  │
│                                                        │
│  recently promoted from Exploration                    │
│  Improve mobile address validation recovery            │
│                                                        │
│  active constraints                                    │
│  avoid checkout redesign                               │
│  preserve validation rule behavior                     │
╰────────────────────────────────────────────────────────╯
```

The Driver combines ordinary backlog priority with the new delivery pressure created by Exploration:

> The next backlog item would normally be **Add saved-address editing** because it is the highest planned item in CV2.E3. However, **Improve mobile address validation recovery** was just promoted from Exploration and sits directly inside the active Epic: reducing checkout abandonment without redesigning checkout. I recommend pulling the promoted Delivery Story now, then returning to saved-address editing. That keeps the roadmap order visible, but lets recent learning influence the next commitment instead of aging in the backlog.

The Navigator decides what to pull:

> Pull the promoted validation recovery story.

The pull is the moment where the Navigator turns a candidate, backlog item, Epic, Value, or maintenance item into active Delivery Work. If the pulled item is above story level, the Driver expands it before implementation.

## Step 2. Delivery Story Identified

The Driver identifies the selected work as Delivery because the intent is formed enough to define a roadmap object. If the pulled work came from Exploration, the Driver first checks whether it is an Epic or a rare single Delivery Story.

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

No repository change has happened yet. The Delivery Story is identified, not implemented. If the promoted candidate is larger than one behavior validation route, the next step is Epic Expansion rather than implementation.

## Step 3. Context Loaded

The Driver reads before acting.

Relevant context may include code, tests, documentation, roadmap, previous decisions, product principles, agent instructions, the Delivery Story's exploration summary, and the full Exploration document when the story was promoted from Exploration.

The Driver does not need to show every file read, but it should be able to explain what context matters.

```text
Delivery
╭────────────────────────────────────────────────────────╮
│        ◫  CONTEXT LOADED                               │
│                                                        │
│  story: Improve mobile address validation recovery     │
│                                                        │
│  read                                                  │
│  checkout address form                                 │
│  validation error mapping                              │
│  mobile autofill tests                                 │
│  product principle: recovery before rejection          │
│                                                        │
│  relevant memory                                       │
│  Exploration found mobile autofill values rejected     │
│  with generic error feedback.                          │
╰────────────────────────────────────────────────────────╯
```

Context loading prevents the Driver from treating the repository as a set of files detached from project memory.

## Step 4. Plan Checkpoint

The Driver proposes the route before implementation.

A good plan names the intent, scope, exclusions, implementation approach, validation route, documentation impact, and risks. It also checks whether the pulled item is truly a Delivery Story or whether it should become an Epic expanded into smaller Delivery Stories.

The plan should identify the observable behavior or capability that will let the Navigator accept the story. For non-UI work, this may be a dry-run, diagnostic command, generated artifact, operation evidence, documented policy, runtime state, or other inspectable output. If the plan can only name private implementation steps, the work is not yet a behavior-verifiable Delivery Story; it should be reframed as a Technical Story inside an Epic or reshaped around an observable validation route.

The Driver says:

> I will keep this story focused on field-level recovery guidance for rejected mobile autofill values. I will not redesign checkout or change address validation rules unless the current rules block the recovery message. I will add tests around mobile autofill-shaped values, update the error mapping, and document the validation route.

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
│  documentation impact                                  │
│  update validation notes if behavior changes           │
│                                                        │
│  risk                                                  │
│  validation rules may be coupled to generic errors     │
╰────────────────────────────────────────────────────────╯
```

The Driver stops. The Navigator confirms, redirects, or narrows the plan.

The Navigator says:

> Good. Keep it to recovery guidance. No checkout redesign.

The plan is now confirmed. Speed has direction.

If the Driver discovers that the requested work is too large for one behavior validation moment, the Driver does not hide multiple behavior steps inside one story. It proposes an Epic expansion instead.

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

The Navigator may accept the expansion, reorder the stories, or narrow the Epic.

## Step 5. Implement Delivery Story

The Driver implements one Delivery Story at a time.

A Delivery Story should create new behavior or capability that can be verified and observed through the validation route named in the plan. It should not be a container for a long implementation hidden behind one validation moment, and it should not close on private implementation alone. If the implementation needs multiple behavior checkpoints, the work is probably an Epic and should be expanded during planning.

For a behavior-visible story, the Driver implements until the new behavior can be validated by the Navigator:

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

For a technical story inside an Epic, the Driver verifies the internal behavior and continues until a behavior-visible checkpoint is reached.

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

During implementation the Driver may discover adjacent work:

> I found that postal code normalization is inconsistent across countries. It does not block this Delivery Story because the rejected mobile autofill value can still be mapped to field-level guidance. I will capture normalization as follow-up instead of expanding the story.

```text
follow_up_captured
  title: Review country-specific postal code normalization
  reason: adjacent validation inconsistency found during delivery
  current story impact: not blocking
```

Delivery protects the Delivery Story boundary so the Navigator can still recognize what is being delivered.

## Step 6. Tests and Behavior Validation Route

The Driver runs relevant automated checks and prepares manual validation.

Automated checks tell the project that known contracts still hold. Behavior validation tells the Navigator how to inspect whether the change matches the intention.

For technical stories inside an Epic, the Driver records internal verification and may continue to the next Delivery Story. The Navigator-facing behavior checkpoint appears when a story creates behavior the Navigator can inspect.

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
│  submit address step                                   │
│  expect field-level recovery guidance                  │
│  expect no generic address failure message             │
│                                                        │
│  conscious exclusions                                  │
│  no desktop visual redesign                            │
│  no validation rule changes                            │
╰────────────────────────────────────────────────────────╯
```

The Driver stops when there is behavior for the Navigator to inspect.

If validation fails, the Delivery Story returns to implementation or planning. A failed validation route is not an embarrassment. It is the method doing its work.

## Step 7. Documentation Updated

Documentation changes happen in the same cycle as the change they describe.

The Driver updates the smallest documentation surface needed to keep the project memory true.

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

Documentation is not cleanup. It is part of delivery.

## Step 8. Review and Coherence Check

The Driver reviews what changed and why.

Review looks at the changed surface. Coherence checks whether Process, Project, and Product still agree.

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

The Driver stops at behavior checkpoints and coherence boundaries. If something is missing, the work returns to the relevant step instead of pretending the Delivery Story is done.

## Step 9. History, Epic Closure, and Release Handoff

When the Delivery Story is coherent, the Driver proposes the history action according to the configured commit policy.

Ariad's default is conservative: propose a descriptive commit message and wait for Navigator confirmation before committing.

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

The Navigator accepts:

> Commit it.

The Driver records history and closes the Delivery Story.

```text
story_closed
  title: Show field-level recovery guidance
  history: committed
  result: verified behavior
```

A Delivery Story is not closed because files changed. It is closed because the change became intelligible, validated, documented, coherent, and recorded.

The Driver then shows the transition: what closed, where it was absorbed, what it unlocked, and what movement is coherent next.

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

When all Delivery Stories in an Epic have closed, the Epic becomes the delivery-level unit of completion.

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

Epic closure suggests, but does not automatically start, release management. The Driver should name the release handoff when the completed Epic changes product behavior or operational state enough to warrant packaging, release notes, deployment, or version decisions.

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

If the closed Epic also completes the Value / CV, the collapse is larger:

```text
value_closed
  value: CV2 Checkout Recovery
  completed Epics: 3/3
  emergent value: checkout abandonment can be diagnosed and reduced without broad redesign
  likely release boundary: MAJOR by Ariad default, unless the project overrides versioning policy
```

A Value / CV close does not force a major release. It asks the release-management question at the value boundary.
