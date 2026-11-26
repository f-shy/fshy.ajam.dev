# Morpheus

> mor.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mor/ | JSON https://fshy.ajam.dev/api/v1/entity/mor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Morpheus

- `compute/morpheus` | paid-only | evidence documented | binding write-gated | category inference API
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:17:30.951Z (live) | stale on 2026-12-26
- url https://mor.org/inference-api
- free tier: OpenAI-compatible AI inference for developers: route production AI traffic through a decentralized inference network with TEE-backed providers, no vendor lock-in, and the same API shape existing apps use; endpoint https://api.mor.org/api/v1. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
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
  - [1] 2026-11-25: the page describes an OpenAI-compatible inference API at https://api.mor.org/api/v1 over TEE-backed providers | capture: sha256:3621b104b072d17a244db66594d31bc722096066e3f48902b4acbc047245cc60 | quote: OpenAI-compatible AI inference for developers. Route production AI traffic through a decentralized inference network with TEE-backed providers, no vendor lock-in, and the same API shape your apps already use.
  - [1] 2026-11-25: the inference API exposes GLM 5, Kimi K2.5, MiniMax M2.5, Qwen3 Coder, Gemma 4, Arcee Trinity and 40+ more models through one API | capture: sha256:3621b104b072d17a244db66594d31bc722096066e3f48902b4acbc047245cc60 | quote: Access GLM 5, Kimi K2.5, MiniMax M2.5, Qwen3 Coder, Gemma 4, Arcee Trinity, and 40+ more models through one API.
  - [1] 2026-11-25: the page still describes the OpenAI-compatible inference API at https://api.mor.org/api/v1 over TEE-backed providers | capture: sha256:3621b104b072d17a244db66594d31bc722096066e3f48902b4acbc047245cc60 | quote: OpenAI-compatible AI inference for developers. Route production AI traffic through a decentralized inference network with TEE-backed providers, no vendor lock-in, and the same API shape your apps already use.
- sources:
  - [1] https://mor.org/inference-api
  - [2] https://mor.org/inference-api/models
  - [3] https://api.coingecko.com/api/v3/simple/price?ids=morpheusai&vs_currencies=usd
