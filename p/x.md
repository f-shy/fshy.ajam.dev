# xAI Grok

> x.ai | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/x/ | JSON https://fshy.ajam.dev/api/v1/entity/x.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xAI Files API (Grok) + public CDN URLs

- `storage/xai-files-api-public-cdn-urls` | qualifies-with-caveat | evidence reported | binding per-object-cap | category LLM provider /v1/files with CDN
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.x.ai/developers/files/managing-files
- free tier: No published total-storage quota. Per-file 512 MB (some pages say 50 MB for the upload reference and 50 MiB for public URLs). Files are PERMANENT by default. `expires_after` is opt-in. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file 512 MB | bytes: 512000000 | source: [1] | note: not stated
- retention: Per-file 512 MB (some pages say 50 MB for the upload reference and 50 MiB for public URLs). Files are PERMANENT by default. `expires_after` is opt-in. | source: [1] | note: not stated
- egress: Every file can mint a public URL on files-cdn.x.ai, Cloudflare-fronted, no API key needed to fetch, no egress charge documented. URL is permanent if the file has no expiry and no expires_after is passed. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB/file [1]
- limits note: Per-object-cap 512 MB (50 MB if you want a public URL. Public URLs are limited to images/video mime types). 'A file can have at most one active public URL at a time.' Public-URL creation can fail if the team hits its active-URL quota.
- interface detail: OpenAI-compatible REST at https://api.x.ai/v1/files. POST upload, GET list, GET {id}, GET {id}/content (streams raw bytes, Content-Type application/octet-stream), DELETE, plus POST {id}/public-url and /public-url/revoke.
- tooling: openai-python with base_url swapped to https://api.x.ai/v1; xai_sdk; curl
- composes with: Upload workflow generates public URLs cached at CDN edge locations. Files maintain one active public URL at a time, and repeated requests return the existing public link idempotently.
- reliability: The absence of a published total quota is the finding, not an oversight. A third-party comparison site says outright 'no storage limit is stated. xAI says only that limits may vary slightly by platform or subscription'. Treat unverified. Files persist 'until you delete them'. Collections is a separate product with a 100 MB/file cap and requires credits in the account. Public URLs only cover image/png, image/jpeg, image/gif, image/webp, video/mp4, video/webm. So the CDN path is media-only; arbitrary blobs must go through the authenticated content endpoint.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
- evidence:
  - [2] 2026-10-21: 'Files default to permanent storage until you delete them'; expires_after range 3600–2592000; 'Stream the raw bytes'; 'The endpoint streams the response, so it works for files of any supported size'
  - [3] 2026-10-21: 'Every file you upload through the Files API lives in private storage by default … Public URLs turn a stored file into a permanent, shareable link on the SpaceXSI CDN that anyone can open — no API key required'; 'File has no expiration, expires_after omitted — URL never expires'; limitations: max 50 MiB, restricted content types
  - [1] 2026-10-21: 'File size: Maximum 512 MB per file'
  - [4] 2026-10-21: 'GET /v1/files/{file_id}/content … Content-Type application/octet-stream'
  - [5] 2026-10-21: 'Maximum file size: 100MB'; 'you must have credits in your account'
  - [6] 2026-10-21: 'no storage limit is stated' for xAI
  - [7] 2026-10-21: PROBE: curl -D - -> 401, Content-Length 35, body {"code":"unauthenticated:no-credentials"}; /v1/files/abc/content -> 401/35; /v1/collections -> 401/77; https://files-cdn.x.ai/test/file_abc.png -> 404 from Cloudflare (host live, CF-fronted)
- sources:
  - [1] https://docs.x.ai/developers/files
  - [2] https://docs.x.ai/developers/files/managing-files
  - [3] https://docs.x.ai/developers/files/public-urls
  - [4] https://docs.x.ai/developers/rest-api-reference/files/download
  - [5] https://docs.x.ai/developers/files/collections
  - [6] https://felloai.com/ai-file-upload-limits/
  - [7] https://api.x.ai/v1/files

## xAI Grok API

- `compute/xai-grok-api` | paid-only | evidence inferred | binding volume-quota | category inference API
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.x.ai/docs/models
- free tier: no free API credit is documented today. The rate card reads 'grok-4.7 $2.00' in and '$6.00' out per million tokens, and the only free thing the site offers is the Playground: 'Try Grok free in the Playground'. The USD 150 a month data-sharing credit that every credit list carries is not on the current documentation index. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: no free credit is documented, so a funded balance is needed before the first call, and the record does not say which rail funds it: the landing page's three steps are sign up, create a key, call, with no credit mentioned, and the card cost is inferred from the paid-only verdict rather than read as a signup requirement. No hold, debit or prepaid answer appears, and whether signup asks for an email or a phone is not stated. The old data-sharing credit required the team to have "already spent a minimum of $5 on the API" before opting in, if that programme still exists
- interface: rest
- limits:
  - volume-quota (binding): there is no allowance to exhaust: a prepaid balance or a card is required before the first call, and the rate table is the only limit. [1]
- limits note: there is no allowance to exhaust: a prepaid balance or a card is required before the first call, and the rate table is the only limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: if the data-sharing credit returns, it is the largest recurring inference allowance among documented hosts: USD 150 a month / USD 2.00 per million input tokens = 75 million grok-4.7 input tokens a month, or 25 million output tokens at USD 6.00.
- reliability: no reliability event recorded
- notes: This is the most-repeated number in this category and the evidence is in conflict, so the rung is inferred from three observations: the live docs index has no free-credit page, the API landing page offers only the Playground, and a 2026 write-up states the programme is gone. Against that, a documentation mirror still carries the full text of the programme. If it is live, the gate is worse than it looks: the team must spend USD 5 before opting in, opting in cannot be reversed, and teams in the United Kingdom and most of the European Union are excluded by country. Unverified: one USD 5 prepayment and a look at the Credits section of console.x.ai. Scope note: documented records already holds storage/xai-files-api-public-cdn-urls, which covers xAI file storage and public CDN URLs; it says nothing about inference credit, and this record does not touch storage.
- extras:
  - facets.class: withdrawn-credit
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: the text rate table: 'grok-4.7 (< 200k prompt tokens) | 500k | $2.00 | $0.50 | $6.00' in, cached, out per 1M tokens, quoted
  - [2] 2026-10-22: the documentation index carries no free-credits page: the only billing entries are 'Management API - Billing Management' and 'Extra usage credits and top-ups', observed by reading the index
  - [3] 2026-10-22: 'grok-4.7 from $2/M tokens, plus image, video, and voice APIs. Try Grok free in the Playground'; the page's three steps are sign up, create a key, call, with no credit mentioned, quoted
  - [4] 2026-10-22: a mirror of the old docs page: 'Get $150 in free API credits each month ... for teams that opt in to data sharing', and 'your team must have already spent a minimum of $5 on the API before choosing to opt in', quoted
  - [5] 2026-10-22: 'The Grok xAI API does not give new accounts free credits ... Claims of $150 a month in credits for sharing request data describe a program that no current xAI billing page documents', reported
- sources:
  - [1] https://docs.x.ai/docs/models
  - [2] https://docs.x.ai/llms.txt
  - [3] https://x.ai/api
  - [4] https://grok-api.apidog.io/free-credits-934025m0
  - [5] https://walterpinem.com/grok-xai-api/
