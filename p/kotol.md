# Tempcloud

> kotol.cloud | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kotol/ | JSON https://fshy.ajam.dev/api/v1/entity/kotol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tempcloud (temp.kotol.cloud)

- `debrid/temp-kotol-cloud` | qualifies-with-caveat | evidence documented | binding per-object-cap | category temporary file host (code-based, anonymous) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://temp.kotol.cloud/
- free tier: Upload a file, receive a code, download with the code; file size limit 10 GiB per file; files deleted automatically after the chosen time limit. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 10 GiB per file | bytes: 10737418240 | source: [1]
- retention: files are deleted automatically after the chosen time limit; the maximum is not stated | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page shows no login step: upload a file and receive a code.
- interface: rest
- limits:
  - per-object-cap (binding): 10 GiB per file [1]
- binding note: A 10 GiB ceiling is the only number the page states; the time limit options are not listed.
- interface detail: Web upload returning a code; downloads take the code; no API was read.
- tooling: Browser upload.
- composes with: A 10 GiB per-file cap with a selectable time limit whose maximum is not stated.
- reliability: Running downloads finish after the time limit; no status page was read.
- evidence note: Cap read on the vendor home page. The selectable time limits are unverified: not on the page read.
- evidence:
  - [1] 2026-11-03: cap is 10 GiB per file | capture: sha256:25a82d45cad2b8bfdf56fc07e00a2c363154994795d9354d13b3dc6a025de58b | quote: File size limit is 10 GiB per file.
  - [1] 2026-11-03: files expire after a chosen time limit | capture: sha256:25a82d45cad2b8bfdf56fc07e00a2c363154994795d9354d13b3dc6a025de58b | quote: All files are deleted automatically after the chosen time limit.
- sources:
  - [1] https://temp.kotol.cloud/
