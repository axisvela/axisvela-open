# Capability planning

A plan is only useful if it can be executed safely and checked afterward. The
ecosystem separates five steps that are often collapsed into one prompt.

## 1. Goal

What outcome is wanted, under which constraints? A goal is not a plan. It should
state the desired result, the boundaries, and the evidence that would count as
success.

## 2. Plan

A plan turns goals, state, capabilities, and constraints into a structured,
revisable artifact. It should be explainable and verifiable before execution.

Project: [ORCHADYN](../projects/orchadyn.md).

## 3. Capability governance

Before a step runs, the system needs to know whether the capability exists, who
may invoke it, under which policy, and with what audit. A capability catalog
makes this explicit.

Project: [MODUREGIS](../projects/moduregis.md). Authorization is evaluated by
[AEGIVELA](../projects/aegivela.md).

## 4. Execution

Long-running work needs durability: retries, compensation, recovery, and a
recorded history. A process instance should survive a crash without repeating
side effects.

Project: [RHEOVELA](../projects/rheovela.md).

## 5. Human decision and verification

High-risk steps may need approval, exception handling, or intervention. The
outcome may need verification against the original intent.

Projects: [SYMBIVELA](../projects/symbivela.md) for human control,
[TEKMOVELA](../projects/tekmovela.md) for verification.

## Why separate the steps

- **Each step has a different artifact.** Goal, plan, capability decision,
  process history, approval, and verification result are not the same thing.
- **Each step has a different owner.** Business, architecture, platform,
  security, operations, and assurance teams can own their own boundary.
- **Each step can be inspected.** Collapsing them into one model call makes the
  decision opaque and the evidence weak.

## A practical test

For a proposed autonomous process, ask:

- Can I see the plan before it runs?
- Can I name the capability and policy for each step?
- If step 3 fails, can the process recover without repeating step 2?
- Who approves the high-risk step?
- What evidence proves the outcome?

If the answers are “it is all in the agent,” the process is not yet plannable,
governable, or verifiable.
