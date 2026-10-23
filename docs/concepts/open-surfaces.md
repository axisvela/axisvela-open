# Open surfaces

“Open source” and “open surface” are not the same claim. AxisVela uses both, and
the difference matters when you evaluate a project.

## Three levels

### Fully open

The repository contains the implementation under an open license.

- [PRAXO-CORE](../projects/praxo-core.md) — MIT.
- [TAXOVELA](../projects/taxovela.md) — MIT.
- [Harmovela](../projects/harmovela.md) — Apache-2.0 protocol and reference
  implementations.

### Open surface

The repository publishes the integration surface — contracts, SDKs, examples,
and sometimes binaries — under an open license. The runtime core or enterprise
edition may be developed separately.

Most `*-open` repositories in the ecosystem are this kind of surface. They are
designed to let you evaluate, integrate, and build without a commercial
commitment, but they are not a promise that the entire runtime is open source.

### Commercial or private

Some cores and enterprise editions are developed in private repositories. They
may add multi-tenancy, high availability, compliance packs, managed deployment,
or other operational features.

## How to evaluate an open surface

1. Read the `LICENSE` in the specific repository. It is authoritative.
2. Check what the repository actually contains: contracts, SDK, examples,
   binaries, or a runnable runtime.
3. Run the examples before assuming production readiness.
4. Check the release and support posture in the repository, not in a summary.
5. Ask what happens at the boundary: can you replace the implementation while
   keeping the contract?

## Why this model

A clean open surface lets a solo maintainer publish useful, testable interfaces
without pretending that every operational feature is free. It also keeps the
licensing boundary honest: the MIT framework and Apache-2.0 surfaces are
explicit, and the commercial editions are separate.

See the [licenses page](../reference/licenses.md) for the current map. When in
doubt, the repository wins.
