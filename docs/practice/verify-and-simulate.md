# Verify and simulate

Probabilistic systems cannot be certified by a single passing run. This guide
uses [TEKMOVELA](../projects/tekmovela.md) for verification and
[PEIRAVELA](../projects/peiravela.md) for simulation.

## 1. Define the observable behavior

Start with acceptance criteria that can be checked:

- what output is required;
- what must never happen;
- what tolerance is allowed;
- which evidence counts as proof.

Avoid criteria like “the answer is good.” Define the observable behavior and the
evaluation method.

## 2. Write a verification contract

A verification contract turns intent into a testable statement. It should include:

- the scenario;
- the preconditions;
- the steps;
- the expected observations;
- the failure conditions;
- the evidence to retain.

TEKMOVELA’s model is built around contracts, governed harnesses, and
trace-linked evidence.

## 3. Make the test reproducible

- pin the model and endpoint;
- pin prompts and tool versions;
- control randomness where possible;
- record seeds;
- isolate external dependencies;
- version the test data.

A test that depends on a live third-party system is not reproducible.

## 4. Test the distribution, not one trace

Following the [PPES](../theory/ppes.md) view, behavior is probabilistic. Run the
contract multiple times and measure:

- success rate and confidence interval;
- failure modes and their frequency;
- cost and latency distributions;
- sensitivity to prompt, model, and context changes.

A single green run is a data point, not assurance.

## 5. Simulate before production

Use [PEIRAVELA](../projects/peiravela.md) for high-risk changes:

- define the world and scenario;
- vary perturbations and controls;
- run a reproducible matrix;
- retain provenance-complete evidence;
- compare outcomes across versions.

Simulation is especially important for physical autonomy, policy changes, and
recovery strategies.

## 6. Gate the release

A release gate should answer:

- Which contracts passed, and with what statistical confidence?
- What changed since the last verified version?
- What evidence supports the decision?
- What is the rollback path?
- Who approved the exception, if any?

## A verification checklist

- [ ] Acceptance criteria are observable and testable.
- [ ] The contract is versioned.
- [ ] The environment is pinned.
- [ ] The test is repeated enough to make a distributional claim.
- [ ] Failure modes are classified.
- [ ] Evidence is retained and linked.
- [ ] A model or policy change triggers re-verification.
- [ ] The release has a rollback path.

## Anti-patterns

- One happy-path run.
- Testing the prompt instead of the behavior.
- Changing the model without re-running the contract.
- Simulation without provenance.
- A gate that can be bypassed silently.

## Next

- [End to end](end-to-end.md) — put verification in the full workflow.
- [Reliability](../concepts/reliability.md) — failure and recovery concepts.
