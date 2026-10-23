# Mnemovela

[English](../../projects/mnemovela.md) | 中文


**仓库：** [axisvela/mnemovela-open](https://github.com/axisvela/mnemovela-open) ·
**许可证：** Apache-2.0 · **语言：** Python 与 Go · **层次：** 运行时与认知

> Agent 记忆的认知运行时：类型化记录、分支语义、混合检索与受治理遗忘。

## 问题

“加一个向量数据库”不是记忆设计。Agent 需要随时间记住事实、决策与上下文；修订或分支
已知内容；有意遗忘；并解释为什么检索到某条记忆。不透明嵌入库做不到这些。

Mnemovela 把记忆当作版本化、可检查的运行时。

## 提供什么

- 类型化认知记忆记录。
- 类 Git 的记忆提交与分支语义。
- 跨结构化与语义信号的混合检索。
- 受治理遗忘与保留策略。
- Python 与 Go 的嵌入式优先运行。
- 语言中立接口：REST、gRPC、JSON-RPC、MCP。
- 可替换存储，企业版支持 PostgreSQL。

## 为什么重要

- **可审计记忆。** 分支与提交让知识变化可追溯。
- **可治理记忆。** 保留与遗忘是一等能力，不是事后补充。
- **可嵌入也可服务化。** 同一运行时可以嵌入 Agent，也可以作为服务运行。

## 如何衔接

Mnemovela 填充 [PRAXO-CORE](praxo-core.md) 的记忆与检索接缝。它为
[PRAXOVELA](praxovela.md) 提供持久上下文，并可被 [GNOSIVELA](gnosivela.md) 的概念与证据
锚定。

## 开始

- [Mnemovela Open 仓库](https://github.com/axisvela/mnemovela-open)
