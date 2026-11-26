# ringcentral team

> ringcentral.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ringcentral/ | JSON https://fshy.ajam.dev/api/v1/entity/ringcentral.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RingCentral Team Messaging (Glip) posts/files

- `storage/ringcentral-team-messaging-posts-files` | trial-only | evidence inferred | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:19.658Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://developers.ringcentral.com/api-reference/Message-Store/readGlipPosts
- disagrees on identity_kind: `storage/ringcentral-team-messaging` says email, `storage/ringcentral-team-messaging-posts-files` says institution
- disagrees on verdict: `storage/ringcentral-team-messaging` says fails-quota, `storage/ringcentral-team-messaging-posts-files` says trial-only
- free tier: No storage quota published; the API reference documents pagination over posts, not a media store with a byte allowance. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: x-request-max-body-size: 30m | source: [1] | note: unverified: the request-body size is not stated as a per-object cap
- retention: By default, message data is never deleted. However, Admins can choose a different retention period based on their organization's needs. | source: [1] | note: Messaging data includes chats, files, notes, and team calendar events.
- egress: Authenticated (OAuth bearer) only; attachments are downloaded through the API. No public CDN URL. | metered: no
- identity: institution
- interface: rest
- limits note: Trial-gated ('Try free' signup), per-user licensing, auth-required reads. No evidence of indefinite retention.
- interface detail: rest
- tooling: ringcentral-python / ringcentral-js SDKs; POST /team-messaging/v1/chats/{chatId}/posts with attachments.
- composes with: Not viable: paid per-user seats (a 'Try free' trial), attachment size caps, and no published permanent retention.
- reliability: Commercial UCaaS seat pricing rather than storage pricing; the free tier is a trial, so it fails the free test before retention even matters.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota published; the API reference documents pagination over posts, not a media store with a byte allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: page is the Team Messaging post-listing reference; site-wide CTA 'Try free', seat-based product, no storage quota row
  - [2] 2026-11-25: the OpenAPI specification sets a 30m request-body size on the file-upload operation | capture: sha256:1592df029df998d0928ef55c42ab16e797dd592ad7b67343b78062c2011dcbd3 | quote: x-request-max-body-size: 30m
  - [3] 2026-11-25: the file-upload guide describes a POST body carrying file contents and states no per-object size | capture: sha256:89fc2be81c0e2b37b21890e07b23dfd243d165191596f18aeaf2cb7be91cddcc | quote: To upload a file, one conducts an HTTP POST to the following URI, using the file's contents as the post body.
  - [4] 2026-11-25: the default is no deletion, with admin-selected retention periods | capture: sha256:ac6a7839a9cecd7266256b88a946f99fbee778949f4874f57f315303a6685cf3 | quote: By default, message data is never deleted. However, Admins can choose a different retention period based on their organization's needs.
  - [4] 2026-11-25: the retention rule covers chats, files, notes and team calendar events | capture: sha256:ac6a7839a9cecd7266256b88a946f99fbee778949f4874f57f315303a6685cf3 | quote: Messaging data includes chats, files, notes, and team calendar events.
- sources:
  - [1] https://developers.ringcentral.com/api-reference/Message-Store/readGlipPosts
  - [2] https://assets-developers.ringcentral.com/dpw/api-reference/specs/public/office/rc-platform.yml?v=2026112520261102-0525
  - [3] https://developers.ringcentral.com/guide/team-messaging/posting/file-uploads
  - [4] https://support.ringcentral.com/article-v2/managing-data-retention-for-ringex-messages.html?brand=RingCentral&product=RingEX&language=en_US

## ringcentral team messaging

- `storage/ringcentral-team-messaging` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:03.330Z (live) | stale on 2026-12-04
- url https://developers.ringcentral.com/api-reference/Message-Store/readGlipPosts
- disagrees on identity_kind: `storage/ringcentral-team-messaging` says email, `storage/ringcentral-team-messaging-posts-files` says institution
- disagrees on verdict: `storage/ringcentral-team-messaging` says fails-quota, `storage/ringcentral-team-messaging-posts-files` says trial-only
- free tier: none reachable: Seat-licensed UCaaS with a trial, not a free tier; auth-only reads; no published storage allowance. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Seat-licensed UCaaS with a trial, not a free tier; auth-only reads; no published storage allowance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Seat-licensed UCaaS with a trial, not a free tier; auth-only reads; no published storage allowance.
  - [2] 2026-11-19: RingEX team messaging is paid with a 14-day trial, not a free storage tier | capture: sha256:adf792632be74d4a0505e5c5ca26bf4e9d603c8cda4de5107c681ad92384a10e | quote: Yes. Free trial is available to new subscribers only. During the 14-day free trial, you will receive support for up to 20 phone lines.
- sources:
  - [1] https://developers.ringcentral.com/api-reference/Message-Store/readGlipPosts
  - [2] https://www.ringcentral.com/office/plansandpricing.html
