# Governance maturity

This is a practical maturity model for agent governance. It is **not** a
certification or a standard. Use it to locate the next useful step.

| Level | Characteristics | Evidence | Typical risk |
| --- | --- | --- | --- |
| **0. Ad hoc** | Agents are built per project; permissions are broad; logs are informal | Screenshots, chat transcripts | Unbounded actions, no audit |
| **1. Instrumented** | Identity, logs, and basic metrics exist; tools are listed | Logs, metrics | Visibility without enforcement |
| **2. Controlled** | Deny-by-default capabilities, policy at boundaries, sandboxing | Policy decisions, effect records | Controls exist but are not tested |
| **3. Assured** | Verification contracts, reproducible tests, release gates, approvals | Verification evidence, approval records | Assurance is partial or manual |
| **4. Adaptive** | Change control, simulation, re-verification, measured governance load | Evidence chain, experiment records | Complexity and governance overhead |

## How to progress

- **0 → 1:** Inventory agents, tools, and data. Add identity and basic traces.
- **1 → 2:** Move policy out of prompts. Add capability allowlists, sandboxes,
  and effect records.
- **2 → 3:** Add verification contracts, release gates, and human approvals for
  high-risk actions.
- **3 → 4:** Add simulation, change control, and re-verification. Measure whether
  governance is helping or destabilizing.

Do not skip levels. A system with verification but no identity cannot attribute
results. A system with policy but no evidence cannot prove it worked.

## The maturity trap

More governance is not always better. UAD’s critical-threshold result suggests
that badly designed enforcement can destabilize behavior. Maturity is not
“more controls”; it is controls that are enforceable, proportionate, and
measured.

## A self-assessment

- Can I list every agent and its owner?
- Can I name the capabilities each agent may use?
- Is policy enforced outside the prompt?
- Can I reconstruct a material action from evidence?
- Are high-risk actions approved by a human?
- Do I re-verify after model or policy changes?
- Do I measure the cost of governance?

## Related

- [Governed autonomy](governed-autonomy.md)
- [UAD](../theory/uad.md) — governance dynamics.
- [Adoption path](../practice/adoption.md)
