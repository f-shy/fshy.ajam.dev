# Gigasend

> gigasend.us | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gigasend/ | JSON https://fshy.ajam.dev/api/v1/entity/gigasend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gigasend

- `debrid/gigasend-us` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous large-file transfer page (browser upload) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T22:12:34.471Z (live) | stale on 2026-12-26
- url https://gigasend.us/
- price USD 0
- free tier: Up to 50 GB free · 7-day link expiration | unit: GB | metered on: none | read on: 2026-10-23 | source: [1] | note: A paid delivery goes up to 250 GB at USD 0.20 per GB with a USD 9 minimum and a 30-day link; the free row is 50 GB.
- per-object cap: Up to 50 GB free, or up to 250 GB with a paid delivery | bytes: 50000000000 | source: [1] | note: Decimal GB as written on the page; the boundary was not pushed to.
- retention: 7-day link expiration on the free tier; 30-day link on a paid delivery | days: 7 | source: [1]
- egress: The page advertises no per-download charge and no account; traffic is not metered on the free tier as stated. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The free tier requires a sender email address.
- interface: browser
- limits:
  - per-object-cap (binding): 50 GB free [1]
- limits note: Four shape probes at the likely API paths returned 403 rather than 404, so the edge is refusing before the application sees the request.
- binding note: Up to 50 GB free with a 7-day link expiration.
- interface detail: A browser drop zone. No anonymous HTTP upload endpoint was found: POST to /api/upload, /upload, /api/files and /v1/upload all returned 403 from the edge, so the upload is a browser-orchestrated presigned flow whose endpoint is inside a JS bundle.
- tooling: Browser only as observed. A wrapper would need a headless browser or the presigned-URL flow read out of the JS bundle; neither was done here.
- composes with: A 50 GB drop with a 7-day life is the hand-off tier: send a finished archive to one reader, not a mirror an archive can be rebuilt from.
- reliability: An SEO-visible 2026 entrant with no published API and an edge that refuses unknown POSTs; nothing indicates long-term operation.
- notes: Browser-only: programmatic use needs a wrapper. No programmatic path found: A browser drop zone. No anonymous HTTP upload endpoint was found: POST to /api/upload, /upload, /api/files and /v1/upload all returned 403 from the edge, so the upload is a browser-orchestrated presigned flow whose endpoint is inside a JS bundle.
- evidence note: The offer and the 7-day expiry are quoted from the vendor page read; the upload path could not be driven from a script, so no byte was moved and the cap is the vendor's sentence only.
- extras:
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload; /api/v1/upload
  - api_result: 403 on every path
- evidence:
  - [1] 2026-10-23: 'Up to 10 GB free - 3-day link expiration' and 'Share up to 10 GB free - or up to 5 TB'
  - probe:https://gigasend.us/api/upload 2026-10-23: multipart POST to /api/upload, /upload, /api/files, /v1/upload, /api/v1/upload -> HTTP 403 on all five, so no anonymous HTTP upload endpoint is exposed
  - [1] 2026-11-25: the free tier now allows 50 GB per transfer with a 7-day link | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
  - [2] 2026-11-25: the paid tier now tops out at 250 GB, not 5 TB, and costs USD 0.20 per GB with a USD 9 minimum | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Send up to 50 GB free with a 7-day download link. Need up to 250 GB or 30-day retention? Pay a flat $0.20/GB ($9.00 minimum)—charged once, nothing renews.
  - [2] 2026-11-25: the current per-transfer caps are 50 GB free and 250 GB paid | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Send up to 50 GB free with a 7-day download link. Need up to 250 GB or 30-day retention? Pay a flat $0.20/GB ($9.00 minimum)—charged once, nothing renews.
  - [1] 2026-11-25: the free per-transfer cap is 50 GB | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
  - [2] 2026-11-25: the free link lasts 7 days and the paid link 30 days | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Send up to 50 GB free with a 7-day download link. Need up to 250 GB or 30-day retention? Pay a flat $0.20/GB ($9.00 minimum)—charged once, nothing renews.
  - [1] 2026-11-25: the free link lasts 7 days | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
  - [2] 2026-11-25: a sender email address is required for the free delivery | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Sender email required
  - [2] 2026-11-25: the free delivery asks the sender for an email address | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Sender email required
  - [1] 2026-11-25: the free cap is 50 GB with a 7-day link | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
  - [1] 2026-11-25: the first-party page states the 50 GB free transfer with a 7-day link | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
  - [2] 2026-11-25: the free tier requires a sender email address | capture: sha256:4559eb54631cf64aeb23a8be1631adcd94007174923f7da46da5bf9d4566d374 | quote: Sender email required
  - [1] 2026-11-25: the free transfer is 50 GB with a 7-day link | capture: sha256:0dd6a921e9ce355a1988d874d8c32be50afa1797d102f40dff1759efdc4a4e98 | quote: Up to 50 GB free · 7-day link expiration
- sources:
  - [1] https://gigasend.us/
  - [2] https://gigasend.us/plans
