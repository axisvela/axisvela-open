# SYNDOVELA

**Repository:** [axisvela/SYNDOVELA-open](https://github.com/axisvela/SYNDOVELA-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Boundary and assurance

> Governance for how agent skills are composed, signed, and consumed across
> runtimes.

## The problem

Agent skills are increasingly assembled from multiple sources and run in
different runtimes. Composition is convenient, but it creates a supply-chain
problem: what exactly is in this skill bundle, who signed it, what does it
depend on, and which runtime should be allowed to execute it?

SYNDOVELA treats skill composition as a governed supply chain.

## What it provides

- A model for agent-skill composition across runtimes.
- SDKs and contracts for producers and consumers.
- Signed release binaries.
- Examples and integration guidance.
- Supply-chain metadata for composed skills.

## Why it matters

- **Provenance for skills.** Consumers can see what a skill bundle contains.
- **Signing and verification.** Artifacts can be checked before use.
- **Cross-runtime governance.** Composition rules are not tied to one runtime.

## How it fits

SYNDOVELA is a supply-chain layer for skills governed by
[MODUREGIS](moduregis.md) and executed by agent runtimes such as
[PRAXOVELA](praxovela.md). It complements [TEKMOVELA](tekmovela.md) assurance by
covering the provenance of the artifacts under test.

## Start

- [Syndovela Open repository](https://github.com/axisvela/SYNDOVELA-open)
