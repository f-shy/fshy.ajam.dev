# xxapi

> xxapi.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xxapi/ | JSON https://fshy.ajam.dev/api/v1/entity/xxapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xxapi

- `inference/xxapi` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://docs.xxapi.ai/
- free tier: A prepaid balance is required before a key can call models: the guide says to confirm the account has a balance and that calls cannot be made without one; no free allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the account must be recharged before a key can be used; no free tier stated
- interface: rest
- limits:
  - volume-quota (binding): prepaid balance must be funded before a key can call; no free tier [1]
- endpoint: https://xxapi.ai/v1
- composes with: the prepaid balance is the scarce link
- reliability: calls cannot be made without a funded balance
- evidence:
  - [1] 2026-11-18: xxapi requires a funded balance before a key can call models | capture: sha256:822d6d452c211c390f513905fa9067a7a9c0f1f5d7a90b13a71202f0701bb859 | quote: 创建密钥之前，先确认 xxapi 账户有余额，没有余额无法调用。
- sources:
  - [1] https://docs.xxapi.ai/
