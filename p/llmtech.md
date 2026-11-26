# LLM Tech

> llmtech.eu | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/llmtech/ | JSON https://fshy.ajam.dev/api/v1/entity/llmtech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LLM Tech

- `inference/llmtech` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway (shared trial key)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://llmtech.eu/docs/
- free tier: Shared and rate-limited: 16 concurrent requests and 20M tokens per day per address, counted across prompt and completion and reset at 00:00 UTC. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: a shared public trial key is published in the docs; no signup or card to use it
- interface: rest
- limits:
  - volume-quota (binding): 20M tokens per day per address; 16 concurrent requests on the shared trial key [1]
- endpoint: https://api.llmtech.eu/v1
- composes with: The key is a real keyless read path for model inference, but it is shared and IP-counted; the demo page also runs with no key at all.
- reliability: the trial key is public and shared, so prompts are not private; a 429 with Retry-After appears at the concurrency limit
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: a public shared trial key serves 20M tokens per day per address with no card | capture: sha256:13a2e7cec34e5118fd58e5e41d32209a03954834f75ac2277349021f5c2d0dae | quote: Shared and rate-limited: 16 concurrent requests and 20M tokens per day per address, counted across prompt and completion and reset at 00:00 UTC.
- sources:
  - [1] https://llmtech.eu/docs/
