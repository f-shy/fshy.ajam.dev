# File-Upload.net

> file-upload.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file-upload/ | JSON https://fshy.ajam.dev/api/v1/entity/file-upload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File-Upload.net

- `debrid/file-upload-net` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free, no premium) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://www.file-upload.net/en/faq.html
- price none: no premium accounts
- free tier: Upload without registration; the maximum size per file is 1 GB; the host works without limits, captchas and premium accounts. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The page is in German.
- per-object cap: Die max. Größe pro Datei beträgt 1 GB. | bytes: 1073741824 | source: [1] | note: bytes = 1 x 1024^3; multi-part archives are not allowed.
- retention: unverified: the page read prints no retention period | source: [1]
- egress: The page says the host works without limits and captchas; no byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The page says files can be uploaded and stored on the host without registration.
- interface: unknown
- limits:
  - per-object-cap (binding): 1 GB per file; multi-part archives not allowed [1]
- binding note: 1 GB per file is the only published number.
- interface detail: Web upload with a no-JavaScript upload variant.
- tooling: Browser only as read.
- composes with: 1 GB per file with no account and no paid tier to raise the cap.
- reliability: The page states there are no premium accounts, so there is no paid tier.
- evidence note: FAQ page read on 2026-11-03; retention is not printed on it.
- evidence:
  - [1] 2026-11-03: per-file cap 1 GB | capture: sha256:1dfe66653e0b260a23535f1bef316bb38703ac08a9410b2ea9c83127a7dc1170 | quote: Die max. Größe pro Datei beträgt 1 GB.
  - [1] 2026-11-03: no premium accounts and no captchas | capture: sha256:1dfe66653e0b260a23535f1bef316bb38703ac08a9410b2ea9c83127a7dc1170 | quote: Unser File Hoster arbeitet ohne Beschränkungen, ohne Limits, ohne Captchas und ohne Premium-Accounts.
- sources:
  - [1] https://www.file-upload.net/en/faq.html
