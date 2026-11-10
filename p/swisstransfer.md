# SwissTransfer

> swisstransfer.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swisstransfer/ | JSON https://fshy.ajam.dev/api/v1/entity/swisstransfer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SwissTransfer (Infomaniak)

- `storage/swisstransfer` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.swisstransfer.com
- free tier: 50 GB per transfer, all files combined, no account required. Hosted in Infomaniak's own Swiss datacentres. One notable global property: the source is open (Infomaniak android/iOS/multiplatform clients on GitHub) and there is a working CLI. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 50 GB | bytes: 50000000000 | source: [1] | note: not stated
- retention: Retention: 15 days by default; 30 only if the SENDER accepts an extension email on day 12 (offer open 3 days) | days: 15 | source: [1] | note: not stated
- egress: Unmetered, no egress pricing published; direct download links plus a 'Download All' ZIP (ZIP is capped. Above 10 GB you must fetch files one by one). | metered: no
- identity: institution
- interface: rest, cli
- limits:
  - retention-clamped: Retention: 15 days [1]
  - retention-clamped: deletes at 15 days [1]
  - per-object-cap (binding): per-object-cap: 50 GB [1]
- limits note: Per-object-cap: 50 GB per transfer (combined, not per file). Retention: 15 days by default; 30 only if the SENDER accepts an extension email on day 12 (offer open 3 days). After expiry Infomaniak states a link cannot be reactivated or extended. pull-count: download cap selectable at 1/20/100/250. 'unlimited' requires a paid plan. Request-rate: the container-create endpoint enforces a reCAPTCHA field (see reliability note).
- interface detail: rest
- tooling: Swissfer (github.com/Blutsh/swissfer, 44 stars, pushed 2026-10-21). Rust CLI, upload AND download, email-confirmed sender. First upload requires a 6-character code emailed to you, then cached. Upstream `send`-style clients do not work.
- composes with: Per-transfer 50 GB x unlimited transfers. With swissfer this is scriptable, so capacity is bounded by how many 50 GB transfers you are willing to mint, each living 15-30 days.
- reliability: The write path requires human verification at the API: POST /api/containers without a recaptcha field returns 400 'The recaptcha field is required. (and 1 more error)'. swissfer routes around this with an emailed 6-char confirmation, not with a token. The 30-day option is a trap. It silently deletes at 15 days unless the sender acts on day 12.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '50 GB', retention table, download caps, 'cannot be reactivated or extended'
  - [2] 2026-10-21: probe: POST -> 400 {'message':'The recaptcha field is required. (and 1 more error)'}
  - [3] 2026-10-21: (Oct 2026) — independent confirmation of the day-12 extension mechanics
- sources:
  - [1] https://www.infomaniak.com/en/support/faq/2929/understanding-swisstransfer-data-limits
  - [2] https://www.swisstransfer.com/api/containers
  - [3] https://linkinseconds.com/blog/swisstransfer-limits
