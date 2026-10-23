# 文档版本说明

[English](../../reference/versioning.md) | 中文

本仓库版本化的是 **AxisVela Open 文档与项目索引**，不是各个产品。每个产品仓库有自己的
发布版本。

## 标签规则

| 标签 | 含义 |
| --- | --- |
| `v0.1.0` | 首个完整公开快照：六个部分、中英文。 |
| `v0.2.0` | 发布与发现能力改进：语言切换、版本说明、变更记录、路线图、引用文件。 |

标签是 annotated 且不可变的。已发布的标签不会被移动。

## 什么会触发版本变化

- **次版本（`0.x`）** — 新部分、新项目条目、实质内容或导航变化、新翻译。
- **补丁（`0.x.y`）** — 修正、坏链、小幅澄清。
- **主版本（`1.0.0`）** — 稳定的文档契约，或 `projects.yaml` schema 的破坏性变更。

1.0 之前，文档明确是快照。产品页可能落后于产品仓库。

## `projects.yaml` schema

机器可读索引有自己的 `schema_version`（当前为 `1`）。字段结构的破坏性变更会提升 schema
版本，与文档标签独立。

## 产品版本是独立的

文档标签不锁定产品版本。如果需要可复现性，请同时记录你使用的产品标签或 commit hash。

## 引用某个版本

使用标签 URL，例如：

```text
AxisVela Open documentation v0.2.0
https://github.com/axisvela/axisvela-open/releases/tag/v0.2.0
```

机器可读引用见
[`CITATION.cff`](https://github.com/axisvela/axisvela-open/blob/main/CITATION.cff)。
