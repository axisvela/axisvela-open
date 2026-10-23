# Build an agent

This guide builds a minimal governed agent with
[PRAXO-CORE](../projects/praxo-core.md). The goal is not a chatbot; it is a loop
with explicit model, tool, policy, event, and evidence boundaries.

## 1. Get the framework

```bash
git clone https://github.com/axisvela/praxo-core
cd praxo-core
go test ./...
```

PRAXO-CORE requires Go 1.25+ (see `go.mod`). The quickstart uses an
OpenAI-compatible endpoint.

```bash
export PRAXO_BASE_URL=http://localhost:11434/v1
export PRAXO_MODEL=llama3.2
GOWORK=off go run ./examples/quickstart
```

On PowerShell:

```powershell
$env:PRAXO_BASE_URL = "http://localhost:11434/v1"
$env:PRAXO_MODEL = "llama3.2"
$env:GOWORK = "off"
go run ./examples/quickstart
```

## 2. The shape of the loop

The core API is intentionally small. A typical construction looks like this
(check the repository for the current signature):

```go
ag, err := agent.New(agent.Options{
    Model:    myModel,
    Tools:    tools,
    Events:   sink,
    Policy:   hook,
    MaxSteps: 8,
})
if err != nil {
    return err
}

result, err := ag.Run(ctx, agent.Session{
    ID:          "session-1",
    TenantID:    "acme",
    WorkspaceID: "default",
}, "Inspect the failing test and propose a fix")
```

The important parts are not the names; they are the boundaries:

- **Model** — a provider-neutral interface.
- **Tools** — explicit contracts with validated inputs.
- **Events** — what happened, for coordination and evidence.
- **Policy** — a decision before an action.
- **MaxSteps** — a bound on autonomy.

## 3. Add one tool

Start with a read-only tool. Give it:

- a name and description;
- an input schema;
- a clear failure mode;
- a result that can be recorded.

Do not start with shell execution or unrestricted file writes. Add capabilities
in increasing blast radius.

## 4. Add a policy hook

A policy hook should answer a narrow question: *may this action proceed under
this identity, capability, and context?*

Start with deny-by-default. Allow specific tools for specific sessions. Log the
decision. If the policy cannot explain a denial, it is not ready.

## 5. Add an event sink

Emit events for:

- run started / finished;
- model call;
- tool invocation;
- policy decision;
- error and recovery.

These events are the raw material for evidence, coordination, and debugging.

## 6. Add memory (optional)

If the agent needs durable context, add [MNEMOVELA](../projects/mnemovela.md)
through the memory seam. Keep session state and durable memory separate. A long
prompt is not a memory architecture.

## 7. Make it governable

Before calling the agent “done,” check:

- [ ] The tool set is minimal and explicit.
- [ ] There is a step and budget limit.
- [ ] Policy is checked before side effects.
- [ ] Every material action is recorded.
- [ ] A failed run can be diagnosed.
- [ ] The model can be swapped without rewriting the agent.

## Next

- [Govern the agent](govern-an-agent.md) — identity, approvals, and evidence.
- [Add memory and context](memory-and-context.md) — durable and grounded state.
- [Verify and simulate](verify-and-simulate.md) — evidence before release.
