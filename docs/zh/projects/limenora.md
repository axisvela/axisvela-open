# LIMENORA

[English](../../projects/limenora.md) | 中文


**仓库：** [axisvela/limenora-open](https://github.com/axisvela/limenora-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 边界与保障

> Agent 与外部世界之间受治理的南北向边界。

## 问题

能直接调用任意 API、MCP 服务器、Webhook 或事件总线的 Agent 是不受控出口。凭据扩散到提示
与配置；策略被绕过；也没有可靠记录说明什么跨越了边界。

LIMENORA 把外部访问变成受治理的网关决定。

## 提供什么

- 边缘与企业网关角色。
- HTTP 代理、CONNECT、Webhook 与事件入口。
- 对受治理流量做 TLS 拦截。
- 边界策略执行。
- 不向 Agent 暴露密钥的凭据注入。
- 请求与决定证据。
- MCP 与合作伙伴系统集成模式。

## 为什么重要

- **一个边界。** 外部访问集中且可观测。
- **密钥不进入 Agent。** 凭据在网关注入。
- **策略在流量实际经过的地方执行。**

## 如何衔接

LIMENORA 填充 [PRAXO-CORE](praxo-core.md) 的工具与集成接缝。它连接
[PRAXOVELA](praxovela.md)、[RHEOVELA](rheovela.md) 与其他运行时到 API 与 MCP 服务器，
同时让 [AEGIVELA](aegivela.md) 策略留在决定路径上。

## 开始

- [Limenora Open 仓库](https://github.com/axisvela/limenora-open)
