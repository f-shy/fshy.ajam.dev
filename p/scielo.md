# scielo data

> scielo.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scielo/ | JSON https://fshy.ajam.dev/api/v1/entity/scielo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## scielo data (data.scielo.org)

- `storage/scielo-data` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.scielo.org/api/info/version
- free tier: none reachable: the API answered HTTP 403 on 2026-11-19 across direct, proxy, pinned and probe routes; no dataset capacity could be read. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: the API answered HTTP 403 on 2026-11-19; routes tried: direct capture, fetch proxy, pinned reads, and a probe record. No dataset capacity could be read.
- notes: Bunny Shield challenge blocked all routes including the API. Datasets were unreachable on 2026-10-21.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Bunny Shield challenge on every route including the API.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Bunny Shield challenge on every route including the API.
  - probe:https://data.scielo.org/api/info/version 2026-11-19: a direct probe of the SciELO data API returned HTTP 403 on 2026-11-19 | capture: sha256:6491916814d4ea7014cb55d190010dfc9d29614ad485305f16d2caef98e9faf3 | quote: "status": 403,
  - probe:https://data.scielo.org/api/info/version 2026-11-19: the SciELO data API returned HTTP 403 on 2026-11-19, so no free capacity could be established | capture: sha256:6491916814d4ea7014cb55d190010dfc9d29614ad485305f16d2caef98e9faf3 | quote: "status": 403,
- sources:
  - [1] https://data.scielo.org/api/info/version
