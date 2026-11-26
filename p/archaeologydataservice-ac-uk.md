# ads

> archaeologydataservice.ac.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archaeologydataservice-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/archaeologydataservice-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ads (archaeology data service)

- `storage/ads` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:53.937Z (live) | stale on 2026-12-04
- url https://archaeologydataservice.ac.uk/deposit-data/
- free tier: None reachable: Deposit is curated and costed per project via the 'Ingest' system; a registered account is required 'so that the ADS can manage your data deposits' and you 'receive costing information'. I. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the first-party page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the first-party page states no retention period for stored bytes | source: [1]
- egress: stated-absent: the first-party page states no egress terms for stored bytes | metered: no
- identity: email | detail: An email address and password are required to register, plus contact details and, where applicable, the organisation represented.
- interface: unknown
- interface detail: stated-absent: the first-party deposit page describes a curated deposit service and states no storage client interface
- tooling: not documented
- composes with: stated-absent: the first-party page states no way to chain byte storage with other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Deposit is curated and costed per project via the 'Ingest' system; a registered account is required 'so that the ADS can manage your data deposits' and you 'receive costing information' — i.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Deposit is curated and costed per project via the 'Ingest' system; a registered account is required 'so that the ADS can manage your data deposits' and you 'receive costing information' — i.
  - [2] 2026-10-21: cited as the basis of the rejection: Deposit is curated and costed per project via the 'Ingest' system; a registered account is required 'so that the ADS can manage your data deposits' and you 'receive costing information' — i.
  - [1] 2026-11-19: deposit is a curated repository service, not a free storage allowance | capture: sha256:76bc6abee4b77096b9e0a74b15b962504b79ca618334afe5adb638bdbb642b58 | quote: Depositing your data in our world leading accredited repository ensures that they will be professionally curated in the long term and easily accessible for future re-use.
  - [2] 2026-11-19: an email address and password are required to register for the deposit system | capture: sha256:633259de72f889d08d4fc48c2c2c2f03f951d1dddef101ff4377990142d1ff65 | quote: To create an account we need an email address (this will become the login for your ADS-easy account) and password, alongside some contact details for you and the organisation you represent (if appropriate).
- sources:
  - [1] https://archaeologydataservice.ac.uk/deposit-data/
  - [2] https://archaeologydataservice.ac.uk/help-guidance/ads-easy-guidance/ads-easy-account-management/
