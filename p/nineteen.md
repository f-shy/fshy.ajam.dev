# Nineteen AI

> nineteen.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nineteen/ | JSON https://fshy.ajam.dev/api/v1/entity/nineteen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nineteen AI

- `compute/nineteen-ai` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:26.615Z (live) | stale on 2026-12-05
- url https://nineteen.ai/
- free tier: Bittensor subnet 19 (Rayon Labs) advertises Llama 3.1 8B at 'Less Than $0.00 / M Tokens', footnoted 'currently'. The app exposes an API key page and an OpenAI-compatible endpoint at api.nineteen.ai/v1. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - request-rate (binding): The price is zero while the subnet subsidises it; no limit is published, so the first real limit is an undocumented per-key rate limit and the second is the subsidy ending. [1]
- limits note: The price is zero while the subnet subsidises it; no limit is published, so the first real limit is an undocumented per-key rate limit and the second is the subsidy ending.
- binding note: the same as limits note
- interface detail: REST API: an OpenAI-style chat completions endpoint at https://api.nineteen.ai/v1/chat/completions with a bearer API key, documented at nineteen.ai/app/api with curl, Python SDK and JavaScript SDK examples.
- tooling: curl against https://api.nineteen.ai/v1/chat/completions; the API page lists Python SDK and JavaScript SDK examples.
- composes with: A free OpenAI-compatible endpoint is a drop-in for any agent loop that expects a base_url and a key, so it chains with local tooling without a gateway.
- reliability: no reliability event recorded
- notes: The 2026-05-18 capture is the quotable source and the live figure is only a search-index snippet. Whether signup needs an email alone or an OAuth account was not verified.
- extras:
  - facets.class: decentralized-free-inference
  - facets.free_tier_kind: perpetual
- evidence:
  - [2] 2026-10-22: Wayback capture of 2026-05-18 reads 'Llama 3.1 8b Less Than $0.00* / M Tokens * currently'
  - [3] 2026-10-22: search index of the live app on 2026-10-22 still shows 'Less Than $0.00 /M Tokens' and an operational status line
  - [4] 2026-10-22: API key page with a bearer token and an OpenAI-style chat/completions endpoint
  - [4] 2026-11-04: an HTTP chat-completions endpoint is documented with curl, Python and JavaScript SDK examples | capture: sha256:586036fd96310932330bd35958fe1526241d4b4b7986843ccdd2ca257d153f32 | quote: curl "https://api.nineteen.ai/v1/chat/completions"
  - [4] 2026-11-04: the API page documents an HTTP chat-completions endpoint with curl examples | capture: sha256:586036fd96310932330bd35958fe1526241d4b4b7986843ccdd2ca257d153f32 | quote: curl "https://api.nineteen.ai/v1/chat/completions"
- sources:
  - [1] https://nineteen.ai/
  - [2] https://web.archive.org/web/20260518235026/https://nineteen.ai/?provider=wayback
  - [3] https://app.sn19.ai/app
  - [4] https://nineteen.ai/app/api
