# SenseNova

> sensenova.cn | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sensenova/ | JSON https://fshy.ajam.dev/api/v1/entity/sensenova.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SenseNova (China)

- `inference/sensenova` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.sensenova.cn/docs
- free tier: Public beta free credits: a general pool with a rolling 5-hour cap of 120,000 credits and a rolling weekly cap of 1,200,000 credits; a separate Flash-Lite pool has 60,000 per 5 hours and 600,000 per week. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: quickstart requires account registration and phone-number verification | country: CN
- interface: rest
- limits:
  - volume-quota (binding): general pool 120,000 credits / 5h and 1,200,000 / week (public beta) [1]
  - volume-quota (binding): Flash-Lite pool 60,000 / 5h and 600,000 / week [1]
- endpoint: https://token.sensenova.cn/v1
- tooling: OpenAI SDK, Anthropic Messages or OpenAI Responses against token.sensenova.cn/v1
- composes with: the rolling 5-hour and weekly credit windows bound sustained use; credit burn per model varies
- reliability: credit windows reset on a rolling basis; a 429 error signals quota or rate exhaustion; beta rules may change
- notes: Public-beta free credits are documented with rolling windows; no public read path was probed. Registration requires a phone number, which is an any-phone gate rather than a pure email gate.
- evidence:
  - [1] 2026-11-18: general credit pool cap rose to 120,000 per 5 hours and 1,200,000 per week | capture: sha256:926508b2014457f07f5d8cafcabe5428426da84daabf2326f6215fed4ab96c31 | quote: 滚动 5 小时窗口的上限将由 60,000 积分提升至 120,000 积分；
- sources:
  - [1] https://platform.sensenova.cn/docs
