# Venice AI

> venice.ai | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/venice/ | JSON https://fshy.ajam.dev/api/v1/entity/venice.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Venice AI (Inference)

- `inference/venice` | qualifies-with-caveat | evidence documented | binding request-rate | category private inference, free app tier and paid/staked API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://venice.ai/pricing
- free tier: a Free app tier with 10 text prompts/day and 15 image prompts/day on base models, private and uncensored, with API access paid by credits; the API also offers a DIEM/VVV staking allowance with no per-call charge and an x402 USDC-on-Base route with no account or API key | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a free Venice account is created at venice.ai/sign-up for the app tier; the API accepts credits, staking, or a USDC wallet with no account over x402
- interface: rest
- limits:
  - request-rate (binding): Free app tier: 10 text prompts/day and 15 image prompts/day on base models [1]
  - write-gated: the API is paid with credits, a DIEM/VVV staking allowance, or USDC per request over x402 [2]
- binding note: the free app allowance is 10 text prompts/day and is web-only; no free programmatic quota is stated
- tooling: an OpenAI-compatible API key, plus an x402 USDC-on-Base path that needs no account or API key
- composes with: pairs with an OpenAI-compatible agent; the free app prompts are web-only, while programmatic access needs credits, a staking allowance, or per-request USDC
- reliability: no reliability event recorded
- notes: the free tier is 10 text prompts/day in the web app; API access is paid, staked, or paid per request in crypto, so no free programmatic allowance is documented.
- evidence:
  - [1] 2026-11-18: the Free tier gives 10 text prompts per day with API access paid by credits | capture: sha256:b59385b37f59f7ac59204e74c8986fad51e304391d8be7f524194ba836c6526e | quote: ✓10 text prompts per day
  - [2] 2026-11-18: API payment routes include credits, DIEM staking and account-free USDC over x402 | capture: sha256:68651c4aa75aae4738bc7e685a08b9f90992ea875fc06b4173491f1d443f9258 | quote: Top up with credits, stake DIEM for a daily allowance, or skip the account entirely with USDC on Base.
- sources:
  - [1] https://venice.ai/pricing
  - [2] https://docs.venice.ai

## Venice AI (Compute)

- `compute/venice-ai` | paid-only | evidence documented | binding volume-quota | category inference API
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:48.361Z (live) | stale on 2026-12-26
- url https://docs.venice.ai/overview/pricing
- free tier: API requests are pay per use at the rates on this page. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: an account for the Free plan ('Sign Up for Free', 10 text prompts and 15 image prompts a day) and credits for API calls: the docs state 'API requests are pay-per-use at the rates on this page. There is no unmetered API tier. A Free account can call the API, and those requests are billed at the same rates', and the plan grid marks API access 'pay with credits'. No evidence row states that a card is required to buy those credits, and no hold, debit or prepaid term is stated, so the card kind is inferred from the credit purchase rather than quoted. The record's notes add that the pay-per-request-in-USDC lane needs no account at all.
- interface: rest
- limits:
  - volume-quota (binding): every call is metered at list rate with no allowance: the balance is the only limit, and the free consumer tier grants no API credit at all. [1]
- limits note: every call is metered at list rate with no allowance: the balance is the only limit, and the free consumer tier grants no API credit at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the USD 5 subscriber credit is the only balance and it arrives with a paid plan; it converts to a few million tokens at the cheapest listed model and sits as balance rather than expiring on a clock.
- reliability: no reliability event recorded
- notes: Venice is widely listed as a free API because the consumer product has a free tier and because the token stake lane reads like an allowance. The docs contradict both readings: staking DIEM or VVV requires buying the token first ('Each Diem = $1/day of credits that refresh daily'), and a free account pays per call. The pay-per-request-in-USDC lane needs no account at all, which is the one route here that touches no identity. Recorded paid-only for the API; the consumer free tier is real and is not an API allowance. The one recorded is the better-evidenced.
- extras:
  - facets.class: paid-inference
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'API requests are pay-per-use at the rates on this page. There is no unmetered API tier. A Free account can call the API, and those requests are billed at the same rates'; 'Pro, Plus, and Max subscribers receive a one-time $5 USD credit on the API balance'; 'Free accounts do not receive this allowance'; 'A paid subscription does not include free or unlimited API usage', quoted
  - [2] 2026-10-22: the consumer plan grid carries a 'Free' column: 'Explore Venice with base AI models' with 'Sign Up for Free', quoted
  - [2] 2026-10-22: Free plan lists 10 text prompts per day and 15 image prompts per day; API access marked 'pay with credits'
  - [3] 2026-10-22: '1 DIEM = $1 every day'; each staked DIEM yields USD 1 of daily renewing credit
  - [4] 2026-10-22: DIEM/USDC on Aerodrome (Base) at USD 1,871.59, liquidity USD 203,620, 24h volume USD 404,491
  - [1] 2026-11-25: the API is pay per use at the rates published on the page | capture: sha256:30961b475074223ae0ef4a74f2ad1b7553451fbff0ee33dc671e869863ae4d85 | quote: API requests are pay per use at the rates on this page.
- sources:
  - [1] https://docs.venice.ai/overview/pricing
  - [2] https://venice.ai/pricing
  - [3] https://venice.ai/lp/diem
  - [4] https://api.dexscreener.com/latest/dex/tokens/0xf4d97f2da56e8c3098f3a8d538db630a2606a024
