# TempFile.org

> tempfile.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tempfile/ | JSON https://fshy.ajam.dev/api/v1/entity/tempfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TempFile.org

- `debrid/tempfile-org` | fails-quota | evidence documented | binding retention-clamped | category temporary file host (anonymous, 1 to 48 hours) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://tempfile.org/
- free tier: Free uploads, max 100 MB, automatically deleted after 1, 6, 24 or 48 hours; no registration required. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 100 MB per file | source: [1]
- retention: files are deleted after 1, 6, 24 or 48 hours | days: 2 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page states no registration is required.
- interface: rest
- limits:
  - per-object-cap: max 100 MB per file [1]
  - retention-clamped (binding): deleted after 1, 6, 24 or 48 hours [1]
- binding note: A 48-hour maximum is the binding clock; the 100 MB cap is second.
- interface detail: Web upload and upload via URL; every file is scanned for viruses and malware; no API was read.
- tooling: Browser upload.
- composes with: Upload via URL imports a remote file, so a link generator can hand it a URL.
- reliability: No status page was read.
- evidence note: Cap and expiry read on the vendor home page.
- evidence:
  - [1] 2026-11-03: files expire in 1 to 48 hours and the cap is 100 MB | capture: sha256:6a6845e670a80b98b2e412bb6fe0e4e5bdc64e45723dda6b61d8da579d12847b | quote: All uploaded files are automatically deleted after 1, 6, 24, or 48 hours. Upload files instantly (max 100 MB).
  - [1] 2026-11-03: no account is needed | capture: sha256:6a6845e670a80b98b2e412bb6fe0e4e5bdc64e45723dda6b61d8da579d12847b | quote: no registration required!
- sources:
  - [1] https://tempfile.org/
