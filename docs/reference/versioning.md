# Documentation versioning

[English](versioning.md) | [中文](../zh/reference/versioning.md)

This repository versions the **AxisVela Open documentation and project index**.
It does not version the individual products. Each product repository carries its
own releases.

## Tag scheme

| Tag | Meaning |
| --- | --- |
| `v0.1.0` | First complete public snapshot: six sections, English and Chinese. |
| `v0.2.0` | Publication and discovery improvements: language selector, versioning, changelog, roadmap, citation. |

Tags are annotated and immutable. A published tag is never moved.

## What changes a version

- **Minor (`0.x`)** — new sections, new project entries, substantial content or
  navigation changes, new translations.
- **Patch (`0.x.y`)** — corrections, broken links, small clarifications.
- **Major (`1.0.0`)** — a stable documentation contract, or a breaking change to
  the `projects.yaml` schema.

Before 1.0, the documentation is explicitly a snapshot. Product pages may lag the
product repositories.

## `projects.yaml` schema

The machine-readable index has its own `schema_version` (currently `1`). A
breaking change to the field structure bumps the schema version, independently of
the documentation tag.

## Product versions are separate

A documentation tag does not pin product versions. If you need reproducibility,
record the product tags or commit hashes you used alongside the documentation
version.

## Citing a version

Use the tag URL, for example:

```text
AxisVela Open documentation v0.2.0
https://github.com/axisvela/axisvela-open/releases/tag/v0.2.0
```

See [`CITATION.cff`](https://github.com/axisvela/axisvela-open/blob/main/CITATION.cff)
for a machine-readable citation.
