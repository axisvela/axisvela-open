# 运行持久化流程

[English](../../practice/durable-process.md) | 中文

长期工作不只需要循环。它需要计划、受治理能力、持久执行、人类决定与证据。本指南展示
AxisVela 示例使用的模式。

## 链路

```text
目标 → ORCHADYN 计划 → MODUREGIS 能力
     → RHEOVELA 流程 → SYMBIVELA 审批 → TEKMOVELA 验证
```

每一步都是可选的，但边界很重要。

## 1. 定义目标与验收标准

陈述结果、约束以及什么算成功。不要从工作流图开始，从决策与证据开始。

## 2. 编译计划

用 [ORCHADYN](../projects/orchadyn.md) 把目标、状态、能力与约束变成结构化、可修订计划。

有用的计划：

- 明确步骤与依赖；
- 受可用能力约束；
- 可验证；
- 假设变化时可修订。

## 3. 治理能力

用 [MODUREGIS](../projects/moduregis.md) 检查计划：

- 每个能力是否存在？
- 谁可以调用？
- 在什么策略下？
- 调用会产生什么证据？

不要让计划发明目录中不存在的能力。

## 4. 持久执行

用 [RHEOVELA](../projects/rheovela.md) 处理长期或易失败的工作。它提供：

- 事件溯源流程实例；
- 确定性、幂等命令；
- 恢复；
- 记录历史。

流程应跨崩溃存活，而不重复副作用。

## 5. 插入人类决定

把审批、异常与干预路由到 [SYMBIVELA](../projects/symbivela.md) 或等价控制。

好的审批展示：

- 步骤与风险；
- 计划上下文；
- 当前证据；
- 批准与拒绝的后果；
- 责任人。

## 6. 验证结果

用 [TEKMOVELA](../projects/tekmovela.md) 对照验收标准检查结果。验证应基于证据，而不是
流程的自我报告。

## 示例：订单异常

典型订单履约异常：

1. 订单无法按计划履约。
2. ORCHADYN 产生修订计划（替代、拆单、退款）。
3. MODUREGIS 检查允许的能力与策略。
4. RHEOVELA 启动流程实例并记录异常。
5. SYMBIVELA 请人批准退款或替代。
6. LIMENORA 通过受治理网关调用外部履约系统。
7. TEKMOVELA 验证结果并用证据闭环。

可运行示例见
[Enterprise Autonomy](https://github.com/axisvela/enterprise-autonomy/tree/main/examples)。

## 恢复清单

- [ ] 流程崩溃后可恢复。
- [ ] 命令幂等。
- [ ] 外部效果被记录。
- [ ] 失败步骤有补偿或升级路径。
- [ ] 人类审批跨重启存活。
- [ ] 最终结果被验证。

## 反模式

- 把工作流引擎当消息总线。
- 忽略能力边界的计划。
- 未连接到执行路径的审批。
- 没有幂等键就重试副作用。
- 把流程历史当作可选。

## 下一步

- [连接外部系统](connect-external-systems.md) — 边界。
- [验证与仿真](verify-and-simulate.md) — 发布前证据。
