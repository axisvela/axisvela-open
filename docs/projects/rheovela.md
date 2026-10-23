# RHEOVELA

**Repository:** [axisvela/rheovela-open](https://github.com/axisvela/rheovela-open) ·
**License:** Apache-2.0 · **Language:** Go, with multi-language worker SDKs · **Layer:** Work and capabilities

> A durable workflow platform for long-running work that must survive failures,
> approvals, and audit.

## The problem

A workflow that only works while everything is healthy is a demo. Real processes
span hours or days, cross system boundaries, require human approval, and must
resume correctly after a crash without repeating side effects.

RHEOVELA treats a process as an event-sourced, deterministic state machine with
idempotent commands — not as a script with retries.

## What it provides

- Event-sourced process instances.
- A deterministic kernel and atomic, idempotent command pipeline.
- Durable execution with recovery.
- Versioned contracts and a five-language worker SDK set.
- HTTP Worker API and OpenAPI specification.
- A model for materializing governed capability plans into process instances.

## Why it matters

- **Recoverability.** Work resumes from recorded history rather than from an
  unknown state.
- **Auditability.** The process history is the source of truth.
- **Language-neutral workers.** Existing services can participate without
  rewriting in one language.

## How it fits

RHEOVELA executes plans produced by [ORCHADYN](orchadyn.md) under capabilities
governed by [MODUREGIS](moduregis.md). Human approvals and exceptions can be
routed through [SYMBIVELA](symbivela.md), and outcomes can be verified by
[TEKMOVELA](tekmovela.md).

## Start

- [Rheovela Open repository](https://github.com/axisvela/rheovela-open)
