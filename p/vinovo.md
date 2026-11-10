# Vinovo

> vinovo.si | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vinovo/ | JSON https://fshy.ajam.dev/api/v1/entity/vinovo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vinovo

- `debrid/vinovo-si` | qualifies-with-caveat | evidence documented | binding retention-clamped | category video host (free upload, monetised) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://vinovo.si/
- free tier: Unlimited storage is stated; video files up to 15GB; inactive files are deleted after 60 days without views or downloads. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 15GB per video file | source: [1]
- retention: 60 days without views or downloads | days: 60 | source: [1]
- egress: No download volume or speed figure is published on the page read. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: The page says users share and monetise videos, which implies an account; the registration form was not read.
- interface: unknown
- limits:
  - per-object-cap: video files up to 15GB [1]
  - retention-clamped (binding): inactive files are deleted after 60 days without views or downloads [1]
- binding note: Sixty days without a view removes a file, which binds before the 15GB cap for any file that is stored and not watched.
- interface detail: Web upload and remote upload from other hosts; no API was read.
- tooling: Browser upload and remote upload.
- composes with: Remote upload copies videos from other hosts, so the host can sit behind a link generator that fetches other hosts.
- reliability: No status page was read.
- evidence note: Cap, retention and storage read on the vendor home page FAQ. Cheapest paid tier: unverified: no price page was found (the premium URL answered HTTP 404).
- evidence:
  - [1] 2026-11-03: the per-file cap is 15GB | capture: sha256:7aabe5979c1307f72d9e909bfb107fdd401f6fdfeaf490653d890509bfe3b0b8 | quote: You can upload video files up to 15GB
  - [1] 2026-11-03: retention is 60 days without views or downloads | capture: sha256:7aabe5979c1307f72d9e909bfb107fdd401f6fdfeaf490653d890509bfe3b0b8 | quote: Inactive files will be deleted after 60 days without views or downloads
  - [1] 2026-11-03: storage is stated as unlimited | capture: sha256:7aabe5979c1307f72d9e909bfb107fdd401f6fdfeaf490653d890509bfe3b0b8 | quote: We offer unlimited storage
- sources:
  - [1] https://vinovo.si/
