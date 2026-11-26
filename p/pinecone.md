# Pinecone Inference

> pinecone.io | Databases and KV, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pinecone/ | JSON https://fshy.ajam.dev/api/v1/entity/pinecone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pinecone

- `databases-kv/pinecone` | qualifies-with-caveat | evidence documented | binding request-rate | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:21:21.176Z (live) | stale on 2026-12-10
- url https://www.pinecone.io/pricing/
- price USD 0.33/GB-month storage; USD 0.10/GB egress | parsed USD 330/TB-mo
- free tier: Starter: 2 GB serverless storage, 5 indexes, 1 project, 1 GB egress per month, us-east-1 only | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 2 GB of index storage per organization; 100 namespaces per index | source: [1]
- retention: free indexes are kept indefinitely; Pinecone removed the inactivity auto-archive policy, so no deletion clock applies to Starter. | source: [2] | note: null is indefinite: the inactivity policy was removed, so no inactivity or expiry deletion applies to Starter.
- egress: 1 GB per month on Starter. Builder is 10 GB; Standard includes 100 GB then USD 0.10/GB | metered: yes | free allowance: 1 GB per month | price per TB: USD 0.10/GB on Standard | source: [1]
- identity: email | detail: email signup; no card on Starter
- interface: rest, cli
- limits:
  - per-object-cap: 2 GB of storage per organization, not per index [1]
  - request-rate (binding): 1 GB egress per month on Starter [1]
  - request-rate (binding): 5 indexes, 1 project per organization, us-east-1 only, and 100 namespaces per index [1]
  - request-rate (binding): no connection limit is published for Starter; recorded as a gap [1]
  - per-object-cap: 100 namespaces per index [1]
  - write-gated: exceeding Starter limits after downgrading may block new requests until usage is within limits [3]
- interface detail: a REST API for data and control planes; Python, Node and Java SDKs; the pinecone CLI
- tooling: the Pinecone SDKs and CLI; no Postgres extension path
- composes with: a free vector index that mostly matters for a workload too large for pgvector on a free Postgres, because pgvector is already available on both Neon and Supabase at no extra cost
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: 2 GB is an organization-level cap and one project is the whole allowance, so there is no way to shard around it. 1 GB a month of egress is 33 MB a day, which a retrieval workload serving embeddings exceeds before the 2 GB of storage matters.
- evidence note: the pricing comparison table was read on 2026-10-22. The 1 GB monthly egress is on it. The project and index counts are on the pricing page too; they are recorded against it rather than against the object-limits page, which does not state them.
- evidence:
  - [1] 2026-10-22: Starter: storage up to 2 GB, egress up to 1 GB/month, indexes up to 5, namespaces per index 100; Builder USD 25 with 10 GB storage and 10 GB egress; Standard unlimited at USD 0.33/GB-month
  - [2] 2026-11-09: new users keep their free indexes indefinitely and there is no auto-archiving of inactive indexes | capture: sha256:43b4c8330b50db341481aff13d61ea2932520d2c81df1565e021ffce899ea70f | quote: Over the coming weeks, we will be opening up instant sign ups for all users, and allowing new users to keep their free indexes indefinitely. No more waitlist, no more auto-archiving of inactive indexes.
  - [4] 2026-11-09: Pinecone removed the inactivity policy, so no inactivity day count applies | capture: sha256:9c19fcced5b2aae58e5dc16b95824829e4bb0124cafc489a0fd413f5016449a1 | quote: Update: Pinecone has since removed the free plan waitlist and the inactivity policy.
  - [3] 2026-11-09: exceeding Starter limits blocks new requests until usage is within limits | capture: sha256:93315d1e71d6eae85e53c0ace17d2a7eb6617251066aa18275c29364939d2e8b | quote: If you exceed Starter limits after downgrading, new requests may be blocked until usage is within limits.
  - [5] 2026-11-09: deletion is tied to account deactivation for non-payment, not to inactivity | capture: sha256:440088c2ee2dbcc7d7302eaf29dcda9e7328f5b4a1bf26d333ea431ff3dc65ba | quote: If your account is deactivated for continued non-payment, account data is retained for 30 days before permanent deletion.
- sources:
  - [1] https://www.pinecone.io/pricing/
  - [2] https://www.pinecone.io/blog/gcp-starter/
  - [3] https://docs.pinecone.io/admin/billing/downgrade-billing-plan
  - [4] https://www.pinecone.io/blog/free-plan-update/
  - [5] https://docs.pinecone.io/guides/production/data-deletion

## Pinecone Inference (embeddings and reranking)

- `inference/pinecone-inference` | qualifies-with-caveat | evidence documented | binding volume-quota | category embedding and rerank API, monthly free token and request allowance on the Starter plan | tier Starter
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://www.pinecone.io/pricing/
- free tier: Starter plan, labelled Free: 5,000,000 embedding tokens a month per model (llama-text-embed-v2, multilingual-e5-large, pinecone-sparse-english-v0, text-embedding-3-small and -large) and 500 rerank requests a month (bge-reranker-v2-m3, pinecone-rerank-v0) | unit: tokens | metered on: request-count | read on: 2026-11-03 | source: [1] | note: the pricing page lists the three Pinecone-hosted embedding models and bge-reranker-v2-m3 only; the limits page also lists text-embedding-3 models and pinecone-rerank-v0 for Starter; gemini-embedding-2 and cohere-rerank-4-fast are not available on Starter
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Pinecone account; the pricing page labels Starter 'Free' and its start link goes to the billing settings of the console; unverified: the sign-up form fields and whether a card is asked, because the console page returned no content to the page reader
- interface: rest
- limits:
  - volume-quota (binding): Starter: 5,000,000 embedding tokens per month per model and 500 rerank requests per month per rerank model; reaching either returns HTTP 429 [1]
  - request-rate: Starter embedding throughput 250,000 passage tokens and 50,000 query tokens per minute per model (llama-text-embed-v2, multilingual-e5-large); bge-reranker-v2-m3 and pinecone-rerank-v0 60 requests per minute; inference requests 100 per second and 2,000 per minute per project [1]
- binding note: 500 rerank requests a month binds first on the rerank side; 5M tokens a month per model on the embedding side
- endpoint: https://api.pinecone.io/embed
- tooling: Pinecone SDKs and the REST inference endpoints embed and rerank; embeddings can be called without creating an index
- composes with: the Starter plan's index allowance (5 indexes, 2 GB) is the same account's vector store, so embed, store and rerank stay under one key
- reliability: no reliability event recorded; the Starter allowance is per month and resets
- notes: derived for scale: 500 rerank requests a month is about 16 a day, so rerank here suits a prototype or a nightly batch
- evidence note: the monthly token and request allowances and the per-minute limits are quoted from the vendor's limits page and pricing page; the sign-up form fields are unverified. The two pages disagree on pinecone-rerank-v0 for Starter.
- evidence:
  - [1] 2026-11-03: Starter allows 5,000,000 embedding tokens a month per model | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | Embedding tokens per month per model | 5,000,000 | 10,000,000 | Unlimited | Unlimited |
  - [1] 2026-11-03: Starter allows 500 rerank requests a month on bge-reranker-v2-m3 | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | `bge-reranker-v2-m3` | 500 | 1,000 | Unlimited | Unlimited |
  - [1] 2026-11-03: Starter allows 500 rerank requests a month on pinecone-rerank-v0, which the pricing page does not list for Starter | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | `pinecone-rerank-v0` | 500 | Not available | Unlimited | Unlimited |
  - [1] 2026-11-03: Starter passage embedding throughput on llama-text-embed-v2 is 250,000 tokens per minute | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | `llama-text-embed-v2` | Passage | 250,000 | 250,000 | 1,000,000 | 1,000,000 |
  - [1] 2026-11-03: bge-reranker-v2-m3 is limited to 60 requests per minute on Starter | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | `bge-reranker-v2-m3` | 60 | 60 | 60 | 60 |
  - [1] 2026-11-03: inference requests are limited to 2,000 per minute per project on every plan | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: | Inference requests per minute per project | 2,000 | 2,000 | 2,000 | 2,000 |
  - [1] 2026-11-03: the monthly limits answer HTTP 429 | capture: sha256:e1668959d515e9a83b1133eb19a4de08607883265d785392bcc8e228e2f9e622 | quote: Reaching a monthly usage limit returns a `429 - TOO_MANY_REQUESTS`.
  - [2] 2026-11-03: the pricing page states 5M tokens a month included on Starter for llama-text-embed-v2 | capture: sha256:8febedf53b359a24e25ca59072d2111c853b5240b074232f1d93a2b9e5f33fd9 | quote: | llama-text-embed-v2 | 5M tokens/mo incl. | 10M tokens/mo incl. | $0.16/M tokens | $0.16/M tokens |
  - [2] 2026-11-03: the pricing page states 500 rerank requests a month included on Starter | capture: sha256:8febedf53b359a24e25ca59072d2111c853b5240b074232f1d93a2b9e5f33fd9 | quote: | bge-reranker-v2-m3 | 500 requests/mo incl. | 1,000 requests/mo incl. | $2/1k requests | $2/1k requests |
  - [2] 2026-11-03: Pinecone Inference is part of the Starter plan, which the page labels Free | capture: sha256:8febedf53b359a24e25ca59072d2111c853b5240b074232f1d93a2b9e5f33fd9 | quote: - Pinecone [Inference](https://docs.pinecone.io/guides/inference/understanding-inference.md)
  - probe:https://api.pinecone.io/embed 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:4634ca74192d96f37c684bb5a176e1dde5df959ff30f99efcfc6b645156716b0 | quote: "status": 401
- sources:
  - [1] https://docs.pinecone.io/reference/api/database-limits/rate-limits.md
  - [2] https://www.pinecone.io/pricing/
