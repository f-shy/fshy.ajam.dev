# APIKO

> apiko.app | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apiko/ | JSON https://fshy.ajam.dev/api/v1/entity/apiko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## APIKO

- `inference/apiko` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://apiko.app/
- free tier: Free to sign up; new accounts get $0.20 free to use on any model, no credit card required. After that pay-as-you-go from a top-up wallet (packs from $5). | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is free and needs no credit card; a $0.20 credit is granted
- interface: rest
- limits:
  - volume-quota (binding): $0.20 one-time free credit on signup; pay-as-you-go thereafter [1]
- endpoint: https://api.apiko.app/v1
- tooling: an OpenAI-compatible key with one-line base_url swap
- composes with: the one-time $0.20 signup credit is the only free allowance; usage is billed from a funded wallet after that
- reliability: the free credit is finite and one-time
- evidence:
  - [1] 2026-11-18: new accounts get $0.20 free with no credit card | capture: sha256:0af6c8f959fce8379d4a3d85badb1086339a1bd774f6fecd1508bf50b4f25c2f | quote: Free to sign up. New accounts get $0.20 free to use on any model, no credit card required.
- sources:
  - [1] https://apiko.app/
