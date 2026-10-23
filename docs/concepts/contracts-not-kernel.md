# Contracts, not a kernel

AxisVela is not a single runtime with plugins. It is a family of independently
versioned products that compose through **versioned contracts**.

That choice has consequences.

## The idea

A shared kernel makes integration easy inside one product and expensive
everywhere else: every consumer inherits the kernel’s release cadence, failure
modes, and governance model. A contract boundary keeps the integration surface
small and lets each side evolve independently.

In practice, a contract can be:

- a versioned API or OpenAPI document;
- a JSON Schema or protocol specification;
- an SDK with a compatibility policy;
- a conformance fixture set;
- a signed artifact format.

The contract is the product boundary. The implementation behind it can change.

## Benefits

- **Independent versioning.** A product can release without forcing every
  consumer to upgrade.
- **Replaceability.** An implementation can be swapped if the contract holds.
- **Organizational fit.** Different teams can own different products without a
  shared release train.
- **Clear licensing.** The open surface can be Apache-2.0 while the runtime is
  separately licensed.

## Costs

- **Integration discipline.** Contracts must be versioned, documented, and
  tested.
- **Conformance work.** “Compatible” needs fixtures, not a press release.
- **More repositories.** The map matters more when the system is not a monorepo.

AxisVela accepts these costs because the alternative — a single kernel that owns
every domain — would make the governance and licensing boundaries impossible to
keep clean.

## Where to see it

- [Harmovela](../projects/harmovela.md) is a protocol with schemas and
  cross-language conformance fixtures.
- The `*-open` repositories publish versioned contracts and SDKs.
- [Enterprise Autonomy](../projects/enterprise-autonomy.md) shows products
  composing across those boundaries in end-to-end examples.

## A useful question

When evaluating a product, ask: *what is the contract, and what happens when the
implementation behind it changes?* If the answer is “the same repository,” it is
a module, not a contract.
