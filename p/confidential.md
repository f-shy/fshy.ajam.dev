# Confidential AI

> confidential.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/confidential/ | JSON https://fshy.ajam.dev/api/v1/entity/confidential.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Confidential AI

- `inference/confidential-ai` | paid-only | evidence documented | binding volume-quota | category confidential inference endpoint, paid
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://confidential.ai/docs/inference-api/get-started
- free tier: no free tier: DeepSeek V4.1 Flash is listed at USD 0.30 input and USD 1.20 output per 1M tokens; a key is obtained by signing up and emailing the vendor | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up in the console, then email hello@confidential.ai for a key to the shared endpoint; self-serve console keys were not yet available at read time
- interface: rest
- limits:
  - volume-quota (binding): paid per-token rates (USD 0.30 in / USD 1.20 out per 1M) with no free allowance [2]
- binding note: no free tokens, so payment binds first
- endpoint: https://api.confidential.ai/v1
- tooling: an OpenAI-compatible client plus TEErminator for local verification of the upstream connection
- composes with: pairs with an OpenAI-compatible agent only through a vendor-issued key and a paid balance
- reliability: no reliability event recorded
- notes: key issuance requires emailing the vendor, and the API is paid per token.
- evidence:
  - [1] 2026-11-18: a key is obtained by signing up and emailing the vendor | capture: sha256:25c851615daaed82f01d49cd4ae1e65d2ee8730a42db8bf2fad08291c0c138ae | quote: Sign up in the [console](https://console.confidential.ai/), then email [hello@confidential.ai](mailto:hello@confidential.ai) for a key to the shared endpoint.
- sources:
  - [1] https://confidential.ai/docs/inference-api/get-started
  - [2] https://confidential.ai
