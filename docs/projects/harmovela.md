# Harmovela

**Repository:** [axisvela/harmovela](https://github.com/axisvela/harmovela) ·
**Examples and ecosystem hub:** [harmovela-open](https://github.com/axisvela/harmovela-open) ·
**License:** Apache-2.0 · **Language:** Protocol, with TypeScript, Python, Go, and Java implementations · **Layer:** Foundation

> An open coordination protocol for autonomous systems. MCP calls a tool;
> Harmovela coordinates what happens over time.

## The problem

MCP is excellent at synchronous capability invocation: ask for a tool, get a
result. It does not define what happens when work spans minutes or days, when
several agents share state, when a task must be delegated or recovered, or when
governance must survive a restart.

Those are coordination problems, and without a shared protocol every system
invents its own incompatible version.

## What it provides

- Seven coordination dimensions: event, task, state, context/memory, delegation,
  recovery, and governance.
- Thirteen dimension modules and five infrastructure modules (harness, runtime,
  CLI, conformance, MCP bridge).
- Versioned specifications, JSON Schemas, and 34 conformance fixtures.
- Reference implementations in TypeScript, Python, Go, and Java.
- Seven transport bindings, including stdio, WebSocket, SSE, gRPC, NATS, Kafka,
  and Redis Streams.
- SQLite and PostgreSQL delivery stores with retry, dead-letter, replay, and
  cross-language conformance.

## Why it matters

- **Vendor-neutral coordination.** The protocol is not owned by one runtime.
- **Conformance is testable.** Multiple implementations are checked against the
  same fixtures.
- **Complements MCP rather than replacing it.** MCP remains the synchronous
  capability layer; Harmovela is the asynchronous coordination layer.

## How it fits

Harmovela is the event/coordination seam in [PRAXO-CORE](praxo-core.md) and a
natural companion to [COORDIVELA](coordivela.md) (development coordination) and
[RHEOVELA](rheovela.md) (durable process execution).

[harmovela-open](https://github.com/axisvela/harmovela-open) is the public
examples and ecosystem hub: runnable integrations, an ecosystem registry, and
authoring guides.

## Start

- [Protocol repository](https://github.com/axisvela/harmovela)
- [Examples and ecosystem](https://github.com/axisvela/harmovela-open)
- [Spec site](https://axisvela.github.io/harmovela/)
