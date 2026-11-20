# IteraCompute

> iteracompute.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iteracompute/ | JSON https://fshy.ajam.dev/api/v1/entity/iteracompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IteraCompute

- `inference/iteracompute` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API, free Qwen3.8-27B monthly token allowance, promotion ends 2026-11-24
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://iteracompute.com/pricing
- free tier: free Qwen3.8-27B: 30M tokens a month, 128K context, 160,000 tokens per minute, no credit card; the promotion ends at 00:00 Pacific Time on November 24, 2026 | unit: tokens | metered on: unstated | read on: 2026-11-04 | source: [1] | note: input and output tokens count, reasoning included, across all keys; no daily quota; allowance resets on the first of each month at 00:00 UTC; output capped at 8,192 tokens; exhausted quota returns 429
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: register and verify an email, or sign in with Google; no card or recharge is required
- interface: rest
- limits:
  - volume-quota (binding): 30M tokens a month on the Free tier [1]
  - request-rate: 160,000 tokens per minute on the Free tier; free requests may queue on shared spare GPU capacity [1]
- binding note: 30M tokens a month binds before the 160,000 tokens per minute rate for sustained use
- endpoint: https://api.iteracompute.com/v1/chat/completions
- tooling: OpenAI-compatible Chat Completions and Responses at https://api.iteracompute.com/v1
- composes with: a cumulative net recharge of $10 gives Starter: 100M tokens a month, 300K TPM, 128K context; $50 gives Pro: 300M tokens a month, 600K TPM, 256K context
- reliability: free Qwen runs on shared spare GPU capacity with queues, slow responses and temporary unavailability possible, and no SLA
- notes: the free model is a promotion that ends 2026-11-24; later access for unrecharged users is not guaranteed
- evidence:
  - [1] 2026-11-04: the Free tier allows 30M tokens a month, 128K context and 160,000 TPM | capture: sha256:320ee39e869818b82e3a800a59c1e7145123f286692e187df4857941d79475a0 | quote: | Free | No recharge required | 30M | 128K | 160,000 |
  - [1] 2026-11-04: the free promotion has an end date | capture: sha256:320ee39e869818b82e3a800a59c1e7145123f286692e187df4857941d79475a0 | quote: The free Qwen3.8-27B promotion ends at 00:00 Pacific Time on November 24, 2026.
  - [1] 2026-11-04: an exhausted quota returns 429 | capture: sha256:320ee39e869818b82e3a800a59c1e7145123f286692e187df4857941d79475a0 | quote: No automatic paid overage: exhausted monthly quota returns 429; wait for reset or unlock a higher tier.
  - [2] 2026-11-04: sign-up needs an email or Google and no card | capture: sha256:dfa6e14b337496317ff77b88d0f3180e202809adea8eec9938818cacc933ee25 | quote: 1. Register and verify your email, or sign in with Google. No card or recharge is required.
  - [2] 2026-11-04: the free model runs on shared spare capacity | capture: sha256:dfa6e14b337496317ff77b88d0f3180e202809adea8eec9938818cacc933ee25 | quote: Free Qwen runs on shared spare GPU capacity.
  - probe:https://api.iteracompute.com/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:ab991ec96f842e8623f3d638a7b9a0166a13a5826e2b681af3e539377676b546 | quote: "status": 401
- sources:
  - [1] https://iteracompute.com/pricing
  - [2] https://iteracompute.com/docs.html
