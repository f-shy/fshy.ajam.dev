# TensorX

> tensorx.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensorx/ | JSON https://fshy.ajam.dev/api/v1/entity/tensorx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TensorX

- `inference/tensorx` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://docs.tensorx.ai/billing.md
- free tier: Prepaid credit only, charged per token; no free inference allowance is published, and accounts are disabled when the balance falls below USD 0.05. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: credit/debit card is the only published payment method; no free tier
- interface: rest
- limits:
  - volume-quota (binding): prepaid credit; account and keys disabled below USD 0.05 [1]
- endpoint: https://api.tensorx.ai/v1
- composes with: the prepaid balance and the USD 0.05 floor bind first
- reliability: a balance below USD 0.05 disables the account and all API keys
- evidence:
  - [1] 2026-11-18: TensorX is prepaid only and disables accounts below USD 0.05, with no free allowance | capture: sha256:934bfae0575580bdcc7188653ab843452e9eeec0256316d779f0bb79f777721a | quote: When your balance falls below $0.05, your account and API keys will be automatically disabled to prevent negative balance.
- sources:
  - [1] https://docs.tensorx.ai/billing.md
