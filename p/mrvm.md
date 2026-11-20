# MrVM

> mrvm.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mrvm/ | JSON https://fshy.ajam.dev/api/v1/entity/mrvm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MrVM

- `compute/mrvm` | dead | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://mrvm.net/
- free tier: The cheapest entry on the largest price-sorted hosting list, dalisoft/awesome-hosting, is 'MrVM | LXC-256 (EUR 0.5/m) | no trial | no free tier'. The vendor site does not carry that product today: https://mrvm.net returns a placeholder reading 'MrVM is preparing for some exciting changes. Updates will follow soon.' and the plan URL https://mrvm.net/lxc returns HTTP 404. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits note: no plan page exists to measure, so nothing can be said about what would bind.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing to chain: with no plan page there is no product to buy.
- reliability: no reliability event recorded
- notes: The EUR 0.50 figure is not necessarily false, only unsupported today: the legacy client portal at clients.mrvm.net is still linked, so existing customers may still be served. What is established is that a new customer cannot see or order that plan from the public site on 2026-10-22.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the site returns a placeholder: 'MrVM is preparing for some exciting changes. Updates will follow soon.', quoted, with upstream status 200
  - [2] 2026-10-22: HTTP 404 with body '404 Not Found / nginx' for the plan URL the aggregator cites
  - [3] 2026-10-22: the aggregator's VPS table lists 'MrVM | LXC-256 (EUR 0.5/m) | No | No' as its cheapest row, quoted
- sources:
  - [1] https://mrvm.net/
  - [2] https://mrvm.net/lxc
  - [3] https://raw.githubusercontent.com/dalisoft/awesome-hosting/master/README.md
