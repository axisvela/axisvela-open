# Relationship index

The map’s edges, with the reason each relationship exists. An edge means “this
project produces something another can consume”; it does **not** mean the
projects must be deployed together.

| From | Relationship | To | Why it matters |
| --- | --- | --- | --- |
| PRAXO-CORE | powers | PRAXOVELA | PRAXOVELA is the product runtime built on the framework. |
| PRAXO-CORE | model seam | NOETIVELA | Model and endpoint routing can be supplied as an adapter. |
| PRAXO-CORE | memory seam | MNEMOVELA | Durable memory and retrieval plug into the loop. |
| PRAXO-CORE | event seam | HARMOVELA | Coordination events can be published to the protocol. |
| PRAXO-CORE | retrieval seam | GNOSIVELA | Grounded knowledge can be retrieved as context. |
| PRAXO-CORE | policy seam | AEGIVELA | Authorization decisions can gate tool calls. |
| PRAXO-CORE | tool seam | LIMENORA | External tools can be reached through a governed gateway. |
| PRAXO-CORE | execution seam | RHEOVELA | Graph or process execution can be delegated to a durable runtime. |
| NOMIVELA | registry context | EIDOVELA | Identity issuance/verification consumes registry and authority-binding context without taking registry write ownership. |
| EIDOVELA | verified identity | AEGIVELA | Authorization consumes a verified identity context. |
| NOMIVELA | authority context | AEGIVELA | Bindings and lifecycle epochs inform policy decisions. |
| GNOSIVELA | grounds | ONTOVELA | Concepts and evidence-backing ground the world model. |
| ONTOVELA | world state | ORCHADYN | Plans are generated against current and historical state. |
| ONTOVELA | world state | PEIRAVELA | Simulations start from an explicit world model. |
| ORCHADYN | plans | MODUREGIS | Plans are checked against governed capabilities. |
| MODUREGIS | governed capabilities | RHEOVELA | Process steps invoke capabilities under policy and audit. |
| RHEOVELA | approvals and exceptions | SYMBIVELA | Humans review, approve, intervene, and accept outcomes. |
| SYMBIVELA | decisions and evidence | AEGIVELA | Approvals and revocations feed the authorization record. |
| TEKMOVELA | verifies | PRAXOVELA, RHEOVELA, KINETOVELA | Verification contracts and release gates apply to runtimes and missions. |
| PEIRAVELA | simulation evidence | TEKMOVELA | Simulation results become evidence for release decisions. |
| SYNDOVELA | skill provenance | MODUREGIS | Composed skills enter the capability catalog with provenance. |
| LIMENORA | external access | PRAXOVELA, RHEOVELA | Outside systems are reached through one governed boundary. |
| TAXOVELA | architecture design | Enterprise Autonomy | Reference architectures and validations inform the examples. |
| PAMP | portfolio management | Enterprise Autonomy | The architecture portfolio frames the program. |
| COORDIVELA | development coordination | Ecosystem projects | Work on the ecosystem itself is coordinated with leases and dependencies. |
| HARMOVELA | runtime coordination | PRAXO-CORE agents | Async coordination is available to agents and runtimes. |
| Enterprise Autonomy | composes | All projects | End-to-end examples show the seams in use. |

## Planned edges: not shipped

[AKROVELA](../projects/akrovela.md) and [DIDACTOVELA](../projects/didactovela.md)
are **unreleased 0.1.0 bootstrap only**: operational health/schema-readiness/version
APIs and source Go version clients. They have no domain execution, datasets,
training, robot integration, binaries or published SDKs. Every edge below is
planned, shown dashed on the [ecosystem map](../ecosystem-map.md), not a verified
integration or an Enterprise Autonomy example.

| From | Planned relationship | To | Authority boundary |
| --- | --- | --- | --- |
| KINETOVELA | bounded operations | AKROVELA | Mission/assignment/effect lifecycle stays with KINETOVELA; local attempts and receipts belong to AKROVELA's intended scope. |
| SYNDOVELA | desired composition | AKROVELA | Bundle, ResolutionLock and desired Runtime Profile stay with SYNDOVELA; no second resolver. |
| MODUREGIS | capability references | AKROVELA | Capability contracts stay with MODUREGIS; ORCHADYN remains the planner. |
| RHEOVELA | workflow delegation | AKROVELA | Durable cross-service Process stays with RHEOVELA; local journaling is not workflow authority. |
| AKROVELA | capture references | DIDACTOVELA | Intended capture admission and dataset lineage do not transfer Mission authority. |
| PEIRAVELA | raw experiment evidence | DIDACTOVELA | Raw SimulationEvidence stays with PEIRAVELA; dataset snapshots and labels are DIDACTOVELA's intended scope. |
| DIDACTOVELA | candidate artifacts | NOETIVELA | Production model/endpoint activation requires explicit authorized admission; training is not deployment. |
| DIDACTOVELA | assessment inputs | TEKMOVELA | Producer metrics cannot issue independent assurance verdicts. |

ONTOVELA retains operational world truth, not raw learning episodes. PRAXO-CORE
remains the MIT framework; no new Core API or robotics runtime is implied.
Robot-local safety remains independent of Mission and site execution.

## Reading the edges

- **Seams are optional.** PRAXO-CORE can run without NOETIVELA or MNEMOVELA.
- **Edges are directional.** A project can produce evidence another consumes
  without depending on it at runtime.
- **The program is not a product.** Enterprise Autonomy composes the products;
  it does not replace their authority.

## Machine-readable

The same relationships are represented in
[`projects.yaml`](https://github.com/axisvela/axisvela-open/blob/main/projects.yaml)
under `relates_to`. For the two bootstrap entries these are planned associations,
as stated in their `value` wording, not shipped dependencies.
