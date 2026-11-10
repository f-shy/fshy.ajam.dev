# nsf access

> access-ci.org | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/access-ci/ | JSON https://fshy.ajam.dev/api/v1/entity/access-ci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ACCESS

- `compute/access` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://allocations.access-ci.org/allocations-policy
- free tier: Explore ACCESS provides up to 400,000 ACCESS Credits, accepted anytime with no deadline, reviewed in one to two business days, lasting 12 months; Discover ACCESS 1,500,000 and Accelerate ACCESS 3,000,000 credit tiers sit above it. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-light credit allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: institution: the allocations policy states 'Principal Investigators (PIs) and users must now be affiliated with an eligible organization' and 'Unaffiliated individuals are no longer eligible to request or be added to an ACCESS allocation'; A card, hold, phone number or ID document is not mentioned in any evidence row: unknown. Country: United States only.
- interface: unknown
- limits:
  - write-gated (binding): The allocations portal refuses a request from any person based outside the US or holding a non-organisational email address, and the policy bans unaffiliated, self-employed and retired people outright, so no identity a registrant can produce passes the first screen. [1]
- limits note: The allocations portal refuses a request from any person based outside the US or holding a non-organisational email address, and the policy bans unaffiliated, self-employed and retired people outright, so no identity a registrant can produce passes the first screen.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None available as a PI. The only route in is as a named user on a project led by an eligible US-based researcher, which requires a US collaborator and PI justification for each non-US user.
- reliability: no reliability event recorded
- notes: Refutation of the common claim that ACCESS is open to anyone with an email. Before July 2025 the programme was far more open; NSF Important Notice No. 149 tightened affiliation, email domain and international restrictions. Tier sizes come from a resource provider's documentation rather than the ACCESS site itself, so the 400K/1.5M/3M figures sit one rung below the policy quotes. No GPU-hour figure is published because credits convert to different resource units per provider; a conversion would be invented, so the field is null.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-light credit allocation
- evidence:
  - [1] 2026-10-22: 'Principal Investigators (PIs) and users must now be affiliated with an eligible organization. Unaffiliated individuals are no longer eligible to request or be added to an ACCESS allocation', quoted
  - [1] 2026-10-22: 'If you are based outside of the U.S., regardless of your institutional affiliation (and this includes international campuses of U.S. institutions), you are not eligible to lead an ACCESS allocated project', quoted
  - [1] 2026-10-22: 'The allocations website will not permit non-U.S.-based persons or persons with generic email addresses to initiate allocations requests', quoted; changes attributed to NSF Important Notice No. 149 of 10 July 2025
  - [1] 2026-10-22: 
  - [2] 2026-10-22: credit thresholds by tier: Explore 400,000, Discover 1,500,000, Accelerate 3,000,000, reported by the Jetstream2 provider documentation
- sources:
  - [1] https://allocations.access-ci.org/allocations-policy
  - [2] https://docs.jetstream-cloud.org/alloc/overview/

## nsf access / open storage network (as an individual route)

- `storage/nsf-access-open-storage-network` | fails-identity | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T01:24:31.184Z (live) | stale on 2026-12-05
- url https://allocations.access-ci.org/allocations-policy
- free tier: 10 TB to 50 TB of S3-compatible storage per project through the ACCESS allocation process, at no cost to researchers; an allocation needs an eligible ACCESS project. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: ACCESS allocates resources at no cost to researchers, OSN storage included; the OSN documentation gives a rate of 3,000 ACCESS credits per 1 TB.
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: Bucket storage is never purged and not backed up. | source: [1]
- egress: not recorded | metered: no
- identity: institution | detail: A PI must be a researcher or educator based in the U.S. and affiliated with an eligible organisation; persons based outside the U.S. cannot request or lead an allocation, and users must be affiliated with an eligible organisation.
- interface: s3-compatible
- limits:
  - volume-quota: 50 TB per-project quota, shared across all buckets in the project [2]
- binding note: the allowance reaches the stored-bytes need; the eligibility gate (organisational affiliation, U.S.-based PI) is what blocks an unaffiliated individual
- interface detail: S3-compatible buckets with an endpoint URL, a bucket name and up to two key pairs; no shell or mounted filesystem.
- tooling: AWS CLI, Cyberduck, Rclone and Restic against the bucket endpoint; buckets and keys are created in the OSN portal.
- composes with: not recorded
- reliability: Eligibility changed under NSF Important Notice No. 149 (July 10, 2025): an organisational affiliation is required and persons based outside the U.S. cannot lead an allocation.
- notes: OSN storage is allocated through ACCESS credits; the OSN documentation gives a first exchange of 10 TB and supplements up to 50 TB; above 50 TB the OSN team is contacted.
- evidence note: documented: the project allocation range, the S3-compatible bucket storage and the per-project quota were read on 2026-11-03 at https://support.access-ci.org/documentation/resources/osn, and the organisational-affiliation and U.S.-based PI requirements at https://allocations.access-ci.org/allocations-policy.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: OSN was 1-50 TB via ACCESS. ACCESS has since tightened under NSF Important Notice No. 149 (2025-07-10) for users based outside the U.S.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: OSN was 1-50 TB via ACCESS. ACCESS has since tightened under NSF Important Notice No. 149 (2025-07-10) for users based outside the U.S.
  - [2] 2026-11-03: OSN project allocations run from 10 TB to 50 TB through ACCESS | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: Project allocations run from 10 TB to 50 TB through the standard ACCESS process.
  - [2] 2026-11-03: unit is TB | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: Project allocations run from 10 TB to 50 TB through the standard ACCESS process.
  - [2] 2026-11-03: quota is on stored bytes | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: Project allocations run from 10 TB to 50 TB through the standard ACCESS process.
  - [3] 2026-11-03: allocation is at no cost | capture: sha256:80dbb2f3c4fd97e05704401ebd51aecae22b88a3c3b04a92eb4deb4b466a75cd | quote: ACCESS allocates many types of research computing resources at no cost to researchers, including OSN storage.
  - [2] 2026-11-03: S3-compatible object storage | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: OSN is a distributed object-storage resource consisting of S3-compatible storage pods hosted at research institutions across the US.
  - [2] 2026-11-03: the resource is S3-compatible object storage with no shell or mount paths | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: OSN is S3-compatible object storage - no directories, mount paths, or shell access.
  - [2] 2026-11-03: client tools | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: It is reached through standard S3 tooling - AWS CLI, Cyberduck, Rclone and Restic - rather than a login shell or a mounted filesystem.
  - [2] 2026-11-03: purge and backup policy | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: | Bucket storage | | 50 TB | Never purged | Not backed up | Per-project quota, shared across all buckets in the project. Requested and managed in the OSN portal. |
  - [2] 2026-11-03: per-project quota | capture: sha256:cb3a27cb935ae490a75580ec081bcb46cf0fb424a86169792080bbce58c0af37 | quote: | Bucket storage | | 50 TB | Never purged | Not backed up | Per-project quota, shared across all buckets in the project. Requested and managed in the OSN portal. |
  - [1] 2026-11-03: an ACCESS allocation needs an eligible organisational affiliation | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: Unaffiliated individuals are no longer eligible to request or be added to an ACCESS allocation.
  - [1] 2026-11-03: non-U.S. persons cannot lead allocations | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: Persons based outside of the U.S. are not eligible to request or lead ACCESS-allocated projects.
  - [1] 2026-11-03: the 10 TB to 50 TB allowance reaches the need but an unaffiliated individual cannot hold or join an allocation | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: If you’re retired, self-employed, or otherwise unaffiliated, even if you are located in the U.S., you are not eligible to lead an allocation nor eligible to use ACCESS resources as part of any allocated project.
  - [1] 2026-11-03: eligibility was tightened under the notice | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: These changes are in response to NSF Important Notice No. 149 (July 10, 2025) and other federal guidelines.
  - [1] 2026-11-03: eligibility binds, not a named limit | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: Unaffiliated individuals are no longer eligible to request or be added to an ACCESS allocation.
  - [3] 2026-11-03: limit above 50 TB | capture: sha256:80dbb2f3c4fd97e05704401ebd51aecae22b88a3c3b04a92eb4deb4b466a75cd | quote: If your project needs more than 50 TB of OSN storage, please contact us at [help@osn.mghpcc.org](mailto:help@osn.mghpcc.org) for options
  - [1] 2026-11-03: ACCESS eligibility requires an affiliation | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: Unaffiliated individuals are no longer eligible to request or be added to an ACCESS allocation.
  - [1] 2026-11-04: persons based outside the U.S. cannot request or lead ACCESS allocations | capture: sha256:591939b742f447fa99bed8092ebef3610eedf883ff184f27735202571a2e2731 | quote: Persons based outside of the U.S. are not eligible to request or lead ACCESS-allocated projects. In many cases, however, you can collaborate with an eligible U.S.-based project PI and use ACCESS resources. See the next question.
- sources:
  - [1] https://allocations.access-ci.org/allocations-policy
  - [2] https://support.access-ci.org/documentation/resources/osn
  - [3] https://openstoragenetwork.github.io/docs/allocations/
