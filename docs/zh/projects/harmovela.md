# Harmovela

[English](../../projects/harmovela.md) | 中文


**仓库：** [axisvela/harmovela](https://github.com/axisvela/harmovela) ·
**示例与生态中心：** [harmovela-open](https://github.com/axisvela/harmovela-open) ·
**许可证：** Apache-2.0 · **语言：** 协议，含 TypeScript/Python/Go/Java 实现 ·
**层次：** 基础层

> 面向自治系统的开放协调协议。MCP 调用工具；Harmovela 协调随时间发生的事。

## 问题

MCP 很适合同步能力调用：请求工具，得到结果。它不定义工作跨越数分钟或数天时会发生什么，
多个 Agent 如何共享状态，任务如何委托或恢复，治理如何跨重启存活。

这些是协调问题。没有共享协议，每个系统都会发明互不兼容的版本。

## 提供什么

- 七个协调维度：事件、任务、状态、上下文/记忆、委托、恢复、治理。
- 十三个维度模块与五个基础设施模块（测试装置、运行时、CLI、一致性、MCP 桥）。
- 版本化规范、JSON Schema 与 34 个一致性夹具。
- TypeScript、Python、Go、Java 参考实现。
- 七种传输绑定：stdio、WebSocket、SSE、gRPC、NATS、Kafka、Redis Streams。
- SQLite 与 PostgreSQL 投递存储，支持重试、死信、重放与跨语言一致性。

## 为什么重要

- **厂商中立协调。** 协议不属于单一运行时。
- **一致性可测试。** 多个实现对照同一夹具检查。
- **补足而不是替代 MCP。** MCP 是同步能力层；Harmovela 是异步协调层。

## 如何衔接

Harmovela 是 [PRAXO-CORE](praxo-core.md) 的事件/协调接缝，也是
[COORDIVELA](coordivela.md)（开发协调）与 [RHEOVELA](rheovela.md)（持久流程）的自然伙伴。

[harmovela-open](harmovela-open.md) 是公开示例与生态中心。

## 开始

- [协议仓库](https://github.com/axisvela/harmovela)
- [示例与生态](https://github.com/axisvela/harmovela-open)
- [规范站](https://axisvela.github.io/harmovela/)
