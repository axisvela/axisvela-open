# TAXOVELA (ArchHarness)

**Repository:** [axisvela/TAXOVELA](https://github.com/axisvela/TAXOVELA) ·
**License:** MIT · **Language:** Python · **Layer:** Design and standards

> An AI-native architecture practice: requirements, design, diagrams,
> validation, and a deterministic gate.

## The problem

Enterprise architecture work is often a pile of documents and diagrams that
disagree with each other and cannot be checked. AI assistants can generate
architecture artifacts quickly, but speed without a gate produces confident,
unverifiable output.

TAXOVELA treats architecture as a pipeline with artifacts, hashes, and gates —
not as a chat transcript.

## What it provides

- A set of skills for Claude Code, OpenCode, Codex, GitHub Copilot, and Cursor:
  requirements, design, diagram generation, validation, security review,
  optimization, and reporting.
- A real CLI (`python -m archharness`) with a multi-project workspace.
- A workflow gatekeeper that enforces stage order and required artifacts.
- Hash-verified artifacts: a diagram cannot be edited underneath a recorded
  decision.
- Six-dimension diagram validation and a CI enforcement gate with
  PASS/WARN/BLOCK outcomes.
- Two renderers from one model: editable draw.io source and presentation-ready
  D2 output.

## Why it matters

- **Deterministic evidence.** The gate is reproducible; the output is not just
  “the model said it looked fine.”
- **Works with the tools people already use.** The same architecture practice
  runs across five AI coding assistants.
- **Designed for review.** Requirements, design, validation, security, and
  committee review are separate, inspectable stages.

## How it fits

TAXOVELA is design-time governance. It complements the runtime and control-plane
projects by making the architecture around them reviewable. It is adjacent to
[PAMP](pamp.md) (portfolio management) and is used with
[Enterprise Autonomy](enterprise-autonomy.md) reference architectures.

Related but separate: [`ea-harness`](https://github.com/axisvela/ea-harness) is
an earlier public architecture skill-pack repository. TAXOVELA is the current
AI-native project.

## Start

- [Repository and setup](https://github.com/axisvela/TAXOVELA)
- [Example gallery](https://github.com/axisvela/TAXOVELA/tree/main/examples)
- [Workflow standard](https://github.com/axisvela/TAXOVELA/blob/main/standards/workflow.yaml)
