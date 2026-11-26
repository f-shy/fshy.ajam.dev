# joule

> github.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-f00-sh/ | JSON https://fshy.ajam.dev/api/v1/entity/github-f00-sh.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## joule

- `compute/joule` | self-hosted, last resort | verdict fails-quota | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-25T05:18:12.886Z (live) | stale on 2026-12-26
- url https://github.com/f00-sh/joule
- free tier: Free access is real but is earned by contributing hardware. The API is 'earned only by contributing compute — free on the public pool (no cash)', under 'an auditable fairness algorithm (√VRAM, tenure boost, leecher penalties)'. Millijoules are minted from 'verified contribution (heartbeats, shards, challenges), scaled fairly'; 'No live contribution / balance ⇒ no access.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: contribution-earned
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: rest
- limits:
  - write-gated (binding): Access requires proving donated GPU contribution first, so the binding constraint is hardware, which the analysis assumes is absent. A CPU-only node is documented as 'lab only'. [1]
- limits note: Access requires proving donated GPU contribution first, so the binding constraint is hardware, which the analysis assumes is absent. A CPU-only node is documented as 'lab only'.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None. The exchange rate is compute for compute, so a user with no compute to offer has nothing to trade.
- reliability: no reliability event recorded
- notes: Documented because it is the cleanest statement of a pattern that recurs across this class: a pool that is free in dollars but priced in donated compute. Gensyn does the same with testnet points, and Dreamify does it with somebody else's 4090s. Without owned hardware, 'no cash buy-in' is not the same as 'reachable'.
- self hosted: yes
- extras:
  - facets.class: community-compute-pool
  - facets.free_tier_kind: contribution-earned
- evidence:
  - [1] 2026-10-22: quoted: 'Access to the OpenAI-compatible API is earned only by contributing compute - free on the public pool (no cash)'; 'No live contribution / balance => no access'; CPU 'works for lab only'
  - [2] 2026-10-22: quoted: '100% free - no money - peer-seeded - website only'; 'You bring the watts'; millijoules are 'a sealed ledger of what you give in'
  - [1] 2026-11-25: API access is free on the public pool but earned only by contributing compute, and credits are millijoules under a fairness algorithm | capture: sha256:06fe673873400463f11f0dab83add5ae56e32d900f22cdcc982c5b1c2b22f819 | quote: Access to the OpenAI-compatible API is earned only by contributing compute — free on the public pool (no cash).
  - [1] 2026-11-25: the README still states API access is earned by contributing compute, free on the public pool, with millijoules under a fairness algorithm | capture: sha256:06fe673873400463f11f0dab83add5ae56e32d900f22cdcc982c5b1c2b22f819 | quote: Access to the OpenAI-compatible API is earned only by contributing compute — free on the public pool (no cash).
- sources:
  - [1] https://github.com/f00-sh/joule
  - [2] https://joule.f00.sh/
