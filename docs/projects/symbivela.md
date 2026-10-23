# SYMBIVELA

**Repository:** [axisvela/symbivela-open](https://github.com/axisvela/symbivela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Human and physical operations

> A human-agent collaboration workspace for goals, plan review, approvals,
> exceptions, intervention, outcomes, and evidence.

## The problem

“Human in the loop” often means a notification and a yes/no button. Real
oversight needs context: what is the goal, what is the machine planning, what
changed, what is at risk, who owns the decision, and what happened afterward.

SYMBIVELA makes human oversight a first-class workspace rather than a modal
dialog.

## What it provides

- Goal setting and shared context.
- Plan review before execution.
- Approvals for high-risk actions.
- Exception queues and intervention.
- Handoffs between humans and agents.
- Outcome acceptance and evidence inspection.
- A web API and collaboration frontend.

## Why it matters

- **Human sovereignty.** People can intervene without managing every step.
- **Accountable decisions.** Approvals and interventions are recorded.
- **Exceptions are normal.** The workspace is designed for the cases that do not
  fit the happy path.

## How it fits

SYMBIVELA is the human-control layer for [RHEOVELA](rheovela.md) processes,
[MODUREGIS](moduregis.md) capabilities, and agent runs in
[PRAXOVELA](praxovela.md). It consumes evidence from
[TEKMOVELA](tekmovela.md) and identity from [AEGIVELA](aegivela.md).

## Start

- [Symbivela Open repository](https://github.com/axisvela/symbivela-open)
