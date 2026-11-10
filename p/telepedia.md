# telepedia

> telepedia.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telepedia/ | JSON https://fshy.ajam.dev/api/v1/entity/telepedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## telepedia

- `storage/telepedia` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://static.telepedia.net/metawiki/1/18/favicon.ico
- free tier: none reachable: 15 MB per file (live siteinfo) and the media CDN is 403 to everything: `static.telepedia.net/metawiki/1/18/favicon.ico` returns 403 both direct and through the fetch proxy. Upload-open /… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: read-gated
  - dead_end.why: 15 MB per file (live siteinfo) and the media CDN is 403 to everything: `static.telepedia.net/metawiki/1/18/favicon.ico` returns 403 both direct and through the fetch proxy. Upload-open /…
  - dead_end.retry_when: if the read path opens anonymously
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 15 MB per file (live siteinfo) and the media CDN is 403 to everything: `static.telepedia.net/metawiki/1/18/favicon.ico` returns 403 both direct and through the fetch proxy. Upload-open /…
- sources:
  - [1] https://static.telepedia.net/metawiki/1/18/favicon.ico
