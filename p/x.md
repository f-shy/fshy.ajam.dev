# xAI

> x.ai | Storage, Inference, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/x/ | JSON https://fshy.ajam.dev/api/v1/entity/x.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xAI Files API (Grok) + public CDN URLs

- `storage/xai-files-api-public-cdn-urls` | qualifies-with-caveat | evidence reported | binding per-object-cap | category LLM provider /v1/files with CDN
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:25.449Z (live) | stale on 2026-12-10
- url https://docs.x.ai/developers/files/managing-files
- free tier: No published total-storage quota. Per-file 512 MB (some pages say 50 MB for the upload reference and 50 MiB for public URLs). Files are PERMANENT by default. `expires_after` is opt-in. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file 512 MB | bytes: 512000000 | source: [1] | note: Maximum file size: 512 MB per file.
- retention: Files default to permanent storage until you delete them. | source: [1] | note: Files default to permanent storage until you delete them.
- egress: Public URLs turn a stored file into a permanent, shareable link on the SpaceXSI CDN that anyone can open — no API key required. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-object-cap (binding): 512 MB/file [1]
- limits note: Per-object-cap 512 MB (50 MB if you want a public URL. Public URLs are limited to images/video mime types). 'A file can have at most one active public URL at a time.' Public-URL creation can fail if the team hits its active-URL quota.
- interface detail: OpenAI-compatible REST at https://api.x.ai/v1/files. POST upload, GET list, GET {id}, GET {id}/content (streams raw bytes, Content-Type application/octet-stream), DELETE, plus POST {id}/public-url and /public-url/revoke.
- tooling: openai-python with base_url swapped to https://api.x.ai/v1; xai_sdk; curl
- composes with: A file can have at most one active public URL at a time; calling create_public_url on a file that already has one returns the existing URL without producing a new one.
- reliability: The absence of a published total quota is the finding, not an oversight. A third-party comparison site says outright 'no storage limit is stated. xAI says only that limits may vary slightly by platform or subscription'. Treat unverified. Files persist 'until you delete them'. Collections is a separate product with a 100 MB/file cap and requires credits in the account. Public URLs only cover image/png, image/jpeg, image/gif, image/webp, video/mp4, video/webm. So the CDN path is media-only; arbitrary blobs must go through the authenticated content endpoint.
- notes: the same as the free tier
- evidence note: the per-file ceiling is quoted from the first-party files page
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
  - [2] 2026-11-10: the managing-files page states permanent storage by default | capture: sha256:a32a2451cb838a3ce7af9f6c9faf5cd51dbf642e1108bd0a74d40e8d432248fb | quote: Files default to permanent storage until you delete them.
  - [1] 2026-11-10: the page states the 512 MB ceiling the basis names | capture: sha256:19da60bcccf156f5bf1e5184c0f9316b6f17de6fbce5a3755485359f6c6dca80 | quote: * File size: Maximum 512 MB per file
  - [2] 2026-11-25: files are stored permanently until deletion | capture: sha256:61a840305e06e7f260e000f47046701ec2baa0047ac9ab00d6aebf315e159e81 | quote: Files default to permanent storage until you delete them.
  - [2] 2026-11-25: the first-party file-size limit is 512 MB per file | capture: sha256:61a840305e06e7f260e000f47046701ec2baa0047ac9ab00d6aebf315e159e81 | quote: * Maximum file size: 512 MB per file
  - [3] 2026-11-25: public URL creation is idempotent with one active URL per file | capture: sha256:5fc70c0bf2b6bec36f592a30f6e91bfb1926a4a7f679aa424e3e60d37be6e20d | quote: A file can have at most one active public URL at a time. Calling `create_public_url` on a file that already has one returns the existing URL without producing a new one — it's safe to call repeatedly.
  - [3] 2026-11-25: public CDN links are shareable without an API key | capture: sha256:5fc70c0bf2b6bec36f592a30f6e91bfb1926a4a7f679aa424e3e60d37be6e20d | quote: Public URLs turn a stored file into a permanent, shareable link on the SpaceXSI CDN that anyone can open — no API key required.
  - [2] 2026-11-25: files are permanent by default | capture: sha256:61a840305e06e7f260e000f47046701ec2baa0047ac9ab00d6aebf315e159e81 | quote: Files default to permanent storage until you delete them.
  - [2] 2026-11-25: the file-size limit is 512 MB per file | capture: sha256:61a840305e06e7f260e000f47046701ec2baa0047ac9ab00d6aebf315e159e81 | quote: * Maximum file size: 512 MB per file
  - [3] 2026-11-25: one active public URL per file, idempotent creation | capture: sha256:5fc70c0bf2b6bec36f592a30f6e91bfb1926a4a7f679aa424e3e60d37be6e20d | quote: A file can have at most one active public URL at a time. Calling `create_public_url` on a file that already has one returns the existing URL without producing a new one — it's safe to call repeatedly.
  - [3] 2026-11-25: CDN links need no API key to fetch | capture: sha256:5fc70c0bf2b6bec36f592a30f6e91bfb1926a4a7f679aa424e3e60d37be6e20d | quote: Public URLs turn a stored file into a permanent, shareable link on the SpaceXSI CDN that anyone can open — no API key required.
- sources:
  - [1] https://docs.x.ai/developers/files
  - [2] https://docs.x.ai/developers/files/managing-files
  - [3] https://docs.x.ai/developers/files/public-urls
  - [4] https://docs.x.ai/developers/rest-api-reference/files/download
  - [5] https://docs.x.ai/developers/files/collections
  - [6] https://felloai.com/ai-file-upload-limits/
  - [7] https://api.x.ai/v1/files

## xAI

- `inference/xai` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.x.ai/docs/models
- free tier: No free text allowance; Grok models are billed per million tokens (e.g. grok-4.7 input USD 2.00, output USD 6.00 per 1M for prompts under 200k). | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key; no card or phone gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): per-token billing; no free tier stated [1]
- endpoint: https://api.x.ai/v1
- tooling: OpenAI-compatible client and the xAI SDK
- composes with: no standing free tier published; usage is charged per token
- reliability: long-context prompts (at or above 200k tokens) are billed at the higher rate for the whole request
- notes: -
- evidence:
  - [1] 2026-11-18: Grok models are priced per million tokens with no free tier | capture: sha256:432d44bab3117b3ff0a2b3a2f7f35e7b6bd4685993b5d7a9167da3d23145d36d | quote: Prices shown per million tokens.
- sources:
  - [1] https://docs.x.ai/docs/models

## xAI Grok API

- `compute/xai-grok-api` | paid-only | evidence inferred | binding volume-quota | category inference API
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:48.800Z (live) | stale on 2026-12-26
- url https://docs.x.ai/docs/models
- free tier: The Grok xAI API does not give new accounts free credits. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
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
  - [5] 2026-11-25: the page states that the API gives new accounts no free credits | capture: sha256:49c3763c1d28ebe53dabd43fab089a13b22d07fa7273fbbf6f9b0d88967e09df | quote: The Grok xAI API does not give new accounts free credits.
  - [5] 2026-11-25: the page still states that the API gives new accounts no free credits | capture: sha256:49c3763c1d28ebe53dabd43fab089a13b22d07fa7273fbbf6f9b0d88967e09df | quote: The Grok xAI API does not give new accounts free credits.
- sources:
  - [1] https://docs.x.ai/docs/models
  - [2] https://docs.x.ai/llms.txt
  - [3] https://x.ai/api
  - [4] https://grok-api.apidog.io/free-credits-934025m0
  - [5] https://walterpinem.com/grok-xai-api/
