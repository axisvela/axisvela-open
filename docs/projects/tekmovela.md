# TEKMOVELA

**Repository:** [axisvela/tekmovela-open](https://github.com/axisvela/tekmovela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Boundary and assurance

> Engineering assurance for autonomous systems: verification contracts,
> reproducible tests, and evidence-based release gates.

## The problem

Agent and autonomous-system behavior is hard to test. Runs are
non-deterministic, failures are hard to reproduce, and release decisions are
often based on anecdote. “It worked in the demo” is not assurance.

TEKMOVELA turns intent and acceptance criteria into verification contracts that
can be executed, diagnosed, and re-run.

## What it provides

- Verification contracts derived from intent and acceptance criteria.
- Governed test harnesses.
- Reproducible closed-loop testing.
- Trace-linked failure diagnosis.
- Release gates with evidence.
- Re-verification triggered by production behavior.
- SDKs and conformance fixtures.

## Why it matters

- **Evidence-based releases.** A gate decision points to artifacts, not opinion.
- **Reproducibility.** The same contract and seed produce the same run.
- **Continuous assurance.** Production signals can trigger re-verification.

## How it fits

TEKMOVELA verifies agents and runtimes such as [PRAXOVELA](praxovela.md),
processes in [RHEOVELA](rheovela.md), and missions in
[KINETOVELA](kinetovela.md). It consumes traces and evidence from the systems it
verifies and can use [PEIRAVELA](peiravela.md) for safe experimentation.

## Start

- [Tekmovela Open repository](https://github.com/axisvela/tekmovela-open)
