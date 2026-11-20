# mini.biz.id

> mini.biz.id | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mini/ | JSON https://fshy.ajam.dev/api/v1/entity/mini.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mini.biz.id

- `compute/mini-biz-id` | dead | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://mini.biz.id/
- free tier: Withdrawn. The site published a 'Micro 1' plan at 'Rp0/mo, Free forever' with 750 MB of space, SSH, HTTP and WebSocket over a shared public IPv4, and now resolves to a domain-for-sale parking page. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: ssh
- limits note: Nothing is available: the domain is listed for sale on a parking page, so there is no service behind the offer.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None: the service is gone.
- reliability: no reliability event recorded
- notes: Documented so the subsequent evaluation does not chase it. The pattern is worth noting because it recurred twice among evaluated offerings: an Indonesian free-VPS hobby project with a real spec sheet that has since lapsed. The honest evidence here is contradictory, since automated retrieval served cached page text while the live route went to a for-sale page, so the death is inferred from the parking redirect plus the TLS name mismatch rather than from a stated closure.
- extras:
  - facets.class: regional-vps
  - facets.free_tier_kind: none
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the host now redirects to 'pulaudomain.com/forsale/mini-biz-id', a domain marketplace listing for mini.biz.id, read; the probe failed TLS with TLSV1_UNRECOGNIZED_NAME, consistent with a parked or reassigned certificate
  - [1] 2026-10-22: 
- sources:
  - [1] https://mini.biz.id/
