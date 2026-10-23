# Observability

Observability asks whether the system is healthy. Evidence asks what happened and
why. Agent systems need both, but they are not the same.

## The three signals

| Signal | Question | Example |
| --- | --- | --- |
| **Metrics** | How much / how often? | Steps per task, tool error rate, cost per run |
| **Logs** | What did a component say? | A tool returned an error |
| **Traces** | How did the request flow? | Model → tool → gateway → external API |

These are optimized for operators. They may be sampled, short-lived, and
unstructured.

## Agent-specific signals

- steps per task and loop exits;
- tool calls by type and outcome;
- policy allows/denies and reasons;
- context size and retrieval quality;
- model and endpoint routing decisions;
- recovery events and time to recovery;
- human interventions and approvals;
- cost and token usage;
- evidence completeness.

## Observability vs evidence

| Observability | Evidence |
| --- | --- |
| Health and performance | Reconstruction and audit |
| Sampled is often fine | Complete for material actions |
| Short retention | Policy-based retention |
| Operator-facing | Auditor- and regulator-facing |

A trace can be evidence if it is structured, complete, linked, and retained. A
metric almost never is.

## Practical rules

1. **Correlate by IDs.** Session, run, trace, tenant, agent, capability.
2. **Do not log secrets or full sensitive payloads.**
3. **Separate operational logs from evidence records.**
4. **Sample high-volume telemetry, not material effects.**
5. **Alert on control-plane failures**, not just errors: policy service down,
   evidence store unavailable, approval backlog.
6. **Make the agent’s decisions visible**: step, tool, policy, outcome.

## A dashboard that matters

- runs started / completed / failed;
- policy deny rate and top reasons;
- tool error rate and latency;
- recovery rate;
- human intervention rate;
- cost per successful task;
- evidence gaps.

If the dashboard only shows model latency, it is not an agent operations
dashboard.

## Related

- [Evidence and auditability](evidence-and-audit.md)
- [Evidence architecture](../architecture/evidence.md)
- [Reliability](reliability.md)
