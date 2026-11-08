# AKROVELA

English | [中文](../zh/projects/akrovela.md)

**Repository:** [axisvela/akrovela-open](https://github.com/axisvela/akrovela-open)
**License:** Apache-2.0 open source; AGPL-3.0-only core; proprietary EE.
**Language:** Go; **Layer:** Physical / site execution

> Intended scope: governed edge and site execution, not fleet planning.

## Status and available baseline

**Unreleased 0.1.0, bootstrap only.** Implemented surfaces are operational
health, schema-readiness and version APIs, plus a source Go version client.
Schema readiness is an operational check, not a domain execution API.
There is no domain execution, dataset or training capability, robot integration,
binary release or published SDK. Source clients do not imply SDK publication.

## The problem and intended scope

Site execution needs an owner for what actually happened locally without
creating another Mission controller or durable workflow engine. Future scope
is local operation admission, execution attempts, node resource limits, durable
receipts and reconciliation. None of these domain capabilities is shipped.

## Authority boundaries

- [KINETOVELA](kinetovela.md) owns Mission, assignment and effect lifecycle.
  AKROVELA's intended local attempts and receipts cannot independently complete,
  reassign or compensate a Mission.
- [RHEOVELA](rheovela.md) owns durable cross-service Processes; a local journal
  is not a second workflow engine.
- [SYNDOVELA](syndovela.md) owns desired Bundle composition, ResolutionLocks and
  Runtime Profiles. Future artifact loading must not become runtime resolution.
- [MODUREGIS](moduregis.md) owns capability contracts and immutable references;
  [ORCHADYN](orchadyn.md) remains the planner.
- [PRAXO-CORE](praxo-core.md) remains the MIT Agent framework. Hosting an
  embedded runtime through a future adapter would not redefine Agent behavior.
- [DIDACTOVELA](didactovela.md) is the intended learning-data lifecycle owner,
  not a shipped capture destination.

All relationships above are planned boundaries, not verified integrations.
Robot-local safety, interlocks and emergency stops remain independent. No
offline execution or safety certification is implied by the bootstrap.

## Licensing and start

Open source in the public repository is Apache-2.0; the runtime core is
AGPL-3.0-only and EE extensions are proprietary. Any future distributed binary
retains its own license; placing it in an open repository does not relicense it.
See the [license index](../reference/licenses.md) and the
[public repository](https://github.com/axisvela/akrovela-open) for authoritative
availability and license notices.
