# MODUREGIS

[English](../../projects/moduregis.md) | 中文


**仓库：** [axisvela/moduregis-open](https://github.com/axisvela/moduregis-open) ·
**许可证：** Apache-2.0 · **语言：** TypeScript 与 Go · **层次：** 工作与能力

> 企业能力控制平面：发布、发现、治理、授权、调用并审计 Agent 被允许做的事。

## 问题

能力散落在 API、脚本、工具与 Agent 技能中。通常没有一个地方能回答：存在什么、谁可以用、
成本多少、运行时发生了什么、是否还应可用。

MODUREGIS 把能力变成受治理目录，而不是隐式函数列表。

## 提供什么

- 带发布与发现的能力注册表。
- 治理元数据与生命周期。
- 授权与调用控制。
- 调用审计记录。
- 管理控制台、HTTP API 与 CLI。
- 技能与相关产物导入工具。

## 为什么重要

- **一个目录。** Agent 与人从同一事实源发现能力。
- **调用时策略。** 授权在能力被调用的地方执行，而不只在设计时。
- **可审计。** 每次调用都有记录。

## 如何衔接

MODUREGIS 治理 [ORCHADYN](orchadyn.md) 计划与 [RHEOVELA](rheovela.md) 流程使用的能力层。
它与 [AEGIVELA](aegivela.md)（授权）和 [SYNDOVELA](syndovela.md)（技能供应链）集成。

## 开始

- [Moduregis Open 仓库](https://github.com/axisvela/moduregis-open)
