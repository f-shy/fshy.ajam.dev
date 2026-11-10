# wellcome trust

> wellcome.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wellcome/ | JSON https://fshy.ajam.dev/api/v1/entity/wellcome.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wellcome Trust - storage as a claimable grant cost

- `storage/wellcome-trust-storage-as-a-claimable-grant-cost` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wellcome.org/research-funding/guidance/managing-grant/costs-grantholders-can-claim
- disagrees on identity_kind: `storage/wellcome-trust-alfred-p-sloan-gordon-and-betty-moore-nsf` says email, `storage/wellcome-trust-storage-as-a-claimable-grant-cost` says institution
- free tier: No byte quota - 'large-scale data storage' is an allowable service charge, plus a 'Data management and sharing plan costs' line. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Funded as a project cost if justified in the data management plan. | metered: no
- identity: institution
- interface: unknown
- limits note: Grants are held by an administering organisation, not an individual - the applicant needs a host institution. Costs are tied to the award period; storage is not funded in perpetuity.
- interface detail: n/a
- tooling: the same as interface detail
- composes with: The DMP is the lever: storage written into a data management and sharing plan becomes a funded cost for the grant's duration, renewable with the grant.
- reliability: Reliable funder, but the individual cannot be the grantee.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No byte quota - 'large-scale data storage' is an allowable service charge, plus a 'Data management and sharing plan costs' line.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Service charges... (for example, sequencing costs, antibody production, large-scale data storage...)'; separate 'Data management and sharing plan costs' heading
- sources:
  - [1] https://wellcome.org/research-funding/guidance/managing-grant/costs-grantholders-can-claim

## wellcome trust, alfred p. sloan, gordon and betty moore, nsf supplements (a

- `storage/wellcome-trust-alfred-p-sloan-gordon-and-betty-moore-nsf` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- page https://fshy.ajam.dev/p/wellcome.md
- disagrees on identity_kind: `storage/wellcome-trust-alfred-p-sloan-gordon-and-betty-moore-nsf` says email, `storage/wellcome-trust-storage-as-a-claimable-grant-cost` says institution
- free tier: none reachable: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: not recorded | note: not applicable
- retention: not recorded
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
  - dead_end.why: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The…
