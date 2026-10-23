# NOMIVELA

**Repository:** [axisvela/NOMIVELA-open](https://github.com/axisvela/NOMIVELA-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Trust and knowledge

> The agent registry and namespace authority: the system of record for agents,
> authority bindings, lifecycle epochs, and discovery.

## The problem

Agent identity is only useful if there is a trustworthy registry behind it. Who
owns this agent? Which namespace does it live in? What authority is bound to it?
Which lifecycle epoch is current? Without a system of record, answers live in
spreadsheets and deployment scripts.

NOMIVELA makes those questions queryable and evidence-bearing.

## What it provides

- Agent identity records and namespaces.
- Authority bindings.
- Lifecycle epochs for agent and identity state.
- Discovery APIs.
- Evidence for registration and lifecycle changes.
- API contracts, schemas, and SDKs for Go, Python, and Java.
- A CLI and conformance fixtures.

## Why it matters

- **One inventory.** Agents, namespaces, and bindings have a single source of
  truth.
- **Lifecycle correctness.** Epochs make rotation and re-registration explicit.
- **Auditability.** Registration and lifecycle changes leave evidence.

## How it fits

EIDOVELA issues identity; NOMIVELA records the agent and its bindings; AEGIVELA
authorizes actions. NOMIVELA is the middle plane that makes the other two
coherent across an enterprise.

## Start

- [Nomivela Open repository](https://github.com/axisvela/NOMIVELA-open)
