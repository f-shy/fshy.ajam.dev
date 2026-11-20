# Tokenify

> tokenify.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tokenify/ | JSON https://fshy.ajam.dev/api/v1/entity/tokenify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tokenify

- `inference/tokenify` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://www.tokenify.dev/docs/quickstart/
- free tier: New accounts receive a small amount of trial credit to try the API; after that, requests are billed per token against prepaid credit topped up by card or stablecoin, and credit does not expire. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create an account and a key is issued during setup; top-up needs a card or stablecoin
- interface: rest
- limits:
  - volume-quota (binding): small trial credit for new accounts, then prepaid top-up by card or stablecoin [1]
- endpoint: https://api.tokenify.dev/v1
- composes with: the small trial credit is the only free route
- reliability: a request without max_tokens reserves the model's entire output ceiling, which can exceed trial credit and return 402
- evidence:
  - [1] 2026-11-18: new accounts get a small trial credit and then must top up | capture: sha256:ecba9e38225d0f534f7bf17b7a4dfde23f8770cafebd95abbe6288e3b76acd78 | quote: New accounts get a small amount to try the API with; after that, [top up](https://www.tokenify.dev/app/billing) by card or stablecoin.
- sources:
  - [1] https://www.tokenify.dev/docs/quickstart/
