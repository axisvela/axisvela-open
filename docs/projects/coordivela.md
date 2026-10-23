# COORDIVELA

**Repository:** [axisvela/coordivela-open](https://github.com/axisvela/coordivela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Foundation

> A coordination control plane for humans and AI agents working on the same
> development work.

## The problem

When several agents and humans work in parallel, they duplicate effort, collide
on the same files or tasks, and lose track of who is waiting on whom. A chat
channel is not a coordination system. Neither is a task board without leases,
dependencies, or conflict handling.

COORDIVELA treats development work as state that must be coordinated
explicitly.

## What it provides

- Work state and ownership with leases.
- Dependencies and schedules across tasks.
- Conflict detection and structured interventions.
- A control plane that humans and agents both use.
- Public contracts, SDKs, examples, and approved core binaries.

## Why it matters

- **Less duplicate work.** Leases and claims make ownership visible before work
  starts.
- **Observable coordination.** Dependencies and interventions are data, not
  hallway conversations.
- **Agent-native.** The same control plane serves human teams and autonomous
  workers.

## How it fits

COORDIVELA coordinates the work of building and operating the ecosystem itself.
It complements [Harmovela](harmovela.md), which coordinates runtime events and
tasks, and [RHEOVELA](rheovela.md), which executes durable business processes.

## Start

- [COORDIVELA Open repository](https://github.com/axisvela/coordivela-open)
