# SYNDOVELA

[English](../../projects/syndovela.md) | 中文


**仓库：** [axisvela/SYNDOVELA-open](https://github.com/axisvela/SYNDOVELA-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 边界与保障

> 治理 Agent 技能如何跨运行时组合、签名与消费。

## 问题

Agent 技能越来越多地由多个来源组装，并在不同运行时执行。组合很方便，却产生供应链问题：
这个技能包里到底有什么、谁签名、依赖什么、哪个运行时可以执行？

SYNDOVELA 把技能组合当作受治理供应链。

## 提供什么

- 跨运行时的 Agent 技能组合模型。
- 面向生产者与消费者的 SDK 与契约。
- 签名发布二进制。
- 示例与集成指南。
- 组合技能的供应链元数据。

## 为什么重要

- **技能溯源。** 消费者能看到技能包包含什么。
- **签名与验证。** 使用前可以检查产物。
- **跨运行时治理。** 组合规则不绑定单一运行时。

## 如何衔接

SYNDOVELA 是 [MODUREGIS](moduregis.md) 治理、[PRAXOVELA](praxovela.md) 等运行时执行的
技能的供应链层。它通过覆盖被测产物的来源，补足 [TEKMOVELA](tekmovela.md) 保障。

## 开始

- [Syndovela Open 仓库](https://github.com/axisvela/SYNDOVELA-open)
