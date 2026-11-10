# file.kiwi Web

> file.kiwi | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file-2/ | JSON https://fshy.ajam.dev/api/v1/entity/file-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## file.kiwi

- `storage/file-kiwi` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://file.kiwi
- free tier: Web Folder Basic: 'No capacity limit. Auto-deleted 90 hours after upload.' API flow: 10 files per WebFolder, 999 GiB max per file | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 999 GiB max per file | bytes: 1072668082176 | source: [1] | note: not stated
- retention: Auto-deleted 90 hours after upload.' API flow: 10 files per WebFolder, 999 GiB max per file | days: 3 | source: [1] | note: not stated
- egress: No egress charge; instead a hard time gate. Free download window is 48 h (<10 GB), 12 h (10-20 GB), 6 h (>=20 GB); after that a $2+ Download Pass or $5 expiry extension is required. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 999 GiB/file [1]
  - retention-clamped: deleted 90 hours [1]
- limits note: 999 GiB/file; 10 files/WebFolder; 90 h total life; download window collapses to 6 h for >=20 GB; 1 concurrent chunk upload; download count capped at 3 in Korea
- interface detail: rest
- tooling: Documented v2 REST API at api.file.kiwi (POST /v2/folders returns presigned R2 PUT URLs), 36 h presigned-URL validity, client-side E2E keys (RFC 8188 AES-128-GCM); no rclone backend
- composes with: No account at all. One API call creates a folder; anonymous IDs are unlimited. Multiplication is trivial, the 90-hour delete is the wall.
- reliability: 6-48 h download windows make it a transfer tool, not storage; the 90 h auto-delete is unconditional
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Web Folder Basic — No capacity limit. Auto-deleted 90 hours after upload. $0'; lifecycle T0 -> T0+6~48 h -> T0+90 h
  - [2] 2026-10-21: Limits table: 'Files per WebFolder 10 · Max file size 999 GiB · Presigned URL validity 36 hours · Download count (Korea) 3'; 'Free Download Hours by File Size: <10 GB 24 hours / 10-20 GB 12 hours / >=20 GB 6 hours'
  - [3] 2026-10-21: 'No Sign-up Required: Use it immediately without registration'
- sources:
  - [1] https://file.kiwi/price
  - [2] https://file.kiwi/api
  - [3] https://file.kiwi/

## file.kiwi Web Folder+ (prepaid Upload-GB)

- `storage/file-kiwi-web-folder` | fails-quota | evidence reported | binding none | category file host (prepaid capacity)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://file.kiwi/price
- price $6.99 per TB for a 7-day hold = $6.99 × (30.4/7) ≈ $30.36/TB/mo to hold 1 TB continuously. To hold 20 TB: ~$607/mo. Roughly 30× the 1fichier/Blomp floor. Dead end for storage; only rational as a paid download-enabler for a one-off link. | parsed USD 30.36/TB-mo
- free tier: Prepaid Upload-GB: 50 GB upload $1.20, 100 GB $1.60, 500 GB $3.99, 1000×n GB $6.99×n. 1 Upload-GB = a 1 GB file kept available for 7 days. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 1 Upload-GB = a 1 GB file kept available for 7 days | days: 7 | source: [1] | note: not stated
- egress: Downloads are gated per-file, not metered: 'download requires a Download Pass or Expiry Postponement'. One-time Download Pass $2.00 (≤5 GB) or $2.00 + $0.40/GB above 5 GB. File Expiration Extension $5.00 buys 6 more hours, repeatable. | metered: yes
- identity: email | detail: email
- interface: rest
- limits note: 90-hour hard auto-delete on the free folder; 7-day default lifetime on paid folders; expiry purchased in 6-hour or 7-day increments
- interface detail: REST
- tooling: official API docs
- composes with: no
- reliability: This is a TRANSFER service priced per upload-with-a-deadline, not storage. The '1000 GB for $6.99' line is a one-shot: 1 TB uploaded and held for 7 days. Annualised storage-equivalent is astronomically worse.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Prepaid Upload-GB: 50 GB upload $1.20, 100 GB $1.60, 500 GB $3.99, 1000×n GB $6.99×n. 1 Upload-GB = a 1 GB file kept available for 7 days.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $6.99 per TB for a 7-day hold = $6.99 × (30.4/7) ≈ $30.36/TB/mo to hold 1 TB continuously. To hold 20 TB: ~$607/mo. Roughly 30× the 1fichier/Blomp floor. Dead end for storage; only rational as a paid download-enabler for a one-off link.
- evidence:
  - [1] 2026-10-21: '50 GB upload $1.20 · 100 GB upload $1.60 · 500 GB upload $3.99 · 1000 × n GB upload $6.99 × n'; '1 Upload-GB lets you upload a 1 GB file and keep it available for 7 days'; 'One-time Download Pass $2.00 … ≤ 5 GB: $2.00 · > 5 GB: + $0.40/GB'; 'File Expiration Extension $5.00 … Each purchase adds 6 hours'
  - [1] 2026-10-21: (free tier) — 'Web Folder Basic … No capacity limit. Auto-deleted 90 hours after upload'
- sources:
  - [1] https://file.kiwi/price
