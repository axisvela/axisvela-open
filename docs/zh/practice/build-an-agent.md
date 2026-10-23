# 构建 Agent

[English](../../practice/build-an-agent.md) | 中文

本指南用 [PRAXO-CORE](../projects/praxo-core.md) 构建一个最小的可治理 Agent。
目标不是聊天机器人，而是一个有明确模型、工具、策略、事件与证据边界的循环。

## 1. 获取框架

```bash
git clone https://github.com/axisvela/praxo-core
cd praxo-core
go test ./...
```

PRAXO-CORE 需要 Go 1.25+（见 `go.mod`）。快速开始使用 OpenAI 兼容端点。

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

## 2. 循环的形状

核心 API 刻意很小。典型构造如下（以仓库当前签名为准）：

```go
ag, err := agent.New(agent.Options{
    Model:    myModel,
    Tools:    tools,
    Events:   sink,
    Policy:   hook,
    MaxSteps: 8,
})
if err != nil {
    return err
}

result, err := ag.Run(ctx, agent.Session{
    ID:          "session-1",
    TenantID:    "acme",
    WorkspaceID: "default",
}, "Inspect the failing test and propose a fix")
```

重要的不是名字，而是边界：

- **模型** — 提供商中立的接口。
- **工具** — 有校验输入的显式契约。
- **事件** — 发生了什么，用于协调与证据。
- **策略** — 行动前的决定。
- **MaxSteps** — 自主性边界。

## 3. 加一个工具

从只读工具开始。给它：

- 名称与描述；
- 输入 schema；
- 明确的失败模式；
- 可被记录的结果。

不要从 shell 执行或无限制文件写入开始。按爆炸半径逐步增加能力。

## 4. 加策略钩子

策略钩子应回答一个窄问题：*在这个身份、能力与上下文下，该行动是否允许？*

从默认拒绝开始。只允许特定会话的特定工具。记录决定。如果策略无法解释拒绝原因，它还没有
准备好。

## 5. 加事件接收器

至少发出：

- 运行开始/结束；
- 模型调用；
- 工具调用；
- 策略决定；
- 错误与恢复。

这些事件是证据、协调与调试的原料。

## 6. 加记忆（可选）

如果 Agent 需要持久上下文，通过记忆接缝加入
[MNEMOVELA](../projects/mnemovela.md)。会话状态与持久记忆分开。长提示不是记忆架构。

## 7. 让它可治理

在称 Agent “完成”之前检查：

- [ ] 工具集最小且显式。
- [ ] 有步数与预算限制。
- [ ] 副作用前检查策略。
- [ ] 每个重要行动被记录。
- [ ] 失败运行可诊断。
- [ ] 模型可以替换而不重写 Agent。

## 下一步

- [治理 Agent](govern-an-agent.md) — 身份、审批与证据。
- [记忆与上下文](memory-and-context.md) — 持久与有据可依的状态。
- [验证与仿真](verify-and-simulate.md) — 发布前证据。
