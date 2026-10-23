# KINETOVELA

[English](../../projects/kinetovela.md) | 中文


**仓库：** [axisvela/kinetovela-open](https://github.com/axisvela/kinetovela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 人类与物理操作

> 面向安全、可观测、可恢复机器人集群任务的物理自治控制平面。

## 问题

软件自治可以靠重启进程停止，物理自治不行。机器人集群需要受限任务、可观测状态、安全恢复
与明确权限模型，才能走出实验室。

KINETOVELA 把生态的治理模型应用到物理执行。

## 提供什么

- 集群与任务操作。
- 公开契约与 SDK。
- 面向机器人与边缘系统的适配器模式。
- 可观测任务状态。
- 受限、可恢复执行。
- 文档与二进制发布。

## 为什么重要

- **物理安全是治理问题。** 权限、状态与恢复必须显式。
- **可观测。** 任务不是黑盒。
- **可恢复。** 失败是状态转换，不是意外。

## 如何衔接

KINETOVELA 消费 [ONTOVELA](ontovela.md) 世界状态、[ORCHADYN](orchadyn.md) 计划与
[TEKMOVELA](tekmovela.md) 验证。任务可以在 [PEIRAVELA](peiravela.md) 中仿真，再通过
[SYMBIVELA](symbivela.md) 审批。

## 开始

- [Kinetovela Open 仓库](https://github.com/axisvela/kinetovela-open)
