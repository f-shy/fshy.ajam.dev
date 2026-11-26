# cheapaimodel

> cheapaimodel.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cheapaimodel/ | JSON https://fshy.ajam.dev/api/v1/entity/cheapaimodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cheapaimodel

- `inference/cheapaimodel` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://cheapaimodel.ai/docs
- free tier: No free allowance is stated. One API key covers the catalog, billed per token from a prepaid US-dollar balance, with per-key expiry, budget and allowlists. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an API key in the console and top up a dollar balance
- interface: rest
- limits:
  - volume-quota (binding): prepaid US-dollar balance, billed per token [1]
- endpoint: https://api.cheapaimodel.ai/v1
- tooling: an OpenAI-compatible base URL; the Anthropic Messages endpoint is listed as coming soon and no model serves it yet
- composes with: the prepaid balance is the scarce link; no free tier is published
- reliability: no model serves the Anthropic /v1/messages endpoint yet, so the Anthropic row does not work today
- notes: no standing free inference allowance is published; billing is prepaid per token
- evidence:
  - [1] 2026-11-18: one key covers the catalog, billed per token from a prepaid USD balance; no free allowance is stated | capture: sha256:51a09330b9d5173004087dd221aa182addb35b9515a1a3ed53d28a7c1e4393b5 | quote: One API key for every model in the catalog, billed per token from a prepaid US-dollar balance.
- sources:
  - [1] https://cheapaimodel.ai/docs
