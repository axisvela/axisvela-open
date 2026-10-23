# PEIRAVELA

[English](../../projects/peiravela.md) | 中文


**仓库：** [axisvela/peiravela-open](https://github.com/axisvela/peiravela-open) ·
**许可证：** Apache-2.0 · **语言：** TypeScript 与 Go · **层次：** 边界与保障

> 可能世界实验控制平面：在生产前于仿真中尝试高风险自治变更。

## 问题

有些变更风险太高，不能直接测试：新策略、不同模型、机器人行为、恢复策略。在生产中运行
它们不是实验，而是等待发生的事故。临时仿真通常产生无法复现或比较的结果。

PEIRAVELA 把仿真当作带溯源的受治理实验。

## 提供什么

- 受治理仿真世界。
- 可复现的 场景 × 扰动 × 控制 × 种子 矩阵。
- 完整溯源的仿真证据。
- 结果独立验证。
- 内嵌 Studio UI 与 HTTP API。
- 控制平面 CLI 与客户端生成。

## 为什么重要

- **安全探索。** 高风险变更可在部署前评估。
- **可比较结果。** 同一矩阵产生可比较运行。
- **证据，不是截图。** 仿真结果主张带溯源。

## 如何衔接

PEIRAVELA 消费 [ONTOVELA](ontovela.md) 的世界模型与 [GNOSIVELA](gnosivela.md) 的知识。
它的证据进入 [TEKMOVELA](tekmovela.md) 发布门禁，并影响
[KINETOVELA](kinetovela.md) 任务设计。

## 开始

- [Peiravela Open 仓库](https://github.com/axisvela/peiravela-open)
