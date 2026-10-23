# Start here

There are five useful ways into AxisVela. Pick the one that matches your job;
you do not need to read the whole map first.

## Build

**You want to embed a governed agent loop or an SDK in your own system.**

Start with [PRAXO-CORE](projects/praxo-core.md), the MIT-licensed Go framework.
It is the smallest part of the ecosystem that still runs on its own.

```bash
git clone https://github.com/axisvela/praxo-core
cd praxo-core
go test ./...
```

A minimal run against a local OpenAI-compatible endpoint:

```bash
export PRAXO_BASE_URL=http://localhost:11434/v1
export PRAXO_MODEL=llama3.2
GOWORK=off go run ./examples/quickstart
```

On PowerShell, set the same variables with `$env:PRAXO_BASE_URL = "..."` and
`$env:PRAXO_MODEL = "..."`.

When you need more than the loop, add one seam at a time:

| Need | Project | What it gives you |
| --- | --- | --- |
| Model routing across providers and endpoints | [NOETIVELA](projects/noetivela.md) | Inference contracts and governed routing |
| Durable memory and retrieval | [MNEMOVELA](projects/mnemovela.md) | Typed memory, branches, hybrid retrieval |
| Async task/state coordination | [HARMOVELA](projects/harmovela.md) | Open coordination protocol |
| Governed access to external systems | [LIMENORA](projects/limenora.md) | Policy-enforcing integration gateway |
| Authorization and approvals | [AEGIVELA](projects/aegivela.md) | Delegated authority, policy enforcement |
| Durable, recoverable processes | [RHEOVELA](projects/rheovela.md) | Event-sourced workflow runtime |

For the full walkthrough, see [Build an agent](practice/build-an-agent.md).

## Evaluate

**You want to understand whether the ecosystem solves a real problem for your
organization.**

Read in this order:

1. [The ecosystem map](ecosystem-map.md) — the layers and the seams.
2. [Enterprise Autonomy](projects/enterprise-autonomy.md) — the public
   introduction and end-to-end examples. Its
   [product overview](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/products.md)
   and
   [technical catalog](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/technical-catalog.md)
   are the fastest way to see what is runnable today.
3. [The project index](projects/index.md) — compare problems, value, and
   licenses side by side.
4. One runnable demo from
   [`enterprise-autonomy/examples/`](https://github.com/axisvela/enterprise-autonomy/tree/main/examples).

The question to keep asking is not “which product is best?” but “which seam do I
need, and what evidence does it leave behind?” For the architectural view, read
[Agent architecture](architecture/index.md).

## Design

**You are designing a governed agent system.**

Read the architecture section in this order:

1. [Reference architecture](architecture/reference-architecture.md) — the layers
   and the end-to-end request path.
2. [Control planes](architecture/control-planes.md) — identity, policy,
   capability, coordination, and assurance.
3. [Contracts and interfaces](architecture/contracts.md) — how independent
   products compose.
4. [Evidence architecture](architecture/evidence.md) — how to make the design
   provable.
5. [Security model](architecture/security.md) — the threat model.

If you need the conceptual grounding first, read
[Agent theory](theory/index.md).

## Operate

**You are responsible for running agents, approvals, and processes.**

The operating stack is usually a combination of:

- [RHEOVELA](projects/rheovela.md) for durable process instances and recovery;
- [SYMBIVELA](projects/symbivela.md) for plan review, approvals, exceptions, and
  intervention;
- [MODUREGIS](projects/moduregis.md) for the governed capability catalog;
- [AEGIVELA](projects/aegivela.md) for authorization, delegation, and revocation;
- [TEKMOVELA](projects/tekmovela.md) and [PEIRAVELA](projects/peiravela.md) for
  verification and safe experimentation before release.

Start with the
[governance patterns](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/governance-patterns.md)
and the
[reference stacks](https://github.com/axisvela/enterprise-autonomy/tree/main/reference-stacks)
in Enterprise Autonomy. For the runnable version, see
[Durable process](practice/durable-process.md) and
[End to end](practice/end-to-end.md).

## Learn

**You want the ideas first, without product detail.**

Read [Agent theory](theory/index.md) first, especially:

- [Unified Agent Dynamics](theory/uad.md)
- [DIKCA](theory/dikca.md)
- [Intent, AOP, and control](theory/intent-aop.md)
- [PPES](theory/ppes.md)

Then use the [concepts](concepts/index.md) for the vocabulary:

- [Governed autonomy](concepts/governed-autonomy.md)
- [Agency and control](concepts/agency-and-control.md)
- [Contracts, not a kernel](concepts/contracts-not-kernel.md)
- [Evidence and auditability](concepts/evidence-and-audit.md)
- [Agent identity in three planes](concepts/agent-identity.md)
- [Coordination vs orchestration](concepts/coordination-vs-orchestration.md)

The [terminology and glossary](concepts/glossary.md) collects the full
vocabulary used across the projects.

## One warning about “open”

An `*-open` repository is an **open surface**: contracts, SDKs, examples, and
sometimes binaries. It is designed to let you evaluate and integrate. It does
not always mean the entire runtime is open source. Check the repository
`LICENSE` and the [licenses page](reference/licenses.md) before making a
commitment.
