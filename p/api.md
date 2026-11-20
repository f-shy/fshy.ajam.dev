# Api.Airforce

> api.airforce | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/api/ | JSON https://fshy.ajam.dev/api/v1/entity/api.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Api.Airforce

- `inference/api-airforce` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, free plan behind a username-and-password account
- needs card no, phone no, ID no, institution no | verified 2026-11-10T02:44:00.000Z (live) | stale on 2026-12-11
- url https://api.airforce/v1
- free tier: Free plan, $0.00/month: 1 request per minute, 1 000 requests per day, free models only | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: GET /v1/models lists 783 ids; 29 carry tier free (6 operational, 1 degraded, 22 major_outage when read) and 754 carry tier paid
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: a free account with a username and a password: no email and no card required to start, and the API key is generated in the dashboard. The g4f.dev provider page states the free tier is available without an API key and its JavaScript example sends no Authorization header; a keyless POST on 2026-11-10 to kimi-k2.7-code answered 401 Missing Authorization, and a second call 429
- interface: rest
- limits:
  - request-rate (binding): 1 request per minute on the Free plan (a paid Starter plan is 20 per minute) [1]
  - volume-quota: 1 000 requests per day on the Free plan, free models only [1]
- binding note: 1 request per minute binds long before 1 000 requests per day
- endpoint: https://api.airforce/v1/chat/completions
- tooling: any OpenAI-compatible client; POST {base}/chat/completions. A GET to the route answers 405 with Allow: POST
- composes with: pairs with an agent as a catalogue with a per-id status field; the Free plan rate of 1 request per minute is the scarce link
- reliability: the listing carries a status per id: 22 of the 29 ids with tier free read major_outage when the listing was fetched, so most free ids were not serving
- notes: a keyless completion is not served for the ids tried on 2026-11-10: kimi-k2.7-code answered 401 Missing Authorization and then 429, gemini-3.6-flash answered 402, and mistral-code-fim-latest answered 401; whether any id answers with no Authorization header is unverified; the account route is the documented one
- evidence note: the plan limits and the signup are first-party; the keyless claim is on the g4f.dev provider page and in a third-party router that lists the service as a keyless upstream. The 2026-10-28 probes sent no completion because probe issues GET and HEAD only; a keyless POST on 2026-11-10 then answered 401 Missing Authorization, and a second call 429
- probe:
  - records[0].probe_id: airforce-v1-models-get
  - records[0].method: GET
  - records[0].url: https://api.airforce/v1/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].model_count: 783
  - records[0].tier_free: 29
  - records[0].tier_free_status.operational: 6
  - records[0].tier_free_status.degraded: 1
  - records[0].tier_free_status.major_outage: 22
  - records[0].tier_paid: 754
  - records[0].body_sha256: 87ca644739712fc0ad8107f67db7e38c7d42e49332fa021ca3d7510576f7d710
  - records[0].probed_at: 2026-10-28T04:49:23.618Z
  - records[0].chat_completion_tested: no
  - records[1].probe_id: airforce-chat-get
  - records[1].method: GET
  - records[1].url: https://api.airforce/v1/chat/completions
  - records[1].http: 405
  - records[1].allow: POST
  - records[1].probed_at: 2026-10-28T04:45:34.991Z
- evidence:
  - [1] 2026-10-28: the Free plan allows 1 request per minute | capture: sha256:b41ad83508d8ee9c814393c13ae4a20fa8bc5440faa6b679ccb5fd45741c35a5 | quote: - 1 request per minute
  - [1] 2026-10-28: the Free plan allows 1 000 requests per day | capture: sha256:b41ad83508d8ee9c814393c13ae4a20fa8bc5440faa6b679ccb5fd45741c35a5 | quote: - 1 000 requests per day
  - [1] 2026-10-28: the Free plan is limited to free models | capture: sha256:b41ad83508d8ee9c814393c13ae4a20fa8bc5440faa6b679ccb5fd45741c35a5 | quote: | Model access | Free models | All models | All models | All models | All models | All models |
  - [2] 2026-10-28: signup needs a username and a password, no email and no card | capture: sha256:0f7b56cfdd37f7343a59c14473dc187e2c238ed2ffa6991ece0b082f39d40a24 | quote: Visit the signup page and create a free account with a username and password. No email or credit card required to start.
  - [2] 2026-10-28: the first-party docs authenticate with an API key in the Authorization header | capture: sha256:0f7b56cfdd37f7343a59c14473dc187e2c238ed2ffa6991ece0b082f39d40a24 | quote: Use your API key in the Authorization header to authenticate requests to any endpoint.
  - [3] 2026-10-28: the g4f.dev provider page states the free tier is available without an API key | capture: sha256:607b04ec9e37a44ee2db10b601177a981850a6e51e21ccf6bfb1437ad5f17f4b | quote: - 🆓 Free Tier: Available without API key
  - [4] 2026-10-28: a keyless GET /v1/models answered 200 with 783 ids, 29 of them tier free | capture: sha256:3d347562d999c332751901f0b9758892358928ca93bb35f68e0e6557e52d358b | quote: models=783; tier=free: 29 (status operational 6, degraded 1, major_outage 22); tier=paid: 754.
  - [5] 2026-10-28: a third-party keyless router lists Api.Airforce as a keyless upstream | capture: sha256:a8751dbcdbd0b350e87244c4bcdedc348fdc9370de65674a9e9ec26960e0977d | quote: multi-provider aggregation (Pollinations + [ApiAirforce](https://api.airforce/) today, more as they appear)
  - probe:https://api.airforce/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 to kimi-k2.7-code answered HTTP 401 Missing Authorization on the first call and HTTP 429 Global rate limit exceeded on the second | capture: sha256:6c8843a845eefa29d808b4eed8f0ad94837bbe57ec4e69987d402ce8e4e1ea90 | quote: "status": 401
  - probe:https://api.airforce/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for gemini-3.6-flash answered 402 on both calls and for mistral-code-fim-latest answered 401 Missing Authorization on both calls | capture: sha256:9e50ce7c9bd5f2ba4fa67d202ad668b465817880e09074bf93f295a0214fd471 | quote: "status": 402
- sources:
  - [1] https://api.airforce/pricing/
  - [2] https://api.airforce/docs/authentication/
  - [3] https://g4f.dev/docs/providers/api-airforce.md
  - [4] https://api.airforce/v1/models
  - [5] https://www.npmjs.com/package/keylessai
