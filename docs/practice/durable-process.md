# Run a durable process

Long-running work needs more than a loop. It needs a plan, governed
capabilities, durable execution, human decisions, and evidence. This guide shows
the pattern used by the AxisVela examples.

## The chain

```text
Goal → ORCHADYN plan → MODUREGIS capabilities
     → RHEOVELA process → SYMBIVELA approvals → TEKMOVELA verification
```

Each step is optional, but the boundaries matter.

## 1. Define the goal and acceptance criteria

State the outcome, the constraints, and what would count as success. Do not start
with a workflow diagram. Start with the decision and the evidence.

## 2. Compile a plan

Use [ORCHADYN](../projects/orchadyn.md) to turn goals, state, capabilities, and
constraints into a structured, revisable plan.

A useful plan is:

- explicit about steps and dependencies;
- constrained by available capabilities;
- verifiable;
- revisable when assumptions change.

## 3. Govern the capabilities

Check the plan against [MODUREGIS](../projects/moduregis.md):

- does each capability exist?
- who may invoke it?
- under which policy?
- what evidence will the invocation produce?

Do not let the plan invent capabilities that are not in the catalog.

## 4. Execute durably

Use [RHEOVELA](../projects/rheovela.md) for long-running or failure-prone work.
It provides:

- event-sourced process instances;
- deterministic, idempotent commands;
- recovery;
- a recorded history.

A process should survive a crash without repeating side effects.

## 5. Insert human decisions

Route approvals, exceptions, and interventions through
[SYMBIVELA](../projects/symbivela.md) or an equivalent control.

A good approval shows:

- the step and its risk;
- the plan context;
- the evidence so far;
- the consequences of approval and denial;
- the accountable person.

## 6. Verify the outcome

Use [TEKMOVELA](../projects/tekmovela.md) to check the outcome against the
acceptance criteria. Verification should be based on evidence, not on the
process’s self-report.

## A worked pattern: order exception

A typical order-fulfillment exception:

1. An order cannot be fulfilled as planned.
2. ORCHADYN produces a revised plan (substitute, split shipment, refund).
3. MODUREGIS checks the allowed capabilities and policy.
4. RHEOVELA starts a process instance and records the exception.
5. SYMBIVELA asks a human to approve the refund or substitution.
6. LIMENORA calls the external fulfillment system through the governed gateway.
7. TEKMOVELA verifies the outcome and closes the loop with evidence.

See the runnable examples in
[Enterprise Autonomy](https://github.com/axisvela/enterprise-autonomy/tree/main/examples).

## Recovery checklist

- [ ] The process can resume after a crash.
- [ ] Commands are idempotent.
- [ ] External effects are recorded.
- [ ] A failed step has a compensation or escalation path.
- [ ] Human approvals survive a restart.
- [ ] The final outcome is verified.

## Anti-patterns

- A workflow engine used as a message bus.
- A plan that ignores capability boundaries.
- Approvals that are not connected to the execution path.
- Retrying a side effect without an idempotency key.
- Treating the process history as optional.

## Next

- [Connect external systems](connect-external-systems.md) — the boundary.
- [Verify and simulate](verify-and-simulate.md) — evidence before release.
