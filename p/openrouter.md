# OpenRouter

> openrouter.ai | Compute, Inference, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/openrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenRouter

- `compute/openrouter` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-28T09:47:56.236Z (live) | stale on 2026-11-28
- url https://openrouter.ai/docs/api-reference/limits
- free tier: Free-model requests (model ids ending in:free) are capped by a table keyed on credits purchased all time, not on account age: 'Less than 10' credits gives 20 requests a minute and 50 requests a day; 'At least 10' credits gives 20 a minute and 1,000 a day. So the allowance with no credits purchased is 50 requests a day, and the 1,000-a-day ceiling requires purchasing credits; the page grants it starting one credit below the table threshold and prints that figure as an unrendered template placeholder. The page also notes 'Making additional accounts or API keys will not affect your rate limits, as we govern capacity globally'. | unit: requests | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-daily-request-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an OpenRouter account; the free usage limits table has a row for fewer than 10 credits purchased at 50 requests a day, so no purchase is needed for that allowance. unverified: the sign-up methods and any card or phone step at account creation
- interface: rest
- limits:
  - request-rate (binding): 50 requests a day binds and it is a request count, not a token count: a 1,000-item job takes 20 days on the no-card lane, and the 20 rpm cap means the day's 50 requests are spent in under three minutes of traffic. [1]
- limits note: 50 requests a day binds and it is a request count, not a token count: a 1,000-item job takes 20 days on the no-card lane, and the 20 rpm cap means the day's 50 requests are spent in under three minutes of traffic.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the fallback array is where this silently becomes a paid lane: a pipeline that lists a paid model as fallback bills for every request the free model refuses, which is why the free router (openrouter/free) is the only safe chain.
- reliability: no reliability event recorded
- notes: The 1,000-requests-a-day figure is not the free tier; it is the post-purchase tier. The no-card ceiling is 50 a day, which is 1,500 a month and is a chat allowance. inference/openrouter-free-ids holds the endpoint and the 401 on an unauthenticated call.
- extras:
  - facets.class: capacity-shape
  - facets.free_tier_kind: recurring-daily-request-allowance
- evidence:
  - [1] 2026-10-22: free usage limits table: 'Less than 10 | 20 | 50' and 'At least 10 | 20 | 1000' for requests per minute and per day, quoted
  - [2] 2026-10-22: 'If you have purchased at least 10 credits, your free model rate limit will be 1000 requests per day. Otherwise, you will be rate limited to 50 free model API requests per day', quoted
  - [3] 2026-10-22: 'If you list a :free model in a models fallback array, OpenRouter tries the next model in the array when the free model is rate-limited... a fallback to a paid model incurs charges even though the first model was :free', quoted
  - [1] 2026-10-28: with fewer than 10 credits purchased all time, free model requests are limited to 20 per minute and 50 per day; the next row, at least 10 credits, reads 20 and 1000 | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Less than 10 | 20 | 50 |
  - [2] 2026-10-28: the FAQ states 1000 free-model requests per day from 10 credits purchased and 50 otherwise | capture: sha256:0a50cc51d3c7f3120263cab64d196d569ad37c8b5e080661b5c80a6441d24f3e | quote: > If you have purchased at least 10 credits, your free model rate limit will be 1000 requests per day.
- sources:
  - [1] https://openrouter.ai/docs/api-reference/limits
  - [2] https://openrouter.ai/docs/faq
  - [3] https://openrouter.ai/docs/guides/routing/model-variants/free

## OpenRouter :free model ids

- `inference/openrouter-free-ids` | qualifies-with-caveat | evidence documented | binding request-rate | category inference endpoint, keyed
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-31T00:12:42.989Z (live) | stale on 2026-12-01
- url https://openrouter.ai/api/v1
- free tier: free-model request caps for model IDs ending in :free, selected by all-time credits purchased: 20 requests per minute with 50 requests per day below 10 credits, and 20 requests per minute with 1000 requests per day from 10 credits | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: GET /api/v1/key reports the daily counter as free_model_daily_requests with a limit field; the per-minute limit is not reported there. The higher daily ceiling is granted starting one credit below the table's threshold of 10 credits; the page prints that figure as an unrendered template placeholder
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and an API key. The sign-up form asks for an email address and a password, with first and last name optional; an unauthenticated API call is refused with 'No cookie auth credentials found'. The lower free-model tier needs no credit purchase. unverified: any phone or card step after the form, which is behind a sign-up
- interface: rest
- limits:
  - request-rate (binding): free model ids (ending in :free), by credits purchased all time: fewer than 10 credits, 20 requests per minute and 50 requests per day; at least 10 credits, 20 requests per minute and 1000 requests per day. The daily window is the UTC day, the 50 a day is a total across free models, and extra accounts or API keys do not change the caps because capacity is governed globally [1]
- binding note: the :free allowance is stated only as requests per minute and requests per day, with the daily tier selected by all-time credits purchased
- endpoint: https://openrouter.ai/api/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: pairs with an agent after a key; the scarce link is the key plus the ':free' suffix, because a zero-priced id without the suffix is a different quota class
- reliability: no reliability event recorded; an unauthenticated GET /api/v1/key answered HTTP 401 with 'No cookie auth credentials found', so the API answers and gates on a key; enforcement of the free-model caps is not measured
- notes: The free-model caps are stated for model ids ending in :free, and the paid variant of a model has no platform-level request cap. The 50 requests a day below 10 credits purchased is a total across all free models, not a per-model figure.
- evidence note: the gating rule, the per-minute and per-day caps and the response fields are quoted from the vendor page; enforcement of the caps is not measured, and a key would move this to measured in one call
- evidence:
  - [1] 2026-10-22: free-model limits apply only to IDs ending in :free; the tier is selected by all-time credits purchased; GET /api/v1/key reports free_model_daily_requests with a limit field; the per-minute cap is not reported there
  - probe:https://openrouter.ai/api/v1/chat/completions 2026-10-22: inclusionai/ling-3.1-flash without a key returned 401 'No cookie auth credentials found' in both runs, which proves the endpoint exists and gates on a key
  - [1] 2026-10-28: the free usage limits table gives 20 requests per minute and 50 requests per day under 10 credits, 20 requests per minute and 1000 requests per day from 10 credits | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Less than 10 | 20 | 50 | | At least 10 | 20 | 1000 |
  - [1] 2026-10-28: the free-model daily counter is a UTC day | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: Free-model requests recorded so far in the current UTC day
  - [1] 2026-10-28: extra accounts or keys do not change the rate limits | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: Making additional accounts or API keys will not affect your rate limits, as we govern capacity globally.
  - [2] 2026-10-28: the FAQ gives the same 50 requests a day total and 1000 requests a day from 10 credits | capture: sha256:0a50cc51d3c7f3120263cab64d196d569ad37c8b5e080661b5c80a6441d24f3e | quote: These models have low rate limits (50 requests per day total) and are usually not suitable for production use. If you have purchased at least 10 credits, the free models will be limited to 1000 requests per day.
  - [1] 2026-10-28: the free usage limits table gives these caps by credits purchased | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Less than 10 | 20 | 50 | | At least 10 | 20 | 1000 |
  - [1] 2026-10-28: the per-minute limit is not reported by the key endpoint and the tier is selected by all-time credits purchased | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: The per-minute limit is not reported there. The `limit` tier is selected by all-time credits purchased, independently of `is_free_tier`.
  - [1] 2026-10-28: the caps are printed on the vendor page | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Less than 10 | 20 | 50 | | At least 10 | 20 | 1000 |
  - [2] 2026-10-28: an account that has purchased nothing is limited to 50 free-model requests a day, so a purchase is not required for the lower tier | capture: sha256:0a50cc51d3c7f3120263cab64d196d569ad37c8b5e080661b5c80a6441d24f3e | quote: If you have purchased at least 10 credits, your free model rate limit will be 1000 requests per day. Otherwise, you will be rate limited to 50 free model API requests per day.
  - [1] 2026-10-28: the free-model limits apply to ids ending in :free | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: If you're using a free model variant (with an ID ending in `:free`), the following limits apply:
  - [1] 2026-10-30: the free usage limits table still gives 20 requests per minute and 50 per day below 10 credits purchased, and 20 per minute and 1000 per day from 10 credits | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Less than 10 | 20 | 50 | | At least 10 | 20 | 1000 |
  - [1] 2026-10-30: the table's columns are all-time credits purchased, requests per minute and requests per day | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: | Credits purchased (all time) | Requests per minute | Requests per day |
  - [1] 2026-10-30: the free-model caps apply to model ids ending in :free | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: If you're using a free model variant (with an ID ending in `:free`), the following limits apply:
  - [2] 2026-10-30: an account with no credits purchased gets 50 free-model requests a day, so the lower tier needs no purchase; 10 credits raise it to 1000 | capture: sha256:c371f9c1c645f0907af3e5716fb37b5a76ebeb06100fdfd42680e85e684290f3 | quote: If you have purchased at least 10 credits, your free model rate limit will be 1000 requests per day. Otherwise, you will be rate limited to 50 free model API requests per day.
  - [2] 2026-10-30: the 50 a day is a total across free models, and 10 credits purchased raise it to 1000 a day | capture: sha256:c371f9c1c645f0907af3e5716fb37b5a76ebeb06100fdfd42680e85e684290f3 | quote: These models have low rate limits (50 requests per day total) and are usually not suitable for production use. If you have purchased at least 10 credits, the free models will be limited to 1000 requests per day.
  - [1] 2026-10-30: the free-model daily counter runs over the UTC day | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: Free-model requests recorded so far in the current UTC day
  - [1] 2026-10-30: extra accounts or API keys do not change the rate limits | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: Making additional accounts or API keys will not affect your rate limits, as we govern capacity globally.
  - [1] 2026-10-30: GET /api/v1/key reports the free-model daily counter and ceiling as free_model_daily_requests | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: The `free_model_daily_requests` field in the `GET /api/v1/key` response above reports the daily counter and ceiling that gate your free-model requests when these limits apply to your account.
  - [1] 2026-10-30: the per-minute cap is not reported by the key endpoint, and the daily tier is selected by all-time credits purchased | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: The per-minute limit is not reported there. The `limit` tier is selected by all-time credits purchased, independently of `is_free_tier`.
  - [1] 2026-10-30: the higher daily ceiling starts one credit below the table's threshold, and the page prints that figure as an unrendered template placeholder | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: To absorb rounding and top-up fees, the higher daily ceiling is granted starting one credit below the table's threshold (currently {FREE_MODEL_CREDITS_THRESHOLD - 1} credits)
  - [3] 2026-10-30: the sign-up form asks for an email address and a password, with first and last name marked optional | capture: sha256:76618d177e8e07e99ce88bd6e910213e33183f31238f8f9775079c9ae7258615 | quote: Email address
  - [3] 2026-10-30: the first name field of the sign-up form is optional | capture: sha256:76618d177e8e07e99ce88bd6e910213e33183f31238f8f9775079c9ae7258615 | quote: First nameOptional
  - probe:https://openrouter.ai/api/v1/key 2026-10-30: GET /api/v1/key without a key answered HTTP 401 'No cookie auth credentials found', so the API is up and requires a key | capture: sha256:36c1407c049a212826f183eabdf3eae02172f79f80806f9afed93f5eeb68c49c | quote: "message":"No cookie auth credentials found","code":401
  - [1] 2026-10-30: 10 credits purchased raise the free-variant daily limit, and the paid variant of a model has no platform-level request cap | capture: sha256:ae62b6aff14b2b0586d0e4c0222657e6660c5f0acaf435988f65639628b03ed3 | quote: On free variants**, purchase at least 10 credits to raise your daily limit, or switch to the paid variant of the model, which has no platform-level request cap.
- sources:
  - [1] https://openrouter.ai/docs/api-reference/limits
  - [2] https://openrouter.ai/docs/faq
  - [3] https://openrouter.ai/sign-up

## OpenRouter Files API (workspace files)

- `storage/openrouter-files-api` | fails-egress | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://openrouter.ai
- free tier: 10 GiB per workspace, stated verbatim: 'Each workspace can store up to 10 GiB in total. When the workspace is full, uploads return a 403 error.' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 100 MiB | bytes: 104857600 | source: [1] | note: not stated
- retention: Keep your own copy of every file you upload.' Only model-created/promoted files are downloadable. Retention: indefinite. | source: [1] | note: not stated
- egress: Files API has 'no separate charge' and files 'do not expire'. But read-gated by design. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 100 MiB [1]
- limits note: Per-object-cap 100 MiB ('A larger file returns a 413 error'); 10 GiB per workspace; content-type sniffed from bytes and restricted to PDF/PNG/JPEG/GIF/WebP/DOCX/XLSX/PPTX/MP3/WAV/FLAC/OGG/UTF-8 text. Arbitrary binaries are rejected at upload. Upload-open / read-gated: 'A request to GET /api/v1/files/{file_id}/content for an uploaded file returns a 400 error. Keep your own copy of every file you upload.' Only model-created/promoted files are downloadable. Retention: indefinite.
- interface detail: rest
- tooling: POST /api/v1/files (multipart), GET /api/v1/files, GET /api/v1/files/{id}/content. Global endpoint only (eu./us. return 403).
- composes with: 10 GiB x unlimited workspaces is arithmetically a chain, but uploaded bytes cannot be downloaded again, so it is a write-only sink, not storage.
- reliability: Beta; in-region endpoints return 403. Downloaded files must be created by a sandbox/model, not uploaded by you.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GiB per workspace, stated verbatim: 'Each workspace can store up to 10 GiB in total. When the workspace is full, uploads return a 403 error.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The maximum file size is 100 MiB ... 413'; 'Each workspace can store up to 10 GiB in total'; 'Files that you upload cannot be downloaded directly'
  - [2] 2026-10-21: 'Maximum file size: 100 MB; empty files are rejected ... must be a PDF, a PNG/JPEG/GIF/WebP image, a DOCX/XLSX/PPTX, an MP3/WAV/FLAC/OGG, or UTF-8 text'
- sources:
  - [1] https://openrouter.ai/docs/guides/features/files-api
  - [2] https://openrouter.ai/docs/api/api-reference/files/upload-a-file
