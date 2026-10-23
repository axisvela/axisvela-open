# Connect external systems

Agents become useful when they can reach real systems. They also become risky.
This guide uses [LIMENORA](../projects/limenora.md) as the pattern for a governed
boundary.

## The problem with direct connections

If an agent can call an API directly:

- credentials end up in prompts or configuration;
- egress destinations are uncontrolled;
- policy is bypassed;
- evidence is scattered;
- a compromised agent has a direct path out.

A gateway centralizes the boundary and makes it observable.

## The pattern

```text
Agent / workflow → LIMENORA gateway → external API / MCP / webhook / event bus
                         │
                         ├─ identity and policy
                         ├─ destination allowlist
                         ├─ credential injection
                         └─ evidence
```

## 1. Define the destinations

List the external systems the agent may reach. Classify them:

- read-only vs write;
- internal vs external;
- sensitive vs public;
- synchronous vs event-driven.

Start with read-only and a small allowlist.

## 2. Move credentials to the gateway

The agent should not hold long-lived credentials. The gateway injects them at
the boundary, scoped to the destination and the request.

Check:

- where secrets are stored;
- how they are rotated;
- whether they appear in logs or traces;
- whether the agent can exfiltrate them.

## 3. Enforce policy at the boundary

The gateway should consult policy before forwarding a request:

- is this destination allowed for this identity?
- is this operation allowed?
- does it need approval?
- does it exceed a rate or cost limit?

A denial should produce evidence, not just an error.

## 4. Record the crossing

For each request, record:

- identity and authority;
- destination and operation;
- policy decision;
- request metadata (not necessarily the full payload);
- response status;
- correlation ID.

This is the evidence that the boundary held.

## 5. Handle failure

- timeouts and retries;
- idempotency keys;
- circuit breaking;
- dead-letter handling for events;
- recovery after a gateway restart.

The gateway is part of the reliability architecture, not just security.

## A checklist

- [ ] The agent has no direct egress.
- [ ] Destinations are allowlisted.
- [ ] Credentials are injected, not embedded.
- [ ] Policy is evaluated at the boundary.
- [ ] Requests and decisions are recorded.
- [ ] Rate and cost limits exist.
- [ ] Failure and retry behavior is defined.
- [ ] The gateway is monitored and can be revoked.

## Anti-patterns

- Putting API keys in the system prompt.
- Letting the agent call arbitrary URLs.
- Logging full payloads with secrets.
- A gateway that forwards without policy.
- Treating the gateway as optional for “internal” systems.

## Next

- [Security model](../architecture/security.md) — the broader threat model.
- [Verify and simulate](verify-and-simulate.md) — test the boundary.
