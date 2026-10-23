# Anti-patterns

A short catalog of recurring mistakes. The detailed version, with controls, is in
[Practice anti-patterns](../practice/anti-patterns.md).

## Design

- **Prompt as policy.** A rule described in context is not enforced.
- **Model as architecture.** The model is a component, not the system.
- **One agent for everything.** Unbounded scope and authority.
- **Vector store as memory.** An index is not a memory architecture.
- **Logs as evidence.** Logs are for debugging, not proof.
- **Shared database integration.** Couples schemas and bypasses policy.
- **No exit path.** Lock-in and unbounded cost.

## Build

- **Unbounded tools.** The agent can do too much.
- **Long-lived shared keys.** Weak identity and slow revocation.
- **Direct external calls.** Credentials and egress are uncontrolled.
- **No step or cost limit.** Runaway loops.
- **Retries without idempotency.** Duplicate effects.
- **One happy-path test.** Probabilistic systems fail differently.
- **Unsigned artifacts.** Supply-chain risk.

## Operate

- **No recovery plan.** Failures become incidents.
- **No revocation path.** Authority cannot be withdrawn.
- **No human override.** The system cannot be stopped.
- **Evidence not retained.** Audit and learning are impossible.
- **No rollback.** A bad change persists.
- **Governance only at the end.** Too late to change the design.

## The meta-pattern

Most anti-patterns share one root: **confusing representation with control**.
A document, a prompt, a diagram, or a log can describe a rule or an action
without enforcing or proving it. Architecture is the difference.

## Related

- [DIKCA](../theory/dikca.md)
- [Governed autonomy](governed-autonomy.md)
- [Practice anti-patterns](../practice/anti-patterns.md)
