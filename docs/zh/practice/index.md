# Agent 实操

[English](../../practice/index.md) | 中文

这些指南把理论和架构变成可以运行的步骤。它们以 AxisVela 项目作为参考实现，但模式可以
移植到其他系统。

## 选择路径

| 目标 | 指南 | 时间 |
| --- | --- | --- |
| 构建并运行最小可治理 Agent | [构建 Agent](build-an-agent.md) | 30–60 分钟 |
| 加身份、策略、审批与证据 | [治理 Agent](govern-an-agent.md) | 1–2 小时 |
| 加持久记忆与有据可依的上下文 | [记忆与上下文](memory-and-context.md) | 1–2 小时 |
| 运行长期、可恢复流程 | [持久化流程](durable-process.md) | 2–4 小时 |
| 安全连接外部系统 | [连接外部系统](connect-external-systems.md) | 1 小时 |
| 发布前验证与仿真 | [验证与仿真](verify-and-simulate.md) | 2–4 小时 |
| 看整个生态如何协作 | [端到端](end-to-end.md) | 3–6 小时 |
| 决定是否采用、如何采用 | [采用路径](adoption.md) | 1 小时阅读 |

## 前置条件

- PRAXO-CORE 和多数 Go 服务需要 Go 1.25+。
- TAXOVELA 与 Python SDK 需要 Python 3.10+。
- enterprise-autonomy 示例建议使用 Docker。
- 只有 TypeScript SDK 和部分前端需要 Node.js。

## 关于开放接口层的提醒

部分指南把 `*-open` 仓库当作集成接口。它可能包含契约、SDK、示例和二进制，但不包含
完整运行时核心。假定组件生产就绪前，请查看仓库 `LICENSE`、README 和发布说明。

## 实操原则

每一步都应留下证据。如果指南要求你添加能力、权限或流程步骤，也要添加证明发生了什么的
记录。一个能工作但无法解释自己的 Agent 还没有完成。
