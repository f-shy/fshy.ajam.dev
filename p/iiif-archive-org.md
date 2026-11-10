# iiif.archive.org

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iiif-archive-org/ | JSON https://fshy.ajam.dev/api/v1/entity/iiif-archive-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iiif.archive.org (free IIIF Image API over any uploaded image)

- `storage/iiif-archive-org` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://iiif.archive.org/iiif/
- free tier: No separate quota. It is a free image server over items you already hold, one image per item. Capacity therefore follows the 1TB/item rule. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 1TB/item | bytes: 1000000000000 | source: [1] | note: not stated
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
- reliability: Third-party workshop doc, not IA's own page.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: (snapshot 2026-07-12) — 'The Internet Archive allows you to upload images and then provides a IIIF Image API service ... images can be accessed as either Version 2 or Version 3'
  - withheld 2026-10-21: same page — 'Ensure you only upload 1 image (if you want multiple images you will need to create multiple items ... collection is Community Image'
  - [2] 2026-10-21: probe: GET -> connection timeout; via fetch proxy -> 522 (same network block as archive.org)
- sources:
  - [1] https://training.iiif.io/iiif-bl-workshop/day-two/image-servers/iiif-hosting-ia.html
  - [2] https://iiif.archive.org/iiif/nasa/info.json
