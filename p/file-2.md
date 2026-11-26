# file.kiwi Web

> file.kiwi | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file-2/ | JSON https://fshy.ajam.dev/api/v1/entity/file-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## file.kiwi

- `storage/file-kiwi` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:26.681Z (live) | stale on 2026-12-04
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
  - [2] 2026-11-19: the v2 API still lists a 999 GiB max file size and 10 files per WebFolder; presigned URLs last 36 hours | capture: sha256:a15ee59ae94fb43b49b165cdce8ecffa1192a36a87417c6b81714f4090d1e408 | quote: | Max file size | 999 GiB |
  - [1] 2026-11-19: the Basic Web Folder has unlimited upload capacity and files are auto-deleted 90 hours after upload | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: Upload Capacity | Unlimited
- sources:
  - [1] https://file.kiwi/price
  - [2] https://file.kiwi/api
  - [3] https://file.kiwi/

## file.kiwi Web Folder+ (prepaid Upload-GB)

- `storage/file-kiwi-web-folder` | fails-quota | evidence reported | binding none | category file host (prepaid capacity)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:37.016Z (live) | stale on 2026-12-04
- url https://file.kiwi/price
- price $6.99 per TB for a 7-day hold = $6.99 × (30.4/7) ≈ $30.36/TB/mo to hold 1 TB continuously. To hold 20 TB: ~$607/mo. Roughly 30× the 1fichier/Blomp floor. Dead end for storage; only rational as a paid download-enabler for a one-off link. | parsed USD 30.36/TB-mo
- free tier: Prepaid kiwi credits: 50 kiwi free on signup; 400 kiwi $1.20, 800 kiwi $1.60, 4000 kiwi $3.99, 8000 kiwi $6.99. 1 kiwi = 1 GB uploaded or 1 GB of retention extended by 1 day; files kept 7 days by default. Web Folder Basic is $0 with unlimited upload size and 90-hour auto-delete. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Files are kept for 7 days on upload, and retention can then be extended in 1-day increments; the free Web Folder Basic is auto-deleted at T0 + 90 h. | days: 7 | source: [1] | note: not stated
- egress: Downloads use a one-time Download Pass priced $1 per file plus $0.30 per started GB (rounded up). Retention extension costs $1.5 per file plus $0.45 per GB, offered for +1 day, +7 days and +30 days. | metered: yes
- identity: email | detail: email
- interface: rest
- limits note: 90-hour auto-delete on the free folder (T0 + 90 h, extendable); 7-day default lifetime on paid folders; retention extended in +1 day, +7 day or +30 day increments.
- interface detail: REST
- tooling: official API docs
- composes with: no
- reliability: This is a TRANSFER service priced per upload-with-a-deadline, not storage. The '1000 GB for $6.99' line is a one-shot: 1 TB uploaded and held for 7 days. Annualised storage-equivalent is astronomically worse.
- notes: Prepaid Upload-GB: 50 GB upload $1.20, 100 GB $1.60, 500 GB $3.99, 1000×n GB $6.99×n. 1 Upload-GB = a 1 GB file kept available for 7 days.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Prepaid Upload-GB: 50 GB upload $1.20, 100 GB $1.60, 500 GB $3.99, 1000×n GB $6.99×n. 1 Upload-GB = a 1 GB file kept available for 7 days.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $6.99 per TB for a 7-day hold = $6.99 × (30.4/7) ≈ $30.36/TB/mo to hold 1 TB continuously. To hold 20 TB: ~$607/mo. Roughly 30× the 1fichier/Blomp floor. Dead end for storage; only rational as a paid download-enabler for a one-off link.
- evidence:
  - [1] 2026-10-21: '50 GB upload $1.20 · 100 GB upload $1.60 · 500 GB upload $3.99 · 1000 × n GB upload $6.99 × n'; '1 Upload-GB lets you upload a 1 GB file and keep it available for 7 days'; 'One-time Download Pass $2.00 … ≤ 5 GB: $2.00 · > 5 GB: + $0.40/GB'; 'File Expiration Extension $5.00 … Each purchase adds 6 hours'
  - [1] 2026-10-21: (free tier) — 'Web Folder Basic … No capacity limit. Auto-deleted 90 hours after upload'
  - [1] 2026-11-19: the first-party price page now sells prepaid kiwi credits at these four price points | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: 400 kiwi$1.20 800 kiwi$1.60 4000 kiwi$3.99 8000 kiwi$6.99
  - [1] 2026-11-19: paid-folder files are kept 7 days by default with 1-day extension increments | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: Files are kept for 7 days on upload, and retention can then be extended in 1-day increments.
  - [1] 2026-11-19: the Download Pass is priced $1 per file plus $0.3 per GB, replacing the earlier $2.00 pass | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: $1 × file count + $0.3 × total GB (rounded up)
  - [1] 2026-11-19: the free folder is auto-deleted 90 hours after upload, and extension increments are now 1/7/30 days | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: Auto-deleted at T0 + 90 h (extendable with an add-on)
  - [1] 2026-11-19: the prepaid kiwi credit is the current unit of upload capacity and retention | capture: sha256:cf7d24e1f9eef317dce1772e58a62c6cb6dd2885dfcd9c869f04e308b9b8d5e0 | quote: 1 kiwi lets you upload 1 GB or extend the retention of 1 GB of uploaded files by 1 day.
- sources:
  - [1] https://file.kiwi/price
