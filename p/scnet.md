# SCNet Token Plan

> scnet.cn | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scnet/ | JSON https://fshy.ajam.dev/api/v1/entity/scnet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SCNet Token Plan

- `coding-subs/scnet-token-plan` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://www.scnet.cn/ac/openapi/doc/2.0/moduleapi/plans/token-plan.html
- free tier: No free tier. Four prepaid monthly plans: Basic CNY 30 (list CNY 50) for 60,000 credits, Standard CNY 110 (list CNY 185) for 240,000 credits, Advanced CNY 265 (list CNY 440) for 600,000 credits, and Flagship CNY 764 (list CNY 1,274) for 1,800,000 credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: one Token Plan per account and one API key per plan; the page does not name a card gate
- interface: rest
- limits:
  - volume-quota (binding): 60,000 to 1,800,000 credits a month depending on the plan [1]
  - volume-quota (binding): one Token Plan per account and one API key per subscription [1]
- endpoint: https://api.scnet.cn/api/llm/v1
- tooling: one sk-tp- API key against the vendor's OpenAI-compatible endpoint
- composes with: one key and one plan per account is the scarce link once the monthly credits run out
- reliability: credits are monthly and the account cannot hold two plans, so there is no way to bridge a month boundary
- evidence:
  - [1] 2026-11-18: four prepaid plans run from CNY 30 for 60,000 credits to CNY 764 for 1,800,000 credits, with one plan and one key per account | capture: sha256:529c04e35f5f34402b6027ff0da7824ce1d400f2fd5533321f3a9e05c1d1a57b | quote: | 旗舰版 | ~~¥1274~~ | ¥764 | 1,800,000 Credits | 极致额度加持，深度 AI 开发首选。含 OpenClaw 2核4G 实例免费使用。 |
  - [1] 2026-11-18: the Basic prepaid plan is CNY 30 per month for 60,000 credits | capture: sha256:529c04e35f5f34402b6027ff0da7824ce1d400f2fd5533321f3a9e05c1d1a57b | quote: | 基础版 | ~~¥50~~ | ¥30 | 60,000 Credits |
  - [1] 2026-11-18: the account may hold only one Token Plan and one API key | capture: sha256:529c04e35f5f34402b6027ff0da7824ce1d400f2fd5533321f3a9e05c1d1a57b | quote: 每个账号最多可同时持有 1 个 Token Plan
- sources:
  - [1] https://www.scnet.cn/ac/openapi/doc/2.0/moduleapi/plans/token-plan.html
