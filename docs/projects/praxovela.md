# PRAXOVELA

**Open surface:** [axisvela/praxovela-open](https://github.com/axisvela/praxovela-open) ·
**License:** Apache-2.0 (public surface) · **Language:** Go, Tauri desktop · **Layer:** Runtime and cognition

> A governable, local-first desktop agent runtime. Deny by default, sandbox
> first, everything audited.

## The problem

A local agent that can read files, call tools, and run commands is useful. It is
also a security boundary problem. Most agent runtimes grant broad permissions,
keep weak records of what happened, and recover poorly from crashes.

PRAXOVELA is built around the opposite defaults: capability use is explicit,
effects are recorded, execution is sandboxed, and a failed run can be recovered
rather than repeated blindly.

## What it provides

- A deny-by-default capability gate for tools and side effects.
- An effect ledger with crash recovery.
- A durable, replayable execution trace.
- Sandbox-first execution.
- Checkpoint and resume support.
- HTTP API, embedded MCP gateway, and a Tauri desktop application.

## Why it matters

- **Local control.** The runtime is designed for local-first execution rather
  than a remote service that owns the agent.
- **Evidence of effects.** The ledger records what the agent actually did, not
  just what it intended.
- **Recoverability.** A crash does not force a full replay of side-effecting
  work.

## How it fits

PRAXOVELA is the product runtime built on [PRAXO-CORE](praxo-core.md). It can use
[MNEMOVELA](mnemovela.md) for memory, [NOETIVELA](noetivela.md) for model
routing, [LIMENORA](limenora.md) for external tools, and
[AEGIVELA](aegivela.md) for authorization.

The `-open` repository is the integration surface. The runtime core and
enterprise edition are developed separately; check the repository for current
availability.

## Start

- [PRAXOVELA Open repository](https://github.com/axisvela/praxovela-open)
