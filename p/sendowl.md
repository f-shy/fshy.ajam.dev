# sendowl

> sendowl.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sendowl/ | JSON https://fshy.ajam.dev/api/v1/entity/sendowl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sendowl

- `storage/sendowl` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:23.339Z (live) | stale on 2026-12-04
- url https://help.sendowl.com/help/how-do-i-upload-large-files
- free tier: No free tier; paid plans only. Current plans include unlimited storage and products, a 50 GB max file size and 100 GB bandwidth included with USD 1/GB overage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Paid plans only. Current plans state unlimited storage and products with a 50 GB max file size and 100 GB included bandwidth.
- notes: No per-file limit and SFTP ingest is genuinely good, but storage is ~1 TB before the plan is moved to a custom/enterprise plan, and there is no free tier ($9/mo minimum).
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No per-file limit and SFTP ingest is genuinely good, but storage is ~1 TB before the plan is moved to a custom/enterprise plan, and there is no free tier ($9/mo minimum).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No per-file limit and SFTP ingest is genuinely good, but storage is ~1 TB before the plan is moved to a custom/enterprise plan, and there is no free tier ($9/mo minimum).
  - [2] 2026-10-21: cited as the basis of the rejection: No per-file limit and SFTP ingest is genuinely good, but storage is ~1 TB before the plan is moved to a custom/enterprise plan, and there is no free tier ($9/mo minimum).
  - [2] 2026-11-19: the current business pricing page states unlimited storage, 50 GB max file size and 100 GB bandwidth with USD 1/GB overage | capture: sha256:8fb4af5c6b7e86e565d4d5fc6b874d8f78e28a6a20c8e19fc83a78f518a03f30 | quote: Unlimited storage & products No caps on what you sell ### 50GB max file size Upload large files with ease ### 100GB bandwidth included Then $1/GB overage
  - [2] 2026-11-19: the current business pricing page states unlimited storage and a 50 GB max file size | capture: sha256:8fb4af5c6b7e86e565d4d5fc6b874d8f78e28a6a20c8e19fc83a78f518a03f30 | quote: Unlimited storage & products No caps on what you sell ### 50GB max file size
  - [2] 2026-11-19: the current paid plans carry no free tier and state unlimited storage with a 50 GB file cap | capture: sha256:8fb4af5c6b7e86e565d4d5fc6b874d8f78e28a6a20c8e19fc83a78f518a03f30 | quote: Unlimited storage & products No caps on what you sell ### 50GB max file size Upload large files with ease ### 100GB bandwidth included Then $1/GB overage
  - [1] 2026-11-19: the help page confirms no per-file size limit on current plans, with SFTP as the ingest route for large files | capture: sha256:c9fab683dd3b1428d2dd9837d9ffe132f4136ac26e269098e0578c0f177f9c75 | quote: On current SendOwl plans there's no limit on the size of the files you sell.
- sources:
  - [1] https://help.sendowl.com/help/how-do-i-upload-large-files
  - [2] https://www.sendowl.com/business-pricing
