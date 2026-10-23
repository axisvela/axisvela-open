# Memory and context

Context is what the model sees now. Memory is what persists. Knowledge is what
is grounded. World state is what is true about the environment. These are
different problems.

## The layers

| Layer | Lifetime | Failure if conflated |
| --- | --- | --- |
| **Context** | One step or session | Prompt bloat, lost provenance |
| **Memory** | Across runs | Stale or ungoverned persistence |
| **Knowledge** | Across systems | Ungrounded claims, conflicting definitions |
| **World state** | Across time | Decisions based on the latest row, not the truth |

## Context engineering

A context window is a working set. Good context engineering asks:

- What is the minimum context needed for this step?
- Which items are authoritative, and which are hints?
- What is stale?
- What is untrusted?
- What will be recorded as used?

More context is not always better. Irrelevant or adversarial context can degrade
decisions and increase cost.

## Memory design

A memory system needs:

- a schema (episodic, semantic, procedural);
- addressing (tenant, session, entity, time);
- retrieval (keyword, vector, graph, recency);
- revision (append, branch, merge, forget);
- governance (retention, consent, deletion).

A vector index provides retrieval. It does not provide the rest.

## Grounding

Grounding attaches meaning and evidence to retrieved material:

- concept definitions;
- entity identity;
- claims with sources;
- conflict handling;
- purpose-scoped views.

Without grounding, retrieval gives plausible text, not usable knowledge.

## World state

For operational decisions, state must be temporal:

- valid time vs recorded time;
- assertions and evidence;
- snapshots and changes.

A dashboard shows a snapshot. A world model lets you ask what was true, when, and
why.

## Rules of thumb

1. Do not put durable memory in the prompt.
2. Do not put untrusted context in the control path.
3. Do not treat retrieval as grounding.
4. Do not treat the latest value as the truth.
5. Record what context was used.

## Related

- [Knowledge architecture](../architecture/knowledge.md)
- [Memory and context practice](../practice/memory-and-context.md)
- [World models](world-models.md)
