# LIMENORA

**Repository:** [axisvela/limenora-open](https://github.com/axisvela/limenora-open) ·
**License:** Apache-2.0 · **Language:** Go · **Layer:** Boundary and assurance

> A governed north-south boundary between agents and the outside world.

## The problem

An agent that can call any API, MCP server, webhook, or event bus directly is an
uncontrolled egress path. Credentials spread into prompts and configuration;
policy is bypassed; and there is no reliable record of what crossed the
boundary.

LIMENORA makes external access a governed gateway decision.

## What it provides

- Edge and enterprise gateway roles.
- HTTP proxying, CONNECT, webhooks, and event ingress.
- TLS interception for governed traffic.
- Policy enforcement at the boundary.
- Credential injection without exposing secrets to the agent.
- Evidence for requests and decisions.
- MCP and partner-system integration patterns.

## Why it matters

- **One boundary.** External access is centralized and observable.
- **Secrets stay out of the agent.** Credentials are injected at the gateway.
- **Policy is enforced where traffic actually flows.**

## How it fits

LIMENORA fills the tool and integration seam in [PRAXO-CORE](praxo-core.md). It
connects [PRAXOVELA](praxovela.md), [RHEOVELA](rheovela.md), and other runtimes
to APIs and MCP servers while keeping [AEGIVELA](aegivela.md) policy in the
decision path.

## Start

- [Limenora Open repository](https://github.com/axisvela/limenora-open)
