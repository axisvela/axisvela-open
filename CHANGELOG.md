# Changelog

This changelog versions the **AxisVela Open documentation and project index**.
It does not version the individual projects. Each product repository carries its
own releases.

## v0.2.0 — 2026-10-23

Publication and discovery release.

### Added

- Site-wide language selector for English and Chinese.
- [Documentation versioning](docs/reference/versioning.md) page, including the
  relationship between documentation tags and product versions.
- [Changelog](docs/reference/changelog.md) and
  [roadmap](docs/reference/roadmap.md) pages.
- `CITATION.cff` for machine-readable citation.
- `robots.txt` for crawlers.
- Version groups in the English and Chinese reference sections.

### Changed

- README version links now point to `v0.2.0`.

## v0.1.0 — 2026-10-23

First complete public snapshot.

### Added

- Six documentation sections: Products & projects, Agent theory, Agent
  architecture, Agent practice, Concepts & terminology, and Reference.
- 25 project entries with problem, value, license, and relationship data in
  `projects.yaml`.
- Agent theory pages grounded in Huiwen Han’s research — UAD, DIKCA, IIC/AOP,
  PPES, enterprise agent taxonomy, multi-agent dynamics, and agent economics —
  with DOI links and publication-status notes.
- Architecture pages: reference architecture, runtime, control planes, contracts,
  knowledge, evidence, deployment, and security.
- Practice guides using AxisVela end to end: build, govern, memory/context,
  durable process, external systems, verification/simulation, and adoption.
- A comprehensive terminology section with 100+ terms.
- Complete Chinese documentation under `docs/zh/`, with language switching and a
  Chinese product index.
- MkDocs Material site with Mermaid diagrams and GitHub Pages deployment.

### Known limitations

- Licenses marked “See repository” must be checked in the product repository.
- Product availability and production readiness vary; product repositories are
  authoritative.
- Some theoretical sources are preprints or working papers; check the DOI record
  for publication status.
- The documentation is a snapshot; project pages may lag the product repositories.
