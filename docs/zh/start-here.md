# 从这里开始

[English](../start-here.md) | 中文

进入 AxisVela 有五条常用路径。选择与你工作最接近的一条即可，不需要先读完整张地图。

## 构建

**你想把可治理的 Agent 循环或 SDK 嵌入自己的系统。**

从 [PRAXO-CORE](projects/praxo-core.md) 开始。它是 MIT 许可的 Go 框架，也是生态中
最小、可以独立运行的部分。

```bash
git clone https://github.com/axisvela/praxo-core
cd praxo-core
go test ./...
```

连接本地 OpenAI 兼容端点的最小运行：

```bash
export PRAXO_BASE_URL=http://localhost:11434/v1
export PRAXO_MODEL=llama3.2
GOWORK=off go run ./examples/quickstart
```

PowerShell：

```powershell
$env:PRAXO_BASE_URL = "http://localhost:11434/v1"
$env:PRAXO_MODEL = "llama3.2"
$env:GOWORK = "off"
go run ./examples/quickstart
```

当循环不够用时，一次只加一个接缝：

| 需要 | 项目 | 提供什么 |
| --- | --- | --- |
| 跨提供商/端点的模型路由 | [NOETIVELA](projects/noetivela.md) | 推理契约与受治理路由 |
| 持久记忆与检索 | [MNEMOVELA](projects/mnemovela.md) | 类型化记忆、分支、混合检索 |
| 异步任务/状态协调 | [HARMOVELA](projects/harmovela.md) | 开放协调协议 |
| 受治理的外部系统访问 | [LIMENORA](projects/limenora.md) | 策略执行的集成网关 |
| 授权与审批 | [AEGIVELA](projects/aegivela.md) | 委托权限与策略执行 |
| 持久、可恢复的流程 | [RHEOVELA](projects/rheovela.md) | 事件溯源工作流运行时 |

完整步骤见[构建 Agent](practice/build-an-agent.md)。

## 评估

**你想判断这个生态是否能解决组织的真实问题。**

建议按以下顺序阅读：

1. [生态地图](ecosystem-map.md) — 层次与接缝。
2. [Enterprise Autonomy](projects/enterprise-autonomy.md) — 公开介绍与端到端示例。
   其中的[产品概览](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/products.md)
   和[技术目录](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/technical-catalog.md)
   是了解当前可运行内容的最快方式。
3. [产品与项目索引](projects/index.md) — 并排比较问题、价值与许可证。
4. 从
   [`enterprise-autonomy/examples/`](https://github.com/axisvela/enterprise-autonomy/tree/main/examples)
   选一个可运行示例。

要持续问的问题不是“哪个产品最好”，而是“我需要哪个接缝，它会留下什么证据”。架构视角
见 [Agent 架构](architecture/index.md)。

## 设计

**你在设计一个可治理的 Agent 系统。**

建议按以下顺序阅读架构部分：

1. [参考架构](architecture/reference-architecture.md) — 层次与端到端请求路径。
2. [控制平面](architecture/control-planes.md) — 身份、策略、能力、协调与保障。
3. [契约与接口](architecture/contracts.md) — 独立产品如何组合。
4. [证据架构](architecture/evidence.md) — 如何让设计可证明。
5. [安全模型](architecture/security.md) — 威胁模型。

如果需要先补概念基础，读 [Agent 理论](theory/index.md)。

## 运维

**你负责运行 Agent、审批和流程。**

运维栈通常是以下组合：

- [RHEOVELA](projects/rheovela.md)：持久化流程实例与恢复；
- [SYMBIVELA](projects/symbivela.md)：计划评审、审批、异常与干预；
- [MODUREGIS](projects/moduregis.md)：受治理的能力目录；
- [AEGIVELA](projects/aegivela.md)：授权、委托与撤销；
- [TEKMOVELA](projects/tekmovela.md) 与 [PEIRAVELA](projects/peiravela.md)：
  发布前验证与安全实验。

可以从 Enterprise Autonomy 的
[治理模式](https://github.com/axisvela/enterprise-autonomy/blob/main/docs/governance-patterns.md)
和[参考栈](https://github.com/axisvela/enterprise-autonomy/tree/main/reference-stacks)
开始。可运行版本见[持久化流程](practice/durable-process.md)和[端到端](practice/end-to-end.md)。

## 学习

**你想先理解思想，而不是产品细节。**

先读 [Agent 理论](theory/index.md)，尤其是：

- [Unified Agent Dynamics](theory/uad.md)
- [DIKCA](theory/dikca.md)
- [意图、AOP 与控制](theory/intent-aop.md)
- [PPES](theory/ppes.md)

然后用[概念与术语](concepts/index.md)建立词汇：

- [可治理自治](concepts/governed-autonomy.md)
- [能动性与控制](concepts/agency-and-control.md)
- [契约，而不是内核](concepts/contracts-not-kernel.md)
- [证据与可审计性](concepts/evidence-and-audit.md)
- [Agent 身份的三个平面](concepts/agent-identity.md)
- [协调 vs 编排](concepts/coordination-vs-orchestration.md)

完整词汇见[术语表](concepts/glossary.md)。

## 关于“开放”的提醒

`*-open` 仓库通常是**开放接口层**：契约、SDK、示例，有时包含二进制。它让你可以评估
和集成，但不一定意味着整个运行时都开源。做承诺前先看仓库 `LICENSE` 和
[许可证页](reference/licenses.md)。
