# AEGIVELA

[English](../../projects/aegivela.md) | 中文


**仓库：** [axisvela/aegivela-open](https://github.com/axisvela/aegivela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 信任与知识

> Agent 的授权、委托、审批、撤销与安全证据。

## 问题

“Agent 有令牌”不是授权模型。Agent 代表用户与系统行动，把工作委托给其他 Agent，并对高
风险行动需要审批。权限必须可衰减、可撤销、可举证。

AEGIVELA 是回答这些问题的授权织构。

## 提供什么

- 策略评估与决定契约。
- 委托权限的范围衰减。
- 审批与执行授权流程。
- 撤销。
- 证明策略。
- 策略执行点（PEP）SDK。
- 决定的安全证据。

## 为什么重要

- **委托而不失去控制。** 权限在 Agent 之间移动时可以收窄。
- **撤销是真实的。** 授权可以被收回。
- **每个决定有证据。** 安全结果可检查。

## 如何衔接

AEGIVELA 消费 [EIDOVELA](eidovela.md) 的已验证身份与 [NOMIVELA](nomivela.md) 的注册上下文。
它为 [PRAXO-CORE](praxo-core.md) 提供策略接缝，并在生态中提供执行点。

## 开始

- [Aegivela Open 仓库](https://github.com/axisvela/aegivela-open)
