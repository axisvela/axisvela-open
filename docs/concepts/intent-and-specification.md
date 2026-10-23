# Intent and specification

An agent needs to know what is wanted. That sounds simple, but “what is wanted”
is usually a mixture of goal, context, constraints, and acceptance criteria. When
those are collapsed into one prompt, the system loses the ability to check
whether it succeeded.

## Four separate things

| Element | Question | Example |
| --- | --- | --- |
| **Goal** | What outcome is wanted? | Resolve the fulfillment exception |
| **Context** | What is relevant now? | Order state, inventory, policy |
| **Constraint** | What must not happen? | No refund above 500 without approval |
| **Acceptance** | How do we know it worked? | Order shipped or refunded, evidence retained |

The [Prompt Conflation Fallacy](../theory/intent-aop.md) names the mistake of
treating all four as “the prompt.”

## Why separation helps

- **Testability.** Acceptance criteria can become verification contracts.
- **Governance.** Constraints can be enforced by policy, not just described.
- **Debuggability.** When the outcome is wrong, you can see which element failed.
- **Reusability.** The same goal can be planned differently under different
  constraints.

## Specification quality

A useful specification is:

- **explicit** about the outcome;
- **bounded** by constraints and capabilities;
- **observable** in its acceptance criteria;
- **versioned** when it changes;
- **linked** to the evidence that proves it.

This is the practical side of Intent-Conditioned Computation and Agent-Oriented
Programming: the developer specifies intent, constraints, and feedback, and the
agent determines the execution path.

## A checklist

- [ ] The goal is stated as an outcome.
- [ ] The constraints are enforceable, not just mentioned.
- [ ] The acceptance criteria are observable.
- [ ] The required context is identified.
- [ ] The specification is versioned.
- [ ] The evidence plan is defined.

## Related

- [Intent, AOP, and control](../theory/intent-aop.md)
- [Capability planning](capability-planning.md)
- [Verification and simulation](../practice/verify-and-simulate.md)
