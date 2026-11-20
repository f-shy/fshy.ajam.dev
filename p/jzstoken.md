# JZSTOKEN

> jzstoken.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jzstoken/ | JSON https://fshy.ajam.dev/api/v1/entity/jzstoken.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JZSTOKEN

- `inference/jzstoken` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://jzstoken.com/
- free tier: jzs-max-3.0 is free until Nov 30, 2026 (UTC): calls to this model are $0 during the promotion, using a dedicated key; the rest of the 78-model catalog is pay-per-token from a $1.50 minimum balance. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: registration then a key in the dashboard; the free promoted model needs a dedicated key
- interface: rest
- limits:
  - volume-quota (binding): one model free at $0 until 2026-11-30; all other models prepaid from $1.50 [1]
- endpoint: https://jzstoken.com/api/v1
- tooling: an OpenAI-compatible key; jzs-max-3.0 needs its own dedicated key
- composes with: the expiring free promotion on one model is the scarce link, not a standing free tier
- reliability: the free period ends 2026-11-30, after which the model presumably becomes paid
- evidence:
  - [1] 2026-11-18: one model is free at $0 during a dated promotion | capture: sha256:65e98975e053fb759aff303b7294711ead54d5188ced7165923b82b448277cff | quote: Calls to this model are $0 during the promotion.
- sources:
  - [1] https://jzstoken.com/
