# 企业 Agent 分类

[English](../../theory/agent-taxonomy.md) | 中文

**来源：** Huiwen Han, *Unified Agent Dynamics* (2026),
[doi:10.5281/zenodo.19822201](https://doi.org/10.5281/zenodo.19822201)。

> “Agent”不是一个类别。应用 Agent、服务 Agent、员工 Agent、物理孪生、人类孪生，
> 风险不同，治理需求也不同。

UAD 提出企业 Agent 的五类分类。分类有用，因为它迫使我们对身份、权限、证据和失败后果
给出不同答案。

## 五种类型

| 类型 | 是什么 | 主要风险 | 治理重点 |
| --- | --- | --- | --- |
| **Agent as Application** | 嵌入产品/工作流的用户侧 Agent | 错误输出、数据泄露 | 沙箱、用户同意、输出证据 |
| **Agent as Service** | 被其他系统调用的长期服务 | 可用性、成本失控、出口不受控 | 身份、速率/成本策略、集成边界 |
| **Agent as Employee** | 有角色、职责与委托权限的 Agent | 过度委托、责任缺口 | 注册、权限绑定、审批、绩效评审 |
| **Agent as Physical Twin** | 控制或镜像物理资产的软件 Agent | 安全、不可逆影响 | 仿真、受限任务、人类接管、恢复 |
| **Agent as Human Twin** | 建模个人偏好、知识或权限的 Agent | 误代表、隐私、同意 | 同意、范围、撤销、溯源 |

这不是成熟度阶梯。一个系统可以同时包含多种类型，Agent 也可能随权限或具身形态改变类型。

## 分类为什么重要

类型决定控制重点：

- **Application：** 沙箱、用户同意、输出证据。
- **Service：** 工作负载身份、速率/成本策略、集成边界。
- **Employee：** 注册、权限绑定、审批、绩效评审。
- **Physical Twin：** 仿真、受限任务、人类接管、恢复。
- **Human Twin：** 同意、范围、撤销、溯源。

把一个拥有委托权限和外部出口的 Agent 当作“普通应用”，是治理错误。

## 生命周期

每个 Agent 都需要生命周期：提议、注册、激活、运行、暂停、撤销、退役。具体名称不重要，
重要的是状态转换：谁能执行、产生什么证据、Agent 的数据与权限之后如何处理。

## 相关

- [企业 Agent 分类（英文完整版）](../../theory/agent-taxonomy.md)
- [Agent 身份](../concepts/agent-identity.md)
- [可治理自治](../concepts/governed-autonomy.md)
