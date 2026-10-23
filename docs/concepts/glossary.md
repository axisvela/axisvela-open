# Glossary

Terms used across the AxisVela projects. Definitions are intentionally short;
the linked project pages provide context.

**Agent** — A software actor that can plan, call capabilities, and produce
effects. An agent may be long-running, delegated to, and governed.

**Capability** — A governed unit of action exposed to agents or workflows.
Capabilities have identity, policy, and audit, not just a function signature.

**Contract** — A versioned interface between independent components: an API, a
schema, a protocol, or a conformance fixture set.

**Coordination** — Shared state and progress across agents over time: events,
tasks, leases, delegation, recovery, and governance.

**Digital twin** — A synchronized model of a specific real-world system, used for
observation, reasoning, and simulation.

**Effect ledger** — A durable record of side effects produced by an agent,
including inputs, decisions, results, and recovery information.

**Evidence** — Structured, linked, tamper-evident, and retained artifacts that
let someone reconstruct and defend a decision.

**Grounding view** — A purpose-scoped projection of governed knowledge, used to
give an agent or planner context with definitions and evidence.

**HITL (human in the loop)** — A designed decision point where a human reviews,
approves, intervenes, or accepts an outcome.

**Inference contract** — A statement of the model behavior required for a task,
used to route requests across providers and endpoints.

**Lease** — A time-bounded claim of ownership over work, used to prevent
duplicate or conflicting execution.

**Open surface** — A public repository containing contracts, SDKs, examples, and
sometimes binaries, without necessarily containing the full runtime.

**Plan** — A structured, revisable artifact describing how to reach a goal under
constraints, separate from the process that executes it.

**Possible world** — A simulated world used to test a scenario, policy, or
behavior without touching production.

**Process instance** — A durable, recoverable execution of a workflow, with a
recorded history.

**Verification contract** — A testable statement of what must be true for a
system to be accepted, derived from intent and acceptance criteria.

**World model** — A shared, temporal representation of operational state and its
evidence, used by agents, planners, and humans.
