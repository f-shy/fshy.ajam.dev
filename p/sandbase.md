# SandBase

> sandbase.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sandbase/ | JSON https://fshy.ajam.dev/api/v1/entity/sandbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SandBase

- `inference/sandbase` | paid-only | evidence documented | binding none | category inference gateway (model marketplace)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://www.sandbase.ai
- free tier: Served by / Pricing: models are listed with per-1M-token prices and percentage discounts; no free inference tier is stated. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is needed for an API key; no free signup credit is stated on the captured page
- interface: rest
- limits:
  - volume-quota: per-1M-token prices with discounts up to 45 percent, for example USD 0.165 input and USD 0.66 output on DeepSeek V4.1 Flash [1]
- endpoint: https://api.sandbase.ai/v1
- composes with: The /docs route returned HTTP 403; the first-party pricing page was used instead. No free allowance is published.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: SandBase lists per-1M-token prices with discounts and no free inference allowance | capture: sha256:462899ba67a9e28340869e2b0cbcd9e5750988409ce12c160eb917626f93580f | quote: | [deepseek/deepseek-v4.1-flash](https://www.sandbase.ai/models/deepseek/deepseek-v4.1-flash) | 45% OFF | DeepSeek | Language | $0.165in$0.66out/ 1M~~$0.30~~in~~$1.20~~out/ 1M |
- sources:
  - [1] https://www.sandbase.ai
