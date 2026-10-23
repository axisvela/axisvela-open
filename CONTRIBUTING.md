# Contributing

This repository is the public map of the AxisVela project family. It documents
and indexes projects; it does not contain their source code.

## What belongs here

- Corrections and improvements to project descriptions, relationships, and
  concepts.
- New project entries, if the project has a public repository and a clear
  problem/value statement.
- Navigation, accessibility, and documentation-site improvements.
- Fixes to broken links or stale claims.

## What does not belong here

- Changes to a product’s implementation. Open an issue or pull request in that
  product’s repository instead.
- Confidential roadmap, customer, security, or commercial information.
- Marketing claims that cannot be checked against a repository or public
  artifact.

## Adding or changing a project

A project entry should answer four questions:

1. **What problem does it address?** Describe the failure or gap, not the
   feature list.
2. **What does it provide?** Name the concrete surface: contracts, SDK, runtime,
   examples, or binaries.
3. **Why does it matter?** Explain the practical consequence for a user.
4. **How does it fit?** Add the relationships, and say whether they are optional
   seams or required dependencies.

Also update:

- `docs/projects/index.md` — the human index.
- `docs/reference/relationships.md` — the edge list, if relationships change.
- `projects.yaml` — the machine-readable entry.
- `docs/reference/licenses.md` — if the license is newly verified.

## Style

- Prefer short sentences and concrete nouns.
- Link to the authoritative repository instead of copying its documentation.
- Say “open surface” when a repository contains contracts/SDKs but not the full
  runtime. Do not imply that every `*-open` repository is a complete open-source
  product.
- Keep claims testable. If a statement cannot be verified from a repository,
  release artifact, or public document, remove it or mark it as a design goal.
- Use the project name as it appears in the repository, even if the historical
  name is different. Note historical names explicitly.

## Pull requests

- Keep a pull request focused on one change.
- Describe what changed and why.
- Include the source for any new factual claim.
- Run `mkdocs build --strict` if you change the documentation site.

## License

By contributing documentation to this repository, you agree that your
contribution is licensed under Apache-2.0. Product repositories carry their own
licenses.
