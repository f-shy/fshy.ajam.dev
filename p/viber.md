# viber business

> viber.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/viber/ | JSON https://fshy.ajam.dev/api/v1/entity/viber.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## viber business as a media host

- `storage/viber-business-as-a-media-host` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.viber.com/docs/api/rest-bot-api/#send-message
- free tier: none reachable: Inverted API: Viber consumes your public image URL, it never produces one. 1-3 MB cap on your file. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Inverted API: Viber consumes your public image URL, it never produces one. 1-3 MB cap on your file.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Inverted API: Viber consumes your public image URL, it never produces one. 1-3 MB cap on your file.
- sources:
  - [1] https://developers.viber.com/docs/api/rest-bot-api/#send-message

## Viber Business Messages / REST Bot API

- `storage/viber-business-messages-rest-bot-api` | fails-quota | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.viber.com/docs/api/rest-bot-api/
- free tier: No storage quota. Same inversion as Kakao: you pass a picture URL, Viber fetches it. Max image 1 MB on iOS, 3 MB on Android, thumbnail 100 KB. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A. Viber hosts nothing for you. It requires 'The URL must have a resource with a .jpeg, .png or .gif file extension as the last path segment', i.e. it is a consumer of your public URLs. | metered: no
- identity: email
- interface: rest
- limits note: 1 MB (iOS) / 3 MB (Android) image cap applies to the file YOU host; Viber rejects larger. Business messaging also requires partner onboarding for phone-number-based sends.
- interface detail: rest
- tooling: viber-bot-python / raw REST POST to https://chatapi.viber.com/pa/send_message. Sender-only API.
- composes with: Not chainable. No upload, no media_id, no listing, no retention. Structurally incapable of storing a byte.
- reliability: Messaging API functions as a media URL consumer rather than a media hosting repository.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota — same inversion as Kakao: you pass a picture URL, Viber fetches it. Max image 1 MB on iOS, 3 MB on Android, thumbnail 100 KB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'media | URL of the image (JPEG, PNG, non-animated GIF) | required. The URL must have a resource with a .jpeg, .png or .gif file extension as the last path segment ... Max image size: 1MB on iOS, 3MB on Android.'
- sources:
  - [1] https://developers.viber.com/docs/api/rest-bot-api/#send-message
