# Gofile

> gofile.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gofile/ | JSON https://fshy.ajam.dev/api/v1/entity/gofile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gofile

- `storage/gofile` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-11T02:59:10.169Z (live) | stale on 2026-11-26
- url https://gofile.io
- free tier: Free accounts are capped at 10,000 stored contents — uploads past the cap fail with `error-limits`. | unit: objects | metered on: object-count | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Content is kept for 10 days of inactivity, and stays longer as long as it keeps being downloaded. | source: [1] | note: not stated
- egress: 100 GB traffic / 30 days | metered: no
- identity: anonymous | detail: No account required.
- interface: rest, rclone
- limits:
  - retention-clamped (binding): Content is kept for 10 days of inactivity, and stays longer as long as it keeps being downloaded. [1]
- limits note: content is deleted after 10 days of inactivity unless it keeps being downloaded; past the storage period content may be moved to cold storage and importing it back requires Premium; most API endpoints (listing, direct links) return error-notPremium; 'Repeatedly exceeding rate limits may result in automatic IP bans'
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: REST API at api.gofile.io (documented, CORS, per-endpoint rate limits); rclone backend 'gofile' (Tier 1) but its docs warn 'if you wish to connect rclone to Gofile you will need a premium account'; guest account creation is a single unauthenticated POST
- composes with: Unlimited guest accounts created by API call (no email, no human-verification step) x 10,000 files each. Probe-verified; each guest account also brings its own 100 GB/30-day traffic bucket, so fetch load can be sharded by account.
- reliability: 10-day inactivity expiry plus cold-storage migration makes it storage-with-a-TTL, not a drive; content-count cap (10k) bites hard on many-small-file datasets
- notes: No storage figure at all on the free tier. Free accounts get temporary storage with a 10,000-content cap per account ('Free accounts are capped at 10,000 stored contents'); free traffic allowance is '100 GB traffic / 30 days'.
- evidence note: the API page states the 10,000-content cap on a free account
- evidence:
  - [2] 2026-10-21: 'Content is kept for 10 days of inactivity', 'Content past its storage period may be moved to cold storage', free traffic counted per IP
  - [3] 2026-10-21: 'Free accounts are capped at 10,000 stored contents', error-limits/error-notPremium statuses, rate limits per IP and per account
  - [4] 2026-10-21: probe: POST (no auth) -> {"status":"ok","data":{"tier":"guest","token":"DtZGU7IXTjUXIor2UTCc8LwVuuELs1e7"}} (unlimited anonymous identities, one HTTP call each)
  - [5] 2026-10-21: probe: POST (no token) -> 200, file stored, downloadPage https://gofile.io/d/nxWCc29o; later GET api.gofile.io/contents/nxWCc29o with the guest token -> {"status":"error-notPremium"}
  - [3] 2026-11-09: the free tier is metered on the number of stored contents | capture: sha256:e5e8274d2efae8b0da1ac174342253647bb822a32afd4f6decf1769531e57489 | quote: Free accounts are capped at 10,000 stored contents — uploads past the cap fail with `error-limits`.
  - [2] 2026-11-09: content survives 10 days of inactivity and longer while it is downloaded | capture: sha256:bcf53f25fbf9b540c33a6a6b133fc9831b6360ad119451ab35288808059f379d | quote: Content is kept for 10 days of inactivity, and stays longer as long as it keeps being downloaded.
  - [1] 2026-11-09: the free plan includes 100 GB of traffic per 30 days | capture: sha256:88056ef8a6bebf9334b7cece8791b49d9aa4a4d32bd388fe99a52e1aadca79ae | quote: 100 GB traffic / 30 days
  - [1] 2026-11-09: the page states the free plan requires no account | capture: sha256:88056ef8a6bebf9334b7cece8791b49d9aa4a4d32bd388fe99a52e1aadca79ae | quote: No account required
  - [3] 2026-11-09: the page states the free-account content cap | capture: sha256:e5e8274d2efae8b0da1ac174342253647bb822a32afd4f6decf1769531e57489 | quote: Free accounts are capped at 10,000 stored contents
  - [2] 2026-11-11: the page states content is kept for 10 days of inactivity and stays longer while it keeps being downloaded | capture: sha256:98b208baa451ae772fcc8a5d5030008fae04fa1d8a9510c6bcdbd8744835612a | quote: Content is kept for <strong class="font-semibold text-slate-200">10 days</strong> of inactivity, and stays longer as long as it keeps being downloaded.
- sources:
  - [1] https://gofile.io/premium
  - [2] https://gofile.io/faq
  - [3] https://gofile.io/api
  - [4] https://api.gofile.io/accounts
  - [5] https://store4.gofile.io/contents/uploadfile
