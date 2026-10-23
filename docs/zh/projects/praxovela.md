# PRAXOVELA

[English](../../projects/praxovela.md) | 中文


**开放接口层：** [axisvela/praxovela-open](https://github.com/axisvela/praxovela-open) ·
**许可证：** Apache-2.0（公开接口） · **语言：** Go、Tauri 桌面 ·
**层次：** 运行时与认知

> 可治理的本地优先桌面 Agent 运行时。默认拒绝、沙箱优先、一切可审计。

## 问题

能读文件、调用工具、运行命令的本地 Agent 很有用，也是安全边界问题。多数 Agent 运行时
授予宽泛权限、记录薄弱，并且崩溃恢复很差。

PRAXOVELA 从相反默认开始：能力使用显式、效果被记录、执行被沙箱约束，失败运行可以恢复，
而不是盲目重来。

## 提供什么

- 默认拒绝的能力门禁。
- 带崩溃恢复的效果账本。
- 持久、可重放的执行追踪。
- 沙箱优先执行。
- 检查点与恢复。
- HTTP API、内嵌 MCP 网关与 Tauri 桌面应用。

## 为什么重要

- **本地控制。** 为本地优先执行设计，而不是由远端服务拥有 Agent。
- **效果证据。** 账本记录 Agent 实际做了什么，而不只是打算做什么。
- **可恢复。** 崩溃不强制完整重放有副作用的操作。

## 如何衔接

PRAXOVELA 是构建在 [PRAXO-CORE](praxo-core.md) 上的产品运行时。它可以为记忆使用
[MNEMOVELA](mnemovela.md)、为模型路由使用 [NOETIVELA](noetivela.md)、为外部工具使用
[LIMENORA](limenora.md)、为授权使用 [AEGIVELA](aegivela.md)。

`-open` 仓库是集成接口。运行时核心与企业版单独开发；当前可用性见仓库。

## 开始

- [PRAXOVELA Open 仓库](https://github.com/axisvela/praxovela-open)
