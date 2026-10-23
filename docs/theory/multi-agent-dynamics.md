# Multi-agent dynamics

A multi-agent system is not “one agent, repeated.” Adding agents changes the
failure modes: coordination cost, shared state, conflicting authority, emergent
behavior, and organizational structure all become first-class problems.

## What changes at scale

| Single agent | Multi-agent system |
| --- | --- |
| One context and one plan | Shared state and divergent context |
| One authority boundary | Delegation chains and conflicting permissions |
| One failure domain | Partial failure and recovery across agents |
| One trace | Correlated traces and causal attribution |
| One lifecycle | Roles, handoffs, leases, and retirement |

UAD’s organizational layer is the relevant lens: agents form roles, authority
relations, and interaction structures. The paper’s stratification result suggests
that heterogeneous systems tend to organize into hierarchical layers predictable
from the interaction matrix. Treat that as a design signal, not a law of nature.

## Coordination dimensions

Harmovela defines seven dimensions that a multi-agent coordination layer must
address:

1. **Event** — what happened.
2. **Task** — what is executing and in which state.
3. **State** — what is true now, and how it changes.
4. **Context / memory** — what informs decisions.
5. **Delegation** — who does what, with which authority.
6. **Recovery** — what happens when something fails.
7. **Governance** — who may do what, and what evidence remains.

Most multi-agent failures are a missing answer to one of these dimensions, not a
model-quality problem.

## Common failure modes

- **Duplicate work.** Two agents claim the same task because there is no lease or
  ownership model.
- **State divergence.** Agents hold incompatible views of the world and act on
  both.
- **Runaway delegation.** Authority expands as it passes between agents, or a
  loop of agents delegates to each other.
- **Coordination overhead.** The system spends more effort coordinating than
  doing.
- **Emergent escalation.** Local rules produce a global behavior nobody
  designed.
- **Attribution loss.** When something goes wrong, no one can reconstruct which
  agent did what under which authority.
- **Complexity ceiling.** The governance load grows faster than the system’s
  capacity to enforce it.

## Design rules

1. **Name roles and responsibilities.** Do not rely on emergent division of
   labor.
2. **Use leases and claims.** Ownership should expire and be observable.
3. **Share state through a protocol, not side channels.** Harmovela or an
   equivalent coordination layer.
4. **Bound delegation.** Authority should attenuate as it moves; see
   [AEGIVELA](../projects/aegivela.md).
5. **Make handoffs explicit.** A handoff is a state transition with an owner and
   evidence.
6. **Design for partial failure.** Recovery is a coordination dimension, not an
   afterthought.
7. **Watch the governance threshold.** More control can destabilize if it is
   poorly designed; measure the effect.
8. **Keep an attribution trail.** Correlated traces and identity are mandatory.

## How it maps to AxisVela

- [HARMOVELA](../projects/harmovela.md) — protocol for the seven coordination
  dimensions.
- [COORDIVELA](../projects/coordivela.md) — coordination of development work:
  leases, dependencies, conflicts, interventions.
- [RHEOVELA](../projects/rheovela.md) — durable process execution and recovery.
- [SYMBIVELA](../projects/symbivela.md) — human oversight of multi-agent work.
- [NOMIVELA](../projects/nomivela.md) and
  [AEGIVELA](../projects/aegivela.md) — identity and bounded authority across
  agents.

## What to take away

- Multi-agent design is organizational design.
- Coordination must be explicit, observable, and recoverable.
- Delegation without attenuation is a security bug.
- Measure coordination cost and governance load, not just task throughput.
