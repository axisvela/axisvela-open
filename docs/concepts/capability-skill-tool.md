# Capability, skill, and tool

These words are often used interchangeably. In a governed system, they are
different layers with different owners and controls.

| Term | What it is | Governance question |
| --- | --- | --- |
| **Tool** | A callable function or API exposed to a model | Is the input schema safe? What is the blast radius? |
| **Capability** | A governed unit of action with identity, policy, and audit | Who may invoke it, under which conditions? |
| **Skill** | A packaged procedure or knowledge artifact that an agent can use | Where did it come from, and what does it contain? |
| **Agent** | An actor that plans and composes capabilities toward a goal | Who is accountable for its decisions? |

## The distinctions matter

- A tool without a capability wrapper is an ungoverned action.
- A capability without a skill may be too low-level for reliable use.
- A skill without provenance is a supply-chain risk.
- An agent without a capability catalog is guessing at what it can do.

## A layered model

```text
Agent
  └─ Skill (procedure / knowledge)
       └─ Capability (governed action)
            └─ Tool (implementation)
```

The layers are not mandatory, but they clarify ownership:

- the tool owner controls the implementation;
- the capability owner controls policy and audit;
- the skill author controls the procedure and its dependencies;
- the agent owner controls the goal and the plan.

## Governance implications

- **Tools** need input validation, sandboxing, and rate limits.
- **Capabilities** need a catalog, policy, and invocation audit.
- **Skills** need signing, provenance, and versioning.
- **Agents** need identity, authority, lifecycle, and evidence.

## Common confusions

- “The model can call any function” — that is a tool surface, not a capability
  model.
- “The skill is just a prompt” — then it has no provenance and no enforceable
  behavior.
- “The capability is just an API” — then it has no policy or audit.

## Related

- [MODUREGIS](../projects/moduregis.md) — capability control plane.
- [SYNDOVELA](../projects/syndovela.md) — skill composition and supply chain.
- [Contracts and interfaces](../architecture/contracts.md).
