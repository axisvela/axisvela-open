# DIDACTOVELA

English | [中文](../zh/projects/didactovela.md)

**Repository:** [axisvela/didactovela-open](https://github.com/axisvela/didactovela-open)
**License:** Apache-2.0 open source; AGPL-3.0-only core; proprietary EE.
**Language:** Go; **Layer:** Learning

> Intended scope: data and learned-policy lifecycle, not runtime authorization.

## Status and available baseline

**Unreleased 0.1.0, bootstrap only.** Implemented surfaces are operational
health, schema-readiness and version APIs, plus a source Go version client.
Schema readiness is an operational check, not a dataset or training API.
There is no domain execution, dataset or training capability, robot integration,
binary release or published SDK. Source clients do not imply SDK publication.

## The problem and intended scope

Learning inputs and candidate artifacts need traceable ownership without
turning training into deployment authority. Future scope is capture admission,
immutable source manifests, episodes, dataset snapshots, labels, reproducible
training recipes/results and candidate learned-policy artifacts. None of these
domain capabilities is shipped.

## Authority boundaries

- [AKROVELA](akrovela.md) local capture and [KINETOVELA](kinetovela.md) effect
  references are potential inputs, not implemented ingestion paths.
- [PEIRAVELA](peiravela.md) owns experiment worlds, perturbations and raw
  SimulationEvidence. DIDACTOVELA's intended datasets do not replace that authority.
- [Noetivela](noetivela.md) owns production models and inference endpoints.
  A candidate checkpoint is inert until explicitly admitted and authorized for
  deployment; training must not activate endpoints or command actuators.
- [TEKMOVELA](tekmovela.md) owns independent assurance verdicts. Training metrics
  and execution success cannot issue their own assurance pass.
- [ONTOVELA](ontovela.md) owns operational world truth, not raw learning episodes.
  Simulated or recorded learning state must not overwrite operational reality.
- A learned policy is a model, not an [AEGIVELA](aegivela.md) authorization policy;
  it grants no execution authority or expanded capability scope.

All relationships above are planned boundaries, not verified integrations.
Source rights, provenance, label admission and training/evaluation isolation are
requirements for future learning work, not capabilities of this bootstrap.

## Licensing and start

Open source in the public repository is Apache-2.0; the runtime core is
AGPL-3.0-only and EE extensions are proprietary. Any future distributed binary
retains its own license; placing it in an open repository does not relicense it.
See the [license index](../reference/licenses.md) and the
[public repository](https://github.com/axisvela/didactovela-open) for authoritative
availability and license notices.
