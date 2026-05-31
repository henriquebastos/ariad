# Work Areas

Ariad distinguishes two kinds of agentic software work: **Exploratory Work** and **Delivery Work**.

This distinction is part of the method, not a runtime state model. Runtimes may implement work areas as modes, but Ariad defines the methodological fields of work.

## Exploration

**Exploration** preserves and thickens signals before commitment.

Exploration begins when something might matter before it is clear enough for delivery. A new idea appears and needs to be worked through. A promising direction reveals itself in the product. A bug is noticed but not understood. A repeated tension appears across sessions. A product discomfort keeps returning. A methodological gap is felt before there is a proposal. The work is real, but it does not yet have enough form to become a delivery commitment.

Exploration is centered on the **Exploratory Story**.

An Exploratory Story is for sensemaking. It gathers signals, facts, tensions, hypotheses, experiments, contradictions, and interpretations until the material gains enough form to become a candidate for Delivery or loses relevance and moves to archive.

Progress in Exploration is not completion of a target. It is condensation of meaning.

## Delivery

**Delivery** turns formed intent into verified change.

Delivery begins when the work has enough form to become a bounded commitment. A Delivery Story names the delivery arc. It is expanded into User Stories and Technical Stories that can be planned, implemented, validated, documented, reviewed, checked for coherence, and recorded in history. The work may come from a direct request, roadmap item, known bug, or candidate promoted from Exploration.

Delivery is centered on the **Delivery Story** as an arc of delivery.

User Stories and Technical Stories give the Driver and Navigator recognizable units of implementation with intent, scope, validation, documentation, review, and closure.

Progress in Delivery is not activity. It is coherent collapse: the point where the change becomes intelligible, validated, documented, coherent, and ready to enter project history.

## Passage between work areas

Exploration and Delivery are connected, but they should not collapse into each other. Both work areas use the [expand/collapse](expand-collapse.md) rhythm differently.

Exploration protects discovery from premature commitment. Delivery protects commitment from vague motion.

A candidate crosses from Exploration into Delivery only when the Navigator accepts that it has enough form. Until then, the material can remain exploratory without becoming roadmap noise. Once accepted into Delivery, the work receives a place in the [roadmap taxonomy](../delivery/roadmap-taxonomy.md): usually Delivery Story first, then User Stories and Technical Stories. Direct promotion to one User Story is the exception for candidates that are already one behavior-sized unit.

```text
signal -> Exploratory Story -> candidate -> Delivery Story -> User/Technical Stories -> verified change
```

Rare direct path:

```text
signal -> Exploratory Story -> behavior-sized candidate -> User Story -> verified change
```

The passage is not mandatory. Some exploratory material pauses or archives. Some delivery work begins directly from a clear Navigator request. The method only requires that the Driver preserve the boundary: do not turn uncertainty into commitment silently, and do not let delivery dissolve back into open-ended exploration without naming the change.

## Runtime language

Ariad should prefer the method language:

```text
Exploration
Exploratory Work
Delivery
Delivery Work
```

Runtime-specific docs may use mode language when describing execution inside a runtime:

```text
Exploratory Mode
Builder Mode
Delivery Mode
```

Mode implies an executing system following a path. Work area names the methodological field. This is why Ariad's canonical docs use Exploration and Delivery, while Maestro or Mirror docs may describe modes.
