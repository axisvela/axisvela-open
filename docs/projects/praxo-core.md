# PRAXO-CORE

**Repository:** [axisvela/praxo-core](https://github.com/axisvela/praxo-core) ·
**License:** MIT · **Language:** Go · **Layer:** Foundation

> The framework layer. A small, embeddable foundation for governed agents — not
> a product, and not tied to one runtime.

## The problem

Teams building agents repeatedly rebuild the same infrastructure: the agent
loop, provider abstraction, tool contracts, memory and event boundaries,
scheduling, policy hooks, sandboxing, checkpoints, and plugin plumbing.
Governance is usually bolted on after the first prototype, when the seams are
already hard to change.

PRAXO-CORE starts from the opposite direction: keep the loop small, make the
boundaries explicit, and leave product and provider decisions to the integrator.

## What it provides

- A governed agent loop with middleware, budgets, context compaction, and
  subagents.
- Primitives for models, tools, memory, events, scheduling, policy, sandboxing,
  checkpoints, retrieval, and a virtual filesystem.
- A runtime plugin plane with process and WASM hosts, plus a conformance kit.
- Optional adapters for OpenAI-compatible endpoints and MCP tool gateways.
- OpenTelemetry instrumentation, benchmarks, bilingual documentation, and a
  public API freeze inventory.

## Why it matters

- **MIT boundary.** Product runtimes can embed the framework without inheriting
  a copyleft obligation.
- **Provider-neutral.** The same interfaces can be backed by NOETIVELA, a
  product router, or a local model endpoint.
- **Governance is structural.** Policy, sandbox, checkpoints, and events are
  seams in the framework rather than afterthoughts in application code.

## How it fits

PRAXO-CORE is the foundation under [PRAXOVELA](praxovela.md) and a natural
starting point for external agents. Its seams connect to:

- [NOETIVELA](noetivela.md) for model and endpoint routing;
- [MNEMOVELA](mnemovela.md) for durable memory and retrieval;
- [HARMOVELA](harmovela.md) for asynchronous coordination events;
- [GNOSIVELA](gnosivela.md) for grounded retrieval;
- [AEGIVELA](aegivela.md) for policy decisions;
- [LIMENORA](limenora.md) for governed tools and external systems;
- [RHEOVELA](rheovela.md) for graph execution and durable processes.

Adapters are optional and product-owned. The framework does not import product
code.

## Start

- [Repository and quickstart](https://github.com/axisvela/praxo-core)
- [pkg.go.dev](https://pkg.go.dev/github.com/axisvela/praxo-core/v2)
- [Documentation site](https://axisvela.github.io/praxo-core/)
- [v2 migration guide](https://github.com/axisvela/praxo-core/blob/main/docs/v2-migration.md)
