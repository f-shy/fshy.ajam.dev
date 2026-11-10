# FileBolt

> filebolt.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebolt/ | JSON https://fshy.ajam.dev/api/v1/entity/filebolt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileBolt

- `debrid/filebolt-net` | qualifies-with-caveat | evidence documented | binding pull-count | category anonymous large-file transfer page (browser upload) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://filebolt.net/
- price USD 0
- free tier: Send Large Files - Free File Sharing and Transfer up to 10 GB. No Email Required. | unit: GB | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: up to 10 GB | bytes: 10000000000 | source: [1]
- retention: unverified: expiry is an option ('optionally with a password or an expiry date'), no default period is published | source: [1]
- egress: No byte allowance stated. The page offers a download limit and revocation per transfer, so traffic out is controlled by the sender rather than metered by the vendor. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'No accounts, no ads: Nobody needs to sign up, neither you nor your recipients'
- interface: unknown
- limits:
  - per-object-cap: 10 GB [1]
  - pull-count (binding): sender can set a download limit per transfer [1]
- limits note: Revocation and per-download visibility are the differentiators the page sells; neither was exercised.
- binding note: The publishable download limit is the first constraint a re-fetch meets: a link with a limit of one is spent by the first reader, and at 1 TiB a month that means a new transfer per read.
- interface detail: Browser drop zone. /api/upload returns 404, /api/files returns 400, so a JSON API exists (the 400 is a validation answer) but its contract is not published.
- tooling: Browser only as observed. The 400 from /api/files is the one opening: it means a JSON endpoint answers, and a wrapper could probe it.
- composes with: A per-transfer download limit and revocation make it a controlled hand-off, which is the opposite of a mirror; it does not chain into an archive.
- reliability: No published operator, no API documentation, and an edge that answers unknown POSTs with 404.
- notes: The controlled-hand-off feature set is real but unmeasured; the record exists so the subsequent audit does not re-discover the name.
- evidence note: The 10 GB offer and the no-account sentence are quoted from the vendor page; nothing was uploaded, so the cap is the page's word.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload
- evidence:
  - [1] 2026-10-23: 'Free File Sharing and Transfer up to 10 GB', 'No accounts, no ads: Nobody needs to sign up, neither you nor your recipients', and the password / download-limit / revocation options
  - probe:https://filebolt.net/api/files 2026-10-23: HTTP 400 from a JSON endpoint at /api/files, so an API exists but publishes no contract
- sources:
  - [1] https://filebolt.net/
