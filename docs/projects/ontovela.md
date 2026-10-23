# ONTOVELA

**Repository:** [axisvela/ontovela-open](https://github.com/axisvela/ontovela-open) ·
**License:** See repository · **Language:** Go · **Layer:** Trust and knowledge

> An evidence-bearing, bitemporal operational world model and digital twin.

## The problem

Dashboards show a snapshot. Decisions need more: what is true now, what was true
then, when did it change, and what evidence supports the claim? Operational
state is usually scattered across systems, with no shared, auditable model.

ONTOVELA provides a shared world model that agents, planners, and people can
reason over without pretending that the latest row is the whole truth.

## What it provides

- Tenant-scoped operational world models.
- Evidence-bearing assertions.
- Bitemporal state: valid time and recorded time.
- Twin state, snapshots, and change history.
- HTTP APIs and SDKs.
- A model that can be consumed by planners, agents, and simulations.

## Why it matters

- **Time-aware truth.** “What did we believe, and when?” is answerable.
- **Evidence attached.** State is not just a value; it has provenance.
- **Shared context.** Multiple systems can reason over the same model rather
  than reconciling divergent copies.

## How it fits

ONTOVELA consumes concepts and evidence from [GNOSIVELA](gnosivela.md) and
provides operational context to [ORCHADYN](orchadyn.md),
[PEIRAVELA](peiravela.md), [TEKMOVELA](tekmovela.md), and
[KINETOVELA](kinetovela.md).

The public repository is the developer platform surface; check the repository
for current license and availability.

## Start

- [Ontovela Open repository](https://github.com/axisvela/ontovela-open)
