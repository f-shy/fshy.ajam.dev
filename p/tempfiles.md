# Tempfiles

> tempfiles.ninja | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tempfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/tempfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tempfiles (tempfiles.ninja)

- `debrid/tempfiles-ninja` | fails-quota | evidence documented | binding retention-clamped | category temporary file host (encrypted, 24 hours) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://tempfiles.ninja/
- free tier: Encrypt and share files up to 100MiB for 24 hours. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 100MiB per file | bytes: 104857600 | source: [1]
- retention: 24 hours | days: 1 | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page shows no login step.
- interface: rest
- limits:
  - per-object-cap: files up to 100MiB [1]
  - retention-clamped (binding): shared for 24 hours [1]
- binding note: A 24-hour clock expires any file before a large transfer is repeated.
- interface detail: Browser upload with client-side encryption; no API was read.
- tooling: Browser upload.
- composes with: A 24-hour clock and 100MiB cap make it a short hand-off only.
- reliability: No status page was read.
- evidence note: Cap and expiry read in the page description; the page body is a script shell.
- evidence:
  - [1] 2026-11-03: cap 100MiB and expiry 24 hours | capture: sha256:484fe879128bf9d70acad7a110ae286cf860a38e01170a9d7bfbb730918429a6 | quote: Encrypt and share files up to 100MiB for 24 hours
- sources:
  - [1] https://tempfiles.ninja/
