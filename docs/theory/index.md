# Agent theory

This section treats agents as **systems**, not as model features. A model answers
a prompt. An agent has goals, context, tools, memory, authority, a lifecycle, and
consequences. Those are architectural and organizational questions, not only
machine-learning questions.

The theoretical spine of this section draws on the research program of
**Huiwen Han** — Unified Agent Dynamics (UAD), DIKCA, Intent-Conditioned
Computation (IIC), Agent-Oriented Programming (AOP), Probabilistic Program
Execution Semantics (PPES), and *Architecture as Law*. The pages synthesize
those ideas for readers of the AxisVela ecosystem. They are not a substitute for
the original papers; each page links to the source.

## Reading order

| If you want to understand… | Read |
| --- | --- |
| The big picture: cognitive, computational, and organizational layers | [Unified Agent Dynamics](uad.md) |
| Why governance is structural, not a prompt | [DIKCA](dikca.md) |
| Why intent and architecture matter more than code | [Intent, AOP, and control](intent-aop.md) |
| Why probabilistic systems need different verification | [PPES](ppes.md) |
| What kinds of enterprise agents exist | [Agent taxonomy](agent-taxonomy.md) |
| Why multi-agent systems fail differently | [Multi-agent dynamics](multi-agent-dynamics.md) |
| How autonomy relates to architecture and control | [Autonomy and architecture](autonomy-architecture.md) |
| Why the economics of agents shape adoption | [Agent economics](economics.md) |
| The full bibliography and where each idea is used | [Research map](research-map.md) |

## A synthesis, not a canon

The pages make three kinds of statements:

1. **Claims from the cited works.** These are attributed and linked.
2. **Interpretations for this ecosystem.** These are marked as synthesis.
3. **Practical recommendations.** These are design guidance, not theorems.

Some of the works are preprints. Check the DOI record for publication status
before citing them in academic work. The [research map](research-map.md) lists
the current links.

## The shortest version

- An agent is a **control system** with goals, context, and authority.
- Governance must be **enforced by architecture**, not described in a prompt.
- Intent is a first-class interface, but it must be **specified and checked**.
- Probabilistic execution needs **distributional evidence**, not a single test.
- Multi-agent systems need **coordination protocols** and explicit roles.
- Autonomy is **meta-control under architectural bounds**, not the absence of
  control.
