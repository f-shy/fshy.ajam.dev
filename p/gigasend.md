# Gigasend

> gigasend.us | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gigasend/ | JSON https://fshy.ajam.dev/api/v1/entity/gigasend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gigasend

- `debrid/gigasend-us` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous large-file transfer page (browser upload) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://gigasend.us/
- price USD 0
- free tier: Up to 10 GB free - 3-day link expiration | unit: GB | metered on: none | read on: 2026-10-23 | source: [1] | note: Paid tiers go to 5 TB per transfer; the free tier is the 10 GB row.
- per-object cap: Up to 10 GB free, or up to 5 TB with a paid transfer | bytes: 10000000000 | source: [1] | note: Decimal GB as written on the page; the boundary was not pushed to.
- retention: 3-day link expiration | days: 3 | source: [1]
- egress: The page advertises no per-download charge and no account; traffic is not metered on the free tier as stated. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The page states no account is needed for the free 10 GB tier; uploads are browser-driven and no registration was attempted.
- interface: unknown
- limits:
  - per-object-cap (binding): 10 GB free [1]
- limits note: Four shape probes at the likely API paths returned 403 rather than 404, so the edge is refusing before the application sees the request.
- binding note: 10 GB per transfer with a 3-day life: at 1 TiB a month the object size forces 100 transfers, and the retention means none of them is still there when the month ends.
- interface detail: A browser drop zone. No anonymous HTTP upload endpoint was found: POST to /api/upload, /upload, /api/files and /v1/upload all returned 403 from the edge, so the upload is a browser-orchestrated presigned flow whose endpoint is inside a JS bundle.
- tooling: Browser only as observed. A wrapper would need a headless browser or the presigned-URL flow read out of the JS bundle; neither was done here.
- composes with: A 10 GB drop with a 3-day life is the hand-off tier: send a finished archive to one reader, not a mirror an archive can be rebuilt from.
- reliability: An SEO-visible 2026 entrant with no published API and an edge that refuses unknown POSTs; nothing indicates long-term operation.
- notes: Browser-only: programmatic use needs a wrapper.
- evidence note: The offer and the 3-day expiry are quoted from the vendor page read; the upload path could not be driven from a script, so no byte was moved and the cap is the vendor's sentence only.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload; /api/v1/upload
  - api_result: 403 on every path
- evidence:
  - [1] 2026-10-23: 'Up to 10 GB free - 3-day link expiration' and 'Share up to 10 GB free - or up to 5 TB'
  - probe:https://gigasend.us/api/upload 2026-10-23: multipart POST to /api/upload, /upload, /api/files, /v1/upload, /api/v1/upload -> HTTP 403 on all five, so no anonymous HTTP upload endpoint is exposed
- sources:
  - [1] https://gigasend.us/
