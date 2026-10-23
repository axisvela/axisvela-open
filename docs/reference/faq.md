# FAQ

## Is AxisVela a company?

No. AxisVela is an independent, solo-maintainer project family. The public
repositories are the open surface; commercial and enterprise editions are
developed separately.

## What is the difference between “open source” and an “open surface”?

Open source means the implementation is in the repository under an open license.
An open surface means the repository publishes contracts, SDKs, examples, and
sometimes binaries, while the runtime core or enterprise edition may be
separate. See [Open surfaces](../concepts/open-surfaces.md).

## Where should I start?

- To build: [PRAXO-CORE](../projects/praxo-core.md).
- To evaluate: [Enterprise Autonomy](../projects/enterprise-autonomy.md) and the
  [ecosystem map](../ecosystem-map.md).
- To learn: [Agent theory](../theory/index.md).
- To apply: [Practice](../practice/index.md).

## Do I need the whole stack?

No. The projects are independently usable. Start with the seam you need:
identity, policy, memory, workflow, integration, or verification. The
[adoption path](../practice/adoption.md) describes a sequence.

## Is PRAXO-CORE production-ready?

PRAXO-CORE is an active framework with versioned releases (see
[pkg.go.dev](https://pkg.go.dev/github.com/axisvela/praxo-core/v2)). Production
readiness depends on your risk, controls, and evidence requirements. Run the
[verification and simulation](../practice/verify-and-simulate.md) steps before
committing.

## Why are there so many projects?

Because the problems are different: identity is not policy, memory is not
grounding, and a workflow engine is not a message bus. The
[ecosystem map](../ecosystem-map.md) shows the separation.

## What is governed autonomy?

Autonomy bounded by policy, evidence, and human decision paths. See
[Governed autonomy](../concepts/governed-autonomy.md).

## How does this relate to MCP?

MCP is a strong fit for synchronous tool and context integration. It is not a
coordination protocol, a workflow engine, or a governance layer. See
[Coordination vs orchestration](../concepts/coordination-vs-orchestration.md).

## Why does the repo `AXISRobo-PAMP` still use the old name?

The repository name retains a historical prefix. The project is part of the
adjacent architecture portfolio. See [PAMP](../projects/pamp.md).

## Why is `ea-harness` separate from TAXOVELA?

They are related but maintained separately. TAXOVELA is the current AI-native
architecture project in this map. See [ea-harness](../projects/ea-harness.md).

## How do I report a security issue?

Email **security@axisvela.com**. Do not open a public issue. See
[Security policy](https://github.com/axisvela/axisvela-open/blob/main/SECURITY.md).

## How do I run the documentation locally?

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

The site is built from `docs/` with MkDocs Material. See
[Contributing](https://github.com/axisvela/axisvela-open/blob/main/CONTRIBUTING.md).

## How do I cite the theory?

Cite the original paper listed in the [research map](../theory/research-map.md),
not this synthesis. For the documentation itself, cite the repository.
