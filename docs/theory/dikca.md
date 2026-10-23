# DIKCA: data, information, knowledge, control, architecture

**Sources:** Huiwen Han, *Intelligence beyond knowledge: control, architecture,
and the structural law of artificial agency* (AI and Ethics, 2026),
[doi:10.1007/s43681-026-01256-3](https://doi.org/10.1007/s43681-026-01256-3);
*Architecture as Law* (2026),
[doi:10.5281/zenodo.19822511](https://doi.org/10.5281/zenodo.19822511).

> Knowledge tells you what is the case. Control tells you what may be done.
> Architecture determines what can be governed at all.

## From DIKW to DIKCA

The classical DIKW hierarchy — Data, Information, Knowledge, Wisdom — describes
epistemic ascent. DIKCA adds two layers that are not epistemic:

| Layer | Role |
| --- | --- |
| **Data** | Raw symbols or observations. |
| **Information** | Data made meaningful relative to an observer and context. |
| **Knowledge** | Claims about what is the case, with justification. |
| **Control** | Constraints on what may be done, and enforcement of those constraints. |
| **Architecture** | The constitutive structure that makes the other layers cohere as a governable system. |

**Autonomy** is then treated as *meta-control*: the capacity of a system to
modify its own control structures under architectural authorization.

## The category error

A recurring mistake is to treat governance as a kind of knowledge. A policy
document, a system prompt, or a safety instruction can *represent* a norm without
*enforcing* it. A model may know the rule and still violate it. Knowledge and
control are different logical types.

The practical consequence is blunt:

- If a constraint is only described, it is advice.
- If a constraint is enforced by an architecture, it is governance.

## Architecture as law

*Architecture as Law* argues that architecture is a constitutive condition for
governable AI. A system without an explicit architecture is not merely
technically incomplete; its behavior cannot be predicted, constrained, or
audited in a principled way.

Architecture is not the same as a diagram or a framework label. It is the set of
constraints that determines:

- which data structures are permissible;
- which information flows are valid;
- which knowledge claims can be represented;
- which control mechanisms can be enforced.

Autonomy without architectural bounds is not advanced intelligence; it is a
governance failure.

## How it maps to AxisVela

| DIKCA layer | AxisVela examples |
| --- | --- |
| Data / Information | Ingestion, events, assertions, traces |
| Knowledge | GNOSIVELA concepts and evidence; ONTOVELA world state; MNEMOVELA memory |
| Control | AEGIVELA policy, MODUREGIS capabilities, SYMBIVELA approvals, sandboxing |
| Architecture | Contract boundaries, runtime seams, evidence architecture, deployment topology |
| Autonomy (meta-control) | Bounded self-modification: policy change, capability registration, plan revision, agent lifecycle |

The ecosystem’s emphasis on contracts, evidence, and control planes is a direct
expression of this view: governance must be structural.

## What to take away

- Do not confuse a prompt with a policy.
- Make the control layer enforceable and inspectable.
- Treat architecture as a governance artifact, not only an engineering artifact.
- Define the conditions under which an agent may change its own controls.
