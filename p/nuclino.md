# Nuclino

> nuclino.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nuclino/ | JSON https://fshy.ajam.dev/api/v1/entity/nuclino.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nuclino (free teams)

- `storage/nuclino` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.nuclino.com
- free tier: Free plan: '2GB total storage', up to 50 items, up to 3 canvases. Storage is per TEAM, and team creation is self-service and unlimited: 'CREATE TEAM ... Available to anyone. Available on all plans', and 'A user can be a member of several teams at the same time'. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress pricing published; attachments served from app.nuclino.com. Not metered anywhere on the pricing page. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 MB per file [1]
- limits note: Per-object-cap: 10 MB per file. The API documents `413 .. an uploaded file exceeds the maximum size of 10 MB (code: FILE_TOO_LARGE)`, and a request body over 100 KB also 413s. request-rate: documented `429` rate limiting (separate page). Retention: no expiry documented; storage is freed only by deletion.
- interface detail: rest
- tooling: Documented public REST API (help.nuclino.com) with a real rate-limit and error contract. No rclone backend.
- composes with: 2 GB x unlimited free teams per user. 10 teams = 20 GB; 100 = 200 GB. This is the cleanest multiply-a-workspace in the niche because the docs state outright that a user can hold many teams and that CREATE TEAM is available to anyone on any plan.
- reliability: Hard 10 MB per-file ceiling makes this shard-only; the 2 GB team quota is small enough that item limits (50 items) bind before bytes do on the Free plan.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Free ... Up to 50 items, Up to 3 canvases, 2GB total storage'; Starter '10GB storage per user'
  - [2] 2026-10-21: '`413` ... an uploaded file exceeds the maximum size of 10 MB (`code`: `FILE_TOO_LARGE`)'; '`429` The rate limit was exceeded'
  - [3] 2026-10-21: 'CREATE TEAM ... Available to anyone. Available on all plans'
  - [4] 2026-10-21: 'A user can be a member of several teams at the same time'
- sources:
  - [1] https://www.nuclino.com/pricing
  - [2] https://help.nuclino.com/0a1bea6c-response-format-and-errors
  - [3] https://help.nuclino.com/6ba3e235-create-a-team
  - [4] https://help.nuclino.com/6d1f45e3-switch-teams
