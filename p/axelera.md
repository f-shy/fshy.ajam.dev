# Axelera AI Voyager

> axelera.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/axelera/ | JSON https://fshy.ajam.dev/api/v1/entity/axelera.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Axelera AI Voyager

- `compute/axelera-ai-voyager` | qualifies-with-caveat | evidence documented | binding none | category cloud VM
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://community.axelera.ai/product-updates/introducing-voyager-wingman-the-fastest-way-to-build-ai-on-axelera-ai-1421
- free tier: A free assistant for Axelera's Voyager SDK, gated by a free community account: 'Access is simple, and free. Registering here on the Axelera community sets you up with a Voyager Wingman account' and 'create an account here on the Axelera community so you can get (free) access to Voyager Wingman and get started immediately with a EUR 25 token voucher'. The vendor states what it does not buy: 'running a pipeline on an Axelera device needs the Linux app on a machine with a card. Web chat will happily plan and write the pipeline, but the card work happens on Linux.' | unit: tokens | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-off-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a free community account: 'Registering here on the Axelera community sets you up with a Voyager Wingman account', and the community front page calls it 'completely free with a community account (which is also free)'. The registration form's fields are not described in any evidence row, so whether an email, phone number or ID document is required is unknown, and no card, hold or payment method is mentioned: unknown.
- interface: unknown
- limits note: EUR 25 of tokens is the whole allowance and no device is attached, so nothing about throughput binds before the voucher is spent.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It composes with nothing on the compute side. The only hardware Axelera ships to an individual is a competition kit: ten selected builders receive a Dell Pro Slim Plus XE5 with a Metis PCIe AIPU, which is a loan of physical hardware that would have to be housed.
- reliability: no reliability event recorded
- notes: The EUR 25 is denominated in assistant tokens, not accelerator-hours, and the announcement does not state an expiry, so expiry is null. The capacity that matters, Metis silicon, needs a purchased card, which the analysis excludes: it assumes no local hardware. The SDK, model zoo and assistant are free and the wall is the card.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: one-off-credit
  - facets.shape.gpu_class: Axelera Metis AIPU, not provided
- evidence:
  - [1] 2026-10-22: 'Access is simple, and free. Registering here on the Axelera community sets you up with a Voyager Wingman account' and 'a EUR 25 token voucher', both quoted
  - [1] 2026-10-22: 'running a pipeline on an Axelera device needs the Linux app on a machine with a card... the card work happens on Linux', quoted
  - [2] 2026-10-22: the community front page repeats that the assistant is 'completely free with a community account (which is also free)'
- sources:
  - [1] https://community.axelera.ai/product-updates/introducing-voyager-wingman-the-fastest-way-to-build-ai-on-axelera-ai-1421
  - [2] https://community.axelera.ai/
