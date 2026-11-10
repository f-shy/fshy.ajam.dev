# Files.dp.ua

> files.dp.ua | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/files-2/ | JSON https://fshy.ajam.dev/api/v1/entity/files-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Files.dp.ua

- `debrid/files-dp-ua` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (free, anonymous) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://files.dp.ua/en/
- price unverified: no paid tier was found
- free tier: Free file sharing without registration; maximum file size 100 GB; stored up to 25 days. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: No total storage or download byte allowance is printed; the upload form offers expiry choices of 1 download, 24 hours, 7 days or 20 days.
- per-object cap: The maximum allowable file size is 100 GB. | bytes: 107374182400 | source: [1] | note: bytes = 100 x 1024^3.
- retention: Your files will be stored on our servers for up to 25 days, after the expiration date will be deleted. | days: 25 | source: [1]
- egress: Upload and download speeds up to 1000 megabits per second are stated; no byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The page states 'Download and forward any files even without registration.'
- interface: unknown
- limits:
  - per-object-cap: 100 GB per file [1]
  - retention-clamped (binding): up to 25 days, then deleted [1]
- binding note: The 25-day expiry is the first limit, since a 100 GB file already fits the cap.
- interface detail: Web upload with an optional numeric password and a choice of expiry.
- tooling: Browser only as read.
- composes with: 100 GB per file with no account is the largest per-file cap in this slice, kept 25 days at most.
- reliability: No paid tier was found on the pages read, so the cheapest paid price is unverified.
- evidence note: Homepage read on 2026-11-03. The FAQ URL tried returned a not-found page.
- evidence:
  - [1] 2026-11-03: per-file cap 100 GB | capture: sha256:91c0c2094f99b21663d7702b303effaaf26d7da981cda54777cc73d6194ef4ad | quote: The maximum allowable file size is 100 GB.
  - [1] 2026-11-03: retention up to 25 days | capture: sha256:91c0c2094f99b21663d7702b303effaaf26d7da981cda54777cc73d6194ef4ad | quote: Your files will be stored on our servers for up to 25 days, after the expiration date will be deleted.
  - [1] 2026-11-03: no registration is needed | capture: sha256:91c0c2094f99b21663d7702b303effaaf26d7da981cda54777cc73d6194ef4ad | quote: Download and forward any files even without registration.
- sources:
  - [1] https://files.dp.ua/en/
