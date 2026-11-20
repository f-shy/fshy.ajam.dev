# Rocket.Chat self-hosted

> rocket.chat | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rocket/ | JSON https://fshy.ajam.dev/api/v1/entity/rocket.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rocket.chat starter / community

- `storage/rocket-chat-starter-community` | self-hosted, last resort | verdict paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.rocket.chat/docs/our-plans
- free tier: none reachable: Both free tiers are self-managed/self-hosted: you supply the storage. Cloud Starter is a 30-day trial, not a free tier. No free hosted storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: Both free tiers are self-managed/self-hosted: you supply the storage. Cloud Starter is a 30-day trial, not a free tier. No free hosted storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both free tiers are self-managed/self-hosted: you supply the storage. Cloud Starter is a 30-day trial, not a free tier. No free hosted storage.
- sources:
  - [1] https://docs.rocket.chat/docs/our-plans

## Rocket.Chat self-hosted (Community / Starter)

- `storage/rocket-chat-self-hosted` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.rocket.chat/docs/our-plans
- free tier: No storage quota. Per-file ceiling is a single setting: 'Maximum File Upload Size (in bytes) ... Use -1 to remove the limit.' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Your own infrastructure. Cloud-hosted workspaces have a storage limit visible in the admin panel, but self-managed does not. | metered: no
- identity: email
- interface: s3, rest, webdav
- limits note: Starter: up to 50 users, self-managed. Community: up to 100 concurrent users, self-hosted only, 10,000 push notifications/month. Per-file limit unlimited if set to -1.
- interface detail: rest
- tooling: Rocket.Chat REST API `POST /api/v1/rooms.media/{rid}` + `rooms.mediaConfirm`. Storage backends: GridFS (MongoDB, default), AmazonS3/MinIO, Google Cloud Storage, WebDAV, FileSystem. The WebDAV and S3 backends make it pluggable into anything.
- composes with: N workspaces x unlimited rooms. The WebDAV backend is the interesting bit: it turns Rocket.Chat into a front-end over any WebDAV store, so it chains rather than multiplies.
- reliability: Solid; the default GridFS backend stores blobs inside MongoDB, which is a poor choice at TB scale (the docs themselves recommend S3/MinIO). Files can be JWT-protected or public per workspace setting.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota. Per-file ceiling is a single setting: 'Maximum File Upload Size (in bytes) ... Use -1 to remove the limit.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Maximum File Upload Size (in bytes) ... Use -1 to remove the limit.'
  - [1] 2026-10-21: 'Storage Type ... GridFS ... AmazonS3 ... Google Cloud Storage ... WebDAV ... FileSystem. We recommend Amazon S3, Minio, or Google Cloud Storage.'
  - [2] 2026-10-21: 'Starter | Up to 50 users | Self-managed and self-hosted'; 'Community | Up to 100 concurrent users | Self-hosted only'
- sources:
  - [1] https://docs.rocket.chat/docs/file-upload
  - [2] https://docs.rocket.chat/docs/our-plans
