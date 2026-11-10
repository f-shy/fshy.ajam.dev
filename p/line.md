# line messaging

> line.biz | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/line/ | JSON https://fshy.ajam.dev/api/v1/entity/line.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## line messaging api content

- `storage/line-messaging-api-content` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.line.biz/en/docs/messaging-api/receiving-messages/
- free tier: none reachable: Auto-deleted after an undisclosed period, no listing endpoint, token-only access. Cannot be addressed as storage even short-term. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: Auto-deleted after an undisclosed period, no listing endpoint, token-only access. Cannot be addressed as storage even short-term.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Auto-deleted after an undisclosed period, no listing endpoint, token-only access. Cannot be addressed as storage even short-term.
- sources:
  - [1] https://developers.line.biz/en/docs/messaging-api/receiving-messages/

## LINE Messaging API — message content endpoint

- `storage/line-messaging-api-message-content-endpoint` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.line.biz/en/docs/messaging-api/receiving-messages/
- free tier: No storage quota is offered at all. Content is a delivery mechanism, not a store. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Retrieval is authenticated only: GET /v2/bot/message/{messageId}/content with a channel access token. No public URL is ever issued. | metered: no
- identity: national-id
- interface: rest
- limits note: Explicit auto-deletion with an undisclosed period: 'Content that users send is automatically deleted after a certain period of time.' LINE does not publish the number, which is worse than a known 30 days because it cannot be reasoned about. No listing endpoint, no bulk download.
- interface detail: rest
- tooling: Line-bot-sdk (Python/Node/Java/Go/PHP). The SDK exposes get_message_content() and nothing else. No listing, no expiry control, no bulk export.
- composes with: Not chainable: there is no enumeration API, so you cannot even address stored objects after the fact without having logged every messageId yourself.
- reliability: Undisclosed retention window plus no enumeration = data becomes unreachable silently. Cannot be used even as a 7-day cache reliably.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota is offered at all. Content is a delivery mechanism, not a store.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Content that users send is automatically deleted after a certain period of time.'
  - [2] 2026-10-21: probe: GET -> 401 (token mandatory, anonymous read impossible)
- sources:
  - [1] https://developers.line.biz/en/docs/messaging-api/receiving-messages/
  - [2] https://api-data.line.me/v2/bot/message/1234567890/content
