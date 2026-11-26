# UpZur Premium

> upzur.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upzur/ | JSON https://fshy.ajam.dev/api/v1/entity/upzur.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UpZur

- `storage/upzur` | qualifies | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:18.733Z (live) | stale on 2026-12-10
- url https://upzur.com
- free tier: Free registered account: 1,953 GB (1.9 TB) storage, 5,120 MB per file, download volume Unlimited, files deleted 120 days after last download | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5,120 MB per file | bytes: 5120000000 | source: [1] | note: Registered: 5120 Mb per file
- retention: Free registered account: 1,953 GB (1.9 TB) storage, 5,120 MB per file, download volume Unlimited, files deleted 120 days after last download | days: 120 | source: [1] | note: Registered: 120 days after last download
- egress: Free, Registered and Premium: Download volume Unlimited | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): 5,120 MB per file [1]
  - retention-clamped: deleted 120 days [1]
- limits note: 5,120 MB per file for registered; 120-day retention reset by download; unlimited download volume; no published upload/day cap
- interface detail: rest
- tooling: XFileSharing Pro; API-key upload path at /api/upload/server?utype=anon (and /api/upload/server?key=<api key> from the account dashboard); web upload form posts to fs<nn>.uploadhive-style cgi-bin; PolyUploader covers the family
- composes with: N free registrations, one per XFileSharing host, each ~0.2-2 TB: UpZur 1,953 GB + FileAxa 488 GB + Mega4up 183 GB + the rest of the family (see notes). A single identity source (free email) times a long commodity host list.
- reliability: anonymous upload_form 302-redirects to login, so the 1.9 TB tier is registration-gated rather than anonymous; the anon API path returned Apache 500 on this host
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: table read live: Free 200 Mb / '-' / Unlimited / 5 days; Registered 5120 Mb / 1953 GB / Unlimited / 120 days after last download; Premium Unlimited/Unlimited/Unlimited/Never
  - [2] 2026-10-21: probe: GET -> 302 Location https://upzur.com/?op=login (anonymous upload gated)
  - [3] 2026-10-21: probe: GET -> 500 Internal Server Error
  - [1] 2026-11-19: the registered free tier is 1953 GB, unchanged | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | Storage space | - | 1953 GB | Unlimited |
  - [1] 2026-11-19: registered files are deleted 120 days after last download, unchanged | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | When are your files deleted? | 5 days after last download | 120 days after last download | Never |
  - [1] 2026-11-25: the registered tier allows 5120 Mb per file | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | Max upload file size | 200 Mb | 5120 Mb | Unlimited |
  - [1] 2026-11-25: registered files are deleted 120 days after last download | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | When are your files deleted? | 5 days after last download | 120 days after last download | Never |
  - [1] 2026-11-25: the first-party table lists Unlimited download volume in all three tiers | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | Download volume | Unlimited | Unlimited | Unlimited |
- sources:
  - [1] https://upzur.com/premium
  - [2] https://upzur.com/?op=upload_form
  - [3] https://upzur.com/api/upload/server?utype=anon

## UpZur Premium

- `storage/upzur-premium` | fails-egress | evidence reported | binding none | category file host (paid tier)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:25.206Z (live) | stale on 2026-12-04
- url https://upzur.com/premium
- price $110/yr ÷ 12 = $9.17/mo for 'unlimited' — so there is no $/TB by construction, which is itself the tell. If you value it at 20 TB it is $0.46/TB/mo and if you value it at 1 TB it is $9.17/TB/mo. Priced per-account, capped by an unpublished bandwidth threshold, with hotlinking blocked by the vendor's own rule and zero… | parsed USD 9.17/mo
- free tier: 'Unlimited upload size, Unlimited storage space, Download volume Unlimited' on Premium. Registered free tier is 1,953 GB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 5120 Mb (5 GB) max upload on free registered; unlimited only on Premium; 120-day retention | days: 120 | source: [1] | note: not stated
- egress: 'Download volume Unlimited' claimed on all tiers including free. | metered: no
- identity: email | detail: email + a human-verification step
- interface: s3, rest, webdav, rclone
- limits note: 5120 Mb (5 GB) max upload on free registered; unlimited only on Premium; 120-day retention
- interface detail: REST/HTTP; no WebDAV or S3
- tooling: no rclone backend
- composes with: part of interface detail
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Unlimited upload size, Unlimited storage space, Download volume Unlimited' on Premium. Registered free tier is 1,953 GB.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $110/yr ÷ 12 = $9.17/mo for 'unlimited' — so there is no $/TB by construction, which is itself the tell. If you value it at 20 TB it is $0.46/TB/mo and if you value it at 1 TB it is $9.17/TB/mo. Reject.
- evidence:
  - [1] 2026-10-21: '7 days USD 4.00 only · 30 days USD 12.00 only · 90 days USD 32.00 only · 180 days USD 62 only · 365 days USD 110 only'; 'Unlimited upload size, Unlimited storage space, Download volume Unlimited'; feature table: 'Max upload file size | 200 Mb | 5120 Mb | Unlimited'
  - [2] 2026-10-21: 'Disable direct linking for accounts exceeding bandwidth thresholds … Modify or terminate services without prior notice'; 'UpZur is not responsible for: User content loss or unavailability'
  - [3] 2026-10-21: 
  - [1] 2026-11-19: the Premium plan advertises unlimited upload, storage and download volume | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: Unlimited upload size, Unlimited storage space, Download volume Unlimited, Remote URL upload Enabled, No Waiting & No Ads & No Captcha
  - [1] 2026-11-19: registered files are removed 120 days after last download; Premium files never | capture: sha256:d9c48b190969f734426b8e5b72fb80e877844a9e5957e356d522d79fb8777492 | quote: | When are your files deleted? | 5 days after last download | 120 days after last download | Never |
  - [2] 2026-11-19: the vendor reserves an undisclosed bandwidth threshold for direct linking | capture: sha256:3ce670ca358d42c0557b8490897fa9b39d3328c594edf637beb2a30dfc4c5295 | quote: - Disable direct linking for accounts exceeding bandwidth thresholds
  - [3] 2026-11-19:  | capture: sha256:49a1395369f2b9c13f2a1ec4de7c507b0e309446ec7ba7438195f58b2e9c87e1
- sources:
  - [1] https://upzur.com/premium
  - [2] https://upzur.com/terms
  - [3] https://upzur.com/faq
