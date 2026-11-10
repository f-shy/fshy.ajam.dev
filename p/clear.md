# ClearML

> clear.ml | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clear/ | JSON https://fshy.ajam.dev/api/v1/entity/clear.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ClearML (hosted free tier)

- `storage/clearml` | fails-quota | evidence reported | binding none | category mlops-artifacts
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://clear.ml
- free tier: Zero free bytes by design. ClearML's free tier is 'Flexible Storage. Store your datasets on any storage service and connect to ClearML – HTTP/S3/GCS/Azure/NAS'. That is bring-your-own-bucket: ClearML supplies the versioning layer, you supply (and pay for) the bytes. Differential storage reduces what you must store, but it does not create storage. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Yours, because the bytes are on your storage. ClearML itself charges nothing for egress since it never holds the data. | metered: no
- identity: email | detail: email.
- interface: s3, rest
- limits note: Differential/dedup versioning means versions store only the change set from the parent, which is a genuine byte-saver. Free plan feature-limited (SSO and configuration vault are paid/enterprise). No included storage at all.
- interface detail: rest
- tooling: clearml Python SDK + clearml-agent; `Dataset.create()` / `dataset.add_files()` / `dataset.upload()` against any S3/GCS/Azure/HTTP/NAS backend. Mature and well documented.
- composes with: There is nothing to multiply. The storage is a pre-existing account at AWS/GCS/Azure, all of which are excluded on cost grounds.
- reliability: Reliable; the server is open source and self-hostable. But as a free-storage route it is a null result: it is a control plane, not a data plane.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Zero free bytes by design. ClearML's free tier is 'Flexible Storage — Store your datasets on any storage service and connect to ClearML – HTTP/S3/GCS/Azure/NAS'. That is bring-your-own-bucket: ClearML supplies the versioning layer, you supply (and pay for) the bytes. Differential storage reduces what you must store, but it does not create storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Flexible Storage — Store your datasets on any storage service and connect to ClearML – HTTP/S3/GCS/Azure/NAS'; 'Differential Storage — Versions only store the change set from parent versions'
- sources:
  - [1] https://clear.ml/pricing
