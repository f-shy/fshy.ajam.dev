# File2Share

> file2share.us | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file2share/ | JSON https://fshy.ajam.dev/api/v1/entity/file2share.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File2Share

- `debrid/file2share-us` | dead | evidence measured | binding none | category transfer.sh-shaped upload, advertised as a transfer.sh replacement | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://file2share.us/
- free tier: none reachable: the site advertises `curl --upload-file` with the same command shape as transfer.sh, and that exact shape returns HTTP 404 | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The offer exists on the marketing page; the endpoint the page names does not answer.
- per-object cap: not reached: the endpoint refused before a size mattered | source: [1]
- retention: not reached | source: [1]
- egress: not assessed: nothing was stored | metered: no | source: [1]
- identity: anonymous | detail: No signup was reached because the upload path does not exist.
- interface: unknown
- limits note: Two shapes tried, both 404. The 404 body is a hosted static error page, not an application error, so the route does not exist rather than being disabled.
- binding note: Nothing binds because nothing answers.
- interface detail: PUT https://file2share.us/<name> and POST https://file2share.us/upload both return a static 404 page.
- tooling: The advertised curl one-liner does not work; nothing else was found.
- composes with: Nothing to chain: a dead advertising page for a replacement for a dead service.
- reliability: A 2026 SEO page marketing a transfer.sh replacement whose own documented command 404s.
- notes: Do not retry the marketing page's command; the path it names does not exist.
- evidence note: The death was measured: two request shapes, both 404, on 2026-10-23.
- extras:
  - routes_tried: PUT /<name>; POST /upload
- evidence:
  - probe:https://file2share.us/payload-1mib.bin 2026-10-23: PUT of 1 048 576 bytes -> HTTP 404 with a static '404 Not Found' page
  - probe:https://file2share.us/upload 2026-10-23: multipart POST -> HTTP 404, same static page
  - [1] 2026-10-23: 'File2Share accepts the same curl --upload-file command' - the claim the two probes refute
- sources:
  - [1] https://file2share.us/transfer-sh-alternative
