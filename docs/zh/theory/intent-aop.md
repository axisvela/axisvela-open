# 意图、AOP 与控制

[English](../../theory/intent-aop.md) | 中文

**来源：** Huiwen Han, *Intent-Conditioned Computation* (2026),
[doi:10.22541/au.177524397.72082163/v1](https://doi.org/10.22541/au.177524397.72082163/v1);
*Agent-Oriented Programming: Foundations of a Semantic Paradigm for the LLM Era*
(2026), [doi:10.2139/ssrn.6563278](https://doi.org/10.2139/ssrn.6563278)。

> 在存储程序计算中，开发者规定控制流；在意向条件计算中，开发者规定意图、约束和反馈，
> 由模型决定执行路径。

## 意向条件计算（IIC）

IIC 是面向基础模型系统的补充抽象。它不替代经典计算，而是指出控制重心的转移：

| 存储程序计算 | 意向条件计算 |
| --- | --- |
| 程序编码显式控制流 | 意图条件化一个学习到的策略 |
| 执行是确定性的 | 执行是概率性、上下文相关的 |
| 正确性由程序定义 | 正确性必须被规格化并评估 |
| 输入是数据 | 上下文、知识、控制都是一等公民 |

IIC 识别五个功能角色：

1. **模型能力** — 学习到的策略引擎。
2. **控制意图** — 目标、约束与反馈。
3. **外置知识** — 检索上下文与知识基底。
4. **确定性代码** — 必须可复现的部分。
5. **数据** — 输入与状态。

核心实践主张是分层：现代系统混合确定性基础设施与意向条件推理。关键是判断哪部分属于
哪种范式。

## Agent-Oriented Programming（AOP）

AOP 把论证推进到编程范式。开发者规定意图、约束和反馈；语义 Agent 决定执行路径。
论文提出 **Semantic Agent Framework（SAF）**，一个七元素模型
`SAF = (G, O, C, A, D, R, F)`，并锚定在统一执行公式：

```text
E(Cap, Intent, Context, Control) → O
```

该框架分离了常被压缩进一个提示词中的关注点，尤其是：

- **G** — 目标规格；
- **D** — 知识基底；
- **R** — 治理约束。

把“提示词”当作一个整体，会混淆这些层。论文称之为 **Prompt Conflation Fallacy**。

## 为什么对架构重要

- **规格是瓶颈。** 当生成变便宜，意图、约束和验收标准的精确性成为稀缺输入。
- **治理不是上下文。** 放在上下文窗口里的规则，不等于被执行的约束。
- **混合才是设计。** 需要可复现的地方保留确定性代码；需要灵活性的地方使用意向条件推理。
- **意图必须可检查。** 如果目标不可检查，系统就无法被验证。

## 与 AxisVela 的映射

- [PRAXO-CORE](../projects/praxo-core.md) 分离循环、模型、工具、策略、沙箱、记忆和事件
  —— 这些接缝让 IIC 可落地。
- [TAXOVELA](../projects/taxovela.md) 是 IIC 论文引用的 ArchHarness 案例：一个混合确定性
  门禁与意向条件设计工作的工作流。
- [ORCHADYN](../projects/orchadyn.md) 把目标与约束变成显式计划；
  [MODUREGIS](../projects/moduregis.md) 分离能力治理；
  [TEKMOVELA](../projects/tekmovela.md) 把验收标准变成验证契约。

## 要点

- 分别规定意图、约束和反馈。
- 不要把治理只放在提示词里。
- 为必须可复现的部分保留确定性主干。
- 让目标可检查，否则无法验证 Agent。
