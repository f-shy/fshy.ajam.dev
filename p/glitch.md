# Glitch

> glitch.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/glitch/ | JSON https://fshy.ajam.dev/api/v1/entity/glitch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Glitch

- `compute/glitch` | dead | evidence documented | binding retention-clamped | category platform host | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-24T03:25:00.000Z (live) | stale on 2026-11-24
- url https://blog.glitch.com/
- free tier: shut down: the newest post on the blog is 2025-07-23, 'Until we meet again', and no hosting is offered | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: project hosting ended on 2025-07-08; the code-download window closed at the end of 2025.
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: not applicable: user profiles were shut down with the hosting
- interface: unknown
- limits:
  - retention-clamped (binding): the blog's newest entry is the shutdown announcement [1]
- limits note: The hosting ended on 2025-07-08 and the code-download window closed on 2025-12-31, so nothing remains to reach and the redirects are all that survive.
- binding note: nothing is served.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Nothing chains. The replacement pattern among evaluated offerings is a free static host plus a free ephemeral container, which is what took Glitch's place.
- reliability: the blog is the cheapest liveness check for this host: one read settles it
- notes: Confirms earlier readings row.
- evidence note: the blog index was read and its newest entry is the goodbye post
- extras:
  - facets.free_tier_kind: none
  - billing_model: none
  - term: none
  - price_arithmetic: none
  - free_tier_kind: none
  - session_cap.restart_required: no
  - session_cap.note: dead
- evidence:
  - [1] 2026-10-22: the blog index has no entry after 2025-07-23, confirming the end state a year later
  - [2] 2026-10-22: quoted: 'On July 8, 2025 Glitch project hosting and user profiles will be shut down'
  - [3] 2026-10-22: 
  - [1] 2026-10-24: quoted: the newest entry is 'Wednesday, July 23, 2025 Until we meet again' linking to /post/goodbye-glitch, and no post after it
  - [1] 2026-10-24: the newest post on the blog is dated 2025-07-23 and titled 'Until we meet again', with nothing published since
- sources:
  - [1] https://blog.glitch.com/
  - [2] https://blog.glitch.com/post/changes-are-coming-to-glitch
  - [3] https://blog.glitch.com/post/goodbye-glitch
