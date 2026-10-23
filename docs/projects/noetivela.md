# Noetivela

**Repository:** [axisvela/noetivela-open](https://github.com/axisvela/noetivela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Runtime and cognition

> An enterprise inference fabric: catalog models and endpoints, turn
> requirements into inference contracts, and route requests with evidence.

## The problem

An enterprise rarely has one model endpoint. It has cloud APIs, private models,
edge inference, regional constraints, cost targets, latency targets, and
quality differences. Hard-coding a provider into an agent makes all of that
rigid and invisible.

Noetivela makes inference a governed routing decision.

## What it provides

- A catalog of models and endpoints.
- Inference contracts derived from task requirements.
- Routing across cloud, private, and edge intelligence.
- Policy, quality, latency, and cost considerations in the decision.
- An OpenAI-compatible HTTP surface plus governed endpoints.
- CLI and Go, Python, and TypeScript SDKs.

## Why it matters

- **Avoid provider lock-in.** Agents call a contract, not a vendor SDK.
- **Make trade-offs explicit.** Cost, latency, quality, and sovereignty become
  routing inputs.
- **Keep an evidence trail.** Routing decisions can be inspected rather than
  guessed.

## How it fits

Noetivela fills the model seam in [PRAXO-CORE](praxo-core.md) and provides
inference for [PRAXOVELA](praxovela.md) and other agents. It is a natural
companion to [GNOSIVELA](gnosivela.md) for grounded context and
[TEKMOVELA](tekmovela.md) for evaluating model-dependent behavior.

## Start

- [Noetivela Open repository](https://github.com/axisvela/noetivela-open)
