# TmpSend

> tmpsend.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tmpsend/ | JSON https://fshy.ajam.dev/api/v1/entity/tmpsend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TmpSend

- `debrid/tmpsend` | qualifies-with-caveat | evidence documented | binding per-object-cap | category temporary file host (anonymous, 7 days) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://tmpsend.com/
- free tier: Free uploads of up to 1GB, hosted for 7 days, unlimited downloads. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 1GB per file | source: [1]
- retention: files are deleted 7 days after upload | days: 7 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page states no account is needed to upload and share.
- interface: rest
- limits:
  - per-object-cap (binding): files up to 1GB [1]
  - retention-clamped: hosted for 7 days [1]
- binding note: A 1GB file ceiling binds before the fixed 7-day clock for large objects.
- interface detail: Web upload; each file gets a unique link; no API was read.
- tooling: Browser upload.
- composes with: A 1GB drop with a fixed 7-day clock and unlimited downloads.
- reliability: No status page was read.
- evidence note: Cap and retention read on the vendor home page.
- evidence:
  - [1] 2026-11-03: the per-file cap is 1GB | capture: sha256:5d07dce925d0bca762b10856c63e04fb234378a5d8188a1da15353052f8c6ef9 | quote: Upload files upto 1GB
  - [1] 2026-11-03: files are hosted 7 days | capture: sha256:5d07dce925d0bca762b10856c63e04fb234378a5d8188a1da15353052f8c6ef9 | quote: Hosted For 7 Days
  - [1] 2026-11-03: downloads are unlimited within the 7 days | capture: sha256:5d07dce925d0bca762b10856c63e04fb234378a5d8188a1da15353052f8c6ef9 | quote: Unlimited downloads of your file FREE for 7 days
- sources:
  - [1] https://tmpsend.com/
