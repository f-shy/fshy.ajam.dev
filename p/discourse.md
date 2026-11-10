# Discourse hosted Free plan

> discourse.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/discourse/ | JSON https://fshy.ajam.dev/api/v1/entity/discourse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Discourse hosted Free plan

- `storage/discourse-hosted-free-plan` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.discourse.org/free
- free tier: 5 GB storage per free site, with unlimited topics, chat and members | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; uploads served from *.discourse-cdn.com behind CloudFront, so a Cloudflare/CloudFront cache sits in front already | metered: no
- identity: email
- interface: rest, rclone
- limits note: 5 GB per site; 2 staff seats; 10 categories; no tags; no private categories; site provisioning throttled ('You have provisioned too many sites in the past hour'); post/upload rate limits are default Discourse
- interface detail: rest
- tooling: Discourse's own REST API is fully available on the free site (POST /uploads.json with an API key, /posts.json, /latest.json); no rclone backend
- composes with: 5 GB x N free sites. Free sites are self-serve from id.discourse.com/create-site with a Discourse ID; provisioning is rate-limited but per-hour, not per-account. 100 sites = 500 GB; 400 sites = 2 TB.
- reliability: Free plan launched 2026-02 and is still labelled beta; the provisioning throttle is the real scaling brake, and the 10-category cap makes bulk-upload workflows awkward.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Unlimited topics, chat and members... 2 staff seats, 5GB storage'
  - [2] 2026-10-21: 'A real Discourse, free forever... No credit card - Unlimited members - Set up in about 1 minute'
  - [3] 2026-10-21: probe: GET -> HTTP 200 application/json (public read API works anonymously); POST https://meta.discourse.org/uploads.json -> HTTP 403 (write path auth-gated as expected)
  - [4] 2026-10-21: probe: GET ... -> 302 -> 200 via CloudFront (uploads are CDN-fronted)
- sources:
  - [1] https://meta.discourse.org/t/youre-invited-to-try-the-discourse-free-plan-beta/395632
  - [2] https://www.discourse.org/free
  - [3] https://meta.discourse.org/latest.json
  - [4] https://sea3.discourse-cdn.com/meta/user_avatar/
