# IteraCompute

> iteracompute.com | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iteracompute/ | JSON https://fshy.ajam.dev/api/v1/entity/iteracompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IteraCompute (Inference)

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

## IteraCompute (Compute)

- `compute/iteracompute` | paid-only | evidence documented | binding volume-quota | category hosted model inference with monthly token plans | tier Free promotion ended; paid 30-day token plans: Lite, Essential, Pro
- needs card no, phone no, ID no, institution no | verified 2026-11-24T10:11:14.843Z (live) | stale on 2026-12-25
- url https://iteracompute.com/pricing/
- free tier: unverified: the free Qwen3.8-27B promotion has ended and no current free allowance is published; retained monthly Auto allowances apply only where completed top-ups before the promotion ended remain positive after refunds | unit: none | metered on: none | read on: 2026-11-24 | source: [1]
- per-object cap: not applicable: the unit is model tokens, not stored objects; an Auto request allows up to 128,000 output tokens in a 1,000,000-token context window | source: [2]
- retention: unused Auto tokens from a plan period expire when the next period starts; inference inputs are retained only as necessary for the stated processing purposes | source: [3]
- egress: the API response is the payload; no separate egress allowance or traffic price is published on the pricing or docs pages | metered: no | source: [4]
- identity: email | detail: register and verify an email address or sign in with Google; the signup form asks for an email and a password of at least 12 characters and accepts the service agreement
- interface: rest, chat
- limits:
  - volume-quota (binding): Lite $10 per 30 days with 100M extra Auto tokens; Essential $20 per 30 days with 200M extra Auto tokens; Pro $50 per 30 days with 500M extra Auto tokens [3]
  - request-rate: 429 is returned for a monthly allowance limit or provider capacity; follow Retry-After and use exponential backoff [2]
  - retention-clamped: unused Auto tokens from the previous plan period expire when a new period starts [3]
- limits note: cash overage uses published per-model retail prices; plan and billing terms are finalised at checkout
- binding note: the paid plans are denominated in 30-day periods with a fixed Auto token allowance, which runs out before an undisclosed provider-capacity rate for sustained use
- interface detail: OpenAI-compatible Chat Completions and Responses at https://api.iteracompute.com/v1; the tier is gated on an API key
- endpoint: https://api.iteracompute.com/v1/chat/completions
- tooling: the OpenAI SDK or any HTTP client, pointed at https://api.iteracompute.com/v1 with a key minted in the console
- composes with: a key works across the listed models and coding agents through one OpenAI-compatible endpoint; unused Auto tokens expire at the period boundary, so jobs that need them should run within one 30-day period
- reliability: Auto selects a model from spare capacity using current demand and cost, so the serving model can change between requests; 429 with free_model_monthly_limit or provider_rate_limit is documented
- notes: The free Qwen3.8-27B allowance advertised by the earlier pricing page ended on 2026-11-24; the current pricing page lists only 30-day token plans, and a retained Auto allowance is conditional on pre-cutoff top-ups.
- evidence note: the price and allowance rows come from the vendor pricing page read 2026-11-24; the end of the free promotion and the signup fields come from the vendor's own pages the same day
- evidence:
  - [3] 2026-11-24: the Lite paid plan is USD 10 per 30 days | capture: sha256:b117bab997a42df6491d33e77fc00dae19c968f537c3dad8a06a3668ec9d88d2 | quote: $10/ 30 days
  - [3] 2026-11-24: Lite includes 100M extra Auto tokens; Essential and Pro include 200M and 500M | capture: sha256:b117bab997a42df6491d33e77fc00dae19c968f537c3dad8a06a3668ec9d88d2 | quote: AutoExtra 100M tokens
  - [3] 2026-11-24: unused Auto tokens expire at the period boundary and cash overage uses retail prices | capture: sha256:b117bab997a42df6491d33e77fc00dae19c968f537c3dad8a06a3668ec9d88d2 | quote: Any unused Auto tokens from the previous plan period expire.
  - [1] 2026-11-24: the free promotion has ended and the Qwen3.8-27B free model has been retired | capture: sha256:89392711812fc86f193f313218567604afff3a0cf35c1ccd2a4cc0ac01fd3f48 | quote: The Free promotion has ended
  - [1] 2026-11-24: retained Auto allowance depends on top-ups completed before the promotion ended | capture: sha256:89392711812fc86f193f313218567604afff3a0cf35c1ccd2a4cc0ac01fd3f48 | quote: You keep your tier’s monthly Auto allowance if the total of your top-ups completed before the Free promotion ended remains positive after refunds. Later top-ups cannot unlock or increase this allowance. Refunds may lower the retained tier. Qwen3.8-27B has been retired.
  - [5] 2026-11-24: signup asks for an email address and a password, and offers Google sign-in | capture: sha256:618aa33c2f4040871d6c6962f5c2118a81a38f78fc7eb31475bedf0a3901389a | quote: Email address
  - [2] 2026-11-24: registration requires a verified email or Google sign-in and no card | capture: sha256:f5ce383bfddaa4e539d57f0f4f7e1ed260f544754b89e22b5b057ac9835bdfba | quote: Register and verify your email, or sign in with Google.
  - [2] 2026-11-24: Auto selects a serving model from spare capacity, so answers are not pinned to one model | capture: sha256:f5ce383bfddaa4e539d57f0f4f7e1ed260f544754b89e22b5b057ac9835bdfba | quote: Auto matches each request with spare capacity across our listed models, using current demand and cost to select a model.
  - [2] 2026-11-24: 429 carries a free_model_monthly_limit code for an exhausted allowance and a provider_rate_limit code for capacity | capture: sha256:f5ce383bfddaa4e539d57f0f4f7e1ed260f544754b89e22b5b057ac9835bdfba | quote: Check your available Auto allowance in Billing. Wallet charges require you to enable pay-as-you-go.
- sources:
  - [1] https://iteracompute.com/free/
  - [2] https://platform.iteracompute.com/docs.html
  - [3] https://iteracompute.com/pricing/
  - [4] https://iteracompute.com/docs.html
  - [5] https://platform.iteracompute.com/sign-up
