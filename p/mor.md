# Morpheus

> mor.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mor/ | JSON https://fshy.ajam.dev/api/v1/entity/mor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Morpheus

- `compute/morpheus` | paid-only | evidence documented | binding write-gated | category inference API
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://mor.org/inference-api
- free tier: OpenAI-compatible inference through TEE-backed providers on a decentralized network, priced per model: Gemma 4 26B at USD 0.15 input and USD 0.40 output per 1M tokens, Kimi K2.5 at USD 0.60 and USD 3.00. Access without paying per token is bought by staking: 'Stake your MOR to get inference from the Morpheus network.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: rest
- limits:
  - write-gated (binding): Every route needs MOR: either per-token payment or a stake that converts to a daily inference session, and MOR must be bought on an exchange first. [1]
- limits note: Every route needs MOR: either per-token payment or a stake that converts to a daily inference session, and MOR must be bought on an exchange first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Morpheus also pays up to 12% APR on deposited stETH, WETH, USDC or USDT, so capital placed there earns MOR that can be restaked for inference; the loop needs capital at the start.
- reliability: no reliability event recorded
- notes: The MOR-per-inference conversion rate is not published on the pages read; mor.org/calc.html is the comparison tool and runs client-side. Without that rate the staking route cannot be priced, and a per-token comparison at USD 0.15 per 1M input is close to centralized list prices, so the stake is a convenience, not a discount, unless the rate is generous.
- extras:
  - facets.class: crypto-capital-gate
- evidence:
  - [1] 2026-10-22: 'Stake your MOR to get inference from the Morpheus network'; endpoint https://api.mor.org/api/v1, OpenAI-compatible
  - [2] 2026-10-22: per-model rates: Gemma 4 26B USD 0.15/0.40 per 1M, Kimi K2.5 USD 0.60/3.00 per 1M
  - [3] 2026-10-22: MOR USD 0.859515
- sources:
  - [1] https://mor.org/inference-api
  - [2] https://mor.org/inference-api/models
  - [3] https://api.coingecko.com/api/v3/simple/price?ids=morpheusai&vs_currencies=usd
