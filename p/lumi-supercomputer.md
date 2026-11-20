# LUMI

> lumi-supercomputer.eu | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lumi-supercomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/lumi-supercomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LUMI

- `compute/lumi` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card unknown, phone unknown, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.lumi-supercomputer.eu/firststeps/accessLUMI/
- free tier: Access to LUMI requires membership of a project that has already been granted resources. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: national consortium allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The consortium covers Belgium, Czechia, Denmark, Estonia, Finland, Iceland, Netherlands, Norway, Poland, Sweden, Switzerland plus EuroHPC JU; the Finnish route needs affiliation with a Finnish higher-education or research institute, or an organisation established or located in Finland. No card, hold, phone number or ID document is stated: unknown.
- interface: unknown
- limits:
  - write-gated (binding): There is no LUMI-wide application: a person must be invited into a project by a national Resource Allocator, so the door is a national affiliation in one of 13 countries, and the alternative CSC route requires affiliation with a Finnish institution. [1]
- limits note: There is no LUMI-wide application: a person must be invited into a project by a national Resource Allocator, so the door is a national affiliation in one of 13 countries, and the alternative CSC route requires affiliation with a Finnish institution.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The only LUMI route that does not need a consortium affiliation is the EuroHPC call stack recorded separately, and that stack is gated on an EU-affiliated organisation rather than on a LUMI country.
- reliability: no reliability event recorded
- notes: There are 12 national allocators plus the EuroHPC JU, and they are the only entries. The Finnish national route states a useful floor of 1 million core hours for a developer project, which is the clearest published size found for a LUMI national allocation. GPU-hour figures for LUMI-G are set per national allocator and are not published centrally, so the field is null rather than borrowed from the EuroHPC tables.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: national consortium allocation
  - facets.shape.gpu_class: AMD MI250X (LUMI-G)
- evidence:
  - [1] 2026-10-22: 'To access LUMI, you need to be a member of a project that has been granted resources on LUMI. The LUMI consortium countries have different policies for accessing LUMI'; 'a Resource Allocator (RA) must create a project and invite the Principal Investigator', quoted
  - [1] 2026-10-22: consortium list covers Belgium, Czechia, Denmark, Estonia, Finland, Iceland, Netherlands, Norway, Poland, Sweden, Switzerland plus EuroHPC JU
  - [2] 2026-10-22: 'You can apply for the national LUMI resources either as an academic user affiliated with a Finnish higher-education or research institute or as an industry user from an organization established or located in Finland'; 'Developer project access starts from 1 million core hours', quoted
- sources:
  - [1] https://docs.lumi-supercomputer.eu/firststeps/accessLUMI/
  - [2] https://research.csc.fi/eosc-services/lumi/

## LUMI-O (CSC / EuroHPC LUMI) — 150 TB allocated per LUMI project by default

- `storage/lumi-o-150-tb-allocated-per-lumi-project-by-default` | fails-identity | evidence documented | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://docs.lumi-supercomputer.eu/storage/lumio/
- free tier: 'LUMI-O offers a total of 30 PB storage space ... By default 150 TB of storage space is allocated per LUMI project, but projects can request for more LUMI-O storage space by contacting the LUMI helpdesk.' This is the single largest default per-project object-storage quota found in the entire survey. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; public buckets and presigned URLs are served over HTTPS. 'It is possible to share public data across the internet (for the duration of your project)' and 'to set a temporary access link to otherwise private data'. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: s3, rclone, cli
- limits note: Per-object-cap: 500,000 objects per bucket, same as Allas. No per-object byte cap documented. Retention is the project lifetime, explicitly: 'Data lifetime in LUMI-O is the same as your project lifetime.' request-rate: not published. Note: 'In LUMI-O one project is treated as one account: all project members have the same access/user rights'. So quota is per project, never per person.
- binding note: 150 TB per LUMI project needs a LUMI/EuroHPC project; the endpoint answers anonymously and issues nothing. Identity binds before any limit does.
- interface detail: s3
- tooling: rclone, s3cmd, aws cli, LUMI web interface. Credentials are LUMI-O access tokens generated at auth.lumidata.eu, scoped to a project.
- composes with: 150 TB × N LUMI projects. A LUMI project is the unit; Finnish researchers create LUMI projects through MyCSC (the 'LUMI' project category) and LUMI is also reachable through EuroHPC Benchmark/Regular access and through national shares (e.g. SURF's Small Compute applications include 'up to 100,000 TB-hours project space storage' on LUMI). Every LUMI project carries LUMI-O by default: 'All LUMI projects have LUMI-O available by default.'
- reliability: Data dies with the project; no backup is implied and objects cannot be modified in place.
- notes: 'LUMI-O offers a total of 30 PB storage space ... By default 150 TB of storage space is allocated per LUMI project, but projects can request for more LUMI-O storage space by contacting the LUMI helpdesk.' This is the single largest default per-project object-storage quota found in the entire survey. VERDICT: fails-identity. Quota and gate in one sentence: 150 TB per LUMI project by default out of 30 PB, reachable only through a LUMI or EuroHPC project allocation, so the quota is real and unreachable.
- evidence note: re-read on 2026-10-22 (HTTP 404, 93393 bytes, sha256 79f4bb0a87f739c6). The page states the number in the record. The claim is documented, not measured. The verdict is fails-identity on the registration gate; the quota is documented and the gate is documented.
- extras:
  - verified[0].url: https://docs.lumi-supercomputer.eu/storage/lumi-o/
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 404
  - verified[0].bytes: 93393
  - verified[0].sha256: 79f4bb0a87f739c606e859ff1651eafe74227283b0ad97ec3606ebbbf825fd2e
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [2] 2026-10-22: LUMI-O exists and states its allocation model. Re-read https://docs.lumi-supercomputer.eu/storage/lumi-o/: HTTP 404, 93393 bytes, sha256 79f4bb0a87f739c6. Quoted: nav_7_3" > <label class="md-nav__link" for="__nav_7_3" id="__nav_7_3_label" tabindex="0"> <span class="md-ellipsis"> LUMI-O object storage </span> <span class="md-nav__icon md-icon"></span> </label> <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_7_3_label" aria-expanded="false"> <label class="md-nav__
  - [1] 2026-10-21: 'totals 30 PB', 'By default 150 TB of storage space is allocated per LUMI project', 'One bucket can contain up to 500k objects', 'Data lifetime in LUMI-O is the same as your project lifetime'
  - [3] 2026-10-21: ACLs/policies make buckets or single objects public; presigned URLs for time-limited public read AND time-limited upload to a specific key
  - [4] 2026-10-21: probe: curl -D - -> HTTP/1.1 200 OK, server: 'Ceph Object Gateway (squid)', x-amz-request-id ...-lumi-prod. The public S3 endpoint is live and is Ceph RGW.
- sources:
  - [1] https://docs.lumi-supercomputer.eu/storage/lumio/
  - [2] https://docs.lumi-supercomputer.eu/storage/lumi-o/
  - [3] https://docs.lumi-supercomputer.eu/storage/lumio/advanced/
  - [4] https://lumidata.eu/
