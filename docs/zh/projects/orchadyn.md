# ORCHADYN

[English](../../projects/orchadyn.md) | 中文


**仓库：** [axisvela/orchadyn-open](https://github.com/axisvela/orchadyn-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 工作与能力

> 把目标、状态、能力与约束编译成可验证、可修订计划的规划编译器。

## 问题

模型生成的计划难以检查、比较或修订。它们把“应该发生什么”和“如何发生”混在一起，忽略
能力边界，并丢失让计划成立的原约束。

ORCHADYN 把规划当作编译：输入显式，输出结构化计划，计划可验证、可修订。

## 提供什么

- 运行时中立的规划模型。
- 从目标、状态、能力与约束生成计划。
- 计划验证与解释。
- 假设变化时修订计划。
- HTTP、MCP 与 CLI 接口。
- 用于追溯的计划账本。

## 为什么重要

- **可解释计划。** 计划是可评审的产物，不是聊天里的一段话。
- **可修订。** 世界变化时可以修订，而不必从头开始。
- **受治理。** 计划受将执行它的能力与策略约束。

## 如何衔接

Orchadyn 位于意图与执行之间。它的计划可以由 [MODUREGIS](moduregis.md) 治理、由
[RHEOVELA](rheovela.md) 执行、由 [SYMBIVELA](symbivela.md) 评审、由
[TEKMOVELA](tekmovela.md) 验证。

## 开始

- [Orchadyn Open 仓库](https://github.com/axisvela/orchadyn-open)
