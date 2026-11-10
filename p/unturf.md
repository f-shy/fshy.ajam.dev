# uncloseai

> unturf.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unturf/ | JSON https://fshy.ajam.dev/api/v1/entity/unturf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uncloseai (unturf)

- `inference/uncloseai` | dead | evidence measured | binding none | category inference endpoint, keyless beta now closed
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-28
- url https://hermes.ai.unturf.com/v1
- free tier: no keyless access: GET /v1/models answers 401 public_beta_closed, saying the endpoint needs an API key and key registration is closed | unit: none | metered on: none | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: the offer was keyless; the endpoint now answers 401 and states that it needs an API key and that key registration is closed
- interface: rest
- limits note: no rate or quota binds: the gate is access, not allowance
- endpoint: https://hermes.ai.unturf.com/v1/chat/completions
- tooling: any OpenAI-compatible client; a key is needed and none can be registered
- composes with: no chain exists while key registration is closed
- reliability: a third-party prober recorded the endpoint answering 5 to 7 of 24 chat calls a day from 15 to 21 Oct and 0 of 24 a day from 22 to 27 Oct
- notes: dead cause: registration-closed; the host still answers, and it refuses every keyless call
- evidence note: the 401 body and the x-maintenance header were read directly; the daily answer counts are third-party
- probe:
  - records[0].probe_id: unturf-v1-models-get
  - records[0].method: GET
  - records[0].url: https://hermes.ai.unturf.com/v1/models
  - records[0].http: 401
  - records[0].authorization_sent: no
  - records[0].x_maintenance: public-beta-closed
  - records[0].error_type: public_beta_closed
  - records[0].probed_at: 2026-10-28T04:47:26.033Z
- evidence:
  - [1] 2026-10-28: the endpoint now refuses a keyless call and says key registration is closed | capture: sha256:c5999d03b995013e3490b8a5b3fecb771ee36cc6fb35c0f891578df5ac497b81 | quote: The public beta is closed for now. This endpoint needs an API key, and key registration is closed; check uncloseai.com for when it reopens.
  - [1] 2026-10-28: the response carries an x-maintenance header of public-beta-closed | capture: sha256:c5999d03b995013e3490b8a5b3fecb771ee36cc6fb35c0f891578df5ac497b81 | quote: x-maintenance: public-beta-closed
  - [2] 2026-10-28: the keyless offer was claimed as free forever with no signup | capture: sha256:07a6e55675bac7af80e7bd5ac6c5df9b1af98d123bb90d3a050ae65e0c1d6b64 | quote: Claimed free forever with no signup, self-published and carried by OmniRoute's routing registry as an endpoint needing no key.
  - [2] 2026-10-28: from 22 Oct a third-party prober got no keyless chat answer | capture: sha256:07a6e55675bac7af80e7bd5ac6c5df9b1af98d123bb90d3a050ae65e0c1d6b64 | quote: | 22 Oct | 24 | 0 of 24 | — |
- sources:
  - [1] https://hermes.ai.unturf.com/v1/models
  - [2] https://stillworks.supercapybara.com/llm/uncloseai
