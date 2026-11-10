# Inception Labs

> inceptionlabs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inceptionlabs/ | JSON https://fshy.ajam.dev/api/v1/entity/inceptionlabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inception Labs (Mercury API)

- `inference/inception-labs` | trial-only | evidence documented | binding volume-quota | category inference endpoint, signup token grant
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://docs.inceptionlabs.ai/get-started
- free tier: 100 million free tokens assigned to each new account, no payment details required; free-tier limits are 1,000 API requests, 1,000,000 input tokens and 100,000 output tokens per minute | unit: tokens | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the quick-start page words the grant as 'initially assigned' to each new user and points to the billing page when the tokens run low; no monthly renewal is stated
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no payment details required, quoted from the quick-start page; the sign-up form itself was not captured, so any further check on it is not established
- interface: rest
- limits:
  - volume-quota (binding): 100 million free tokens per new account; billing information is requested when they run low [1]
  - request-rate: Free Tier per minute: 1,000 API requests, 1,000,000 input tokens, 100,000 output tokens (Pay As You Go: 3,000 requests, 3,000,000 input, 300,000 output) [2]
- binding note: the 100 million token grant runs out before the per-minute ceiling is a constraint
- endpoint: https://api.inceptionlabs.ai/v1/chat/completions
- tooling: any OpenAI-compatible client against https://api.inceptionlabs.ai/v1, or the vendor SDKs (pip install inceptionai, npm install inceptionai)
- composes with: a large one-off token grant with a high per-minute ceiling, suited to a burst of batch calls before any paid plan; the grant, not the rate, is the scarce link
- reliability: a one-off grant rather than a renewing allowance: once the 100 million tokens are spent the account needs billing information
- notes: the model on the quick-start page is mercury-3; the grant is worded as an initial assignment, so the verdict is trial-only until a renewal is shown.
- evidence note: the grant and the per-minute limits are quoted from the vendor's quick-start and rate-limit pages; no call was made. Renewal behaviour and the sign-up form are not established.
- evidence:
  - [1] 2026-10-28: each new account gets 100 million free tokens and no payment details are required | capture: sha256:0b3590a9eec6b9fba9dd71347e79a98f621a39b4693866d8811bb398ba9c137c | quote: Every new account includes 100 million free tokens — no payment details required.
  - [1] 2026-10-28: billing information is asked for only when the free tokens run low | capture: sha256:0b3590a9eec6b9fba9dd71347e79a98f621a39b4693866d8811bb398ba9c137c | quote: When your free tokens are running low, navigate to [Billing](https://platform.inceptionlabs.ai/dashboard/billing) to add your payment information for continued usage beyond the free tier.
  - [2] 2026-10-28: free tier allows 1,000 API requests per minute (3,000 on Pay As You Go) | capture: sha256:279e1aeb81a162e9a016b89107d6949a933e1e6517b60fb0f6e9cccdcf6d28d0 | quote: | API Requests | 1,000 | 3,000 | Custom |
  - [2] 2026-10-28: free tier allows 1,000,000 input tokens per minute | capture: sha256:279e1aeb81a162e9a016b89107d6949a933e1e6517b60fb0f6e9cccdcf6d28d0 | quote: | Input Tokens | 1,000,000 | 3,000,000 | Custom |
  - [2] 2026-10-28: free tier allows 100,000 output tokens per minute | capture: sha256:279e1aeb81a162e9a016b89107d6949a933e1e6517b60fb0f6e9cccdcf6d28d0 | quote: | Output Tokens | 100,000 | 300,000 | Custom |
  - probe:https://api.inceptionlabs.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:e3b553a615915ce48c40ea1fbe63b09d030a7555acdce22c11804e4827c04b75 | quote: "status": 401
- sources:
  - [1] https://docs.inceptionlabs.ai/get-started
  - [2] https://docs.inceptionlabs.ai/get-started/rate-limits
