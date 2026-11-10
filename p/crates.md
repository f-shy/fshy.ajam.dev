# crates.io

> crates.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crates/ | JSON https://fshy.ajam.dev/api/v1/entity/crates.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## crates.io

- `storage/crates-io` | qualifies-with-caveat | evidence reported | binding pull-count | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://crates.io
- free tier: 10 MB per .crate file. No limit on versions per crate ('There is no limit to the number of versions which can be published'), no documented cap on total crates or total bytes per account. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Effectively permanent. 'the code cannot be deleted', 'publish is generally permanent'. | source: [1] | note: not stated
- egress: Free and unmetered, Cloudflare-fronted, CORS-open. Probe: static.crates.io .crate GET -> 200, Server: cloudflare, Cache-Control: 'public,max-age=31536000,immutable', Access-Control-Allow-Origin: *, Accept-Ranges: bytes. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - request-rate: 1000 downloads/month [1]
  - per-ip-shaping: 1.4 GB/day [1]
  - pull-count (binding): 1000 downloads/month [1]
- limits note: 10 MB per .crate. Publish rate: burst 5 new crates, then 1 per 10 min; burst 30 new versions, then 1 per minute (documented, leaky-bucket). No delete after 72h unless <1000 downloads/month-per-month AND no dependents AND single owner. Version numbers can never be reused or overwritten.
- binding note: a per-object fetch counter turns bulk distribution into a counting problem
- interface detail: rest
- tooling: PUT /api/v1/crates/new (binary metadata+body protocol), GET https://static.crates.io/crates/<name>/<name>-<ver>.crate. Clients: cargo publish, cargo-upload style wrappers. No rclone backend.
- composes with: UNBOUNDED on crates x versions but throttled hard: 5 new crates burst then 1 per 10 minutes; 30 versions burst then 1 per minute. At 10 MB/crate, 10 TiB needs ~1,048,576 crates. At 1 new crate per 10 min that is ~20 years, so crates.io is capacity-unlimited and throughput-useless for bulk. Use it as a low-priority shard, not the primary.
- reliability: Effectively permanent. 'the code cannot be deleted', 'publish is generally permanent'. Excellent durability, terrible write throughput: ~144 crates/day sustained, i.e. ~1.4 GB/day at 10 MB. Never disappears, but you cannot fill it fast.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'crates.io currently has a 10MB size limit on the .crate file'; 'There is no limit to the number of versions which can be published'; 'the version can never be overwritten, and the code cannot be deleted'
  - [2] 2026-10-21: 'allow a burst of 5 new crates published at once by a single user account, with a rate limit of 1 crate every 10 minutes'; 'burst of 30 new versions ... 1 crate per minute'
  - [3] 2026-10-21: deletion only if published <72h, or <1000 downloads per month published, and no dependents
  - [4] 2026-10-21: probe: GET -> 200, Content-Length: 58433, Server: cloudflare, Cache-Control: public,max-age=31536000,immutable
- sources:
  - [1] https://doc.rust-lang.org/cargo/reference/publishing.html
  - [2] https://crates.io/docs/rate-limits
  - [3] https://crates.io/policies
  - [4] https://static.crates.io/crates/serde/serde-1.0.0.crate

## iroh-n0des (crate)

- `storage/iroh-n0des` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://crates.io/crates/iroh-n0des
- free tier: none reachable: The old standalone rendezvous/discovery crate for 'p2p quic connections dialed by public key'. Superseded by the iroh 1.x address-lookup/pkarr path; repo README now just renders… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The old standalone rendezvous/discovery crate for 'p2p quic connections dialed by public key'. Superseded by the iroh 1.x address-lookup/pkarr path; repo README now just renders…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The old standalone rendezvous/discovery crate for 'p2p quic connections dialed by public key'. Superseded by the iroh 1.x address-lookup/pkarr path; repo README now just renders…
  - [2] 2026-10-21: cited as the basis of the rejection: The old standalone rendezvous/discovery crate for 'p2p quic connections dialed by public key'. Superseded by the iroh 1.x address-lookup/pkarr path; repo README now just renders iroh-service
- sources:
  - [1] https://crates.io/crates/iroh-n0des
  - [2] https://github.com/n0-computer/iroh-n0des
