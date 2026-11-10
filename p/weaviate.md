# Weaviate Cloud

> weaviate.io | Databases and KV, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/weaviate/ | JSON https://fshy.ajam.dev/api/v1/entity/weaviate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Weaviate Cloud

- `databases-kv/weaviate-cloud` | qualifies-with-caveat | evidence documented | binding per-object-cap | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://weaviate.io/pricing
- free tier: 1 cluster per user, 100,000 objects, 1 GB memory, 10 GB disk, 1 collection, up to 3 tenants, always free | unit: objects | metered on: object-count | read on: 2026-10-22 | source: [1]
- per-object cap: 100,000 objects per cluster; 1 collection | source: [2]
- retention: always free, with no deletion clock published | source: [2]
- egress: not published on the pricing page; recorded as a gap | metered: no | source: [2]
- identity: email | detail: email signup; no card on Free
- interface: rest, cli
- limits:
  - per-object-cap (binding): 100,000 objects and one collection [2]
  - request-rate: one cluster per user; three tenants [2]
  - request-rate: no connection limit is published for the sandbox; recorded as a gap [3]
- interface detail: a REST API and GraphQL; Python, TypeScript, Java and Go clients
- tooling: the weaviate-client libraries; GraphQL for queries
- composes with: the only free vector tier that caps objects rather than bytes, so it is the right shape for many small records and the wrong shape for a few large ones
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: One collection is the constraint that decides it. A multi-tenant design that needs a collection per tenant stops at one, and a single collection with 100,000 objects is a small index.
- evidence note: the pricing page was read.
- evidence:
  - [1] 2026-10-22: Free: 'Always free - 1 cluster per user'; '100,000 objects - 1 GB memory - 10 GB disk'; '1 collection, up to 3 tenants'; the comparison table repeats object limit 100,000 and collection limit 1
- sources:
  - [1] https://weaviate.io/pricing
  - [2] https://weaviate.io/pricing/
  - [3] https://www.weaviate.io/pricing

## Weaviate Embeddings (Weaviate Cloud free cluster)

- `inference/weaviate-embeddings` | qualifies-with-caveat | evidence documented | binding request-rate | category embedding inference tied to a vector database cluster, daily request cap on a free cluster | tier Free cluster
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
- url https://docs.weaviate.io/cloud/embeddings
- free tier: usable on a free Weaviate Cloud cluster at 2,000 embedding requests per cluster per day; with 200 objects per batch that is at most 400,000 embeddings a day. Text models: snowflake-arctic-embed-m-v1.5 and -l-v2.0; multimodal: ModernVBERT/colmodernvbert; no reranker is listed | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: the service is called from a cluster, with no separate key: 'you only need a connection to your Weaviate Cloud cluster'
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Weaviate Cloud account and a free cluster; unverified: the sign-up form fields and whether a card is asked, because the console answered with a login wall to the page reader
- interface: rest
- limits:
  - request-rate (binding): 2,000 requests per cluster per day on a free cluster; batch import is capped at 200 objects per batch, so at most 400,000 embeddings per day [1]
- binding note: 2,000 requests per cluster per day is the only published limit on a free cluster
- tooling: Weaviate client libraries vectorize on import and query; the service is enabled by default for every cluster
- composes with: embeddings stay inside the same free cluster that stores the vectors
- reliability: the page calls Weaviate Embeddings a paid service that can be tried free on a free cluster; the data is processed in the United States
- notes: derived: 2,000 requests * 200 objects per batch = 400,000 embeddings per day, as the vendor page states
- evidence note: the daily request cap, the batch size and the model list are quoted from the vendor page; the sign-up fields are unverified.
- evidence:
  - [1] 2026-11-03: a free cluster is limited to 2,000 embedding requests per cluster per day | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: Weaviate Embeddings only imposes usage limits on requests for free clusters. The rate limit for free clusters is `2000` requests per cluster per day.
  - [1] 2026-11-03: a free cluster can generate at most 400,000 embeddings a day with 200 objects per batch | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: This means that you can generate up to a maximum of `400 000` embeddings (`2000 (requests) * 200 (objects per request)`) within your free cluster.
  - [1] 2026-11-03: Weaviate Embeddings can be tried free on a free cluster | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: > You can try it out for free on a free cluster.
  - [1] 2026-11-03: snowflake-arctic-embed-l-v2.0 is one of the hosted text embedding models | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: - [`Snowflake/snowflake-arctic-embed-l-v2.0`](https://docs.weaviate.io/cloud/embeddings/models#snowflake-arctic-embed-l-v2.0)
- sources:
  - [1] https://docs.weaviate.io/cloud/embeddings
