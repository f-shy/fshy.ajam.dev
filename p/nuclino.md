# Nuclino

> nuclino.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nuclino/ | JSON https://fshy.ajam.dev/api/v1/entity/nuclino.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nuclino (free teams)

- `storage/nuclino` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:27.599Z (live) | stale on 2026-11-25
- url https://www.nuclino.com
- free tier: Free plan: up to 50 items, up to 3 canvases, 2GB total storage. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress pricing published; attachments served from app.nuclino.com. Not metered anywhere on the pricing page. | metered: no
- identity: email | detail: First name, last name, email and password
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 MB per file [1]
- limits note: Per-object-cap: 10 MB per file. The API documents `413 .. an uploaded file exceeds the maximum size of 10 MB (code: FILE_TOO_LARGE)`, and a request body over 100 KB also 413s. request-rate: documented `429` rate limiting (separate page). Retention: no expiry documented; storage is freed only by deletion.
- interface detail: rest
- tooling: Documented public REST API (help.nuclino.com) with a real rate-limit and error contract. No rclone backend.
- composes with: 2 GB x unlimited free teams per user. 10 teams = 20 GB; 100 = 200 GB. This is the cleanest multiply-a-workspace in the niche because the docs state outright that a user can hold many teams and that CREATE TEAM is available to anyone on any plan.
- reliability: Hard 10 MB per-file ceiling makes this shard-only; the 2 GB team quota is small enough that item limits (50 items) bind before bytes do on the Free plan.
- notes: the same as the free tier
- evidence note: the pricing page lists the Free plan's item, canvas and storage limits
- evidence:
  - [1] 2026-10-21: 'Free ... Up to 50 items, Up to 3 canvases, 2GB total storage'; Starter '10GB storage per user'
  - [2] 2026-10-21: '`413` ... an uploaded file exceeds the maximum size of 10 MB (`code`: `FILE_TOO_LARGE`)'; '`429` The rate limit was exceeded'
  - [3] 2026-10-21: 'CREATE TEAM ... Available to anyone. Available on all plans'
  - [4] 2026-10-21: 'A user can be a member of several teams at the same time'
  - [1] 2026-11-09: the Free plan allows up to 50 items and 3 canvases with 2 GB total storage | capture: sha256:ff5b4cdff63752c456901eeb4d265753cc05e8b2a2ef87e7214711e9693a613c | quote: ## Free /user/month The basic version of Nuclino. [GET STARTED](https://app.nuclino.com/signup) - Up to 50 items - Up to 3 canvases - 2GB total storage
  - [5] 2026-11-09: the sign-up form asks for first name, last name, email and password | capture: sha256:1992bd587e67f9ac65508a9e5895d751ac635c8f219ee1b09dd6178e6104fd2a | quote: First name Last name Email Password
  - [2] 2026-11-09: an uploaded file is capped at 10 MB | capture: sha256:0bd76544b4c427ad0805f3136b6f05858a5a063d4580e842888e49c8573b64ff | quote: | `413` | The request body exceeds the maximum size of 100 KB, or an uploaded file exceeds the maximum size of 10 MB (`code`: `FILE_TOO_LARGE`). |
- sources:
  - [1] https://www.nuclino.com/pricing
  - [2] https://help.nuclino.com/0a1bea6c-response-format-and-errors
  - [3] https://help.nuclino.com/6ba3e235-create-a-team
  - [4] https://help.nuclino.com/6d1f45e3-switch-teams
  - [5] https://app.nuclino.com/signup
