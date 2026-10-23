# Terminology and glossary

A working vocabulary for agent systems. Definitions are intentionally short;
follow the links for the longer treatment.

## Agents and autonomy

**Agent** — A software actor that pursues goals, uses capabilities, and produces
effects. An agent may be long-running, delegated to, and governed. See
[Agent taxonomy](agent-taxonomy.md).

**Agency** — The capacity to act toward a goal. Distinct from autonomy (how much
the agent chooses) and control (what bounds it). See
[Agency and control](agency-and-control.md).

**Autonomy** — The degree to which an agent can choose and modify its actions
without external intervention. Autonomy is bounded by architecture and control.

**Autonomy level** — A practical label for how much an agent may do without
approval: assisted, supervised, delegated, bounded autonomous, or meta-control.
See [Autonomy and architecture](../theory/autonomy-architecture.md).

**Bounded autonomy** — Autonomy inside an enforced envelope: capabilities,
budgets, step limits, time limits, and recovery rules.

**Meta-control** — The capacity of a system to modify its own control structures
under architectural authorization. A high-autonomy property, not a default.
See [DIKCA](../theory/dikca.md).

**Agent lifecycle** — The states an agent passes through: proposed, registered,
activated, operated, suspended, revoked, retired. Transitions should have owners
and evidence.

**Agent registry** — A system of record for agents, namespaces, authority
bindings, and lifecycle epochs. See [NOMIVELA](../projects/nomivela.md).

**Agent identity** — A verifiable representation of an agent workload, its
tenant, and its authority context. See [Agent identity](agent-identity.md).

**Agent type** — One of five enterprise categories: Application, Service,
Employee, Physical Twin, Human Twin. See
[Enterprise agent taxonomy](../theory/agent-taxonomy.md).

**Multi-agent system (MAS)** — A system of multiple agents that coordinate,
delegate, and share state. See
[Multi-agent dynamics](../theory/multi-agent-dynamics.md).

**Delegation** — Transferring authority or work to another agent or person.
Delegation should attenuate authority, not amplify it.

**Handoff** — A structured transfer of work and context between agents or
humans, with an owner and evidence.

**Role** — A named set of responsibilities and authority within a system or
organization.

**Supervision** — Human or automated oversight of an agent’s plans and actions.

**Human-in-the-loop (HITL)** — A designed decision point where a human reviews,
approves, intervenes, or accepts an outcome. See [SYMBIVELA](../projects/symbivela.md).

**Human-on-the-loop** — A model where a human monitors and can intervene, but
does not approve every step.

**Human sovereignty** — The right and ability of humans to know, approve,
intervene, revoke, and inspect. See
[Autonomy and architecture](../theory/autonomy-architecture.md).

**Kill switch** — A mechanism to stop an agent or process quickly, ideally
without stopping the whole system.

**Escalation** — Moving a decision or exception to a higher authority when the
current path cannot resolve it.

## Architecture and control

**Architecture** — The constitutive structure that determines which
configurations are possible, which controls are enforceable, and which evidence
can be produced. See [DIKCA](../theory/dikca.md).

**Architectonic constraint** — A constraint that defines what a system may
become, not just what it currently does.

**Control** — Constraints on what may be done, plus the mechanisms that enforce
them. Control is not the same as knowledge or description.

**Control plane** — The part of a system that decides identity, policy,
capability, coordination, and assurance. See
[Control planes](../architecture/control-planes.md).

**Data plane** — The part of a system that executes work and moves payloads.

**Policy** — A rule or set of rules about what is allowed, under which
conditions, and with what evidence.

**Policy decision point (PDP)** — The component that evaluates policy and
returns a decision. See [AEGIVELA](../projects/aegivela.md).

**Policy enforcement point (PEP)** — The component that enforces a policy
decision at a boundary.

**Guardrail** — A control that constrains behavior, ideally at an architectural
boundary. A guardrail in a prompt is advice; a guardrail in a PEP is control.

**Sandbox** — An execution environment that limits what an agent can access or
do. See [PRAXOVELA](../projects/praxovela.md).

**Capability gate** — A control that allows or denies a capability before
invocation.

**Least privilege** — Granting the minimum authority needed for a task, for the
shortest necessary time.

**Defense in depth** — Layering independent controls so a single failure does
not remove protection.

**Trust boundary** — A boundary where data, identity, or authority changes
trust level. Controls belong at trust boundaries.

**Contract** — A versioned interface between independent components: an API,
schema, protocol, SDK, or conformance fixture. See
[Contracts and interfaces](../architecture/contracts.md).

**Open surface** — A public repository containing contracts, SDKs, examples, and
sometimes binaries, without necessarily containing the full runtime. See
[Open surfaces](open-surfaces.md).

**Conformance** — Demonstrated compatibility with a contract, usually through
fixtures and tests.

**Versioning** — Assigning identifiers to contract or product revisions so
consumers can manage compatibility.

**Deprecation** — A planned transition away from a contract or feature, with a
date and migration path.

**Reference architecture** — A reusable architecture pattern used to guide
implementations. See
[Reference architecture](../architecture/reference-architecture.md).

**Deployment shape** — The trust topology of a deployment: local-first,
single-tenant service, enterprise hybrid, or edge/physical. See
[Deployment shapes](../architecture/deployment.md).

**Local-first** — A design where data and execution live primarily on the user’s
device.

**Hybrid deployment** — A deployment spanning on-premises, cloud, and edge
components with explicit federation.

**Edge** — Computing near the physical system or data source, often with limited
connectivity and higher safety constraints.

## Intent, planning, and work

**Intent** — The outcome a person or system wants, including constraints and
success criteria. See [Intent and specification](intent-and-specification.md).

**Specification** — An explicit statement of goal, context, constraints, and
acceptance criteria.

**Acceptance criterion** — An observable condition that determines whether an
outcome is acceptable. It should be testable.

**Constraint** — A restriction on what may be done or how it may be done.

**Goal** — The desired outcome, separate from the plan to achieve it.

**Plan** — A structured, revisable artifact describing how to reach a goal under
constraints. See [ORCHADYN](../projects/orchadyn.md).

**Planning** — The activity of producing or revising a plan.

**Replanning** — Revising a plan when assumptions, state, or constraints change.

**Verification contract** — A testable statement of what must be true for a
system to be accepted. See [TEKMOVELA](../projects/tekmovela.md).

**Workflow** — A defined sequence of steps for a process. A workflow engine adds
durability, state, and recovery.

**Process instance** — A durable execution of a workflow with recorded history.
See [RHEOVELA](../projects/rheovela.md).

**Durable execution** — Execution that survives process or device failure and
resumes from recorded state.

**Idempotency** — The property that repeating an operation does not repeat its
effect.

**Compensation** — An action that offsets or reverses a completed step.

**Checkpoint** — A saved state from which execution can resume.

**Recovery** — Restoring a system or process to a valid state after failure.

**Retry** — Re-attempting an operation after failure. Safe only with idempotency
or compensation.

**Timeout** — A bound on how long an operation may take.

**Circuit breaker** — A mechanism that stops calling a failing dependency to
prevent cascading failure.

**Approval** — A human decision to allow a high-risk action. It should reference
the plan, evidence, and accountable person.

**Exception** — A case that does not follow the expected path and requires a
decision.

**Intervention** — A human action that changes or stops an executing process.

## Capabilities, skills, and tools

**Tool** — A callable function or API exposed to a model. Tools need input
validation, sandboxing, and limits.

**Capability** — A governed unit of action with identity, policy, and audit. See
[Capability, skill, and tool](capability-skill-tool.md).

**Capability catalog** — A governed registry of capabilities. See
[MODUREGIS](../projects/moduregis.md).

**Skill** — A packaged procedure or knowledge artifact an agent can use. Skills
need provenance and versioning.

**Skill bundle** — A composed set of skills distributed as an artifact. See
[SYNDOVELA](../projects/syndovela.md).

**Plugin** — An extension loaded into a runtime at a controlled boundary. See
[PRAXO-CORE](../projects/praxo-core.md).

**MCP (Model Context Protocol)** — A protocol for exposing tools and context to
models. MCP handles synchronous capability invocation; it is not a full
coordination or governance layer.

**Adapter** — A component that connects one interface to another, such as a
model provider adapter or a gateway adapter.

**Gateway** — A boundary component that mediates access to external systems. See
[LIMENORA](../projects/limenora.md).

**Egress** — Outbound network traffic from an agent or system. Egress should be
governed.

**Credential injection** — Supplying credentials at a boundary so the agent does
not hold them.

**Rate limit** — A bound on how often an operation may be performed.

**Budget** — A bound on cost, tokens, time, or steps for a run.

**Cost ceiling** — The maximum acceptable cost for a task or period.

## Memory, context, and knowledge

**Context** — The information available to the model at a step: goal, session
state, retrieved items, tool descriptions.

**Context window** — The model’s bounded input capacity. It is a working set,
not a memory system.

**Context engineering** — Designing what enters the context, in what order, with
what provenance, and what is excluded.

**Memory** — Durable state that persists across runs: episodic, semantic,
procedural, or working.

**Episodic memory** — Records of specific events and experiences.

**Semantic memory** — Stable facts, concepts, and preferences.

**Procedural memory** — Reusable procedures and skills.

**Working memory** — Short-lived state for the current task.

**Retrieval** — Selecting relevant information from a store for the current
context.

**Retrieval-augmented generation (RAG)** — Using retrieved context to condition
model output. Retrieval is not grounding by itself.

**Grounding** — Attaching meaning and evidence to retrieved material: concepts,
entities, claims, sources, conflicts.

**Grounding view** — A purpose-scoped projection of governed knowledge. See
[GNOSIVELA](../projects/gnosivela.md).

**Ontology** — A structured set of concepts and relations for a domain.

**Entity resolution** — Determining when different references point to the same
entity.

**Assertion** — A claim about state or fact, ideally with provenance.

**Claim** — A statement that may be true or false, and should be evidence-backed
when used for decisions.

**Evidence** — Structured, linked, tamper-evident, and retained artifacts that
support reconstruction and defense. See
[Evidence and auditability](evidence-and-audit.md).

**Provenance** — The origin and history of a piece of data, claim, or artifact.

**Bitemporal** — Distinguishing valid time (when something was true) from
recorded time (when the system learned it).

**Valid time** — The time period during which a fact is true in the world.

**Recorded time** — The time at which the system recorded a fact.

**World model** — A shared, temporal representation of operational state and its
evidence. See [World models](world-models.md).

**Digital twin** — A synchronized model of a specific real-world system.

**Simulation** — Executing a model of a system to explore possible outcomes.

**Possible world** — A simulated world used to test scenarios without touching
production. See [PEIRAVELA](../projects/peiravela.md).

**Forgetting** — Deliberate removal or expiry of memory. A governance feature,
not a bug.

**Freshness** — How current a piece of information is, relative to its use.

**Conflict** — A disagreement between claims or sources that must be governed
rather than averaged away.

## Identity, security, and trust

**Identity** — A representation of an actor (human, agent, workload, service)
that can be verified.

**Workload identity** — An identity bound to a running workload rather than a
shared key.

**Attestation** — Evidence about a workload’s properties, used to establish
trust. See [EIDOVELA](../projects/eidovela.md).

**Proof of possession (PoP)** — A cryptographic demonstration that the holder of
a token also holds the associated key.

**OIDC** — OpenID Connect, an identity layer on OAuth 2.0.

**SPIFFE** — A standard for workload identity in distributed systems.

**mTLS** — Mutual TLS, where both parties authenticate with certificates.

**Token** — A credential representing an identity or authority, ideally
short-lived and scoped.

**Scope** — The set of actions or resources an authority permits.

**Scope attenuation** — Reducing authority when delegating.

**Authority binding** — A recorded association between an agent and the
authority it may exercise.

**Revocation** — Withdrawing authority or credentials before their expiry.

**Authentication** — Establishing who an actor is.

**Authorization** — Deciding what an authenticated actor may do.

**Principal** — The actor on whose behalf an action is taken.

**Tenant** — An isolated organizational boundary in a multi-tenant system.

**Namespace** — A naming and isolation scope for agents or resources.

**Prompt injection** — Untrusted content that attempts to change an agent’s
instructions or behavior.

**Data exfiltration** — Unauthorized transfer of data outside a trust boundary.

**Supply chain** — The set of dependencies, artifacts, and processes that produce
a system. Agent skills and models are part of it.

**SBOM** — Software bill of materials: an inventory of components and
dependencies.

**Signing** — Cryptographic proof that an artifact came from a trusted source and
was not altered.

**Agent worm** — Malicious behavior that propagates across agents or agent
systems. See [Security model](../architecture/security.md).

**Denial of wallet** — An attack or failure that causes unbounded cost.

**Zero trust** — A security stance that verifies every access rather than
trusting a network location.

## Evidence, reliability, and operations

**Observability** — The ability to infer system health from metrics, logs, and
traces. See [Observability](observability.md).

**Telemetry** — Emitted measurements and events about system behavior.

**Trace** — A record of a request’s path across components.

**Span** — A timed operation within a trace.

**Metric** — A numeric measurement aggregated over time.

**Log** — A timestamped record emitted by a component.

**Effect ledger** — A durable record of side effects, inputs, decisions, and
recovery information. See [PRAXOVELA](../projects/praxovela.md).

**Audit trail** — A chronological record of decisions and actions, suitable for
review.

**Evidence bundle** — A packaged set of evidence for a decision or release.

**Evidence chain** — The linked sequence from goal to verification. See
[Evidence architecture](../architecture/evidence.md).

**Tamper-evident** — A property where alteration or omission can be detected.

**Retention** — How long evidence or data is kept, and under what policy.

**Release gate** — A checkpoint that must be passed before a release.

**Verification** — Checking that an outcome meets a contract or acceptance
criterion.

**Certification** — A formal or independent confirmation of a property. Use the
term carefully; most evidence is not certification.

**Reliability** — The ability of a system to continue operating correctly under
failure. See [Reliability](reliability.md).

**Failure domain** — The scope of impact when a component fails.

**Blast radius** — The maximum damage an action or failure can cause.

**Runbook** — A documented procedure for operating or recovering a system.

**SLO / SLI** — Service level objective / indicator: a target and a measurement
for service quality.

**Incident** — An unplanned event that degrades or threatens the system.

**Postmortem** — A structured review of an incident and its causes.

## Coordination and protocols

**Coordination** — Shared state and progress across agents over time: events,
tasks, leases, delegation, recovery, governance. See
[Coordination vs orchestration](coordination-vs-orchestration.md).

**Orchestration** — Sequencing work through a defined process, often with
durability and recovery.

**Protocol** — A shared set of rules and message formats for interaction. See
[Harmovela](../projects/harmovela.md).

**Event** — A record that something happened.

**Task** — A unit of work with a lifecycle.

**State** — What is true now, and how it changes.

**Lease** — A time-bounded claim of ownership over work.

**Claim** — In coordination, an assertion of ownership or intent over a task.

**Dependency** — A relationship where one unit of work requires another.

**Scheduling** — Assigning work to time or resources.

**Transport** — The mechanism by which messages move (stdio, WebSocket, SSE,
gRPC, NATS, Kafka, Redis Streams).

**Conformance fixture** — A test vector used to verify compatible behavior
across implementations.

**Interoperability** — The ability of independent systems to work together
through shared contracts.

**A2A** — Agent-to-agent interaction. Treat it as a coordination and security
problem, not just a message format.

## Business and governance

**Governance** — The system of decision rights, controls, and evidence that
directs and constrains behavior.

**Accountability** — The obligation to answer for an action or outcome.

**Responsibility** — The assignment of ownership for a decision or artifact.

**Risk** — The combination of uncertainty and consequence. In architecture, risk
often means decision exposure, not only a security threat.

**Decision exposure** — The value at stake, uncertainty, constraints, and
consequence of insufficient visibility around a decision.

**Policy version** — The identifier of the policy used for a decision, needed
for reproducibility and audit.

**Change control** — The process for approving, testing, and rolling back
changes.

**Separation of duties** — Dividing authority so no single actor can perform a
high-risk action alone.

**Audit** — An independent examination of evidence and controls.

**Compliance** — Conformity with laws, regulations, or standards. Compliance is
not the same as security or quality.

**Enterprise architecture (EA)** — The practice of aligning business, data,
applications, and technology across an enterprise.

**Viewpoint** — A convention for framing a set of stakeholder concerns. See
[PACT and AVDM](../theory/research-map.md).

**Concern** — A stakeholder interest or quality attribute that an architecture
must address.

**Reference taxonomy** — A reusable catalog of viewpoints or concepts, such as
PACT.

**Adoption** — The process of evaluating, piloting, and integrating a system.
See [Adoption path](../practice/adoption.md).

**Pilot** — A bounded deployment used to test value and controls.

**Open core** — A model where an open surface or core is combined with a
commercial edition.

**Commercial edition** — A separately licensed edition with additional
operational or enterprise capabilities.

**Licensing** — The legal terms under which a project may be used, modified, and
distributed. The repository `LICENSE` is authoritative.

## Acronyms

- **AADM** — Architecture Artifact Decision Model.
- **AOP** — Agent-Oriented Programming.
- **ARCM** — Architectural Responsibility Configuration.
- **AVDM** — Architecture Viewpoint Decision Model.
- **CEF** — Constraint Engineering Framework.
- **DIKCA** — Data, Information, Knowledge, Control, Architecture.
- **EA** — Enterprise Architecture.
- **HITL** — Human-in-the-loop.
- **IIC** — Intent-Conditioned Computation.
- **MAS** — Multi-agent system.
- **MCP** — Model Context Protocol.
- **OIDC** — OpenID Connect.
- **PACT** — Practical Architecture Viewpoint Taxonomy.
- **PDP / PEP** — Policy Decision Point / Policy Enforcement Point.
- **PPES** — Probabilistic Program Execution Semantics.
- **RAG** — Retrieval-Augmented Generation.
- **SBOM** — Software Bill of Materials.
- **SLO / SLI** — Service Level Objective / Indicator.
- **SPIFFE** — Secure Production Identity Framework for Everyone.
- **UAD** — Unified Agent Dynamics.
