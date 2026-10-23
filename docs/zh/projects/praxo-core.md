# PRAXO-CORE

[English](../../projects/praxo-core.md) | 中文


**仓库：** [axisvela/praxo-core](https://github.com/axisvela/praxo-core) ·
**许可证：** MIT · **语言：** Go · **层次：** 基础层

> 框架层。一个可嵌入、可治理 Agent 的小型基础——不是产品，也不绑定单一运行时。

## 问题

构建 Agent 的团队反复重造同一套基础设施：Agent 循环、提供商抽象、工具契约、记忆与事件
边界、调度、策略钩子、沙箱、检查点与插件管线。治理通常在原型之后才补，而那时接缝已经
很难改。

PRAXO-CORE 从相反方向开始：保持循环小，让边界显式，把产品与提供商决策留给集成方。

## 提供什么

- 可治理 Agent 循环：中间件、预算、上下文压缩、子 Agent。
- 模型、工具、记忆、事件、调度、策略、沙箱、检查点、检索、虚拟文件系统原语。
- 运行时插件平面：进程与 WASM 宿主，以及一致性工具包。
- OpenAI 兼容与 MCP 工具网关适配器。
- OpenTelemetry、基准测试、双语文档与公开 API 冻结清单。

## 为什么重要

- **MIT 边界。** 产品运行时可以嵌入框架而不继承 copyleft 义务。
- **提供商中立。** 同一接口可以由 NOETIVELA、产品路由器或本地模型端点支撑。
- **治理是结构性的。** 策略、沙箱、检查点与事件是框架接缝，不是应用层补丁。

## 如何衔接

PRAXO-CORE 是 [PRAXOVELA](praxovela.md) 的基础，也是外部 Agent 的自然起点。它的接缝连接：

- [NOETIVELA](noetivela.md)：模型与端点路由；
- [MNEMOVELA](mnemovela.md)：持久记忆与检索；
- [HARMOVELA](harmovela.md)：异步协调事件；
- [GNOSIVELA](gnosivela.md)：有据可依的检索；
- [AEGIVELA](aegivela.md)：策略决定；
- [LIMENORA](limenora.md)：受治理工具与外部系统；
- [RHEOVELA](rheovela.md)：图执行与持久流程。

适配器是可选的，且由产品拥有。框架不导入产品代码。

## 开始

- [仓库与快速开始](https://github.com/axisvela/praxo-core)
- [pkg.go.dev](https://pkg.go.dev/github.com/axisvela/praxo-core/v2)
- [文档站](https://axisvela.github.io/praxo-core/)
