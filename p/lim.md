# Limrun

> lim.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lim/ | JSON https://fshy.ajam.dev/api/v1/entity/lim.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Limrun

- `compute/limrun` | paid-only | evidence reported | binding write-gated | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:22.000Z (live) | stale on 2026-11-06
- url https://lim.run
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: pricing is split between idle and active states; the page does not render the rates [1]
  - write-gated (binding): access is a console signup or a demo booking, with no free tier stated [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Documentation states pricing splits between idle and active; classification rests on the absence of a free tier.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: pricing is explicitly split between idle and active, so an idle machine has its own rate
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: an S3-backed cache keeps warm builds
  - ps.durability: S3-backed cache
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the cache is kept
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'keep warm builds with an S3-backed cache. Pricing is split between idle and' ... with an MCP server card and 'Sign up or log in' at console.limrun.com; the extracted body does not carry the price table
- sources:
  - [1] https://lim.run
