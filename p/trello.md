# Trello card attachments

> trello.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/trello/ | JSON https://fshy.ajam.dev/api/v1/entity/trello.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Trello card attachments

- `storage/trello-card-attachments` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:24.771Z (live) | stale on 2026-12-10
- url https://trello.com
- free tier: 10MB limit for each attachment (there is no total limit for storage, just a per-file limit) | unit: unlimited | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: 10 MB/file | bytes: 10000000 | source: [1] | note: 10MB limit for each attachment; no total storage limit.
- retention: Deleting an attachment permanently removes the file from Amazon S3; deleting a card also deletes its attached files. | source: [1] | note: Deleting an attachment permanently removes the file from Amazon S3; deleting a card also deletes its attached files.
- egress: Uploaded attachments require user authorization to display; attachments and previews on public boards remain accessible without an account. | metered: no
- identity: institution | detail: unverified: the plan page states no registration requirement
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 MB/file [1]
- limits note: 10 MB/file on Free; per-board attachment ceiling exists in the API response model (limits.attachments.perBoard warnAt 32400 / disableAt 36000). I.e. ~32k attachments/board before hard stop; 10 MB is small for bulk data.
- interface detail: rest
- tooling: documented Trello REST API: POST /1/cards/{id}/attachments (multipart file or url), plus GET /1/cards/{id}/attachments; py-trello and trello-rclone-style wrappers exist
- composes with: Free plan: up to 10 open boards and up to 10 Collaborators; 10MB per attachment with no total storage limit.
- reliability: attachments are real copies inside Trello ('Attachments from your computer create an actual copy within Trello'); Atlassian has deprecated/changed API auth (key+token still works) but attachments have been stable for a decade
- notes: 10 MB per attachment on Free, 250 MB on Standard. And explicitly 'there is no total limit for storage, just a per-file limit'.
- evidence note: the support.atlassian.com plan page states a 10MB limit for each attachment with no total storage limit
- evidence:
  - [1] 2026-10-21: '10MB limit for each attachment (there is no total limit for storage, just a per-file limit)' and '250MB limit for each attachment' on Standard
  - [2] 2026-10-21: POST attachments, live API reference
  - [3] 2026-10-21: 'Attachments from your computer create an actual copy within Trello'
  - [1] 2026-11-09: the Free plan allows a 10MB attachment with no total storage limit | capture: sha256:781986390b01ac35a0fe016a68ee87df95a30ba0280674aa76d68bbccafe14af | quote: 10MB limit for each attachment (there is no total limit for storage, just a per-file limit)
  - [1] 2026-11-25: the free plan limits each attachment to 10MB with no total storage limit | capture: sha256:781986390b01ac35a0fe016a68ee87df95a30ba0280674aa76d68bbccafe14af | quote: 10MB limit for each attachment (there is no total limit for storage, just a per-file limit)
  - [3] 2026-11-25: attachment and card deletion permanently removes the stored files | capture: sha256:149082f49aae8ae0166ad7e3fe128b1f430a79ea8e91c6b6216b608f6c7da0e8 | quote: Deleting the attachment in Trello permanently removes the file from Amazon S3. Deleting a card will also delete any files attached to that card.
  - [3] 2026-11-25: uploaded attachments check authorization, except on public boards where they remain accessible without an account | capture: sha256:149082f49aae8ae0166ad7e3fe128b1f430a79ea8e91c6b6216b608f6c7da0e8 | quote: Effective December 1, 2023, all uploaded attachments will check for user authorization in order to display the file due to security considerations. ... Attachments and previews on public boards will remain fully accessible without an account.
  - [1] 2026-11-25: the free plan lists 10 open boards, 10 collaborators and a 10MB attachment limit with no total storage limit | capture: sha256:781986390b01ac35a0fe016a68ee87df95a30ba0280674aa76d68bbccafe14af | quote: - Up to 10 open boards - Up to 10 [Collaborators](https://support.atlassian.com/trello/docs/workspace-user-limit/) - Unlimited Power-Ups - 10MB limit for each attachment (there is no total limit for storage, just a per-file limit)
- sources:
  - [1] https://support.atlassian.com/trello/docs/which-trello-plan-is-best-for-me/
  - [2] https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-attachments-post
  - [3] https://support.atlassian.com/trello/docs/adding-attachments-to-cards/
