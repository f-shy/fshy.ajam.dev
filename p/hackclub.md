# Hack Club AI

> hackclub.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hackclub/ | JSON https://fshy.ajam.dev/api/v1/entity/hackclub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hack Club AI

- `inference/hack-club-ai` | fails-identity | evidence documented | binding volume-quota | category inference gateway, keyed; model listing is keyless
- needs card no, phone no, ID no, institution yes | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-28
- url https://ai.hackclub.com/proxy/v1
- free tier: Every account can spend $3 per day across all endpoints and make 7,500 requests per 30 minutes; no credit card | unit: mixed | metered on: request-count | read on: 2026-10-28 | source: [1] | note: the model catalogue is OpenRouter's; GET /proxy/v1/models answers 200 with no key while the chat call answers 401 without one
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: sign in with a Hack Club account, then create an API key; the rules page states the service is for teens 18 and under only, and lists a 403 for an account that needs identity verification
- interface: rest
- limits:
  - request-rate: 7,500 requests per 30 minutes per user, shared across all endpoints; 429 Too Many Requests with a Retry-After header [1]
  - volume-quota (binding): USD 3 per day of spend per account across all endpoints, resets at 00:00 UTC; 402 Payment Required when reached [1]
- binding note: the USD 3 per day spending cap binds for large models; the 7,500 per 30 minutes request ceiling is far above it
- endpoint: https://ai.hackclub.com/proxy/v1/chat/completions
- tooling: any OpenAI-compatible client with an sk-hc-v1 key created on the dashboard (up to 50 active keys)
- composes with: no keyless chain: the chat route needs a key issued to a signed-in Hack Club account
- reliability: a keyless chat call answers 401 Authentication required while the keyless listing answers 200, so a listing check alone mistakes it for an open endpoint
- evidence note: identity and limits are first-party; the 401 on a keyless chat call is from a third-party prober, and the keyless listing was read by GET. No completion was sent
- probe:
  - records[0].probe_id: hackclub-proxy-models-get
  - records[0].method: GET
  - records[0].url: https://ai.hackclub.com/proxy/v1/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].probed_at: 2026-10-28T04:43:23.476Z
  - records[0].chat_completion_tested: no
- evidence:
  - [1] 2026-10-28: the service is restricted to a teen audience of Hack Club | capture: sha256:42f561557e3c18af30ca81342a65091ee6eeb6e9f6da771d9c1deda2c694eaf6 | quote: 1. For teens. This service is for teens 18 and under only. Hack Club is a charity — please do not abuse this service.
  - [1] 2026-10-28: the request ceiling is 7,500 per 30 minutes per user | capture: sha256:42f561557e3c18af30ca81342a65091ee6eeb6e9f6da771d9c1deda2c694eaf6 | quote: Every user can make 7,500 requests per 30 minutes, shared across all endpoints.
  - [1] 2026-10-28: the daily spend cap is USD 3 | capture: sha256:42f561557e3c18af30ca81342a65091ee6eeb6e9f6da771d9c1deda2c694eaf6 | quote: Every account can spend $3 per day across all endpoints. The day resets at 00:00 UTC.
  - [2] 2026-10-28: access starts with a Hack Club sign-in | capture: sha256:81e952690fb038eafa3390a6926fdee42d22ead065274fc5511ed7d7dc5b8883 | quote: [Sign in with Hack Club](https://ai.hackclub.com/auth/login) [Read the docs](https://docs.ai.hackclub.com/)
  - [2] 2026-10-28: no credit card is needed | capture: sha256:81e952690fb038eafa3390a6926fdee42d22ead065274fc5511ed7d7dc5b8883 | quote: Every model on OpenRouter, plus image generation, embeddings, web search and OCR, behind one OpenAI-compatible API. No credit card.
  - [3] 2026-10-28: a third-party prober found the listing keyless and the chat call keyed | capture: sha256:34aa29edf68cc49c49bdcf1119b702b0c338ae9d71d2a58db4b4586122b9a223 | quote: Listing answers a bare GET with 200 and a full model catalogue; the chat call answers 401 Authentication required.
- sources:
  - [1] https://docs.ai.hackclub.com/guide/rules.html
  - [2] https://ai.hackclub.com/
  - [3] https://stillworks.supercapybara.com/free-llm-api-no-key
