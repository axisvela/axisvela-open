# Memory and context

A context window is a working set, not a memory system. This guide shows how to
combine context, durable memory, grounding, and world state without collapsing
them into one vector store.

## The four layers

| Layer | Store | Use it for |
| --- | --- | --- |
| Context | Runtime assembly | The current task, recent turns, retrieved passages |
| Memory | [MNEMOVELA](../projects/mnemovela.md) | Durable facts, decisions, episodes, preferences |
| Grounding | [GNOSIVELA](../projects/gnosivela.md) | Definitions, entity identity, claims, evidence, conflicts |
| World state | [ONTOVELA](../projects/ontovela.md) | Operational state, temporal assertions, twin snapshots |

## A context assembly pattern

For each step, assemble context in this order:

1. **Task intent** — the current goal and constraints.
2. **Session state** — what happened in this run.
3. **Durable memory** — relevant prior decisions and facts.
4. **Grounded knowledge** — definitions and evidence-backed claims.
5. **World state** — current and relevant historical state.
6. **Tool descriptions** — only the tools allowed for this step.

Then record which items were used. Context without provenance is hard to debug
and impossible to audit.

## Memory patterns

### Episode memory

Store what happened: decisions, outcomes, failures. Use it for learning and
continuity, not as a source of truth.

### Semantic memory

Store stable facts and preferences. Ground them when they are claims about the
world. Give them a source and a freshness policy.

### Procedural memory

Store reusable procedures and skills. Version them. Do not let a procedure
silently change behavior across runs.

### Working memory

Keep it in the session. Do not persist everything. Forgetting is a feature.

## Grounding pattern

Before using a claim in a decision:

- resolve the entities;
- check the definition;
- attach the evidence;
- check for conflicts;
- scope the view to the task and tenant.

GNOSIVELA’s grounding views are designed for this. If you skip grounding, the
model will fill gaps with plausible guesses.

## World-state pattern

For operational decisions, query state at a point in time:

- what is true now;
- what was true when the plan was made;
- what changed since;
- who asserted it.

ONTOVELA’s bitemporal model distinguishes valid time from recorded time. That is
what makes “the system believed X at time T” answerable.

## Anti-patterns

- **One vector store for everything.** It collapses four different layers.
- **Context without provenance.** You cannot explain why the agent used a fact.
- **Memory without forgetting.** Retention becomes a liability.
- **Grounding without conflicts.** Conflicting claims get averaged into
  nonsense.
- **World state as a dashboard snapshot.** It loses history and evidence.

## A checklist

- [ ] Context, memory, grounding, and world state are separate.
- [ ] Retrieved items carry a source.
- [ ] Memory has a retention and deletion policy.
- [ ] Claims are grounded and checked for conflicts.
- [ ] World state is temporal and evidence-bearing.
- [ ] The agent records which context it used.

## Next

- [Durable process](durable-process.md) — use memory and state in long-running
  work.
- [Knowledge architecture](../architecture/knowledge.md) — the architectural
  view.
