# Hyperbolic Serverless

> hyperbolic.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyperbolic/ | JSON https://fshy.ajam.dev/api/v1/entity/hyperbolic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hyperbolic

- `compute/hyperbolic` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:28.017Z (live) | stale on 2026-12-04
- url https://www.hyperbolic.ai/marketplace
- free tier: no free tier: on-demand GPU rental at starting-from rates per GPU-hour of $3.19 for an H100 SXM, $3.99 for an H200 and $5.99 for a B200, refreshed weekly from supplier rates; the page lists none of A100 80 GB, L40S, RTX 4090 or L4, states no billing granularity and no minimum bill, and states no minimum term for on-demand; failed instances are not charged; payment by credit card or Stripe | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up page text offers 'Sign Up with Email' and the marketplace page says 'Payment works by credit card or Stripe'; the form fields are not in the stored page and whether a card is required before the first rental is not stated
- interface: unknown
- limits:
  - request-rate (binding): $3.19 a GPU-hour for an H100 SXM; $3.99 for an H200 and $5.99 for a B200 [1]
  - retention-clamped: the rates refresh weekly, so a price quoted today is not a price next week [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the marketplace page was read on 2026-10-22 and states the per-GPU rates and that they refresh weekly. The record's free-tier claim is contradicted, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: H100 SXM
  - shape.gpu_count: 1
  - shape.note: H100 SXM, H200 and B200 are the named on-demand classes
  - session_cap.restart_required: no
  - session_cap.note: on-demand GPUs with no commitment; the page states no reap
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Rent GPUs starting at $3.19/GPU/hr' and 'GPU rentals on Hyperbolic start at $3.19/hr for an NVIDIA H100 SXM. H200s are $3.99/hr and B200s are $5.99/hr, with pricing refreshed weekly', quoted
  - [1] 2026-11-03: the starting-from price table lists H100 SXM at $3.19 per GPU hour, with H200 and B200 and no other card | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: | Nvidia H100 SXM | $3.19 / HR |
  - [1] 2026-11-03: the marketplace page was read on this date | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: | Nvidia H100 SXM | $3.19 / HR |
  - [2] 2026-11-03: the sign-up page offers an email sign-up | capture: sha256:dc4e289ee01aa68264c872fa7a7410f22b2dc27132fad3a859905726f7dfbe93 | quote: or Sign Up with Email
  - [1] 2026-11-03: on-demand has no minimum term; the page states no billing granularity or minimum bill | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: No. On-demand GPU instances do not require a minimum term or contract.
  - [1] 2026-11-03: failed instances are not charged and payment is by credit card or Stripe | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: You pay only for what you use, with no charges for failed instances. Payment works by credit card or Stripe.
  - [1] 2026-11-03: the listed rates are starting-from rates refreshed weekly | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: Note: Pricing is refreshed weekly based on the best available rates from suppliers on our platform.
  - [1] 2026-11-03: the marketplace page still lists H100 SXM at $3.19 per GPU hour | capture: sha256:9633bb5c222ec6ee82686a9b879ea1e4fa88a5844ee8f0dc5279a6417f89669d | quote: | Nvidia H100 SXM | $3.19 / HR |
- sources:
  - [1] https://www.hyperbolic.ai/marketplace
  - [2] https://app.hyperbolic.ai/signup

## Hyperbolic Serverless Inference

- `inference/hyperbolic-inference` | paid-only | evidence documented | binding volume-quota | category inference endpoint, pay-per-token, one-time deposit
- needs card yes, phone no, ID no, institution no | verified 2026-10-28T04:36:19.314Z (live) | stale on 2026-11-28
- url https://hyperbolic.ai/docs/inference/overview
- free tier: None for inference: 'You may not launch GPU instances nor storage volumes, or use Inference, with a free-tier account.' A personal account becomes Pro with a one-time deposit of USD 5 or more, and requests made with an Organization API key do not require Pro. | unit: none | metered on: unstated | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: signup verifies an email address, and inference needs a one-time deposit of at least USD 5 made through a payment form before any call; the payment methods that form accepts are not listed on the pages read
- interface: rest
- limits:
  - request-rate: 300 requests per minute per API key; above that the API returns HTTP 429 [2]
  - volume-quota (binding): a one-time deposit of USD 5 or more upgrades a personal account to Pro, and the credit balance must stay above zero (HTTP 402 when it does not) [1]
- binding note: inference is refused outright on the Free Tier (HTTP 403 inference_requires_pro), so the first constraint is the USD 5 deposit, not a rate
- endpoint: https://api.hyperbolic.ai/inference/v1/chat/completions
- tooling: OpenAI SDKs with base URL https://api.hyperbolic.ai/inference/v1 and an sk_live_ key; text models only
- composes with: pay-per-token text models behind an OpenAI-compatible base URL; the USD 5 deposit is a one-off, with no subscription
- reliability: no reliability event recorded
- notes: GPU rental by the same vendor is a separate offer (compute/hyperbolic). The previous inference API at api.hyperbolic.xyz included the Free Tier and is decommissioned, returning 404; the current API needs a Pro plan or an Organization.
- evidence note: documentation pages only; the 300 requests per minute ceiling is a documented figure and not measured
- evidence:
  - [1] 2026-10-28: the Free Tier cannot use inference | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: You may not launch GPU instances nor storage volumes, or use [Inference](/docs/inference/overview), with a free-tier account.
  - [1] 2026-10-28: inference needs a Pro plan (a one-time deposit of USD 5 or more) or an Organization | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: A Pro plan, or an Organization. Personal accounts on the Free Tier can't use inference. To upgrade, make a one-time deposit of \$5 or more.
  - [1] 2026-10-28: signup verifies an email address | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: [Sign up for Hyperbolic](https://app.hyperbolic.ai), then verify your email address.
  - [1] 2026-10-28: the upgrade is a payment form for USD 5 | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: an Upgrade to Pro dialog opens with your message, a Free vs Pro comparison, and a $5 payment form
  - [1] 2026-10-28: the previous inference API at api.hyperbolic.xyz is decommissioned and returns 404 | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: Requests to `https://api.hyperbolic.xyz/v1` now return `404` with a message that the endpoint was decommissioned.
  - [1] 2026-10-28: the previous inference API included the Free Tier and the current one needs a Pro plan or an Organization | capture: sha256:acb9a3f3dd161105c0dba7ee4917dedc591a4e8daa3604bac190e96c9e4c035b | quote: | Plan | Free Tier included | Pro plan or Organization |
  - [2] 2026-10-28: the inference API returns 429 above 300 requests per minute per key | capture: sha256:2056357592f6af6d267e779714b9cfd36f39bd974078163644a57f45c00e396d | quote: | `429` | The API key sent more than 300 requests in a minute | Retry with exponential backoff. For a higher limit, [contact sales](mailto:sales@hyperbolic.ai) |
  - [2] 2026-10-28: a Free Tier personal account gets 403 inference_requires_pro | capture: sha256:2056357592f6af6d267e779714b9cfd36f39bd974078163644a57f45c00e396d | quote: | `403` | `inference_requires_pro` | The personal account is on the Free Tier | Upgrade with a one-time \$5 deposit under Settings > Plan, or use an Organization API key |
- sources:
  - [1] https://www.hyperbolic.ai/docs/llms-full.txt
  - [2] https://www.hyperbolic.ai/docs/inference/performance-limits
