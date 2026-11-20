# Deta Space

> deta.space | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deta/ | JSON https://fshy.ajam.dev/api/v1/entity/deta.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deta Space

- `compute/deta-space` | dead | evidence documented | binding retention-clamped | category cloud VM | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://deta.space/
- free tier: nothing reachable: deta.space returned a Cloudflare 530 on 2026-10-24. The sunset on 2024-10-17 deleted all apps, horizons, websites and data. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: data was deleted at the sunset; nothing remains
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: not applicable: no signup page is served
- interface: unknown
- limits:
  - retention-clamped (binding): origin answers 530 on the root path [1]
- limits note: The service was discontinued on a published date and stored data was deleted.
- binding note: there is no service to bind.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing. The composition it enabled, a free always-on personal server with disk, has no replacement among evaluated offerings at the same zero price.
- reliability: a 530 is an origin failure, not a rate limit
- notes: Still notable because 'free always-on personal cloud' is recommended from posts written before 2024-10-17.
- evidence note: the 530 was observed today on the root path; the sunset date is carried from earlier readings.
- extras:
  - facets.class: inverse-dead
  - facets.free_tier_kind: none
  - billing_model: none
  - term: none
  - price_arithmetic: none
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: dead
- evidence:
  - [2] 2026-10-22: submission dated 2024-09-02 stating Space would be sunset on 17 October 2024
  - [3] 2026-10-22: the vendor's own notice dated 2024-09-26 that apps, horizons, websites and data would be removed at sunset, with export tools provided
  - [4] 2026-10-22: a hosted project confirms the shutdown date and that all apps and data including third-party apps would be deleted
  - [1] 2026-10-24: 
  - [1] 2026-10-24: HTTP 530 on 2026-10-24; the host does not answer
- sources:
  - [1] https://deta.space/
  - [2] https://news.ycombinator.com/item?id=41426388
  - [3] https://shutdownlikeaboss.com/post/762742417220878336/reminder-space-is-shutting-down-in-3-weeks
  - [4] https://github.com/WebCrateApp/webcrate/discussions/90
