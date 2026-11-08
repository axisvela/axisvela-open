# 关系索引

[English](../../reference/relationships.md) | 中文

地图的边，以及每个关系存在的原因。边表示“这个项目产出某种可被另一个项目消费的东西”；
**不**表示这些项目必须一起部署。

| 从 | 关系 | 到 | 为什么重要 |
| --- | --- | --- | --- |
| PRAXO-CORE | 支撑 | PRAXOVELA | PRAXOVELA 是构建在框架上的产品运行时 |
| PRAXO-CORE | 模型接缝 | NOETIVELA | 模型与端点路由可作为适配器提供 |
| PRAXO-CORE | 记忆接缝 | MNEMOVELA | 持久记忆与检索接入循环 |
| PRAXO-CORE | 事件接缝 | HARMOVELA | 协调事件可发布到协议 |
| PRAXO-CORE | 检索接缝 | GNOSIVELA | 有据可依的知识可作为上下文检索 |
| PRAXO-CORE | 策略接缝 | AEGIVELA | 授权决定可门禁工具调用 |
| PRAXO-CORE | 工具接缝 | LIMENORA | 外部工具可通过受治理网关到达 |
| PRAXO-CORE | 执行接缝 | RHEOVELA | 图或流程执行可委托给持久运行时 |
| NOMIVELA | 注册上下文 | EIDOVELA | 身份签发/验证消费注册与权限绑定上下文，不接管注册表写入 |
| EIDOVELA | 已验证身份 | AEGIVELA | 授权消费已验证身份上下文 |
| NOMIVELA | 权限上下文 | AEGIVELA | 绑定与生命周期纪元影响策略决定 |
| GNOSIVELA | 锚定 | ONTOVELA | 概念与证据锚定世界模型 |
| ONTOVELA | 世界状态 | ORCHADYN | 计划基于当前与历史状态生成 |
| ONTOVELA | 世界状态 | PEIRAVELA | 仿真从显式世界模型开始 |
| ORCHADYN | 计划 | MODUREGIS | 计划对照受治理能力检查 |
| MODUREGIS | 受治理能力 | RHEOVELA | 流程步骤在策略与审计下调用能力 |
| RHEOVELA | 审批与异常 | SYMBIVELA | 人评审、批准、干预并接受结果 |
| SYMBIVELA | 决定与证据 | AEGIVELA | 审批与撤销进入授权记录 |
| TEKMOVELA | 验证 | PRAXOVELA、RHEOVELA、KINETOVELA | 验证契约与发布门禁适用于运行时与任务 |
| PEIRAVELA | 仿真证据 | TEKMOVELA | 仿真结果成为发布决定证据 |
| SYNDOVELA | 技能溯源 | MODUREGIS | 组合技能带溯源进入能力目录 |
| LIMENORA | 外部访问 | PRAXOVELA、RHEOVELA | 外部系统通过一个受治理边界到达 |
| TAXOVELA | 架构设计 | Enterprise Autonomy | 参考架构与验证影响示例 |
| PAMP | 组合管理 | Enterprise Autonomy | 架构组合框定项目计划 |
| COORDIVELA | 开发协调 | 生态项目 | 生态自身的工作通过租约与依赖协调 |
| HARMOVELA | 运行时协调 | PRAXO-CORE Agent | Agent 与运行时获得异步协调 |
| Enterprise Autonomy | 组合 | 所有项目 | 端到端示例展示接缝如何被使用 |

## 规划关系：尚未交付

[AKROVELA](../projects/akrovela.md) 与 [DIDACTOVELA](../projects/didactovela.md)
均为**未发布的 0.1.0，仅 bootstrap 初始化阶段**：只有运行健康、schema 就绪检查、版本 API
与源码形式的 Go 版本客户端。没有领域执行、数据集、训练、机器人集成、二进制或已发布的
SDK。下表所有关系均为规划，在[生态地图](../ecosystem-map.md)中使用虚线；不是已验证的
集成，也不是 Enterprise Autonomy 已有示例。

| 从 | 规划关系 | 到 | 权威边界 |
| --- | --- | --- | --- |
| KINETOVELA | 受限操作 | AKROVELA | Mission、分配与效果生命周期仍属 KINETOVELA；本地尝试与回执是 AKROVELA 预期范围。 |
| SYNDOVELA | 期望组合 | AKROVELA | Bundle、ResolutionLock 与期望 Runtime Profile 仍属 SYNDOVELA；不再造解析器。 |
| MODUREGIS | 能力引用 | AKROVELA | 能力契约仍属 MODUREGIS；ORCHADYN 仍是规划器。 |
| RHEOVELA | 工作流委托 | AKROVELA | 跨服务持久 Process 仍属 RHEOVELA；本地日志不是工作流权威。 |
| AKROVELA | 采集引用 | DIDACTOVELA | 预期采集准入与数据集谱系不转移 Mission 权威。 |
| PEIRAVELA | 原始实验证据 | DIDACTOVELA | 原始 SimulationEvidence 仍属 PEIRAVELA；数据集快照与标签是 DIDACTOVELA 预期范围。 |
| DIDACTOVELA | 候选产物 | NOETIVELA | 生产模型与端点激活须显式授权准入；训练不是部署。 |
| DIDACTOVELA | 评估输入 | TEKMOVELA | 生产者指标不能签发独立保障结论。 |

ONTOVELA 保留运营世界真相，不是原始学习 episode。PRAXO-CORE 仍是 MIT 框架，不意味着
新增 Core API 或机器人运行时。机器人本地安全独立于 Mission 与站点执行。

## 如何读这些边

- **接缝是可选的。** PRAXO-CORE 可以在没有 NOETIVELA 或 MNEMOVELA 的情况下运行。
- **边有方向。** 一个项目可以产出另一个项目消费的证据，而不在运行时依赖它。
- **项目计划不是产品。** Enterprise Autonomy 组合产品，不替代产品权威。

## 机器可读

同样的关系在
[`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml) 的
`relates_to` 中表示。两个 bootstrap 条目的 `value` 已明确这些是规划关联，不是已交付依赖。
