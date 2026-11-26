# Cisco Webex

> webex.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webex/ | JSON https://fshy.ajam.dev/api/v1/entity/webex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cisco Webex — Messages API file attachments

- `storage/cisco-webex-messages-api-file-attachments` | fails-egress | evidence inferred | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://developer.webex.com/docs/basics#message-attachments
- free tier: No storage quota published. Per-attachment cap is the only hard number: 'Message attachments are limited to 100MB each.' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention is governed by the org's retention policy (license-dependent); free-tier spaces are not a documented permanent store | source: [1] | note: not stated
- egress: No per-GB egress charge found, but files are fetched by authenticated API call or a short-lived download URL tied to the message. Not an anonymous CDN path. | metered: no
- identity: institution
- interface: rest
- limits note: 100 MB per attachment. Retention is governed by the org's retention policy (license-dependent); free-tier spaces are not a documented permanent store. Auth required for every read.
- interface detail: rest
- tooling: webexteamssdk / webex-python-sdk; POST /v1/messages with multipart files, GET /v1/contents/{id}. Room Tabs API can attach a persistent URL to a space but does not store bytes.
- composes with: 100 MB/attachment x unlimited messages in a space is genuinely large in principle, but free Webex accounts have message-retention limits and the org pays per user beyond the free tier.
- reliability: Retention is policy-driven rather than fixed, so an admin policy change or license lapse can remove content without any API-visible warning. Unverified for the free tier specifically. Blocked from the retention help page.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No storage quota published. Per-attachment cap is the only hard number: 'Message attachments are limited to 100MB each.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Message attachments are limited to 100MB each.'
  - [2] 2026-10-21: unverified: blocked by challenge (no retention number obtained)
- sources:
  - [1] https://developer.webex.com/docs/basics#message-attachments
  - [2] https://help.webex.com/en-us/article/8c1lzx/Manage-retention-policies-in-Webex-App
