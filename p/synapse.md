# Synapse

> synapse.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/synapse/ | JSON https://fshy.ajam.dev/api/v1/entity/synapse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Synapse (Sage Bionetworks)

- `storage/synapse` | qualifies-with-caveat | evidence inferred | binding per-ip-shaping | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:23.062Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://www.synapse.org
- free tier: No clear public storage cap found. Platform is free SaaS on S3; documented pain point is a '1GB per day' quota on modelState (compute artifacts), not on file storage. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: The upload page states that Synapse can store files of all types within a project and gives no per-file size limit.
- retention: No retention period is stated on the upload page; files must be stored within a project. | source: [1] | note: The upload page states no retention period; files must be stored within a project.
- egress: Anonymous users cannot create projects in Synapse, upload or download data, add wiki content, or comment in a discussion forums. | metered: no
- identity: anonymous | detail: Certified users have access to full Synapse functionality, including the ability to upload files and tables as well as create folders.
- interface: s3, rest, oci
- limits:
  - per-ip-shaping (binding): 1GB per day [1]
  - per-ip-shaping (binding): 1 GB/day [1]
- limits note: per-object-cap: none documented for plain files; 1 GB/day on modelState. Retention: indefinite for public content. Gate: upload requires 'certified user' status (a quiz), so no anonymous write path exists.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: Python/Java/R clients (`synapseclient`), REST API, and a built-in Docker registry. Also supports custom storage locations (your own S3/GCS). Which makes it a metadata layer over someone else's bucket rather than storage itself.
- composes with: Synapse provides physical storage for files using Amazon S3, however, you can configure your own custom storage locations as well.
- reliability: Certification gate plus no published quota means capacity is discretionary; large uploads are known to be throttled/queued without a documented ceiling. Treat quota as unverified.
- notes: Files must be stored within a project.
- evidence:
  - [1] 2026-10-21: 'you need to be a certified user', S3-backed, no quota stated
  - [2] 2026-10-21: files can live in your own S3/GCS bucket, Synapse keeps metadata
  - [3] 2026-10-21: 'Model State exceeded 1GB per day quota'
  - [4] 2026-11-09: the account-types page states certified users can upload files and tables | capture: sha256:50d324dff3cfd9e831ea93b914a2fc171c311e23d111984a9cd057f691601564 | quote: Certified users have access to full Synapse functionality, including the ability to upload files and tables as well as create folders.
  - [1] 2026-11-09: the upload page states files are stored in projects and gives no storage quota, per-file cap or retention figure | capture: sha256:9b7477f07e26cf475e48da370a20e33828c562411bfefcec762f11f94f949f92 | quote: Files must be stored within a project.
  - [1] 2026-11-11: the upload page states that files must be stored within a project | capture: sha256:d74bd42b0845910c730a337e671a633ea7134b23a76a95f453eaca50ff085816 | quote: Files must be stored within a project.
  - [1] 2026-11-25: the upload page states the kinds of files and their location without a per-file size limit | capture: sha256:9b7477f07e26cf475e48da370a20e33828c562411bfefcec762f11f94f949f92 | quote: Synapse can be used to store files of all types. Files must be stored within a project.
  - [1] 2026-11-25: the upload page states where files are stored and gives no retention period | capture: sha256:9b7477f07e26cf475e48da370a20e33828c562411bfefcec762f11f94f949f92 | quote: Synapse can be used to store files of all types. Files must be stored within a project.
  - [1] 2026-11-25: the upload page gives no retention period and requires files to be inside a project | capture: sha256:9b7477f07e26cf475e48da370a20e33828c562411bfefcec762f11f94f949f92 | quote: Synapse can be used to store files of all types. Files must be stored within a project.
  - [1] 2026-11-25: the upload page states file storage within a project with no cap or retention period | capture: sha256:9b7477f07e26cf475e48da370a20e33828c562411bfefcec762f11f94f949f92 | quote: Synapse can be used to store files of all types. Files must be stored within a project.
  - [4] 2026-11-25: the account-types page denies anonymous downloads | capture: sha256:50d324dff3cfd9e831ea93b914a2fc171c311e23d111984a9cd057f691601564 | quote: Anonymous users cannot create projects in Synapse, upload or download data, add wiki content, or comment in a discussion forums.
  - [4] 2026-11-25: the account-types page still denies anonymous downloads | capture: sha256:50d324dff3cfd9e831ea93b914a2fc171c311e23d111984a9cd057f691601564 | quote: Anonymous users cannot create projects in Synapse, upload or download data, add wiki content, or comment in a discussion forums.
  - [2] 2026-11-25: the custom-storage page documents Synapse S3 storage and user-configured storage locations | capture: sha256:58b2c94ed60369767f0796581af4c8238b1fb9cd913278080ec78cbac80edd2d | quote: Synapse provides physical storage for files using Amazon S3, however, you can configure your own custom storage locations as well.
  - [2] 2026-11-25: the custom-storage page still documents user-configured storage locations | capture: sha256:58b2c94ed60369767f0796581af4c8238b1fb9cd913278080ec78cbac80edd2d | quote: Synapse provides physical storage for files using Amazon S3, however, you can configure your own custom storage locations as well.
- sources:
  - [1] https://docs.synapse.org/synapse-docs/uploading-and-organizing-data
  - [2] https://docs.synapse.org/synapse-docs/custom-storage-locations
  - [3] https://www.synapse.org/Synapse:syn4224222/discussion/threadId=1648
  - [4] https://docs.synapse.org/synapse-docs/synapse-user-account-types
