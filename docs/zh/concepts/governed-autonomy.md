# 可治理自治

[English](../../concepts/governed-autonomy.md) | 中文

自主性不是二元的。系统可以在*决定什么*上自主，同时在*允许做什么*、*必须记录什么*以及
*何时必须由人决定*上保持受限。

可治理自治就是把那些边界显式化的纪律。

## 三个问题

每个自主行动都应能回答三个问题。

### 1. 允许什么？

执行前，系统需要对能力、数据和副作用给出显式答案。答案可以来自能力目录、策略决定、
沙箱、租约或组合。关键属性是答案存在于行动*之前*，而不是之后。

相关：[MODUREGIS](../projects/moduregis.md)、[AEGIVELA](../projects/aegivela.md)、
[PRAXOVELA](../projects/praxovela.md)。

### 2. 实际发生了什么？

意图与效果不同。可治理系统记录效果：调用了什么、输入是什么、在哪个策略下、结果是什么、
如何恢复。没有这些，调试与审计会变成考古。

相关：[PRAXOVELA](../projects/praxovela.md)、[RHEOVELA](../projects/rheovela.md)、
[TEKMOVELA](../projects/tekmovela.md)。

### 3. 谁做的决定？

高风险行动需要明确的决定路径：所有者、审批、撤销路径与干预方式。“Agent 决定的”不是
问责模型。

相关：[SYMBIVELA](../projects/symbivela.md)、[AEGIVELA](../projects/aegivela.md)、
[EIDOVELA](../projects/eidovela.md)。

## 为什么重要

多数 Agent 失败不是模型失败，而是边界失败：

- 不该可用的工具可用；
- 行动没有记录；
- 人无法知道 Agent 即将做什么；
- 流程无法在不重复效果的情况下恢复。

可治理自治在接缝处结构化地解决这些问题。

## 一个实用测试

对任何自主工作流，问：

1. 我能说出授权每一步的策略或能力吗？
2. 我能从产物重建效果历史吗？
3. 我能指出批准高风险步骤的人或系统吗？
4. 我能在不即兴发挥的情况下停止、撤销或恢复吗？

如果任何答案是“得查日志”，工作流还没有被治理，只是被自动化了。
