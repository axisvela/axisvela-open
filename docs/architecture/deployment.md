# Deployment shapes

The same architectural patterns can be deployed in different shapes. The shape
determines the trust boundary, where controls live, and what evidence is
available.

## Four shapes

### 1. Local-first

The agent runs on a user’s machine. Data and tools are local; the model may be
local or remote.

- **Trust boundary:** the device and the user session.
- **Controls:** local policy, sandbox, capability allowlist, local effect ledger.
- **Evidence:** local ledger and trace; export for audit if needed.
- **Best fit:** personal agents, desktop automation, offline work.
- **Examples:** PRAXOVELA, PRAXO-CORE embedded in a tool.

### 2. Single-tenant service

The agent runs as a service for one organization.

- **Trust boundary:** the service boundary and the enterprise network.
- **Controls:** workload identity, policy service, capability catalog, gateway.
- **Evidence:** central evidence store, process history.
- **Best fit:** internal automation, long-running workflows.
- **Examples:** RHEOVELA, LIMENORA, MODUREGIS.

### 3. Enterprise hybrid

Some components run on-premises, some in a private cloud, some at the edge.

- **Trust boundary:** multiple, with explicit federation.
- **Controls:** federated identity, policy, data residency, gateway per boundary.
- **Evidence:** aggregated with provenance and retention rules.
- **Best fit:** regulated enterprises, multi-site operations.
- **Examples:** Enterprise Autonomy reference stacks.

### 4. Edge and physical

The agent controls or mirrors a physical system.

- **Trust boundary:** the device, the network link, and the physical world.
- **Controls:** bounded missions, local safety interlocks, human override,
  simulation before deployment.
- **Evidence:** mission records, sensor evidence, recovery logs.
- **Best fit:** robots, industrial systems, remote assets.
- **Examples:** KINETOVELA, ONTOVELA twins, PEIRAVELA simulation.

## Deployment matrix

| Concern | Local-first | Single-tenant service | Enterprise hybrid | Edge / physical |
| --- | --- | --- | --- | --- |
| Identity | User + device | Workload + tenant | Federated | Device + workload |
| Policy | Local | Central | Federated | Local safety + central |
| Capability catalog | Local allowlist | Central registry | Federated | Mission-specific |
| Evidence | Local ledger | Central store | Aggregated | Mission record |
| Recovery | Checkpoint | Durable process | Multi-site | Safe stop / recovery |
| Verification | Unit / trace | Integration / contract | Cross-system | Simulation + field |

## Design questions

1. Where does the action cross a trust boundary?
2. Which control must be local for latency or safety?
3. Which control must be central for consistency?
4. Where does evidence need to survive a device or site failure?
5. What is the offline behavior?
6. How are secrets and credentials injected?
7. How are updates and model changes rolled out and verified?

## Start small

A common adoption path:

1. Local-first pilot with PRAXO-CORE and a bounded tool set.
2. Add identity, policy, and evidence.
3. Move long-running work to a durable workflow runtime.
4. Add a gateway for external systems.
5. Add verification and simulation before expanding autonomy.
6. Federate only when the organizational boundary requires it.

The mistake is to start with the most complex shape because the diagram looks
impressive. Start with the smallest shape that has a real trust boundary.

## What to take away

- Deployment shape is an architectural decision, not an afterthought.
- Controls should live at the boundary they protect.
- Evidence and recovery must match the failure modes of the shape.
- Hybrid and edge deployments need explicit federation, not hope.
