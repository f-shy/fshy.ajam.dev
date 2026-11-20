# Qdrant Cloud

> qdrant.tech | Databases and KV, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qdrant/ | JSON https://fshy.ajam.dev/api/v1/entity/qdrant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qdrant Cloud

- `databases-kv/qdrant-cloud` | qualifies | evidence documented | binding per-object-cap | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:21:21.972Z (live) | stale on 2026-12-10
- url https://qdrant.tech/pricing/
- free tier: free tier cluster with 1 GB RAM and 4 GB disk, no high availability, one cluster | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 4 GB disk per cluster | source: [1]
- retention: free tier clusters are automatically suspended after 1 week of inactivity and deleted after 4 weeks of inactivity if not reactivated; reactivation prevents deletion | days: 28 | source: [2] | note: days is the deletion clock: the cluster is suspended after 1 week of inactivity and deleted at 4 weeks of inactivity; reactivating it before deletion prevents deletion
- egress: not published on the pricing page; recorded as a gap | metered: no | source: [1]
- identity: email | detail: email or GitHub signup; no card on Free
- interface: rest, cli
- limits:
  - per-object-cap (binding): 4 GB disk per cluster; 1 GB RAM [1]
  - request-rate: one cluster per account on Free [1]
  - request-rate: no connection limit is published for the free tier; recorded as a gap [1]
- interface detail: a REST API and gRPC; Python, JS and Rust clients
- tooling: the qdrant-client libraries over gRPC or REST
- composes with: the largest free vector storage by disk, and the closest thing to a self-managed index without a host
- reliability: no high availability on the free tier, so the single node is the availability
- notes: 4 GB of disk holds roughly 1.4 million vectors at 768 dimensions and 4 bytes per component, before index overhead. That puts the ~1 million vectors in circulation in the right order. The figure comes from arithmetic, not from a measurement. What happens at 1 GB of RAM is not published. The page offers an upgrade and states no refusal, throttle or deletion. That absence is documented, and it is not headroom.
- evidence note: the pricing FAQ was read; the numbers are in the page's own answers.
- evidence:
  - [1] 2026-10-22: 'The free tier includes 1GB RAM and 4GB disk storage'; the free tier is 'limited to 1GB RAM and 4GB disk without high availability'
  - [2] 2026-11-09: the create-cluster page states free tier clusters are suspended after 1 week of inactivity and deleted after 4 weeks if not reactivated | capture: sha256:bdc2a5ddef5ce5ed983445fe4cd710b182bda104fe3986708fe9f3fcdfb4e32e | quote: If unused, free tier clusters are automatically suspended after 1 week, and deleted after 4 weeks of inactivity if not reactivated. You can upgrade to a standard cluster at any time.
- sources:
  - [1] https://qdrant.tech/pricing/
  - [2] https://qdrant.tech/documentation/cloud/create-cluster/

## Qdrant Cloud Inference (free models on a free cluster)

- `inference/qdrant-cloud-inference` | qualifies-with-caveat | evidence documented | binding none | category embedding inference inside a vector database cluster, free models with no stated token cap | tier Free cluster
- needs card unknown, phone no, ID no, institution no | verified 2026-11-18T04:36:13.441Z (live) | stale on 2026-12-19
- url https://qdrant.tech/cloud-inference/
- free tier: BM25 and a dense model such as all-MiniLM-L6-v2 are free to use on free-tier clusters, with no token charge; larger models (mxbai, SPLADE) run on metered tokens with a monthly free allowance of up to 5 million tokens per model on paid clusters only. No rerank model is listed | unit: tokens | metered on: request-count | read on: 2026-11-03 | source: [1] | note: unverified: no request or token cap for the free models appears on the pages read; the Inference tab of a cluster in the console lists the current models, which the page reader could not open
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the log-in page offers an email address, Continue with Google or Continue with GitHub; unverified: whether the sign-up asks for a card
- interface: rest
- limits:
  - request-rate: unverified: no rate or token limit for the free models is published on the pages read [1]
- binding note: no limit on the free models is published; the free cluster's own 1 GB RAM and 4 GB disk bound what can be stored
- interface detail: Server-side inference through the cluster own REST/gRPC API: pass a Document (text) or Image object with a "model" name in place of a precomputed vector in the upsert and query routes; auth is the cluster API key in the api-key header. Free Qdrant-hosted models need no extra key. Qdrant-hosted inference runs in the US region for free models and can be called from any region. External-provider models are proxied through the same cluster API with the provider key in a per-request header (openai-api-key / cohere-api-key / jina-api-key / openrouter-api-key).
- endpoint: https://<cluster-id>.<region>.cloud.qdrant.io:6333 (REST) / :6334 (gRPC); inference via PUT /collections/<collection>/points?wait=true and POST /collections/<collection>/points/query; no standalone inference host
- tooling: the Qdrant client sends text or images in the upsert and query calls and the cluster embeds them; external providers (OpenAI, Cohere, Jina AI, OpenRouter) are proxied with a per-request provider key header. Python client uses QdrantClient(url=..., api_key=..., cloud_inference=True) and the same route works from the JS/Rust/Java/C#/Go SDKs; without cloud_inference the Python client embeds locally via FastEmbed.
- composes with: embedding and search in one call on the same free cluster; the free tier is the cluster of 1 GB RAM and 4 GB disk
- reliability: no reliability event recorded
- notes: A concrete cluster endpoint and the Inference-tab model/usage details are unverified: behind a sign-up. The 2026-11-03 and 2026-11-18 captures of the marketing page differ in bytes but not in quoted text. No request could be sent: the inference route is a per-cluster data plane at <cluster-id>.<region>.cloud.qdrant.io, so no hostname resolves until an account has created a cluster, and this research does not create accounts.
- evidence note: The endpoint pattern, routes, method and api-key auth are quoted from first-party Qdrant docs; the dedicated remote inference service is internal and not a caller-facing endpoint; the concrete per-cluster endpoint and the Inference-tab catalogue are behind a sign-up.
- evidence:
  - [1] 2026-11-03: BM25 and the dense all-MiniLM-L6-v2 model are free, including on free-tier clusters | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Start at no cost: BM25 and a dense model like all-MiniLM-L6-v2 are free to use, including on free-tier clusters.
  - [1] 2026-11-03: free models carry no token charges; the 5 million token monthly allowance is for paid clusters | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Free models carry no token charges, and paid Qdrant Cloud users receive a monthly free allowance of up to 5 million tokens per model.
  - [1] 2026-11-03: the free models run in the US region and can be called from any region | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Inference runs in the EU for clusters in EU regions and in the US for clusters in all other regions. Free models are hosted in the US region but can be called from any region.
  - [2] 2026-11-03: the Qdrant Cloud log-in page offers an email, Google or GitHub sign-in | capture: sha256:15d9d1000da7f21455c01361b4d63835f5d1010a61c438dfd3c810c6a40520f2 | quote: Continue with GitHub
  - [3] 2026-11-18: inference search uses POST to the cluster /collections/<collection>/points/query route with the cluster API key in the api-key header | capture: sha256:dc77b5c074a14c3c81e30e5b44848bb9ed0677188c3535a60fe8e56c53e01acb | quote: curl -X POST "https://xyz-example.qdrant.io:6333/collections/<your-collection>/points/query" \ -H "Content-Type: application/json" \ -H "api-key: <paste-your-api-key-here>"
  - [4] 2026-11-18: inference is server-side and invoked by passing an Inference Object instead of a precomputed vector | capture: sha256:b8012b788d6353680d05a157b8aadd80c29b53ff4ad8b4ca8aea2668f28cf273 | quote: When using Qdrant Cloud Inference or Qdrant’s BM25 model, embeddings are generated server-side. Instead of pre-computed vectors, you pass Inference Objects when ingesting or querying data.
  - [5] 2026-11-18: the cluster REST and gRPC APIs are the inference interface; there is no separate inference API | capture: sha256:c7e66ff52c238f8015577698c85ab9c17a802101f8760882f8c9d6858c14b115 | quote: Use inference through the Qdrant SDKs and the REST or gRPC APIs when upserting points and when querying the database.
  - [6] 2026-11-18: free Qdrant-hosted models need no extra API key and work on free-tier clusters | capture: sha256:a0db5081e115edac95c28ed045badea2b7c66e0233ac2480e650f07109dfc6c3 | quote: Models hosted by Qdrant Cloud, listed in the Models tables. They need no extra API key, and the free ones also work on free-tier clusters.
  - [7] 2026-11-18: external-provider inference is proxied through the Qdrant API with a per-request provider-key header | capture: sha256:b2a2b188a14417569496ec81e9398272422c95487ab07deade6b303d45285896 | quote: Provide the provider’s API key in the request header (`openai-api-key`, `cohere-api-key`, `jina-api-key`, or `openrouter-api-key`).
- sources:
  - [1] https://qdrant.tech/cloud-inference/
  - [2] https://cloud.qdrant.io/
  - [3] https://qdrant.tech/documentation/inference/cloud-inference/
  - [4] https://qdrant.tech/documentation/inference/inference-api/
  - [5] https://qdrant.tech/documentation/cloud/inference/
  - [6] https://qdrant.tech/documentation/embeddings/qdrant-cloud-inference/
  - [7] https://qdrant.tech/documentation/inference/external-inference-providers/
