# Enterprise agent taxonomy

**Source:** Huiwen Han, *Unified Agent Dynamics* (2026),
[doi:10.5281/zenodo.19822201](https://doi.org/10.5281/zenodo.19822201).

> “Agent” is not one category. An application agent, a service agent, an agent
> employee, a physical twin, and a human twin have different risks and different
> governance needs.

UAD proposes a five-type taxonomy for enterprise agents. The categories are
useful because they force different answers to identity, authority, evidence,
and failure-consequence questions.

## The five types

| Type | What it is | Typical risk | Governance emphasis |
| --- | --- | --- | --- |
| **Agent as Application** | A user-facing agent embedded in a product or workflow | Wrong output, data leakage | Sandboxing, user consent, output evidence |
| **Agent as Service** | A long-running service invoked by other systems | Availability, runaway cost, uncontrolled egress | Identity, rate/cost policy, integration boundary |
| **Agent as Employee** | An agent with a role, responsibilities, and delegated authority | Over-delegation, accountability gaps | Registry, authority bindings, approvals, performance review |
| **Agent as Physical Twin** | A software agent controlling or mirroring a physical asset | Safety, irreversible effects | Simulation, bounded missions, human override, recovery |
| **Agent as Human Twin** | A model of a person’s preferences, knowledge, or authority | Misrepresentation, privacy, consent | Consent, scope, revocation, provenance |

The taxonomy is not a maturity ladder. A system can contain several types at
once, and an agent can change type as its authority or embodiment changes.

## Lifecycle questions

Regardless of type, an enterprise agent needs a lifecycle. The UAD paper models
this as a finite state machine. At a practical level, the questions are:

- Who proposes the agent?
- Who registers it and assigns a namespace?
- What identity does it receive?
- What authority is bound to it?
- When is it suspended, revoked, or retired?
- What evidence remains after retirement?

The exact state names are less important than the existence of explicit
transitions and an owner for each transition.

## How it maps to AxisVela

| Type | AxisVela examples |
| --- | --- |
| Application | A PRAXOVELA desktop agent; a TAXOVELA skill workflow |
| Service | A NOETIVELA routing service; a LIMENORA gateway; a RHEOVELA worker |
| Employee | An agent registered in NOMIVELA, authorized by AEGIVELA, reviewed in SYMBIVELA |
| Physical Twin | A KINETOVELA fleet mission; an ONTOVELA asset twin |
| Human Twin | A governed representation of a person’s context or authority (design space; handle with consent and scope) |

The mapping is illustrative, not a product classification.

## What to take away

- Classify the agent before choosing controls.
- Different types need different identity, evidence, and approval models.
- Physical and human twins raise the cost of failure; design for override and
  revocation.
- Make lifecycle transitions explicit and auditable.
