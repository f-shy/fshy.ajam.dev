# Klavo AI

> klavo.ru | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/klavo/ | JSON https://fshy.ajam.dev/api/v1/entity/klavo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Klavo AI

- `inference/klavo` | paid-only | evidence documented | binding write-gated | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://ai.klavo.ru/docs
- free tier: No free allowance is stated on the docs read 2026-11-18: the quickstart requires registration and a balance top-up in the 'Tariff' section before a key can call the catalog. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: registration plus a top-up in the Tariff section is needed before calls succeed
- interface: rest
- limits:
  - volume-quota: a topped-up balance is reserved before each request; 402 insufficient_balance otherwise [1]
  - write-gated (binding): the binding constraint named on the first-party page [1]
- endpoint: https://api.klavo.ru/v1
- tooling: an OpenAI-compatible key (kl-) with session prefix caching
- composes with: the top-up prerequisite is the scarce link; no free text tier is published
- reliability: without max_tokens the response is reserved at 16,384 tokens and shortened if the balance is low
- evidence:
  - [1] 2026-11-18: registration and a balance top-up are required before a key works | capture: sha256:0f6e5503fff2c42f3beb57943088587517f210e5f823643c25518bee085e909e | quote: и пополните баланс в разделе
- sources:
  - [1] https://ai.klavo.ru/docs
