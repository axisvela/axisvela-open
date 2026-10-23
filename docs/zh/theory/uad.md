# Unified Agent Dynamics（UAD）

[English](../../theory/uad.md) | 中文

**来源：** Huiwen Han, *Unified Agent Dynamics: A Multi-Layer Socio-Technical
Framework for Enterprise AI Agents* (2026),
[doi:10.5281/zenodo.19822201](https://doi.org/10.5281/zenodo.19822201)。

> 企业 Agent 不是孤立工具，而是认知、计算与组织动力学相互作用的社技术行动者。

## 三个层次

UAD 把企业 Agent 建模为三个层次：

| 层次 | 覆盖内容 | 回答的问题 |
| --- | --- | --- |
| **认知层（LC）** | 目标、知识、推理、记忆、上下文 | Agent 知道什么、意图是什么？ |
| **计算层（LP）** | 模型、工具、运行时、控制、执行 | Agent 如何行动？ |
| **组织层（LO）** | 角色、权限、激励、治理、生命周期 | 谁拥有它，受什么规则约束？ |

多数 Agent 工程只关注 LC 与 LP。UAD 的核心主张是：组织层不是外包装，它参与 Agent 的
动态。

## 动力学方程

UAD 提出一个规范形式：

```text
dF/dt = G_int(F) + G_env(F, E) + G_ctrl(F, C)
```

- `F` 是 Agent 状态；
- `G_int` 是内部动力学（推理、记忆、规划）；
- `G_env` 是与环境 `E` 的交互；
- `G_ctrl` 是治理/控制项 `C`。

关键变化是：治理是动力学中的**一项**，不是 Agent 行动之后才补上的东西。

## 三个推论

论文推导出三个与治理相关的性质：

1. **治理临界阈值。** 超过某个执行强度 `μc`，更强的控制可能通过 Hopf 分岔使行为
   不稳定。更多控制不一定更稳定，控制设计本身很重要。
2. **分层。** 异构企业多智能体系统倾向于自组织成层级结构，并可从交互结构预测。
3. **复杂度上限。** 受治理的最优控制存在容量上限；超过它与治理失败相关。

这些是仿真研究中的理论结果，不是普遍常数。它们的实践价值是方向性的：治理有动力学，
复杂度有极限。

## 五类企业 Agent

UAD 区分五类：**Application、Service、Employee、Physical Twin、Human Twin**。
它们在自主性、身份、责任和失败后果上不同。实践版本见
[Agent 分类](agent-taxonomy.md)。

## 与 AxisVela 的映射

| UAD 层次 | AxisVela 示例 |
| --- | --- |
| 认知 | Mnemovela（记忆）、Gnosivela（知识锚定）、Ontovela（世界模型）、Orchadyn（规划） |
| 计算 | PRAXO-CORE（循环与原语）、PRAXOVELA（运行时）、Noetivela（推理）、Limenora（工具） |
| 组织 | Enterprise Autonomy（组合）、Symbivela（人类控制）、Aegivela/NOMIVELA/EIDOVELA（权限）、COORDIVELA（工作协调） |

映射是示意性的。一个产品可以同时属于多个层次。

## 要点

- 不要把治理设计成后处理步骤。
- 显式建模组织层：角色、权限、生命周期与责任。
- 预期非线性：控制太少不安全，设计糟糕的控制也会破坏稳定。
- 控制制度要与 Agent 类型匹配。
