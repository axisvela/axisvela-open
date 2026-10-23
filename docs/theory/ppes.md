# PPES: probabilistic program execution semantics

**Sources:** Huiwen Han, *Probabilistic Program Execution Semantics for
Foundation Models* (2026),
[doi:10.2139/ssrn.7063738](https://doi.org/10.2139/ssrn.7063738); *PPES: A
Probabilistic Execution Semantics for Foundation Models* (Authorea, 2026),
[doi:10.22541/au.177212176.67413084/v2](https://doi.org/10.22541/au.177212176.67413084/v2).

> A foundation model is not a deterministic interpreter. It is a probabilistic
> execution engine with observable outputs and hidden latent state.

## The problem with classical semantics

Classical program semantics assumes a program maps inputs to outputs through
explicit control flow. That assumption supports debugging, testing, and
verification. Foundation-model systems violate it:

- the same prompt can produce different outputs;
- behavior depends on hidden state (for example, the KV cache);
- the “program” is distributed across weights, prompt, context, and runtime
  policy;
- correctness is distributional, not a single trace.

Treating such a system as a classical program produces misleading guarantees.

## The PPES view

PPES interprets a foundation model as a **probabilistic interpreter**:

- a runtime program corresponds to a prompt;
- execution state includes observable outputs and latent variables;
- transitions are governed by a learned Markov kernel;
- execution is resolved at inference time, a phase absent from classical
  computing.

The formal development uses measurable spaces and probability kernels, and
proves structural properties such as termination, trace monotonicity,
Lipschitz continuity under parameter perturbation, and the Markov property of
latent state. It also establishes a notion of semantic irreducibility: an
observable-only abstraction cannot fully capture the system.

## Why it matters

- **Verification must be distributional.** A single passing run is weak
  evidence. You need distributions, repeated trials, and statistical claims.
- **Prompt equivalence is a semantic question.** Two prompts are not equivalent
  because they look similar; they are equivalent relative to an observable
  behavior and a tolerance.
- **Model updates need semantic certification.** A new model version can change
  the distribution without changing the interface.
- **Latent state matters.** Caching, context, and runtime state are part of the
  execution semantics, not implementation details.

## How it maps to AxisVela

- [TEKMOVELA](../projects/tekmovela.md) turns acceptance criteria into
  verification contracts and reproducible tests — the practical counterpart of
  distributional verification.
- [PEIRAVELA](../projects/peiravela.md) runs governed experiments over
  scenario × perturbation × control × seed matrices, producing evidence that can
  be compared across model or policy changes.
- [NOETIVELA](../projects/noetivela.md) makes model/endpoint selection explicit,
  which is necessary when behavior is a property of the execution distribution.

## What to take away

- Do not claim correctness from one run.
- Define the observable behavior and the tolerance before testing.
- Treat model changes as semantic changes that require re-verification.
- Keep latent and runtime state in the evidence model.
