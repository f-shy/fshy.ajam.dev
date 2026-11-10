# INCITE

> doeleadershipcomputing.org | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/doeleadershipcomputing/ | JSON https://fshy.ajam.dev/api/v1/entity/doeleadershipcomputing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## INCITE (ALCF + OLCF, US DOE)

- `storage/incite` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://doeleadershipcomputing.org/incite-faqs/
- free tier: 100 trillion bytes (~100 TB) of data storage awarded across the programme each year; per-project archival quota at OLCF is 200 TB (shared across Project/World/User Archive on Kronos). | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Tenured infrastructure; data survives, but the allocation expires and the archival quota can be clawed back after project end - treat as renewable-while-funded, not permanent. | source: [1] | note: not stated
- egress: Globus/GridFTP and SSH transfer free to allocation holders; no egress meter. Data is not a public HTTP origin. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: s3, sftp, scp, ssh
- limits:
  - write-gated: reviewed annual renewal request [1]
- limits note: Annual call only (mid-April to mid/late June), awards 1-3 years with a peer-reviewed annual renewal request. Post-project archival storage is explicitly at the facility's discretion ('The facilities reserve the right to limit the amount and duration of archival storage once a project has been completed'). Data must be research data.
- binding note: 100 TB is awarded to projects by a review panel; there is no route from an unaffiliated individual to an allocation.
- interface detail: posix
- tooling: SSH/scp/sftp, Globus, Lustre + HPSS/Kronos nearline mounts; no S3.
- composes with: One allocation = one project directory on a 100+ PB Lustre (Eagle/Orion) plus up to 200 TB nearline archive. Storage is not separately metered, so a storage-heavy proposal can request a large quota against a small compute request - but the proposal must still justify compute.
- reliability: Tenured infrastructure; data survives, but the allocation expires and the archival quota can be clawed back after project end - treat as renewable-while-funded, not permanent.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '100 trillion bytes of data storage space'; '1-3 years (renewable)'; 'Multiyear awards must submit annual renewal requests'
  - [1] 2026-10-21: Q10: 'Are foreign researchers and teams eligible to apply? Yes... U.S. collaborations are encouraged, but not required.' Q11: 'the solicitation is open to individual researchers'
  - [2] 2026-10-21: 'open to US- and non-US-based researchers and research organizations'; 'Citizenship and specific funding sources are not qualifiers'
  - [3] 2026-10-21: Project Archive 200 TB, no purge flag
- sources:
  - [1] https://doeleadershipcomputing.org/incite-faqs/
  - [2] https://doeleadershipcomputing.org/wp-content/uploads/sites/123/2025/04/INCITE-Overview-and-Policies_2026.pdf
  - [3] https://docs.olcf.ornl.gov/data/index.html

## INCITE

- `compute/incite` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://doeleadershipcomputing.org/call-for-proposals/
- free tier: Up to 60% of the allocatable time on Frontier (OLCF) and Aurora (ALCF) is allocated through INCITE for calendar year 2027; for each resource, allocations are anticipated to be between 500K and 2M node-hours on Aurora and Frontier, and individual awards may be higher. Non-proprietary research projects are not charged for access. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: merit-reviewed allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The PI may be foreign and unaffiliated on paper, but the award is conditional on each participating institution signing the ANL/ORNL user agreement, and the applicant must already hold all funding and resources needed to execute the campaign at application time. [1]
- limits note: The PI may be foreign and unaffiliated on paper, but the award is conditional on each participating institution signing the ANL/ORNL user agreement, and the applicant must already hold all funding and resources needed to execute the campaign at application time.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The awarded resource is time plus 100 trillion bytes of storage across the programme; it does not include labour, travel or postdoc funding, so it composes only with a grant the applicant already holds.
- reliability: no reliability event recorded
- notes: Two review phases: an international peer-review panel on scientific merit, then a technical assessment of computational readiness by LCF staff. Requests under 20% of the average award are redirected to Director's Discretionary or ALCC. Early Career Track reserves 10% of allocatable time for PIs within 10 years of a PhD who have not previously been INCITE PI. Polaris is no longer available; Aurora and Frontier are the only INCITE resources for 2027. The 20% utilisation criterion is the real filter at this scale: a solo researcher must show the campaign consumes a fifth of an exascale machine. Node-hour to GPU-hour conversion depends on the system (Frontier nodes carry 4 MI300A APUs), so earlier readings should not convert without a per-system figure.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: merit-reviewed allocation
  - facets.shape.gpu_class: AMD MI300A (Frontier) / Intel Data Center GPU Max (Aurora)
- evidence:
  - [1] 2026-10-22: allocations anticipated between 500K and 2M node-hours on Aurora and Frontier, up to 60% of allocatable time, CY2027, quoted
  - [1] 2026-10-22: 'US and non-US based Individuals and/or teams of researchers from academia, national laboratories, industry, and federal agencies are eligible to apply', quoted
  - [1] 2026-10-22: application window Wednesday April 8, 2026 through 8:00 pm EDT Monday June 15, 2026; awards announced November 2026, quoted
  - [1] 2026-10-22: 'each participating institution on the awarded proposal must accept or already have signed the user agreement; otherwise, access by the institution's researcher(s) to the LCF system will be delayed', quoted
  - [2] 2026-10-22: FAQ 8: 'researchers are expected to have all funding and any other elements necessary to ensure the success of their research project in place at the time of their application'; FAQ 26 repeats it as an eligibility condition
- sources:
  - [1] https://doeleadershipcomputing.org/call-for-proposals/
  - [2] https://doeleadershipcomputing.org/incite-faqs/
