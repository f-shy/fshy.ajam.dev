# temp-files

> temp-files.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/temp-files/ | JSON https://fshy.ajam.dev/api/v1/entity/temp-files.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## temp-files

- `debrid/temp-files-com` | fails-quota | evidence documented | binding per-object-cap | category temporary file host (anonymous, 7 days) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://www.temp-files.com/
- free tier: Current limits: 10 files, 100 MB per file, 2.0 GB total, 7 days maximum. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 100 MB per file | source: [1]
- retention: expiry up to 7 days, chosen per upload | days: 7 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The upload page shows no login step.
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB per file; 10 files and 2.0 GB total per batch [1]
  - retention-clamped: 7 days maximum [1]
- binding note: The 100 MB per-file ceiling is far below a large archive.
- interface detail: Browser upload with drag, paste and share settings (expiry, download limit, password); no API was read.
- tooling: Browser upload.
- composes with: The limits line caps one upload batch at 10 files, 100 MB each and 2.0 GB total.
- reliability: No status page was read.
- evidence note: Limits read on the vendor home page.
- evidence:
  - [1] 2026-11-03: per-file cap 100 MB, 2.0 GB total, 7 days maximum | capture: sha256:c2581bde8eb7215f42cc8509d58cec3f27495107da29b59d2cbaad6024b0d887 | quote: Current limits: 10 files · 100 MB / file · 2.0 GB total · 7d max
- sources:
  - [1] https://www.temp-files.com/
