# sxcu.net

> sxcu.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sxcu/ | JSON https://fshy.ajam.dev/api/v1/entity/sxcu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sxcu.net

- `debrid/sxcu-net` | fails-quota | evidence documented | binding per-object-cap | category image and short-video host (anonymous, API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://sxcu.net/
- free tier: Free anonymous uploader and link shortener; maximum file size 95MB; accepted types are png, jpg, jpeg, gif, ico, bmp, tif, tiff, webm and webp; no registration required. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 95MB per file; image and webm types only | source: [1]
- retention: unverified: the page states no retention window | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page states registration is not required.
- interface: rest
- limits:
  - per-object-cap (binding): maximum file size 95MB [1]
- binding note: A 95MB ceiling and an image-only type list bound the host.
- interface detail: A documented API for upload and collections is linked from the page; it was not read.
- tooling: ShareX and any HTTP client against the API.
- composes with: The accepted file types are images and short video only, so it is not a general file path.
- reliability: No status page was read.
- evidence note: Cap and types read on the vendor home page. Retention is unverified: not on the page read.
- evidence:
  - [1] 2026-11-03: the per-file cap is 95MB | capture: sha256:764432e588bf75a62ae6f4f0e627fef34f8e219046983c096e5f33ffa54eb802 | quote: With a maximum file size of 95MB.
  - [1] 2026-11-03: no account is needed | capture: sha256:764432e588bf75a62ae6f4f0e627fef34f8e219046983c096e5f33ffa54eb802 | quote: sxcu.net does not require a registration
- sources:
  - [1] https://sxcu.net/
