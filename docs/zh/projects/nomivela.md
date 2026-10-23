# NOMIVELA

[English](../../projects/nomivela.md) | 中文


**仓库：** [axisvela/NOMIVELA-open](https://github.com/axisvela/NOMIVELA-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 信任与知识

> Agent 注册中心与命名空间权威：Agent、权限绑定、生命周期纪元与发现的记录系统。

## 问题

Agent 身份只有在有可信注册中心时才有用。谁拥有这个 Agent？在哪个命名空间？绑定了什么
权限？当前是哪个生命周期纪元？没有记录系统，答案会散落在表格与部署脚本里。

NOMIVELA 让这些问题可查询、可带证据回答。

## 提供什么

- Agent 身份记录与命名空间。
- 权限绑定。
- Agent 与身份状态的生命周期纪元。
- 发现 API。
- 注册与生命周期变更证据。
- API 契约、schema 与 Go/Python/Java SDK。
- CLI 与一致性夹具。

## 为什么重要

- **一个清单。** Agent、命名空间与绑定有单一事实源。
- **生命周期正确。** 纪元让轮换与重新注册显式。
- **可审计。** 注册与生命周期变更留下证据。

## 如何衔接

EIDOVELA 签发身份；NOMIVELA 记录 Agent 与绑定；AEGIVELA 授权行动。NOMIVELA 是让另外
两个平面在企业中保持一致的中间平面。

## 开始

- [Nomivela Open 仓库](https://github.com/axisvela/NOMIVELA-open)
