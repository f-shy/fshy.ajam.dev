# Voyage AI

> voyageai.com | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/voyageai/ | JSON https://fshy.ajam.dev/api/v1/entity/voyageai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Voyage AI (Compute)

- `compute/voyage-ai` | trial-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.voyageai.com/docs/pricing
- free tier: The first 200 million tokens for voyage-4-large, voyage-4, voyage-4-lite, voyage-context-4 and voyage-code-4, and the first 50 million tokens for voyage-multilingual-2, voyage-finance-2, voyage-law-2 and voyage-code-2, are free for every account. For the multimodal endpoint the first 200 million text tokens and 150 billion pixels for voyage-multimodal-3.5 and voyage-multimodal-3 are free for every account. | unit: tokens | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): the 200 million tokens is a lifetime allowance per account and not a monthly one, so an index built once against it cannot be rebuilt or extended at the same price; a re-embed after a model change consumes the remainder immediately. [1]
- limits note: the 200 million tokens is a lifetime allowance per account and not a monthly one, so an index built once against it cannot be rebuilt or extended at the same price; a re-embed after a model change consumes the remainder immediately.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 200 million embedding tokens is enough to embed roughly 100 GiB of English text once, which is a whole RAG corpus, and it pairs with a free Postgres plus pgvector on Neon or Supabase so the vector store costs nothing either; what breaks is any re-index, because the allowance is consumed and does not reset.
- reliability: no reliability event recorded
- notes: Found in amitpandeytiktok/awesome-free-compute-2026 STACK.md, which is a June 2026 snapshot, so the vendor page was read to confirm the figure still holds on 2026-10-22. The docs page answered, so the vendor figure is documented and not inferred.
- extras:
  - facets.class: credit-large-enough-for-real-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'The first 200 million tokens for voyage-4-large, voyage-4, voyage-4-lite, voyage-context-4, and voyage-code-3 ... are free for every account', with 50 million for the -2 models, quoted
  - [1] 2026-10-22: 'The first 200M text tokens and 150B pixels for voyage-multimodal-3.5 and voyage-multimodal-3 are free for every account', quoted; after that USD 0.12 per million tokens and USD 0.60 per billion pixels
- sources:
  - [1] https://docs.voyageai.com/docs/pricing

## Voyage AI (Inference)

- `inference/voyage-ai` | trial-only | evidence documented | binding volume-quota | category embedding and reranker API, lifetime free token allowance
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-03T09:59:10.910Z (live) | stale on 2026-12-04
- url https://docs.voyageai.com/docs/pricing
- free tier: The first 200 million tokens for voyage-4-large, voyage-4, voyage-4-lite, voyage-context-4 and voyage-code-4, or the first 50 million tokens for voyage-finance-2, voyage-law-2 and voyage-code-2, are free for every account. The sentence above the embeddings table also names voyage-code-3 and voyage-multilingual-2, which the tables list as older models with no free tokens. The first 200M text tokens and 150B pixels for voyage-multimodal-3.5 and voyage-multimodal-3 are free, and the first 200 million tokens for the rerankers rerank-3 and rerank-3-lite are free for each account; the sentence above the reranker table also names rerank-2.5, rerank-2.5-lite, rerank-2 and rerank-2-lite, which the older-models table lists with no free tokens. Older models carry no free tokens and Batch API usage does not draw on them. The page says only 'the first' tokens; whether the allowance resets is unverified. | unit: tokens | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the free-token sentence above the embeddings table names voyage-code-3, voyage-multilingual-2 and, above the reranker table, rerank-2.5, rerank-2.5-lite, rerank-2 and rerank-2-lite, while the tables give the 200 million tokens to voyage-code-4, rerank-3 and rerank-3-lite and list the named models in the older-models table with no free tokens; the tables are read as authoritative. After the free tokens, voyage-4 costs USD 0.06 per million tokens and voyage-4-lite USD 0.02. unverified: whether the allowance is counted per account for the life of the account or resets; the page says only 'the first' tokens
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is enough for an API key ('Upon creating an account, we instantly generate an API key'); the rate-limit page says the free tokens still apply after a payment method is entered and ties usage Tier 1 to adding one; unverified: the signup form fields and whether a card or phone is asked, because the dashboard redirects to a login page that answered HTTP 400 on every route tried
- interface: rest
- limits:
  - volume-quota (binding): 200 million free tokens per account on voyage-4-large, voyage-4, voyage-4-lite, voyage-context-4 and voyage-code-4 and 50 million on voyage-finance-2, voyage-law-2 and voyage-code-2; 200M text tokens and 150B pixels on the multimodal models; 200 million on rerank-3 and rerank-3-lite [1]
  - request-rate: unverified: the rate-limit table lists 2000 RPM and 8M TPM for voyage-4 and voyage-3.5 and 16M TPM for voyage-4-lite, but the usage-tier table ties Tier 1 to a payment method being added, so the limit of an account with no payment method is not stated [2]
- binding note: the free tokens are a finite per-account allowance (200 million on the current models), which is large but not renewable; request limits for an account with no payment method are unverified
- interface detail: REST at https://api.voyageai.com/v1 (embeddings and rerank); official Python package voyageai; a Batch API and a Files API exist but are billed and excluded from the free tokens
- endpoint: https://api.voyageai.com/v1/embeddings
- tooling: official Python package (pip install voyageai) with the VOYAGE_API_KEY environment variable, or raw HTTP from any language
- composes with: 200 million embedding tokens is enough to embed a large text corpus once; pair it with a free Postgres with pgvector or another free vector store so the index costs nothing either. A re-embed after a model change draws the allowance down again, and the allowance does not reset.
- reliability: the free-token sentences above the embeddings and reranker tables of the pricing page name voyage-code-3, voyage-multilingual-2, rerank-2.5, rerank-2.5-lite, rerank-2 and rerank-2-lite, which the older-models table lists with no free tokens; the vendor markets Voyage AI as part of MongoDB
- evidence note: the free-token counts, the exclusion of batch usage and older models, the instant API key and the rate-limit table are quoted from vendor pages; the free account's rate limit and the signup fields are unverified.
- evidence:
  - [1] 2026-11-03: 200 million free tokens on the current embedding models, 50 million on the older domain models, for every account | capture: sha256:0edd42c2be66a948a64eaf6b513c4e5412727c56dc6656c2a32ade235f31abf8 | quote: The first 200 million tokens for `voyage-4-large`, `voyage-4`, `voyage-4-lite`, `voyage-context-4`, and `voyage-code-3`, or the first 50 million tokens for `voyage-multilingual-2`, `voyage-finance-2`, `voyage-law-2`, and `voyage-code-2`, are free for every account.
  - [1] 2026-11-03: the table gives 200 million free tokens for voyage-code-4 | capture: sha256:0edd42c2be66a948a64eaf6b513c4e5412727c56dc6656c2a32ade235f31abf8 | quote: | `voyage-code-4` | $0.00012 | $0.12 | 200 million |
  - [1] 2026-11-03: the multimodal models carry 200M free text tokens and 150B free pixels | capture: sha256:0edd42c2be66a948a64eaf6b513c4e5412727c56dc6656c2a32ade235f31abf8 | quote: The first 200M text tokens and 150B pixels for `voyage-multimodal-3.5` and `voyage-multimodal-3` are free for every account.
  - [1] 2026-11-03: Batch API usage does not draw on the free tokens | capture: sha256:0edd42c2be66a948a64eaf6b513c4e5412727c56dc6656c2a32ade235f31abf8 | quote: Free token credits do not apply to Batch API usage.
  - [1] 2026-11-03: older models carry no free tokens | capture: sha256:0edd42c2be66a948a64eaf6b513c4e5412727c56dc6656c2a32ade235f31abf8 | quote: The following table shows the pricing for older models. Please note that we do not offer free tokens for them.
  - [2] 2026-11-03: voyage-3.5 is limited to 2000 requests and 8M tokens per minute | capture: sha256:8de0b520c8b312b20d47252050146a64348c52260fcb1ccece0ca874614f8230 | quote: For example, the `voyage-3.5` API rate limits are set at 2000 RPM (requests per minute) and 8M TPM (tokens per minute)
  - [2] 2026-11-03: usage Tier 1 is defined as a payment method added | capture: sha256:8de0b520c8b312b20d47252050146a64348c52260fcb1ccece0ca874614f8230 | quote: | 1 | Payment method added. | See table above. |
  - [2] 2026-11-03: the free tokens still apply after a payment method is entered | capture: sha256:8de0b520c8b312b20d47252050146a64348c52260fcb1ccece0ca874614f8230 | quote: Even with a payment method entered, the free tokens (e.g., 200M tokens for Voyage series 3) will still apply.
  - [3] 2026-11-03: an API key is generated at account creation | capture: sha256:e2068eb3473f0e8e58729c63e66c607255a6044b68da589c486eca519d3d91d6 | quote: Upon creating an account, we instantly generate an API key for you.
  - [4] 2026-11-03: the embeddings endpoint is POST https://api.voyageai.com/v1/embeddings | capture: sha256:67f67999c28a90c03d820526d0416ef7c0e3120b6420a15fd714b513c78719a7 | quote: Voyage text embeddings can be accessed by calling the endpoint `POST https://api.voyageai.com/v1/embeddings`.
  - [5] 2026-11-03: the service is presented as Voyage AI by MongoDB | capture: sha256:10b3dbc44fb9482d5fd23c38ec8f21e5c8892f8b93587128c5aaf602565142d3 | quote: Voyage AI by MongoDB
  - probe:dashboard.voyageai.com 2026-11-03: the dashboard signup answers HTTP 400 behind a login redirect, so the signup fields are unread | capture: sha256:d1061e09927757424628e6f144872c301b01a5223c3c9b67bfafac0a75226047 | quote: "status": 400
  - [1] 2026-11-03: the reranker table gives rerank-3 200 million free tokens | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `rerank-3` | $0.00005 | $0.05 | $0.0025 | 200 million |
  - [1] 2026-11-03: the older-models table carries no free tokens | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: The following table shows the pricing for older models. Please note that we do not offer free tokens for them.
  - [1] 2026-11-03: the embeddings table gives voyage-finance-2, voyage-law-2 and voyage-code-2 50 million free tokens | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `voyage-finance-2` `voyage-law-2` `voyage-code-2` | $0.00012 | $0.12 | 50 million |
  - [1] 2026-11-03: the reranker table gives rerank-3-lite 200 million free tokens | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `rerank-3-lite` | $0.00002 | $0.02 | $0.001 | 200 million |
  - [1] 2026-11-03: the embeddings table gives voyage-code-4 200 million free tokens | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `voyage-code-4` | $0.00012 | $0.12 | 200 million |
  - [1] 2026-11-03: voyage-multilingual-2 is in the older-models table with no free-token column | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `voyage-multilingual-2` `voyage-large-2-instruct` `voyage-large-2` | $0.00012 | $0.12 |
  - [1] 2026-11-03: rerank-2 and rerank-2.5 are in the older-models table | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `rerank-1` `rerank-2` `rerank-2.5` | $0.00005 | $0.05 |
  - [1] 2026-11-03: rerank-2-lite and rerank-2.5-lite are in the older-models table | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: | `voyage-3-lite` `rerank-lite-1` `rerank-2-lite` `rerank-2.5-lite` | $0.00002 | $0.02 |
  - [1] 2026-11-03: the prose sentence above the embeddings table names voyage-code-3 and voyage-multilingual-2 | capture: sha256:776c20f3d7f4e26c9d096606507eaf4e1fd439b45af427f8601d9252d73ea4fe | quote: The first 200 million tokens for `voyage-4-large`, `voyage-4`, `voyage-4-lite`, `voyage-context-4`, and `voyage-code-3`, or the first 50 million tokens for `voyage-multilingual-2`, `voyage-finance-2`, `voyage-law-2`, and `voyage-code-2`, are free for every account.
- sources:
  - [1] https://docs.voyageai.com/docs/pricing
  - [2] https://docs.voyageai.com/docs/rate-limits
  - [3] https://docs.voyageai.com/docs/faq
  - [4] https://docs.voyageai.com/docs/embeddings
  - [5] https://www.voyageai.com/
