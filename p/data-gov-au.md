# data.gov.au

> data.gov.au | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov-au/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov-au.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov.au

- `storage/data-gov-au` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:32.920Z (live) | stale on 2026-12-04
- url https://data.gov.au/api/3/action/package_search?rows=0
- free tier: none reachable: CloudFront returns 403 'Request blocked' for both the API and the register page, so no probe was possible. Publishing is in any case restricted to Australian government agenci | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution | detail: account with an email ending in .gov.au or .edu.au; membership of a federal, state or local government organisation and permission from that organisation to publish on its behalf
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
  - [3] 2026-11-19: publishing requires a government-organisation email, so registration is institution-gated | capture: sha256:3df3c4a059beea3b1d28c5576f2434b83407b95d343e1b02fe7f5a82e496e4a9 | quote: If you intend to publish data to data.gov.au, you will need to register an account with an email belonging to a federal, state or local government organisation (i.e. email ending in .gov.au or .edu.au).
  - [4] 2026-11-19: the first-party about page says the portal publishes agency data | capture: sha256:b9442c915874e72eb8b32af5e026e7771438795912e310c8ce140812165300b8 | quote: Data.gov.au is the central source of Australian open government data. Anyone can access the public data published by federal, state and local government agencies.
  - probe:https://data.gov.au/user/register 2026-11-19: the first-party register page answered HTTP 403 | capture: sha256:91e3e495ac514ad0ae913d95c7de64286a84259801d4b413cf487360117772ec | quote: "status": 403
- sources:
  - [1] https://data.gov.au/api/3/action/package_search?rows=0
  - [2] https://data.gov.au/user/register
  - [3] https://data.gov.au/user-guide/getting-started/creating-account
  - [4] https://data.gov.au/about
