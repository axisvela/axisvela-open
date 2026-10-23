# RHEOVELA

[English](../../projects/rheovela.md) | 中文


**仓库：** [axisvela/rheovela-open](https://github.com/axisvela/rheovela-open) ·
**许可证：** Apache-2.0 · **语言：** Go，含多语言 Worker SDK · **层次：** 工作与能力

> 面向必须跨故障、审批与审计存活的长期工作的持久工作流平台。

## 问题

只在一切健康时能工作的工作流只是演示。真实流程持续数小时或数天，跨系统边界，需要人类
审批，并且必须在崩溃后正确恢复而不重复副作用。

RHEOVELA 把流程当作事件溯源、确定性状态机 + 幂等命令，而不是带重试的脚本。

## 提供什么

- 事件溯源流程实例。
- 确定性内核与原子、幂等命令管线。
- 带恢复的持久执行。
- 版本化契约与五语言 Worker SDK。
- HTTP Worker API 与 OpenAPI 规范。
- 把受治理能力计划物化为流程实例的模型。

## 为什么重要

- **可恢复。** 从记录历史恢复，而不是从未知状态。
- **可审计。** 流程历史是事实来源。
- **语言中立 Worker。** 现有服务无需用单一语言重写即可参与。

## 如何衔接

RHEOVELA 执行 [ORCHADYN](orchadyn.md) 产出、受 [MODUREGIS](moduregis.md) 治理的计划。
人类审批与异常可通过 [SYMBIVELA](symbivela.md) 路由，结果可由
[TEKMOVELA](tekmovela.md) 验证。

## 开始

- [Rheovela Open 仓库](https://github.com/axisvela/rheovela-open)
