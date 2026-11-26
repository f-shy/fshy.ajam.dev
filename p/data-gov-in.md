# data.gov.in

> data.gov.in | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-in/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-in.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.in (india)

- `storage/data-gov-in` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.920Z (inherited) | stale on 2026-12-04
- url https://data.gov.in/api/3/action/package_search
- free tier: none reachable: Host did not resolve/connect at all (curl exit 6/000) from this network, so nothing could be verified. India's public-data policy routes publication through ministry nodal officers under… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: unverified: https://www.data.gov.in/ answered a server error through the read service on 2026-11-19; a direct probe of the same first-party URL answered HTTP 200; routes tried: read service, pinned read providers, header fetch, archive, direct probe
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Host did not resolve/connect at all (curl exit 6/000) from this network, so nothing could be verified. India's public-data policy routes publication through ministry nodal officers under…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Host did not resolve/connect at all (curl exit 6/000) from this network, so nothing could be verified. India's public-data policy routes publication through ministry nodal officers under…
  - [2] 2026-10-21: cited as the basis of the rejection: Host did not resolve/connect at all (curl exit 6/000) from this network, so nothing could be verified. India's public-data policy routes publication through ministry nodal officers under the
  - probe:https://www.data.gov.in/ 2026-11-19: the first-party portal answered HTTP 200 to a direct probe | capture: sha256:1069066977be32b8d7014e19d95157395f4d64d7c5dbcc0d22b384c2ca199c9a | quote: "status": 200
- sources:
  - [1] https://data.gov.in/api/3/action/package_search
  - [2] https://data.gov.in/user/register
