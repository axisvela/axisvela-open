# Adoption path

This guide is for teams deciding whether and how to adopt the ecosystem. It is a
practical sequence, not a sales process.

## 1. Evaluate

Start with a real problem, not a product tour.

- Read [Start here](../start-here.md) and the
  [ecosystem map](../ecosystem-map.md).
- Pick one runnable example from
  [Enterprise Autonomy](https://github.com/axisvela/enterprise-autonomy).
- Identify the control you lack today: identity, policy, evidence, recovery,
  verification, or integration.
- Check the [licenses](../reference/licenses.md) and the open-surface boundary.

**Exit criteria:** you can name the seam you need and the evidence you want.

## 2. Pilot

Build the smallest system that exercises the seam.

- Use PRAXO-CORE for the agent.
- Add one control plane at a time.
- Keep the tool set small.
- Record evidence from day one.
- Define what “success” means before the pilot.

**Exit criteria:** the pilot runs, fails safely, and produces usable evidence.

## 3. Integrate

Connect the pilot to real systems.

- Put external access behind LIMENORA or an equivalent gateway.
- Add identity and authority bindings.
- Make long-running work durable.
- Add approvals for high-risk steps.
- Add verification for release changes.

**Exit criteria:** a real workflow completes end to end with evidence and a
recovery path.

## 4. Scale

Only after the controls are proven.

- Add agents and capabilities.
- Add coordination (Harmovela, COORDIVELA).
- Add simulation and verification for higher-risk changes.
- Federate across sites or tenants if needed.
- Review cost, latency, and governance load.

**Exit criteria:** the system can be operated, audited, and changed without
losing control.

## Build vs buy

| Question | Consider |
| --- | --- |
| Is this capability a commodity? | Routing, model access, generic tools may be bought. |
| Is the context proprietary? | Keep it; it is hard to replicate. |
| Is the evidence yours? | Own the evidence chain. |
| What is the exit cost? | Prefer contracts and open surfaces with migration paths. |
| What is the cost curve? | Inference-heavy designs need routing and budgets. |

## Open surface vs commercial edition

An `*-open` repository is an integration surface. It may be enough for a pilot
and for building your own runtime. An enterprise edition may add multi-tenancy,
high availability, compliance, or managed operations.

Do not assume the open surface is the full product. Do not assume the commercial
edition is required for every use case. Check the repository and the license.

## A risk review

- What is the failure blast radius?
- What can the agent change in the real world?
- Where are credentials and data?
- What is the recovery path?
- What evidence will exist after an incident?
- Can authority be revoked quickly?
- What is the model and skill supply chain?
- What is the cost ceiling?

## A pilot checklist

- [ ] One real problem and one success criterion.
- [ ] One agent, one bounded tool set.
- [ ] Identity and policy from the start.
- [ ] Evidence retained.
- [ ] Failure and recovery tested.
- [ ] A human approval path for high-risk actions.
- [ ] A plan for removing the pilot if it fails.

## What to take away

- Adopt by seam, not by stack.
- Prove evidence and recovery before scaling autonomy.
- Keep the exit path open.
- A pilot that cannot fail safely is not a pilot.
