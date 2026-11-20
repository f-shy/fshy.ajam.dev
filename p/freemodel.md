# FreeModel

> freemodel.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freemodel/ | JSON https://fshy.ajam.dev/api/v1/entity/freemodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FreeModel

- `inference/freemodel` | qualifies | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://freemodel.dev/pricing
- free tier: USD 300 in credits on signup, no payment info required, against FRE-5.4 and FRE-5.5. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup plus account verification; the page states no payment info is required for the USD 300
- interface: rest
- limits:
  - volume-quota (binding): USD 300 of credits on signup [1]
- endpoint: https://cc.freemodel.dev/v1
- composes with: USD 300 is the scarce link; the page prices nothing beyond the credit
- reliability: a signup credit with no published expiry or rate limit, so the constraint after the credit is unmeasured
- evidence:
  - [1] 2026-11-18: every new account receives USD 300 in credits instantly and no payment info is required | capture: sha256:0900656787fe1d23df9697bba42b427865de8ae276afdcef1db435f6b90072a3 | quote: Every new account gets $300 in credits instantly — no payment info required. Start building right away.
- sources:
  - [1] https://freemodel.dev/pricing
