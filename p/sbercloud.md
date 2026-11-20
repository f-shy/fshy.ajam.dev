# sbercloud

> sbercloud.ru | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sbercloud/ | JSON https://fshy.ajam.dev/api/v1/entity/sbercloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sbercloud / sberdisk

- `storage/sbercloud-sberdisk` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:25.777Z (live) | stale on 2026-12-04
- url https://docs.sbercloud.ru/
- free tier: none reachable: SberCloud was rebranded into Cloud.ru (docs.sbercloud.ru now serves Cloud.ru Evolution docs), so it is the same 15 GB free tier, not a second provider. The consumer SberDisk is 15 GB free… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Commercial IaaS with no bulk free object storage; the consumer SberDisk offers 15 GB free. docs.sbercloud.ru could not be resolved on 2026-11-19.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: SberCloud was rebranded into Cloud.ru (docs.sbercloud.ru now serves Cloud.ru Evolution docs), so it is the same 15 GB free tier, not a second provider. The consumer SberDisk is 15 GB free…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: SberCloud was rebranded into Cloud.ru (docs.sbercloud.ru now serves Cloud.ru Evolution docs), so it is the same 15 GB free tier, not a second provider. The consumer SberDisk is 15 GB free…
  - [2] 2026-10-21: cited as the basis of the rejection: SberCloud was rebranded into Cloud.ru (docs.sbercloud.ru now serves Cloud.ru Evolution docs), so it is the same 15 GB free tier, not a second provider. The consumer SberDisk is 15 GB free, w
  - [2] 2026-11-19: the consumer SberDisk free allowance is 15 GB | capture: sha256:f98e33bbb4dd110cd6f1be7cd0a1a2478e6a5ff7815ca814d371d051b638eae1 | quote: «СберДиск» предоставляет бесплатно 15 ГБ.
- sources:
  - [1] https://docs.sbercloud.ru/
  - [2] https://www.fontanka.ru/2026/05/20/76431223/
