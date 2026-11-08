# AKROVELA

[English](../../projects/akrovela.md) | 中文

**仓库：** [axisvela/akrovela-open](https://github.com/axisvela/akrovela-open)
**许可证：** 开源部分 Apache-2.0；核心 AGPL-3.0-only；EE 专有。
**语言：** Go · **层次：** 物理 / 站点执行

> 预期定位：受治理的边缘与站点执行，而不是集群规划。

## 状态与现有基线

**未发布的 0.1.0，仅 bootstrap 初始化阶段。** 已实现的接口仅为运行健康、schema
就绪检查与版本 API，以及源码形式的 Go 版本客户端。schema 就绪检查是运维检查，
不是领域执行 API。没有领域执行、数据集、训练能力或机器人集成，也没有二进制发布或
已发布的 SDK。源码客户端不等于 SDK 已发布。

## 问题与预期范围

站点执行需要记录本地实际发生的事实，但不能再造 Mission 控制器或持久工作流引擎。
未来范围是本地操作准入、执行尝试、节点资源限制、持久回执与对账。这些领域能力均未交付。

## 权威边界

- [KINETOVELA](kinetovela.md) 拥有 Mission、分配与效果生命周期。AKROVELA 未来的
  本地尝试与回执不能独立完成、重新分配或补偿 Mission。
- [RHEOVELA](rheovela.md) 拥有跨服务持久 Process；本地日志不是第二个工作流引擎。
- [SYNDOVELA](syndovela.md) 拥有期望的 Bundle 组合、ResolutionLock 与 Runtime Profile。
  未来产物加载不能变成运行时重新解析。
- [MODUREGIS](moduregis.md) 拥有能力契约与不可变引用；[ORCHADYN](orchadyn.md)
  仍是规划器。
- [PRAXO-CORE](praxo-core.md) 仍是 MIT Agent 框架。未来通过适配器承载嵌入式运行时，
  不会重新定义 Agent 行为。
- [DIDACTOVELA](didactovela.md) 是预期的学习数据生命周期所有者，不是已交付的采集目的地。

以上关系均为规划边界，不是已验证的集成。机器人本地安全、联锁与急停必须独立运行。
初始化基线不意味着支持离线执行，也不意味着安全认证。

## 许可证与入口

公开仓库的开源部分采用 Apache-2.0，运行时核心采用 AGPL-3.0-only，EE 扩展为专有。
未来分发的二进制保留自身许可证；放入开放仓库不会改变其许可。
可用性与许可声明以[许可证索引](../reference/licenses.md)和
[公开仓库](https://github.com/axisvela/akrovela-open)为准。
