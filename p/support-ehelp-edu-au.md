# ardc nectar research cloud

> support.ehelp.edu.au | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/support-ehelp-edu-au/ | JSON https://fshy.ajam.dev/api/v1/entity/support-ehelp-edu-au.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ardc nectar research cloud (australia) as free object storage

- `storage/ardc-nectar-research-cloud-as-free-object-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:55.371Z (live) | stale on 2026-12-04
- url https://support.ehelp.edu.au/support/solutions/articles/6000055380-resources-available-to-you
- free tier: None reachable: Every researcher gets a 'project trial with 4 VCPUs allocated for six months', but object storage is not part of the trial. It is an RC-NAS allocation item reviewed by the Nectar Allocation. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the support page states no per-object size cap | source: [1] | note: not applicable
- retention: All project trials expire and their quota is reduced to zero after six months if the 4 VCPUs are not consumed beforehand. | days: 180 | source: [1]
- egress: Off-Net: 1 GB of off-net traffic per core per month. | metered: yes
- identity: email
- interface: unknown
- interface detail: stated-absent: the support page offers object storage as an allocation item but states no object-storage API token; its shared file system service is reached via NFS, CIFS (SMB) or CEPHFS
- tooling: not documented
- composes with: stated-absent: the support page states no way to chain object storage into a free store; object storage is an allocation item requested through an allocation request, not part of the project trial
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: Every researcher gets a 'project trial with 4 VCPUs allocated for six months', but object storage is not part of the trial — it is an RC-NAS allocation item reviewed by the Nectar…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Every researcher gets a 'project trial with 4 VCPUs allocated for six months', but object storage is not part of the trial — it is an RC-NAS allocation item reviewed by the Nectar…
  - [2] 2026-10-21: cited as the basis of the rejection: Every researcher gets a 'project trial with 4 VCPUs allocated for six months', but object storage is not part of the trial — it is an RC-NAS allocation item reviewed by the Nectar Allocation
  - [1] 2026-11-19: the free Nectar trial is four VCPUs for six months, with object storage an allocation item rather than part of the trial | capture: sha256:3a15eee51db8b1b08cf5896ec8f6d89282260b1ca5f053d95bb31f3856efe9b5 | quote: All researchers initially (and without application) get a project trial with 4 VCPUs allocated for six months.
  - [1] 2026-11-19: the page names file-system access modes for the shared file system service but no object-storage API | capture: sha256:3a15eee51db8b1b08cf5896ec8f6d89282260b1ca5f053d95bb31f3856efe9b5 | quote: Access to these systems can be via NFS, CIFS (SMB) or CEPHFS, depending on the site.
  - [1] 2026-11-19: the first-party support page states a six-month trial expiry | capture: sha256:3a15eee51db8b1b08cf5896ec8f6d89282260b1ca5f053d95bb31f3856efe9b5 | quote: All project trials will expire and their quota will be reduced to zero after six months if the 4 VCPUs are not consumed beforehand.
  - [1] 2026-11-19: object storage requires a request and is not part of the free trial, with no chaining path stated | capture: sha256:3a15eee51db8b1b08cf5896ec8f6d89282260b1ca5f053d95bb31f3856efe9b5 | quote: you may choose to request a quota of object storage
  - [1] 2026-11-19: the first-party support page states a monthly off-net traffic allowance of 1 GB per core | capture: sha256:3a15eee51db8b1b08cf5896ec8f6d89282260b1ca5f053d95bb31f3856efe9b5 | quote: Off-Net: 1 GB of off-net traffic per core per month.
- sources:
  - [1] https://support.ehelp.edu.au/support/solutions/articles/6000055380-resources-available-to-you
  - [2] https://support.ehelp.edu.au/support/solutions/articles/6000191233-research-cloud-national-allocation-scheme-rc-nas-policy
