# Security

Agent security spans the model, context, tools, identity, network, supply chain,
and human approval path. A secure model does not make a secure agent.

## The main threat categories

| Threat | Control |
| --- | --- |
| Prompt injection | Treat retrieved content as data; keep policy outside the prompt |
| Tool abuse | Capability allowlist, least privilege, sandbox |
| Credential leakage | Gateway injection, scoped tokens, redaction |
| Data exfiltration | Egress allowlist, DLP policy, gateway |
| Runaway delegation | Scope attenuation, limits, revocation |
| Supply-chain compromise | Signing, provenance, SBOM, allowlists |
| Agent worms | Segmentation, identity, signed instructions, monitoring |
| Denial of wallet | Budgets, rate limits, step limits |
| Unsafe physical action | Mission bounds, interlocks, simulation, override |

## Identity is the first control

An agent should have a verifiable identity and a bounded authority scope. Shared
API keys make attribution and revocation weak. Workload identity,
proof-of-possession tokens, and a registry of authority bindings are the
foundation.

## Enforcement, not description

A rule in a system prompt is context. A rule enforced by a policy decision point,
a sandbox, or a gateway is control. Security architecture should place
enforcement where the action crosses a boundary.

## Agent worms

Agent worms propagate malicious instructions or actions across agents. The
defense is not only a better prompt filter; it is segmentation, identity,
signed instructions, bounded delegation, and fast containment. See the
[security model](../architecture/security.md) for the threat table.

## A checklist

- [ ] Identity is workload-based.
- [ ] Capabilities are deny-by-default.
- [ ] Egress is governed.
- [ ] Secrets are not in prompts or logs.
- [ ] Delegation attenuates and can be revoked.
- [ ] Artifacts are signed.
- [ ] Budgets and step limits exist.
- [ ] Human override works.
- [ ] Evidence supports incident response.

## Related

- [Security model](../architecture/security.md)
- [Agent identity](agent-identity.md)
- [Govern an agent](../practice/govern-an-agent.md)
