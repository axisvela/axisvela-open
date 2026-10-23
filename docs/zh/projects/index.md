# 产品与项目

[English](../../projects/index.md) | 中文

公开地图中的每个项目，以及它解决的问题与提供的价值。每行链接到更详细的中文页面与权威仓库。

部分条目是产品，部分是项目计划（例如 Enterprise Autonomy），部分是相邻或相关项目。
`projects.yaml` 中的 `kind` 字段记录这种区别。

## 总览

| 项目 | 层次 | 解决的问题 | 提供什么 | 许可证 |
| --- | --- | --- | --- | --- |
| [PRAXO-CORE](praxo-core.md) | 基础层 | 每个团队都重造 Agent 循环、提供商抽象、工具契约与治理 | MIT Go 框架：循环、原语、适配器、策略、沙箱、插件 | MIT |
| [TAXOVELA](taxovela.md) | 设计 | 架构产物不一致、不可验证，且与 AI 辅助设计脱节 | AI 原生架构技能与 CLI，带确定性验证门禁 | MIT |
| [Harmovela](harmovela.md) | 基础层 | MCP 覆盖同步调用，但不覆盖长期多智能体协调 | 事件、任务、状态、委托、恢复、治理的开放协议 | Apache-2.0 |
| [Harmovela Open](harmovela-open.md) | 基础层（配套） | 协议集成者需要示例与生态目录 | 可运行示例、生态注册表、编写指南 | Apache-2.0 |
| [COORDIVELA](coordivela.md) | 基础层 | 人与 Agent 在共享开发工作上重复或冲突 | 协调控制平面：租约、依赖、调度、干预 | Apache-2.0 |
| [PRAXOVELA](praxovela.md) | 运行时 | 本地 Agent 需要真实能力，但不能失去对副作用的控制 | 默认拒绝运行时：效果账本、恢复、可重放追踪 | Apache-2.0 接口层 |
| [Mnemovela](mnemovela.md) | 运行时 | Agent 记忆常是不透明向量库，没有生命周期 | 类型化、可分支、可审计的认知运行时与混合检索 | Apache-2.0 |
| [Noetivela](noetivela.md) | 运行时 | 模型/端点泛滥，策略、成本、质量与主权难管理 | 带契约与受治理路由的推理织构 | Apache-2.0 |
| [ORCHADYN](orchadyn.md) | 工作 | 把目标与约束变成可执行计划很随意 | 规划编译器：可验证、可修订计划 | Apache-2.0 |
| [MODUREGIS](moduregis.md) | 工作 | 企业无法安全发现、授权与审计能力 | 能力控制平面：目录、策略、调用、审计 | Apache-2.0 |
| [RHEOVELA](rheovela.md) | 工作 | 长期流程需要持久、恢复、审批与审计 | 面向受治理能力计划的持久工作流平台 | Apache-2.0 |
| [EIDOVELA](eidovela.md) | 信任 | Agent 需要可验证身份与工作负载证明，而不是共享密钥 | Agent 身份提供者：OIDC、持有证明令牌 | Apache-2.0 |
| [NOMIVELA](nomivela.md) | 信任 | 没有 Agent、命名空间与权限绑定的记录系统 | Agent 注册中心与命名空间权威 | Apache-2.0 |
| [AEGIVELA](aegivela.md) | 信任 | Agent 授权粗放，委托权限难撤销 | 授权、委托、审批、撤销与安全证据 | Apache-2.0 |
| [GNOSIVELA](gnosivela.md) | 知识 | 企业概念、主张与冲突碎片化、无锚定 | 语义与知识织构，带范围化知识锚定视图 | Apache-2.0 |
| [ONTOVELA](ontovela.md) | 知识 | 决策需要可信的当前与历史运营状态 | 有证据、双时间的运营世界模型与数字孪生 | 见仓库 |
| [LIMENORA](limenora.md) | 边界 | 外部 API/MCP/事件访问绕过策略并泄露凭据 | 受治理南北向集成网关与证据 | Apache-2.0 |
| [TEKMOVELA](tekmovela.md) | 保障 | Agent 系统难以验证，发布决定缺证据 | 验证契约、可复现测试、发布门禁 | Apache-2.0 |
| [PEIRAVELA](peiravela.md) | 保障 | 高风险自治变更无法在生产中安全试验 | 可能世界实验控制平面与仿真证据 | Apache-2.0 |
| [SYNDOVELA](syndovela.md) | 保障 | Agent 技能跨运行时组合，缺少供应链保障 | 技能组合治理、签名产物、溯源 | Apache-2.0 |
| [SYMBIVELA](symbivela.md) | 人类 | 人对 Agent 计划与异常失去实质控制 | 目标、审批、干预与证据的协作工作台 | Apache-2.0 |
| [KINETOVELA](kinetovela.md) | 物理 | 机器人集群需要安全、可观测、可恢复的任务执行 | 物理自治控制平面：集群与任务操作 | Apache-2.0 |
| [Enterprise Autonomy](enterprise-autonomy.md) | 项目计划 | 很难看到产品如何端到端组合 | 公开介绍、参考栈、可运行示例 | 见仓库 |
| [PAMP](pamp.md) | 相邻 | 企业架构组合需要实用管理平台 | 企业架构管理平台 | 见仓库 |

## 按问题选择

| 问题 | 起点 |
| --- | --- |
| “我需要一个可嵌入的 Agent 循环。” | PRAXO-CORE |
| “我需要随时间协调多个 Agent。” | Harmovela、COORDIVELA |
| “我需要跨重启与审批的流程。” | RHEOVELA、SYMBIVELA |
| “我需要知道 Agent 被允许做什么。” | AEGIVELA、MODUREGIS |
| “我需要知道 Agent 是谁。” | EIDOVELA、NOMIVELA |
| “我需要可信上下文，而不只是检索。” | GNOSIVELA、ONTOVELA、MNEMOVELA |
| “我需要安全连接外部系统。” | LIMENORA |
| “我需要它仍然有效的证据。” | TEKMOVELA、PEIRAVELA |
| “我需要设计和评审架构。” | TAXOVELA、PAMP |
| “我需要看到它们一起工作。” | Enterprise Autonomy |

## 相邻与相关项目

- **[PAMP](pamp.md)** 是企业架构管理平台。仓库仍保留历史名称 `AXISRobo-PAMP`。
- **[ea-harness](ea-harness.md)** 是早期公开架构技能包仓库。[TAXOVELA](taxovela.md) 是当前
  AI 原生架构项目；两者独立维护。

## 关于“开放接口层”

上表中部分行是产品**开放接口层**，而不是完整运行时。开放接口层通常包含版本化契约、SDK、
示例，有时包含签名二进制。运行时核心或企业版可能单独开发。项目页与仓库 `LICENSE` 是
包含内容的最终依据。
