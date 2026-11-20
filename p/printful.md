# printful

> printful.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/printful/ | JSON https://fshy.ajam.dev/api/v1/entity/printful.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## printful

- `storage/printful` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:57.504Z (live) | stale on 2026-12-04
- url https://help.printful.com/hc/en-us/articles/360014066319
- free tier: None reachable: print files up to 200 MB and 20,000 x 20,000 px; the file is an input to printing, not hosted storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: 200 MB per print file, max 20,000x20,000 px, PNG/JPG only, and PDF is explicitly prohibited on every print method. The REST API is excellent and completely irrelevant. The file is an input.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200 MB per print file, max 20,000x20,000 px, PNG/JPG only, and PDF is explicitly prohibited on every print method. The REST API is excellent and completely irrelevant — the file is an input
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 200 MB per print file, max 20,000x20,000 px, PNG/JPG only, and PDF is explicitly prohibited on every print method. The REST API is excellent and completely irrelevant — the file is an input
  - [2] 2026-10-21: cited as the basis of the rejection: 200 MB per print file, max 20,000x20,000 px, PNG/JPG only, and PDF is explicitly prohibited on every print method. The REST API is excellent and completely irrelevant — the file is an input
  - [2] 2026-11-19: current print-file ceiling is 200 MB and 20,000 x 20,000 px | capture: sha256:00286b359893a4cf6270ae743ffb82fcb935101c34668736e63ca379ff138339 | quote: Design files added to your File library can be up to 200 MB, with maximum dimensions of 20,000 × 20,000 px.
  - [2] 2026-11-19: PDF is an accepted upload format | capture: sha256:00286b359893a4cf6270ae743ffb82fcb935101c34668736e63ca379ff138339 | quote: PDFs are an accepted file format, but they can contain hidden layers, embedded fonts, blend modes, strokes, transparency effects, and other elements that may render differently during production.
  - [1] 2026-11-19: the originally cited article answered HTTP 403 on 2026-11-19 | capture: sha256:946bd28b379293d4b67fb1b02be261fb0af9fd00caffe94e157c673c0197bc69 | quote: Printful Help Center
- sources:
  - [1] https://help.printful.com/hc/en-us/articles/360014066319
  - [2] https://help.printful.com/hc/en-us/articles/50264019148177
