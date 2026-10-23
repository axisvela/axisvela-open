# Unified Agent Dynamics (UAD)

**Source:** Huiwen Han, *Unified Agent Dynamics: A Multi-Layer Socio-Technical
Framework for Enterprise AI Agents* (2026),
[doi:10.5281/zenodo.19822201](https://doi.org/10.5281/zenodo.19822201).

> Enterprise agents are not isolated tools. They are socio-technical actors whose
> cognitive, computational, and organizational dynamics interact.

## The three layers

UAD models an enterprise agent across three layers:

| Layer | What it covers | Questions it answers |
| --- | --- | --- |
| **Cognitive (LC)** | Goals, knowledge, reasoning, memory, context | What does the agent know and intend? |
| **Computational (LP)** | Models, tools, runtime, control, execution | How does the agent act? |
| **Organizational (LO)** | Roles, authority, incentives, governance, lifecycle | Who owns it, and under what rules? |

Most agent engineering focuses on LC and LP. UAD’s central claim is that the
organizational layer is not an external wrapper; it participates in the agent’s
dynamics.

## The dynamics equation

UAD proposes a canonical form:

```text
dF/dt = G_int(F) + G_env(F, E) + G_ctrl(F, C)
```

- `F` is the agent’s state.
- `G_int` is internal dynamics (reasoning, memory, planning).
- `G_env` is interaction with the environment `E`.
- `G_ctrl` is the governance/control term `C`.

The important move is that governance is a **term in the dynamics**, not an
afterthought applied after the agent has already acted.

## Three consequences

The paper derives three governance-relevant properties:

1. **A critical governance threshold.** Beyond a certain enforcement intensity
   `μc`, stronger control can destabilize behavior (a Hopf bifurcation). More
   control is not always more stable; control design matters.
2. **Stratification.** Heterogeneous enterprise multi-agent systems tend to
   self-organize into hierarchical layers that can be predicted from the
   interaction structure.
3. **A complexity ceiling.** Governance-enforced optimal control has a capacity
   limit; exceeding it is associated with governance failure.

Treat these as theoretical results from a simulation study, not as universal
constants. Their practical value is directional: governance has dynamics, and
complexity has limits.

## Five enterprise agent types

UAD distinguishes five types: **Agent as Application, Service, Employee,
Physical Twin, and Human Twin**. The types differ in autonomy, identity,
accountability, and failure consequences. See the
[agent taxonomy](agent-taxonomy.md) for the practical version.

## How it maps to AxisVela

| UAD layer | AxisVela examples |
| --- | --- |
| Cognitive | Mnemovela (memory), Gnosivela (grounding), Ontovela (world model), Orchadyn (planning) |
| Computational | PRAXO-CORE (loop and primitives), PRAXOVELA (runtime), Noetivela (inference), Limenora (tools) |
| Organizational | Enterprise Autonomy (composition), Symbivela (human control), Aegivela/NOMIVELA/EIDOVELA (authority), COORDIVELA (work coordination) |

The map is illustrative. A product can contribute to more than one layer.

## What to take away

- Do not design governance as a post-processing step.
- Model the organizational layer explicitly: roles, authority, lifecycle, and
  accountability.
- Expect non-linear effects: too little control is unsafe, but poorly designed
  control can also destabilize.
- Match the control regime to the agent type.
