# Synapse

> synapse.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/synapse/ | JSON https://fshy.ajam.dev/api/v1/entity/synapse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Synapse (Sage Bionetworks)

- `storage/synapse` | qualifies-with-caveat | evidence inferred | binding per-ip-shaping | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.synapse.org
- free tier: No clear public storage cap found. Platform is free SaaS on S3; documented pain point is a '1GB per day' quota on modelState (compute artifacts), not on file storage. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: per-object-cap: none documented for plain files; 1 GB/day on modelState. Retention: indefinite for public content | source: [1] | note: not stated
- egress: Free to download for public projects; anonymous download of public entities is supported. | metered: no
- identity: anonymous
- interface: s3, rest, oci
- limits:
  - per-ip-shaping (binding): 1GB per day [1]
  - per-ip-shaping (binding): 1 GB/day [1]
- limits note: per-object-cap: none documented for plain files; 1 GB/day on modelState. Retention: indefinite for public content. Gate: upload requires 'certified user' status (a quiz), so no anonymous write path exists.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Python/Java/R clients (`synapseclient`), REST API, and a built-in Docker registry. Also supports custom storage locations (your own S3/GCS). Which makes it a metadata layer over someone else's bucket rather than storage itself.
- composes with: Unlimited projects per certified user. The interesting chain is the inverse: point Synapse at a custom S3/GCS location and you get a free DOI-style sharing and permissions layer over any bucket you already have.
- reliability: Certification gate plus no published quota means capacity is discretionary; large uploads are known to be throttled/queued without a documented ceiling. Treat quota as unverified.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'you need to be a certified user', S3-backed, no quota stated
  - [2] 2026-10-21: files can live in your own S3/GCS bucket, Synapse keeps metadata
  - [3] 2026-10-21: 'Model State exceeded 1GB per day quota'
- sources:
  - [1] https://docs.synapse.org/synapse-docs/uploading-and-organizing-data
  - [2] https://docs.synapse.org/synapse-docs/custom-storage-locations
  - [3] https://www.synapse.org/Synapse:syn4224222/discussion/threadId=1648
