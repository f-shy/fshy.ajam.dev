# National Research Platform

> nrp.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nrp/ | JSON https://fshy.ajam.dev/api/v1/entity/nrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## National Research Platform (NRP / Nautilus, US) — free Ceph S3 to any namespace holder, multi-site

- `storage/national-research-platform-free-ceph-s3-to-any-namespace` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T21:21:15.500Z (live) | stale on 2026-12-10
- url https://nrp.ai/documentation/userdocs/storage/ceph-s3/
- free tier: The Nautilus Ceph storage cluster can be accessed via S3 protocol. It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: There is a per-file size limit of 16 TB in CephFS. Ceph provides an S3-compatible protocol interface (with a per-file size limit of 5 TiB). | bytes: 16000000000000 | source: [1] | note: The 16 TB limit is for CephFS files; the S3-compatible interface has a per-file size limit of 5 TiB.
- retention: Any volume that was not accessed for 6 months can be purged without notification. | days: 180 | source: [1] | note: unverified: no retention period beyond the 6-month purge rule is stated on the policies page
- egress: It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud. | metered: no
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
- notes: No published byte quota. The docs are explicit that the storage is donated: 'The Nautilus Ceph storage cluster can be accessed via S3 protocol. It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud.' Quota is whatever the namespace is granted by admins; CephFS carries a documented 16 TB per-file cap.
- evidence:
  - [1] 2026-10-21: 'It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud'; six pool endpoints; 'You can get your credentials (key and secret) in the User Portal ... for public Ceph pools'
  - [2] 2026-10-21: 'Any storage volume that was not accessed for 6 months can be purged without notification'; pod/utilisation enforcement rules
  - [3] 2026-10-21: 'There is a per-file size limit of 16 TB in CephFS'
  - [4] 2026-10-21: probe: curl -> 200 (187 bytes Ceph RGW ListAllMyBucketsResult); s3-central and s3-east identical; s3-haosu/s3-tide/s3-ha documented as further endpoints. Endpoints live and answering S3.
  - [1] 2026-11-11: the Ceph S3 cluster is the provider's own storage and is free for its users | capture: sha256:944599bb35d80308cbf00de74b237db44cf8b5b57d67d1ffb1cfbedcf67bd6c1 | quote: The Nautilus Ceph storage cluster can be accessed via S3 protocol. It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud.
  - [3] 2026-11-25: CephFS files are capped at 16 TB and the S3-compatible interface at 5 TiB per file | capture: sha256:bd1a8fe0d062fb7445ca4a2d498c61e95f6123d40d6b2ffde1fd4e72c3458e08 | quote: There is a per-file size limit of 16 TB in CephFS. ... Ceph provides an S3-compatible protocol interface (with a per-file size limit of 5 TiB).
  - [2] 2026-11-25: an unaccessed volume can be purged after 6 months without notification | capture: sha256:55ad7cf678f4ba1338861d922385eac61171a0c4098308bd4a00596a9b83f798 | quote: Any volume that was not accessed for 6 months can be purged without notification.
  - [1] 2026-11-25: the Nautilus Ceph storage is the provider's own and free for its users | capture: sha256:ecd3c50bb186c2b8376441f1ddf23b0e9a53e0361f7ef79254b0627b94e4a52c | quote: It uses our own storage, which is free for our users and is not part of Amazon or any commercial cloud.
- sources:
  - [1] https://nrp.ai/documentation/userdocs/storage/ceph-s3/
  - [2] https://nrp.ai/documentation/userdocs/start/policies/
  - [3] https://nrp.ai/documentation/userdocs/storage/intro/
  - [4] https://s3-west.nrp-nautilus.io/
