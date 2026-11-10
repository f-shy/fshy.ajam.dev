# Chute

> codecraftsol.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codecraftsol/ | JSON https://fshy.ajam.dev/api/v1/entity/codecraftsol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chute

- `debrid/chute-codecraftsol-org` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous large-file transfer page (browser upload) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://chute.codecraftsol.org/
- price USD 0
- free tier: Free file transfer for files up to 10 GB. No account, no ads, no waiting. | unit: GB | metered on: none | read on: 2026-10-23 | source: [1] | note: The page compares itself to WeTransfer's free limit, which dates the copy to the WeTransfer 2 GB era.
- per-object cap: Send up to 10 GB per transfer | bytes: 10000000000 | source: [1]
- retention: unverified: 'Links expire on their own and the files are deleted for good' - no duration is given | source: [1] | note: Expiry exists; its length is not published.
- egress: No byte allowance or download counter is stated; the page offers optional end-to-end encryption and password protection. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The page states no sign-up for sender or recipient; no upload was attempted.
- interface: unknown
- limits:
  - per-object-cap (binding): 10 GB per transfer [1]
- limits note: The service is a single-purpose page whose operator identity is a personal subdomain (codecraftsol.org); there is no company page to read.
- binding note: 10 GB per transfer is the only published number; retention is unknown, so what fails second cannot be named.
- interface detail: Browser drop zone. /upload and /v1/upload answer 405 and /api/upload answers 404, so the anonymous upload is a browser flow with no documented endpoint.
- tooling: Browser only as observed; no API page is linked.
- composes with: A 10 GB no-signup drop with optional E2E is a hand-off to one reader; with no published expiry it cannot be scheduled against.
- reliability: A personal-subdomain service with no published cap on volume and no stated expiry period.
- notes: Listed as a lead for the subsequent audit rather than a settled provider: the numbers are the vendor's and the mechanism is unmeasured.
- evidence note: Offer and the existence of expiry are quoted from the vendor page; the retention length and the upload path are both missing.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload; /api/v1/upload
- evidence:
  - [1] 2026-10-23: 'Send up to 10 GB per transfer - five times WeTransfer's free limit', 'No sign-up for you or whoever you're sending to', 'Links expire on their own and the files are deleted for good'
  - probe:https://chute.codecraftsol.org/api/upload 2026-10-23: shape sweep: /api/upload 404, /upload 405, /api/files 404, /v1/upload 405, /api/v1/upload 404
- sources:
  - [1] https://chute.codecraftsol.org/
