# EIDOVELA

**Repository:** [axisvela/eidovela-open](https://github.com/axisvela/eidovela-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Trust and knowledge

> A native identity provider for agents: lifecycle, trust domains, and workload
> attestation.

## The problem

Agents are often authenticated with long-lived API keys shared between
workloads. That makes identity coarse, revocation slow, and provenance weak. An
agent should be able to prove *which workload* it is, *which tenant* it belongs
to, and *how long* the credential is valid.

EIDOVELA applies identity-provider discipline to agents.

## What it provides

- Agent lifecycle and identity issuance.
- Tenant trust domains.
- Workload attestation using Kubernetes, SPIFFE, or mTLS.
- `private_key_jwt` enrollment.
- Proof-of-possession-bound tokens.
- OIDC interfaces and SDKs.
- Conformance fixtures and examples.

## Why it matters

- **Short-lived, bound credentials.** Tokens are tied to a workload and a proof
  of possession, not just a string.
- **Trust domains.** Multi-tenant systems can separate identity roots.
- **Lifecycle-aware.** Identity is issued, rotated, and revoked as part of agent
  lifecycle.

## How it fits

EIDOVELA answers “who is this agent?” [NOMIVELA](nomivela.md) records the agent
and its authority bindings; [AEGIVELA](aegivela.md) decides what the identity may
do. Together they form the identity, registry, and authorization planes.

## Start

- [Eidovela Open repository](https://github.com/axisvela/eidovela-open)
