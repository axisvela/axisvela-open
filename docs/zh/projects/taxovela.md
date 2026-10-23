# TAXOVELA（ArchHarness）

[English](../../projects/taxovela.md) | 中文


**仓库：** [axisvela/TAXOVELA](https://github.com/axisvela/TAXOVELA) ·
**许可证：** MIT · **语言：** Python · **层次：** 设计与标准

> AI 原生架构实践：需求、设计、图、验证与确定性门禁。

## 问题

企业架构工作常是一堆互相矛盾、无法检查的文档与图。AI 助手可以快速生成架构产物，但没有
门禁的速度只会产生自信而不可验证的输出。

TAXOVELA 把架构当作带产物、哈希与门禁的流水线，而不是聊天记录。

## 提供什么

- 面向 Claude Code、OpenCode、Codex、GitHub Copilot、Cursor 的技能：
  需求、设计、图生成、验证、安全评审、优化、报告。
- 真正的 CLI（`python -m archharness`）与多项目工作区。
- 工作流门禁：强制阶段顺序与必需产物。
- 哈希验证产物：图不能在已记录决定下被静默修改。
- 六维图验证与 CI 执行门禁（PASS/WARN/BLOCK）。
- 一个模型生成两种渲染：可编辑 draw.io 与展示用 D2。

## 为什么重要

- **确定性证据。** 门禁可复现，不只是“模型说看起来不错”。
- **适配已有工具。** 同一套架构实践可跨五个 AI 编程助手运行。
- **为评审设计。** 需求、设计、验证、安全与委员会评审是独立、可检查的阶段。

## 如何衔接

TAXOVELA 是设计时治理。它补足运行时与控制平面项目，让它们周围的架构可评审。它与
[PAMP](pamp.md)（组合管理）相邻，并与 [Enterprise Autonomy](enterprise-autonomy.md)
参考架构一起使用。

相关但独立：[`ea-harness`](ea-harness.md) 是早期公开架构技能包；TAXOVELA 是当前 AI 原生项目。

## 开始

- [仓库与安装](https://github.com/axisvela/TAXOVELA)
- [示例库](https://github.com/axisvela/TAXOVELA/tree/main/examples)
- [工作流标准](https://github.com/axisvela/TAXOVELA/blob/main/standards/workflow.yaml)
