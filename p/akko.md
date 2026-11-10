# akkoma

> akko.wtf | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akko/ | JSON https://fshy.ajam.dev/api/v1/entity/akko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## akkoma / pleroma hosts as a distinct quota tier

- `storage/akkoma-pleroma-hosts-as-a-distinct-quota-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://akko.wtf/nodeinfo/2.0
- free tier: none reachable: Probed akko.wtf, cofe.rocks, pleroma.envs.net, spinster.xyz. The first three return `{"error":"Nodeinfo schema version not handled"}` on /nodeinfo/2.0 and no useful /api/meta; only spinster. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Probed akko.wtf, cofe.rocks, pleroma.envs.net, spinster.xyz. The first three return `{"error":"Nodeinfo schema version not handled"}` on /nodeinfo/2.0 and no useful /api/meta; only spinster.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Probed akko.wtf, cofe.rocks, pleroma.envs.net, spinster.xyz. The first three return `{"error":"Nodeinfo schema version not handled"}` on /nodeinfo/2.0 and no useful /api/meta; only spinster.
  - [2] 2026-10-21: cited as the basis of the rejection: Probed akko.wtf, cofe.rocks, pleroma.envs.net, spinster.xyz. The first three return `{"error":"Nodeinfo schema version not handled"}` on /nodeinfo/2.0 and no useful /api/meta; only spinster.
- sources:
  - [1] https://akko.wtf/nodeinfo/2.0
  - [2] https://spinster.xyz/api/v2/instance
