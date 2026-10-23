# Evidence architecture

Evidence is not a log dump. It is a structured, linked, tamper-evident, and
retained record that lets someone reconstruct and defend a decision. This page
describes how to design for it.

## The evidence chain

For a governed action, the chain usually looks like this:

```text
goal → plan → capability → policy decision → identity → execution effect
     → outcome → verification → human decision
```

Each link should be addressable. If a link is missing, the chain is a narrative,
not evidence.

| Link | Typical artifact | Source |
| --- | --- | --- |
| Goal | Intent record, acceptance criteria | Caller, TAXOVELA, ORCHADYN |
| Plan | Structured plan and revision history | ORCHADYN |
| Capability | Capability version and metadata | MODUREGIS |
| Policy | Allow/deny decision and policy version | AEGIVELA |
| Identity | Workload identity and authority scope | EIDOVELA, NOMIVELA |
| Execution | Effect record, inputs, result | PRAXOVELA, RHEOVELA |
| Outcome | Process state, output artifact | RHEOVELA, agent runtime |
| Verification | Test result, evidence bundle | TEKMOVELA |
| Human decision | Approval, exception, intervention | SYMBIVELA |

## Properties

1. **Structured.** A known schema, not free-text logs.
2. **Linked.** IDs connect the decision, action, and outcome.
3. **Tamper-evident.** Hashes, signatures, or an append-only store.
4. **Retained.** The evidence outlives the process and the runtime.
5. **Scoped.** Access control and tenant isolation apply to evidence too.

## Evidence vs observability

| Observability | Evidence |
| --- | --- |
| Answers “is it healthy?” | Answers “what happened and why?” |
| Optimized for operators | Optimized for reconstruction and audit |
| Often sampled | Must be complete for material actions |
| Short retention is common | Retention is a policy requirement |
| Metrics, logs, traces | Structured records, bundles, proofs |

You need both, but one does not substitute for the other.

## Storage patterns

- **Local ledger.** PRAXOVELA’s effect ledger for local-first agents.
- **Process history.** RHEOVELA’s event-sourced state for durable work.
- **Evidence bundles.** TEKMOVELA’s verification artifacts.
- **Simulation records.** PEIRAVELA’s provenance-complete experiment evidence.
- **World-state history.** ONTOVELA’s bitemporal assertions.
- **Security decisions.** AEGIVELA’s authorization evidence.

A central evidence store can aggregate these, but it should not rewrite them.
Preserve the source record and its provenance.

## Anti-patterns

- **“We have logs.”** Logs are optimized for debugging, not proof.
- **Mutable evidence.** If an operator can edit the record, it is not evidence.
- **Orphaned evidence.** An effect record without the policy decision or identity
  is incomplete.
- **Evidence without retention.** A record deleted after seven days cannot
  support a quarterly audit.
- **Evidence without access control.** Audit data is sensitive.

## A test

Pick a material action and try to answer these using only artifacts:

- What was the goal?
- Which plan and capability were used?
- Who authorized it, under which policy version?
- Which identity acted?
- What was the effect?
- What was the outcome?
- Who verified it?
- Who approved the high-risk step?

If any answer requires a person’s memory, the evidence architecture is
incomplete.

## What to take away

- Design evidence as part of the action, not after it.
- Link the chain; completeness matters more than volume.
- Separate observability from evidence.
- Treat retention and access control as first-class.
