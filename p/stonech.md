# flm

> stonech.at | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stonech/ | JSON https://fshy.ajam.dev/api/v1/entity/stonech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## flm (flm.stonech.at)

- `inference/flm` | qualifies-with-caveat | evidence documented | binding request-rate | category inference endpoint, keyless, one auto-selected model
- needs card no, phone no, ID no, institution no | verified 2026-11-10T01:21:20.504Z (live) | stale on 2026-12-11
- url https://flm.stonech.at/v1
- free tier: No account and no API key. Per IP address: 60 requests per minute, 20,000 requests per day, 10,000,000 tokens per day, at most 65,536 input tokens and 8,192 output tokens per request | unit: tokens | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the service chooses the model on every request; GET /v1/models lists one id, auto, and a requested model is ignored
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: none: the guide lists Authentication as None; omit the Authorization header or send Bearer flm_anonymous, and any other key is rejected with 401
- interface: rest
- limits:
  - request-rate (binding): 60 requests per minute per IP address (rolling 60-second window); over the limit the service answers 429 rate_limit_exceeded with a retry-after header [1]
  - volume-quota: 20,000 requests per day and 10,000,000 tokens per day per IP address, both reset at 00:00 UTC; 65,536 input tokens and 8,192 output tokens per request [1]
- binding note: the 60 requests per minute per IP address binds before the 20,000 per day
- endpoint: https://flm.stonech.at/v1/chat/completions
- tooling: any OpenAI-compatible client; POST {base}/chat/completions with no Authorization header, or with Bearer flm_anonymous for SDKs that insist on a key. GET /limits returns the live limits as JSON and is not counted
- composes with: pairs with an agent loop that sets max_tokens; the model cannot be pinned, and the service picks one per request
- reliability: under load the service answers 429 rate_limited after making a request wait up to 8s for capacity, and 502 upstream_error when an answer fails mid-way; identical temperature-0 requests may be served from a short-lived cache
- notes: the requested model is never echoed because the service ignores it; the guide names no field that reports the model chosen, so which model answered a given request is unknown
- evidence note: the limits, the model list and the x-ratelimit headers were read by GET; no chat completion was sent, because probe issues GET and HEAD only, so whether a completion answers is…
- probe:
  - records[0].probe_id: flm-v1-models-get
  - records[0].method: GET
  - records[0].url: https://flm.stonech.at/v1/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].model_ids: auto
  - records[0].ratelimit_headers.x-ratelimit-limit-requests: 60
  - records[0].ratelimit_headers.x-ratelimit-limit-tokens: 10000000
  - records[0].body_sha256: 7ed98fb0d5385b11890fb4366b75932f1f47018d38aed01ee158c04d446bad1c
  - records[0].probed_at: 2026-10-28T04:42:49.584Z
  - records[0].chat_completion_tested: no
  - records[1].probe_id: flm-limits-get
  - records[1].method: GET
  - records[1].url: https://flm.stonech.at/limits
  - records[1].http: 200
  - records[1].authorization_sent: no
  - records[1].body.requests_per_minute: 60
  - records[1].body.requests_per_day: 20000
  - records[1].body.tokens_per_day: 10000000
  - records[1].body.max_input_tokens: 65536
  - records[1].body.max_output_tokens: 8192
  - records[1].probed_at: 2026-10-28T04:42:47.629Z
- evidence:
  - [1] 2026-10-28: the guide states Authentication is None: no account and no key are needed | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: None. Either omit the Authorization header, or (for SDKs that require a key) send:
  - [1] 2026-10-28: the request-rate limit is 60 per minute per IP address | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: - Requests per minute: 60 (rolling 60-second window)
  - [1] 2026-10-28: the daily request limit is 20,000 | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: - Requests per day: 20,000 (resets 00:00 UTC)
  - [1] 2026-10-28: the daily token limit is 10,000,000, input plus output | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: - Tokens per day: 10,000,000 (input + output; resets 00:00 UTC)
  - [1] 2026-10-28: the per-request input cap is 65,536 tokens | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: - Max input tokens per request: 65,536
  - [1] 2026-10-28: the requested model is not honoured and not echoed back: the service picks one | capture: sha256:298e0b67c30da55b19a5d0ae05f3976b52ca231b82e0ff06248b688d0853f5d0 | quote: The model is chosen automatically for every request. Any "model" you send is ignored; use "auto".
  - [2] 2026-10-28: a keyless GET /v1/models answered 200 and returned the x-ratelimit-limit-requests header at 60 | capture: sha256:7bc6629878e0ff2cf92ba86e8b64ffa092ac520c3c995aa2f77da0af607808e3 | quote: x-ratelimit-limit-requests: 60
  - [2] 2026-10-28: the only model id listed is auto | capture: sha256:7bc6629878e0ff2cf92ba86e8b64ffa092ac520c3c995aa2f77da0af607808e3 | quote: {"object":"list","data":[{"id":"auto","object":"model","created":0,"owned_by":"flm"}]
  - [3] 2026-10-28: the home page states no account, no API key and no credit card | capture: sha256:315185a868ac95f4f737c9dade875241b82ddb5bbbdbe73fc1af894d4d6f0e21 | quote: - $0, no signupNo account, no API key, no credit card.
  - probe:https://flm.stonech.at/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 for auto answered 200 twice with content 'pong' | capture: sha256:71bcfd3b3b6de19a40bda447f510ac934f1ba5c2a33f972080052bffed9c5e03 | quote: "status": 200
- sources:
  - [1] https://flm.stonech.at/docs.txt
  - [2] https://flm.stonech.at/v1/models
  - [3] https://flm.stonech.at/
