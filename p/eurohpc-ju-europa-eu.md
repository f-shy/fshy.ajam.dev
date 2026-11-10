# PRACE

> eurohpc-ju.europa.eu | Compute, Storage; 7 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eurohpc-ju-europa-eu/ | JSON https://fshy.ajam.dev/api/v1/entity/eurohpc-ju-europa-eu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EuroHPC AI Factories

- `compute/eurohpc-ai-factories` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en
- free tier: Fast Lane access offers up to 50,000 GPU hours for a maximum of three months, with approval within four working days on a rolling first-in-first-out basis and expert support from the hosting AI Factory; Playground access sits below it for entry-level users. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: fast-turnaround allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The call requires the applicant organisation to prove its status with a valid VAT number and a Participant Identification Code, and requires the PI to hold an employment contract in that organisation, which excludes a person with no registered company. [1]
- limits note: The call requires the applicant organisation to prove its status with a valid VAT number and a Participant Identification Code, and requires the PI to hold an employment contract in that organisation, which excludes a person with no registered company.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Playground access is explicitly pitched as the way to gather the technical data that a Fast Lane or Large Scale application needs, so the two tiers form a ladder from a small test to 50,000 GPU hours, provided the applicant is a company.
- reliability: no reliability event recorded
- notes: This is the largest single GPU-hour number found that is not gated on peer-reviewed science: 50,000 GPU hours, four working days, no competitive selection. earlier readings already holds a storage-side row rejecting Playground access as 'industry only' with verdict fails-quota; that row is not wrong but it records no number. The binding constraint here is not the industry framing, it is the VAT number and PIC, which is the concrete thing a single person lacks. Classified as fails-identity rather than fails-quota because the size is not the objection. The Playground per-application GPU-hour cap is published only in a system table that did not render through automated retrieval, so it is null here.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: fast-turnaround allocation
  - facets.shape.gpu_class: system-dependent (LUMI MI250X, JUPITER GH200, Leonardo A100, MareNostrum 5 H100)
- evidence:
  - [1] 2026-10-22: 'requiring up to 50,000 GPU hours for a maximum of 3 months' with approval within 4 working days on FIFO, quoted
  - [2] 2026-10-22: 'The status of the organization will need to be proven by providing the valid organization VAT number and, if applicable, the Participant Identification Code (PIC)', quoted
  - [2] 2026-10-22: 'the Principal Investigator has an employment contract in the organisation at the time of proposal submission and valid for at least 3 months after the end of the allocation period', quoted
  - [3] 2026-10-22: 'The Industrial Innovation Access modes are open and free-of-charge to AI SMEs (including startups) for innovation purposes', quoted
  - [4] 2026-10-22: 'For More than 50,000 GPU hours'; 'Access is granted within 10 working days from cut-off date'; allocations for 3, 6 or 12 months, quoted
  - [4] 2026-10-22: deadline model multiple cut-off, roughly two per month from 30 Jan 2026 through 4 Jan 2027, quoted
  - [5] 2026-10-22: 'Your organization must be a startup, SME or other industrial organization. AI for Industrial Innovation calls are not open for academic use or public sector organizations'; 'Your organization must have a valid VAT number'; 'must be incorporated in a Horizon 2020 country', quoted
  - [6] 2026-10-22: LUMI AI Factory Large Scale gives 'over 50.000 GPU hours, up to 1 year' free of charge for eligible companies, reported by the hosting entity
  - [5] 2026-10-22: AI Factory call table: Playground '<= 5,000' GPU hours, Fast Lane '5,001 - 50,000', Large Scale '> 50,000', published by the LUMI hosting entity
  - [7] 2026-10-22: 'Applications will be processed in the order they are received. There is no competitive selection process and access can be granted within two working days'; allocations for 1, 2 or 3 months, quoted
  - [8] 2026-10-22: 'The AI Factories for Industrial Innovation call is open for applicants coming from industrial sector only'; 'Access time offered via the EUROHPC JU access calls is free of charge', quoted
  - [9] 2026-10-22: 'Please note that individual persons or temporary teams are not entitled to our services', quoted
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes/fast-lane-access-ai-factories_en
  - [2] https://www.eurohpc-ju.europa.eu/document/download/bd7aa666-bdf3-4436-b5ec-0b34a781e817_en?filename=Terms%20of%20Reference%20-%20AIF%20Access%20Calls.pdf
  - [3] https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en
  - [4] https://www.eurohpc-ju.europa.eu/large-scale-access-ai-factories_en
  - [5] https://lumi-supercomputer.eu/technical-guide-for-compute-proposals/
  - [6] https://lumi-ai-factory.eu/large-scale-access-to-lumi-ai-factory/
  - [7] https://www.eurohpc-ju.europa.eu/playground-access-ai-factories_en
  - [8] https://www.eurohpc-ju.europa.eu/ai-factories/faqs-ai-factories_en
  - [9] https://lumi-ai-factory.eu/pricing-and-eligibility/

## EuroHPC JU Benchmark

- `compute/eurohpc-ju-benchmark` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en
- free tier: A continuously open call with monthly cut-offs, giving a limited number of node hours for code scalability tests or AI application tests before applying for Regular or Extreme Scale access; the maximum allocation period is three months, with a maximum time-to-resources-access of two to three weeks. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / benchmark allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The benchmark tier is the cheapest door in the EuroHPC stack, but it is still awarded through a proposal evaluated by the Access Resource Committee, and the call text targets researchers and HPC application developers established in an EU Member State or a Horizon-associated country. [1]
- limits note: The benchmark tier is the cheapest door in the EuroHPC stack, but it is still awarded through a proposal evaluated by the Access Resource Committee, and the call text targets researchers and HPC application developers established in an EU Member State or a Horizon-associated country.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The benchmark result is designed to feed a Regular or Extreme Scale proposal, so the tier's real value is the scaling data it produces, not the node hours.
- reliability: no reliability event recorded
- notes: The maximum node-hour figure per system is not stated in the call body; the page says the exact amount is subject to the systems participating in each cut-off. A number here would be invented, so it is null. The eligibility sentence comes from the Regular Access page, whose terms the benchmark call shares; the benchmark call's own information-for-applicants PDF was not opened, so the precise benchmark eligibility wording is one step removed and is the thing to check if a reconciler wants this rung raised.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / benchmark allocation
  - facets.shape.gpu_class: system-dependent (LUMI MI250X, JUPITER GH200, Leonardo A100)
- evidence:
  - [1] 2026-10-22: 'Users receive a limited number of node hours; the maximum allocation period is three months', quoted
  - [1] 2026-10-22: deadline model multiple cut-off with monthly dates from 1 Jan 2026 to 31 Dec 2033, quoted
  - [1] 2026-10-22: 'a first-come-first-serve principle will be applied and proposals will be awarded according to the available monthly quota of resources', quoted
  - [2] 2026-10-22: Regular Access meta description: 'Researchers from academia, research institutes, public authorities, and industry established or located in an EU Member State or in a country associated with Horizon 2020 can apply'…
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en
  - [2] https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en

## EuroHPC JU Regular Access (LUMI, Leonardo, MareNostrum 5, JUPITER)

- `storage/eurohpc-ju-regular-access` | fails-identity | evidence documented | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-12-05
- url https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en
- free tier: LUMI-O object storage: 150 TB default quota per project, expandable up to 2.1 PB, retained for the project lifetime, billing rate 0.25x. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: Access to EuroHPC systems is free of charge.
- per-object cap: source: [1] | note: not stated
- retention: LUMI-O object storage is retained for the project lifetime. | source: [1] | note: not stated
- egress: Free for allocation holders within the facility; object storage endpoints (LUMI-O S3) are internet-reachable. | metered: no
- identity: institution | detail: Applicants must be researchers from academia, research institutes, public authorities or industry established or located in an EU Member State, a Participating State or a third country associated to the Digital Europe Programme or to Horizon Europe.
- interface: s3-compatible, rclone
- limits:
  - retention-clamped: allocations are granted for one (1) year [2]
- limits note: Geography is the hard gate: eligibility is limited to entities 'established or located in an EU Member State or in a Participating State or in a third country associated to the Digital Europe Programme or to Horizon Europe'. The published country list runs to ~45 states (incl. Turkiye, Tunisia, Ukraine, Georgia, Armenia, Israel, UK) and excludes everyone else. Allocations are one year; ~4 months from cut-off to access.
- binding note: the default object storage quota reaches the stored-volume need; the gate is eligibility (identity), not quota: applicants must be established or located in an eligible state
- interface detail: s3
- tooling: LUMI-O is S3-compatible (rclone 's3'); other sites expose Lustre/POSIX plus Globus.
- composes with: Storage comes attached to a compute award, so a storage-heavy proposal can be packaged inside a modest compute request. One-year allocations with successive cut-offs allow re-application.
- reliability: Well-run; the constraint is purely eligibility and the compute-justification burden.
- notes: Node-hours plus an associated storage quota set by the hosting entity (LUMI-O alone defaults to 150 TB per LUMI project). Not a standalone storage call.
- evidence note: Documented from vendor pages re-read on 2026-11-04: https://docs.lumi-supercomputer.eu/storage/ (LUMI-O 150 TB, project lifetime), https://www.eurohpc-ju.europa.eu/supercomputers/supercomputers-access-policy-and-faq_en (free of charge; eligibility) and https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en (one-year allocations).
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Node-hours plus an associated storage quota set by the hosting entity (LUMI-O alone defaults to 150 TB per LUMI project). Not a standalone storage call.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: eligible-country list; 'Researchers from academia, research institutes, public authorities, and industry established or located in an EU Member State or in a Participating State...'
  - [2] 2026-10-21: 'The allocations are granted for one (1) year'; cut-offs 30 Mar 2026 / 4 Sep 2026; tracks Scientific / Industry / Public Administration
  - [3] 2026-11-03: LUMI-O object storage: 150 TB quota, expandable up to 2.1 PB, retained for the project lifetime, billing rate 0.25x | capture: sha256:ac3a527daab5ffd4d026df2c871220b561ca9791e1af6d05cb07fd14ac2d1820 | quote: | Object storage | 150 TB | 500M (500k/bucket) | Yes, up to 2.1 PB | project lifetime | 0.25x |
  - [1] 2026-11-03: access is free of charge | capture: sha256:66f092ce08ed3b985915f89112d99be28f920e3c88c1927615f543809a73e361 | quote: Currently access is free of charge.
  - [2] 2026-11-03: regular access allocations are granted for one year | capture: sha256:b910e1d7be4ff424cb4a401d0ad780c2a7538defa772dc2775bfc040bdd53a57 | quote: Type of access: The allocations are granted for one (1) year.
  - [1] 2026-11-03: access is for researchers from academia, research institutes, public authorities and industry established or located in eligible states | capture: sha256:66f092ce08ed3b985915f89112d99be28f920e3c88c1927615f543809a73e361 | quote: Researchers from academia, research institutes, public authorities, and industry established or located in an EU Member State or in a Participating State or in a third country associated to the Digital Europe Programme or to Horizon Europe
  - [2] 2026-11-03: allocations are granted for one year | capture: sha256:b910e1d7be4ff424cb4a401d0ad780c2a7538defa772dc2775bfc040bdd53a57 | quote: Type of access: The allocations are granted for one (1) year.
  - [1] 2026-11-04: access is for researchers from academia, research institutes, public authorities and industry in eligible states | capture: sha256:66f092ce08ed3b985915f89112d99be28f920e3c88c1927615f543809a73e361 | quote: Researchers from academia, research institutes, public authorities, and industry established or located in an EU Member State or in a Participating State or in a third country associated to the Digital Europe Programme or to Horizon Europe
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/supercomputers/supercomputers-access-policy-and-faq_en
  - [2] https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en
  - [3] https://docs.lumi-supercomputer.eu/storage/

## eu ai factories — playground access

- `storage/eu-ai-factories-playground-access` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.eurohpc-ju.europa.eu/playground-access-ai-factories_en
- free tier: None reachable: Free, FIFO, no competitive selection, access within 2 working days. The closest thing in Europe to a self-serve allocation. But it is aimed at 'Industry users' (SMEs/startups) and opens a 1. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Free, FIFO, no competitive selection, access within 2 working days — the closest thing in Europe to a self-serve allocation. But it is aimed at 'Industry users' (SMEs/startups) and opens a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free, FIFO, no competitive selection, access within 2 working days — the closest thing in Europe to a self-serve allocation. But it is aimed at 'Industry users' (SMEs/startups) and opens a…
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/playground-access-ai-factories_en

## eurohpc benchmark access (as a storage route)

- `storage/eurohpc-benchmark-access` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en
- free tier: none reachable: Explicitly a short pre-allocation test: 'Users receive a limited number of node hours; the maximum allocation period is three months.' No storage allocation and no renewal path beyond… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Explicitly a short pre-allocation test: 'Users receive a limited number of node hours; the maximum allocation period is three months.' No storage allocation and no renewal path beyond…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly a short pre-allocation test: 'Users receive a limited number of node hours; the maximum allocation period is three months.' No storage allocation and no renewal path beyond…
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en

## eurohpc ju benchmark access as a storage route

- `storage/eurohpc-ju-benchmark-access-as-a-storage-route` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en
- free tier: none reachable: Benchmark access gives 'a limited number of node hours; the maximum allocation period is three months' for code-scaling tests. No storage allocation is described at all. Regular/Extreme… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Benchmark access gives 'a limited number of node hours; the maximum allocation period is three months' for code-scaling tests. No storage allocation is described at all. Regular/Extreme…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Benchmark access gives 'a limited number of node hours; the maximum allocation period is three months' for code-scaling tests. No storage allocation is described at all. Regular/Extreme…
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-benchmark-access_en

## PRACE

- `compute/prace` | dead | evidence documented | binding none | category national HPC allocation
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.eurohpc-ju.europa.eu/supercomputers/supercomputers-access-policy-and-faq_en
- free tier: PRACE no longer runs its own access calls; at the end of 2022 the EuroHPC JU took over management of the peer-review and support process, and the PRACE site now serves an archive of calls that closed in 2023. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: unknown
- limits note: There is nothing left to apply for: the programme's allocation function moved into the EuroHPC JU, so the successor question is answered by the EuroHPC rows rather than by a PRACE row.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: PRACE's review machinery is the same machinery now operating the EuroHPC calls, so its successor is the EuroHPC Benchmark, Development, Regular and Extreme Scale set recorded elsewhere in documented records.
- reliability: no reliability event recorded
- notes: The answer is that the successor is not a separate brand: it is the EuroHPC JU, which absorbed PRACE's peer-review process at the end of 2022. No quota is recorded because there is no live call. Identity cost is recorded as 'none' rather than a normal vocabulary value, because a withdrawn programme has no applicant and no identity to produce; recording 'institution' here would imply a door that no longer exists.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'At the end of 2022, the EuroHPC JU, as owner of an increasing number of world-class European supercomputers, took over from PRACE the management of this peer-review and support process', quoted
  - [2] 2026-10-22: PRACE's Regular Access page lists its last open call as the 2023-07-07 cut-off and files every later item under 'Closed Calls'
- sources:
  - [1] https://www.eurohpc-ju.europa.eu/supercomputers/supercomputers-access-policy-and-faq_en
  - [2] https://prace-ri.eu/prace-archive/legacy-hpc-access/eurohpc-access/eurohpc-ju-regular-access-mode/
