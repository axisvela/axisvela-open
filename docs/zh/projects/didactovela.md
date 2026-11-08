# DIDACTOVELA

[English](../../projects/didactovela.md) | 中文

**仓库：** [axisvela/didactovela-open](https://github.com/axisvela/didactovela-open)
**许可证：** 开源部分 Apache-2.0；核心 AGPL-3.0-only；EE 专有。
**语言：** Go · **层次：** 学习

> 预期定位：数据与学习策略生命周期，而不是运行时授权。

## 状态与现有基线

**未发布的 0.1.0，仅 bootstrap 初始化阶段。** 已实现的接口仅为运行健康、schema
就绪检查与版本 API，以及源码形式的 Go 版本客户端。schema 就绪检查是运维检查，
不是数据集或训练 API。没有领域执行、数据集、训练能力或机器人集成，也没有二进制发布或
已发布的 SDK。源码客户端不等于 SDK 已发布。

## 问题与预期范围

学习输入与候选产物需要可追溯的归属，但训练不能变成部署权威。未来范围是采集准入、
不可变来源清单、episode、数据集快照、标签、可复现训练配方与结果，以及候选学习策略产物。
这些领域能力均未交付。

## 权威边界

- [AKROVELA](akrovela.md) 的本地采集和 [KINETOVELA](kinetovela.md) 的效果引用是
  潜在输入，不是已实现的摄取路径。
- [PEIRAVELA](peiravela.md) 拥有实验世界、扰动与原始 SimulationEvidence。
  DIDACTOVELA 预期的数据集不替代该权威。
- [Noetivela](noetivela.md) 拥有生产模型与推理端点。候选检查点在显式准入并授权部署前
  保持惰性；训练不得激活端点或向执行器发送命令。
- [TEKMOVELA](tekmovela.md) 拥有独立保障结论；训练指标与执行成功不能自行签发保障通过。
- [ONTOVELA](ontovela.md) 拥有运营世界真相，不是原始学习 episode。
  仿真或记录的学习状态不能覆盖运营现实。
- 学习策略是模型，不是 [AEGIVELA](aegivela.md) 授权策略；它不授予执行权限或扩大能力范围。

以上关系均为规划边界，不是已验证的集成。来源权利、溯源、标签准入与训练/评估隔离是
未来学习工作的要求，不是此初始化基线的能力。

## 许可证与入口

公开仓库的开源部分采用 Apache-2.0，运行时核心采用 AGPL-3.0-only，EE 扩展为专有。
未来分发的二进制保留自身许可证；放入开放仓库不会改变其许可。
可用性与许可声明以[许可证索引](../reference/licenses.md)和
[公开仓库](https://github.com/axisvela/didactovela-open)为准。
