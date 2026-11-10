# Leonardo.Ai

> leonardo.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leonardo/ | JSON https://fshy.ajam.dev/api/v1/entity/leonardo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leonardo.Ai (Compute)

- `compute/leonardo-ai` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://leonardo.ai/pricing
- free tier: Free plan at USD 0 a month with 'Fast Tokens 150 / day', 'Model Access Auto Only', 'Creations access Public', 'Quality settings Basic', 'Personal collections 1'. The allowance is daily and does not accumulate: 150 tokens a day is at most 4,500 in a 30-day month, and only for an account that spends the balance every day. | unit: tokens | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-daily-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): the daily reset is the whole budget: 150 tokens expire each day, so a 5,000-image job cannot be accumulated and takes 34 days at one image a token, and the free plan is locked to 'Auto Only' model selection so the cheapest token cost is not always available. [1]
- limits note: the daily reset is the whole budget: 150 tokens expire each day, so a 5,000-image job cannot be accumulated and takes 34 days at one image a token, and the free plan is locked to 'Auto Only' model selection so the cheapest token cost is not always available.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 150 images a day, generated into a public gallery, is a slow synthetic-image feed for a training set; pair it with a free object store and a free runner to pull the outputs, since the free plan gives no bulk download. What breaks: the 'Auto Only' model lock and the 'Basic' quality setting, which means the images are not the model version a paid plan would give, and any dataset that needs a specific checkpoint cannot be built here at all.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The vendor page proves 150 tokens a day; what a token buys comes from the vendor's help centre rather than the pricing page: one token per standard 768x768 image, 2 for background removal, 5 for an upscale, 40 for a Nano Banana image (reported via a Portuguese-language review read 2026-10-22, dated 2026-09-20, which cites the vendor Token Usage table). So the honest range is 3 images a day on the most expensive model to 150 a day at one token. Not established: whether signup demands a card; the pricing page does not say.
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: recurring-daily-allowance
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the FREE plan column prints '$0/month', 'Fast Tokens 150 / day', 'Model Access Auto Only', 'Creations access Public', 'Quality settings Basic', quoted
  - [1] 2026-10-22: the comparison table prints 'Fast Tokens | 150 / daily' for FREE against '8,500 / monthly' for Essential, confirming the daily rather than monthly unit, quoted
- sources:
  - [1] https://leonardo.ai/pricing

## Leonardo.Ai (Inference)

- `inference/leonardo-ai` | paid-only | evidence documented | binding write-gated | category image and video generation API, purchased credit only
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://leonardo.ai/api
- free tier: none for the API: API access is separate from free or web app subscriptions and needs purchased API credits before a key can be created. The Free web-app plan gives 150 Fast Tokens a day, which reset daily, and does not include API calls. API credit is pay as you go, does not expire, and allows up to 10 concurrent generations. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: third-party pages report a USD 5 starter credit on a new API account; no vendor page read states it, so it is unverified
- per-object cap: not applicable
- retention: images generated through the API do not expire and stay accessible from the web app
- egress: metered: no
- identity: card | detail: a free Leonardo account (email signup form not read), then a purchase of API credit ('Buy Credit') before 'Create New Key'; unverified: which payment methods are accepted and the minimum purchase
- interface: rest
- limits:
  - write-gated (binding): API access is separate from free or web app subscriptions: purchased API credits are needed before any key is created [1]
  - volume-quota: Free web-app plan: 150 Fast Tokens a day, reset daily, no accumulation; not usable through the API [2]
- binding note: an API key needs purchased credit, so the 150 daily Fast Tokens of the Free web plan never reach the API
- interface detail: REST at https://cloud.leonardo.ai/api/rest/v1 with a bearer API key; optional webhook callback set when the key is created
- endpoint: https://cloud.leonardo.ai/api/rest/v1/generations
- tooling: raw HTTP with an API key created on the API Access page of the web app; the web app can export a generation as ready-to-use API code
- composes with: the Free web-app plan is a daily allowance for the browser, usable for hand-made images, and the API is a separate paid lane; a batch pipeline needs bought API credit first. A free image allowance with an API is not available here.
- reliability: web-app tokens and API credit are separate balances billed separately
- evidence note: the separation of the API from the Free plan, the credit purchase before a key, the 10 concurrent generations and the 150 daily Fast Tokens are quoted from vendor pages; a starter credit on a new API account is unverified.
- evidence:
  - [1] 2026-11-03: API access needs purchased credits and is separate from free subscriptions | capture: sha256:22cc37585f53d1e11f6626d85a5b8965c1f77a80e093e3f7ecd54336e2f89a25 | quote: Purchase API Credits. API access is separate from free or web app subscriptions.
  - [1] 2026-11-03: API plans are distinct from the web app plans | capture: sha256:22cc37585f53d1e11f6626d85a5b8965c1f77a80e093e3f7ecd54336e2f89a25 | quote: Note: API plans are distinct from the Leonardo web app plans. API plans unlock access to the API.
  - [3] 2026-11-03: an API account starts from a free Leonardo account and a credit purchase | capture: sha256:cdecd7a9e3010b4137410844d0a61a7f1726a0021457fc8000dd9379e44c97bd | quote: You’ll need a free Leonardo account to get started.
  - [3] 2026-11-03: the pay-as-you-go API allows up to 10 concurrent generations | capture: sha256:cdecd7a9e3010b4137410844d0a61a7f1726a0021457fc8000dd9379e44c97bd | quote: Up to 10 concurrent generations
  - [3] 2026-11-03: API credit does not expire | capture: sha256:cdecd7a9e3010b4137410844d0a61a7f1726a0021457fc8000dd9379e44c97bd | quote: API credit doesn’t expire
  - [2] 2026-11-03: the Free web plan gets 150 Fast Tokens a day | capture: sha256:cf340ff3d09b5a0e8d93cf5e30ca38034a64987ade7b64f8f2c91ee916810cd0 | quote: | Fast Tokens | 150 / daily | 8,500 / monthly | 25,000 / monthly | 60,000 / monthly |
  - [2] 2026-11-03: free-user tokens reset daily | capture: sha256:cf340ff3d09b5a0e8d93cf5e30ca38034a64987ade7b64f8f2c91ee916810cd0 | quote: If you’re a free user, you’re allocated a certain number of tokens each day, and these reset daily, allowing you to perform actions within this limit.
  - [4] 2026-11-03: API-generated images do not expire | capture: sha256:39743124f39906e86cf9c0417952305cf882a2120d3f7a7134e84a9b5cd334ad | quote: No, images generated via the Leonardo.Ai API will not expire and can also be accessed from the Web App at any time.
- sources:
  - [1] https://docs.leonardo.ai/docs/getting-started
  - [2] https://leonardo.ai/pricing
  - [3] https://leonardo.ai/api
  - [4] https://docs.leonardo.ai/docs/faq
