# Agent identity in three planes

Agent identity is often reduced to “an API key.” That collapses three different
problems into one weak mechanism. A useful model separates them.

## Plane 1: issuance

**Who is this workload, and can it prove it?**

An identity provider issues a credential after verifying the workload. The
credential should be short-lived and bound to a proof of possession, so a stolen
token is not enough. Workload attestation can use Kubernetes, SPIFFE, or mTLS.

Project: [EIDOVELA](../projects/eidovela.md).

## Plane 2: registry and namespace

**Which agent is this, who owns it, and what is its lifecycle state?**

Identity issuance is not a registry. An enterprise needs a system of record for
agents, namespaces, authority bindings, and lifecycle epochs. Without it,
identity is a stream of credentials with no inventory.

Project: [NOMIVELA](../projects/nomivela.md).

## Plane 3: authorization and delegation

**What may this agent do, on whose behalf, and with what evidence?**

Authorization evaluates policy, attenuates delegated authority, routes approvals,
supports revocation, and produces evidence. It consumes identity and registry
context but is a separate decision.

Project: [AEGIVELA](../projects/aegivela.md).

## Why the separation matters

- **Different failure modes.** A valid credential does not imply a valid
  authorization. A registered agent does not imply a trustworthy workload.
- **Different lifecycles.** Credentials rotate quickly; registry records live
  longer; policies change on business cadence.
- **Different audiences.** Security teams own issuance, platform teams own the
  registry, and application teams own policy.

## A common mistake

Using one long-lived token for many agents, then trying to recover attribution
from logs. The identity plane is not a logging problem. It has to be designed
before the agent acts.

## Related

- [Governed autonomy](governed-autonomy.md)
- [Evidence and auditability](evidence-and-audit.md)
- [MODUREGIS](../projects/moduregis.md) — capability authorization at
  invocation.
