# Coordination vs orchestration

These terms are often used interchangeably. In distributed agent systems they
describe different problems — and mixing them produces architectures that are
hard to reason about.

## Three layers

| Layer | Question | Typical mechanism |
| --- | --- | --- |
| Capability invocation | “Can you do this now?” | MCP, HTTP API, tool call |
| Coordination | “What is happening across agents and time?” | Events, tasks, state, leases, delegation |
| Orchestration | “In what order should this durable process run?” | Workflow engine, state machine |

## Capability invocation

MCP is a good fit for synchronous capability calls: discover a tool, invoke it,
get a result. It is deliberately narrow. It does not define how a task survives
a restart, how state is shared, or how an agent delegates to another agent.

## Coordination

Coordination is about shared state over time: who is doing what, what changed,
what is stale, what is blocked, what needs recovery. Harmovela defines a
protocol for this with seven dimensions (event, task, state, context/memory,
delegation, recovery, governance).

Coordination does not prescribe a workflow. It gives independent participants a
shared vocabulary.

Project: [Harmovela](../projects/harmovela.md). For coordination of development
work itself, see [COORDIVELA](../projects/coordivela.md).

## Orchestration

Orchestration is about durable execution: a process with steps, retries,
compensation, recovery, and a recorded history. It is appropriate when the work
has a defined lifecycle and must survive failure.

Project: [RHEOVELA](../projects/rheovela.md).

## Choosing

- If the problem is “call this tool,” use a capability interface.
- If the problem is “several agents need to agree on what is happening,” use a
  coordination protocol.
- If the problem is “this process must run for days and recover,” use a durable
  workflow engine.

Many real systems need all three. The mistake is using a workflow engine as a
message bus, or a tool protocol as a coordination layer.
