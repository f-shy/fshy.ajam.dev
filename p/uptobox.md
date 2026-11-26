# uptobox

> uptobox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uptobox/ | JSON https://fshy.ajam.dev/api/v1/entity/uptobox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## uptobox

- `storage/uptobox` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://uptobox.com/
- free tier: none reachable: Seized and still dead. The domain answers with a Cloudflare 522 and a French/English maintenance banner ('Nous réalisons une maintenance et nous revenons très vite'), which reads like a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Seized and still dead. The domain answers with a Cloudflare 522 and a French/English maintenance banner ('Nous réalisons une maintenance et nous revenons très vite'), which reads like a…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Seized and still dead. The domain answers with a Cloudflare 522 and a French/English maintenance banner ('Nous réalisons une maintenance et nous revenons très vite'), which reads like a…
  - probe:https://uptobox.com/ 2026-11-19: a direct GET of uptobox.com answered HTTP 522 with no body on 2026-11-19, so the host still does not serve | capture: sha256:7535e943073f3fd4369c4b608bd50f1565aa3310412b3446a632335c955a803f | quote: "status": 522
- sources:
  - [1] https://uptobox.com/
