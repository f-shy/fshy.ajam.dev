# Uptomega

> uptomega.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uptomega/ | JSON https://fshy.ajam.dev/api/v1/entity/uptomega.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uptomega

- `debrid/uptomega` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (XFileSharing, free upload, premium) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://uptomega.net/
- free tier: The upload form states a 4000 Mb maximum file size; the premium table lists the free column with no storage figure and Unlimited download volume. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 4000 Mb per file on the free upload form; 8000, 10000 and 20000 Mb on the premium columns | source: [2]
- retention: 5 days after the last download in the first column; 15, 20 and 30 days in the premium columns | days: 5 | source: [1]
- egress: Download volume is Unlimited in every column. The premium table lists four periods (7, 30, 120 and 365 days) with the prices not captured. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The upload form shows no login step; only agreement to the terms is requested. Premium purchase and registration were not read.
- interface: rest
- limits:
  - per-object-cap: 4000 Mb per file on the free upload form, up to 20000 Mb on the top premium column [2]
  - retention-clamped (binding): files are deleted 5 days after the last download in the first column [1]
- binding note: Five days after the last download binds before the per-file cap.
- interface detail: Web upload with remote URL copy and a torrent-leech tab; the torrent server was reported unavailable.
- tooling: Browser upload, remote URL copy and a torrent leech tab on the upload form.
- composes with: Premium periods are 7, 30, 120 and 365 days; the table shows a 4000 to 20000 Mb per-file range and 5 to 30 days of retention.
- reliability: The pages answered HTTP 403 to the page reader while still returning their content. The upload page reports no live torrent server.
- evidence note: Caps and expiry read on the vendor upload form and premium table. Cheapest paid tier: unverified: the premium table names periods of 7, 30, 120 and 365 days but no prices were captured.
- evidence:
  - [2] 2026-11-03: the upload form states a 4000 Mb file limit | capture: sha256:a8ed4569b1ff2fd9dee84c96a80a71afe7c6ed864002e7cd410d6facd0bd5c39 | quote: Max file size is 4000 Mb
  - [1] 2026-11-03: per-file caps by column: 4000 Mb to 20000 Mb | capture: sha256:191ccb79dda043b7abebd51114d7dc82bdfdb7f79afbcf3913367b66a3133bfe | quote: Max upload file size 4000 Mb 8000 Mb 10000 Mb 20000 Mb
  - [1] 2026-11-03: expiry by column: 5 days after last download in the first column | capture: sha256:191ccb79dda043b7abebd51114d7dc82bdfdb7f79afbcf3913367b66a3133bfe | quote: When are your files deleted? 5 days after last download 15 days after last download 20 days after last download 30 days after last download
  - [1] 2026-11-03: download volume is unlimited in every column | capture: sha256:191ccb79dda043b7abebd51114d7dc82bdfdb7f79afbcf3913367b66a3133bfe | quote: Download volume Unlimited Unlimited Unlimited Unlimited
- sources:
  - [1] https://uptomega.net/premium.html
  - [2] https://uptomega.net/
