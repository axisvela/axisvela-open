# Noetivela

[English](../../projects/noetivela.md) | 中文


**仓库：** [axisvela/noetivela-open](https://github.com/axisvela/noetivela-open) ·
**许可证：** Apache-2.0 · **语言：** Go · **层次：** 运行时与认知

> 企业推理织构：编目模型与端点，把需求变成推理契约，并按证据路由请求。

## 问题

企业很少只有一个模型端点。它有云 API、私有模型、边缘推理、区域限制、成本目标、延迟目标
与质量差异。把提供商硬编码进 Agent 会让这些变得僵化且不可见。

Noetivela 把推理变成受治理的路由决定。

## 提供什么

- 模型与端点目录。
- 从任务需求推导的推理契约。
- 跨云、私有与边缘智能的路由。
- 决策中的策略、质量、延迟与成本考虑。
- OpenAI 兼容 HTTP 接口与受治理端点。
- CLI 与 Go、Python、TypeScript SDK。

## 为什么重要

- **避免提供商锁定。** Agent 调用契约，而不是厂商 SDK。
- **让权衡显式。** 成本、延迟、质量与主权成为路由输入。
- **保留证据轨迹。** 路由决定可检查，而不是猜测。

## 如何衔接

Noetivela 填充 [PRAXO-CORE](praxo-core.md) 的模型接缝，为
[PRAXOVELA](praxovela.md) 与其他 Agent 提供推理。它与
[GNOSIVELA](gnosivela.md)（有据可依的上下文）和 [TEKMOVELA](tekmovela.md)
（评估模型相关行为）自然搭配。

## 候选产物边界

Noetivela 保留生产模型与推理端点权威。[DIDACTOVELA](didactovela.md) 预期产出候选
学习策略产物，不激活端点，也不授予执行权限。DIDACTOVELA 为未发布的 0.1.0，仅 bootstrap
初始化阶段；候选产物交接为规划，尚未交付，未来仍须显式授权部署准入。

## 开始

- [Noetivela Open 仓库](https://github.com/axisvela/noetivela-open)
