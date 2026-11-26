# Mixlayer

> mixlayer.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixlayer/ | JSON https://fshy.ajam.dev/api/v1/entity/mixlayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mixlayer

- `inference/mixlayer` | qualifies-with-caveat | evidence documented | binding none | category inference platform, free model plus paid models
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://mixlayer.ai
- free tier: one model is free at USD 0 input and USD 0 output per million tokens, qwen/qwen3.5-4b-free (131,072 token context, text and image); all other listed models are paid; sign-up and an API key are required | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign-up at console.mixlayer.com and an API key from console.mixlayer.com/app/api-keys; no card or phone field is stated on the docs pages read
- interface: rest
- limits:
  - volume-quota: qwen/qwen3.5-4b-free is USD 0 per million input and output tokens; all other models carry positive rates [1]
- binding note: the free model has no published rate ceiling, so nothing binds above the working scale for it
- endpoint: https://models.mixlayer.ai/v1
- tooling: an OpenAI-compatible key plus the Mixlayer CLI and MCP server
- composes with: pairs with an OpenAI-compatible agent through the single $0 model; the scarce link is that only one small model is free
- reliability: no reliability event recorded
- notes: a genuine $0 model is listed in the first-party catalog; no separate quota for the free model is published on the page read.
- evidence:
  - [1] 2026-11-18: a free model at USD 0 input and output per million tokens | capture: sha256:c106230cc20d9f6d081328666b0857767e2fafce412d9e6386ab98838c3f8620 | quote: | `qwen/qwen3.5-4b-free` | 131,072 | $0 | $0 | Text, image |
  - [2] 2026-11-18: the API is OpenAI-compatible and sign-up plus an API key are required | capture: sha256:305104eb702310392b6e9b3a7eb1cf38b227a8c6491d9368e0e6feff44d52faf | quote: Mixlayer is an inference platform for open source AI models. We expose an OpenAI-compatible REST API, so you can drop Mixlayer into most existing applications by swapping the base URL and API key.
- sources:
  - [1] https://mixlayer.ai
  - [2] https://docs.mixlayer.com
