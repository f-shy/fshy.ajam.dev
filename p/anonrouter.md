# AnonRouter

> anonrouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anonrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/anonrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AnonRouter

- `inference/anonrouter` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, privacy-routed
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.anonrouter.ai/free-models
- free tier: Free models cost $0 including inference fees (anonrouter/free or an exact :free ID); the standard account allowance is 20 requests per minute, 100,000 reserved tokens per minute and 2 concurrent free requests. | unit: tokens | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free models require a verified, non-disposable email (or a credited purchase) and an account opt-in to Anonymous routes
- interface: rest
- limits:
  - request-rate (binding): 20 requests per minute, 100,000 reserved tokens per minute, 2 concurrent free requests per account [1]
- endpoint: https://api.anonrouter.ai/v1
- tooling: an OpenAI-compatible inference key with free models enabled on the account
- composes with: the verified-email eligibility gate and the shared per-account free allowance are the scarce links
- reliability: free capacity is shared and can return 429 before the stated allowance; no paid fallback
- evidence:
  - [1] 2026-11-18: free models cost $0 with a stated per-account free allowance | capture: sha256:c5e3036c850061420861040c75902e10f7a86a0623d64c9e37e754b9a5681972 | quote: The standard account allowance is 20 requests per minute, 100,000 reserved tokens per minute, and 2 concurrent free requests, shared across its keys and free models.
- sources:
  - [1] https://docs.anonrouter.ai/free-models
