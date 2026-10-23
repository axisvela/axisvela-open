# Projects

Every project in the public map, with the problem it addresses and the value it
provides. Each row links to a page with more detail and the authoritative
repository.

Some entries are products, some are programs (for example, Enterprise Autonomy),
and some are adjacent or related projects. The `kind` field in
[`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml)
records the distinction.

## At a glance

| Project | Layer | Problem it addresses | What you get | License |
| --- | --- | --- | --- | --- |
| [PRAXO-CORE](praxo-core.md) | Foundation | Every team rebuilds the agent loop, provider abstraction, tool contracts, and governance | MIT Go framework with loop, primitives, adapters, policy, sandbox, plugins | MIT |
| [TAXOVELA](taxovela.md) | Design | Architecture artifacts are inconsistent, unverifiable, and disconnected from AI-assisted design | AI-native architecture skills and CLI with deterministic validation gates | MIT |
| [Harmovela](harmovela.md) | Foundation | MCP covers synchronous calls, not long-running multi-agent coordination | Open protocol for events, tasks, state, delegation, recovery, governance | Apache-2.0 |
| [Harmovela Open](harmovela-open.md) | Foundation (companion) | Protocol integrators need examples and an ecosystem registry | Runnable examples, ecosystem registry, authoring guides | Apache-2.0 |
| [COORDIVELA](coordivela.md) | Foundation | Humans and agents duplicate or conflict on shared development work | Coordination control plane: leases, dependencies, schedules, interventions | Apache-2.0 |
| [PRAXOVELA](praxovela.md) | Runtime | Local agents need real capabilities without losing control of side effects | Deny-by-default runtime with effect ledger, recovery, replayable traces | Apache-2.0 surface |
| [Mnemovela](mnemovela.md) | Runtime | Agent memory is often an opaque vector store with no lifecycle | Typed, branchable, auditable cognition runtime with hybrid retrieval | Apache-2.0 |
| [Noetivela](noetivela.md) | Runtime | Model and endpoint sprawl makes policy, cost, quality, and sovereignty hard | Inference fabric with contracts and governed routing | Apache-2.0 |
| [ORCHADYN](orchadyn.md) | Work | Turning goals and constraints into executable plans is ad hoc | Planning compiler producing verified, revisable plans | Apache-2.0 |
| [MODUREGIS](moduregis.md) | Work | Enterprises cannot safely discover, authorize, and audit capabilities | Capability control plane with registry, policy, invocation, audit | Apache-2.0 |
| [RHEOVELA](rheovela.md) | Work | Long-running processes need durability, recovery, approvals, and audit | Durable workflow platform for governed capability plans | Apache-2.0 |
| [EIDOVELA](eidovela.md) | Trust | Agents need verifiable identity and workload attestation, not shared API keys | Agent identity provider with OIDC and proof-of-possession tokens | Apache-2.0 |
| [NOMIVELA](nomivela.md) | Trust | There is no system of record for agents, namespaces, and authority bindings | Agent registry and namespace authority with lifecycle epochs | Apache-2.0 |
| [AEGIVELA](aegivela.md) | Trust | Agent authorization is coarse and delegated authority is hard to revoke | Authorization, delegation, approval, revocation, and security evidence | Apache-2.0 |
| [GNOSIVELA](gnosivela.md) | Knowledge | Enterprise concepts, claims, and conflicts are fragmented and ungrounded | Semantic and knowledge fabric with scoped grounding views | Apache-2.0 |
| [ONTOVELA](ontovela.md) | Knowledge | Decisions need trustworthy current and historical operational state | Evidence-bearing bitemporal world model and digital twin | See repo |
| [LIMENORA](limenora.md) | Boundary | External API/MCP/event access bypasses policy and leaks credentials | Governed north-south integration gateway with evidence | Apache-2.0 |
| [TEKMOVELA](tekmovela.md) | Assurance | Agent systems are hard to verify and release decisions lack evidence | Verification contracts, reproducible tests, release gates | Apache-2.0 |
| [PEIRAVELA](peiravela.md) | Assurance | High-risk autonomy changes cannot be tried safely in production | Possible-world experiment control plane with simulation evidence | Apache-2.0 |
| [SYNDOVELA](syndovela.md) | Assurance | Agent skills are composed across runtimes without supply-chain assurance | Skill composition governance, signed artifacts, provenance | Apache-2.0 |
| [SYMBIVELA](symbivela.md) | Human | Humans lose meaningful control of agent plans and exceptions | Collaboration workspace for goals, approvals, intervention, evidence | Apache-2.0 |
| [KINETOVELA](kinetovela.md) | Physical | Robot fleets need safe, observable, recoverable mission execution | Physical-autonomy control plane for fleet and mission operations | Apache-2.0 |
| [Enterprise Autonomy](enterprise-autonomy.md) | Program | It is hard to see how the products compose end to end | Public introduction, reference stacks, runnable examples | See repo |
| [PAMP](pamp.md) | Adjacent | Enterprise-architecture portfolios need a practical management platform | Enterprise architecture management platform | See repo |

## Choose by problem

| Problem | Useful starting points |
| --- | --- |
| “I need an agent loop I can embed.” | PRAXO-CORE |
| “I need to coordinate several agents over time.” | Harmovela, COORDIVELA |
| “I need a process that survives restarts and approvals.” | RHEOVELA, SYMBIVELA |
| “I need to know what an agent is allowed to do.” | AEGIVELA, MODUREGIS |
| “I need to know who the agent is.” | EIDOVELA, NOMIVELA |
| “I need trustworthy context, not just retrieval.” | GNOSIVELA, ONTOVELA, MNEMOVELA |
| “I need to connect to external systems safely.” | LIMENORA |
| “I need evidence that it still works.” | TEKMOVELA, PEIRAVELA |
| “I need to design and review the architecture.” | TAXOVELA, PAMP |
| “I need to see it all working together.” | Enterprise Autonomy |

## Adjacent and related projects

- **[PAMP](pamp.md)** is an enterprise-architecture management platform. Its
  repository still carries the historical `AXISRobo-PAMP` name.
- **[ea-harness](ea-harness.md)** is an earlier public architecture skill-pack
  repository. [TAXOVELA](taxovela.md) is the current AI-native architecture
  project; the two are maintained separately.

## About “open surface”

Several rows above are product **open surfaces** rather than the full runtime.
An open surface typically contains versioned contracts, SDKs, examples, and
sometimes signed binaries. The runtime core or enterprise edition may be
developed separately. The project page and the repository `LICENSE` are the
authoritative source for what is included.
