# AxisVela Open 文档

[English](../index.md) | 中文

这里是 AxisVela 项目家族的公开地图，以及理解 Agent 系统所需的理论、架构、实操与
术语。

## 六个部分

| 部分 | 用途 |
| --- | --- |
| [产品与项目](projects/index.md) | 每个项目是什么、解决什么问题、如何衔接 |
| [Agent 理论](theory/index.md) | 概念主线：UAD、DIKCA、意图、PPES、分类、多智能体动力学 |
| [Agent 架构](architecture/index.md) | 运行时、控制平面、契约、知识、证据、部署、安全 |
| [Agent 实操](practice/index.md) | 以 AxisVela 为参考实现的分步指南 |
| [概念与术语](concepts/index.md) | 核心概念与完整术语表 |
| [参考](reference/index.md) | 关系、许可证、来源、标准、FAQ |

## 选择一条路径

| 路径 | 适合谁 | 入口 |
| --- | --- | --- |
| **构建** | 想嵌入可治理 Agent 循环或 SDK 的开发者 | [构建 Agent](practice/build-an-agent.md) |
| **评估** | 评估生态的架构师与技术负责人 | [从这里开始](start-here.md) |
| **设计** | 设计可治理 Agent 系统的架构师 | [Agent 架构](architecture/index.md) |
| **运维** | 负责运行 Agent、审批与流程的团队 | [从这里开始](start-here.md) |
| **学习** | 想先理解理论与术语的读者 | [Agent 理论](theory/index.md) |

## 两个索引

- **人类索引：** [产品与项目](projects/index.md) — 每个项目的层级、问题、价值与许可证。
- **机器可读索引：**
  [`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml)
  — 供目录工具、文档工具和 AI Agent 使用。

## 关于独立性

[AKROVELA](projects/akrovela.md)（预期站点执行）与
[DIDACTOVELA](projects/didactovela.md)（预期数据与学习生命周期）均为
**未发布的 0.1.0，仅 bootstrap 初始化阶段**。现有基线只有运行健康、schema 就绪检查、
版本 API 与源码形式的 Go 版本客户端。不提供领域执行、数据集、训练、机器人集成、
二进制或已发布的 SDK；新增生态关系均为规划，尚未交付。

各项目独立版本化。本仓库不包含产品源码，也不覆盖产品文档。如果产品页与产品仓库
冲突，以产品仓库为准；如果理论页与所引论文冲突，以论文为准。
