# g4f.space public provider routes

> g4f.space | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/g4f/ | JSON https://fshy.ajam.dev/api/v1/entity/g4f.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## g4f.space public provider routes (GPT4Free hosted)

- `inference/g4f-space-public-routes` | fails-quota | evidence reported | binding volume-quota | category inference gateway, anonymous, proof-of-work credits
- needs card no, phone no, ID no, institution no | verified 2026-10-28T04:36:18.974Z (live) | stale on 2026-11-12
- url https://g4f.space/api
- free tier: Five routes (/api/groq, /api/ollama, /api/pollinations, /api/nvidia, /api/gemini) are listed as none required for an API key, but a chat call answered 402 insufficient_credits asking for proof-of-work credits to earn anonymous usage | unit: mixed | metered on: unstated | read on: 2026-10-28 | source: [1] | note: the credit amount per call is not published; /v1 on the same host is listed as requiring a key from g4f.dev/api_key.html, though GET /v1/models answers 200 with no key
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: no key for the /api/<provider> routes per the g4f.dev table (none required); the price is proof-of-work credits rather than an identity
- interface: rest
- limits:
  - volume-quota (binding): a credit balance earned by proof-of-work: an anonymous chat call with none answers 402 insufficient_credits; the credits per call are unpublished [2]
- binding note: the proof-of-work credit balance gates every anonymous completion
- endpoint: https://g4f.space/api/groq/chat/completions
- tooling: any OpenAI-compatible client with base URL https://g4f.space/api/<provider>; the doc says to pass a placeholder key for SDKs that require one
- composes with: pairs with nothing until the credit scheme is understood: an anonymous call with no credit is refused
- reliability: GET /api/pollinations/models returns entries whose message is Error 404 DEPLOYMENT_NOT_FOUND on Vercel, and /api/auto/models returns 404; the groq, ollama, nvidia and gemini listings answer 200
- notes: the five routes front other providers (groq.com, ollama.com, pollinations.ai, nvidia.com, a hosted Gemini provider) and the listings carry per-model request counters; the routes differ in availability
- evidence note: the listings were read by GET; the 402 on a chat call comes from a third-party hourly prober that sends chat calls with no Authorization header. No completion was sent, because probe issues GET and HEAD only
- probe:
  - records[0].probe_id: g4fspace-groq-models-get
  - records[0].method: GET
  - records[0].url: https://g4f.space/api/groq/models
  - records[0].http: 200
  - records[0].authorization_sent: no
  - records[0].x_provider: groq.com
  - records[0].probed_at: 2026-10-28T04:45:03.814Z
  - records[0].chat_completion_tested: no
  - records[1].probe_id: g4fspace-ollama-models-get
  - records[1].method: GET
  - records[1].url: https://g4f.space/api/ollama/models
  - records[1].http: 200
  - records[1].x_provider: ollama.com
  - records[1].probed_at: 2026-10-28T04:45:07.696Z
  - records[2].probe_id: g4fspace-nvidia-models-get
  - records[2].method: GET
  - records[2].url: https://g4f.space/api/nvidia/models
  - records[2].http: 200
  - records[2].x_provider: nvidia.com
  - records[2].probed_at: 2026-10-28T04:45:14.311Z
  - records[3].probe_id: g4fspace-gemini-models-get
  - records[3].method: GET
  - records[3].url: https://g4f.space/api/gemini/models
  - records[3].http: 200
  - records[3].x_provider: gemini-v1beta
  - records[3].probed_at: 2026-10-28T04:45:15.622Z
  - records[4].probe_id: g4fspace-auto-models-get
  - records[4].method: GET
  - records[4].url: https://g4f.space/api/auto/models
  - records[4].http: 404
  - records[4].probed_at: 2026-10-28T04:45:16.863Z
- evidence:
  - [1] 2026-10-28: the g4f.dev table lists the groq route as needing no API key | capture: sha256:5d01eb3a56123e72a4d95acab02e0aabbbd05272284ed7bbf266ddfe118192ba | quote: | [https://g4f.space/api/groq](https://g4f.space/api/groq/models) | none required | Use Groq provider |
  - [2] 2026-10-28: a third-party prober got 402 insufficient_credits on a keyless chat call to the g4f.space routes | capture: sha256:34aa29edf68cc49c49bdcf1119b702b0c338ae9d71d2a58db4b4586122b9a223 | quote: 402 insufficient_credits: "No cake credits. Bake proof-of-work cakes ... to earn anonymous usage." Anonymous, but not free of charge -- the price is compute rather than a key.
  - [3] 2026-10-28: the keyless GET /api/groq/models answered 200 and proxied the groq.com listing | capture: sha256:e521739b851214e0f8fbcfa8555ed3384b53c8d6a6bccc054d305953295043a7 | quote: x-provider: groq.com
- sources:
  - [1] https://g4f.dev/docs/ready_to_use.html
  - [2] https://stillworks.supercapybara.com/free-llm-api-no-key
  - [3] https://g4f.space/api/groq/models
