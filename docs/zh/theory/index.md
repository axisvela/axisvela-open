# Agent 理论

[English](../../theory/index.md) | 中文

这一部分把 Agent 当作**系统**，而不是模型功能。模型回答一个提示；Agent 有目标、
上下文、工具、记忆、权限、生命周期和后果。这些是架构与组织问题，不只是机器学习问题。

本节的理论主线来自 **Huiwen Han** 的研究：Unified Agent Dynamics（UAD）、DIKCA、
Intent-Conditioned Computation（IIC）、Agent-Oriented Programming（AOP）、
Probabilistic Program Execution Semantics（PPES）以及 *Architecture as Law*。
这些页面面向 AxisVela 的读者做综合解释，不替代原始论文；每页都链接到来源。

## 阅读顺序

| 想理解…… | 阅读 |
| --- | --- |
| 全局图景：认知层、计算层、组织层 | [Unified Agent Dynamics](uad.md) |
| 为什么治理是结构性的，不是提示词 | [DIKCA](dikca.md) |
| 为什么意图与架构比代码更重要 | [意图、AOP 与控制](intent-aop.md) |
| 为什么概率系统需要不同的验证方式 | [PPES](ppes.md) |
| 企业 Agent 有哪些类型 | [Agent 分类](agent-taxonomy.md) |
| 多智能体为什么会以不同方式失败 | [多智能体动力学](multi-agent-dynamics.md) |
| 自主性、控制与架构的关系 | [自主性与架构](autonomy-architecture.md) |
| Agent 的经济学如何影响采用 | [Agent 经济学](economics.md) |
| 完整文献与每个思想的使用位置 | [研究地图](research-map.md) |

## 综合，而不是经典

这些页面包含三类陈述：

1. **来自所引论文的论断**：标注来源并链接。
2. **面向本生态的解释**：标注为综合。
3. **实践建议**：属于设计指导，不是定理。

部分工作是预印本。在学术写作中引用前，请查看 DOI 记录的发表状态。
[研究地图](research-map.md)列出了当前链接。

## 最短版本

- Agent 是一个具备目标、上下文和权限的**控制系统**。
- 治理必须由**架构强制执行**，而不是写在提示词里。
- 意图是一等接口，但必须被**明确规格化并检查**。
- 概率执行需要**分布级证据**，而不是一次测试。
- 多智能体系统需要**协调协议**与明确角色。
- 自主性是**架构边界下的元控制**，不是没有控制。
