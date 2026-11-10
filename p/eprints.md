# roar

> eprints.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eprints/ | JSON https://fshy.ajam.dev/api/v1/entity/eprints.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## roar (roar.eprints.org)

- `storage/roar` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://roar.eprints.org/rawlist.txt
- free tier: none reachable: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via
- sources:
  - [1] https://roar.eprints.org/rawlist.txt
