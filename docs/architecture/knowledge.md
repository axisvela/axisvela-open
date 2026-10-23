# Knowledge and memory architecture

Agents need more than a context window. They need memory, grounded knowledge, and
a model of the world. These are different layers with different failure modes.

## Four layers

| Layer | Question | AxisVela examples |
| --- | --- | --- |
| **Context** | What is in front of the model right now? | Prompt assembly, retrieved passages, session state |
| **Memory** | What should persist across runs? | MNEMOVELA: typed records, branches, retrieval, forgetting |
| **Grounding** | What do terms and claims mean, and what evidence supports them? | GNOSIVELA: concepts, entities, assertions, conflicts, scoped views |
| **World model** | What is true about the operating environment, and when? | ONTOVELA: bitemporal state, assertions, twin snapshots |

A vector store is none of these by itself. It is an index. Memory, grounding,
and world models require structure, lifecycle, and provenance.

## Memory architecture

A useful memory design answers:

- **What is stored?** Episodic events, semantic facts, procedural knowledge,
  user preferences, decisions.
- **How is it addressed?** By identity, tenant, session, entity, time, or
  purpose.
- **How is it retrieved?** Keyword, vector, graph, recency, importance, or a
  combination.
- **How is it revised?** Append, branch, merge, supersede, forget.
- **How is it governed?** Retention, consent, access control, deletion.

MNEMOVELA’s design emphasizes typed records, Git-like branches, hybrid retrieval,
and governed forgetting. Those are architectural choices, not feature checkboxes.

## Grounding architecture

Grounding is the bridge between retrieval and meaning:

- concepts have definitions;
- entities have stable identities;
- claims carry evidence;
- conflicts are explicit;
- views are scoped to a purpose.

GNOSIVELA calls the output a **grounding view**. The important property is that a
consumer can see not just the context, but why it should trust it.

## World-model architecture

An operational world model must be temporal and evidence-bearing:

- **valid time** — when something was true;
- **recorded time** — when the system learned it;
- **assertions** — who claimed it, with what evidence;
- **snapshots and changes** — what the state was at a point in time.

ONTOVELA provides this layer for twins and operational state. PEIRAVELA uses
world models as the starting point for simulation.

## Design rules

1. **Separate context from memory.** A long prompt is not durable memory.
2. **Separate memory from knowledge.** Remembering a claim is not the same as
   grounding it.
3. **Separate knowledge from world state.** A definition is not an observation.
4. **Carry provenance.** Every retrieved item should be traceable.
5. **Make freshness explicit.** Stale context is a silent failure.
6. **Govern deletion.** Forgetting is a requirement, not an edge case.
7. **Scope by purpose.** A planner, a support agent, and an auditor may need
   different views of the same knowledge.

## Anti-patterns

- “We put everything in a vector database.” That is an index, not an architecture.
- “The model will figure out the definitions.” It will guess.
- “The latest row is the truth.” It may be the latest belief, not the truth.
- “We never delete anything.” That is a compliance and quality problem.

## What to take away

- Context, memory, grounding, and world state are distinct layers.
- Provenance and lifecycle are part of the architecture.
- Retrieval quality is necessary but not sufficient; grounding and temporality
  are what make knowledge usable for decisions.
