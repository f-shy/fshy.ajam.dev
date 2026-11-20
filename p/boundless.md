# Boundless

> boundless.network | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boundless/ | JSON https://fshy.ajam.dev/api/v1/entity/boundless.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Boundless

- `inference/boundless` | paid-only | evidence documented | binding volume-quota | category inference gateway, pay-per-token
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://inference.boundless.network/models
- free tier: no free tier published: every model lists a USD per-1M-token input and output rate; one free-model entry (minimax-m3-free) is marked Not serving | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key is required for the gateway; no card or phone field is stated on the models page
- interface: rest
- limits:
  - volume-quota (binding): per-token USD rates for every serving model; no free token allowance is listed [1]
- binding note: no free allowance exists, so payment binds first
- endpoint: https://api.inference.boundless.network/v1
- tooling: an OpenAI-compatible key and the vendor's gateway clients
- composes with: pairs with an OpenAI-compatible agent on a paid per-token basis; no standing free route
- reliability: no reliability event recorded
- notes: the lone free-labelled entry is Not serving; all serving models carry per-token rates.
- evidence:
  - [1] 2026-11-18: rates are USD per 1M tokens and a free-labelled model is Not serving | capture: sha256:bf7dc95496f6e5c8cc88a79563146c81c3ae4ed02ea5ebdcc4c794a20c32f2ea | quote: Rates are USD per 1M tokens, on-demand tier, read live from the gateway; cached input is charged at the cached rate when a request reuses a prefix the gateway already holds.
- sources:
  - [1] https://inference.boundless.network/models
