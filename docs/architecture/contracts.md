# Contracts and interfaces

AxisVela composes independent products through **versioned contracts**, not a
shared runtime kernel. This page explains what that means in practice.

## What counts as a contract

| Contract type | Example | What it protects |
| --- | --- | --- |
| HTTP/OpenAPI | Rheovela worker API | Request/response compatibility |
| JSON Schema | Harmovela events and tasks | Data shape and validation |
| Protocol specification | Harmovela coordination dimensions | Semantics across implementations |
| SDK | AEGIVELA and EIDOVELA identity SDKs | Language-level ergonomics and compatibility |
| Conformance fixtures | Cross-language test vectors | Behavioral equivalence |
| Signed artifact | Skill bundles, release binaries | Provenance and integrity |
| CLI contract | `tek`, `rheo`, `archharness` | Automation stability |

A contract is not a document that describes an implementation. It is the
boundary that lets the implementation change without breaking consumers.

## Versioning

A practical contract policy:

1. **Version the interface, not the internals.** Consumers depend on the
   contract, not the runtime.
2. **Make breaking changes explicit.** Use a new major version or a new contract
   path.
3. **Keep a compatibility window.** Deprecate with a date and a migration path.
4. **Test the contract.** Conformance fixtures are part of the product.
5. **Publish the open surface.** Contracts, SDKs, and examples should be
   discoverable without a sales call.

## Independent products, not a monolith

The alternative to contracts is a shared kernel: one runtime that owns every
domain. That is simpler inside one product and more expensive everywhere else. It
couples release cadence, failure modes, and governance.

Contracts accept integration discipline in exchange for:

- independent versioning;
- replaceable implementations;
- clean licensing boundaries;
- organizational separation.

## Examples in the ecosystem

- **PRAXO-CORE seams.** Model, tool, memory, event, policy, sandbox, checkpoint,
  and execution are interfaces. A product or integrator supplies adapters.
- **Harmovela.** The protocol defines coordination semantics across languages and
  transports, with conformance fixtures.
- **Rheovela.** Worker SDKs and an HTTP Worker API let existing services
  participate without rewriting in Go.
- **Open surfaces.** The `*-open` repositories publish contracts and SDKs; the
  core or enterprise runtime may be separate.

## Anti-patterns

- **Shared database as integration.** It couples schemas and bypasses policy.
- **Copy-paste SDK.** A fork of the client is not a contract.
- **Undocumented behavior.** If consumers rely on it, it is part of the
  contract, whether you admit it or not.
- **Silent breaking change.** A patch release that changes semantics destroys
  trust faster than a major version.
- **Contract without conformance.** “Compatible” needs tests, not a claim.

## A useful test

Ask: *if we replaced the implementation behind this interface tomorrow, what
would break?* If the answer is “everything,” it is a kernel, not a contract. If
the answer is “nothing that depends only on the contract,” the boundary is real.
