# ScyllaDB Cloud

> scylladb.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scylladb/ | JSON https://fshy.ajam.dev/api/v1/entity/scylladb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ScyllaDB Cloud

- `databases-kv/scylladb-cloud` | trial-only | evidence documented | binding retention-clamped | category fully managed wide-column NoSQL database (Cassandra/DynamoDB API) | tier Developer Free Trial (30-day) / Production Evaluation (48-hour)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:17.998Z (live) | stale on 2026-12-20
- url https://scylladb.com/pricing
- free tier: Developer Free Trial: a 30-day trial on smaller instances (e.g. AWS t3.micro); Production Evaluation: a 48-hour free trial of production-grade instances. One free trial per account. | unit: mixed | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: Two time-boxed trials, not a perpetual free tier: 30 days on small instances and 48 hours on production-grade instances. No perpetual free cluster is published on the first-party pricing or docs pages.
- per-object cap: unverified: no per-object size cap stated on the first-party pages read; trial clusters are limited to the smallest indexing node size (AWS t4g.medium / GCP e2-medium, 2 vCPUs and 4 GiB RAM each) | source: [2] | note: The only published size constraint is the trial node size, not a single-object cap.
- retention: the free offering is a time-limited trial: 30 days for the developer trial and 48 hours for the production evaluation, after which a regular paid cluster is required | days: 30 | source: [1] | note: The 30-day figure is the developer trial length; the production evaluation is 48 hours. Both expire rather than delete data on a storage cap.
- egress: standard cloud-provider rates apply for Internet egress and inter-region transfer; no fixed free egress allowance is published on the first-party pages read | metered: yes | source: [1]
- identity: email | detail: sign-up asks for a company email address, first name, last name and company name, or Google/GitHub/LinkedIn; no card is taken at sign-up, and payment information is prompted only when creating a regular paid cluster
- interface: cli, unknown
- limits:
  - retention-clamped (binding): one 30-day developer trial or one 48-hour production evaluation per account [1]
  - volume-quota: trial clusters limited to the smallest indexing node size: AWS t4g.medium or GCP e2-medium, 2 vCPUs and 4 GiB RAM [2]
- binding note: Both free paths are time-boxed trials that expire (30 days or 48 hours) and require a paid cluster afterwards, so the clock binds before any storage or request cap.
- interface detail: CQL binary protocol version 3 (Apache Cassandra compatibility) and the Alternator DynamoDB-compatible API; direct TLS connections on standard CQL ports with an IP allowlist. No dedicated CQL token exists in the interface vocabulary, so 'unknown' names it.
- tooling: shard-aware CQL drivers (C++, Java, Python, Go, Rust), any CQLv3-compatible Cassandra driver, a Terraform provider, and ScyllaDB Monitoring; rclone does not apply
- composes with: a free-trial CQL cluster reached over the public endpoint from a tunnel or a small worker gives a programme-accessible store for the trial window; the self-hosted ScyllaDB server is a last-resort option and is not a hosted free tier
- reliability: trial clusters get no production SLA or backup guarantee; public-IP direct connections are intended for evaluation, and production uses VPC peering or PrivateLink.
- notes: Hosted ScyllaDB Cloud offers two free trials on a vendor-managed cluster. A self-hosted ScyllaDB server is a last-resort option and is not a hosted free tier. The key distinction is trial-only: both free paths expire and there is no perpetual free cluster.
- evidence note: First-party pages read on 2026-11-19: the pricing page (trials and billing), the free-trial docs, the quick-start docs (payment prompt), and the account sign-up page (identity gate).
- evidence:
  - [1] 2026-11-19: a 30-day developer free trial runs on smaller instances | capture: sha256:76ec65549a9ca60fd9ba873846569ee07a5cea9987528e17381a1c3b48439d4c | quote: Developer Free Trial: A 30-day trial running on smaller instances (e.g., AWS t3.micro), perfect for exploring the CQL interface and building prototypes.
  - [1] 2026-11-19: a separate 48-hour evaluation of production-grade instances | capture: sha256:76ec65549a9ca60fd9ba873846569ee07a5cea9987528e17381a1c3b48439d4c | quote: Production Evaluation: A 48-hour free trial of production-grade instances.
  - [2] 2026-11-19: one free trial per account, at no cost | capture: sha256:79fcd6968e534ec0f8ae5fe73c272c660b288f9d78d36642f71e173fee32c755 | quote: The ScyllaDB Cloud free trial lets you explore ScyllaDB Cloud at no cost, including ScyllaDB drivers and monitoring. You get one free trial per account.
  - [2] 2026-11-19: the smallest trial node size on AWS | capture: sha256:79fcd6968e534ec0f8ae5fe73c272c660b288f9d78d36642f71e173fee32c755 | quote: AWS — t4g.medium (2 vCPUs, 4 GiB RAM)
  - [3] 2026-11-19: the account sign-up gate requires a company email address | capture: sha256:f452338e1aa3274695b78b0ce7d7e8f19c8f27e67d446449b0bdaf78771be653 | quote: Company Email Only
  - [4] 2026-11-19: payment information is asked only on the regular paid-cluster path, not the free-trial path | capture: sha256:b36a1dc03a32ade67cbec0e0788a8b12aa2ff6cc7c81d79e5cda8a7ec7316bfb | quote: If not already provided, the wizard will prompt you to provide the required payment information.
- sources:
  - [1] https://scylladb.com/pricing
  - [2] https://cloud.docs.scylladb.com/stable/cloud-setup/free-trial.html
  - [3] https://auth.cloud.scylladb.com/oauth/account/sign-up
  - [4] https://cloud.docs.scylladb.com/stable/scylladb-quickstart/index.md
