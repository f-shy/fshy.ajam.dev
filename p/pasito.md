# Pasito

> pasito.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pasito/ | JSON https://fshy.ajam.dev/api/v1/entity/pasito.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pasito

- `debrid/pasito-me` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous file and note sharing page | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:32.906Z (live) | stale on 2026-12-04
- url https://pasito.me/
- price USD 0
- free tier: Free, no signup: a single file up to 10 GB, or a stack of files bundled into one link. | unit: GB | metered on: none | read on: 2026-10-23 | source: [1] | note: The page states a 10 GB limit per file or bundle; no total storage quota or monthly allowance is stated.
- per-object cap: Up to 10 GB per single file; a bundle of files is 10 GB in total. | bytes: 10000000000 | source: [1]
- retention: The sender chooses the expiry, from 1 day up to 30 days; files are permanently deleted after it. | days: 30 | source: [1]
- egress: No download byte allowance is stated; a share can carry a sender-set download or view limit and an expiry of up to 30 days. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Zero accounts or sign-ups required'; no subscription is offered.
- interface: unknown
- limits:
  - per-object-cap (binding): 10 GB per file or per bundle [1]
- limits note: Everything beyond the title had to be inferred from a client-rendered page, which is why this record is unverified rather than documented.
- binding note: The 10 GB per-file or per-bundle limit is the only limit the page states; no total quota, monthly allowance or download cap is published.
- interface detail: Client-rendered page; the served HTML is 6 193 bytes with no form and no API path. /api/upload and /upload answer 404.
- tooling: Browser only as observed; nothing to drive from a script without reading the JS bundle.
- composes with: A 10 GB drop plus encrypted notes is a hand-off; with no published expiry it cannot be scheduled against.
- reliability: The page is a JS application that serves no readable offer; the operator is unnamed.
- notes: Page body read: 10 GB per file or bundle, expiry 1 to 30 days, no account. Whether datacenter addresses are accepted is not published.
- evidence note: The page body states the 10 GB limit, the 1 to 30 day expiry and the no-signup claim. No upload or download was attempted, so nothing is measured and the API shape is unknown.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload; /api/v1/upload
- evidence:
  - [1] 2026-10-23: the served HTML is a 6 193-byte client-side app whose <title> reads 'Pasito - Free 10 GB file sharing, photo albums & encrypted notes, no signup'
  - probe:https://pasito.me/api/upload 2026-10-23: HTTP 404 on /api/upload, /upload, /api/files, /v1/upload, /api/v1/upload
  - [1] 2026-11-03: a single file up to 10 GB or a bundle is free with no signup | capture: sha256:51400957149a05d3c59fc6a009220bd7152f43d5b8e5ba2b851c0fe391e7b5c2 | quote: Send a single file up to 10 GB, or bundle a stack into one short link — all of it free, no signup.
  - [1] 2026-11-03: the upload box states the 10 GB limit for a file or a stack | capture: sha256:51400957149a05d3c59fc6a009220bd7152f43d5b8e5ba2b851c0fe391e7b5c2 | quote: Up to 10 GB · single file or a stack
  - [1] 2026-11-03: expiry is chosen by the sender between 1 and 30 days, then files are deleted | capture: sha256:51400957149a05d3c59fc6a009220bd7152f43d5b8e5ba2b851c0fe391e7b5c2 | quote: Choose exactly when your links stop working. From 1 day up to 30 days, after which files are permanently deleted.
  - [1] 2026-11-03: per-share expiry and download or view limit are sender options; no allowance is stated | capture: sha256:51400957149a05d3c59fc6a009220bd7152f43d5b8e5ba2b851c0fe391e7b5c2 | quote: Every share — file, bundle, album, or note — can carry a password, an expiry of up to 30 days, a download or view limit, and a quiet 30-second window to undo the send.
  - [1] 2026-11-03: no account or sign-up is required | capture: sha256:51400957149a05d3c59fc6a009220bd7152f43d5b8e5ba2b851c0fe391e7b5c2 | quote: - Zero accounts or sign-ups required
- sources:
  - [1] https://pasito.me/
