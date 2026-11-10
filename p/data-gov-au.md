# data.gov.au

> data.gov.au | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-au/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-au.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.au

- `storage/data-gov-au` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.gov.au/api/3/action/package_search?rows=0
- free tier: none reachable: CloudFront returns 403 'Request blocked' for both the API and the register page, so no probe was possible. Publishing is in any case restricted to Australian government agenci | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: CloudFront returns 403 'Request blocked' for both the API and the register page, so no probe was possible. Publishing is in any case restricted to Australian government agenci
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: CloudFront returns 403 'Request blocked' for both the API and the register page, so no probe was possible. Publishing is in any case restricted to Australian government agenci
  - [2] 2026-10-21: cited as the basis of the rejection: CloudFront returns 403 'Request blocked' for both the API and the register page, so no probe was possible. Publishing is in any case restricted to Australian government agenci
- sources:
  - [1] https://data.gov.au/api/3/action/package_search?rows=0
  - [2] https://data.gov.au/user/register
