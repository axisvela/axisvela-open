# 常见问题

[English](../../reference/faq.md) | 中文

## AxisVela 是一家公司吗？

不是。AxisVela 是由独立维护者维护的项目家族。公开仓库是开放接口层；商业版与企业版
单独开发。

## “开源”和“开放接口层”有什么区别？

开源指实现以开放许可证在仓库中。开放接口层指仓库发布契约、SDK、示例，有时包含二进制，
但运行时核心或企业版可能单独存在。见[开放接口层](../concepts/open-surfaces.md)。

## 我应该从哪里开始？

- 想构建：[PRAXO-CORE](../projects/praxo-core.md)。
- 想评估：[Enterprise Autonomy](../projects/enterprise-autonomy.md) 与
  [生态地图](../ecosystem-map.md)。
- 想学习：[Agent 理论](../theory/index.md)。
- 想实操：[Agent 实操](../practice/index.md)。

## 我需要整套栈吗？

不需要。项目可以独立使用。从你需要的接缝开始：身份、策略、记忆、工作流、集成或验证。
[采用路径](../practice/adoption.md)描述了一个顺序。

## PRAXO-CORE 生产就绪吗？

PRAXO-CORE 是活跃框架，有版本化发布（见
[pkg.go.dev](https://pkg.go.dev/github.com/axisvela/praxo-core/v2)）。生产就绪取决于你的
风险、控制与证据要求。做承诺前先跑
[验证与仿真](../practice/verify-and-simulate.md)。

## 为什么有这么多项目？

因为问题不同：身份不是策略，记忆不是知识锚定，工作流引擎不是消息总线。
[生态地图](../ecosystem-map.md)展示这种分离。

## 什么是可治理自治？

受策略、证据与人类决定路径约束的自主性。见
[可治理自治](../concepts/governed-autonomy.md)。

## 与 MCP 是什么关系？

MCP 很适合同步工具与上下文集成。它不是协调协议、工作流引擎或治理层。见
[协调 vs 编排](../concepts/coordination-vs-orchestration.md)。

## 为什么 `AXISRobo-PAMP` 还用旧名字？

仓库名保留了历史前缀。项目属于相邻的架构组合。见 [PAMP](../projects/pamp.md)。

## 为什么 `ea-harness` 与 TAXOVELA 分开？

它们相关但独立维护。TAXOVELA 是当前 AI 原生架构项目。见
[ea-harness](../projects/ea-harness.md)。

## 如何报告安全问题？

发邮件到 **security@axisvela.com**。不要开公开 issue。见
[安全策略](https://github.com/axisvela/axisvela-open/blob/main/SECURITY.md)。

## 如何在本地运行文档？

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

站点由 MkDocs Material 从 `docs/` 构建。见
[贡献指南](https://github.com/axisvela/axisvela-open/blob/main/CONTRIBUTING.md)。

## 如何引用理论？

引用[研究地图](../theory/research-map.md)中列出的原始论文，而不是本综合文档。引用文档
本身时，引用本仓库。
