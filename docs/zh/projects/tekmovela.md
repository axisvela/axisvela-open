# TEKMOVELA

[English](../../projects/tekmovela.md) | 中文


**仓库：** [axisvela/tekmovela-open](https://github.com/axisvela/tekmovela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 边界与保障

> 自治系统的工程保障：验证契约、可复现测试与基于证据的发布门禁。

## 问题

Agent 与自治系统行为难以测试。运行非确定性、失败难以复现、发布决定常基于轶事。
“演示时能跑”不是保障。

TEKMOVELA 把意图与验收标准变成可执行、可诊断、可重跑的验证契约。

## 提供什么

- 从意图与验收标准推导验证契约。
- 受治理测试装置。
- 可复现闭环测试。
- 追踪关联的失败诊断。
- 带证据的发布门禁。
- 由生产行为触发的重新验证。
- SDK 与一致性夹具。

## 为什么重要

- **基于证据的发布。** 门禁决定指向产物，而不是意见。
- **可复现。** 同一契约与种子产生同一运行。
- **持续保障。** 生产信号可以触发重新验证。

## 如何衔接

TEKMOVELA 验证 [PRAXOVELA](praxovela.md) 等 Agent 与运行时、[RHEOVELA](rheovela.md)
中的流程，以及 [KINETOVELA](kinetovela.md) 中的任务。它消费被验证系统的追踪与证据，
并可使用 [PEIRAVELA](peiravela.md) 做安全实验。

## 开始

- [Tekmovela Open 仓库](https://github.com/axisvela/tekmovela-open)
