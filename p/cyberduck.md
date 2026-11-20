# enter cloud suite object storage

> cyberduck.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyberduck/ | JSON https://fshy.ajam.dev/api/v1/entity/cyberduck.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## enter cloud suite object storage

- `storage/enter-cloud-suite-object-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:35.940Z (live) | stale on 2026-12-04
- url https://docs.cyberduck.io/protocols/openstack/enter_cloud_suite/
- free tier: None. Pay-per-use object storage priced from 0.075 EUR per GB per month; the documented protocol is OpenStack Swift, not S3. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: OpenStack Swift, pay-per-use IaaS, no public price list. Only protocol documentation exists. Zero pricing transparency, and Swift is not S3.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: OpenStack Swift, pay-per-use IaaS, no public price list — only protocol documentation exists. Zero pricing transparency, and Swift is not S3.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: OpenStack Swift, pay-per-use IaaS, no public price list — only protocol documentation exists. Zero pricing transparency, and Swift is not S3.
  - [1] 2026-11-19: the first-party-connected page states a pay-per-use price, so no free storage allocation is given | capture: sha256:121c7da6a1ab4ad640b542514dc1345d33a887b80def66ba048a1f9fbe47585b | quote: You only pay for the space and time you use – starting at 0.075€ per Gb per month – and can even archive data for very short periods of time.
- sources:
  - [1] https://docs.cyberduck.io/protocols/openstack/enter_cloud_suite/
