# EBCloud

> ebcloud.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ebcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ebcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EBCloud

- `inference/ebcloud` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://www.ebcloud.com
- free tier: A CNY 20 no-threshold voucher is given for signup and verification. The large-model API is billed per token (for example DeepSeek-V4.1-Flash-1017 at CNY 2 per million input tokens), and compute points must be bought before using the model API. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: signup and verification are required for the voucher; the model API requires console registration and a prepaid compute-point purchase
- interface: rest
- limits:
  - volume-quota (binding): CNY 20 no-threshold signup voucher; model API billed per token after buying compute points [1]
- endpoint: https://maas-api.ebcloud.com/v1
- tooling: OpenAI API format for the large-model service, with an API key created in the console
- composes with: the CNY 20 signup voucher and the prepaid compute-point purchase bind before the per-token price
- reliability: compute points can only be bought with the cash balance of the ebcloud account, so a cash recharge precedes model API use
- notes: the only free allowance found is a CNY 20 signup verification voucher, not a standing free inference tier; the model API itself is prepaid
- evidence:
  - [1] 2026-11-18: signup and verification give a CNY 20 no-threshold voucher; the large-model API is billed per token and compute points must be bought before use | capture: sha256:3d5db7a92712527e088f4cebf73bb33433281a536a2ea75bfc1c6b1b9d9b9c3d | quote: 免费试用注册认证送20元无门槛代金券
- sources:
  - [1] https://www.ebcloud.com
