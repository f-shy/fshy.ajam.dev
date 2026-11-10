# Gofile

> gofile.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gofile/ | JSON https://fshy.ajam.dev/api/v1/entity/gofile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gofile

- `storage/gofile` | qualifies-with-caveat | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gofile.io
- free tier: No storage figure at all on the free tier. Free accounts get temporary storage with a 10,000-content cap per account ('Free accounts are capped at 10,000 stored contents'); free traffic allowance is '100 GB traffic / 30 days'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 30 days' | content is deleted after 10 days of inactivity unless it keeps being downloaded; past the storage period content may be moved to cold storage and importing it back requires Premium; most API endpoints (listing, direct links) return error-notPremium; 'Repeatedly exceeding rate limits may result in automatic IP bans' | days: 30 | source: [1] | note: not stated
- egress: free plan: '100 GB traffic / 30 days'; 'We never throttle bandwidth' but traffic over the allowance restricts download functionality. Premium removes caps entirely | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - retention-clamped (binding): deleted after 10 days [1]
- limits note: content is deleted after 10 days of inactivity unless it keeps being downloaded; past the storage period content may be moved to cold storage and importing it back requires Premium; most API endpoints (listing, direct links) return error-notPremium; 'Repeatedly exceeding rate limits may result in automatic IP bans'
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: REST API at api.gofile.io (documented, CORS, per-endpoint rate limits); rclone backend 'gofile' (Tier 1) but its docs warn 'if you wish to connect rclone to Gofile you will need a premium account'; guest account creation is a single unauthenticated POST
- composes with: Unlimited guest accounts created by API call (no email, no human-verification step) x 10,000 files each. Probe-verified; each guest account also brings its own 100 GB/30-day traffic bucket, so fetch load can be sharded by account.
- reliability: 10-day inactivity expiry plus cold-storage migration makes it storage-with-a-TTL, not a drive; content-count cap (10k) bites hard on many-small-file datasets
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Content is kept for 10 days of inactivity', 'Content past its storage period may be moved to cold storage', free traffic counted per IP
  - [3] 2026-10-21: 'Free accounts are capped at 10,000 stored contents', error-limits/error-notPremium statuses, rate limits per IP and per account
  - [4] 2026-10-21: probe: POST (no auth) -> {"status":"ok","data":{"tier":"guest","token":"DtZGU7IXTjUXIor2UTCc8LwVuuELs1e7"}} (unlimited anonymous identities, one HTTP call each)
  - [5] 2026-10-21: probe: POST (no token) -> 200, file stored, downloadPage https://gofile.io/d/nxWCc29o; later GET api.gofile.io/contents/nxWCc29o with the guest token -> {"status":"error-notPremium"}
- sources:
  - [1] https://gofile.io/premium
  - [2] https://gofile.io/faq
  - [3] https://gofile.io/api
  - [4] https://api.gofile.io/accounts
  - [5] https://store4.gofile.io/contents/uploadfile
