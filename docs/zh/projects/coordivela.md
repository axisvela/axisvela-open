# COORDIVELA

[English](../../projects/coordivela.md) | 中文


**仓库：** [axisvela/coordivela-open](https://github.com/axisvela/coordivela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 基础层

> 面向共享开发工作的人与 AI Agent 的协调控制平面。

## 问题

多个 Agent 与人并行工作时，会重复劳动、在同一文件或任务上冲突，并丢失谁在等谁的线索。
聊天频道不是协调系统，没有租约、依赖或冲突处理的任务板也不是。

COORDIVELA 把开发工作当作必须显式协调的状态。

## 提供什么

- 带租约的工作状态与所有权。
- 跨任务的依赖与调度。
- 冲突检测与结构化干预。
- 人与 Agent 共用的控制平面。
- 公开契约、SDK、示例与批准的核心二进制。

## 为什么重要

- **减少重复工作。** 租约与声明让所有权在工作开始前可见。
- **可观测协调。** 依赖与干预是数据，不是走廊对话。
- **Agent 原生。** 同一控制平面服务人类团队与自主工作者。

## 如何衔接

COORDIVELA 协调构建与运营生态本身的工作。它补足 [Harmovela](harmovela.md)（协调运行时
事件与任务）与 [RHEOVELA](rheovela.md)（执行业务流程）。

## 开始

- [COORDIVELA Open 仓库](https://github.com/axisvela/coordivela-open)
