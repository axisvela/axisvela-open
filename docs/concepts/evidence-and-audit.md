# Evidence and auditability

A log line says that something happened. Evidence lets you **reconstruct** what
happened, **verify** that it was allowed, and **defend** the decision later.

## Why logs are not enough

Logs are usually optimized for operators, not for proof. They may be incomplete,
mutable, missing context, or disconnected from the policy that authorized the
action. When a decision is challenged, “search the logs” is not an answer.

Evidence has four properties:

1. **Structured** — it records the action, inputs, decision, result, and
   identity in a known shape.
2. **Linked** — it connects the policy, the approval, the execution, and the
   outcome.
3. **Tamper-evident** — it can be checked for alteration or omission.
4. **Retained** — it survives the process that produced it.

## Evidence in the ecosystem

| Evidence | Produced by | Used for |
| --- | --- | --- |
| Effect ledger | [PRAXOVELA](../projects/praxovela.md) | Knowing what an agent actually did |
| Execution trace | [PRAXOVELA](../projects/praxovela.md) | Replay, diagnosis, and audit |
| Process history | [RHEOVELA](../projects/rheovela.md) | Recovering and auditing long-running work |
| Verification result | [TEKMOVELA](../projects/tekmovela.md) | Release gates and re-verification |
| Simulation evidence | [PEIRAVELA](../projects/peiravela.md) | Comparing possible worlds |
| Assertion and state history | [ONTOVELA](../projects/ontovela.md) | Knowing what was true, and when |
| Authorization decision | [AEGIVELA](../projects/aegivela.md) | Explaining allow/deny outcomes |
| Identity and lifecycle record | [EIDOVELA](../projects/eidovela.md), [NOMIVELA](../projects/nomivela.md) | Attributing actions to an agent |

## Evidence is not the same as observability

Observability asks “is the system healthy?” Evidence asks “can I prove what
happened and why?” A system can be highly observable and still have no audit
trail, and vice versa. Mature systems need both.

## A practical test

Pick a high-risk action. Try to answer, using only artifacts:

- Which agent acted?
- Under which identity and authority?
- Which policy allowed it?
- What exactly was invoked?
- What was the result?
- Who approved it, if anyone?
- Can the action be reversed or recovered?

If any answer requires a human memory or a mutable dashboard, the evidence model
is incomplete.
