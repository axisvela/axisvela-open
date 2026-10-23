# Govern an agent

A working agent is not a governed agent. This guide adds the control planes that
make autonomy defensible.

## 1. Give the agent an identity

Do not authenticate agents with shared API keys. Use workload identity and
short-lived, proof-of-possession tokens.

- [EIDOVELA](../projects/eidovela.md) issues identity and verifies workload
  attestation.
- [NOMIVELA](../projects/nomivela.md) records the agent, namespace, authority
  bindings, and lifecycle epoch.
- [AEGIVELA](../projects/aegivela.md) authorizes actions and enforces decisions
  through a PEP.

The minimum questions:

- Which workload is this?
- Which tenant and namespace does it belong to?
- What authority is bound to it?
- How is the credential rotated and revoked?

## 2. Bound the capabilities

Make the capability set explicit:

- publish capabilities in a governed catalog
  ([MODUREGIS](../projects/moduregis.md));
- attach policy and metadata to each capability;
- deny unknown capabilities by default;
- record every invocation.

A capability is not just a function. It has an owner, a risk level, a policy, and
an audit trail.

## 3. Put policy outside the prompt

Move governance from instructions to enforcement:

- evaluate policy before the action;
- use a PEP at the boundary;
- attenuate authority when delegating;
- support revocation;
- record the decision and the policy version.

If the only thing preventing a bad action is a sentence in the system prompt, the
action is not governed.

## 4. Add human approval for high-risk steps

Define what “high-risk” means. Examples:

- destructive data changes;
- financial transactions;
- external communication;
- physical actuation;
- privilege changes.

Route those steps through [SYMBIVELA](../projects/symbivela.md) or an equivalent
approval path. The approval should reference the plan, the capability, the
evidence, and the accountable person.

## 5. Produce evidence

Record the chain:

```text
goal → plan → capability → policy decision → identity → effect → outcome
```

Use the effect ledger, process history, or verification bundle appropriate to
the runtime. Retain it according to policy. Make it tamper-evident.

## 6. Test the controls

- Try an unauthorized tool. It should be denied.
- Try a delegated action with excessive scope. It should be attenuated.
- Revoke authority mid-run. It should stop.
- Remove the policy service. High-risk actions should fail closed.
- Tamper with evidence. The system should detect it.
- Replay a failed run. Effects should not be duplicated.

## A governance checklist

- [ ] Identity is workload-based, not a shared key.
- [ ] The agent is registered with an owner and lifecycle.
- [ ] Capabilities are cataloged and deny-by-default.
- [ ] Policy is enforced outside the prompt.
- [ ] Delegation attenuates authority.
- [ ] High-risk actions require approval.
- [ ] Evidence links the full decision chain.
- [ ] Revocation and recovery have been tested.
- [ ] A human can intervene.

## Next

- [Durable process](durable-process.md) — long-running governed work.
- [Security model](../architecture/security.md) — threat-model the design.
