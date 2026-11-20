# basecamp for free

> basecamp-help.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/basecamp-help/ | JSON https://fshy.ajam.dev/api/v1/entity/basecamp-help.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## basecamp for free

- `storage/basecamp-for-free` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:03:51.457Z (live) | stale on 2026-12-04
- url https://5.basecamp-help.com/article/1144-basecamp-for-free
- free tier: 1 GB of file storage, 1 project and 3 users on the permanent free plan; additional storage and public sharing links are not available on the free plan | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: the free plan asks for no credit card; other sign-up fields: unverified: behind a sign-up
- interface: rest
- limits:
  - volume-quota (binding): 1 GB of file storage on the free plan [1]
- limits note: additional storage is not available on the free plan; the largest paid plan, Pro Unlimited, holds 1000 GB (1 TB) at $199/mo billed annually
- binding note: the free plan holds 1 GB of file storage and additional storage is not an option on it
- interface detail: REST API: create an attachment, then create an upload in a project vault
- tooling: vendor REST API (bc3-api): POST /attachments.json uploads a file, then an upload is created under a project vault; the free plan has 1 project
- composes with: not recorded
- reliability: free plan: 1 GB of file storage; additional storage is not available on the free plan
- notes: 1 GB of file storage, 1 project and 3 users on the free plan; public sharing links and additional storage are not available on the free plan
- evidence note: Re-read on 2026-11-03 from vendor pages: https://5.basecamp-help.com/article/1144-basecamp-for-free (1 GB of file storage; additional storage not available; permanent free plan, no credit card), https://basecamp.com/pricing (Pro Unlimited 1000 GB at $199/mo billed annually), https://github.com/basecamp/bc3-api/blob/master/sections/attachments.md and https://github.com/basecamp/bc3-api/blob/master/sections/uploads.md (upload endpoints). Every field that decides the verdict cites a vendor capture.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB of file storage, 1 project, 3 users; 'Public sharing links' and 'additional storage' explicitly not available on the free plan. No API for files.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 1 GB of file storage, 1 project, 3 users; 'Public sharing links' and 'additional storage' explicitly not available on the free plan. No API for files.
  - [1] 2026-11-03: the free plan includes 1 GB of file storage | capture: sha256:0c0b296a317e55449febda1952ab5c4bac62d9cf11ef5b28bae1a57c8e311417 | quote: - 1 GB of file storage
  - [2] 2026-11-03: the largest paid plan holds 1000 GB (1 TB) at $199/mo billed annually | capture: sha256:b4d7afa69c7ce46861d87fcfce38b963670825bc9461c2a6613b7d12312a8640 | quote: | Pro Unlimited $199/mo, billed annually | UNLIMITED projects 1000 GB (1 TB) storage UNLIMITED users
  - [1] 2026-11-03: additional storage is not available on the free plan | capture: sha256:0c0b296a317e55449febda1952ab5c4bac62d9cf11ef5b28bae1a57c8e311417 | quote: - Account upgrades (Admin Pro Pack, Timesheet, additional storage)
  - [3] 2026-11-03: the vendor API documents a file upload endpoint | capture: sha256:48edd39e54938670dc3087a7f0d543aeb35bc9019ab24de70e36aebc4b287de2 | quote: `POST /attachments.json` uploads a file.
  - [4] 2026-11-03: the vendor API documents creating an upload in a vault | capture: sha256:38127287a57d95c4908552f79292fcbc67cdfeb7355d4dc6abc07a7882aa7e5e | quote: `POST /vaults/2/uploads.json` creates an upload under the vault with an ID of `2`.
  - [1] 2026-11-03: the free plan is permanent and asks for no credit card | capture: sha256:0c0b296a317e55449febda1952ab5c4bac62d9cf11ef5b28bae1a57c8e311417 | quote: Basecamp for Free is a permanent free plan — no trial period, no credit card required.
- sources:
  - [1] https://5.basecamp-help.com/article/1144-basecamp-for-free
  - [2] https://basecamp.com/pricing
  - [3] https://github.com/basecamp/bc3-api/blob/master/sections/attachments.md
  - [4] https://github.com/basecamp/bc3-api/blob/master/sections/uploads.md
