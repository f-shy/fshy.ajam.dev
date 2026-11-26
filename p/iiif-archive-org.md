# iiif.archive.org

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iiif-archive-org/ | JSON https://fshy.ajam.dev/api/v1/entity/iiif-archive-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iiif.archive.org (free IIIF Image API over any uploaded image)

- `storage/iiif-archive-org` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-11T06:09:39.445Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://iiif.archive.org/iiif/
- free tier: No separate quota. It is a free image server over items you already hold, one image per item. Capacity therefore follows the 1TB/item rule. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1TB/item | bytes: 1000000000000 | source: [2] | note: not stated
- retention: One image per item for reliable IIIF (multiple images need multiple items); must upload to the 'Community Image' collection or the viewer breaks; test-style uploads can be deleted after 30 days. | days: 30 | source: [1] | note: not stated
- egress: Free, and it is a rendering endpoint, so one stored master serves arbitrary region/size/rotation/quality requests. The cheapest possible way to serve image bytes at many sizes. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 1TB/item [1]
  - retention-clamped: deleted after 30 days [1]
- limits note: One image per item for reliable IIIF (multiple images need multiple items); must upload to the 'Community Image' collection or the viewer breaks; test-style uploads can be deleted after 30 days.
- interface detail: rest
- tooling: IIIF Image API v2 and v3 (Cantaloupe server); any IIIF viewer or plain GET on /iiif/<identifier>/info.json; no rclone backend
- composes with: Allows storing high-resolution master images and serving rendered image tiles or thumbnails via IIIF endpoints, reducing outbound transfer bandwidth across requests.
- reliability: unverified: iiif.archive.org/iiif/nasa/info.json answered HTTP 302 on 2026-11-11 and redirected to /image/iiif/2/None/info.json, where the read timed out; no image was served.
- notes: Ensure you only upload 1 image ( if you want multiple images you will need to create multiple items)
- evidence:
  - [1] 2026-10-21: (snapshot 2026-07-12) — 'The Internet Archive allows you to upload images and then provides a IIIF Image API service ... images can be accessed as either Version 2 or Version 3'
  - withheld 2026-10-21: same page — 'Ensure you only upload 1 image (if you want multiple images you will need to create multiple items ... collection is Community Image'
  - [3] 2026-10-21: probe: GET -> connection timeout; via fetch proxy -> 522 (same network block as archive.org)
  - [1] 2026-11-11: the workshop page states the one-image-per-item constraint | capture: sha256:d9e531a80a2cfeb9d0c072f604bd86ab759d5014bc3afb49b454f61c69673752 | quote: Ensure you only upload 1 image ( if you want multiple images you will need to create multiple items)
  - probe:https://iiif.archive.org/iiif/nasa/info.json 2026-11-11: the host redirects instead of serving an image info document | capture: sha256:cf2ea3e14f4b5e7e40286f7136feb6c4b531debbf8e2031ff23fa60cbb2c730d | quote: "status": 302
  - [2] 2026-11-11: the 1TB per-item limit is stated on the Internet Archive help page, not the workshop page | capture: sha256:d275db5cf0e45fcf37c38b13a12c1cb3776620ad3e376f2443b89d14bf73354c | quote: Currently, there is a 1TB size limit for item pages.
- sources:
  - [1] https://training.iiif.io/iiif-bl-workshop/day-two/image-servers/iiif-hosting-ia.html
  - [2] https://help.archive.org/help/uploading-tips/
  - [3] https://iiif.archive.org/iiif/nasa/info.json
