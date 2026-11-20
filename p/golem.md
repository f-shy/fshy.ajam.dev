# Golem Network

> golem.network | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/golem/ | JSON https://fshy.ajam.dev/api/v1/entity/golem.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Golem Network

- `compute/golem-network` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.golem.network/docs/golem/overview/requestor-faq
- free tier: Peer-to-peer compute priced by each provider per CPU-hour; mainnet requestors pay in GLM plus gas. The only free lane is the testnet: tGLM is 'test currency that you can obtain for free to test your requestor node. These tokens have no real value.' GLM was USD 0.110439 on 2026-10-22. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: testnet-faucet
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - write-gated (binding): Real capacity requires GLM on mainnet plus gas, which requires a purchase; the free testnet token carries no capacity guarantee. [1]
- limits note: Real capacity requires GLM on mainnet plus gas, which requires a purchase; the free testnet token carries no capacity guarantee.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At GLM USD 0.1104, a provider asking 0.1 GLM per CPU-hour costs about USD 0.011 per CPU-hour, below most list prices; the chain breaks on gas per agreement and on the thin provider market.
- reliability: no reliability event recorded
- notes: A third-party report says the testnet marketplace shows 0 active offers, which could not be confirmed because the page is rendered in JavaScript. A measured CPU-hour price would need a funded mainnet requestor node.
- extras:
  - facets.class: depin-marketplace
  - facets.free_tier_kind: testnet-faucet
- evidence:
  - [1] 2026-10-22: tGLM is free test currency with no real value; GLM is the tradeable token
  - [2] 2026-10-22: testnet tokens come from a faucet and 'It is free, but you cannot expect capacity and performance'; mainnet needs GLM plus gas
  - [3] 2026-10-22: GLM USD 0.110439
  - [4] 2026-10-22: marketplace page read 200; offers render client-side, so the live offer count was not readable from the extracted text
- sources:
  - [1] https://docs.golem.network/docs/golem/overview/requestor-faq
  - [2] https://docs.golem.network/docs/golem/overview
  - [3] https://api.coingecko.com/api/v3/simple/price?ids=golem&vs_currencies=usd
  - [4] https://marketplace.golem.network/
