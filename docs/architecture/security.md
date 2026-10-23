# Security model

Agent security is not only model security. The attack surface includes the
model, the context, the tools, the identity, the network, the supply chain, and
the human approval path.

This page is a practical threat model for the architecture. It is not a
replacement for a product’s `SECURITY.md`.

## Threats and controls

| Threat | What it looks like | Primary controls |
| --- | --- | --- |
| **Prompt injection** | Untrusted content instructs the agent to ignore policy or exfiltrate data | Treat retrieved content as data; separate control from context; policy outside the prompt |
| **Tool abuse** | The agent invokes a destructive or over-broad tool | Capability allowlist, least privilege, sandbox, approval |
| **Credential leakage** | Secrets appear in prompts, logs, or model calls | Gateway credential injection, secret redaction, scoped tokens |
| **Data exfiltration** | The agent sends sensitive data to an external endpoint | Egress gateway, allowlisted destinations, DLP-style policy |
| **Runaway delegation** | Authority expands across agents or loops | Scope attenuation, delegation limits, revocation, loop bounds |
| **Supply-chain compromise** | A skill, plugin, or artifact is malicious or altered | Signatures, provenance, SBOM, allowlisted registries |
| **Agent worms** | An agent propagates malicious instructions or actions across agents | Segmentation, identity, signed instructions, monitoring, containment |
| **Model supply chain** | A model or adapter behaves differently than expected | Provider governance, evaluation, semantic certification, rollback |
| **Denial of wallet** | The agent consumes unbounded tokens or tool calls | Budgets, rate limits, step limits, routing policy |
| **Unsafe physical action** | A robot or edge agent exceeds its envelope | Mission bounds, interlocks, simulation, human override |

## Agent worms

The paper *A Four-Layer Taxonomy of AI Agent Worm Propagation* proposes a
structured way to classify how malicious behavior spreads across agent systems.
Use it as a threat-modeling aid: identify the propagation layer, then design
containment at that layer.

The general security principles still apply:

- segment agents by trust domain;
- require identity for agent-to-agent interaction;
- sign and verify instructions and artifacts;
- bound delegation and recursion;
- monitor for abnormal propagation;
- make containment and revocation fast.

## Controls mapped to architecture

| Boundary | Control | AxisVela pattern |
| --- | --- | --- |
| Identity | Workload identity, proof of possession | EIDOVELA, NOMIVELA |
| Authorization | Policy decision and PEP enforcement | AEGIVELA |
| Capability | Allowlist, metadata, invocation audit | MODUREGIS |
| Execution | Sandbox, step limits, budgets | PRAXOVELA, PRAXO-CORE |
| Network | Egress allowlist, credential injection | LIMENORA |
| Artifact | Signing, provenance, verification | SYNDOVELA, TEKMOVELA |
| Human | Approval, intervention, revocation | SYMBIVELA |
| Evidence | Tamper-evident records | Effect ledger, process history, verification bundles |

## A security review checklist

1. What can the agent read, and where does that data come from?
2. What can the agent invoke, and what is the blast radius?
3. Where are credentials stored and injected?
4. Which destinations can the agent reach?
5. Can authority be delegated? Is it attenuated and revocable?
6. What happens if retrieved content is malicious?
7. What is signed, and what verifies the signature?
8. What are the budgets and step limits?
9. Can a human stop the agent quickly?
10. What evidence exists after an incident?
11. Has the behavior been tested under adversarial conditions?
12. Is there a rollback path for model, policy, and skill changes?

## What to take away

- Separate control from context; a prompt is not a security boundary.
- Put enforcement at the boundary the attacker must cross.
- Assume delegation will be abused; design attenuation and revocation.
- Treat agents as a supply-chain and identity problem, not only a model problem.
- Evidence is a security control: it enables detection, response, and learning.
