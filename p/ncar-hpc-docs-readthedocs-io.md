# NSF NCAR

> ncar-hpc-docs.readthedocs.io | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ncar-hpc-docs-readthedocs-io/ | JSON https://fshy.ajam.dev/api/v1/entity/ncar-hpc-docs-readthedocs-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ncar glade (campaign / work / scratch)

- `storage/ncar-glade` | fails-identity | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T01:24:31.181Z (live) | stale on 2026-12-05
- url https://ncar-hpc-docs.readthedocs.io/en/latest/storage-systems/glade/
- free tier: Per-user quotas for account holders: Home 50 GB, Work 2 TB (not purged), Scratch 30 TB and 10 million files (purged after 180 days). Campaign Storage has no default quota and is allocated per project on request. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: Scratch is purged after 180 days; Work is not purged; Campaign Storage is medium-term, typically three to five years. | source: [1]
- egress: not recorded | metered: no
- identity: institution | detail: eligible U.S. post-secondary institution or non-profit research organization; unsponsored requests need a letter from an advisor or department head
- interface: unknown
- limits:
  - retention-clamped: Scratch 30 TB per user, purged after 180 days [1]
  - volume-quota: Work 2 TB per user [1]
  - write-gated: Campaign Storage only by project allocation request [1]
- limits note: Home 50 GB, Work 2 TB, Scratch 30 TB with a 10 million file limit and a 180 day purge; Campaign Storage by allocation request.
- binding note: access needs a project allocation at an eligible institution; scratch is then clamped by a purge
- interface detail: not documented
- tooling: Globus web and command-line transfers to the NSF NCAR Campaign Storage collection; /glade paths on the Derecho and Casper clusters
- composes with: not recorded
- reliability: University Campaign Storage requests are prioritised, not guaranteed; the documentation says NSF NCAR is not currently funded to provide long-term data storage services to the university community.
- notes: Work is 2 TB per user and Scratch is 30 TB but PURGED at 180 days; Campaign Storage is the only large tier and it is allocation-request-gated for university projects. The 30 TB scratch is…
- evidence note: documented: the work and scratch quotas and the scratch purge were read on 2026-11-03 at https://ncar-hpc-docs.readthedocs.io/en/latest/storage-systems/glade/, the eligible-institution and advisor-letter requirements at https://ncar-hpc-docs.readthedocs.io/en/latest/allocations/university-allocations/, and the campaign storage terms at https://ncar-hpc-docs.readthedocs.io/en/stable/storage-systems/glade/campaign/.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Work is 2 TB per user and Scratch is 30 TB but PURGED at 180 days; Campaign Storage is the only large tier and it is allocation-request-gated for university projects. The 30 TB scratch is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Work is 2 TB per user and Scratch is 30 TB but PURGED at 180 days; Campaign Storage is the only large tier and it is allocation-request-gated for university projects. The 30 TB scratch is…
  - [1] 2026-11-03: scratch is 30 TB and 10 million files per user and is purged after 180 days | capture: sha256:b78409d1c78590156c7c058a6d19d4d7050bb85047ae88513d8c7e9f486a26ba | quote: | Scratch:<br> /glade/derecho/scratch/\<username> | 30TB / 10M | No | PURGED<br> 180 days | Temporary space.
  - [1] 2026-11-03: work is 2 TB per user and not purged | capture: sha256:b78409d1c78590156c7c058a6d19d4d7050bb85047ae88513d8c7e9f486a26ba | quote: | Work:<br> /glade/work/\<username> | 2 TB | No | Not purged | User work space.
  - [2] 2026-11-03: access is limited to eligible institutions | capture: sha256:8796a1bfbeb2454dd0e23a619e7b7494aa2915c0e10abaf9c29311e5d22163a2 | quote: Eligible institutions encompass 2- and 4-year colleges and universities, including community colleges, predominantly undergraduate-serving institutions, and non-profit research organizations.
  - [2] 2026-11-03: unsponsored requests need an advisor or department-head letter | capture: sha256:8796a1bfbeb2454dd0e23a619e7b7494aa2915c0e10abaf9c29311e5d22163a2 | quote: They must provide a letter from their advisor or department head commenting on the quality of the proposed research and affirming that funds are not within the scope of a funded grant.
  - [3] 2026-11-03: campaign requests are prioritised, not guaranteed | capture: sha256:1ac83eeb97f2deb5224ac781e4403e60bc4d02d13888cd3b890c98ff320d4be2 | quote: Because NSF NCAR is not currently funded to provide long-term data storage services to the university community, university users' requests for these allocations are prioritized based on the following factors.
  - [3] 2026-11-03: campaign storage is reached through Globus | capture: sha256:1ac83eeb97f2deb5224ac781e4403e60bc4d02d13888cd3b890c98ff320d4be2 | quote: - through the Globus web and command-line interfaces
  - [1] 2026-11-03: campaign storage is allocated per project on request | capture: sha256:b78409d1c78590156c7c058a6d19d4d7050bb85047ae88513d8c7e9f486a26ba | quote: | Campaign Storage:<br> /glade/campaign | N/A | No | Not purged | Project space allocations (via allocation request) |
  - [3] 2026-11-03: campaign storage is medium-term | capture: sha256:1ac83eeb97f2deb5224ac781e4403e60bc4d02d13888cd3b890c98ff320d4be2 | quote: Campaign Storage is designed to provide medium-term storage for project data, typically for three to five years.
  - [3] 2026-11-03: university campaign requests go through the allocation system as supplements to a project allocation | capture: sha256:1ac83eeb97f2deb5224ac781e4403e60bc4d02d13888cd3b890c98ff320d4be2 | quote: University users can request Campaign Storage space through the NSF NCAR Resource Allocation System as supplements to their project allocations.
  - [2] 2026-11-04: an unsponsored request needs a letter from the advisor or department head | capture: sha256:8796a1bfbeb2454dd0e23a619e7b7494aa2915c0e10abaf9c29311e5d22163a2 | quote: - A letter from the individual’s advisor or department head must affirm the quality of the proposed research and that the work is not within the scope of a funded grant.
- sources:
  - [1] https://ncar-hpc-docs.readthedocs.io/en/latest/storage-systems/glade/
  - [2] https://ncar-hpc-docs.readthedocs.io/en/latest/allocations/university-allocations/
  - [3] https://ncar-hpc-docs.readthedocs.io/en/stable/storage-systems/glade/campaign/

## NSF NCAR Derecho

- `compute/nsf-ncar-derecho` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ncar-hpc-docs.readthedocs.io/en/latest/allocations/university-allocations/
- free tier: An Exploratory and Classroom allocation carries 500,000 Derecho core-hours and 1,500 Derecho GPU-hours, is accepted continuously, and requires "No external funding award", which the provider states explicitly in its funding eligibility column. A Small allocation raises that to 1 million core-hours and 2,500 GPU-hours and does require an NSF award. Derecho is 2,488 nodes with nearly 320,000 AMD EPYC cores plus 82 nodes holding 328 NVIDIA A100 GPUs, and access is "at no cost to you, your institution, or your research grants". | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: continuous-small-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): "To use Derecho, you must be a U.S.-based researcher, and your research must be in the Earth system sciences or related to Earth system science", so the half-million core-hours fail on both country and field before any funding question arises. [1]
- limits note: "To use Derecho, you must be a U.S.-based researcher, and your research must be in the Earth system sciences or related to Earth system science", so the half-million core-hours fail on both country and field before any funding question arises.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Derecho composes with nothing in the file because the field restriction is absolute: the machine is for Earth system science, so the 500,000 core-hours are only usable as a climate, weather or geoscience workload, and a general data-science job would be a false application rather than a clever one.
- reliability: no reliability event recorded
- notes: The number is the largest free core-hour figure found that does not require a funding award, and the reason it is recorded as a refutation rather than capacity is one sentence about U.S. residency. The Data Analysis route on Casper accepts any funding source, which makes it the only part of the NCAR offer not tied to an award, but it is for analysing NCAR-hosted data rather than for arbitrary compute. Large allocations have no upper limit and are reviewed in March and September; the September 18, 2026 deadline is the next one after this reading.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: continuous-small-allocation
  - facets.shape.gpu_class: NVIDIA A100
- evidence:
  - [1] 2026-10-22: Exploratory and Classroom: Derecho 500,000 core-hours and Derecho GPU 1,500 GPU-hours, continuous, funding eligibility "No external funding award", quoted from the table
  - [1] 2026-10-22: Small: Derecho 1 million core-hours and 2,500 GPU-hours, continuous, NSF award required, quoted from the table
  - [2] 2026-10-22: "Derecho boasts 2,488 nodes with nearly 320,000 AMD EPYC cores and 82 nodes with 328 NVIDIA A100 GPUs"; "access to these Derecho and other resources is provided at no cost to you, your institution, or your research grants", quoted
  - [2] 2026-10-22: "To use Derecho, you must be a U.S.-based researcher, and your research must be in the Earth system sciences"; "we can offer access to graduate students, postdocs, and new faculty without NSF funding", quoted
  - [1] 2026-10-22: the Data Analysis allocation on Casper accepts "Any funding source" in the funding eligibility column, quoted
- sources:
  - [1] https://ncar-hpc-docs.readthedocs.io/en/latest/allocations/university-allocations/
  - [2] https://commons.ucar.edu/discussion/tools-you-can-use-derecho-supercomputer
