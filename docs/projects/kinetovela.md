# KINETOVELA

**Repository:** [axisvela/kinetovela-open](https://github.com/axisvela/kinetovela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Human and physical operations

> A governed physical-autonomy control plane for safe, observable robot-fleet
> missions.

## The problem

Software autonomy can be stopped with a process restart. Physical autonomy
cannot. Robot fleets need bounded missions, observable state, safe recovery, and
a clear authority model before they can operate outside a lab.

KINETOVELA applies the ecosystem’s governance model to physical execution.

## What it provides

- Fleet and mission operations.
- Public contracts and SDKs.
- Adapter patterns for robot and edge systems.
- Observable mission state.
- Bounded, recoverable execution.
- Documentation and binary releases.

## Why it matters

- **Physical safety is a governance problem.** Permissions, state, and recovery
  must be explicit.
- **Observability.** A mission is not a black box.
- **Recoverability.** Failures are handled as state transitions, not surprises.

## How it fits

KINETOVELA consumes world state from [ONTOVELA](ontovela.md), plans from
[ORCHADYN](orchadyn.md), and verification from [TEKMOVELA](tekmovela.md). It can
be simulated in [PEIRAVELA](peiravela.md) before a mission is approved through
[SYMBIVELA](symbivela.md).

## Start

- [Kinetovela Open repository](https://github.com/axisvela/kinetovela-open)
