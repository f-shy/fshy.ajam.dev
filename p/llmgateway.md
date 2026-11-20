# LLM Gateway

> llmgateway.io | Coding subscriptions, Inference; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/llmgateway/ | JSON https://fshy.ajam.dev/api/v1/entity/llmgateway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DevPass (LLM Gateway)

- `coding-subs/llmgateway` | qualifies-with-caveat | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://llmgateway.io/pricing
- free tier: DevPass paid plans start at Lite USD 29/month (USD 58 included usage), Pro USD 79 and Max USD 179. LLM Gateway offers free models on the free tier without buying credits and BYOK is free; the 5% platform fee applies only when buying prepaid credits. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: an LLM Gateway account and a key; BYOK and free models need no card, while paid DevPass and credit top-ups are card-backed
- interface: rest, cli
- limits:
  - volume-quota (binding): DevPass Lite USD 29/month for USD 58 of monthly model usage [2]
  - request-rate: daily pacing caps each rolling 24h window at 8-10% of the monthly allowance [2]
- endpoint: https://api.llmgateway.io/v1
- tooling: OpenAI-compatible API; DevPass Code, Claude Code, OpenCode, Cursor and Cline, plus a self-hosted AGPLv3 gateway
- composes with: the free route is BYOK or the free model catalogue; the flat-price DevPass plan is the paid alternative and its daily pacing caps the allowance
- reliability: a 5% fee is added at credit purchase and 1.5% for international cards; refunds are limited to 14 days while under 10% used
- notes: Qualifies-with-caveat. The free route here is BYOK or the free model catalogue on the vendor gateway, not the flat-price DevPass subscription; no public read path was probed.
- evidence:
  - [1] 2026-11-18: free models are available on the free tier without buying credits | capture: sha256:d29b0de773495bd483000b936509a229c0208569b06820699af21f10d20e80f0 | quote: Free models are available on the free tier without buying credits.
  - [1] 2026-11-18: BYOK is free and the 5% fee applies only to credit purchases | capture: sha256:d29b0de773495bd483000b936509a229c0208569b06820699af21f10d20e80f0 | quote: Bringing your own provider keys is free, and self-hosting is free under AGPLv3.
  - [2] 2026-11-18: DevPass Lite is USD 29 per month with an included allowance and daily pacing | capture: sha256:e9f337f0543da38bc7705c067c7c874319b01f5a0bcaf1f7ec397941937b728d | quote: Price: $29/month
- sources:
  - [1] https://llmgateway.io/pricing
  - [2] https://devpass.llmgateway.io/pricing

## LLM Gateway (providers)

- `inference/llmgateway-providers` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:36:40.000Z (live) | stale on 2026-12-19
- url https://llmgateway.io/pricing
- disagrees on verdict: `inference/llm-gateway` says paid-only, `inference/llmgateway-providers` says qualifies-with-caveat
- free tier: Free models are available on the free tier without buying credits; free-model use requires a verified email and is rate limited to 5 requests per 10 minutes until credits are added, then 20 requests per minute. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a verified email is required for free-model use
- interface: rest
- limits:
  - request-rate (binding): 5 free-model requests per 10 minutes without credits; 20 per minute after any credit purchase [1]
- endpoint: https://api.llmgateway.io/v1
- composes with: the free-model request budget is the scarce link until credits are bought
- reliability: free-model limits are low until the account has bought credits, and the free list can change
- evidence:
  - [1] 2026-11-18: free models are available without buying credits on the free tier | capture: sha256:d29b0de773495bd483000b936509a229c0208569b06820699af21f10d20e80f0 | quote: Free models are available on the free tier without buying credits.
  - [2] 2026-11-18: free-model use needs a verified email and is limited to 5 requests per 10 minutes until credits are added | capture: sha256:d6a3405f110d9252019819232f991ddce913e50605e46cd09243873387bac6d5 | quote: Adding even a small amount of credits to your account (e.g., $10) will immediately upgrade your free model rate limits from 5 requests per 10 minutes to 20 requests per minute (free-model use still requires a verified email).
- sources:
  - [1] https://llmgateway.io/pricing
  - [2] https://docs.llmgateway.io/llms-full.txt

## LLM Gateway (inference/llm-gateway)

- `inference/llm-gateway` | paid-only | evidence documented | binding request-rate | category inference gateway, free-model mechanism with an empty catalogue
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.593Z (live) | stale on 2026-11-28
- url https://llmgateway.io/pricing
- disagrees on verdict: `inference/llm-gateway` says paid-only, `inference/llmgateway-providers` says qualifies-with-caveat
- free tier: free models (zero input and output price) carry their own limits: 5 requests per 10 minutes per free model for an organization with zero credits, 20 requests per minute per free model once any credits are purchased; the live model list shows 0 Free Models on the day read | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the pricing page still says free models are available on the free tier without buying credits; managed cloud is prepaid credits with a $10 minimum top-up and a 5% platform fee
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free models need a verified email address, and unverified accounts receive a 403; no card is named for the free models
- interface: rest
- limits:
  - request-rate (binding): per organization per free model: 5 requests per 10 minutes with zero credits; 20 requests per minute once any credit has been purchased; credits are not deducted for free models [1]
- binding note: 5 requests per 10 minutes per model is the ceiling if a free model is listed
- endpoint: https://api.llmgateway.io/v1/chat/completions
- tooling: any OpenAI-compatible client at https://api.llmgateway.io/v1
- composes with: paid gateway with a documented free-model lane; only worth a key if free models are listed again
- reliability: the free-model lane is documented but the model directory lists none, so a key may have nothing free to call
- notes: verdict is paid-only because the directory lists no free model; it moves up if free models reappear.
- evidence note: limits and the verified-email rule are quoted from the vendor's rate-limit page and the empty free list from the model directory; no call was made.
- evidence:
  - [1] 2026-10-28: zero-credit organizations get 5 requests per 10 minutes per free model | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: - 5 requests per 10 minutes per free model
  - [1] 2026-10-28: organizations that purchased credits get 20 requests per minute per free model | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: - 20 requests per minute per free model
  - [1] 2026-10-28: free models require a verified email address | capture: sha256:49002dfe5453397942d152d86dc23620640538511e1e5f6d1e3333beed6c3109 | quote: Using free models also requires a verified email address — unverified accounts receive a `403`.
  - [2] 2026-10-28: the pricing page states free models exist on the free tier | capture: sha256:bd8807b703e0aae0c309dff2d568b80a7702abd39047eb189c82abb6c353a202 | quote: - Free models are available on the free tier without buying credits.
  - [3] 2026-10-28: the model directory counts 0 free models | capture: sha256:7dcc87a8eec63431dcb883aaaf071f41bc7af64b3c65166704d01015e97a0b8d | quote: Tool-enabled 0 Free Models
- sources:
  - [1] https://docs.llmgateway.io/resources/rate-limits
  - [2] https://llmgateway.io/pricing
  - [3] https://llmgateway.io/models
