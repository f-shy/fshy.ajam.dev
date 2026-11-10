# Estonia e-Residency

> e-resident.gov.ee | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/e-resident-gov-ee/ | JSON https://fshy.ajam.dev/api/v1/entity/e-resident-gov-ee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Estonia e-Residency

- `storage/estonia-e-residency` | fails-quota | evidence reported | binding none | category gov-digital-identity
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.e-resident.gov.ee/
- free tier: None. The programme issues a digital identity card + DigiDoc software and the right to run an EU company; it confers no storage allocation of any kind. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: n/a. | metered: no
- identity: national-id | detail: national-id
- interface: unknown
- limits note: Fails on quota outright (0 GB). Also costs a state fee and requires an in-person card pickup at an embassy. So it is slower and pricier than any qualifying provider while delivering no bytes.
- interface detail: Digital signature / authentication (X-Road, DigiDoc). Not a storage API.
- tooling: DigiDoc client; no object store.
- composes with: n/a.
- reliability: genuinely open to non-residents (that is its purpose) and would solve the identity problem for EU services generally, but carries no storage — recorded here because it is the canonical 'does e-residency come with storage' question and the answer is no.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: None. The programme issues a digital identity card + DigiDoc software and the right to run an EU company; it confers no storage allocation of any kind.
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: the four steps are: apply online, wait for approval and card delivery, pick up card in person ('bring with you your ID'), set up card with DigiDoc. No storage, hosting or cloud component anywhere in the process.
- sources:
  - [1] https://www.e-resident.gov.ee/become-an-e-resident/
