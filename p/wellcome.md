# wellcome trust

> wellcome.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wellcome/ | JSON https://fshy.ajam.dev/api/v1/entity/wellcome.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wellcome Trust - storage as a claimable grant cost

- `storage/wellcome-trust-storage-as-a-claimable-grant-cost` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:32.842Z (live) | stale on 2026-12-04
- url https://wellcome.org/research-funding/guidance/managing-grant/costs-grantholders-can-claim
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
  - [1] 2026-11-19: large-scale data storage remains an allowable service charge on the live costs page | capture: sha256:da9b0a643561cf777c0be4c35edf915558ebe90795fc036b35fe81b65de330ae | quote: This includes costs charged by an external supplier to deliver a piece of work (for example, sequencing costs, antibody production, large-scale data storage or providing expert consultancy advice).
  - [1] 2026-11-19: the data management and sharing plan costs line is still published | capture: sha256:da9b0a643561cf777c0be4c35edf915558ebe90795fc036b35fe81b65de330ae | quote: ### Data management and sharing plan costs Includes costs associated with delivering data management and sharing plans.
- sources:
  - [1] https://wellcome.org/research-funding/guidance/managing-grant/costs-grantholders-can-claim

## wellcome trust, alfred p. sloan, gordon and betty moore, nsf supplements (a

- `storage/wellcome-trust-alfred-p-sloan-gordon-and-betty-moore-nsf` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:51.191Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/wellcome.md
- free tier: none reachable: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the Sloan grants page states what the foundation will not fund and states no per-object size cap | note: not applicable
- retention: stated-absent: the Sloan grants page states what the foundation will not fund and states no retention period for stored bytes
- egress: stated-absent: the Sloan grants page states what the foundation will not fund and states no egress terms for stored bytes | metered: no
- identity: institution
- interface: unknown
- interface detail: stated-absent: these are research-funding organisations that award grants to institutions and fund storage as a grant cost; they expose no storage client interface
- tooling: not documented
- composes with: stated-absent: these are grant funders that pay storage costs on a grant held by an administering institution; the first-party page states no service-chaining mechanism for byte storage
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All four fund organisations, not people. Wellcome pays 'large-scale data storage' only as a service charge on a grant held by an administering organisation. Sloan states plainly 'The…
  - [1] 2026-11-19: Wellcome pays storage as a reimbursable cost on a grant held by an administering organisation, not as a free service a person can sign up for | capture: sha256:da9b0a643561cf777c0be4c35edf915558ebe90795fc036b35fe81b65de330ae | quote: You can claim costs detailed in your award letter. All costs charged to a grant must be auditable. Your administering organisation must be able to justify and account for all expenditure incurred.
  - [2] 2026-11-19: the first-party funder page states grants go to organisations, not individuals, and states no storage client interface | capture: sha256:1a870ebfbbe6b33b4dce60cc00d708016ed9cdce9f76dffe794f019292dc9420 | quote: The Foundation does not make grants to individuals except through its [Books](https://sloan.org/programs/public-understanding/books) program.
- sources:
  - [1] https://wellcome.org/research-funding/guidance/managing-grant/costs-grantholders-can-claim
  - [2] https://sloan.org/grants/apply/what-we-do-not-fund
