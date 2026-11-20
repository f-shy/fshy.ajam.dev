# LithosAI

> lithosai.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lithosai/ | JSON https://fshy.ajam.dev/api/v1/entity/lithosai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LithosAI

- `inference/lithosai` | paid-only | evidence documented | binding none | category inference gateway (prepaid)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.lithosai.com/billing.md
- free tier: LithosAI inference service is prepaid. Each request is metered to the token and debited from your organization's balance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: email signup with a prepaid organization balance; top-up from USD 5
- interface: rest
- limits:
  - volume-quota: prepaid balance; no free inference allowance stated [1]
- endpoint: https://api.lithosai.cloud/v1
- composes with: No free text inference allowance is published on the captured billing page; the only figures are prepaid top-up amounts.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: LithosAI inference is prepaid with no free allowance stated; top-ups are USD 5 to 5,000 | capture: sha256:7c6595f06ca2f1a2f725af248296b3c6f6cf669fd79c3ae0096aaf3f9ef56c05 | quote: LithosAI inference service is prepaid. Each request is metered to the token and debited from your organization's balance.
- sources:
  - [1] https://docs.lithosai.com/billing.md
