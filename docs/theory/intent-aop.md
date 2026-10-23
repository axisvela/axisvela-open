# Intent, AOP, and control

**Sources:** Huiwen Han, *Intent-Conditioned Computation* (2026),
[doi:10.22541/au.177524397.72082163/v1](https://doi.org/10.22541/au.177524397.72082163/v1);
*Agent-Oriented Programming: Foundations of a Semantic Paradigm for the LLM Era*
(2026), [doi:10.2139/ssrn.6563278](https://doi.org/10.2139/ssrn.6563278).

> In stored-program computing, the developer specifies control flow. In
> intent-conditioned computing, the developer specifies intent, constraints, and
> feedback, and a model determines the execution path.

## Intent-Conditioned Computation (IIC)

IIC is a complementary abstraction for systems built on foundation models. It
does not replace classical computing. It names a different locus of control:

| Stored-program computing | Intent-conditioned computing |
| --- | --- |
| Program encodes explicit control flow | Intent conditions a learned policy |
| Execution is deterministic | Execution is probabilistic and context-sensitive |
| Correctness is defined by the program | Correctness must be specified and evaluated |
| Inputs are data | Context, knowledge, and control are first-class |

IIC identifies five functional roles:

1. **Model capabilities** — the learned policy engine.
2. **Control intentions** — goals, constraints, and feedback.
3. **Externalized knowledge** — retrieved context and knowledge substrates.
4. **Deterministic code** — the parts that must remain reproducible.
5. **Data** — the inputs and state.

The practical claim is stratification: modern systems mix deterministic
infrastructure with intent-conditioned reasoning. The art is deciding which part
belongs to which paradigm.

## Agent-Oriented Programming (AOP)

AOP extends the argument into a programming paradigm. The developer specifies
intent, constraints, and feedback; a semantic agent determines the execution
path. The paper introduces the **Semantic Agent Framework (SAF)**, a seven-element
model `SAF = (G, O, C, A, D, R, F)`, and anchors it in the unified execution
formula:

```text
E(Cap, Intent, Context, Control) → O
```

The framework separates concerns that are often collapsed into one prompt. In
particular:

- **G** — goal specification;
- **D** — knowledge substrate;
- **R** — governance constraint.

Treating “the prompt” as one object conflates these layers. The paper calls this
the **Prompt Conflation Fallacy**.

## Why this matters for architecture

- **Specification is the bottleneck.** As generation becomes cheap, precision in
  intent, constraints, and acceptance criteria becomes the scarce input.
- **Governance is not context.** A rule placed in the context window is not the
  same as an enforced control.
- **The hybrid is the design.** Keep deterministic code where reproducibility is
  required; use intent-conditioned reasoning where flexibility is required.
- **Intent must be testable.** If the goal cannot be checked, the system cannot
  be verified.

## How it maps to AxisVela

- [PRAXO-CORE](../projects/praxo-core.md) separates the loop, model, tools,
  policy, sandbox, memory, and events — the seams that make IIC practical.
- [TAXOVELA](../projects/taxovela.md) is the ArchHarness case study cited in the
  IIC paper: a workflow that mixes deterministic gates with intent-conditioned
  design work.
- [ORCHADYN](../projects/orchadyn.md) turns goals and constraints into explicit
  plans; [MODUREGIS](../projects/moduregis.md) separates capability governance
  from the plan; [TEKMOVELA](../projects/tekmovela.md) turns acceptance criteria
  into verification contracts.

## What to take away

- Specify intent, constraints, and feedback separately.
- Do not put governance only in the prompt.
- Keep a deterministic spine for anything that must be reproducible.
- Make the goal checkable, or you cannot verify the agent.
