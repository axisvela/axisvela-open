# Agent architecture

Architecture is where governance becomes enforceable. A policy that exists only
in a prompt is advice; a policy attached to a boundary is control.

This section describes the architecture patterns behind the AxisVela projects,
independent of any single product. The patterns are intentionally composable:
you can adopt one seam without adopting the whole ecosystem.

## Four principles

1. **Control at boundaries.** Put policy, identity, and egress controls where
   actions cross a boundary, not in the middle of a prompt.
2. **Separate the planes.** The data plane executes; the control planes decide,
   authorize, coordinate, and verify.
3. **Evidence by construction.** If an action matters, the architecture should
   produce the evidence as a side effect of doing the work.
4. **Deploy in shapes.** Local-first, server, hybrid, and edge deployments have
   different trust boundaries. The architecture should name them.

## Reading order

| Page | Question |
| --- | --- |
| [Reference architecture](reference-architecture.md) | What does a complete agent system look like? |
| [Runtime](runtime.md) | What happens inside an agent runtime? |
| [Control planes](control-planes.md) | Where are identity, policy, capability, coordination, and assurance decided? |
| [Contracts](contracts.md) | How do independent products integrate without a shared kernel? |
| [Knowledge](knowledge.md) | How do memory, grounding, and world models fit? |
| [Evidence](evidence.md) | How does the system produce defensible evidence? |
| [Deployment](deployment.md) | What are the deployment shapes and trust boundaries? |
| [Security](security.md) | What are the threats and the controls? |
| [Ecosystem map](../ecosystem-map.md) | Which projects implement which parts? |

## Relationship to the theory

The architecture pages apply the ideas in [Agent theory](../theory/index.md):

- UAD’s cognitive/computational/organizational layers become runtime, control,
  and program architecture.
- DIKCA’s control and architecture layers become enforceable controls and
  structural contracts.
- IIC/AOP’s intent and control separation becomes explicit goals, plans,
  policies, and verification.
- PPES’s distributional view becomes evidence and verification architecture.

## A warning

There is no single “correct” architecture. The right shape depends on the risk,
the deployment boundary, and the evidence you need. Treat these pages as a
catalog of patterns and trade-offs, not a mandate.
