# Patrins

> patrins.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/patrins/ | JSON https://fshy.ajam.dev/api/v1/entity/patrins.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Patrins

- `storage/patrins` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:37.736Z (live) | stale on 2026-12-04
- url https://patrins.com
- free tier: Free: 8 GB storage, unlimited bandwidth. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1 TB per file | bytes: 1000000000000 | source: [1] | note: not stated
- retention: Anonymous downloads expire 7 hours after link generation; temp files auto-delete at 7 days. | days: 0 | source: [1] | note: not stated
- egress: Unlimited bandwidth on all plans, stated on the pricing table and repeated in docs. No egress product. | metered: no
- identity: email
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
- notes: Two separate numbers, and the split matters: free plan storage is 8 GB, but the per-file ceiling is unlimited (marketing says 1 TB) on every plan including free, with unlimited bandwidth. Anonymous temporary uploads accept up to 1 TB per file and self-delete after 7 days.
- evidence note: All plans include unlimited file size, unlimited bandwidth, and every platform feature.
- evidence:
  - [1] 2026-10-21: table: 'Free | 8 GB | Unlimited | Unlimited' (storage | max file size | bandwidth), and rate-limit table 500/hr and 30/hr per IP
  - [2] 2026-10-21: 'Free uploads up to 1 TB. No account required for temporary files.', 'Temporary files auto-delete after 7 days'
  - [3] 2026-10-21: '1 TB max file size', '8 GB free forever storage', rclone webdav config snippet
  - withheld 2026-10-21: probe: POST /api/upload-init -> 401 {"error":"Authentication required"}; GET /api/public/upload/init -> 404
  - [1] 2026-11-11: the plan table states Free: 8 GB storage and Bandwidth Unlimited | capture: sha256:4b1fb6106b5202760bbcbc808eae7bdf0dbcd88927a96feb3b5f31a873fa05d8 | quote: Free ... 8 GB ... Max File Size ... Unlimited ... Bandwidth ... Unlimited
  - [1] 2026-11-11: the plan table and the Temporary Files section state the storage, unit and expiry | capture: sha256:4b1fb6106b5202760bbcbc808eae7bdf0dbcd88927a96feb3b5f31a873fa05d8 | quote: Free ... 8 GB ... Bandwidth ... Unlimited ... Temporary Files ... 1 day ... 7 days (default) ... 30 days
  - [1] 2026-11-11: the docs state that all plans, free included, have unlimited file size and unlimited bandwidth | capture: sha256:cb81587b341651a16afd80dbc4052d878f9e04e2d117d6d4c8abdc592821f90b | quote: All plans include unlimited file size, unlimited bandwidth, and every platform feature.
  - [1] 2026-11-19: the plan table states Free 8 GB storage with unlimited file size and bandwidth | capture: sha256:0fd42be4d84af456d4bc3d8406866fbf461d7e6f1da6b590c09088095c279ef8 | quote: | Free | 8 GB | Unlimited | Unlimited |
  - [2] 2026-11-19: anonymous temporary uploads still accept up to 1 TB per file | capture: sha256:ca69e5bed287ac150e7629a4ab4fd1edf2b1f04f8f93d57472bc817605779d18 | quote: Free uploads up to 1 TB. No account required for temporary files.
  - [4] 2026-11-19: account creation requires an email address and password, with Google, Yandex and passkey as alternatives; no card or institution is asked for | capture: sha256:3239e644cdcd0330ae3a423a516b957270c6108de1a6dd7bfb5a010bf45f774d | quote: <input id="registerEmail" class="form-field" type="email" placeholder="Email address" required autocomplete="email">
  - [4] 2026-11-19: the sign-up form offers Google as a registration route | capture: sha256:3239e644cdcd0330ae3a423a516b957270c6108de1a6dd7bfb5a010bf45f774d | quote: Continue with Google
- sources:
  - [1] https://patrins.com/docs
  - [2] https://patrins.com/upload
  - [3] https://patrins.com/
  - [4] https://patrins.com/register
