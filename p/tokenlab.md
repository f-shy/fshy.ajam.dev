# TokenLab

> tokenlab.sh | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenlab/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenlab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TokenLab

- `inference/tokenlab` | paid-only | evidence documented | binding volume-quota | category inference gateway (prepaid)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://tokenlab.sh/en/pricing
- free tier: TokenLab has no subscriptions and no seat licenses. Add funds to your balance once, and every API call is deducted at the per-model rate listed in the model catalog. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: top up before use; no free signup credit is stated
- interface: rest
- limits:
  - volume-quota (binding): USD 5 minimum top-up; a USD 5 first-top-up bonus on USD 10; balance does not expire [1]
- endpoint: https://api.tokenlab.sh/v1
- composes with: No free text inference allowance is published in the fetched pricing page.
- reliability: failed image or video tasks are not charged
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: TokenLab is prepaid only with no free tier stated; the first top-up bonus is USD 5 on a USD 10 payment | capture: sha256:c4d6507724fac2886afa3c22bfadc941650c9619030fe402e0997a1fe47cad2c | quote: TokenLab has no subscriptions and no seat licenses. Add funds to your balance once, and every API call is deducted at the per-model rate listed in the model catalog.
- sources:
  - [1] https://tokenlab.sh/en/pricing
