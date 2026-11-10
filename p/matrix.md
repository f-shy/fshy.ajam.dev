# Matrix media

> matrix.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/matrix/ | JSON https://fshy.ajam.dev/api/v1/entity/matrix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Matrix media repository (matrix.org homeserver)

- `storage/matrix-media-repository` | fails-quota | evidence reported | binding per-ip-shaping | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://matrix.org/homeserver/pricing/
- free tier: Free plan: 10 MB maximum per attachment, 100 MB of attachments per 24 hours, up to 500 MB per 28 days. Premium: 100 MB per attachment, 1 GB/24h, 5 GB/28d. Accounts not on any plan get 500 MB/24h up to 2 GB/28d. So the total is a few GB per month. Not a storage provider at all. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Egress itself is free ('the HTTPS data transfer to/from the matrix.org homeserver' does not count towards limits), but that is irrelevant at a 500 MB/28-day ingest rate. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-ip-shaping (binding): 1 GB/24h [1]
- limits note: Unauthenticated media download is deprecated and already frozen: the spec says servers SHOULD 'freeze' the old /_matrix/media/* endpoints so post-freeze uploads are only reachable via authenticated endpoints. Probed: matrix.org /_matrix/client/v1/media/config -> 401 M_MISSING_TOKEN, unauthenticated /_matrix/media/v3/download/... -> 404. So no anonymous CDN reads.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Excellent. The Content Repository API is a real spec, mxc:// URIs, every Matrix client library implements it. Self-hosted Synapse has no such caps (only max_upload_size, default 10M historically).
- composes with: Any federation of homeservers multiplies it, but you are then running the homeservers yourself, which is just 'buy a server'. On the public homeserver there is no chaining path: limits are per-account and the 28-day cap is the binding one.
- reliability: Stable, but the 28-day rolling cap means an upload-heavy workload simply stops. matrix.org also states pricing is not final and free users 'may be changed to a free plan in the future'.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan: 10 MB maximum per attachment, 100 MB of attachments per 24 hours, up to 500 MB per 28 days. Premium: 100 MB per attachment, 1 GB/24h, 5 GB/28d. Accounts not on any plan get 500 MB/24h up to 2 GB/28d. So the total is a few GB per month — not a storage provider at all.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Size of attachment that can be sent | 10MB maximum per attachment ... Total size of attachments | 100MB per 24 hours, up to 500MB per 28 days'
  - [2] 2026-10-21: 'The unauthenticated download endpoints have been deprecated ... servers SHOULD freeze'
  - [3] 2026-10-21: probe: GET -> 401 M_MISSING_TOKEN; unauth media download -> 404
- sources:
  - [1] https://matrix.org/homeserver/pricing/
  - [2] https://spec.matrix.org/latest/client-server-api/#content-repository
  - [3] https://matrix.org/_matrix/client/v1/media/config

## Matrix.org homeserver (media repository)

- `storage/matrix-org-homeserver` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://matrix.org/homeserver/pricing/
- free tier: Free plan: 10 MB max per attachment, 100 MB per 24 h, capped at 500 MB per 28 days. Premium: 100 MB per attachment, 1 GB/24 h up to 5 GB/28 days. Accounts not yet on a plan get fair-use 500 MB/24 h and 2 GB/28 days. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, no metered egress, and media is served through the homeserver so you can front it with Cloudflare. | metered: no
- identity: institution
- interface: rest
- limits note: Transfer is limited to 500 MB per 28 days on a rolling window. Uploads require authenticated media access. Anonymous requests return HTTP 404 on media download endpoints and HTTP 401 on unauthenticated client endpoints.
- interface detail: rest
- tooling: Matrix client-server API `/_matrix/media/v3/upload` and `/_matrix/client/v1/media/download`. Every SDK supports it (matrix-nio, matrix-js-sdk, mautrix-*); Element is the reference client.
- composes with: Federated: N accounts on N homeservers each get their own 500 MB/28-day allowance, and media federates across servers. But per-account throughput is the binding constraint, not the divisor.
- reliability: matrix.org introduced paid plans in 2025 and explicitly reserves the right to move existing users onto the free plan's tighter limits, so quotas can shrink under you. Synapse also purges unreferenced media.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan: 10 MB max per attachment, 100 MB per 24 h, capped at 500 MB per 28 days. Premium: 100 MB per attachment, 1 GB/24 h up to 5 GB/28 days. Accounts not yet on a plan get fair-use 500 MB/24 h and 2 GB/28 days.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Size of attachment that can be sent: 10MB maximum per attachment (Free) / Total size of attachments and data usage: 100MB per 24 hours, up to 500MB per 28 days (Free)'
  - [1] 2026-10-21: 'Data usage limit of 500MB per 24 hour period, up to a limit of 2GB per 28 days apply' (fair use, no plan)
  - [2] 2026-10-21: probe: GET -> 404 M_NOT_FOUND; GET https://matrix.org/_matrix/client/v1/media/download/matrix.org/abc -> 401 M_MISSING_TOKEN (authenticated media enforced)
- sources:
  - [1] https://matrix.org/homeserver/pricing/
  - [2] https://matrix.org/_matrix/media/v3/download/matrix.org/abc
