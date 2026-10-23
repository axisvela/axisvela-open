# Agency and control

**Agency** is the capacity to act toward a goal. **Autonomy** is the degree to
which an agent can choose and modify its actions without external intervention.
**Control** is the set of constraints that bound those actions.

The three are related but not identical. A system can be highly agentic and
tightly controlled (a well-governed agent), or weakly agentic and poorly
controlled (a script with broad credentials).

## Control is not knowledge

A policy can be written down, described in a prompt, or represented in a model’s
context. None of those *enforce* it. Enforcement requires an architectural
mechanism: a policy decision point, a sandbox, a capability allowlist, a gateway,
or an approval path.

This distinction is central to [DIKCA](../theory/dikca.md): knowledge answers
“what is the case,” control answers “what may be done.”

## Meta-control

Autonomy at the highest level is **meta-control**: the capacity to modify one’s
own control structures. An agent that can change its own policy, capabilities, or
plan is exercising meta-control.

Meta-control is not a feature to enable casually. It requires:

- an architecture that bounds what can be changed;
- separation of duties;
- change evidence;
- re-verification after the change;
- a way to revoke the change.

## A practical distinction

| Question | Concept |
| --- | --- |
| Can the system pursue a goal? | Agency |
| Can it choose its own steps? | Autonomy |
| What bounds those steps? | Control |
| Can it change the bounds? | Meta-control |
| Who is accountable? | Governance |

## Why it matters

- Calling a system “autonomous” without naming the bounds is marketing, not
  architecture.
- Adding control does not always increase safety; poorly designed control can
  destabilize behavior (see [UAD](../theory/uad.md)).
- The right question is not “how autonomous is it?” but “what can it do, what
  stops it, and what proves it?”

## Related

- [Autonomy and architecture](../theory/autonomy-architecture.md)
- [Governed autonomy](governed-autonomy.md)
- [Agent identity](agent-identity.md)
