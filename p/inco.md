# Inco

> inco.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inco/ | JSON https://fshy.ajam.dev/api/v1/entity/inco.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inco

- `inference/inco` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://platform.inco.ai/docs
- free tier: No free inference allowance is stated. GET /v1/models returns a public catalog without a key; with a key it lists the models the workspace may call, at per-million-token prices. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create a key on the API keys page for a workspace; no free inference allowance is stated
- interface: rest
- limits:
  - volume-quota (binding): per-million-token prices in the catalog; an empty balance returns 402 credit_balance_exhausted [1]
  - request-rate: per-minute rate limit and monthly workspace spend limit; a 429 carries Retry-After for the rate limit [1]
- endpoint: https://api.inco.ai/v1
- tooling: an OpenAI-compatible base URL with an sk-inco- key; OpenAI Chat Completions, Responses and Anthropic Messages are supported
- composes with: the workspace key and per-token prices bind; model discovery itself is public
- reliability: a stream cut at its one-hour limit is billed for the output sent; workspace spend limits reset on the 1st UTC; relayed models may be unavailable in some countries
- notes: no standing free inference allowance is published; model discovery is public but calls require a key and a funded workspace
- evidence:
  - [1] 2026-11-18: GET /v1/models returns a public catalog without a key; workspace model access and prices require a key | capture: sha256:0fa718d93be99b879651587a1a70afd416ff3d0cc60f4d9dd5864dd571dd27d0 | quote: Without a key it returns the public catalog; with your key, it lists the models your workspace may call, at its prices.
- sources:
  - [1] https://platform.inco.ai/docs
