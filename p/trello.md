# Trello card attachments

> trello.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trello/ | JSON https://fshy.ajam.dev/api/v1/entity/trello.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trello card attachments

- `storage/trello-card-attachments` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://trello.com
- free tier: 10 MB per attachment on Free, 250 MB on Standard. And explicitly 'there is no total limit for storage, just a per-file limit'. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB/file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free direct download links, Atlassian CDN; no egress metering published | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 MB/file [1]
- limits note: 10 MB/file on Free; per-board attachment ceiling exists in the API response model (limits.attachments.perBoard warnAt 32400 / disableAt 36000). I.e. ~32k attachments/board before hard stop; 10 MB is small for bulk data.
- interface detail: rest
- tooling: documented Trello REST API: POST /1/cards/{id}/attachments (multipart file or url), plus GET /1/cards/{id}/attachments; py-trello and trello-rclone-style wrappers exist
- composes with: unlimited cards x 10 MB x unlimited boards x unlimited free Workspaces (10 members each). This is genuinely 'per-record unlimited': no bucket cap, only a per-file cap. 500 GB = 51,200 attachments
- reliability: attachments are real copies inside Trello ('Attachments from your computer create an actual copy within Trello'); Atlassian has deprecated/changed API auth (key+token still works) but attachments have been stable for a decade
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '10MB limit for each attachment (there is no total limit for storage, just a per-file limit)' and '250MB limit for each attachment' on Standard
  - [2] 2026-10-21: POST attachments, live API reference
  - [3] 2026-10-21: 'Attachments from your computer create an actual copy within Trello'
- sources:
  - [1] https://support.atlassian.com/trello/docs/which-trello-plan-is-best-for-me/
  - [2] https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-attachments-post
  - [3] https://support.atlassian.com/trello/docs/adding-attachments-to-cards/
