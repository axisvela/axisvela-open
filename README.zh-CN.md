# AxisVela Open

**面向可治理自治的独立项目公开地图。**

[English](README.md) | 中文

**文档版本：** [v0.1.0](https://github.com/axisvela/axisvela-open/releases/tag/v0.1.0)

AxisVela 是一个独立维护的开源项目家族，面向构建和运行 Agent、工作流、机器人、
数字孪生以及连接它们的系统。各个项目共享同一种设计立场——以契约代替共享内核，
以证据代替断言，以人类控制代替盲目自动化——但每个产品都独立版本化，可以单独使用。

本仓库是地图，不是单体仓库。它说明每个项目要解决什么问题、提供什么价值，以及
这些项目之间如何衔接。

[从这里开始](docs/zh/start-here.md) · [产品与项目](docs/zh/projects/index.md) ·
[Agent 理论](docs/zh/theory/index.md) · [Agent 架构](docs/zh/architecture/index.md) ·
[Agent 实操](docs/zh/practice/index.md) · [概念与术语](docs/zh/concepts/index.md) ·
[参考](docs/zh/reference/index.md) · [机器可读索引](projects.yaml)

## 从问题出发，而不是从产品出发

| 如果你需要…… | 从这里开始 |
| --- | --- |
| 构建可治理、可嵌入的 Agent 循环 | [PRAXO-CORE](docs/zh/projects/praxo-core.md) — MIT Go 框架 |
| 理解整个生态如何组合 | [Enterprise Autonomy](docs/zh/projects/enterprise-autonomy.md) — 公开介绍与可运行示例 |
| 运行长期、可恢复的业务流程 | [RHEOVELA](docs/zh/projects/rheovela.md) — 持久化工作流平台 |
| 为 Agent 提供可验证身份与受限权限 | [EIDOVELA](docs/zh/projects/eidovela.md)、[NOMIVELA](docs/zh/projects/nomivela.md)、[AEGIVELA](docs/zh/projects/aegivela.md) |
| 在不绕过策略的前提下连接外部系统 | [LIMENORA](docs/zh/projects/limenora.md) — 受治理的集成网关 |
| 用 AI 助手设计和验证企业架构 | [TAXOVELA](docs/zh/projects/taxovela.md) — 架构技能包与 CLI |

## 这里的“可治理自治”指什么

可治理自治不是模型能力，而是一套运行纪律，围绕三个问题：

1. **允许做什么？** 能力、数据和副作用在执行前被显式策略约束。
2. **实际发生了什么？** 行动留下证据：效果账本、追踪、流程历史、仿真记录或验证结果。
3. **谁做的决定？** 高风险步骤有明确责任人、审批路径，以及干预、撤销和恢复机制。

不同项目在不同层次回答这些问题。
[概念部分](docs/zh/concepts/index.md)解释这些思想，
[生态地图](docs/zh/ecosystem-map.md)展示每个项目的位置。

## 一张图看懂

| 层次 | 覆盖内容 | 代表项目 |
| --- | --- | --- |
| 设计与标准 | 架构设计、验证与组合管理 | TAXOVELA、PAMP |
| 基础层 | Agent 框架、协调协议、开发协调 | PRAXO-CORE、Harmovela、COORDIVELA |
| 运行时与认知 | Agent 执行、记忆、推理路由 | PRAXOVELA、Mnemovela、Noetivela |
| 工作与能力 | 规划、能力治理、持久化流程 | ORCHADYN、MODUREGIS、RHEOVELA |
| 信任与知识 | 身份、注册、授权、知识锚定、世界模型 | EIDOVELA、NOMIVELA、AEGIVELA、GNOSIVELA、ONTOVELA |
| 边界与保障 | 集成、验证、仿真、技能供应链 | LIMENORA、TEKMOVELA、PEIRAVELA、SYNDOVELA |
| 人类与物理操作 | 人类监督、机器人集群控制 | SYMBIVELA、KINETOVELA |
| 项目计划 | 端到端组合与示例 | Enterprise Autonomy |

层次是阅读辅助，不是依赖链。产品通过版本化契约集成，可以独立采用。

## 开放接口层与商业版

- **完全开源项目：** PRAXO-CORE（MIT）、TAXOVELA（MIT）、Harmovela 协议（Apache-2.0）。
- **开放接口层：** 多数产品发布 Apache-2.0 的 `*-open` 仓库，包含契约、SDK、示例，
  有时包含二进制。运行时或企业版可能单独开发。
- **许可证不同：** 始终以具体仓库的 `LICENSE` 为准。参见
  [许可证](docs/zh/reference/licenses.md)。

实际含义：你可以评估接口并基于它构建，而不必购买任何东西；但开放接口层不等于
整个运行时都开源。

## 建议阅读顺序

| 如果你是…… | 建议阅读 |
| --- | --- |
| 刚接触这个生态 | [从这里开始](docs/zh/start-here.md) → [生态地图](docs/zh/ecosystem-map.md) → [产品与项目](docs/zh/projects/index.md) |
| 架构师 | [Agent 理论](docs/zh/theory/index.md) → [Agent 架构](docs/zh/architecture/index.md) → [Enterprise Autonomy](docs/zh/projects/enterprise-autonomy.md) |
| 开发者 | [构建 Agent](docs/zh/practice/build-an-agent.md) → [治理 Agent](docs/zh/practice/govern-an-agent.md) → [端到端](docs/zh/practice/end-to-end.md) |
| 研究者 | [Agent 理论](docs/zh/theory/index.md) → [研究地图](docs/zh/theory/research-map.md) → [阅读清单](docs/zh/reference/reading-list.md) |

## 仓库结构

- [`docs/zh/projects/`](docs/zh/projects/index.md) — 每个项目的目标、问题、价值与关系。
- [`docs/zh/theory/`](docs/zh/theory/index.md) — 理论主线：UAD、DIKCA、IIC/AOP、PPES、
  分类、多智能体动力学、经济学，并结合 Huiwen Han 的研究。
- [`docs/zh/architecture/`](docs/zh/architecture/index.md) — 运行时、控制平面、契约、
  知识、证据、部署与安全。
- [`docs/zh/practice/`](docs/zh/practice/index.md) — 以 AxisVela 为参考实现的分步指南。
- [`docs/zh/concepts/`](docs/zh/concepts/index.md) — 核心概念与完整术语表。
- [`docs/zh/reference/`](docs/zh/reference/index.md) — 关系、许可证、来源、标准与 FAQ。
- [`projects.yaml`](projects.yaml) — 机器可读的项目索引。
- [`llms.txt`](llms.txt) — 面向 AI 发现的紧凑索引。

## 状态

这些项目仍处于早期阶段。公开契约已版本化，但在仓库宣布 1.0 之前，API 可能在小版本
之间变化。每个项目的 `CHANGELOG.md`、`ROADMAP.md` 和发布标签是最终依据。

AxisVela 是由独立维护者维护的项目家族，不是公司。公开仓库是开放接口层；商业版和
企业版单独开发。

## 贡献、安全与许可证

- [贡献指南](CONTRIBUTING.md) — 文档修正、项目提案，以及本仓库与产品仓库的边界。
- [安全策略](SECURITY.md) — 私下报告漏洞。
- [行为准则](CODE_OF_CONDUCT.md)。
- 本仓库的文档与示例采用 Apache-2.0。产品仓库各自携带许可证。
