# JarvisClaw free route

> jarvisclaw.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jarvisclaw/ | JSON https://fshy.ajam.dev/api/v1/entity/jarvisclaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JarvisClaw free route (auto/free)

- `inference/jarvisclaw-free` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, keyless free route, x402 pay-per-call for other models
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-28
- url https://api.jarvisclaw.ai/v1
- free tier: Requests with model auto/free and no credential are not billed and are rate limited per IP address in gateway calls per minute; no number is published | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: auto/free routes to an open-weight model from a shared free pool, so the served model is chosen by the gateway; any other model answers HTTP 402 with a price quote in USDC
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: none for the free route: send no Authorization header at all; a placeholder key is rejected with 401, and no account or wallet is needed
- interface: rest
- limits:
  - request-rate (binding): unpublished: the page says the free route is rate limited per IP address, measured in gateway calls per minute, and gives no number [1]
- binding note: the per-IP gateway-call ceiling is the only stated limit and its value is not published
- endpoint: https://api.jarvisclaw.ai/v1/chat/completions
- tooling: plain HTTP POST with no Authorization header; an OpenAI SDK always sends a key header, which the free route rejects with 401. CORS is allowed for browser use
- composes with: pairs with prototypes that need a model to answer rather than a particular model; the paid route is an x402 wallet payment on Base or Solana
- reliability: the free models are served from a shared pool, so latency varies; GET /v1/models without a credential answers 401, so the catalogue is not open
- notes: the echoed model on a completion was not observed; the page states the response names the model that answered
- evidence note: the free route was not exercised: probe issues GET and HEAD only. A GET to /v1/models with no credential answered 401 Invalid token, and a GET to /v1/chat/completions answered 402 with a payment quote, so neither GET shows a completion
- probe:
  - records[0].probe_id: jarvisclaw-v1-models-get
  - records[0].method: GET
  - records[0].url: https://api.jarvisclaw.ai/v1/models
  - records[0].http: 401
  - records[0].authorization_sent: no
  - records[0].error_message: Invalid token
  - records[0].probed_at: 2026-10-28T04:43:11.573Z
  - records[1].probe_id: jarvisclaw-chat-get
  - records[1].method: GET
  - records[1].url: https://api.jarvisclaw.ai/v1/chat/completions
  - records[1].http: 402
  - records[1].authorization_sent: no
  - records[1].body_kind: x402 payment quote
  - records[1].probed_at: 2026-10-28T04:43:14.580Z
  - records[1].chat_completion_tested: no
- evidence:
  - [1] 2026-10-28: the free route needs no key, account or wallet and is rate limited per IP | capture: sha256:a452ebefb70b6cf08fc28c0c02acd9fecfb92008d7afb1a72288633b4b45a1d1 | quote: Call a free LLM with one curl command: no API key, no account and no wallet. OpenAI-compatible, rate limited per IP, with paid models one 402 quote away.
  - [1] 2026-10-28: the free route admits only requests with no credential at all | capture: sha256:a452ebefb70b6cf08fc28c0c02acd9fecfb92008d7afb1a72288633b4b45a1d1 | quote: Send no Authorization header at all. The free tier admits only requests that carry no credential, and a placeholder key is rejected with 401.
  - [1] 2026-10-28: the only published limit is per IP address per minute, with no number | capture: sha256:a452ebefb70b6cf08fc28c0c02acd9fecfb92008d7afb1a72288633b4b45a1d1 | quote: Rate limited per IP address, measured in gateway calls per minute.
  - [1] 2026-10-28: the model is chosen by the gateway and named in the response, so the requested id is not honoured as such | capture: sha256:a452ebefb70b6cf08fc28c0c02acd9fecfb92008d7afb1a72288633b4b45a1d1 | quote: auto/free routes to an open-weight model from the free pool. The response names the model that answered, so you can see which one you got.
  - [2] 2026-10-28: a keyless GET to /v1/models answered 401 Invalid token | capture: sha256:506207c36780a5866b669a33243a2b30261845bd331ba6be4c574fc98d32389f | quote: Invalid token
  - probe:https://api.jarvisclaw.ai/v1/chat/completions 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 402 with a payment quote, so no free route is served | capture: sha256:6e38d7fdbd48f6ee7f703bdbd4100ddd5a12ee4f6637e14ad2e56160a41eaeee | quote: "status": 402
- sources:
  - [1] https://jarvisclaw.ai/en/free-llm-api
  - [2] https://api.jarvisclaw.ai/v1/models
