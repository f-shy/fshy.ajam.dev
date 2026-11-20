# nostr.download

> nostr.download | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nostr-3/ | JSON https://fshy.ajam.dev/api/v1/entity/nostr-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nostr.download (route96 Blossom server)

- `storage/nostr-download` | qualifies | evidence reported | binding per-object-cap | category p2p-blob-storage
- needs card no, phone no, ID no, institution no | verified 2026-11-11T06:50:28.648Z (live) | stale on 2026-11-26
- url https://nostr.download/
- free tier: Per-file upload cap 10737418240 bytes; files with zero egress are deleted after 7 days. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10.00 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: Files with zero egress are deleted after 7 days. | source: [1] | note: not stated
- egress: Unmetered. Files served by GET /<sha256>, Content-addressed. Served through the server's own CDN; no egress counter is exposed anywhere. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - per-object-cap (binding): 10.00 GB per file [1]
  - retention-clamped: Delete never-downloaded files: After 1 days [1]
- limits note: per-object-cap 10 GB. Retention is download-triggered, not time-based: a file nobody fetches within 24 h is deleted. Anything in the hot working set survives indefinitely.
- interface detail: Blossom (BUD-01/02/04/06) + NIP-96. Plain HTTP PUT /upload, GET /<sha256>, HEAD /upload for preflight. Pinned by NIP-94 kind 1063 events.
- tooling: any HTTP client. Auth is a signed nostr event (kind 24242), so a locally generated keypair is the only credential. route96 (v0l), lotus, or hzrd149/blossom clients all speak it.
- composes with: Content-addressed by SHA-256, so a chunk-per-object scheme maps onto it natively with no index server. The hash IS the locator.
- reliability: single volunteer operator, no SLA, no durability warranty ('Do not use this service as your only backup'). Purges never-downloaded objects after 24 h, so a write-only cold archive decays to zero.
- notes: 10.00 GB per file (hard cap, read off the server's own the provider). No published per-user total. 'Inactive file deletion: No limit'. 'Delete never-downloaded files: After 1 days'.
- evidence note: max_upload_size: 10737418240; delete_zero_egress_days: 7
- evidence:
  - [2] 2026-10-21: 'Max upload size 10240 MB', 'Whitelist Open'
  - [1] 2026-10-21: 'Maximum file size 10.00 GB', 'Inactive file deletion: ? No limit', 'Delete never-downloaded files ? After 1 days'
  - [3] 2026-10-21: PUT with no auth returns HTTP 401 / x-reason 'Auth header not found', i.e. the endpoint is live and the only gate is the signature, not an account
  - [4] 2026-11-11: the props endpoint still reports the same upload cap and 7-day zero-egress retention | capture: sha256:1f149fee9ec9a3e87b025ca4ee074b3188df98e084e763b202224f5d37703cf4
- sources:
  - [1] https://nostr.download/tos
  - [2] https://nostr.download/
  - [3] https://nostr.download/upload
  - [4] https://nostr.download/props
