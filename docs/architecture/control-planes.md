# Control planes

A data plane does the work. A control plane decides whether, how, and under what
conditions the work may happen. Most agent failures are control-plane failures
that look like model failures.

## Data plane vs control plane

| Data plane | Control plane |
| --- | --- |
| Executes tools and processes | Decides identity, policy, capability, coordination |
| Handles payloads and state | Handles authority, constraints, and evidence |
| Scales with work | Scales with decisions and governance |
| Failure is visible as an error | Failure is visible as an unauthorized or ungoverned action |

A system with a strong data plane and a weak control plane can be fast, capable,
and ungovernable.

## Five control planes

| Plane | Question | AxisVela examples |
| --- | --- | --- |
| **Identity** | Who is acting, and can it prove it? | EIDOVELA, NOMIVELA |
| **Policy** | What is allowed, and who approved it? | AEGIVELA, SYMBIVELA |
| **Capability** | What can be invoked, and how is it governed? | MODUREGIS, ORCHADYN |
| **Coordination** | Who is doing what, and what is the state? | Harmovela, COORDIVELA |
| **Assurance** | How do we know it still works? | TEKMOVELA, PEIRAVELA, SYNDOVELA |

These planes are related but not interchangeable. A valid identity does not imply
authorization. A capability catalog does not imply coordination. A passing test
does not imply that the right action was authorized.

## How the planes interact

A useful request path:

1. **Identity** establishes the agent and workload.
2. **Capability** resolves what the agent wants to invoke.
3. **Policy** authorizes the invocation under the current context.
4. **Coordination** ensures no conflicting work and a clear owner.
5. **Execution** happens in the data plane.
6. **Assurance** checks the outcome and records evidence.

The order can vary, but the decisions must be explicit.

## Design rules

- **Do not put control in the prompt.** A prompt is context, not enforcement.
- **Keep the planes separable.** Teams should be able to change policy without
  rewriting the runtime.
- **Make decisions observable.** Each plane should emit a decision record.
- **Fail closed on high-risk actions.** When the control plane is unavailable,
  the safe default is deny for consequential actions.
- **Use the same identity across planes.** Otherwise attribution breaks.
- **Bound delegation.** Authority should attenuate, not amplify, across agents.
- **Separate development coordination from runtime coordination.** They have
  different state and failure modes.

## A minimal implementation

You do not need all five planes to start. A practical sequence:

1. Identity and a policy hook (deny by default).
2. A capability list and a sandbox.
3. An effect ledger and trace.
4. Approvals for high-risk actions.
5. Coordination when multiple agents or long-running work appear.
6. Assurance when changes need evidence.

This sequence keeps the control plane proportional to the risk.

## What to take away

- Control planes are the architecture of governance.
- Each plane answers a different question; collapsing them creates blind spots.
- If a decision is not recorded, it is not a control plane; it is a hope.
