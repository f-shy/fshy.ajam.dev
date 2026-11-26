# Thinking Machines

> thinkingmachines.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thinkingmachines/ | JSON https://fshy.ajam.dev/api/v1/entity/thinkingmachines.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Thinking Machines

- `inference/thinkingmachines` | paid-only | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://tinker-docs.thinkingmachines.ai/tinker/compatible-apis/anthropic/
- free tier: No free text allowance stated; Tinker offers Anthropic-compatible inference using a Tinker API key, with production throughput via a waitlist. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Tinker API key; signup fields not detailed on this page
- interface: rest
- limits:
  - write-gated (binding): waitlist for production inference throughput [1]
- endpoint: https://tinker.thinkingmachines.dev/services/tinker-prod/anthropic/api/v1
- tooling: Anthropic SDK by overriding the base URL and API key
- composes with: no free tier; a waitlist gates higher or more stable production throughput
- reliability: prompt caching is unsupported and thinking-block signatures are empty
- notes: No free tier on the compatible-API page; usage requires a Tinker API key.
- evidence:
  - [1] 2026-11-18: Tinker requires an API key and offers a production waitlist | capture: sha256:9d0593859eb32054366052523a4fd1100dc0401df4054269c36b8012771012d8 | quote: For higher or more stable throughput, or guidance on large-scale setups, [join our waitlist for production inference]
- sources:
  - [1] https://tinker-docs.thinkingmachines.ai/tinker/compatible-apis/anthropic/
