# akkoma

> akko.wtf | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/akko/ | JSON https://fshy.ajam.dev/api/v1/entity/akko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## akkoma / pleroma hosts as a distinct quota tier

- `storage/akkoma-pleroma-hosts-as-a-distinct-quota-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.938Z (inherited) | stale on 2026-12-04
- url https://akko.wtf/nodeinfo/2.0
- free tier: none reachable: Probed akko.wtf, cofe.rocks, pleroma.envs.net, spinster.xyz. The first three return `{"error":"Nodeinfo schema version not handled"}` on /nodeinfo/2.0 and no useful /api/meta; only spinster. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: no stated per-object cap; https://akko.wtf/nodeinfo/2.0 answered HTTP 404 on 2026-11-19 (body: Nodeinfo schema version not handled; routes tried: direct capture, pinned jina-keyless, pinned cfbr, fetch --dump-headers, probe) | source: [1] | note: not applicable
- retention: unverified: no stated retention; https://akko.wtf/nodeinfo/2.0 answered HTTP 404 on 2026-11-19 (body: Nodeinfo schema version not handled; routes tried: direct capture, pinned jina-keyless, pinned cfbr, fetch --dump-headers, probe) | source: [1]
- egress: unverified: no stated egress terms; https://akko.wtf/nodeinfo/2.0 answered HTTP 404 on 2026-11-19 (body: Nodeinfo schema version not handled; routes tried: direct capture, pinned jina-keyless, pinned cfbr, fetch --dump-headers, probe) | metered: no
- identity: email
- interface: unknown
- interface detail: unverified: no stated interface; https://akko.wtf/nodeinfo/2.0 answered HTTP 404 on 2026-11-19 (body: Nodeinfo schema version not handled; routes tried: direct capture, pinned jina-keyless, pinned cfbr, fetch --dump-headers, probe)
- tooling: not documented
- composes with: unverified: no stated chaining; https://akko.wtf/nodeinfo/2.0 answered HTTP 404 on 2026-11-19 (body: Nodeinfo schema version not handled; routes tried: direct capture, pinned jina-keyless, pinned cfbr, fetch --dump-headers, probe)
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
  - probe:https://akko.wtf/nodeinfo/2.0 2026-11-19: the nodeinfo endpoint returns a schema-version error and exposes no storage quota | capture: sha256:e2ed0b619020bb683dbdebcf6f66c49445e70fea87bf312dbd8fe27b81efb5ab | quote: {"error":"Nodeinfo schema version not handled"}
  - probe:https://spinster.xyz/api/v2/instance 2026-11-19: the reachable host publishes per-attachment size limits but no general storage quota | capture: sha256:a50b5c90963a5063b2ec58cd3b2fce821f99ee2bf21cc9b9676bca547df1e9e7 | quote: "image_size_limit":100000000,"video_size_limit":100000000
  - probe:https://akko.wtf/nodeinfo/2.0 2026-11-19: the first-party nodeinfo endpoint answered HTTP 404 on 2026-11-19 | capture: sha256:b91d840f1917e9e1e91647630889ab9e3797f4a6b55af1965d3f138f6012ba41 | quote: "status": 404
- sources:
  - [1] https://akko.wtf/nodeinfo/2.0
  - [2] https://spinster.xyz/api/v2/instance
