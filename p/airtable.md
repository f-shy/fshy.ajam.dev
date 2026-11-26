# Airtable

> airtable.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/airtable/ | JSON https://fshy.ajam.dev/api/v1/entity/airtable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Airtable (free plan) - attachment fields

- `storage/airtable-attachment-fields` | qualifies-with-caveat | evidence reported | binding request-rate | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-25T03:33:11.121Z (live) | stale on 2026-12-10
- url https://airtable.com
- free tier: 1 GB of attachment storage per base on the Free plan | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Individual attachments can be up to 5 GB; on the Free plan the per-base allowance caps a single attachment at 1 GB. | source: [1] | note: On the Free plan a single attachment is capped at 1 GB by the 1 GB per-base attachment allowance; the direct file-bytes upload API accepts at most 5 MB.
- retention: source: [1] | note: The Free plan includes 2 weeks of revision and snapshot history; Airtable states it never removes data when record or attachment limits are reached.
- egress: Free; attachments served from airtableusercontent.com (CloudFront-fronted) with expiring signed URLs | metered: no
- identity: institution | detail: unverified: the sign-up page rendered no form fields on 2026-11-09
- interface: rest
- limits:
  - request-rate (binding): 1000 API calls per workspace per month [1]
- limits note: 1,000 records per base on Free; 5 MB per direct API upload; 1,000 API calls per workspace per MONTH on Free; only 5 editor/creator collaborators; 1 GB per base is the billing-flag field maxTotalAttachmentSizeInBytes=1000000000
- binding note: calls are bounded rather than bytes, which is fatal to a nightly job on a monthly counter
- interface detail: rest
- tooling: Official Web API v0: POST /v0/{baseId}/{recordId}/{attachmentFieldId}/uploadAttachment accepts raw bytes up to 5 MB, larger files go via the content.airtable.com upload-then-attach flow
- composes with: 1 GB x 1,500 bases x N workspaces = ~1.5 TB per free workspace as documented, multiplied by unlimited free workspaces. Pricing config also states 'unlimited bases' on Free; the 1,500 figure is the per-workspace cap. This is the single largest documented multiplicative figure in this area.
- reliability: 1,000 API calls per month on Free is a hard wall - that is ~33 uploads/day, so the 1.5 TB chain is rate-limited long before it is capacity-limited.
- notes: 1 GB attachment storage per base on Free, with unlimited bases and 1,500 bases per workspace
- evidence:
  - [1] 2026-10-21: 'How many bases can a single workspace store? 1500 Bases per workspace'; also '1000 records per base... 1GB per of attachment storage per base' for the Free tier
  - [2] 2026-10-21: (raw page JSON) - Free plan object: maxTotalAttachmentSizeInBytes=1000000000, maxRowsPerApplication=1000, 'descriptionMarkdown: Unlimited bases / 1,000 records per base / 1GB attachment space per base'; Enterprise: maxTotalAttachmentSizeInBytes=1000000000000 (1 TB/base)
  - [3] 2026-10-21: 'Upload an attachment up to 5 MB to an attachment cell via the file bytes directly'
  - [4] 2026-10-21: probe: GET -> HTTP 401 (API live, auth-gated)
  - [1] 2026-11-09: the Free plan's 1GB per-base attachment storage is unchanged | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1GB per of [attachment storage](https://support.airtable.com/docs/attachment-field) per base
  - [3] 2026-11-09: a direct file-bytes upload is capped at 5 MB | capture: sha256:899958232dcb5f0f57dd474f14dc43f14e69c153dd3a58c6b5ed4ef286a84a98 | quote: Upload an attachment up to 5 MB to an attachment cell via the file bytes directly.
  - [1] 2026-11-09: the Free plan allows 1000 API calls per workspace per month | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1000 [API calls](https://support.airtable.com/docs/getting-started-with-airtables-web-api#api-record-limits) per workspace per month
  - [5] 2026-11-09: the sign-up page rendered only a shell, with no form fields | capture: sha256:6d1570815405e08b350f9e274ca825947069cfd9554cccb8bfd0563c43d8d375 | quote: ## Welcome to Airtable
  - [1] 2026-11-19: the free-plan API call cap is unchanged at 1000 per workspace per month | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1000 [API calls](https://support.airtable.com/docs/getting-started-with-airtables-web-api#api-record-limits) per workspace per month
  - [3] 2026-11-19: the direct-upload per-object cap is unchanged at 5 MB | capture: sha256:899958232dcb5f0f57dd474f14dc43f14e69c153dd3a58c6b5ed4ef286a84a98 | quote: Upload an attachment up to 5 MB to an attachment cell via the file bytes directly.
  - [6] 2026-11-25: the attachment-field documentation states a 5 GB individual attachment limit | capture: sha256:50a1e24221905e9d171b312e08a58c186c3902c970fb7640372e084d74e74a24 | quote: Airtable supports individual attachments up to 5GB in size
  - [6] 2026-11-25: the Free plan reduces the single-attachment maximum to 1 GB | capture: sha256:50a1e24221905e9d171b312e08a58c186c3902c970fb7640372e084d74e74a24 | quote: - *Note that this will also reduce the size that a single attachment can be from 20 GB to 1 GB
  - [1] 2026-11-25: the Free plan states a 2 week revision and snapshot history | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 2 weeks of [revision and snapshot history](https://support.airtable.com/docs/taking-and-restoring-base-snapshots)
  - [3] 2026-11-25: the direct file-bytes upload endpoint accepts at most 5 MB | capture: sha256:899958232dcb5f0f57dd474f14dc43f14e69c153dd3a58c6b5ed4ef286a84a98 | quote: Upload an attachment up to 5 MB to an attachment cell via the file bytes directly.
  - [2] 2026-11-25: Airtable states data is not removed when limits are reached | capture: sha256:bc7507c4bb9cfbcc36a5baea0d500caeac2c263e5fa980ffa0b73d665b90615c | quote: If you reach (or are over) our record or attachment limits, you’ll still be able to use your bases and we will never remove your data.
  - [1] 2026-11-25: the 1 GB per-base attachment allowance is unchanged | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1GB per of [attachment storage](https://support.airtable.com/docs/attachment-field) per base
  - [1] 2026-11-25: the 1000-call monthly API limit is unchanged | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1000 [API calls](https://support.airtable.com/docs/getting-started-with-airtables-web-api#api-record-limits) per workspace per month
  - [6] 2026-11-25: the 5 GB individual attachment limit is stated | capture: sha256:50a1e24221905e9d171b312e08a58c186c3902c970fb7640372e084d74e74a24 | quote: Airtable supports individual attachments up to 5GB in size
- sources:
  - [1] https://support.airtable.com/docs/airtable-plans
  - [2] https://airtable.com/pricing
  - [3] https://airtable.com/developers/web/api/upload-attachment
  - [4] https://api.airtable.com/v0/meta/bases
  - [5] https://airtable.com/signup
  - [6] https://support.airtable.com/docs/attachment-field

## airtable for nonprofits (50% off, not free)

- `storage/airtable-for-nonprofits` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T21:15:53.937Z (live) | stale on 2026-12-04
- url https://support.airtable.com/articles/2277136852-airtable-plans-overview
- free tier: None reachable: Nonprofit plans are 'a 50% monthly discount per user on Team plans'. Not a grant. Attachment storage per base: Free 1 GB, Team 20 GB, Business 100 GB, Enterprise 'Unlimited attachment stora. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: No per-object size cap stated; attachment storage is a per-base total (1 GB Free, 20 GB Team, 100 GB Business). | source: [1] | note: not applicable
- retention: Revision and snapshot history is kept for 2 weeks on Free and 1 year on Team and Business; attachment lifetime is otherwise not stated. | source: [1]
- egress: stated-absent: the first-party plans page states no price or quota for traffic out of Airtable | metered: no
- identity: email | detail: A credit card is required to pay for a discounted nonprofit Team plan.
- interface: rest
- interface detail: A workspace/database product reached through a REST API and the web app; attachments are held per base.
- tooling: not documented
- composes with: stated-absent: the first-party plans page states no way to chain attachment storage with other services
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
  - [1] 2026-11-19: the nonprofit offer is a discount on a paid plan, not a free grant | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: Airtable offers 50% off the monthly cost of the Team plan for qualifying organizations.
  - [2] 2026-11-19: a credit card is required to pay for a discounted nonprofit Team plan | capture: sha256:bf18859c56626cc403b406122e2cbf4bfc93dd4a30be7e32da8e2c47ad18841a | quote: Discounted Team plans must be paid using a credit card.
  - [1] 2026-11-19: the first-party plans page documents a REST API quota | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1000 [API calls]
  - [1] 2026-11-19: the first-party Free-plan table states a 2-week revision and snapshot history | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 2 weeks of [revision and snapshot history]
  - [1] 2026-11-19: the first-party Free-plan table states attachment storage per base and no per-object cap | capture: sha256:db0cd8f2c67bfa465dfc4ba9341815e87f74a60840d4e6477d0dab43e225b84b | quote: 1GB per of [attachment storage] per base
- sources:
  - [1] https://support.airtable.com/articles/2277136852-airtable-plans-overview
  - [2] https://support.airtable.com/articles/4920135568-applying-for-non-profit-education-and-student-airtable-plans
