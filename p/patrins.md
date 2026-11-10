# Patrins

> patrins.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/patrins/ | JSON https://fshy.ajam.dev/api/v1/entity/patrins.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Patrins

- `storage/patrins` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://patrins.com
- free tier: Two separate numbers, and the split matters: free plan storage is 8 GB, but the per-file ceiling is unlimited (marketing says 1 TB) on every plan including free, with unlimited bandwidth. Anonymous temporary uploads accept up to 1 TB per file and self-delete after 7 days. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1 TB per file | bytes: 1000000000000 | source: [1] | note: not stated
- retention: Anonymous downloads expire 7 hours after link generation; temp files auto-delete at 7 days. | days: 0 | source: [1] | note: not stated
- egress: Unlimited bandwidth on all plans, stated on the pricing table and repeated in docs. No egress product. | metered: no
- identity: institution
- interface: rest, webdav, rclone, cli
- limits:
  - per-object-cap (binding): 1 TB per file [1]
  - per-object-cap (binding): 1 TB/file [1]
  - retention-clamped: delete after 7 days [1]
  - retention-clamped: expire 7 hours [1]
- limits note: Free 8 GB storage, unlimited file size, unlimited bandwidth. Rate limits: public upload init 500/hour (files <1 GB) and 30/hour (>=1 GB) per IP; chunks 500/hour; finalize 30/hour; bulk zip 10/hour per user. Anonymous downloads expire 7 hours after link generation; temp files auto-delete at 7 days.
- interface detail: webdav
- tooling: Supports rclone via WebDAV (`https://patrins.com/dav`). Features REST API and tus 1.0 resumable uploads, webhooks, command-line interface, Telegram integration, and WebDAV drive mapping.
- composes with: rclone WebDAV mount + N free accounts x 8 GB permanent, or the anonymous 1 TB-per-file path for transit. The 8 GB cap is the binding number for storage; 1 TB/file only helps if something downstream holds the bytes.
- reliability: Per-file cap without matching storage is the classic trap: 1 TB/file x 8 GB total means the big-file capability is unusable without paying. API init returns 401 'Authentication required' without a bearer token, so 'no account needed' only holds for the temp flow.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table: 'Free | 8 GB | Unlimited | Unlimited' (storage | max file size | bandwidth), and rate-limit table 500/hr and 30/hr per IP
  - [2] 2026-10-21: 'Free uploads up to 1 TB. No account required for temporary files.', 'Temporary files auto-delete after 7 days'
  - [3] 2026-10-21: '1 TB max file size', '8 GB free forever storage', rclone webdav config snippet
  - withheld 2026-10-21: probe: POST /api/upload-init -> 401 {"error":"Authentication required"}; GET /api/public/upload/init -> 404
- sources:
  - [1] https://patrins.com/docs
  - [2] https://patrins.com/upload
  - [3] https://patrins.com/
