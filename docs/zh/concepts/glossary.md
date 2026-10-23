# 术语与词汇表

[English](../../concepts/glossary.md) | 中文

Agent 系统的工作词汇。定义刻意简短；链接指向更完整的说明。

## Agent 与自主性

**Agent（智能体）** — 追求目标、使用能力并产生效果的软件行动者。可以是长期的、被委托的、
受治理的。见 [Agent 分类](agent-taxonomy.md)。

**Agency（能动性）** — 朝目标行动的能力。区别于自主性（Agent 自主选择的程度）与控制
（什么约束它）。见 [能动性与控制](agency-and-control.md)。

**Autonomy（自主性）** — Agent 在没有外部干预时选择与修改行动的程度，受架构与控制约束。

**Autonomy level（自主性级别）** — 对 Agent 可无审批做多少事的实用标签：辅助、监督、委托、
有界自治、元控制。见 [自主性与架构](../theory/autonomy-architecture.md)。

**Bounded autonomy（有界自治）** — 在强制包络内的自主性：能力、预算、步数、时间与恢复规则。

**Meta-control（元控制）** — 系统在架构授权下修改自身控制结构的能力。高级自主性属性，
不是默认配置。见 [DIKCA](../theory/dikca.md)。

**Agent lifecycle（Agent 生命周期）** — 提议、注册、激活、运行、暂停、撤销、退役。
状态转换应有所有者与证据。

**Agent registry（Agent 注册中心）** — Agent、命名空间、权限绑定与生命周期纪元的记录系统。
见 [NOMIVELA](../projects/nomivela.md)。

**Agent identity（Agent 身份）** — Agent 工作负载、租户与权限上下文的可验证表示。见
[Agent 身份](agent-identity.md)。

**Agent type（Agent 类型）** — 五类企业类别：Application、Service、Employee、Physical
Twin、Human Twin。见 [企业 Agent 分类](../theory/agent-taxonomy.md)。

**Multi-agent system（多智能体系统，MAS）** — 多个 Agent 协调、委托并共享状态的系统。见
[多智能体动力学](../theory/multi-agent-dynamics.md)。

**Delegation（委托）** — 把权限或工作转交给另一个 Agent 或人。委托应衰减权限，而不是放大。

**Handoff（交接）** — Agent 或人之间有结构的工作与上下文转移，带所有者与证据。

**Role（角色）** — 系统或组织中命名的职责与权限集合。

**Supervision（监督）** — 人或自动系统对 Agent 计划与行动的监督。

**HITL（Human-in-the-loop，人类在环）** — 设计好的人类决策点：评审、批准、干预或接受结果。
见 [SYMBIVELA](../projects/symbivela.md)。

**Human-on-the-loop（人类在环上）** — 人监控并可干预，但不审批每一步。

**Human sovereignty（人类主权）** — 人知道、批准、干预、撤销与检查的权利与能力。见
[自主性与架构](../theory/autonomy-architecture.md)。

**Kill switch（急停开关）** — 快速停止 Agent 或流程的机制，最好不停止整个系统。

**Escalation（升级）** — 当前路径无法解决时，把决定或异常交给更高权限。

## 架构与控制

**Architecture（架构）** — 决定哪些配置可能、哪些控制可执行、哪些证据可产生的构成性结构。
见 [DIKCA](../theory/dikca.md)。

**Architectonic constraint（架构性约束）** — 定义系统可以成为什么，而不只是当前做什么的约束。

**Control（控制）** — 对允许行为的约束，以及执行这些约束的机制。控制不等于知识或描述。

**Control plane（控制平面）** — 决定身份、策略、能力、协调与保障的部分。见
[控制平面](../architecture/control-planes.md)。

**Data plane（数据平面）** — 执行工作与移动载荷的部分。

**Policy（策略）** — 关于什么允许、在什么条件下、带什么证据的规则。

**PDP（策略决定点）** — 评估策略并返回决定的组件。见 [AEGIVELA](../projects/aegivela.md)。

**PEP（策略执行点）** — 在边界执行策略决定的组件。

**Guardrail（护栏）** — 约束行为的控制，最好在架构边界。提示词里的护栏是建议；PEP 里的
护栏是控制。

**Sandbox（沙箱）** — 限制 Agent 可访问或可执行内容的执行环境。见
[PRAXOVELA](../projects/praxovela.md)。

**Capability gate（能力门禁）** — 调用前允许或拒绝能力的控制。

**Least privilege（最小权限）** — 只授予任务所需的最小权限，时间尽可能短。

**Defense in depth（纵深防御）** — 叠加独立控制，使单点失败不移除保护。

**Trust boundary（信任边界）** — 数据、身份或权限改变信任级别的边界。控制应位于信任边界。

**Contract（契约）** — 独立组件之间的版本化接口：API、schema、协议、SDK 或一致性夹具。见
[契约与接口](../architecture/contracts.md)。

**Open surface（开放接口层）** — 发布契约、SDK、示例，有时包含二进制的公开仓库，但不一定
包含完整运行时。见 [开放接口层](open-surfaces.md)。

**Conformance（一致性/符合性）** — 通过夹具与测试证明与契约兼容。

**Versioning（版本化）** — 给契约或产品修订分配标识，便于消费者管理兼容性。

**Deprecation（弃用）** — 有计划地淘汰契约或功能，带日期与迁移路径。

**Reference architecture（参考架构）** — 用于指导实现的可复用架构模式。见
[参考架构](../architecture/reference-architecture.md)。

**Deployment shape（部署形态）** — 部署的信任拓扑：本地优先、单租户服务、企业混合、边缘/
物理。见 [部署形态](../architecture/deployment.md)。

**Local-first（本地优先）** — 数据与执行主要在用户设备上的设计。

**Hybrid deployment（混合部署）** — 跨本地、云与边缘，带显式联邦的部署。

**Edge（边缘）** — 靠近物理系统或数据源的计算，通常连接受限、安全约束更高。

## 意图、规划与工作

**Intent（意图）** — 人或系统想要的结果，包括约束与成功标准。见
[意图与规格](intent-and-specification.md)。

**Specification（规格）** — 对目标、上下文、约束与验收标准的显式陈述。

**Acceptance criterion（验收标准）** — 判断结果是否可接受的可观测条件，应可测试。

**Constraint（约束）** — 对可以做什么或如何做的限制。

**Goal（目标）** — 期望结果，与实现它的计划分开。

**Plan（计划）** — 在约束下达成目标的结构化、可修订产物。见
[ORCHADYN](../projects/orchadyn.md)。

**Planning（规划）** — 产生或修订计划的活动。

**Replanning（重规划）** — 当假设、状态或约束变化时修订计划。

**Verification contract（验证契约）** — 系统被接受前必须成立的可测试陈述。见
[TEKMOVELA](../projects/tekmovela.md)。

**Workflow（工作流）** — 流程的步骤序列。工作流引擎增加持久性、状态与恢复。

**Process instance（流程实例）** — 带记录历史的持久工作流执行。见
[RHEOVELA](../projects/rheovela.md)。

**Durable execution（持久执行）** — 跨进程或设备故障存活，并从记录状态恢复的执行。

**Idempotency（幂等）** — 重复操作不会重复效果的性质。

**Compensation（补偿）** — 抵消或反转已完成步骤的行动。

**Checkpoint（检查点）** — 可从中恢复执行的保存状态。

**Recovery（恢复）** — 失败后把系统或流程恢复到有效状态。

**Retry（重试）** — 失败后重新尝试。只有在幂等或补偿存在时才安全。

**Timeout（超时）** — 对操作时长的限制。

**Circuit breaker（熔断）** — 停止调用失败依赖以防止级联故障的机制。

**Approval（审批）** — 人允许高风险行动的决定。应引用计划、证据与责任人。

**Exception（异常）** — 不按预期路径发展、需要决定的案例。

**Intervention（干预）** — 人改变或停止执行中流程的行动。

## 能力、技能与工具

**Tool（工具）** — 暴露给模型的可调用函数或 API。工具需要输入校验、沙箱与限制。

**Capability（能力）** — 带身份、策略与审计的受治理行动单元。见
[能力、技能与工具](capability-skill-tool.md)。

**Capability catalog（能力目录）** — 受治理的能力注册表。见
[MODUREGIS](../projects/moduregis.md)。

**Skill（技能）** — Agent 可使用的打包流程或知识产物。技能需要溯源与版本化。

**Skill bundle（技能包）** — 作为产物分发的一组技能。见
[SYNDOVELA](../projects/syndovela.md)。

**Plugin（插件）** — 在受控边界加载到运行时的扩展。见
[PRAXO-CORE](../projects/praxo-core.md)。

**MCP（Model Context Protocol）** — 向模型暴露工具与上下文的协议。MCP 处理同步能力调用，
不是完整协调或治理层。

**Adapter（适配器）** — 把一个接口连接到另一个接口的组件，例如模型提供商适配器或网关适配器。

**Gateway（网关）** — 调解外部系统访问的边界组件。见 [LIMENORA](../projects/limenora.md)。

**Egress（出口）** — Agent 或系统的出站网络流量。出口应受治理。

**Credential injection（凭据注入）** — 在边界提供凭据，使 Agent 不持有它们。

**Rate limit（速率限制）** — 对操作频率的限制。

**Budget（预算）** — 对一次运行的成本、token、时间或步数的限制。

**Cost ceiling（成本上限）** — 任务或周期可接受的最高成本。

## 记忆、上下文与知识

**Context（上下文）** — 某一步模型可用的信息：目标、会话状态、检索项、工具描述。

**Context window（上下文窗口）** — 模型有界输入容量。它是工作集，不是记忆系统。

**Context engineering（上下文工程）** — 设计什么进入上下文、顺序、溯源以及排除什么。

**Memory（记忆）** — 跨运行持久的状态：情景、语义、程序性或工作记忆。

**Episodic memory（情景记忆）** — 具体事件与经验的记录。

**Semantic memory（语义记忆）** — 稳定事实、概念与偏好。

**Procedural memory（程序性记忆）** — 可复用流程与技能。

**Working memory（工作记忆）** — 当前任务的短期状态。

**Retrieval（检索）** — 为当前上下文从存储中选择相关信息。

**RAG（检索增强生成）** — 用检索上下文条件化模型输出。检索本身不是知识锚定。

**Grounding（知识锚定）** — 给检索材料附加意义与证据：概念、实体、主张、来源、冲突。

**Grounding view（知识锚定视图）** — 受治理知识按用途限定的投影。见
[GNOSIVELA](../projects/gnosivela.md)。

**Ontology（本体）** — 领域概念与关系的结构化集合。

**Entity resolution（实体解析）** — 判断不同引用是否指向同一实体。

**Assertion（断言）** — 关于状态或事实的主张，最好带溯源。

**Claim（主张）** — 可能真也可能假的陈述；用于决策时应带证据。

**Evidence（证据）** — 支持重建与辩护的结构化、关联、可防篡改、可保留产物。见
[证据与可审计性](evidence-and-audit.md)。

**Provenance（溯源）** — 数据、主张或产物的来源与历史。

**Bitemporal（双时间）** — 区分有效时间（何时为真）与记录时间（系统何时得知）。

**Valid time（有效时间）** — 事实在世界上为真的时间段。

**Recorded time（记录时间）** — 系统记录事实的时间。

**World model（世界模型）** — 运营状态及其证据的共享、时间性表示。见
[世界模型](world-models.md)。

**Digital twin（数字孪生）** — 特定真实系统的同步模型。

**Simulation（仿真）** — 执行系统模型以探索可能结果。

**Possible world（可能世界）** — 用于在不触碰生产的情况下测试场景的仿真世界。见
[PEIRAVELA](../projects/peiravela.md)。

**Forgetting（遗忘）** — 有意移除或过期记忆。是治理功能，不是缺陷。

**Freshness（新鲜度）** — 信息相对于用途的当前程度。

**Conflict（冲突）** — 主张或来源之间的不一致，应被治理而不是平均掉。

## 身份、安全与信任

**Identity（身份）** — 可验证的行动者（人、Agent、工作负载、服务）表示。

**Workload identity（工作负载身份）** — 绑定到运行中工作负载的身份，而不是共享密钥。

**Attestation（证明）** — 关于工作负载属性的证据，用于建立信任。见
[EIDOVELA](../projects/eidovela.md)。

**PoP（持有证明）** — 证明令牌持有者同时持有相关密钥的密码学演示。

**OIDC** — OpenID Connect，OAuth 2.0 上的身份层。

**SPIFFE** — 分布式系统工作负载身份标准。

**mTLS** — 双向 TLS，双方用证书认证。

**Token（令牌）** — 表示身份或权限的凭据，最好短期且限定范围。

**Scope（范围）** — 权限允许的行动或资源集合。

**Scope attenuation（范围衰减）** — 委托时缩减权限。

**Authority binding（权限绑定）** — Agent 与其可行使权限之间的记录关联。

**Revocation（撤销）** — 在到期前收回权限或凭据。

**Authentication（认证）** — 确认行动者是谁。

**Authorization（授权）** — 决定已认证行动者可以做什么。

**Principal（主体）** — 代表其行动的参与者。

**Tenant（租户）** — 多租户系统中的隔离组织边界。

**Namespace（命名空间）** — Agent 或资源的命名与隔离范围。

**Prompt injection（提示注入）** — 不可信内容试图改变 Agent 指令或行为。

**Data exfiltration（数据外泄）** — 未经授权把数据传出信任边界。

**Supply chain（供应链）** — 产生系统的依赖、产物与流程集合。Agent 技能与模型也是其中一部分。

**SBOM（软件物料清单）** — 组件与依赖清单。

**Signing（签名）** — 证明产物来自可信来源且未被篡改。

**Agent worm（Agent 蠕虫）** — 跨 Agent 或 Agent 系统传播的恶意行为。见
[安全模型](../architecture/security.md)。

**Denial of wallet（钱包拒绝服务）** — 造成无界成本的攻击或失败。

**Zero trust（零信任）** — 每次访问都验证，而不是信任网络位置的安全立场。

## 证据、可靠性与运维

**Observability（可观测性）** — 从指标、日志、追踪推断系统健康的能力。见
[可观测性](observability.md)。

**Telemetry（遥测）** — 关于系统行为的测量与事件。

**Trace（追踪）** — 请求跨组件路径的记录。

**Span（跨度）** — 追踪中的一个计时操作。

**Metric（指标）** — 随时间聚合的数值测量。

**Log（日志）** — 组件发出的带时间戳记录。

**Effect ledger（效果账本）** — 记录副作用、输入、决定与恢复信息的持久账本。见
[PRAXOVELA](../projects/praxovela.md)。

**Audit trail（审计轨迹）** — 可评审的决定与行动时间记录。

**Evidence bundle（证据包）** — 为决定或发布打包的一组证据。

**Evidence chain（证据链）** — 从目标到验证的关联序列。见
[证据架构](../architecture/evidence.md)。

**Tamper-evident（可防篡改）** — 可检测修改或遗漏的性质。

**Retention（保留）** — 证据或数据保留多久，以及按什么策略。

**Release gate（发布门禁）** — 发布前必须通过的检查点。

**Verification（验证）** — 检查结果是否满足契约或验收标准。

**Certification（认证）** — 对某性质的形式或独立确认。谨慎使用；多数证据不是认证。

**Reliability（可靠性）** — 系统在故障下继续正确运行的能力。见 [可靠性](reliability.md)。

**Failure domain（失败域）** — 组件失败时的影响范围。

**Blast radius（爆炸半径）** — 行动或失败可能造成的最大损害。

**Runbook（运行手册）** — 运维或恢复系统的文档化流程。

**SLO / SLI** — 服务等级目标 / 指标：服务质量目标与测量。

**Incident（事故）** — 降低或威胁系统的非计划事件。

**Postmortem（复盘）** — 对事故及其原因的结构化评审。

## 协调与协议

**Coordination（协调）** — 跨 Agent 随时间的共享状态与进展：事件、任务、租约、委托、恢复、
治理。见 [协调 vs 编排](coordination-vs-orchestration.md)。

**Orchestration（编排）** — 通过定义好的流程排序工作，通常带持久性与恢复。

**Protocol（协议）** — 交互的共享规则与消息格式。见 [Harmovela](../projects/harmovela.md)。

**Event（事件）** — 某事发生的记录。

**Task（任务）** — 有生命周期的工作单元。

**State（状态）** — 现在什么是真的，以及如何变化。

**Lease（租约）** — 对工作有期限的所有权声明。

**Claim（声明）** — 在协调中，对任务所有权或意图的断言。

**Dependency（依赖）** — 一个工作单元需要另一个的关系。

**Scheduling（调度）** — 把工作分配到时间或资源。

**Transport（传输）** — 消息移动机制（stdio、WebSocket、SSE、gRPC、NATS、Kafka、
Redis Streams）。

**Conformance fixture（一致性夹具）** — 用于验证跨实现兼容行为的测试向量。

**Interoperability（互操作性）** — 独立系统通过共享契约协作的能力。

**A2A（Agent-to-Agent）** — Agent 间交互。应作为协调与安全问题处理，而不只是消息格式。

## 业务与治理

**Governance（治理）** — 指导与约束行为的决策权、控制与证据体系。

**Accountability（问责）** — 对行动或结果作出解释的义务。

**Responsibility（责任）** — 对决定或产物的所有权分配。

**Risk（风险）** — 不确定性与后果的组合。在架构中，风险常指决策暴露，而不只是安全威胁。

**Decision exposure（决策暴露）** — 决策中的价值、不确定性、约束以及可见性不足的后果。

**Policy version（策略版本）** — 用于决定的策略标识，用于可复现与审计。

**Change control（变更控制）** — 批准、测试与回滚变更的流程。

**Separation of duties（职责分离）** — 分割权限，使单一行动者无法独自完成高风险行动。

**Audit（审计）** — 对证据与控制的独立检查。

**Compliance（合规）** — 符合法律、法规或标准。合规不等于安全或质量。

**Enterprise architecture（企业架构，EA）** — 跨企业对齐业务、数据、应用与技术的实践。

**Viewpoint（视点）** — 框定一组利益相关者关注的约定。见
[PACT 与 AVDM](../theory/research-map.md)。

**Concern（关注点）** — 架构必须处理的利益相关者兴趣或质量属性。

**Reference taxonomy（参考分类法）** — 可复用的视点或概念目录，例如 PACT。

**Adoption（采用）** — 评估、试点与集成系统的过程。见 [采用路径](../practice/adoption.md)。

**Pilot（试点）** — 用于验证价值与控制的受限部署。

**Open core（开放核心）** — 开放接口层或核心与商业版结合的模型。

**Commercial edition（商业版）** — 带额外运营或企业能力、单独许可的版本。

**Licensing（许可证）** — 项目使用、修改与分发的法律条款。仓库 `LICENSE` 是最终依据。

## 缩写

- **AADM** — Architecture Artifact Decision Model
- **AOP** — Agent-Oriented Programming
- **ARCM** — Architectural Responsibility Configuration
- **AVDM** — Architecture Viewpoint Decision Model
- **CEF** — Constraint Engineering Framework
- **DIKCA** — Data, Information, Knowledge, Control, Architecture
- **EA** — Enterprise Architecture
- **HITL** — Human-in-the-loop
- **IIC** — Intent-Conditioned Computation
- **MAS** — Multi-agent system
- **MCP** — Model Context Protocol
- **OIDC** — OpenID Connect
- **PACT** — Practical Architecture Viewpoint Taxonomy
- **PDP / PEP** — Policy Decision Point / Policy Enforcement Point
- **PPES** — Probabilistic Program Execution Semantics
- **RAG** — Retrieval-Augmented Generation
- **SBOM** — Software Bill of Materials
- **SLO / SLI** — Service Level Objective / Indicator
- **SPIFFE** — Secure Production Identity Framework for Everyone
- **UAD** — Unified Agent Dynamics
