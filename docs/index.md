# AxisVela Open documentation

This site is the public map of the AxisVela project family, plus the theory,
architecture, practice, and vocabulary needed to reason about agent systems.

## The six sections

| Section | What it is for |
| --- | --- |
| [Products & projects](projects/index.md) | What each project is, the problem it solves, and how it fits |
| [Agent theory](theory/index.md) | The conceptual spine: UAD, DIKCA, intent, PPES, taxonomy, multi-agent dynamics |
| [Agent architecture](architecture/index.md) | Runtime, control planes, contracts, knowledge, evidence, deployment, security |
| [Agent practice](practice/index.md) | Step-by-step guides using AxisVela as the reference implementation |
| [Concepts & terminology](concepts/index.md) | The vocabulary: agency, context, capability, identity, reliability, maturity |
| [Reference](reference/index.md) | Relationships, licenses, sources, standards, FAQ |

## Choose a path

| Path | Who it is for | Start |
| --- | --- | --- |
| **Build** | Developers who want to embed a governed agent loop or SDK | [Build an agent](practice/build-an-agent.md) |
| **Evaluate** | Architects and technical leads comparing the ecosystem | [Start here → Evaluate](start-here.md#evaluate) |
| **Operate** | Teams running workflows, approvals, and agent operations | [Start here → Operate](start-here.md#operate) |
| **Learn** | Readers who want the theory and vocabulary first | [Agent theory](theory/index.md) |
| **Design** | Architects designing a governed agent system | [Agent architecture](architecture/index.md) |

## Two indexes

- **Human index:** [Projects](projects/index.md) — one row per project, with the
  problem, the value, the layer, and the license.
- **Machine-readable index:**
  [`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml)
  — the same map in a format that catalogs, documentation tools, and AI agents
  can consume.

## A note on independence

The projects are independently versioned. This repository does not contain their
source code and does not override their documentation. If a product page and a
product repository disagree, the product repository wins. If a theory page and a
cited paper disagree, the paper wins.
