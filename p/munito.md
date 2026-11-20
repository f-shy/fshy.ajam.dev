# Munito AI

> munito.ai | Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/munito/ | JSON https://fshy.ajam.dev/api/v1/entity/munito.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Munito AI

- `inference/munito` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.munito.ai/pricing
- disagrees on verdict: `inference/munito` says qualifies-with-caveat, `inference/munito-eu` says fails-identity
- free tier: A free tier open to a new account with a verified phone number, when capacity is available; at a zero balance the account continues on the free tier, and paid routes start at USD 0.099 per 1M input tokens. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: the free tier requires a verified phone number on the account
- interface: rest
- limits:
  - request-rate (binding): free-tier use depends on available capacity [1]
- endpoint: https://api.munito.ai/inference/v1
- composes with: capacity is the scarce link, so a free-tier plan cannot be depended on at a fixed hour
- reliability: the free tier is explicitly capacity-gated, so a request can be refused while the account is in good standing
- evidence:
  - [1] 2026-11-18: a phone-verified account can use the free tier when capacity is available, and a zero balance falls back to it | capture: sha256:2cc7770abad2e9b625d84f4b344044ff05fe8f3a72b839e87bb968923f6ecf2a | quote: - Free tier. A new account with a verified phone number can use the free tier, when capacity is available.
- sources:
  - [1] https://docs.munito.ai/pricing

## Munito AI (EU)

- `inference/munito-eu` | fails-identity | evidence documented | binding volume-quota | category inference gateway (EU region)
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.munito.ai/pricing
- disagrees on verdict: `inference/munito` says qualifies-with-caveat, `inference/munito-eu` says fails-identity
- free tier: A new account with a verified phone number can use the free tier, when capacity is available. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: a verified phone number is required to enter the free tier; capacity must also be available
- interface: rest
- limits:
  - volume-quota (binding): free tier usage when capacity is available; at a zero balance the account continues on the free tier [1]
- endpoint: https://api.eu.munito.ai/inference/v1
- composes with: This is the EU-hosted variant of Munito AI (api.eu.munito.ai); the free tier and its phone gate are documented on the shared pricing page. The /regions page fetched for this id only lists base URLs.
- reliability: the free tier is capacity-dependent; 421 if a data-region request goes to the wrong regional host
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: the Munito AI free tier is open to a new account with a verified phone number, subject to capacity | capture: sha256:2cc7770abad2e9b625d84f4b344044ff05fe8f3a72b839e87bb968923f6ecf2a | quote: A new account with a verified phone number can use the free tier, when capacity is available.
- sources:
  - [1] https://docs.munito.ai/pricing
