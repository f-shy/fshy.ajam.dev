# Mixedbread

> mixedbread.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mixedbread/ | JSON https://fshy.ajam.dev/api/v1/entity/mixedbread.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mixedbread (managed search with reranking)

- `inference/mixedbread-search-starter` | trial-only | evidence documented | binding volume-quota | category managed search store with built-in embedding and rerank, one-time free credit | tier Starter
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://www.mixedbread.com/pricing
- free tier: Starter plan: $5 in one-time credits, no card required; 3 workspace users, 3 stores, 100 queries per minute and 6,000 upload requests per minute. Embeddings and reranking are billed inside Store indexing and search, not as standalone calls: standalone direct embedding and reranking APIs are no longer documented | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the credit is USD and is spent on content tokens indexed, storage, and queries; semantic search is $4 per 1K queries and $7.50 per 1K with reranking
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the pricing page states 'No card required' for Starter; unverified: the sign-up form fields, because the app page answered with a login wall to the page reader
- interface: rest
- limits:
  - volume-quota (binding): $5 of one-time credit; at the listed prices $5 covers about 1,250 plain semantic queries or about 666 with reranking, before any indexing cost [1]
  - request-rate: Starter: 100 queries per minute and 6,000 ingestion requests per minute; operation-class limits 1,200 reads, 600 lists, 360 writes per minute [1]
- binding note: the $5 one-time credit is the binding limit; once spent the plan must move to Scale at $20 a month
- endpoint: https://api.mixedbread.com/v1/stores/search
- tooling: Python and TypeScript SDKs and a REST endpoint at api.mixedbread.com/v1/stores/search; upload files to a store, then search with search_options.rerank
- composes with: a caller that needs raw vectors or a bare rerank call cannot get them here; Jina AI, Pinecone Inference and Cohere trial keys serve that shape
- reliability: the earlier standalone embedding and reranking APIs were withdrawn from the documentation; the open-weight models remain on Hugging Face
- notes: derived: $5 / ($7.50 per 1,000 queries) = about 666 queries with reranking; $5 / ($4 per 1,000 queries) = 1,250 queries without
- evidence note: the plan, credit, no-card statement, limits, prices and the withdrawal of the direct APIs are quoted from vendor pages; the sign-up form was not readable.
- evidence:
  - [1] 2026-11-03: the Starter plan is free, with $5 of one-time credits and no card | capture: sha256:2ab2f4bd584891c9f5a5d861e616cace3d0319b23749436db7296e62e0298c3f | quote: Try Mixedbread with $5 in one-time credits. No card required.
  - [1] 2026-11-03: Starter allows 100 queries per minute | capture: sha256:2ab2f4bd584891c9f5a5d861e616cace3d0319b23749436db7296e62e0298c3f | quote: | Query | 100 req / min | 2,400 req / min | Custom |
  - [1] 2026-11-03: Starter allows 6,000 ingestion requests per minute | capture: sha256:2ab2f4bd584891c9f5a5d861e616cace3d0319b23749436db7296e62e0298c3f | quote: | Ingestion | 6,000 req / min | 12,000 req / min | Custom |
  - [1] 2026-11-03: the $5 credit buys roughly 666 semantic queries with reranking, since each thousand cost $7.50 | capture: sha256:2ab2f4bd584891c9f5a5d861e616cace3d0319b23749436db7296e62e0298c3f | quote: Per thousand queries: $0.10 for grep, $4 for semantic search, or $7.50 for semantic search with reranking.
  - [2] 2026-11-03: the standalone direct embedding and reranking API reference pages were withdrawn | capture: sha256:e1e38524be2ab3d71b5c329bcab847e2151bba3baf0e0b915cad37e7e526c03f | quote: pages are no longer part of the current documentation, but the model artifacts
  - [2] 2026-11-03: reranking is now a step inside Store search, not a separate endpoint | capture: sha256:e1e38524be2ab3d71b5c329bcab847e2151bba3baf0e0b915cad37e7e526c03f | quote: Stores handle parsing, indexing, retrieval, and reranking as one workflow.
  - [3] 2026-11-03: the rerank models run inside Store search; mxbai-rerank-large-v2 is one of them | capture: sha256:c3fc8672d21212919653d66e4e63db385fbb20c3c81f0419ab8a7b9f2f0107a0 | quote: | `mixedbread-ai/mxbai-rerank-large-v2` | Pointwise | 1.5B-parameter model tuned for accuracy across 100+ languages. |
  - [4] 2026-11-03: read operations are limited to 1,200 per minute with a burst capacity of 1,000 | capture: sha256:4daa645d55634686f35b4e141a64ccd6abfd2039024afb3ec9b6e03b1be7fed6 | quote: | Read | 1,200 | 1,000 | 1 minute |
  - probe:https://api.mixedbread.com/v1/stores/search 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:e47573ad60ded82e908f726f18ac901c25c365ed878123b9e90a9bd9f8279dc9 | quote: "status": 401
- sources:
  - [1] https://www.mixedbread.com/pricing
  - [2] https://www.mixedbread.com/docs/models/reranking
  - [3] https://www.mixedbread.com/docs/stores/search/rerank
  - [4] https://www.mixedbread.com/docs/api-reference/rate-limits
