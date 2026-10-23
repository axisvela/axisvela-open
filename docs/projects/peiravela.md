# PEIRAVELA

**Repository:** [axisvela/peiravela-open](https://github.com/axisvela/peiravela-open) ·
**License:** Apache-2.0 · **Language:** TypeScript and Go · **Layer:** Boundary and assurance

> A possible-world experiment control plane: try high-risk autonomy changes in
> simulation before they reach production.

## The problem

Some changes are too risky to test directly: a new policy, a different model, a
robot behavior, a recovery strategy. Running them in production is not an
experiment; it is an incident waiting to happen. Ad-hoc simulations usually
produce results that cannot be reproduced or compared.

PEIRAVELA treats simulation as a governed experiment with provenance.

## What it provides

- Governed simulation worlds.
- Reproducible scenario × perturbation × control × seed matrices.
- Provenance-complete simulation evidence.
- Independent verification of results.
- An embedded Studio UI and HTTP API.
- Control-plane CLI and client generation.

## Why it matters

- **Safe exploration.** High-risk changes can be evaluated before deployment.
- **Comparable results.** The same matrix produces comparable runs.
- **Evidence, not screenshots.** Claims about simulation outcomes carry
  provenance.

## How it fits

PEIRAVELA consumes world models from [ONTOVELA](ontovela.md) and knowledge from
[GNOSIVELA](gnosivela.md). Its evidence feeds [TEKMOVELA](tekmovela.md) release
gates and informs [KINETOVELA](kinetovela.md) mission design.

## Start

- [Peiravela Open repository](https://github.com/axisvela/peiravela-open)
