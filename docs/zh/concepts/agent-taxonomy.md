# Agent 分类

[English](../../concepts/agent-taxonomy.md) | 中文

“Agent”是一个过载的词。为了治理和架构，区分五类企业类型有帮助。

| 类型 | 是什么 | 最重要的失败 |
| --- | --- | --- |
| **Application** | 产品内的用户侧 Agent | 错误输出、数据泄露 |
| **Service** | 被其他系统调用的长期服务 | 可用性、成本、出口不受控 |
| **Employee** | 有角色与委托权限的 Agent | 过度委托、责任缺口 |
| **Physical Twin** | 控制或镜像物理资产的 Agent | 安全、不可逆影响 |
| **Human Twin** | 建模个人上下文或权限的 Agent | 误代表、隐私、同意 |

这些类型不是成熟度阶梯。一个系统可以同时包含多种类型，Agent 也可能随权限或具身形态改变
类型。

## 为什么分类

类型决定控制重点：

- **Application：** 沙箱、用户同意、输出证据。
- **Service：** 工作负载身份、速率/成本策略、集成边界。
- **Employee：** 注册、权限绑定、审批、绩效评审。
- **Physical Twin：** 仿真、受限任务、人类接管、恢复。
- **Human Twin：** 同意、范围、撤销、溯源。

把一个拥有委托权限和外部出口的 Agent 当作“普通应用”，是治理错误。

## 生命周期

每个 Agent 都需要生命周期：提议、注册、激活、运行、暂停、撤销、退役。具体名称不重要，
重要的是转换：谁能执行、产生什么证据、Agent 的数据与权限之后如何处理。

## 相关

- [企业 Agent 分类（理论）](../theory/agent-taxonomy.md)
- [Agent 身份](agent-identity.md)
- [可治理自治](governed-autonomy.md)
