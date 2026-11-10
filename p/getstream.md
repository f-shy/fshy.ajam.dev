# Stream Chat

> getstream.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getstream/ | JSON https://fshy.ajam.dev/api/v1/entity/getstream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stream Chat (GetStream) free/Maker plan

- `storage/stream-chat-free-maker-plan` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://getstream.io/chat/docs/node/storage-and-bandwidth/
- free tier: No free storage allowance stated as a byte figure on the storage page; instead 'Stream applies fair-usage limits to storage, bandwidth, and API calls on every Chat plan' with overage rates once exceeded. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Metered past the fair-use allowance. 'You only start to pay extra for storage and bandwidth after you exceed these fair usage limits'. Attachments are served from Stream's CDN but are tied to channel membership/auth. | metered: yes
- identity: institution
- interface: rest
- limits note: Fair-usage storage + bandwidth ceiling; user-configurable retention policies exist expressly to REDUCE storage, which signals storage is the cost centre. Attachment size caps apply. Overage is billed per GB.
- interface detail: rest
- tooling: Stream-chat SDKs (JS/React/Node/Python); server-side client can upload attachments to a channel. No bulk/opaque-object API. Attachment shape is image/file on a message.
- composes with: Fails the multiplication test: fair-use storage caps plus per-GB overage means more accounts is the only lever, and each account is a SaaS tenant with its own MAU billing.
- reliability: No deletion cliff, but a billing cliff: exceeding fair use converts free storage into an invoice rather than an error, which is worse for a fixed-budget client.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No free storage allowance stated as a byte figure on the storage page; instead 'Stream applies fair-usage limits to storage, bandwidth, and API calls on every Chat plan' with overage rates once exceeded.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Stream applies fair-usage limits to storage, bandwidth, and API calls on every Chat plan. You only start to pay extra for storage and bandwidth after you exceed these fair usage limits.'
  - [2] 2026-10-21: read live: 'Chat Message Storage ... Additional usage costs when stored messages exceed the included amount'
- sources:
  - [1] https://getstream.io/chat/docs/node/storage-and-bandwidth/
  - [2] https://getstream.io/chat/pricing/

## stream chat free plan as bulk storage

- `storage/stream-chat-free-plan-as-bulk-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://getstream.io/chat/docs/node/storage-and-bandwidth/
- free tier: none reachable: Fair-usage storage ceiling with per-GB overage; converting free into an invoice is a fail, not a qualification. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Fair-usage storage ceiling with per-GB overage; converting free into an invoice is a fail, not a qualification.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Fair-usage storage ceiling with per-GB overage; converting free into an invoice is a fail, not a qualification.
- sources:
  - [1] https://getstream.io/chat/docs/node/storage-and-bandwidth/
