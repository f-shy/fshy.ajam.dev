# Predibase

> predibase.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/predibase/ | JSON https://fshy.ajam.dev/api/v1/entity/predibase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Predibase

- `compute/predibase` | dead | evidence documented | binding none | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://predibase.com/pricing
- free tier: gone as an independent product. The pricing URL now lands on Rubrik Agent Cloud, an enterprise governance product, and Predibase became a wholly owned Rubrik subsidiary on 2025-06-24. There is no self-serve inference tier and no free credit to claim. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits note: nothing binds: there is no signup page, and the only route to the technology is a Rubrik enterprise sales conversation.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: the inference stack moved inside a data-protection product, so it composes with nothing a single person can hold.
- reliability: no reliability event recorded
- notes: A reader following an aggregator link now lands on an agent-governance page with a 'Get a demo' button and no price.
- extras:
  - facets.class: acquired
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the URL now serves rubrik.com/products/rubrik-agent-cloud: title 'AI Agent Operations Platform', heading 'Rubrik Agent Cloud', 'Control agents with AI using Rubrik Agent Cloud powered by SAGE', observed redirect
  - [2] 2026-10-22: 'On June 24, 2025, Rubrik, Inc. agreed to acquire Predibase, Inc. Following the acquisition, Predibase will be a wholly owned subsidiary of the Company', quoted from the Form 8-K
  - [3] 2026-10-22: 'Rubrik announced it has entered into an agreement to acquire Predibase to accelerate agentic AI adoption from pilot to production at scale', quoted
- sources:
  - [1] https://predibase.com/pricing
  - [2] https://www.sec.gov/Archives/edgar/data/1943896/000194389625000033/rbrk-20250624.htm
  - [3] https://www.rubrik.com/company/newsroom/press-releases/25/rubrik-to-acquire-predibase-to-accelerate-agentic-ai-adoption
