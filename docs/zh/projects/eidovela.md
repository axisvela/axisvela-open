# EIDOVELA

[English](../../projects/eidovela.md) | 中文


**仓库：** [axisvela/eidovela-open](https://github.com/axisvela/eidovela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 信任与知识

> Agent 原生身份提供者：生命周期、信任域与工作负载证明。

## 问题

Agent 常用工作负载间共享的长期 API key 认证。这让身份粗放、撤销缓慢、溯源薄弱。Agent
应能证明*哪个工作负载*、*哪个租户*、*凭据有效多久*。

EIDOVELA 把身份提供者的纪律应用到 Agent。

## 提供什么

- Agent 生命周期与身份签发。
- 租户信任域。
- 使用 Kubernetes、SPIFFE 或 mTLS 的工作负载证明。
- `private_key_jwt` 注册。
- 持有证明绑定令牌。
- OIDC 接口与 SDK。
- 一致性夹具与示例。

## 为什么重要

- **短期、绑定凭据。** 令牌绑定工作负载与持有证明，而不只是字符串。
- **信任域。** 多租户系统可以分离身份根。
- **生命周期感知。** 身份随 Agent 生命周期签发、轮换与撤销。

## 如何衔接

EIDOVELA 回答“这个 Agent 是谁”。[NOMIVELA](nomivela.md) 记录 Agent 与权限绑定；
[AEGIVELA](aegivela.md) 决定身份可以做什么。三者共同构成身份、注册与授权平面。

## 开始

- [Eidovela Open 仓库](https://github.com/axisvela/eidovela-open)
