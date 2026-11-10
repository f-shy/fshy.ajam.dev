# Anthropic

> claude.com | Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/claude/ | JSON https://fshy.ajam.dev/api/v1/entity/claude.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Claude Managed Agents

- `compute/claude-managed-agents` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:34.000Z (live) | stale on 2026-11-22
- url https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing
- free tier: no compute tier: the product is priced per million tokens with postpaid billing only and no prepaid credits; there is no machine and no free compute allowance | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: per million input and output tokens, from $2 to $10 an input MTok on the current models [1]
  - write-gated (binding): postpaid in arrears only, with no prepaid credits, so a balance cannot be topped up in advance [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and carries the per-model token ladder and the postpaid-only payment model. There is no compute product here, so the record's free-tier framing does not apply
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a managed agent runs turns against tokens; there is no machine and no session clock
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the Claude Platform pricing page was read on 2026-10-22 and is a per-million-token model ladder with prompt-caching rates: 'Claude Opus 5.5 $4 / MTok, $5 / MTok, $8 / MTok' and 'Claude Sonnet 5.5 $2 / MTok', with 'Arrears only (postpaid); no prepaid credits'. It prices tokens, not machines
- sources:
  - [1] https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing

## Anthropic AI

- `compute/anthropic-ai` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:49.063Z (live) | stale on 2026-12-04
- url https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program
- free tier: 'If successful, we will apply up to $20,000 in API credits to your account for a 6-month period.' Eligibility, quoted: 'This program provides free API credits for our standard model suite to researchers in academia and nonprofit organizations working on scientific research topics we consider high priority', and the FAQ adds 'designed for researchers attached to research institutions'. Applications are evaluated 'on the first Monday of each month'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): credit is restricted to researchers attached to a research institution or nonprofit, so an unaffiliated applicant has no qualifying category however strong the proposal. [1]
- limits note: credit is restricted to researchers attached to a research institution or nonprofit, so an unaffiliated applicant has no qualifying category however strong the proposal.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The credit is API spend, not compute, so it composes with nothing in the compute class. It also cannot be topped up in place: the program takes a new application rather than an increase, and the credits are for API use only, not the web app.
- reliability: no reliability event recorded
- notes: Inference rather than compute, recorded here because it is the same door: USD 20,000 with a named institution attached. The adjacent Anthropic route for an individual is a Claude team plan for scientists, which the vendor's own announcement restricts to 'a principal investigator ... or nonprofit research institution', so both Anthropic lanes close on the same condition. The distinction to keep on promotion: the API is open to anyone with a Console account, so the product is reachable and only the grant is gated.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: 'up to $20,000 in API credits to your account for a 6-month period', 'for our standard model suite to researchers in academia and nonprofit organizations', 'designed for researchers attached to research institutions', 'We evaluate submissions on the first Monday of each month', quoted; page 200
  - [1] 2026-11-03: the award is up to USD 20,000 of API credit for 6 months; the page lists no GPU | capture: sha256:727731655333ae72832c2e287101b05d8153d070ba3ae52f7d3736bbeef865ef | quote: If successful, we will apply up to $20,000 in API credits to your account for a 6-month period.
- sources:
  - [1] https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program

## Anthropic Claude Files API

- `storage/anthropic-claude-files-api` | fails-egress | evidence reported | binding per-object-cap | category LLM provider /v1/files
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://platform.claude.com/docs/en/build-with-claude/files
- free tier: 1 TB per organization; 500 MB per file; files persist until deleted or until expires_at | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB per file | bytes: 500000000 | source: [1] | note: not stated
- retention: 1 TB per organization; 500 MB per file; files persist until deleted or until expires_at | per-object-cap 500 MB | source: [1] | note: not stated
- egress: No egress fee documented. | metered: no
- identity: any-phone | detail: any-phone
- interface: rest, cli
- limits:
  - per-object-cap (binding): 500 MB per file [1]
- limits note: per-object-cap 500 MB. Files cannot be modified or renamed after upload. Files API request size capped at 500 MB (Messages 32 MB, Batch 256 MB).
- interface detail: REST POST/GET/DELETE /v1/files; GET /v1/files/{file_id}/content; `ant files` CLI; Python/TS/Go/Java/C# SDKs
- tooling: anthropic SDK; curl with x-api-key + anthropic-version headers
- composes with: 1 TB per org, and 'Each organization can have up to 100 workspaces' with files scoped to the workspace. Nominally 100 TB if workspaces were a cheap axis. But see the read gate.
- reliability: HARD READ GATE, stated in the docs not in a forum. Uploading is therefore write-only data loss. (Anthropic separately requires phone verification for new Console accounts.)
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: 1 TB per organization; 500 MB per file; files persist until deleted or until expires_at
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Maximum file size: 500 MB for each file'; 'Total storage: 1 TB for each organization'; 'Download files that were created by skills or the code execution tool. Files you upload cannot be downloaded.'
  - [1] 2026-10-21: 'Each organization can have up to 100 workspaces'; 'Files are scoped to the workspace they were uploaded in'
  - [2] 2026-10-21: consumer side is much smaller: 'Project files — File size: 30MB per file'
  - [3] 2026-10-21: PROBE: curl -D - -> HTTP 404 with a JSON error body, Cloudflare-fronted; endpoint does not answer unauthenticated (not a 0-byte 200)
- sources:
  - [1] https://platform.claude.com/docs/en/build-with-claude/files
  - [2] https://support.claude.com/en/articles/8241126-upload-files-to-claude
  - [3] https://api.anthropic.com/v1/files?beta=true

## claude files api as an archive

- `storage/claude-files-api-as-an-archive` | fails-quota | evidence documented | binding write-gated | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:18.956Z (live) | stale on 2026-12-04
- url https://platform.claude.com/docs/en/build-with-claude/files
- free tier: 1 TB total storage for each organization and 500 MB for each file; Files API operations are free. Files that are uploaded cannot be downloaded (write-only): only files created by skills or the code execution tool can be downloaded. The 1 TB limit is for each organization, so its workspaces add no space. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB for each file | bytes: 500000000 | source: [1] | note: not applicable
- retention: Files persist until deleted with DELETE /v1/files/{file_id} or until their expires_at, which is optional and set at upload between 1 hour and 90 days. | source: [1]
- egress: Files that are uploaded cannot be downloaded: downloading an uploaded file returns a 400 error, and only files created by skills or the code execution tool can be downloaded. Files API operations are free. | metered: no
- identity: email
- interface: rest
- limits:
  - volume-quota: 1 TB total storage for each organization [1]
  - per-object-cap: 500 MB for each file [1]
  - write-gated (binding): files that are uploaded cannot be downloaded [1]
  - request-rate: approximately 500 requests per minute for file-related API calls [1]
- limits note: 1 TB of storage for each organization, 500 MB for each file, uploads that cannot be downloaded, and approximately 500 file-related requests per minute.
- binding note: uploaded files cannot be downloaded, so the 1 TB organization quota cannot be read back; workspaces do not add space because the quota is for each organization
- interface detail: REST endpoints under /v1/files: upload, list, retrieve metadata, delete; content download only for files generated by skills or the code execution tool
- tooling: Files API of the Claude API through its SDKs and the ant CLI; file-related API calls are limited to approximately 500 requests per minute.
- composes with: not recorded
- reliability: 1 TB for each organization and 500 MB for each file are documented limits, and uploaded files cannot be downloaded (write-only). The 1 TB limit is for each organization, so extra workspaces add no space.
- notes: the same as reliability
- evidence note: the verdict rests on the vendor Files API documentation, read on 2026-11-03: it quotes 1 TB total storage for each organization, 500 MB for each file, that uploaded files cannot be downloaded, approximately 500 file-related requests per minute and free Files API operations
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB for each organization and 500 MB for each file are documented limits, and uploaded files cannot be downloaded (write-only). The 1 TB limit is for each organization, so extra workspaces add no space.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 1 TB/org quota is real and per-file 500 MB is real, but uploaded files are explicitly non-downloadable — write-only. 100 workspaces x 1 TB would be 100 TB of nominal space and zero bytes…
  - [1] 2026-11-03: the Files API total storage is 1 TB for each organization | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Total storage: 1 TB for each organization
  - [1] 2026-11-03: the maximum file size is 500 MB for each file | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Maximum file size: 500 MB for each file
  - [1] 2026-11-03: the maximum file size is 500 MB | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Maximum file size: 500 MB for each file
  - [1] 2026-11-03: files persist until deleted or expired | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Files persist until you delete them with the `DELETE /v1/files/{file_id}` endpoint or they reach their `expires_at`.
  - [1] 2026-11-03: uploaded files cannot be downloaded | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Files you upload cannot be downloaded.
  - [1] 2026-11-03: the Files API is a REST interface under /v1/files | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Downloading its content (`GET /v1/files/{file_id}/content`) returns a 404 error.
  - [1] 2026-11-03: the content endpoint is GET /v1/files/{file_id}/content | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Downloading its content (`GET /v1/files/{file_id}/content`) returns a 404 error.
  - [1] 2026-11-03: file-related calls are limited to approximately 500 requests per minute | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: File-related API calls are limited to approximately 500 requests per minute.
  - [1] 2026-11-03: the organization quota is 1 TB | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Total storage: 1 TB for each organization
  - [1] 2026-11-03: 500 MB for each file | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Maximum file size: 500 MB for each file
  - [1] 2026-11-03: files that are uploaded cannot be downloaded | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Files you upload cannot be downloaded.
  - [1] 2026-11-03: file-related API calls are limited to approximately 500 requests per minute | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: File-related API calls are limited to approximately 500 requests per minute.
  - [1] 2026-11-03: Files API operations are free | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Files API operations are free:
  - [1] 2026-11-03: each organization can have up to 100 workspaces, and the 1 TB quota is for each organization | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Each organization can have up to 100 workspaces
  - [1] 2026-11-03: the storage limit is 1 TB for each organization | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Total storage: 1 TB for each organization
  - [1] 2026-11-03: the quota is 1 TB for each organization | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Total storage: 1 TB for each organization
  - [1] 2026-11-03: the documented organization quota is unchanged at 1 TB | capture: sha256:d76d63653e04a49e68fbc74aa312c7d02de3e8e889e72358aa372127f6c10bdf | quote: Total storage: 1 TB for each organization
- sources:
  - [1] https://platform.claude.com/docs/en/build-with-claude/files
