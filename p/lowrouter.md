# LowRouter

> lowrouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lowrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/lowrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LowRouter

- `inference/lowrouter` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://lowrouter.ai/pricing
- free tier: No standing free tier: a new account can request an invite for EUR 5 of trial credit; otherwise the smallest top-up is EUR 5.00. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an invite is requested through the register page; no card needed to request trial credit
- interface: rest
- limits:
  - volume-quota (binding): EUR 5 trial credit by invite, otherwise EUR 5 minimum top-up [1]
- endpoint: https://api.lowrouter.ai/v1
- composes with: the invite-gated trial credit is the only free route
- reliability: trial credit requires an invite, which is not an open self-serve route
- evidence:
  - [1] 2026-11-18: a new account can request EUR 5 of trial credit by invite and otherwise must top up at least EUR 5 | capture: sha256:ba3629bdb2f0229655f09d27eff3623dc67602a6de253dbb02fc5d2925e70a27 | quote: for €5 of trial credit. Otherwise the smallest top-up is €5.00.
- sources:
  - [1] https://lowrouter.ai/pricing
