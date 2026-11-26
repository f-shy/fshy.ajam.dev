# pixelfed flagship

> pixelfed.social | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pixelfed-2/ | JSON https://fshy.ajam.dev/api/v1/entity/pixelfed-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pixelfed flagship (pixelfed.social, pixelfed.art)

- `storage/pixelfed-flagship` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.981Z (live) | stale on 2026-12-04
- url https://pixelfed.social/api/v1/instance
- free tier: none reachable: Hosts pixelfed.social and pixelfed.art returned Cloudflare 521 origin unreachable on 2026-10-21. Regional instances answered normally but the primary instances were unreachable. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The flagship Pixelfed hosts pixelfed.social and pixelfed.art now answer the instance API with HTTP 200 and valid instance JSON; the earlier origin-unreachable outage is no longer present. Per-instance media limits are image_size_limit and video_size_limit of 15360000 bytes.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both returned Cloudflare 521 (origin unreachable) on every probe. The software works and pixelfed.de/pixelfed.au answered normally, but the two biggest hosts were down…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both returned Cloudflare 521 (origin unreachable) on every probe. The software works and pixelfed.de/pixelfed.au answered normally, but the two biggest hosts were down, so
  - [2] 2026-10-21: cited as the basis of the rejection: Both returned Cloudflare 521 (origin unreachable) on every probe. The software works and pixelfed.de/pixelfed.au answered normally, but the two biggest hosts were down, so
  - [3] 2026-10-21: cited as the basis of the rejection: Both returned Cloudflare 521 (origin unreachable) on every probe. The software works and pixelfed.de/pixelfed.au answered normally, but the two biggest hosts were down, so
  - [1] 2026-11-19: pixelfed.social now answers with valid instance JSON | capture: sha256:c38a50b5eaee54318ac2d9f27a28edbdfdaa08c32d51f025c5c06b1d74d25541 | quote: "uri":"pixelfed.social","title":"pixelfed"
  - [2] 2026-11-19: pixelfed.art now answers with valid instance JSON | capture: sha256:3fb29cc778b742f93cd90fb4de9ba2a444b0ae01c16e7daf6f9bca6f873b2e24 | quote: "uri":"pixelfed.art"
  - [3] 2026-11-19: pixelfed.de answers with valid instance JSON | capture: sha256:28ef9acc209bfec24a1c02c44365dc5f4782542fb739bec2e373deeb707b0500 | quote: "uri":"pixelfed.de"
- sources:
  - [1] https://pixelfed.social/api/v1/instance
  - [2] https://pixelfed.art/api/v1/instance
  - [3] https://pixelfed.de/api/v1/instance
