# Agent taxonomy

“Agent” is an overloaded word. For governance and architecture, it helps to
distinguish five enterprise types.

| Type | What it is | Failure that matters most |
| --- | --- | --- |
| **Application** | A user-facing agent inside a product | Wrong output, data leakage |
| **Service** | A long-running service called by other systems | Availability, cost, uncontrolled egress |
| **Employee** | An agent with a role and delegated authority | Over-delegation, accountability gaps |
| **Physical Twin** | An agent controlling or mirroring a physical asset | Safety, irreversible effects |
| **Human Twin** | A model of a person’s context or authority | Misrepresentation, privacy, consent |

These types are not a maturity ladder. A system can contain several at once, and
an agent can change type as its authority or embodiment changes.

## Why classify

The type determines the control emphasis:

- **Application:** sandboxing, user consent, output evidence.
- **Service:** workload identity, rate/cost policy, integration boundary.
- **Employee:** registry, authority bindings, approvals, performance review.
- **Physical Twin:** simulation, bounded missions, human override, recovery.
- **Human Twin:** consent, scope, revocation, provenance.

Classifying an agent as “just an app” when it has delegated authority and
external egress is a governance error.

## Lifecycle

Every agent needs a lifecycle: proposed, registered, activated, operated,
suspended, revoked, retired. The exact names matter less than the transitions:
who can perform them, what evidence they produce, and what happens to the
agent’s data and authority afterward.

## Related

- [Enterprise agent taxonomy](../theory/agent-taxonomy.md)
- [Agent identity](agent-identity.md)
- [Governed autonomy](governed-autonomy.md)
