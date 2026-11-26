# ToAPIs

> toapis.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/toapis/ | JSON https://fshy.ajam.dev/api/v1/entity/toapis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ToAPIs

- `inference/toapis` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://toapis.com/pricing
- free tier: Every model is billed by actual usage with a USD 0 monthly fee and no seat licenses; top up once into a shared balance (1 credit is about USD 0.005); no free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: sign in and top up in the Billing Center; no free tier stated
- interface: rest
- limits:
  - volume-quota (binding): shared prepaid USD balance, 1 credit about USD 0.005 [1]
- endpoint: https://toapis.com/v1
- composes with: the shared prepaid balance is the scarce link
- reliability: failed upstream calls are not billed
- evidence:
  - [1] 2026-11-18: ToAPIs bills by actual usage with no monthly fee and no free inference allowance | capture: sha256:4b263f9fd9b56d5b00a6d9ced2d78a115789280791c98a9f0853b99f4d77f75b | quote: $0 monthly fee, no seat licenses
- sources:
  - [1] https://toapis.com/pricing
