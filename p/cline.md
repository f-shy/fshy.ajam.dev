# Cline

> cline.bot | Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cline/ | JSON https://fshy.ajam.dev/api/v1/entity/cline.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ClinePass

- `coding-subs/cline-pass` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.cline.bot/getting-started/clinepass
- free tier: No free tier. ClinePass is a flat USD 9.99/month subscription giving 2-5x the API rate limits of standard access; it is optional and a separate provider from Cline usage-billing. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a Cline account dashboard subscription; the page shows a Subscribe link and a card-backed monthly plan but does not enumerate signup fields
- interface: rest, cli
- limits:
  - request-rate: rolling 5-hour usage window [1]
  - volume-quota (binding): calendar-week and calendar-month usage windows [1]
- endpoint: https://api.cline.bot/api/v1
- tooling: Cline IDE extension, Cline CLI, and any OpenAI-compatible client sending an X-Response-Format: openai header
- composes with: one flat-rate key shared across all ClinePass models; usage is metered by a rolling 5-hour, weekly and monthly cap
- reliability: model deprecations are performed for capacity reasons (GLM-5.2, Kimi K2.6, K2.7 Code and DeepSeek V4 Flash were removed)
- evidence:
  - [1] 2026-11-18: ClinePass is a paid monthly subscription at USD 9.99 with no free tier | capture: sha256:0de64b4190d2ce296ff7c5d92635e76a5d7d8353de9ea1bdf01a363f86f1ab78 | quote: \$9.99/month
  - [1] 2026-11-18: usage is bound by a 5-hour rolling window plus weekly and monthly limits | capture: sha256:0de64b4190d2ce296ff7c5d92635e76a5d7d8353de9ea1bdf01a363f86f1ab78 | quote: ClinePass measures usage against three limits:
  - [1] 2026-11-18: ClinePass is optional and separate from Cline usage-billing | capture: sha256:0de64b4190d2ce296ff7c5d92635e76a5d7d8353de9ea1bdf01a363f86f1ab78 | quote: It's completely optional. You don't need ClinePass to use Cline
- sources:
  - [1] https://docs.cline.bot/getting-started/clinepass

## Cline

- `coding-subs/cline` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category BYOK coding agent
- needs card no, phone no, ID no, institution no | verified 2026-11-03T17:29:12.673Z (live) | stale on 2026-12-04
- url https://cline.bot/pricing
- free tier: free for individual developers; bring your own API key or use managed infrastructure | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: the product costs nothing; the inference it calls is the bill
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: a GitHub account for the extension marketplace
- interface: cli
- limits note: no vendor-imposed usage cap, because the vendor does not serve the inference no vendor quota binds: the vendor does not serve the usage this record prices
- interface detail: a VS Code extension; any OpenAI-compatible or Anthropic-compatible endpoint
- tooling: VS Code extension; accepts an arbitrary base URL and key
- reliability: no reliability event recorded
- notes: Its cost is entirely the upstream endpoint.
- evidence note: the price model is quoted from the vendor page. Nothing about capacity can be measured here because capacity belongs to the endpoint chosen.
- self hosted: yes
- evidence:
  - [1] 2026-10-22: individual use is free, and the product is described as BYO API key or managed infrastructure, with an Enterprise tier for organisations
  - [1] 2026-10-30: the product stays free for individual developers; inference is billed on usage or brought as an own key | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: Cline is free for individual developers.
  - [1] 2026-11-03: the individual plan is still free; there is no vendor quota | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: Cline is free for individual developers.
  - [1] 2026-11-03: the Free card lists model inference at cost or with the user's own key, so the inference is the cost and no vendor quota binds | capture: sha256:75a7ec46968077117635d0859cfed55fe422145d6eba50a32382aa066008aa60 | quote: - Purchase and Model Inference at Cost or BYOK
- sources:
  - [1] https://cline.bot/pricing
