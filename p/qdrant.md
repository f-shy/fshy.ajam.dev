# Qdrant Cloud

> qdrant.tech | Databases and KV, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qdrant/ | JSON https://fshy.ajam.dev/api/v1/entity/qdrant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qdrant Cloud

- `databases-kv/qdrant-cloud` | qualifies | evidence documented | binding per-object-cap | category vector database
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-22
- url https://qdrant.tech/pricing/
- free tier: free tier cluster with 1 GB RAM and 4 GB disk, no high availability, one cluster | unit: GB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 4 GB disk per cluster | source: [1]
- retention: no deletion clock and no exhaustion behaviour is published; the FAQ says only that if data growth exceeds the free tier you 'can easily upgrade'. Nothing states what happens to a cluster that reaches 1 GB of RAM | source: [1] | note: an absence of a failure mode rather than a failure mode, which is weaker evidence than a stated limit
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
- sources:
  - [1] https://qdrant.tech/pricing/

## Qdrant Cloud Inference (free models on a free cluster)

- `inference/qdrant-cloud-inference` | qualifies-with-caveat | evidence documented | binding none | category embedding inference inside a vector database cluster, free models with no stated token cap | tier Free cluster
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:34:03.660Z (live) | stale on 2026-12-04
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
- tooling: the Qdrant client sends text or images in the upsert and query calls and the cluster embeds them; external providers (OpenAI, Cohere, Jina AI, OpenRouter) are accepted with the caller's own key
- composes with: embedding and search in one call on the same free cluster; the free tier is the cluster of 1 GB RAM and 4 GB disk
- reliability: no reliability event recorded
- evidence note: the free-model statement, the paid-only 5M token allowance and the region note are quoted from the vendor page; the free models' limits and the sign-up card question are unverified.
- evidence:
  - [1] 2026-11-03: BM25 and the dense all-MiniLM-L6-v2 model are free, including on free-tier clusters | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Start at no cost: BM25 and a dense model like all-MiniLM-L6-v2 are free to use, including on free-tier clusters.
  - [1] 2026-11-03: free models carry no token charges; the 5 million token monthly allowance is for paid clusters | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Free models carry no token charges, and paid Qdrant Cloud users receive a monthly free allowance of up to 5 million tokens per model.
  - [1] 2026-11-03: the free models run in the US region and can be called from any region | capture: sha256:3630eec3acd9d50a22dcc83f9d217cddec8b117e4740ac8e9f106451d9445dea | quote: Inference runs in the EU for clusters in EU regions and in the US for clusters in all other regions. Free models are hosted in the US region but can be called from any region.
  - [2] 2026-11-03: the Qdrant Cloud log-in page offers an email, Google or GitHub sign-in | capture: sha256:15d9d1000da7f21455c01361b4d63835f5d1010a61c438dfd3c810c6a40520f2 | quote: Continue with GitHub
- sources:
  - [1] https://qdrant.tech/cloud-inference/
  - [2] https://cloud.qdrant.io/
