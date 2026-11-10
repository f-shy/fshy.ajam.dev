# edmond

> mpg.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mpg/ | JSON https://fshy.ajam.dev/api/v1/entity/mpg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## edmond (max planck, edmond.mpdl.mpg.de)

- `storage/edmond` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://edmond.mpdl.mpg.de/api/dataverses/:root/storage/quota?showInherited=true
- free tier: none reachable: 308 permanent redirect to edmond.mpg.de on every path. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: identity
  - dead_end.why: 308 permanent redirect to edmond.mpg.de on every path.
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 308 permanent redirect to edmond.mpg.de on every path.
  - [2] 2026-10-21: cited as the basis of the rejection: 308 permanent redirect to edmond.mpg.de on every path.
- sources:
  - [1] https://edmond.mpdl.mpg.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://edmond.mpg.de/api/
