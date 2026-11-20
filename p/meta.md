# Meta

> meta.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meta/ | JSON https://fshy.ajam.dev/api/v1/entity/meta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meta

- `inference/meta` | paid-only | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://dev.meta.ai/docs/pricing-rate-limits
- free tier: No free text allowance; Model API is pay-as-you-go per token (e.g. Muse Spark standard input USD 1.25 per 1M tokens), with Contributor mode at a discount in exchange for training rights. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key; no card or phone gate stated on the pricing page
- interface: rest
- limits:
  - request-rate (binding): 3,000 RPM and 4,000,000 TPM per team on standard models [1]
- endpoint: https://api.meta.ai/v1
- tooling: OpenAI SDK, Anthropic SDK or OpenAI-compatible clients
- composes with: no standing free text tier; Contributor mode trades content for lower price, not zero
- reliability: rate limits apply per team, not per API key; Contributor mode uses content to train future models
- notes: No text free tier on the Model API pricing page; Contributor mode is a discount, not a free allowance.
- evidence:
  - [1] 2026-11-18: Meta Model API bills per token with no free tier stated | capture: sha256:fe09c13eaf207805f3b0a79aec689df4f27f28f0a7cc8ba26ba3232a20be5683 | quote: Use our models with pay-as-you-go billing on Meta Model API
- sources:
  - [1] https://dev.meta.ai/docs/pricing-rate-limits
