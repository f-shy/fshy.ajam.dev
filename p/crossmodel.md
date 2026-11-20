# CrossModel

> crossmodel.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crossmodel/ | JSON https://fshy.ajam.dev/api/v1/entity/crossmodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CrossModel

- `inference/crossmodel` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://www.crossmodel.ai/docs
- free tier: No free allowance is stated on the docs read 2026-11-18: the gateway bills actual token usage and rejects requests when the balance runs out. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an API key tied to a topped-up balance is required before calls succeed
- interface: rest
- limits:
  - volume-quota (binding): pay per actual token usage; requests rejected when balance runs out [1]
- endpoint: https://api.crossmodel.ai/v1
- tooling: an OpenAI-compatible (cm-) or Anthropic-compatible key with base_url swap
- composes with: the prepaid balance is the scarce link; no free tier is published
- reliability: rate limits are tracked per key and return 429 rate_limit_error when exceeded
- evidence:
  - [1] 2026-11-18: billing is per token and requests fail without balance | capture: sha256:8098eb09c61d0f63dedce0ec0066dd3bcb5a218b0825924d518d1683fdf2d037 | quote: you pay for actual token usage; requests are rejected when your balance runs out.
- sources:
  - [1] https://www.crossmodel.ai/docs
