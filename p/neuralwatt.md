# Neuralwatt

> neuralwatt.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neuralwatt/ | JSON https://fshy.ajam.dev/api/v1/entity/neuralwatt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neuralwatt

- `inference/neuralwatt` | fails-identity | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://portal.neuralwatt.com/docs
- free tier: USD 1.00 in free trial credit, unlocked only by adding a payment method; new accounts otherwise start at a USD 0 balance. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the USD 1.00 trial credit is unlocked by adding a payment method in the billing dashboard
- interface: rest
- limits:
  - volume-quota (binding): USD 1.00 of trial credit, gated on a payment method [1]
- endpoint: https://api.neuralwatt.com/v1
- composes with: the card gate is the scarce link before the credit is even usable
- reliability: the credit is USD 1.00 and cannot be reached without a card, so the gate binds before the quota
- evidence:
  - [1] 2026-11-18: new accounts start at a USD 0 balance and adding a payment method unlocks USD 1.00 in free trial credit | capture: sha256:78d30ae5492720fc73282396408043f940a70ac30a31493dee9d580dc3fce168 | quote: 2. Add a payment method in Dashboard > Billing — new accounts start with a $0 balance, and adding a payment method unlocks $1.00 in free trial credit (no charge required; the credit is valid for 30 days)
- sources:
  - [1] https://portal.neuralwatt.com/docs
