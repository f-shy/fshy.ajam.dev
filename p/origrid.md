# Origrid

> origrid.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/origrid/ | JSON https://fshy.ajam.dev/api/v1/entity/origrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Origrid

- `storage/origrid` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anon-host
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://origrid.io
- free tier: 25 GB per file with NO account; 50 GB per file / 50 GB storage with a free account; Contributor tier (automatic: 25 GB stored + 30 days old + clean record) gives 100 GB storage, 50 GB/file and links that never expire; Verified Uploader = 100 GB/file + 5 TB storage + links that never expire. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 25 GB per file | bytes: 25000000000 | source: [1] | note: not stated
- retention: Retention: 15 days anonymous, 90 days from last download for a free account, never for Contributor/Plus | days: 15 | source: [1] | note: not stated
- egress: No ads, no wait, no cap, full speed on every plan; no per-download bandwidth meter stated. Bytes are served from R2/B2 origins via short-lived signed URLs. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 25 GB per file [1]
  - per-object-cap (binding): 50 GB per file [1]
  - retention-clamped: Retention: 15 days [1]
  - write-gated: invite-only Verified tier [1]
- limits note: per-object-cap: 25 GB/file anonymous, 50 GB/file free account. Retention: 15 days anonymous, 90 days from last download for a free account, never for Contributor/Plus. Storage cap is the real bind: 50 GB free account, 100 GB Contributor, 5 TB only on the invite-only Verified tier.
- interface detail: rest
- tooling: Own REST API, documented and keyless for the anonymous path. /api/upload/create, /api/upload/part, /api/upload/complete. Remote-upload endpoint POST /api/upload/remote pulls a URL server-side (no local bandwidth).
- composes with: Anonymous upload needs no key at all, so per-identity multiplication is free; but each anon file lives only 15 days from last download. The interesting route is the automatic Contributor tier: park 25 GB, wait 30 days, and links stop expiring (100 GB). A slow-burn archive, not a hot tier.
- reliability: READ PATH IS GATED BY A MINTED TOKEN, not a static URL: /d/<id> is HTML whose Download button is a signed /dl/<JWT> that 302s to an R2 presigned URL with X-Amz-Expires=21600. The token is re-minted on every page view, so the file is durable but the link is not shareable as a bytes URL. You must re-scrape /d/<id> to fetch. Retains originals byte-exact.
- notes: the same as the free tier
- evidence:
  - withheld 2026-10-21: probe: POST /api/upload/create (no auth) -> 200 {fileId, key, uploadId, partSize 67108864, claimToken}
  - withheld 2026-10-21: probe: PUT presigned part -> 200; POST /api/upload/complete -> {"id":"BbSXVbzMZ","status":"processing","url":"/d/BbSXVbzMZ"}
  - withheld 2026-10-21: probe: GET /d/BbSXVbzMZ -> 200 text/html; GET signed /dl/... -> 302 -> R2 presigned (X-Amz-Expires=21600); final GET 200 1048576 bytes, sha256 MATCH a60c67af...69a3a
  - withheld 2026-10-21: probe: GET /api/v1/files without key -> 401 {"message":"Invalid API key."}
- sources:
  - [1] https://origrid.io/pricing

## storj / sia / origrid / swisstransfer / transfer.it

- `storage/storj-sia-origrid-swisstransfer-transfer-it-fails-quota` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T01:28:45.679Z (inherited) | stale on 2026-11-18
- page https://fshy.ajam.dev/p/origrid.md
- free tier: Storj has no free tier left, only a 30-day trial ('Free for 30 days', '25GB free storage for 30 days', 'No credit card required'). Sia's hosted product is 50 GB on the $0 plan. Origrid allows 25 GB per file with no account, and 50 GB per file with 50 GB of storage on a free account. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not recorded | note: not applicable
- retention: not recorded
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: the same as the free tier
- notes: the same as the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Storj has no free tier left, only a 30-day trial ('Free for 30 days', '25GB free storage for 30 days', 'No credit card required'). Sia's hosted product is 50 GB on the $0 plan. Origrid allows 25 GB per file with no account, and 50 GB per file with 50 GB of storage on a free account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Storj has no free tier left, only a 30-day trial ('Free for 30 days', '25GB free storage for 30 days', 'No credit card required'). Sia's hosted product is 50 GB on the $0 plan. Origrid is…
  - [1] 2026-11-03: Origrid allows 25 GB per file with no account; its free account gives 50 GB per file and 50 GB storage | capture: sha256:16f32d5a053a4edeba0b20848e516bb1a62f20139c9d8ac08203850bf07c106f | quote: No account needed to start (25 GB per file without one).
  - [2] 2026-11-03: the Storj free trial is 25GB for 30 days, free for 30 days, with no credit card required | quote: 25GB free storage for 30 days
  - [3] 2026-11-03: the first (Free) plan column of the Sia Storage App pricing table holds 50 GB of storage | capture: sha256:6832a746ff5596eecdce8233f71d3755e62b0011d6f4c364fcb38e82023dd2fd | quote: Storage 50 GB 500 GB
- sources:
  - [1] https://origrid.io/pricing
  - [2] https://www.storj.io/pricing
  - [3] https://sia.storage/
