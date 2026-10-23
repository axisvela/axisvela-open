# Governed autonomy

Autonomy is not a binary. A system can be autonomous in *what it decides* while
remaining bounded in *what it is allowed to do*, *what it must record*, and
*when a human must decide*.

Governed autonomy is the discipline of making those boundaries explicit.

## Three questions

Every autonomous action should be answerable against three questions.

### 1. What is allowed?

Before execution, the system needs an explicit answer about capabilities, data,
and side effects. That answer can come from a capability catalog, a policy
decision, a sandbox, a lease, or a combination. The important property is that
the answer exists *before* the action, not after.

Related: [MODUREGIS](../projects/moduregis.md),
[AEGIVELA](../projects/aegivela.md), [PRAXOVELA](../projects/praxovela.md).

### 2. What actually happened?

Intent and effect are different. A governed system records the effect: what was
invoked, with which inputs, under which policy, with which result, and how it
can be recovered. Without this, debugging and audit become archaeology.

Related: [PRAXOVELA](../projects/praxovela.md),
[RHEOVELA](../projects/rheovela.md),
[TEKMOVELA](../projects/tekmovela.md).

### 3. Who decided?

High-risk actions need a named decision path: an owner, an approval, a
revocation route, and a way to intervene. “The agent decided” is not an
accountability model.

Related: [SYMBIVELA](../projects/symbivela.md),
[AEGIVELA](../projects/aegivela.md),
[EIDOVELA](../projects/eidovela.md).

## Why this matters

Most agent failures are not model failures. They are boundary failures:

- a tool was available when it should not have been;
- an action was taken without a record;
- a human could not tell what the agent was about to do;
- a process could not be recovered without repeating effects.

Governed autonomy addresses those failures structurally, at the seams where
they occur.

## A practical test

For any autonomous workflow, ask:

1. Can I name the policy or capability that authorized each step?
2. Can I reconstruct the effect history from artifacts?
3. Can I point to the person or system that approved the high-risk step?
4. Can I stop, revoke, or recover without improvising?

If any answer is “we would have to check the logs,” the workflow is not yet
governed. It is merely automated.
