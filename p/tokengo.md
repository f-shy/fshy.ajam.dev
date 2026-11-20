# TokenGo

> tokengo.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokengo/ | JSON https://fshy.ajam.dev/api/v1/entity/tokengo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TokenGo

- `inference/tokengo` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://www.tokengo.com/docs/guides/billing
- free tier: Charged by actual token consumption from a prepaid balance topped up through Stripe or a redemption code; no free inference allowance is published. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: top-up through Stripe with preset amounts from USD 10; a redemption code also works
- interface: rest
- limits:
  - volume-quota (binding): prepaid balance from Stripe top-ups or redemption codes; no free tier [1]
- endpoint: https://api.tokengo.com/v1
- composes with: the prepaid balance is the scarce link
- reliability: a group ratio other than 1.0 multiplies the cost
- evidence:
  - [1] 2026-11-18: TokenGO is a prepaid per-token service with no published free allowance | capture: sha256:6059fce55636e687fe347a0c4db23df20e832c119b5c7321b0ca6a6bc09cfd5c | quote: TokenGO charges based on actual token consumption:
- sources:
  - [1] https://www.tokengo.com/docs/guides/billing
