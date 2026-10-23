# AEGIVELA

**Repository:** [axisvela/aegivela-open](https://github.com/axisvela/aegivela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Trust and knowledge

> Authorization, delegation, approvals, revocation, and security evidence for
> agents.

## The problem

“The agent has a token” is not an authorization model. Agents act on behalf of
users and systems, delegate work to other agents, and need approval for
high-risk actions. Authority must be attenuable, revocable, and evidenced.

AEGIVELA is the authorization fabric that answers those questions.

## What it provides

- Policy evaluation and decision contracts.
- Scope attenuation for delegated authority.
- Approval and execution-grant flows.
- Revocation.
- Attestation policy.
- A Policy Enforcement Point (PEP) SDK.
- Security evidence for decisions.

## Why it matters

- **Delegation without losing control.** Authority can be narrowed as it moves
  between agents.
- **Revocation is real.** Grants can be withdrawn.
- **Evidence for every decision.** Security outcomes are inspectable.

## How it fits

AEGIVELA consumes verified identity from [EIDOVELA](eidovela.md) and registry
context from [NOMIVELA](nomivela.md). It provides the policy seam used by
[PRAXO-CORE](praxo-core.md) and enforcement points across the ecosystem.

## Start

- [Aegivela Open repository](https://github.com/axisvela/aegivela-open)
