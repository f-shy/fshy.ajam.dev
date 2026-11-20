# Weaviate Cloud

> weaviate.io | Databases and KV, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/weaviate/ | JSON https://fshy.ajam.dev/api/v1/entity/weaviate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Weaviate Cloud

- `databases-kv/weaviate-cloud` | qualifies-with-caveat | evidence documented | binding per-object-cap | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:21:21.973Z (live) | stale on 2026-12-10
- url https://weaviate.io/pricing
- free tier: 1 cluster per user, 100,000 objects, 1 GB memory, 10 GB disk, 1 collection, up to 3 tenants, always free | unit: objects | metered on: object-count | read on: 2026-10-22 | source: [1]
- per-object cap: 100,000 objects per cluster; 1 collection | source: [2]
- retention: a free cluster is suspended after 7 days of inactivity with data preserved, and permanently deleted after 30 days of total inactivity (about 23 days after suspension); a warning email is sent 1 day before deletion | days: 30 | source: [3] | note: days is the deletion clock: the cluster is suspended after 7 days of inactivity with data preserved; reactivating it from the console prevents deletion
- egress: not published on the pricing page; recorded as a gap | metered: no | source: [2]
- identity: email | detail: email signup; no card on Free
- interface: rest, cli
- limits:
  - per-object-cap (binding): 100,000 objects and one collection [2]
  - request-rate: one cluster per user; three tenants [2]
  - request-rate: no connection limit is published for the sandbox; recorded as a gap [4]
- interface detail: a REST API and GraphQL; Python, TypeScript, Java and Go clients
- tooling: the weaviate-client libraries; GraphQL for queries
- composes with: the only free vector tier that caps objects rather than bytes, so it is the right shape for many small records and the wrong shape for a few large ones
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: One collection is the constraint that decides it. A multi-tenant design that needs a collection per tenant stops at one, and a single collection with 100,000 objects is a small index.
- evidence note: the pricing page was read.
- evidence:
  - [1] 2026-10-22: Free: 'Always free - 1 cluster per user'; '100,000 objects - 1 GB memory - 10 GB disk'; '1 collection, up to 3 tenants'; the comparison table repeats object limit 100,000 and collection limit 1
  - [3] 2026-11-09: the create-cluster page states suspension after 7 days of inactivity with data preserved, permanent deletion after 30 days of total inactivity, and a warning email 1 day before deletion | capture: sha256:2a846c3d1a316eb182d43d8912d8be0041c4406a4a7b9d4d7322feba8344d35d | quote: After 7 days of inactivity, the cluster is suspended and your data is preserved. ... If a cluster stays inactive, it is permanently deleted after 30 days of total inactivity (about 23 days after it is suspended). Weaviate sends a warning email 1 day before the cluster is deleted.
  - [3] 2026-11-09: the page states the 7-day suspension with data preserved, reactivation from the console, and deletion at 30 days of inactivity | capture: sha256:2a846c3d1a316eb182d43d8912d8be0041c4406a4a7b9d4d7322feba8344d35d | quote: After 7 days of inactivity, the cluster is suspended and your data is preserved. ... You can reactivate a suspended cluster from the [Weaviate Cloud console](https://console.weaviate.cloud/). ... it is permanently deleted after 30 days of total inactivity
- sources:
  - [1] https://weaviate.io/pricing
  - [2] https://weaviate.io/pricing/
  - [3] https://docs.weaviate.io/cloud/manage-clusters/create
  - [4] https://www.weaviate.io/pricing

## Weaviate Embeddings (Weaviate Cloud free cluster)

- `inference/weaviate-embeddings` | qualifies-with-caveat | evidence documented | binding request-rate | category embedding inference tied to a vector database cluster, daily request cap on a free cluster | tier Free cluster
- needs card unknown, phone no, ID no, institution no | verified 2026-11-18T05:36:39.022Z (live) | stale on 2026-12-19
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
- interface detail: Weaviate Embeddings is a managed service at POST https://api.embedding.weaviate.io/v1/embeddings/embed with a JSON body of input / model / dimensions / optional is_search_query, authenticated by an Authorization Bearer token (Weaviate Cloud API key or OIDC token) and an X-Weaviate-Cluster-Url header. Callers reach it through a Weaviate Cloud cluster text2vec-weaviate vectorizer over the cluster REST/gRPC API; no separate key is needed (cluster credentials authorize it).
- endpoint: https://api.embedding.weaviate.io/v1/embeddings/embed (POST); called server-side by the cluster text2vec-weaviate vectorizer — callers use their cluster REST endpoint and API key, with no separate embeddings key
- tooling: Weaviate client libraries vectorize on import and query; the service is enabled by default for every cluster. Enable vector_config Configure.Vectors.text2vec_weaviate() (Python) / text2vecWeaviate (JS, Java, C#); Go has no direct support and must pass X-Weaviate-Api-Key and X-Weaviate-Cluster-Url headers manually. The optional base_url vectorizer parameter overrides the service origin, but the server accepts only https://api.embedding.weaviate.io or an origin in MODULES_WEAVIATE_EMBEDDINGS_ALLOWED_BASE_URLS.
- composes with: embeddings stay inside the same free cluster that stores the vectors
- reliability: the page calls Weaviate Embeddings a paid service that can be tried free on a free cluster; the data is processed in the United States
- notes: derived: 2,000 requests * 200 objects per batch = 400,000 embeddings per day, as the vendor page states. The embeddings service host and POST route are pinned from Weaviate own server source at commit df6395886859be4020542bfdd0d485dad4829220 (2026-11-09), read 2026-11-18; the host answered HTTP 401 with a Bearer-token guidance body to an unauthenticated GET; a concrete cluster REST host and API key are unverified: behind a sign-up. The 2026-11-03 and 2026-11-18 captures of the overview page differ in bytes but all carried-over quotes match. On 2026-11-18 one keyless POST of an embedding body to /v1/embeddings/embed returned HTTP 401 missing authentication token, so the embed route is live.
- evidence note: the endpoint host and route are quoted from first-party Weaviate server source, corroborated by a live 401 from the host; the documented no-extra-key auth is quoted from Weaviate docs; the concrete per-cluster endpoint and API key are behind a sign-up.
- evidence:
  - [1] 2026-11-03: a free cluster is limited to 2,000 embedding requests per cluster per day | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: Weaviate Embeddings only imposes usage limits on requests for free clusters. The rate limit for free clusters is `2000` requests per cluster per day.
  - [1] 2026-11-03: a free cluster can generate at most 400,000 embeddings a day with 200 objects per batch | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: This means that you can generate up to a maximum of `400 000` embeddings (`2000 (requests) * 200 (objects per request)`) within your free cluster.
  - [1] 2026-11-03: Weaviate Embeddings can be tried free on a free cluster | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: > You can try it out for free on a free cluster.
  - [1] 2026-11-03: snowflake-arctic-embed-l-v2.0 is one of the hosted text embedding models | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: - [`Snowflake/snowflake-arctic-embed-l-v2.0`](https://docs.weaviate.io/cloud/embeddings/models#snowflake-arctic-embed-l-v2.0)
  - [2] 2026-11-18: cluster credentials authorize the embeddings service | capture: sha256:c82262da9641546c6d3b32d8530f3df6796ecc07454a2bc2c010d138720df757 | quote: Your Weaviate Cloud credentials are automatically used to authorize your access to Weaviate Embeddings.
  - [3] 2026-11-18: the Weaviate Embeddings service endpoint is https://api.embedding.weaviate.io with path /v1/embeddings/embed | capture: sha256:40ef38c86af0a88d904a7f1b30d2c5ce91d5d70fb3349a21de5c7258eb6bc62e | quote: const ( DefaultBaseURL = "https://api.embedding.weaviate.io" URLPath = "/v1/embeddings/embed" )
  - [3] 2026-11-18: the service route is called with HTTP POST | capture: sha256:40ef38c86af0a88d904a7f1b30d2c5ce91d5d70fb3349a21de5c7258eb6bc62e | quote: req, err := http.NewRequestWithContext(ctx, "POST", url, bytes.NewReader(body))
  - [3] 2026-11-18: auth is an Authorization token plus the X-Weaviate-Cluster-Url header | capture: sha256:40ef38c86af0a88d904a7f1b30d2c5ce91d5d70fb3349a21de5c7258eb6bc62e | quote: req.Header.Set("Authorization", token) req.Header.Add("X-Weaviate-Cluster-Url", clusterURL)
  - [1] 2026-11-18: callers need only a cluster connection; no separate embeddings key | capture: sha256:9e27698b31eefdc45a797572199a60fd1a2801555116f472dd7214a9f79c1cd9 | quote: In order to use Weaviate Embeddings you only need a connection to your Weaviate Cloud cluster. No additional authentication is specifically needed, and the Weaviate Embeddings service is enabled by default for all clusters.
  - [4] 2026-11-18: the optional base_url override is restricted to the default origin or a server allowlist | capture: sha256:f4c02358a101b6c2e1dcb628a5bd9db6298c4afbfaa9a1aaa7501d36493a3f55 | quote: const AllowedBaseURLsEnv = "MODULES_WEAVIATE_EMBEDDINGS_ALLOWED_BASE_URLS"
  - probe:https://api.embedding.weaviate.io/v1/embeddings/embed 2026-11-18: a keyless POST to https://api.embedding.weaviate.io/v1/embeddings/embed returned HTTP 401 with body {'detail':'Missing authentication token. Please provide an API key or OIDC authentication token in the Authori and no completion in 615 ms Probe start 2026-11-18T05:36:39.022Z. | capture: sha256:e2961577fe8aad6633bed359aa71ef4db0d89d5b1b0ac470a2efd3ed4856d382 | quote: a keyless POST to https://api.embedding.weaviate.io/v1/embeddings/embed returned HTTP 401 with body {'detail':'Missing authentication token. Please provide an API key or OIDC authentication token in the Authori and no completion in 615 ms
- sources:
  - [1] https://docs.weaviate.io/cloud/embeddings
  - [2] https://docs.weaviate.io/weaviate/model-providers/weaviate/embeddings
  - [3] https://raw.githubusercontent.com/weaviate/weaviate/main/usecases/modulecomponents/clients/weaviateembed/weaviate_embed.go
  - [4] https://raw.githubusercontent.com/weaviate/weaviate/main/usecases/modulecomponents/clients/weaviateembed/base_url.go
