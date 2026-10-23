# 标准与协议

[English](../../reference/standards.md) | 中文

架构在存在标准的地方使用标准。本页列出最重要的标准，以及它们与生态的关系。

## 契约与数据

| 标准 | 是什么 | 用在哪里 |
| --- | --- | --- |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | HTTP API 描述格式 | 产品 API 与 SDK 契约 |
| [JSON Schema](https://json-schema.org/draft/2020-12) | JSON 数据 schema 语言 | Harmovela 事件、工具输入、契约 |
| [JSON-RPC](https://www.jsonrpc.org/specification) | 远程过程调用协议 | Mnemovela 与运行时接口 |
| [gRPC](https://grpc.io/docs/) | RPC 框架 | 高吞吐服务接口 |
| [CloudEvents](https://cloudevents.io/) | 事件信封规范 | 事件互操作（使用处） |

## 身份与安全

| 标准 | 是什么 | 用在哪里 |
| --- | --- | --- |
| [OAuth 2.0](https://oauth.net/2/) | 授权框架 | 委托访问 |
| [OpenID Connect](https://openid.net/connect/) | OAuth 2.0 上的身份层 | Agent 身份提供者接口 |
| [SPIFFE](https://spiffe.io/) | 工作负载身份框架 | 工作负载证明 |
| [W3C DID](https://www.w3.org/TR/did-core/) | 去中心化标识符 | 身份模式（设计空间） |
| [mTLS](https://datatracker.ietf.org/doc/html/rfc8705) | 双向 TLS | 工作负载认证 |
| [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) | 零信任架构 | 信任边界设计 |

## 遥测与运维

| 标准 | 是什么 | 用在哪里 |
| --- | --- | --- |
| [OpenTelemetry](https://opentelemetry.io/) | 追踪、指标、日志 | 运行时与网关遥测 |
| [OpenTelemetry 语义约定](https://opentelemetry.io/docs/specs/semconv/) | 遥测命名约定 | 一致的追踪与指标 |
| [SLSA](https://slsa.dev/) | 供应链等级 | 构建与产物完整性 |
| [CycloneDX](https://cyclonedx.org/) | SBOM 格式 | 软件与技能清单 |

## 架构实践

| 标准 | 是什么 | 用在哪里 |
| --- | --- | --- |
| ISO/IEC/IEEE 42010 | 架构描述 | 视点与关注点 |
| [TOGAF](https://www.opengroup.org/togaf) | 企业架构框架 | 组合与方法上下文 |
| [ArchiMate](https://www.opengroup.org/archimate-forum/archimate-overview) | 架构建模语言 | 企业架构模型 |
| C4 | 软件架构图 | 系统/容器/组件视图 |
| arc42 | 架构文档模板 | 文档结构 |

## 风险与安全框架

| 框架 | 是什么 | 用在哪里 |
| --- | --- | --- |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | AI 风险管理框架 | 治理与风险框定 |
| [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | LLM 应用风险 | 威胁建模 |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | 应用安全验证 | 安全评审 |

## 生态中的协议

- [MCP](https://modelcontextprotocol.io/) — 工具与上下文集成。
- [A2A](https://github.com/a2aproject/A2A) — Agent 间交互模式。
- Harmovela — 异步协调协议（见[项目页](../projects/harmovela.md)）。

## 如何使用本页

标准是工具，不是徽章。一个“使用”标准的项目应能展示契约、一致性证据，以及标准被执行
的边界。如果不能，标准只是标签，不是架构。
