# Reliability and failure

Agents fail differently from deterministic services. The model is
non-deterministic, tools fail partially, context can be lost, and a retry can
duplicate a side effect. Reliability is an architectural property, not a retry
setting.

## Failure domains

| Domain | Example failure | Control |
| --- | --- | --- |
| Model | Timeout, rate limit, changed behavior | Routing, timeouts, fallback, re-verification |
| Tool | Partial failure, bad response | Validation, idempotency, compensation |
| Context | Missing or stale context | Provenance, freshness, context checks |
| Process | Crash, restart, lost state | Durable process, checkpoints |
| Coordination | Duplicate or conflicting work | Leases, claims, idempotency |
| Human | Approval bottleneck, missed escalation | Queues, SLAs, escalation paths |
| Economy | Runaway cost | Budgets, step limits, routing |

## Core concepts

- **Idempotency.** Repeating a command should not repeat its effect.
- **Durability.** State survives a process or device failure.
- **Recovery.** The system resumes from recorded state.
- **Compensation.** A completed step can be undone or offset.
- **Timeout.** A slow dependency does not hang the system forever.
- **Backoff.** Retries do not amplify an outage.
- **Circuit breaking.** A failing dependency is isolated.
- **Checkpoint.** A run can resume without replaying everything.
- **Budget.** The agent cannot spend or act without bound.

## Agent-specific failure modes

- **Non-deterministic retries.** The retry produces a different plan or output.
- **Effect duplication.** A tool call is repeated after a crash.
- **Context drift.** The agent loses the goal or constraints across steps.
- **Tool cascades.** One failed tool causes a sequence of compensating calls.
- **Approval deadlock.** A process waits forever for a human.
- **Cost runaway.** The agent loops or calls expensive models without a bound.

## A reliability checklist

- [ ] Every external effect has an idempotency key.
- [ ] Long-running work is durable.
- [ ] Recovery is tested, not assumed.
- [ ] Timeouts and backoff are configured.
- [ ] Compensation exists for irreversible steps.
- [ ] Budgets and step limits are enforced.
- [ ] Approval paths have escalation and expiry.
- [ ] Evidence survives the failure.

## The difference from “it works”

A demo shows the happy path. Reliability is about the unhappy paths:

- the tool times out;
- the model returns malformed output;
- the process restarts;
- the human does not answer;
- the external system is down;
- the evidence store is unavailable.

Design for those, and the happy path takes care of itself.

## Related

- [Durable process](../practice/durable-process.md)
- [PPES](../theory/ppes.md) — probabilistic execution.
- [Evidence architecture](../architecture/evidence.md)
