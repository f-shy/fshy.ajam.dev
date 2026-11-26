# api.video

> api.video | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/api-2/ | JSON https://fshy.ajam.dev/api/v1/entity/api-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## api.video

- `storage/api-video` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:54.755Z (live) | stale on 2026-12-04
- url https://api.video/pricing/
- free tier: none reachable: Encoding free but hosting is $0.00285 per minute per month and delivery $0.0017 per minute. Per-minute-of-video pricing, so it is both paid and duration-shaped; 10,000 hours would be… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the api.video pricing page; hosting is metered per minute of video stored. | source: [1] | note: not applicable
- retention: Videos are stored with backups so access is retained; no fixed retention period is stated on the pricing page. | source: [1]
- egress: Video delivery is metered at $0.0017 per minute of video delivered. | metered: no
- identity: email | detail: the first-party pricing page states no commitments or credit card are required
- interface: rest
- interface detail: Access is through upload, write and read API calls.
- tooling: not documented
- composes with: Encodes, hosts and delivers video through its own CDN; metered per minute of video, so it can serve video but not hold a general-purpose byte store.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Encoding free but hosting is $0.00285 per minute per month and delivery $0.0017 per minute. Per-minute-of-video pricing, so it is both paid and duration-shaped; 10,000 hours would be…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Encoding free but hosting is $0.00285 per minute per month and delivery $0.0017 per minute. Per-minute-of-video pricing, so it is both paid and duration-shaped; 10,000 hours would be…
  - [1] 2026-11-19: hosting is still priced per minute of video stored, not a byte allowance | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: PER MINUTE OF VIDEO STORED
  - [1] 2026-11-19: the signup gate does not ask for a card | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: No commitments or credit card required
  - [1] 2026-11-19: api.video exposes upload, write and read API calls with rate limits | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: 100 Upload API calls/min
  - [1] 2026-11-19: hosting is metered by minutes of video stored rather than a single-object cap; no per-object cap is stated | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: Total length or storage of your hosted videos.
  - [1] 2026-11-19: videos are stored with backups and no fixed retention period is stated | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: Api.video securely stores your videos with backups so that you never lose access to your content
  - [1] 2026-11-19: video delivery is priced at $0.0017 per minute delivered | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: $0.0017 PER MINUTE OF VIDEO DELIVERED
  - [1] 2026-11-19: api.video delivers video through its own worldwide CDN | capture: sha256:db07f6ed8c8ac947e4906d791dc988ba00365eb48a1f28971f44e9d3d0733ff3 | quote: Delivery on the CDN (worldwide)
- sources:
  - [1] https://api.video/pricing/
