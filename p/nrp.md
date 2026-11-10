# National Research Platform

> nrp.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nrp/ | JSON https://fshy.ajam.dev/api/v1/entity/nrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## National Research Platform (NRP / Nautilus, US) — free Ceph S3 to any namespace holder, multi-site

- `storage/national-research-platform-free-ceph-s3-to-any-namespace` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nrp.ai/documentation/userdocs/storage/ceph-s3/
- free tier: No published byte quota. The docs are explicit that the storage is donated: 'The Nautilus Ceph storage cluster can be accessed via S3 protocol. It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud.' Quota is whatever the namespace is granted by admins; CephFS carries a documented 16 TB per-file cap. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: CephFS has 'a per-file size limit of 16 TB | bytes: 16000000000000 | source: [1] | note: not stated
- retention: Retention: 'Any storage volume that was not accessed for 6 months can be purged without notification'. This is the hard floor on it as an archive. | days: 180 | source: [1] | note: not stated
- egress: Free and unmetered ('free for our users'), served from university-hosted Ceph RGW pods across west/central/east. | metered: no
- identity: institution
- interface: s3, rclone, cli
- limits:
  - retention-clamped: Retention: 'Any storage volume that was not accessed for 6 months [1]
  - per-object-cap (binding): per-object-cap: CephFS has 'a per-file size limit of 16 TB [1]
- limits note: Per-object-cap: CephFS has 'a per-file size limit of 16 TB'; S3 per-object cap not stated. Retention: 'Any storage volume that was not accessed for 6 months can be purged without notification'. This is the hard floor on it as an archive. request-rate: not published; pods are policed instead ('a user can not submit more than 4 pods' outside the utilisation rules; interactive pods 'destroyed in 6 hours'). Gate: CILogon account, then namespace admin status via 'eligible faculty members and researchers can request to become namespace admin' (at LBNL this is an email).
- interface detail: s3
- tooling: rclone/aws cli/restic against https://s3-west|s3-central|s3-east.nrp-nautilus.io. Credentials from the User Portal S3 Tokens page (nrp.ai/s3token/) for public Ceph pools. Inside-cluster and outside-cluster endpoints documented.
- composes with: Six independent Ceph pools (west, central, east, haosu, tide, ha) each with their own S3 endpoint. 'public Ceph pools' give self-service tokens. So any CILogon-authenticated researcher can mint S3 credentials without an admin. That is the closest thing to self-service in this whole niche.
- reliability: 6-month untouched-data purge is documented and unannounced; namespaces under-utilising requests are closed. Treat as hot storage only, never archive.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud'; six pool endpoints; 'You can get your credentials (key and secret) in the User Portal ... for public Ceph pools'
  - [2] 2026-10-21: 'Any storage volume that was not accessed for 6 months can be purged without notification'; pod/utilisation enforcement rules
  - [3] 2026-10-21: 'There is a per-file size limit of 16 TB in CephFS'
  - [4] 2026-10-21: probe: curl -> 200 (187 bytes Ceph RGW ListAllMyBucketsResult); s3-central and s3-east identical; s3-haosu/s3-tide/s3-ha documented as further endpoints. Endpoints live and answering S3.
- sources:
  - [1] https://nrp.ai/documentation/userdocs/storage/ceph-s3/
  - [2] https://nrp.ai/documentation/userdocs/start/policies/
  - [3] https://nrp.ai/documentation/userdocs/storage/intro/
  - [4] https://s3-west.nrp-nautilus.io/
