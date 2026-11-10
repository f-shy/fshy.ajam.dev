# minio gateway

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-minio/ | JSON https://fshy.ajam.dev/api/v1/entity/github-minio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## minio gateway (s3/gcs/azure/hdfs) as a pooling layer

- `storage/minio-gateway-as-a-pooling-layer` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/minio/minio/issues/14331
- free tier: none reachable: Removed, not merely deprecated: 'MinIO Gateway will be removed by June 1st, 2022 from the MinIO repository'. There is a documented migration path away from it, and the entire minio/minio… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Removed, not merely deprecated: 'MinIO Gateway will be removed by June 1st, 2022 from the MinIO repository'. There is a documented migration path away from it, and the entire minio/minio…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Removed, not merely deprecated: 'MinIO Gateway will be removed by June 1st, 2022 from the MinIO repository'. There is a documented migration path away from it, and the entire minio/minio…
  - [2] 2026-10-21: cited as the basis of the rejection: Removed, not merely deprecated: 'MinIO Gateway will be removed by June 1st, 2022 from the MinIO repository'. There is a documented migration path away from it, and the entire minio/minio rep
- sources:
  - [1] https://github.com/minio/minio/issues/14331
  - [2] https://www.min.io/blog/deprecation-of-the-minio-gateway
