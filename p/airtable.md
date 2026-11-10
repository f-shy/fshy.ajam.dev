# Airtable

> airtable.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/airtable/ | JSON https://fshy.ajam.dev/api/v1/entity/airtable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Airtable (free plan) - attachment fields

- `storage/airtable-attachment-fields` | qualifies-with-caveat | evidence reported | binding request-rate | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://airtable.com
- free tier: 1 GB attachment storage per base on Free, with unlimited bases and 1,500 bases per workspace | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; attachments served from airtableusercontent.com (CloudFront-fronted) with expiring signed URLs | metered: no
- identity: institution
- interface: rest
- limits:
  - request-rate (binding): 33 uploads/day [1]
- limits note: 1,000 records per base on Free; 5 MB per direct API upload; 1,000 API calls per workspace per MONTH on Free; only 5 editor/creator collaborators; 1 GB per base is the billing-flag field maxTotalAttachmentSizeInBytes=1000000000
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: rest
- tooling: Official Web API v0: POST /v0/{baseId}/{recordId}/{attachmentFieldId}/uploadAttachment accepts raw bytes up to 5 MB, larger files go via the content.airtable.com upload-then-attach flow
- composes with: 1 GB x 1,500 bases x N workspaces = ~1.5 TB per free workspace as documented, multiplied by unlimited free workspaces. Pricing config also states 'unlimited bases' on Free; the 1,500 figure is the per-workspace cap. This is the single largest documented multiplicative figure in this area.
- reliability: 1,000 API calls per month on Free is a hard wall - that is ~33 uploads/day, so the 1.5 TB chain is rate-limited long before it is capacity-limited.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'How many bases can a single workspace store? 1500 Bases per workspace'; also '1000 records per base... 1GB per of attachment storage per base' for the Free tier
  - [2] 2026-10-21: (raw page JSON) - Free plan object: maxTotalAttachmentSizeInBytes=1000000000, maxRowsPerApplication=1000, 'descriptionMarkdown: Unlimited bases / 1,000 records per base / 1GB attachment space per base'; Enterprise: maxTotalAttachmentSizeInBytes=1000000000000 (1 TB/base)
  - [3] 2026-10-21: 'Upload an attachment up to 5 MB to an attachment cell via the file bytes directly'
  - [4] 2026-10-21: probe: GET -> HTTP 401 (API live, auth-gated)
- sources:
  - [1] https://support.airtable.com/docs/airtable-plans
  - [2] https://airtable.com/pricing
  - [3] https://airtable.com/developers/web/api/upload-attachment
  - [4] https://api.airtable.com/v0/meta/bases

## airtable for nonprofits (50% off, not free)

- `storage/airtable-for-nonprofits` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://support.airtable.com/articles/2277136852-airtable-plans-overview
- free tier: None reachable: Nonprofit plans are 'a 50% monthly discount per user on Team plans'. Not a grant. Attachment storage per base: Free 1 GB, Team 20 GB, Business 100 GB, Enterprise 'Unlimited attachment stora. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Nonprofit plans are 'a 50% monthly discount per user on Team plans' — not a grant. Attachment storage per base: Free 1 GB, Team 20 GB, Business 100 GB, Enterprise 'Unlimited attachment…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Nonprofit plans are 'a 50% monthly discount per user on Team plans' — not a grant. Attachment storage per base: Free 1 GB, Team 20 GB, Business 100 GB, Enterprise 'Unlimited attachment…
  - [2] 2026-10-21: cited as the basis of the rejection: Nonprofit plans are 'a 50% monthly discount per user on Team plans' — not a grant. Attachment storage per base: Free 1 GB, Team 20 GB, Business 100 GB, Enterprise 'Unlimited attachment stora
- sources:
  - [1] https://support.airtable.com/articles/2277136852-airtable-plans-overview
  - [2] https://support.airtable.com/articles/4920135568-applying-for-non-profit-education-and-student-airtable-plans
