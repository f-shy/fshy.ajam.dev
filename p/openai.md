# OpenAI

> openai.com | Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openai/ | JSON https://fshy.ajam.dev/api/v1/entity/openai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenAI Codex

- `compute/openai-codex` | qualifies-with-caveat | evidence documented | binding write-gated | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:27:57.615Z (live) | stale on 2026-12-05
- url https://developers.openai.com/codex/codex-for-oss
- free tier: 'Open-source maintainers can apply for API credits, six months of ChatGPT Pro with Codex, and Codex Security', and 'Over the past year, the Codex Open Source Fund ($1 million) has supported projects that need API credits'. The form adds 'API credits for coding, maintainer automation, release workflows, and core open source work'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: a time-boxed grant decided by review, not a recurring credit: six months of ChatGPT Pro with Codex for selected maintainers, conditional Codex Security, and API credits whose cash value is not published
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: the application form asks for the email of an existing ChatGPT account, a public GitHub username, a public repository URL, the applicant's role as primary or core maintainer, a reason the repository qualifies, and an OpenAI Organization ID; applications are reviewed on a rolling basis and only selected applicants are notified
- interface: rest
- limits:
  - write-gated (binding): A review decides entry and the maintainer must be a primary or core maintainer of a public repository with a public GitHub profile; the cash value of the API credit is not published. [1]
- limits note: A review decides entry and the maintainer must be a primary or core maintainer of a public repository with a public GitHub profile; the cash value of the API credit is not published.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the only record in this category denominated in inference rather than machines, and it is the cheapest way to run an agent over a repository: six months of a frontier coding subscription plus API credit covers the review loop that the other records would have to pay for in tokens.
- reliability: no reliability event recorded
- notes: The page changed shape within the year: the fund began as USD 1 million of API credits and now leads with a six-month subscription, so the cash-equivalent value is not published and is left null. Codex Security is 'conditional' and reviewed case by case. The gate is maintainership of a project with traction, which is the same bar as every other vendor programme here, but the review is rolling and there is no cohort.
- extras:
  - facets.class: vendor-oss-credits
  - facets.free_tier_kind: recurring-credit
- evidence:
  - [1] 2026-10-22: quoted the USD 1 million fund, the six months of ChatGPT Pro with Codex, the API credits, and 'If you're a core maintainer or run a widely used public project, apply'
  - [2] 2026-10-22: the live application form, which asks for a ChatGPT account email, a public GitHub username, a public repository URL and the applicant's maintainer role, and states reviews run on a rolling basis
  - [1] 2026-10-30: the programme grants six months of ChatGPT Pro with Codex, a fixed term rather than a recurring allowance | capture: sha256:d4540806f21b0b06e48ff5feccc9fc5ec4d427e745a41e8c452b8dca638a0a0d | quote: Six months of ChatGPT Pro with Codex for day-to-day coding, triage, review, and maintainer workflows
  - [2] 2026-10-30: the form requires the email of an existing ChatGPT account, alongside a public GitHub username, a public repository and an OpenAI Organization ID | capture: sha256:d7b7e2a10b0e8d302e9fcb82aaad36c58b6ae175833d03fd116209eed2793137 | quote: Email *Enter the email associated with your ChatGPT account.
  - [1] 2026-10-30: the programme still offers API credits, six months of ChatGPT Pro with Codex and Codex Security; the cash value of the API credits is still not published | capture: sha256:d4540806f21b0b06e48ff5feccc9fc5ec4d427e745a41e8c452b8dca638a0a0d | quote: Open-source maintainers can apply for API credits, six months of ChatGPT Pro with Codex, and Codex Security.
  - [1] 2026-11-03: the programme still offers API credits, six months of ChatGPT Pro with Codex and Codex Security to maintainers who apply | capture: sha256:d4540806f21b0b06e48ff5feccc9fc5ec4d427e745a41e8c452b8dca638a0a0d | quote: Open-source maintainers can apply for API credits, six months of ChatGPT Pro with Codex, and Codex Security.
  - [1] 2026-11-04: the Codex for OSS offer is unchanged: API credits, six months of ChatGPT Pro with Codex, and Codex Security | capture: sha256:d4540806f21b0b06e48ff5feccc9fc5ec4d427e745a41e8c452b8dca638a0a0d | quote: Open-source maintainers can apply for API credits, six months of ChatGPT Pro with Codex, and Codex Security.
- sources:
  - [1] https://developers.openai.com/codex/codex-for-oss
  - [2] https://openai.com/form/codex-for-oss/

## OpenAI Files API — per-project file storage

- `storage/openai-files-api-per-project-file-storage` | qualifies-with-caveat | evidence reported | binding per-object-cap | category LLM provider /v1/files
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.openai.com/api/reference/resources/files/methods/create
- price free (raw file storage); vector-store storage $0.10/GB/day after 1 GB — avoid attaching to vector stores | parsed USD 3000/TB-mo
- free tier: 2.5 TB per project; 512 MB per file; no organization-wide storage cap; orgs may create up to 2,000 projects by default | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 512 MB per file | bytes: 512000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered separately for upload/download of files; retrieval is a plain authenticated GET. No published per-GB transfer fee on the Files API surface. | metered: yes
- identity: any-phone | detail: any-phone
- interface: rest
- limits:
  - per-object-cap (binding): 512 MB per file [1]
- limits note: Per-object-cap 512 MB. Upload rate 1,000 requests/min/authenticated user. Vector-store attachment has its own 2,000 files/min/org limit. `purpose` is the real gate. See reliability_note.
- interface detail: REST `POST/GET/DELETE /v1/files`, `GET /v1/files/{file_id}/content`; OpenAI SDKs; works through OpenAI-compatible gateways
- tooling: openai-python, openai-node, curl; `purpose` field selects the lifecycle class
- composes with: 2,000 projects/org x 2.5 TB = nominally 5 PB per org. Files are project-scoped and cannot be moved between projects, so a pooler must track (project -> file_id). Because `purpose=batch` and `purpose=vision` are both uploadable AND downloadable, they are the only two classes usable as actual storage.
- reliability: READ GATE IS PER-PURPOSE, NOT PER-ACCOUNT. An OpenAI staff-adjacent answer on the developer forum gives the directionality table: assistants up/NO down; user_data up/NO down; fine-tune up/NO down; evals up/NO down; batch up/YES down; vision up/YES down; *_output down only. So `purpose=user_data` and `purpose=assistants` are write-only. Uploading there is data loss. Storage is genuinely free (no per-GB-day charge for raw files; the $0.10/GB-day on the pricing page is vector store storage, not Files API storage). Identity: ChatGPT signup is email-only, but generating the FIRST API key now mandates phone verification (SMS or WhatsApp, one number reusable 3x, rolled out to a listed set of countries). That is the binding constraint here.
- notes: the same as the free tier
- extras:
  - price_verbatim: free (raw file storage); vector-store storage $0.10/GB/day after 1 GB — avoid attaching to vector stores
- evidence:
  - [2] 2026-10-21: 'Individual files can be up to 512 MB, and each project can store up to 2.5 TB of files in total. There is no organization-wide storage limit. Uploads ... rate-limited to 1,000 requests per minute'
  - [1] 2026-10-21: 'OpenAI currently supports a file storage quota of 2.5 TB of files per project', updated 2 days ago
  - [3] 2026-10-21: 'Organizations can create up to 2,000 projects by default'; 'Project resources (such as files, assistants, storage, or threads) are scoped to the project'
  - [4] 2026-10-21: 'Retrieve file content: get /files/{file_id}/content'
  - [5] 2026-10-21: directionality table; 'Not allowed to download files of purpose: user_data'
  - [6] 2026-10-21: 'You can't download files that you've uploaded to the assistants yourself'
  - [7] 2026-10-21: 'File search | Storage | $0.10 / GB per day (1 GB free)' — this is vector-store storage, NOT raw file storage
  - [8] 2026-10-21: 'Phone verification is now mandated on platform.openai.com for generating your initial API key'
  - [9] 2026-10-21: PROBE: curl -D - -> HTTP/1.1 401, Content-Length 616, real JSON error, x-openai-proxy-wasm; /v1/files/{id}/content also 401/616 — endpoint live, not a 0-byte 200
- sources:
  - [1] https://help.openai.com/en/articles/8724843-file-storage-quota-errors-for-api-users
  - [2] https://developers.openai.com/api/reference/resources/files/methods/create
  - [3] https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform
  - [4] https://developers.openai.com/api/reference/resources/files/
  - [5] https://community.openai.com/t/file-uploads-error-why-can-t-i-download-files-with-purpose-user-data/1357013
  - [6] https://community.openai.com/t/not-allowed-to-download-files-of-purpose-assistants/528220
  - [7] https://platform.openai.com/docs/pricing
  - [8] https://help.openai.com/en/articles/8983040-what-does-phone-verification-look-like
  - [9] https://api.openai.com/v1/files

## OpenAI Containers (Code Interpreter / Hosted Shell)

- `compute/openai-containers` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:36.000Z (live) | stale on 2026-11-22
- url https://developers.openai.com/api/docs/pricing
- free tier: no container tier: the API is priced per million tokens and per audio minute, from $0.10 an input MTok on the cheapest current model | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): per million input and output tokens, from $0.10 to $30.00 an input MTok on the current models [1]
  - per-object-cap: audio transcription bills per minute, from $0.0045 to $0.034 [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the API pricing page was read on 2026-10-22 and carries model and audio rates only. There is no container product on it, so the record's free-tier framing does not apply and the verdict moves to paid-only
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: suspends on idle (auto_stop_idle)
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a container is billed per minute while it runs on the container pricing page this record does not cite
  - free_tier_kind: none
  - granularity.min_billed_s: 300
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the API pricing page was read on 2026-10-22 and is a per-million-token model table plus per-minute audio rates: 'gpt-6-luna $0.10 / $0.50 per MTok', 'gpt-5.5-pro $30.00 / $180.00', 'gpt-transcribe $0.0045 / minute'. It prices tokens and minutes, not containers
- sources:
  - [1] https://developers.openai.com/api/docs/pricing

## ChatGPT consumer file storage / Library + Projects

- `storage/chatgpt-consumer-file-storage-library-projects` | fails-quota | evidence reported | binding per-object-cap | category Consumer AI chat product
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://help.openai.com/en/articles/8555545-file-uploads-faq
- free tier: 25 GB shared upload storage per user, 100 GB per organization. 512 MB per file. Project file counts: Free 5, Go/Plus 25, Edu/Pro/Business/Enterprise 40. GPT knowledge: 20 files. 'Users can create an unlimited amount of projects.' | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 512 MB per file | bytes: 512000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Files can be previewed and downloaded from the project sources list; no egress fee. | metered: no
- identity: any-phone | detail: any-phone
- interface: unknown
- limits:
  - request-rate: 3 uploads/day [1]
  - per-object-cap (binding): 512 MB per file [1]
  - write-gated: review, download, or delete it') which is the inverse of the API's purpose-based read [1]
- limits note: Per-object-cap 512 MB; CSV/spreadsheets ~50 MB; images 20 MB. Upload rate: 80 files per 3 hours; free users 3 uploads/day. Retention not stated as a limit. Library persists.
- interface detail: Web/app UI. `GET /v1/files` with an API key does NOT expose ChatGPT Library files. The API and the consumer product are separate stores.
- tooling: None programmatic for the consumer store.
- composes with: Unlimited projects x 40 files x 512 MB = nominal 20 GB per project, but the 25 GB/user byte wall across all of it is the real cap. Nothing multiplies.
- reliability: Storage allocation is 25 GB per user as shared upload storage across the entire account without project stacking. Files can be previewed, downloaded, or deleted from project source lists.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 25 GB shared upload storage per user, 100 GB per organization. 512 MB per file. Project file counts: Free 5, Go/Plus 25, Edu/Pro/Business/Enterprise 40. GPT knowledge: 20 files. 'Users can create an unlimited amount of projects.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Shared upload storage is capped at 25 GB per user and 100 GB per organization'; 'You can upload up to 80 files every 3 hours. Free users are limited to 3 file uploads per day.'; project file caps by plan
  - [2] 2026-10-21: 'After a file is added to a project, you can open it from the project sources list to preview, download, or delete it'; 'Users can create an unlimited amount of projects.'
  - [1] 2026-10-21: 'All files uploaded to a GPT or a ChatGPT conversation have a hard limit of 512MB per file'
- sources:
  - [1] https://help.openai.com/en/articles/8555545-file-uploads-faq
  - [2] https://help.openai.com/en/articles/10169521-chatgpt-projects
