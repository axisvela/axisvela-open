# AxisVela Open

**A public map of independent projects for governed autonomy.**

[English](README.md) | [中文](README.zh-CN.md)

**Documentation version:** [v0.1.0](https://github.com/axisvela/axisvela-open/releases/tag/v0.1.0)

AxisVela is an independent, open-source project family for people building and
operating agents, workflows, robots, digital twins, and the systems that connect
them. The projects share a design stance — contracts over a shared kernel,
evidence over assertions, and human control over blind automation — but each
product is independently versioned and can be used on its own.

This repository is the map, not a monorepo. It explains what each project is
for, the problem it solves, the value it provides, and how the pieces relate.

[Start here](docs/start-here.md) · [Products](docs/projects/index.md) ·
[Theory](docs/theory/index.md) · [Architecture](docs/architecture/index.md) ·
[Practice](docs/practice/index.md) · [Concepts](docs/concepts/index.md) ·
[Reference](docs/reference/index.md) · [Machine-readable index](projects.yaml)

[![Go Reference](https://pkg.go.dev/badge/github.com/axisvela/praxo-core/v2.svg)](https://pkg.go.dev/github.com/axisvela/praxo-core/v2)

## Start with the problem, not the product

| If you need to… | Start with |
| --- | --- |
| Build an agent loop you can govern and embed | [PRAXO-CORE](docs/projects/praxo-core.md) — MIT Go framework |
| Understand how the whole ecosystem fits together | [Enterprise Autonomy](docs/projects/enterprise-autonomy.md) — public introduction and runnable examples |
| Run a long-lived, recoverable business process | [RHEOVELA](docs/projects/rheovela.md) — durable workflow platform |
| Give agents verifiable identity and bounded authority | [EIDOVELA](docs/projects/eidovela.md), [NOMIVELA](docs/projects/nomivela.md), [AEGIVELA](docs/projects/aegivela.md) |
| Connect agents to APIs, MCP servers, and events without bypassing policy | [LIMENORA](docs/projects/limenora.md) — governed integration gateway |
| Design and validate enterprise architecture with AI assistants | [TAXOVELA](docs/projects/taxovela.md) — architecture skill pack and CLI |

## What “governed autonomy” means here

Governed autonomy is not a model feature. It is an operating discipline built
from three questions:

1. **What is allowed?** Capabilities, data, and side effects are bounded by
   explicit policy before execution.
2. **What actually happened?** Actions leave evidence: effect ledgers, traces,
   process history, simulation records, or verification results.
3. **Who decided?** High-risk steps have a named owner, an approval path, and a
   way to intervene, revoke, or recover.

Different projects answer these questions at different layers. The
[concepts section](docs/concepts/index.md) explains the ideas; the
[ecosystem map](docs/ecosystem-map.md) shows where each project sits.

## The map at a glance

| Layer | What it covers | Representative projects |
| --- | --- | --- |
| Design and standards | Architecture design, validation, and portfolio management | TAXOVELA, PAMP |
| Foundation | Agent framework, coordination protocol, development coordination | PRAXO-CORE, Harmovela, COORDIVELA |
| Runtime and cognition | Agent execution, memory, inference routing | PRAXOVELA, Mnemovela, Noetivela |
| Work and capabilities | Planning, capability governance, durable process | ORCHADYN, MODUREGIS, RHEOVELA |
| Trust and knowledge | Identity, registry, authorization, grounding, world models | EIDOVELA, NOMIVELA, AEGIVELA, GNOSIVELA, ONTOVELA |
| Boundary and assurance | Integration, verification, simulation, skill supply chain | LIMENORA, TEKMOVELA, PEIRAVELA, SYNDOVELA |
| Human and physical operations | Human oversight, robot fleet control | SYMBIVELA, KINETOVELA |
| Program | End-to-end composition and examples | Enterprise Autonomy |

The layers are a reading aid, not a dependency chain. Products integrate through
versioned contracts and can be adopted independently.

## Open surfaces and commercial editions

- **Fully open projects:** PRAXO-CORE (MIT), TAXOVELA (MIT), and the Harmovela
  protocol (Apache-2.0).
- **Open product surfaces:** most products publish an Apache-2.0 `*-open`
  repository containing contracts, SDKs, examples, and sometimes binaries. The
  runtime or enterprise edition may be developed separately.
- **Licenses vary:** always treat the `LICENSE` in the specific repository as
  authoritative. See [licenses](docs/reference/licenses.md) for the current map.

The practical consequence: you can evaluate the interfaces and build against
them without buying anything, but an open surface is not a promise that the
entire runtime is open source.

## Suggested reading order

| If you are… | Read |
| --- | --- |
| New to the ecosystem | [Start here](docs/start-here.md) → [Ecosystem map](docs/ecosystem-map.md) → [Products](docs/projects/index.md) |
| An architect | [Agent theory](docs/theory/index.md) → [Agent architecture](docs/architecture/index.md) → [Enterprise Autonomy](docs/projects/enterprise-autonomy.md) |
| A builder | [Build an agent](docs/practice/build-an-agent.md) → [Govern an agent](docs/practice/govern-an-agent.md) → [Durable process](docs/practice/durable-process.md) |
| A researcher | [Agent theory](docs/theory/index.md) → [Research map](docs/theory/research-map.md) → [Reading list](docs/reference/reading-list.md) |

## How this repository is organized

- [`docs/projects/`](docs/projects/index.md) — one page per project: problem,
  what it provides, why it matters, and how it fits.
- [`docs/theory/`](docs/theory/index.md) — the conceptual spine: UAD, DIKCA,
  intent/AOP, PPES, taxonomy, multi-agent dynamics, economics. It synthesizes
  Huiwen Han’s research program and links each page to the original source.
- [`docs/architecture/`](docs/architecture/index.md) — runtime, control planes,
  contracts, knowledge, evidence, deployment, and security.
- [`docs/practice/`](docs/practice/index.md) — step-by-step guides using AxisVela
  as the reference implementation.
- [`docs/concepts/`](docs/concepts/index.md) — the vocabulary and the deeper
  conceptual notes, including a comprehensive terminology section.
- [`docs/reference/`](docs/reference/index.md) — relationships, licenses, sources,
  standards, and FAQ.
- [`projects.yaml`](projects.yaml) — a machine-readable project index for
  tooling, catalogs, and AI agents.
- [`llms.txt`](llms.txt) — a compact index for AI-assisted discovery.

## Status

These projects are early stage. Public contracts are versioned, but APIs may
change between minor releases until a repository declares 1.0. Each project’s
`CHANGELOG.md`, `ROADMAP.md`, and release tags are the source of truth.

AxisVela is a solo-maintainer, independent project family — not a company. The
public repositories are the open surface; commercial and enterprise editions are
developed separately.

## Contributing, security, and license

- [Contributing](CONTRIBUTING.md) — documentation fixes, project proposals, and
  the boundary between this repo and product repos.
- [Security](SECURITY.md) — report vulnerabilities privately.
- [Code of Conduct](CODE_OF_CONDUCT.md).
- Documentation and examples in this repository are licensed under Apache-2.0.
  Product repositories carry their own licenses.
