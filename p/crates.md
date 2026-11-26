# crates.io

> crates.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crates/ | JSON https://fshy.ajam.dev/api/v1/entity/crates.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## crates.io

- `storage/crates-io` | qualifies-with-caveat | evidence reported | binding request-rate | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-25T04:14:17.957Z (live) | stale on 2026-12-10
- url https://crates.io
- free tier: crates.io currently has a 10MB size limit on the `.crate` file. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per .crate file | source: [1] | note: the Cargo publishing reference states a 10MB size limit on the .crate file
- retention: The version can never be overwritten, and the code cannot be deleted. | source: [1] | note: a published version can never be overwritten and the code cannot be deleted; crates.io aims to be a permanent archive, with conditional owner deletion described in the policies
- egress: Free and unmetered, Cloudflare-fronted, CORS-open. Probe: static.crates.io .crate GET -> 200, Server: cloudflare, Cache-Control: 'public,max-age=31536000,immutable', Access-Control-Allow-Origin: *, Accept-Ranges: bytes. | metered: no
- identity: email | detail: An email address must be provided and verified on the Account Settings page.
- interface: rest, rclone
- limits:
  - request-rate (binding): 1 new crate every 10 minutes after a burst of 5 new crates [2]
  - request-rate (binding): 1 new version per minute after a burst of 30 new versions [2]
  - retention-clamped: deletion only if published under 72 hours or single owner and fewer than 1000 downloads per month since publication, and no other crate depends on it [3]
- limits note: 10 MB per .crate. Publish rate: burst 5 new crates, then 1 per 10 min; burst 30 new versions, then 1 per minute (documented, leaky-bucket). No delete after 72h unless <1000 downloads/month-per-month AND no dependents AND single owner. Version numbers can never be reused or overwritten.
- binding note: rate limits apply to publishing new crates and new versions
- interface detail: rest
- tooling: PUT /api/v1/crates/new (binary metadata+body protocol), GET https://static.crates.io/crates/<name>/<name>-<ver>.crate. Clients: cargo publish, cargo-upload style wrappers. No rclone backend.
- composes with: UNBOUNDED on crates x versions but throttled hard: 5 new crates burst then 1 per 10 minutes; 30 versions burst then 1 per minute. At 10 MB/crate, 10 TiB needs ~1,048,576 crates. At 1 new crate per 10 min that is ~20 years, so crates.io is capacity-unlimited and throughput-useless for bulk. Use it as a low-priority shard, not the primary.
- reliability: Effectively permanent. 'the code cannot be deleted', 'publish is generally permanent'. Excellent durability, terrible write throughput: ~144 crates/day sustained, i.e. ~1.4 GB/day at 10 MB. Never disappears, but you cannot fill it fast.
- notes: 10 MB per .crate file. No limit on versions per crate ('There is no limit to the number of versions which can be published'), no documented cap on total crates or total bytes per account.
- evidence note: the Cargo publishing page states a 10MB size limit on the .crate file
- evidence:
  - [1] 2026-10-21: 'crates.io currently has a 10MB size limit on the .crate file'; 'There is no limit to the number of versions which can be published'; 'the version can never be overwritten, and the code cannot be deleted'
  - [2] 2026-10-21: 'allow a burst of 5 new crates published at once by a single user account, with a rate limit of 1 crate every 10 minutes'; 'burst of 30 new versions ... 1 crate per minute'
  - [3] 2026-10-21: deletion only if published <72h, or <1000 downloads per month published, and no dependents
  - [4] 2026-10-21: probe: GET -> 200, Content-Length: 58433, Server: cloudflare, Cache-Control: public,max-age=31536000,immutable
  - [1] 2026-11-09: a .crate file is capped at 10MB | capture: sha256:df52936a811167cd36d1f5986b35e743facfbca0244ab36f01066226d564a971 | quote: [crates.io](https://crates.io/) currently has a 10MB size limit on the `.crate` file.
  - [1] 2026-11-09: a published version can never be overwritten or deleted | capture: sha256:df52936a811167cd36d1f5986b35e743facfbca0244ab36f01066226d564a971 | quote: The version can never be overwritten, and the code cannot be deleted.
  - [1] 2026-11-09: an email address must be provided and verified | capture: sha256:df52936a811167cd36d1f5986b35e743facfbca0244ab36f01066226d564a971 | quote: You will also need to provide and verify your email address on the [Account Settings](https://crates.io/settings/profile) page.
  - [2] 2026-11-09: new-crate publishing allows a burst of 5, then 1 crate every 10 minutes | capture: sha256:275493e8f5665053f4774b267a2e4f542027ca1d3f72007909f16af4d3dc0035 | quote: For brand new crate publishes, allow a burst of 5 new crates published at once by a single user account, with a rate limit of 1 crate every 10 minutes allowed after that burst
  - [2] 2026-11-09: new-version publishing allows a burst of 30, then 1 version per minute | capture: sha256:275493e8f5665053f4774b267a2e4f542027ca1d3f72007909f16af4d3dc0035 | quote: For new versions of existing crates, allow a burst of 30 new versions published at once by a single user account, with a rate limit of 1 crate per minute allowed after that burst
  - [3] 2026-11-09: deletion requires publication under 72 hours or a single owner, fewer than 1000 downloads per month since publication, and no dependents | capture: sha256:3398843ae7e55b69fe7c80f1c555eb3fd7a8ef266353b2a7c2f4265f3b08fc35 | quote: Crate owners can delete their crates under certain conditions: the crate has been published for less than 72 hours, or the crate only has a single owner, the crate has been downloaded less than 1000 times for each month it has been published, and the crate is not depended upon by any other crate on crates.io.
  - [2] 2026-11-09: rate limits apply to publishing new crates and new versions | capture: sha256:275493e8f5665053f4774b267a2e4f542027ca1d3f72007909f16af4d3dc0035 | quote: Crates.io has rate limits on publishes of new crates and publishes of new versions of existing crates to mitigate
  - [1] 2026-11-25: a published .crate file is capped at 10MB | capture: sha256:2815047d35b140fe686be84265e216e6766c068eb77bce24c6cd766bc7c57615 | quote: [crates.io](https://crates.io/) currently has a 10MB size limit on the `.crate` file.
  - [1] 2026-11-25: published code is retained permanently and cannot be deleted or overwritten | capture: sha256:2815047d35b140fe686be84265e216e6766c068eb77bce24c6cd766bc7c57615 | quote: The version can never be overwritten, and the code cannot be deleted.
  - [1] 2026-11-25: the Cargo reference still states the 10MB .crate limit | capture: sha256:2815047d35b140fe686be84265e216e6766c068eb77bce24c6cd766bc7c57615 | quote: [crates.io](https://crates.io/) currently has a 10MB size limit on the `.crate` file.
- sources:
  - [1] https://doc.rust-lang.org/cargo/reference/publishing.html
  - [2] https://crates.io/docs/rate-limits
  - [3] https://crates.io/policies
  - [4] https://static.crates.io/crates/serde/serde-1.0.0.crate

## iroh-n0des (crate)

- `storage/iroh-n0des` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:05.854Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: the iroh-n0des crate is an iroh protocol library, not a hosted byte-storage service | capture: sha256:5fd03f045f85fb00652c1c798e97e4d23c7071c8308f2ff6e4239304bbed91aa | quote: An iroh protocol to interact with n0des, using iroh itself.
  - [2] 2026-11-19: the iroh-n0des repository now presents itself as the iroh-services client | capture: sha256:7a9c6c34aa6962674684e42d160c2eb59d18072ebd39f7c33242f3ec07a7abd9 | quote: An iroh protocol to interact with iroh-services, using iroh itself.
- sources:
  - [1] https://crates.io/crates/iroh-n0des
  - [2] https://github.com/n0-computer/iroh-n0des
