# Ghost(Pro)

> ghost.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ghost/ | JSON https://fshy.ajam.dev/api/v1/entity/ghost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ghost(Pro) — 5 MB on free trial/Starter, 100 MB Publisher; self-hosted is unbounded

- `storage/ghost-5-mb-on-free-trial-starter-100-mb-publisher-self-h` | trial-only | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ghost.org
- free tier: "When uploading media files to Ghost, while there is no limit on the number of files you can upload to your site, there is a file size limit based on your Ghost(Pro) plan. Free trial: 5mb / Starter: 5mb / Publisher: 100mb / Business: 250mb / Custom: 1gb" | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 5 MB | bytes: 5000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: CDN-served; free tier has no egress billing. Fair Use Policy applies to media hosting. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 5 MB [1]
- limits note: Per-object-cap 5 MB (free/Starter), 100 MB (Publisher), 250 MB (Business), 1 GB (Custom). No file-count cap on any plan. Ghost Fair Use Policy constrains 'other file types made available'. Enforcement is the practical ceiling.
- interface detail: rest
- tooling: Ghost Content API + Admin API (REST), official JS SDK. Self-hosted Ghost has no file-count or size limit except the web server config: "The upload limit is effectively determined by the web server that's serving your Ghost site."
- composes with: The interesting half is not Ghost(Pro). It is that Ghost's unlimited-file design means a self-hosted Ghost on any free host inherits an unbounded media library. That chains Ghost's admin API to whatever free compute/storage is already available, rather than being storage itself.
- reliability: Ghost(Pro) free trial expires; the unlimited-file behaviour only persists on a paid plan or self-hosted install.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: "When uploading media files to Ghost, while there is no limit on the number of files you can upload to your site, there is a file size limit based on your Ghost(Pro) plan. Free trial: 5mb / Starter: 5mb / Publisher: 100mb / Business: 250mb / Custom: 1gb"
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: per-plan 5mb/100mb/250mb/1gb table, "no limit on the number of files"
  - [2] 2026-10-21: limit is the web server's on self-hosted
- sources:
  - [1] https://ghost.org/help/media-file-size-limits/
  - [2] https://forum.ghost.org/t/media-upload-limits-hosted-vs-self-hosted/52476
