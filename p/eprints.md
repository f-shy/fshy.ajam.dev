# roar

> eprints.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eprints/ | JSON https://fshy.ajam.dev/api/v1/entity/eprints.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## roar (roar.eprints.org)

- `storage/roar` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:03.330Z (live) | stale on 2026-12-04
- url https://roar.eprints.org/rawlist.txt
- free tier: none reachable: the rawlist.txt dump is now readable but is metadata only (a registry of open-access repositories), not a bulk file store | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloudflare 522/403 on the raw endpoints. rawlist.txt (the one machine-readable dump) times out at 22 s; /view/software/dspace.html returns a 7 KB Cloudflare error page. Only recoverable via
  - [1] 2026-11-19: the rawlist.txt dump is a registry metadata listing, not a bulk file store | capture: sha256:484dba78348dea480115c327f7a37cfb7d6a3aa31887dfe03be6b0c8df5dad0a | quote: eprintid: 1
  - [1] 2026-11-19: the rawlist.txt dump is a metadata listing of repository records, not user file storage | capture: sha256:484dba78348dea480115c327f7a37cfb7d6a3aa31887dfe03be6b0c8df5dad0a | quote: eprintid: 1
- sources:
  - [1] https://roar.eprints.org/rawlist.txt
