# Autonomy and architecture

**Sources:** Huiwen Han, *DIKCA* (AI and Ethics, 2026),
[doi:10.1007/s43681-026-01256-3](https://doi.org/10.1007/s43681-026-01256-3);
*Architecture as Law* (2026),
[doi:10.5281/zenodo.19822511](https://doi.org/10.5281/zenodo.19822511).

> Autonomy is not the absence of control. It is the capacity to modify one’s own
> control structures under architectural bounds.

## A practical autonomy ladder

The following ladder is a **synthesis for design discussions**, not a standard
from the cited papers. It is useful for choosing controls.

| Level | What the system may do | Minimum control |
| --- | --- | --- |
| **Assisted** | Suggest actions; a human executes | Review, logging |
| **Supervised** | Execute low-risk steps; a human approves high-risk steps | Policy, approvals, evidence |
| **Delegated** | Execute a bounded task with delegated authority | Identity, scope attenuation, revocation |
| **Bounded autonomous** | Plan and execute within a defined envelope | Sandbox, budgets, recovery, audit |
| **Meta-control** | Modify its own policies, capabilities, or plans within architecture | Change control, separation of duties, re-verification |

Most enterprise systems should aim for supervised or delegated autonomy first.
Bounded autonomy is appropriate only when the envelope is enforced, not merely
described. Meta-control is a governance capability, not a feature to enable by
default.

## Architecture as law

The core claim is that architecture is constitutive: it determines which
configurations are possible, which controls are enforceable, and which evidence
can be produced. A system without architectonic specification is not just
incomplete; it is ungovernable in principle.

This has a direct design consequence:

- A policy that is not enforceable at an architectural boundary is advice.
- An approval that is not connected to an execution path is theater.
- An evidence claim that is not produced by the architecture is a narrative.

## Human sovereignty

Autonomy is bounded by the right and ability of humans to:

- know what the agent is about to do;
- approve, deny, or modify high-risk actions;
- intervene during execution;
- revoke authority;
- inspect evidence afterward;
- change the architecture that grants autonomy.

These are not UX features. They are control-plane requirements.

## How it maps to AxisVela

| Autonomy concern | AxisVela pattern |
| --- | --- |
| Bounded action | PRAXOVELA capability gate, PRAXO-CORE policy and sandbox |
| Delegated authority | EIDOVELA identity, NOMIVELA bindings, AEGIVELA attenuation |
| Approval and intervention | SYMBIVELA |
| Recovery | RHEOVELA, PRAXOVELA checkpoints |
| Re-verification after change | TEKMOVELA, PEIRAVELA |
| Architectural change control | Contract versioning, open surfaces, release gates |

## A checklist

Before increasing autonomy, ask:

1. What is the envelope, and where is it enforced?
2. What can the agent change about itself?
3. Who can revoke authority, and how quickly?
4. What evidence proves the envelope held?
5. What happens when the agent is wrong?
6. Can a human intervene without stopping the whole system?
7. Has the new autonomy level been verified and simulated?

If these questions do not have architectural answers, the autonomy level is not
ready.
