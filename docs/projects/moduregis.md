# MODUREGIS

**Repository:** [axisvela/moduregis-open](https://github.com/axisvela/moduregis-open) ·
**License:** Apache-2.0 · **Language:** TypeScript and Go · **Layer:** Work and capabilities

> An enterprise capability control plane: publish, discover, govern, authorize,
> invoke, and audit what agents are allowed to do.

## The problem

Capabilities are scattered across APIs, scripts, tools, and agent skills. There
is often no single place to answer: what exists, who may use it, what it costs,
what happened when it ran, and whether it should still be available.

MODUREGIS makes capabilities a governed catalog rather than an implicit list of
functions.

## What it provides

- A capability registry with publishing and discovery.
- Governance metadata and lifecycle.
- Authorization and invocation controls.
- Audit records for invocations.
- A management console, HTTP API, and CLI.
- Import tooling for skills and related artifacts.

## Why it matters

- **One catalog.** Agents and humans discover capabilities from the same source
  of truth.
- **Policy at invocation.** Authorization is enforced where the capability is
  invoked, not only at design time.
- **Auditability.** Every invocation has a record.

## How it fits

MODUREGIS governs the capability layer used by [ORCHADYN](orchadyn.md) plans and
[RHEOVELA](rheovela.md) processes. It integrates with
[AEGIVELA](aegivela.md) for authorization and
[SYNDOVELA](syndovela.md) for skill supply-chain concerns.

## Start

- [Moduregis Open repository](https://github.com/axisvela/moduregis-open)
