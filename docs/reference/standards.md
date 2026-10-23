# Standards and protocols

The architecture uses established standards where they exist. This page lists the
ones that matter most, with a note on how they relate to the ecosystem.

## Contracts and data

| Standard | What it is | Where it fits |
| --- | --- | --- |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | HTTP API description format | Product APIs and SDK contracts |
| [JSON Schema](https://json-schema.org/draft/2020-12) | Schema language for JSON data | Harmovela events, tool inputs, contracts |
| [JSON-RPC](https://www.jsonrpc.org/specification) | Remote procedure call protocol | Mnemovela and runtime interfaces |
| [gRPC](https://grpc.io/docs/) | RPC framework | High-throughput service interfaces |
| [CloudEvents](https://cloudevents.io/) | Event envelope specification | Event interoperability (where used) |

## Identity and security

| Standard | What it is | Where it fits |
| --- | --- | --- |
| [OAuth 2.0](https://oauth.net/2/) | Authorization framework | Delegated access |
| [OpenID Connect](https://openid.net/connect/) | Identity layer on OAuth 2.0 | Agent identity provider interfaces |
| [SPIFFE](https://spiffe.io/) | Workload identity framework | Workload attestation |
| [W3C DID](https://www.w3.org/TR/did-core/) | Decentralized identifiers | Identity patterns (design space) |
| [mTLS](https://datatracker.ietf.org/doc/html/rfc8705) | Mutual TLS | Workload authentication |
| [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) | Zero trust architecture | Trust-boundary design |

## Telemetry and operations

| Standard | What it is | Where it fits |
| --- | --- | --- |
| [OpenTelemetry](https://opentelemetry.io/) | Traces, metrics, logs | Runtime and gateway telemetry |
| [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) | Naming conventions for telemetry | Consistent traces and metrics |
| [SLSA](https://slsa.dev/) | Supply-chain levels | Build and artifact integrity |
| [CycloneDX](https://cyclonedx.org/) | SBOM format | Software and skill inventories |

## Architecture practice

| Standard | What it is | Where it fits |
| --- | --- | --- |
| ISO/IEC/IEEE 42010 | Architecture description | Viewpoints and concerns |
| [TOGAF](https://www.opengroup.org/togaf) | Enterprise architecture framework | Portfolio and method context |
| [ArchiMate](https://www.opengroup.org/archimate-forum/archimate-overview) | Architecture modeling language | Enterprise architecture models |
| C4 | Software architecture diagrams | System/container/component views |
| arc42 | Architecture documentation template | Document structure |

## Risk and security frameworks

| Framework | What it is | Where it fits |
| --- | --- | --- |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | AI risk management framework | Governance and risk framing |
| [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | LLM application risks | Threat modeling |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Application security verification | Security review |

## Protocols in the ecosystem

- [MCP](https://modelcontextprotocol.io/) — tool and context integration.
- [A2A](https://github.com/a2aproject/A2A) — agent-to-agent interaction patterns.
- Harmovela — asynchronous coordination protocol (see
  [the project page](../projects/harmovela.md)).

## How to use this page

Standards are tools, not badges. A project “using” a standard should be able to
show the contract, the conformance evidence, and the boundary where the standard
is enforced. If it cannot, the standard is a label, not an architecture.
