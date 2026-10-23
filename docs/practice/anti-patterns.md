# Anti-patterns and checklists

A collection of recurring mistakes, organized by phase, with the control that
prevents them.

## Design anti-patterns

| Anti-pattern | Why it fails | Better pattern |
| --- | --- | --- |
| **Prompt as policy** | A prompt describes a rule; it does not enforce it | Policy at an architectural boundary |
| **Model as architecture** | The model is a component, not the system | Explicit layers, contracts, and controls |
| **One agent for everything** | Unbounded scope and authority | Roles, capabilities, and delegation limits |
| **Vector store as memory** | An index is not a memory architecture | Separate context, memory, grounding, world state |
| **Logs as evidence** | Logs are optimized for debugging, not proof | Structured, linked, retained evidence |
| **Shared database integration** | Couples schemas and bypasses policy | Versioned contracts and APIs |
| **No exit path** | Lock-in and unbounded cost | Open surfaces and replaceable adapters |
| **Simulation as decoration** | A demo is not an experiment | Reproducible matrices and provenance |

## Build anti-patterns

| Anti-pattern | Why it fails | Better pattern |
| --- | --- | --- |
| **Unbounded tools** | The agent can do too much | Minimal, explicit capabilities |
| **Long-lived shared keys** | Weak identity and slow revocation | Workload identity and short-lived tokens |
| **Direct external calls** | Credentials and egress are uncontrolled | Governed gateway |
| **No step or cost limit** | Runaway loops and denial of wallet | Budgets and step limits |
| **Retries without idempotency** | Duplicate effects | Idempotency keys and recorded effects |
| **Testing one happy path** | Probabilistic systems fail differently | Distributional testing |
| **Unsigned artifacts** | Supply-chain risk | Signing and provenance |

## Operate anti-patterns

| Anti-pattern | Why it fails | Better pattern |
| --- | --- | --- |
| **No recovery plan** | Failures become incidents | Checkpoints and durable process |
| **No revocation path** | Authority cannot be withdrawn | Revocation tested |
| **No human override** | The system cannot be stopped | Intervention and kill switch |
| **Evidence not retained** | Audit and learning are impossible | Retention and access control |
| **No rollback** | A bad change persists | Versioned releases and rollback |
| **Governance as a gate at the end** | Too late to change the design | Governance at the boundary |

## Checklists

### Design review

- [ ] The problem and success criteria are explicit.
- [ ] The agent type and autonomy level are named.
- [ ] The control planes are identified.
- [ ] The evidence chain is designed.
- [ ] The failure and recovery paths are defined.
- [ ] The exit path is acceptable.

### Security review

- [ ] Identity is workload-based.
- [ ] Capabilities are deny-by-default.
- [ ] Egress is governed.
- [ ] Secrets are injected, not embedded.
- [ ] Artifacts are signed.
- [ ] Delegation attenuates.
- [ ] Revocation is tested.

### Operations review

- [ ] Budgets and step limits exist.
- [ ] Evidence is complete and retained.
- [ ] Recovery is tested.
- [ ] Human override works.
- [ ] Model/policy/skill changes trigger re-verification.
- [ ] A rollback exists.

### Release review

- [ ] Contracts pass.
- [ ] Verification evidence exists.
- [ ] The change is understood.
- [ ] The risk is accepted by an accountable person.
- [ ] The rollback is ready.

## The simplest test

Ask: *if this agent does the wrong thing tomorrow, what stops it, what proves it,
and who can turn it off?* If the answer is “the prompt,” the design is not done.
