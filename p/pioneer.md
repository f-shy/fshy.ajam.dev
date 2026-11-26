# Pioneer

> pioneer.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pioneer/ | JSON https://fshy.ajam.dev/api/v1/entity/pioneer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pioneer

- `inference/pioneer` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://agent.pioneer.ai/llms.txt
- free tier: No free text allowance stated; the Fastino docs describe a paid API key (FASTINO_API_KEY) and per-1M-token inference prices such as GLiDE at USD 0.04 input / USD 0 output. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key from the platform; signup fields not detailed
- interface: rest
- limits:
  - volume-quota (binding): per-token billing; no free tier stated [2]
- endpoint: https://api.fastino.ai/v1
- tooling: OpenAI-compatible client and the vendor SDKs against api.fastino.ai/v1
- composes with: no free tier published; inference bills per token after credit top-up
- reliability: Auto Train is private with no public route; GLiDE output tokens are priced at USD 0
- notes: No self-serve free text allowance found; pricing is per token with no free credit grant.
- evidence:
  - [1] 2026-11-18: the docs index lists pricing and an API-key authentication page | capture: sha256:7aa8c4a501f9e22947410515a1512bab086981e47ed9d5b6c5b15a5b90e8558b | quote: Read API keys from `FASTINO_API_KEY` and never embed credentials in code, logs, or reports.
  - [2] 2026-11-18: inference is priced per 1M tokens | capture: sha256:935ba050ef9709cabd047e0c524d2874d4ce67269a99bedbd4baf9ccc6417a6e | quote: GLiDE | \$0.04 | \$0
- sources:
  - [1] https://agent.pioneer.ai/llms.txt
  - [2] https://docs.fastino.ai/pricing.md
