# Sakana AI

> sakana.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sakana/ | JSON https://fshy.ajam.dev/api/v1/entity/sakana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Sakana AI

- `inference/sakana` | paid-only | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://console.sakana.ai/models
- free tier: No free text allowance stated; Fugu models bill per token (Fugu Max USD 2 input / USD 6 output per 1M) and Fugu Cyber is pay-as-you-go only with a manual access request. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an API key and, for Fugu Cyber, a submitted access request with verified contact information
- interface: rest
- limits:
  - write-gated (binding): Fugu Cyber requires a manual access request form and approval [1]
  - volume-quota: Fugu Max USD 2/M input, USD 6/M output [1]
- endpoint: https://api.sakana.ai/v1
- tooling: OpenAI SDK (Responses, Chat Completions) and Anthropic SDK (Messages)
- composes with: no free tier; Fugu Cyber additionally requires a reviewed access request
- reliability: Fugu Cyber output pricing is 40-60% below comparable frontier models but still paid
- notes: -
- evidence:
  - [1] 2026-11-18: Fugu Cyber requires a reviewed access request and pay-as-you-go billing | capture: sha256:371063305030b0ab5960883ed0635e0aa9ae9639cae73e3e9f2e8ffe0234d11d | quote: In order to use Fugu Cyber, users must submit an access request
- sources:
  - [1] https://console.sakana.ai/models
