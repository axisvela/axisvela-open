# World models and digital twins

An agent that reasons about an enterprise needs more than retrieved text. It
needs a model of **what exists**, **what is true**, **what changed**, and **what
evidence supports the claim**.

## Operational world model

An operational world model is a shared representation of the state relevant to
decisions: assets, orders, facilities, missions, people, policies, and their
relationships. It is not a dashboard and not a data lake. It is a model that can
answer questions.

## Digital twin

A digital twin is a world model for a specific system — a factory, a fleet, a
supply chain — kept in sync with the real system through assertions and
observations. The twin is useful when it is **temporal** and **evidence-bearing**:

- **Temporal (bitemporal):** it distinguishes when something was true from when
  the system recorded it.
- **Evidence-bearing:** every assertion points to its source and confidence.

Project: [ONTOVELA](../projects/ontovela.md).

## Concepts and grounding

A world model needs agreed definitions. Without them, “customer,” “site,” or
“active” mean different things in different systems. A semantic layer defines
concepts, resolves entities, evidence-backs claims, and governs conflicts.

Project: [GNOSIVELA](../projects/gnosivela.md).

## Possible worlds

A world model describes what is. A simulation explores what could be. A
governed experiment defines worlds, scenarios, perturbations, controls, and
seeds, then produces evidence that can be compared and verified.

Project: [PEIRAVELA](../projects/peiravela.md).

## Why it matters for agents

- **Shared context.** Agents, planners, and humans reason over the same state.
- **Grounded decisions.** Claims carry evidence instead of confident prose.
- **Safe experimentation.** High-risk changes can be tested in a possible world
  before they touch the real one.
- **Auditability.** The history of beliefs is part of the record.

## A caution

A world model is only as good as its ingestion and governance. A twin that
silently accepts every assertion is a very expensive dashboard. Evidence,
conflict handling, and freshness are not optional.
