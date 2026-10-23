# Runtime architecture

An agent runtime is the place where intent becomes action. The runtime determines
what the agent can see, what it can do, how much it can do, what it records, and
how it recovers.

## The components

| Component | Responsibility | PRAXO-CORE seam |
| --- | --- | --- |
| **Loop** | Decide the next step and stop at a bound | `pkg/agent` |
| **Model** | Produce decisions and tool calls | `pkg/model` |
| **Tools** | Invoke capabilities with validated inputs | `pkg/tool`, `pkg/toolcall` |
| **Memory** | Assemble context and store durable state | `pkg/memory` |
| **Events** | Publish what happened | `pkg/event` |
| **Policy** | Authorize or deny actions | `pkg/policy` |
| **Sandbox** | Constrain execution | `pkg/sandbox` |
| **Checkpoint** | Resume without repeating effects | `pkg/checkpoint` |
| **Plugins** | Extend the runtime at a controlled boundary | `pkg/plugin` |
| **Scheduler** | Run recurring or delayed work | `pkg/scheduler` |

The exact package names are PRAXO-CORE’s; the responsibilities are general.

## The execution cycle

```text
observe → decide → authorize → act → record → evaluate → (repeat or stop)
```

- **Observe:** assemble context from the session, memory, tools, and events.
- **Decide:** call the model to choose a step or produce a final answer.
- **Authorize:** evaluate policy before the action, not after.
- **Act:** invoke the tool inside the sandbox, within budget and scope.
- **Record:** write the effect, inputs, decision, and result.
- **Evaluate:** check whether the goal is met or the loop should stop.

A runtime that omits authorization or recording is not a governed runtime; it is
a tool-calling loop.

## Runtime invariants

Good runtimes make the following invariants explicit:

1. **Deny by default.** No tool is available unless granted.
2. **Bounded steps.** The loop has a maximum step count and budget.
3. **Pre-action authorization.** Policy is checked before side effects.
4. **Effect evidence.** Every material action leaves a record.
5. **Recoverability.** A failed run can resume without blindly repeating
   effects.
6. **Context isolation.** Sessions, tenants, and workspaces are separated.
7. **Provider neutrality.** The model is an interface, not a hard-coded vendor.

## Local vs service runtimes

| Concern | Local-first runtime | Service runtime |
| --- | --- | --- |
| Trust boundary | The user’s machine | The service boundary |
| Identity | Local user + workload | Tenant + workload identity |
| Data | Local files and stores | Shared stores and queues |
| Failure | Process crash, device loss | Partial failure, network partition |
| Evidence | Local ledger and trace | Central evidence store |
| Best fit | Personal agents, desktop tools | Multi-user, long-running, governed work |

PRAXOVELA is a local-first design; RHEOVELA is a service-oriented durable
runtime. They can be combined.

## What to measure

- steps per task and cost per task;
- tool-error rate and policy-deny rate;
- recovery rate and time to recovery;
- context size and retrieval quality;
- evidence completeness;
- human intervention rate.

These are runtime health metrics, not model benchmarks.

## What to take away

- The loop is the easy part; the seams are the architecture.
- Put policy and sandboxing before action.
- Record effects as a first-class output.
- Design for recovery before you need it.
