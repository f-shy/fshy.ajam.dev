# dspace registry cohort

> ehu.eus | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ehu/ | JSON https://fshy.ajam.dev/api/v1/entity/ehu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dspace registry cohort (60 of 60 sampled)

- `storage/dspace-registry-cohort` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:44.043Z (live) | stale on 2026-12-04
- url http://academico.ehu.eus
- free tier: None reachable: Every sampled site from page 1 of the official registry failed /server/api/info. They are DSpace 6 or earlier with no REST API, or the host is gone. The registry is a museum, not an invento. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Every sampled site from page 1 of the official registry failed /server/api/info — they are DSpace 6 or earlier with no REST API, or the host is gone. The registry is a museum, not an…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Every sampled site from page 1 of the official registry failed /server/api/info — they are DSpace 6 or earlier with no REST API, or the host is gone. The registry is a museum, not an…
  - [2] 2026-10-21: cited as the basis of the rejection: Every sampled site from page 1 of the official registry failed /server/api/info — they are DSpace 6 or earlier with no REST API, or the host is gone. The registry is a museum, not an invento
  - [3] 2026-10-21: cited as the basis of the rejection: Every sampled site from page 1 of the official registry failed /server/api/info — they are DSpace 6 or earlier with no REST API, or the host is gone. The registry is a museum, not an invento
  - [4] 2026-11-19: the sampled site serves a DSpace repository | capture: sha256:d3cd413afad501924d84f3889edd1ad23f233fe8ecb37393833c1e8e330b93ed | quote: DSpace software
  - probe:https://academico.ehu.eus/server/api/info 2026-11-19: the sampled DSpace site's REST info path answered HTTP 404 on 2026-11-19 | capture: sha256:d569fdc3c5ccae7c284b41295e8646cc44cc4cc4ef4c5f0310648c747ad375db | quote: "status": 404
- sources:
  - [1] http://academico.ehu.eus
  - [2] http://corlib.pdn.ac.lk
  - [3] http://ir.nust.ac.zw
  - [4] https://academico.ehu.eus/
