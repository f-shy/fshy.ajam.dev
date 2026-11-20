# seaart

> seaart.ai | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seaart/ | JSON https://fshy.ajam.dev/api/v1/entity/seaart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SeaCloudAI Sandbox

- `compute/seacloudai` | paid-only | evidence unverified | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:55:04.000Z (inherited) | stale on 2026-11-06
- url https://sandbox-gateway.cloud.seaart.ai
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: SeaArt SeaCloud AI gateway endpoints return empty responses on automated health probes. Free compute allocations remain unverified against live endpoints.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: unverified: no route returned the page on 2026-10-22. The origin returns an empty body on https://sandbox-gateway.cloud.seaart.ai and the fetch route answers exit 4, so no page content was received.
- sources:
  - [1] https://sandbox-gateway.cloud.seaart.ai

## seaart (seaart.ai)

- `storage/seaart` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:25.778Z (inherited) | stale on 2026-12-04
- url https://www.seaart.ai/api/v1/model/detail
- free tier: none reachable: Model metadata is readable anonymously (POST /api/v1/model/detail returns a full JSON object with model_ver_info_v2, file_id, hashs) but there is no anonymous file download… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Model metadata is readable anonymously (POST /api/v1/model/detail returns a full JSON object with model_ver_info_v2, file_id, hashs) but there is no anonymous file download…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Model metadata is readable anonymously (POST /api/v1/model/detail returns a full JSON object with model_ver_info_v2, file_id, hashs) but there is no anonymous file download…
  - probe:https://www.seaart.ai/api/v1/model/detail 2026-11-19: the model-detail API endpoint returns HTTP 405 to a plain GET on 2026-11-19 | capture: sha256:9b1eac6c66b904dad90bdd213bfef22b5b0e0d79b4f88aa3fb32f719e324e6fa | quote: "status": 405,
- sources:
  - [1] https://www.seaart.ai/api/v1/model/detail

## seaart ai

- `storage/seaart-ai` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:25.778Z (live) | stale on 2026-12-04
- url https://www.seaart.ai/pricing
- free tier: none reachable: Renders as an app shell; the /pricing and /models pages returned only nav chrome and generator marketing with no storage or upload-limit numbers. Same class as TensorArt: a generation site… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Renders as an app shell; the /pricing and /models pages returned only nav chrome and generator marketing with no storage or upload-limit numbers. Same class as TensorArt: a generation site…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Renders as an app shell; the /pricing and /models pages returned only nav chrome and generator marketing with no storage or upload-limit numbers. Same class as TensorArt: a generation site…
  - [2] 2026-10-21: cited as the basis of the rejection: Renders as an app shell; the /pricing and /models pages returned only nav chrome and generator marketing with no storage or upload-limit numbers. Same class as TensorArt: a generation site w
  - [3] 2026-10-21: cited as the basis of the rejection: Renders as an app shell; the /pricing and /models pages returned only nav chrome and generator marketing with no storage or upload-limit numbers. Same class as TensorArt: a generation site w
  - [2] 2026-11-19: SeaArt is an image/video generation community site with no storage capacity stated on its first-party pages | capture: sha256:8607af852011a107a2eb162713dd1599a00924b5734a79f6289a4f7722477aad | quote: Turn your ideas into images, videos, and characters in minutes. Create, remix, and share with the community.
- sources:
  - [1] https://www.seaart.ai/pricing
  - [2] https://www.seaart.ai/
  - [3] https://www.seaart.ai/models
