# Agent practice

These guides turn the theory and architecture into steps you can run. They use
the AxisVela projects as the reference implementation, but the patterns are
portable.

## Choose a path

| Goal | Guide | Time |
| --- | --- | --- |
| Build and run a minimal governed agent | [Build an agent](build-an-agent.md) | 30–60 min |
| Add identity, policy, approvals, and evidence | [Govern an agent](govern-an-agent.md) | 1–2 h |
| Add durable memory and grounded context | [Memory and context](memory-and-context.md) | 1–2 h |
| Run a long-lived, recoverable process | [Durable process](durable-process.md) | 2–4 h |
| Connect the agent to external systems safely | [Connect external systems](connect-external-systems.md) | 1 h |
| Verify and simulate before release | [Verify and simulate](verify-and-simulate.md) | 2–4 h |
| See the whole ecosystem working together | [End to end](end-to-end.md) | 3–6 h |
| Decide whether and how to adopt | [Adoption path](adoption.md) | 1 h reading |

## Prerequisites

- Go 1.25+ for PRAXO-CORE and most Go services.
- Python 3.10+ for TAXOVELA and the Python SDKs.
- Docker is useful for the enterprise-autonomy demos.
- Node.js is only needed for the TypeScript SDKs and some frontends.

## A warning about open surfaces

Some guides use an `*-open` repository as the integration surface. That surface
may contain contracts, SDKs, examples, and binaries without the full runtime
core. Check the repository `LICENSE`, README, and release notes before assuming a
component is production-ready.

## The practice rule

Every step should leave evidence. If a guide asks you to add a capability,
permission, or process step, also add the record that proves what happened. An
agent that works but cannot explain itself is not finished.
