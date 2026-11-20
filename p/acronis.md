# acronis cyber protect

> acronis.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/acronis/ | JSON https://fshy.ajam.dev/api/v1/entity/acronis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## acronis cyber protect (bundled cloud storage)

- `storage/acronis-cyber-protect` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.937Z (live) | stale on 2026-12-04
- url https://dl.acronis.com/u/rc/Acronis-Cyber-Protect-Edition-Comparison-EN-US-220421.pdf
- free tier: none reachable: Cloud storage is a license add-on, not a product. Essentials tier includes 5 GB per workstation; 50 GB requires Standard, 250 GB requires Advanced/Server. No free storage-only tier, no… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: No per-object size cap stated; cloud storage is a per-workload quota (5-250GBs) bundled in a license. | source: [1] | note: not applicable
- retention: The PDF lists 'Retention rules' as a feature but states no fixed retention period for cloud-stored bytes. | source: [1]
- egress: stated-absent: the first-party PDF states no price or quota for traffic out of Acronis Cloud storage | metered: no
- identity: email
- interface: cli
- interface detail: A backup product, not a general byte store: backups go to local storage, Acronis Cloud, service-provider cloud or SFTP.
- tooling: not documented
- composes with: stated-absent: the first-party PDF states no way to chain the bundled cloud storage with other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Cloud storage is a license add-on, not a product. Essentials tier includes 5 GB per workstation; 50 GB requires Standard, 250 GB requires Advanced/Server. No free storage-only tier, no…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Cloud storage is a license add-on, not a product. Essentials tier includes 5 GB per workstation; 50 GB requires Standard, 250 GB requires Advanced/Server. No free storage-only tier, no…
  - [1] 2026-11-19: the edition comparison still ties 5 GB to Essentials and 50 GB to higher paid editions, with no standalone free storage tier | capture: sha256:065884be1b34fec06becd57f7e901e13e04d2b8b3df115ad3252198bc5704c62 | quote: Workstation 5GB 50GB 50GB 50GB
  - [1] 2026-11-19: the first-party edition-comparison PDF lists SFTP backup as an access route | capture: sha256:065884be1b34fec06becd57f7e901e13e04d2b8b3df115ad3252198bc5704c62 | quote: Backup to SFTP
  - [1] 2026-11-19: the first-party PDF names retention rules as a feature without stating a period | capture: sha256:065884be1b34fec06becd57f7e901e13e04d2b8b3df115ad3252198bc5704c62 | quote: Retention rules
  - [1] 2026-11-19: the first-party PDF states a bundled per-workload storage allowance and no per-object cap | capture: sha256:065884be1b34fec06becd57f7e901e13e04d2b8b3df115ad3252198bc5704c62 | quote: The subscription-based license also includes a free amount of Acronis-hosted cloud storage (5-250GBs), depending on the protected workload.
- sources:
  - [1] https://dl.acronis.com/u/rc/Acronis-Cyber-Protect-Edition-Comparison-EN-US-220421.pdf
