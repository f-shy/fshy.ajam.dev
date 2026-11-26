# Couchbase Capella

> couchbase.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/couchbase/ | JSON https://fshy.ajam.dev/api/v1/entity/couchbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Couchbase Capella

- `databases-kv/couchbase-capella` | qualifies-with-caveat | evidence documented | binding retention-clamped | category managed NoSQL document database with key-value, SQL++, search and vector workloads | tier Free
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T00:19:24.698Z (live) | stale on 2026-12-20
- url https://www.couchbase.com/pricing
- free tier: One free tier operational cluster per organization: 1 node, 8 GB RAM, 8 to 10 GB data storage depending on cloud, SQL++ and key value, Search (vector, FTS, geo), Mobile App Services, RBAC with scopes and collections, forum support; no credit card required and free for continuous use while active | unit: GB | metered on: stored-bytes | read on: 2026-11-19 | source: [1] | note: The pricing page states 1 node and 8 GB of RAM. Cloud reference pages give the data-storage allowance as 10 GB on AWS and Azure and 8 GB on GCP. The plan is perpetual while the cluster is active, not a trial.
- per-object cap: unverified: the free-tier page does not state a per-document size cap; the Capella Data API platform limit is 100 MB per request and response payload, but that is an interface limit and not a stated per-object cap on the free tier | source: [2] | note: The 100 MB figure is the Data API payload limit and is recorded under limits[] as an interface cap, not as a per-object cap.
- retention: Data and state are preserved while the cluster is active. After more than 72 hours without activity Couchbase turns off the free cluster and linked App Services, preserving data and state; after more than 30 days without activity Couchbase deletes the cluster and linked App Services. Upgrading from the free plan to a paid Support plan also deletes the existing free cluster. | days: 30 | source: [3] | note: days is the inactivity period that triggers deletion. The 72-hour mark only turns the cluster off and preserves data; the 30-day mark deletes it.
- egress: Capella passes through cloud-provider data transfer charges based on GiB and transfer type. Internet egress is commonly .09 credits per GB in North American and European regions; inter-zone or intra-region transfer is commonly .01 credit per GB on AWS and GCP and free on Azure. Data import into Capella and transfer between instances in the same Availability Zone are free. No free egress allowance is published for the free plan. | metered: yes | source: [4]
- identity: email | detail: The sign-up page offers Email Address, GitHub Account or Google Account. The billing docs state no credit balance or credit card is needed for the Free plan.
- interface: rest, cli
- limits:
  - volume-quota: 1 free tier operational cluster per organization; 10 GB data storage on AWS and Azure and 8 GB on GCP; 1 node, 8 GB RAM [5]
  - retention-clamped (binding): cluster turns off after more than 72 hours of inactivity with data preserved, and is deleted after more than 30 days of inactivity [3]
  - request-rate: Data API is limited to 10,000 requests per second per node; payloads restricted to 100 MB [2]
- binding note: The cluster is deleted after 30 days without activity, so a workload with a persistent idle gap fails before the 8 to 10 GB storage or the 10,000 requests per second interface limit is reached.
- interface detail: Couchbase SDKs (Java, Python, Node.js, PHP and others) connect over the couchbases:// TLS protocol; a RESTful Data API exposes document CRUD under /v1/ with passthrough to Query and Search services; a Management API and the Capella web console manage the cluster.
- endpoint: couchbases://<cluster>.dp.cloud.couchbase.com
- tooling: Couchbase SDKs (Java, Python, Node.js, PHP), any HTTP client such as curl or Postman against the Data API, the cbbackupmgr CLI for backup, the Capella web console, and a Management API key for automation
- composes with: A free Capella cluster can hold a document and vector store behind a free Worker or tunnel for a public REST path, with the SDK or Data API as the write interface.
- reliability: The free cluster turns off after 72 hours idle and is deleted after 30 days idle; upgrading to a paid plan deletes the existing free cluster, and the backup and restore, private endpoint, network peering, audit log and on/off schedule features are not available on the free tier.
- notes: The free tier is a real managed Couchbase Server cluster, not a sandbox. Two caveats bind: the cluster is deleted after 30 days idle and upgrading to a paid plan deletes it, so data must be backed out with cbbackupmgr before either. The storage allowance differs by cloud: 10 GB on AWS and Azure, 8 GB on GCP. The per-document cap is not published; the 100 MB figure is the Data API payload limit, not a free-tier object cap. Couchbase Server is also available as self-hosted software, but that offer is the last resort and is not the offer recorded here.
- evidence note: All figures come from first-party Couchbase pricing, product, billing and docs pages captured and quoted on 2026-11-19. No probe was run, so the rung stays documented.
- evidence:
  - [1] 2026-11-19: the free tier is a managed NoSQL database with about 1 node and 8 GB, no credit card required | capture: sha256:6f847bd444e61b7e74beefaae8e6e7aba63396d0b470429119fb9787173a9ba7 | quote: The Capella free tier offers a fully managed NoSQL DBaaS with credits, sample data, SQL++ queries, search, mobile sync, and a small cluster (≈1 node, ~8GB) for prototyping – no credit card required.
  - [4] 2026-11-19: the Free plan is perpetual while active and needs no card or credit balance | capture: sha256:f5cd214c3aa486f621bfbda76c315fad6c9391511ad5ba2557d818ecdcc5f53e | quote: Clusters and services on the Free plan are always free and available, as long as you're actively using them. You do not need to have a credit balance or credit card in your organization to use the Free plan.
  - [4] 2026-11-19: one free cluster per organization and no in-place support-plan change | capture: sha256:f5cd214c3aa486f621bfbda76c315fad6c9391511ad5ba2557d818ecdcc5f53e | quote: Each organization can use only 1 free tier cluster. You cannot change the support plan for a free tier cluster to a paid plan.
  - [4] 2026-11-19: data transfer out is metered and passed through rather than free | capture: sha256:f5cd214c3aa486f621bfbda76c315fad6c9391511ad5ba2557d818ecdcc5f53e | quote: Capella passes through the cost of data transfer charges, based on the GiB amount and type of data transfer, for each operational cluster.
  - [3] 2026-11-19: the signup gate offers email address, GitHub account or Google account | capture: sha256:0ab4fe078c1ef17af94e390267b6d5a13ad917f3a2d9740cb8a0edfd0230533b | quote: To create an account, go to the Couchbase Capella Sign-up page and choose one of the following sign-up options:
  - [3] 2026-11-19: one free cluster per organization, with a 72-hour inactivity turn-off | capture: sha256:0ab4fe078c1ef17af94e390267b6d5a13ad917f3a2d9740cb8a0edfd0230533b | quote: Only 1 free tier operational cluster is available per organization and it automatically turns off after 72 hours of inactivity.
  - [3] 2026-11-19: thirty days of inactivity deletes the free cluster | capture: sha256:0ab4fe078c1ef17af94e390267b6d5a13ad917f3a2d9740cb8a0edfd0230533b | quote: If there's no activity in your free tier operational cluster for more than 30 days, Couchbase deletes the operational cluster and any linked App Services.
  - [3] 2026-11-19: upgrading to a paid plan deletes the free cluster | capture: sha256:0ab4fe078c1ef17af94e390267b6d5a13ad917f3a2d9740cb8a0edfd0230533b | quote: When upgrading from a free tier plan to a paid Support plan, Couchbase deletes your existing free tier operational cluster.
  - [5] 2026-11-19: AWS free-tier clusters allow 10 GB of data storage | capture: sha256:e3e50646c1224655de4a160aa5538047e77e0fe2acc4da36416ea7e93b0aed48 | quote: Free tier operational clusters only allow 10 GB of data storage.
  - [6] 2026-11-19: GCP free-tier clusters include 8 GB of data storage | capture: sha256:86073b994f7bcbc0b09cd18fd5f50e2327f2341f15f0af181d1b286b25948adc | quote: Free tier operational clusters include 8 GB of data storage.
  - [2] 2026-11-19: a REST interface with document CRUD and query and search passthrough is documented | capture: sha256:d35828da4de6bbd08916210bddd640d6f29d57b0a26a6d663388ea4fb506a0f8 | quote: The Couchbase Capella Data API is a secure REST API that enables you to create, read, update, and delete data. It also provides passthrough access to the Query Service and the Search Service, so that you can run SQL++ queries and full-text searches.
  - [2] 2026-11-19: the Data API is rate-limited to 10,000 requests per second per node | capture: sha256:d35828da4de6bbd08916210bddd640d6f29d57b0a26a6d663388ea4fb506a0f8 | quote: Requests are limited to 10,000 requests per second per node.
  - [2] 2026-11-19: the Data API payload is capped at 100 MB | capture: sha256:d35828da4de6bbd08916210bddd640d6f29d57b0a26a6d663388ea4fb506a0f8 | quote: Requests and response payloads are restricted to 100 MB.
- sources:
  - [1] https://www.couchbase.com/pricing
  - [2] https://docs.couchbase.com/cloud/data-api-guide/data-api-intro.md
  - [3] https://docs.couchbase.com/cloud/get-started/create-account.html
  - [4] https://docs.couchbase.com/cloud/billing/billing.html
  - [5] https://docs.couchbase.com/cloud/reference/aws.html
  - [6] https://docs.couchbase.com/cloud/reference/gcp.html
