# Digital Research

> alliancecan.ca | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alliancecan/ | JSON https://fshy.ajam.dev/api/v1/entity/alliancecan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Digital Research Alliance of Canada — 1 TB default object storage per project, up to 40 TB project / 100 TB nearline via Rapid Access Service

- `storage/digital-research-alliance-of-canada-1-tb-default-object` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-01T18:05:17.595Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.alliancecan.ca/wiki/Arbutus_object_storage
- free tier: 'All Arbutus projects are allocated a default 1TB of object storage. If more is required, you can either request an additional 9TB available through our Rapid Access Service. More than 10TB must be requested and allocated under the annual Resource Allocation Competition.' The RAS policy adds: PIs 'can request additional storage resources in any General Purpose cluster without submitting a RAC application, up to a maximum of 40 TB of project storage and 100 TB of nearline storage', with the total across all clusters capped at those numbers. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered egress. OpenStack Swift and S3 interfaces serve objects over HTTPS, and buckets can be configured for public read access. | metered: yes
- identity: institution | detail: an account is registered on the CCDB portal. The Principal Investigator role that requests the storage is an academic PI: a full- or part-time faculty member, an adjunct faculty member, or a librarian at a Canadian university, college or research hospital eligible to hold Canada Foundation for Innovation grants; a lead researcher at an eligible Canadian research institute is the second route, and industry, non-profit and government researchers apply for paid access through a regional organisation. A sponsored user needs no affiliation of their own but 'require a sponsor to create an account on CCDB'. No card and no phone number is asked for.
- interface: s3, rclone, cli
- limits:
  - write-gated (binding): application, up to a maximum of 40 TB of project storage and 100 TB of nearline storage', w [1]
- limits note: Per-object-cap: not documented for Arbutus. Retention: object storage is not backed up. 'management of a project's object storage containers is self-service. This includes operations such as backups because the object store itself is not backed up.' request-rate: not published. Gate: CCDB account (institutional), and storage above 10 TB requires an email to support@tech.alliancecan.ca from a PI.
- interface detail: s3
- tooling: OpenStack Swift or S3 against the Arbutus object store; rclone/swift/s3cmd all work. 'We offer access to the OpenStack Object Store via two different protocols: Swift or Amazon Simple Storage Service (S3). ... object storage containers and objects created with Swift or S3 can be accessed using both protocols.'
- composes with: Allocation provides 1 TB default, 9 TB via Resource Allocation Competition, and up to 40 TB project storage per principal investigator upon email request. Nearline tape storage provides up to 100 TB.
- reliability: Not backed up and self-managed; the docs are Anubis-protected (proof-of-work challenge) which also means scraping the current page fails and you must read the archived copy.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: captured 2024-09-14 via Wayback: 'All Arbutus projects are allocated a default 1TB of object storage... request an additional 9TB available through our Rapid Access Service. More than 10TB must be requested and allocated under the annual Resource Allocation Competition.'
  - [2] 2026-10-21: 'up to a maximum of 40 TB of project storage and 100 TB of nearline storage. These resources can be requested all in one cluster or split across multiple ones, but the total amount across all clusters must not exceed 40 TB of project storage or 100 TB of nearline storage.'
  - withheld 2026-10-21: firecrawl provider -> returns the Wikipedia language-list boilerplate; Wayback capture of the same URL -> also Anubis 'Sad Anubis / Access Denied'. Documented as a challenge-walled host; numbers above come from the 2024-09-14 capture, which predates the wall.
  - [3] 2026-10-21: probe: curl -> 302 (host alive, redirects to auth)
  - [4] 2026-11-01: an account outside that affiliation exists only as a sponsored user of a PI, so the identity is still an institution | capture: sha256:9b826889e75e19a67059789e738e1c8bf14939c1b7ad94e1579d9f3947861f40 | quote: Sponsored User: any individual whom a Principal Investigator has identified and approved for access to resources and services.
  - [5] 2026-11-01: access to a system is a separate request after the account, by the PI and each sponsored user | capture: sha256:3e0148c4cca366044c9ca1899637b88a5716042b711eec17d1fdbde2a54f5272 | quote: To use any computational resource offered by the Alliance, the PI and any sponsored user that needs those resources must first request access to the desired system(s) in this page
  - [6] 2026-11-01: the CCDB registration form is an agreements screen, and the allocation is a separate request | capture: sha256:0461ffd074fd063584614ebfe32015ad3e7d0340ba02baca6f277d93d2bcb7ef | quote: I have read, understood, and agree that my use of Alliance Federation Systems and Services will be consistent with the Policies, Standards, Terms, and Procedures of the Alliance Federation
- sources:
  - [1] https://docs.alliancecan.ca/wiki/Arbutus_object_storage
  - [2] https://ualberta-rcg.github.io/ragflow-wiki-data/base/policies/rapid_access_service/
  - [3] https://arbutus.cloud.computecanada.ca/
  - [4] https://docs.alliancecan.ca/wiki/User_roles_to_access_resources_and_services_of_the_Alliance_Federation
  - [5] https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/rapid-access-service
  - [6] https://ccdb.alliancecan.ca/account_application

## Digital Research Alliance

- `compute/digital-research-alliance` | fails-identity | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://alliancecan.ca/en/services/advanced-research-computing/research-portal/resource-allocation-competitions
- free tier: Canada's national platform ran about 233,000 CPU cores, 62,000 virtual CPUs, 2,610 GPUs and 150 PB of storage across Cedar, Graham, Niagara, Beluga and Arbutus. It reserves "a target of 20% for researchers to use through the Rapid Access Service (RAS), which grants all users access to modest quantities of compute, storage and cloud resources as soon as they have a Compute Canada account", against 80% allocated competitively. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits note: no binding constraint identified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: no open question recorded
- evidence:
  - [2] 2026-10-22: "approximately 233,000 CPU cores, 62,000 virtual CPUs, 2,610 GPUs and 150 PB of storage on Cedar [...] Graham [...] Niagara [...] Beluga [...] and Arbutus", quoted
  - [2] 2026-10-22: "the CCF reserves a target of 20% for researchers to use through the Rapid Access Service (RAS), which grants all users access to modest quantities of compute, storage and cloud resources as soon as they have a Compute Canada account", quoted
  - [3] 2026-10-22: to apply to a Resource Allocation Competition, PIs and Co-PIs must "be a faculty member at a Canadian academic institution" and "have an active Alliance account with an Academic Principal Investigator role", quoted
  - [2] 2026-10-22: the 2021 competition awarded 40 percent of CPU core years requested, 90 percent of storage and 22 percent of GPUs requested, quoted
- sources:
  - [1] https://alliancecan.ca/en/services/advanced-research-computing/research-portal/resource-allocation-competitions
  - [2] https://alliancecan.ca/en/services/advanced-research-computing/research-portal/resource-allocation-competitions/2021-resource-allocations-competition-results
  - [3] https://www.uoguelph.ca/research/alerts/content/digital-research-alliance-canada-2024-annual-resource-allocation-competition
