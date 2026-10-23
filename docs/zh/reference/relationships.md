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
| EIDOVELA | 签发身份 | NOMIVELA | 签发的身份记录在注册中心 |
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

## 如何读这些边

- **接缝是可选的。** PRAXO-CORE 可以在没有 NOETIVELA 或 MNEMOVELA 的情况下运行。
- **边有方向。** 一个项目可以产出另一个项目消费的证据，而不在运行时依赖它。
- **项目计划不是产品。** Enterprise Autonomy 组合产品，不替代产品权威。

## 机器可读

同样的关系在
[`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml) 的
`relates_to` 中表示。
