# GRO.data

> goettingen-research-online.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goettingen-research-online/ | JSON https://fshy.ajam.dev/api/v1/entity/goettingen-research-online.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GRO.data (Göttingen)

- `storage/gro-data` | fails-identity | evidence reported | binding none | category institutional Dataverse
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.791Z (live) | stale on 2026-12-04
- url https://data.goettingen-research-online.de
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1] | note: The quota endpoint reports "No quota defined for this collection".
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free | metered: no
- identity: institution | detail: Institution. 'You can use your existing MPI or university email address to log in via Single Sign-On'. Explicitly an email-domain gate, and an SSO one at that, so a gmail address cannot pass.
- interface: rest
- limits note: no quota, no file-count limit exposed
- interface detail: REST
- tooling: the same as interface detail
- composes with: none
- reliability: Web front-end HTML endpoints frequently time out. The underlying REST API responds normally.
- notes: The quota endpoint reports "No quota defined for this collection".
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no quota defined (API)
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: {"message":"No quota defined for this collection"}
  - [2] 2026-10-21: 'You can use your existing MPI or university email address to log in via Single Sign-On'
  - [1] 2026-11-09: the root collection's quota endpoint returns this message in place of a byte quota | capture: sha256:2dac66e641692ca359f379b0dd652436616700e5eef4f51ae875a1892c79e452 | quote: No quota defined for this collection
  - [1] 2026-11-09: the quota endpoint answered on 2026-11-09 | capture: sha256:2dac66e641692ca359f379b0dd652436616700e5eef4f51ae875a1892c79e452 | quote: date: Mon, 09 Nov 2026 15:01:00 GMT
  - [1] 2026-11-19: the root collection's quota endpoint still reports no quota | capture: sha256:d84d57b3f68503381d5bbeed89490215f615d897697b2f83fb4612b947c63bab
- sources:
  - [1] https://data.goettingen-research-online.de/api/dataverses/1/storage/quota?showInherited=true
  - [2] https://web.archive.org/web/20260504091221/https://data.goettingen-research-online.de/
