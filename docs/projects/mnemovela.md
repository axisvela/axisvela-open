# Mnemovela

**Repository:** [axisvela/mnemovela-open](https://github.com/axisvela/mnemovela-open) ·
**License:** Apache-2.0 · **Language:** Python and Go · **Layer:** Runtime and cognition

> A cognition runtime for agent memory: typed records, branch semantics, hybrid
> retrieval, and governed forgetting.

## The problem

“Add a vector database” is not a memory design. Agents need to remember facts,
decisions, and context over time; to revise or branch what they know; to forget
on purpose; and to explain why a memory was retrieved. An opaque embedding store
gives none of that.

Mnemovela treats memory as a versioned, inspectable runtime.

## What it provides

- Typed cognitive memory records.
- Git-like commit and branch semantics for memory state.
- Hybrid retrieval across structured and semantic signals.
- Governed forgetting and retention policies.
- Embedded-first operation in Python and Go.
- Language-neutral interfaces: REST, gRPC, JSON-RPC, and MCP.
- Replaceable storage backends, from embedded stores to PostgreSQL in the
  enterprise edition.

## Why it matters

- **Memory you can audit.** Branches and commits make it possible to see how
  knowledge changed.
- **Memory you can govern.** Retention and forgetting are first-class, not an
  afterthought.
- **Embedded or served.** The same runtime can live inside an agent or run as a
  service.

## How it fits

Mnemovela fills the memory and retrieval seam in [PRAXO-CORE](praxo-core.md). It
provides durable context for [PRAXOVELA](praxovela.md) and can be grounded by
[GNOSIVELA](gnosivela.md) concepts and evidence.

## Start

- [Mnemovela Open repository](https://github.com/axisvela/mnemovela-open)
