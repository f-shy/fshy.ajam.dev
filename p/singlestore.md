# SingleStore

> singlestore.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/singlestore/ | JSON https://fshy.ajam.dev/api/v1/entity/singlestore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SingleStore

- `compute/singlestore` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:57.261Z (live) | stale on 2026-12-05
- url https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/about-singlestore-helios/singlestore-helios-editions/shared-edition/
- free tier: Shared Edition, quoted: 'SingleStore provides a free entry point to get started with SingleStore Helios for low-throughput and prototype applications.' Limits table: 'Data Size | 1 GB of compressed data. SingleStore typically sees 75% compression on average', 'Number of Tables per Database | 10', 'Number of Databases per Shared Cluster | 1', and 'Number of Shared Clusters | Unlimited.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - per-object-cap (binding): 1 GB of compressed data per cluster fails first, but 10 tables per database is the constraint a schema hits sooner; unlimited clusters per organization is the workaround and it partitions the data by hand. [1]
- limits note: 1 GB of compressed data per cluster fails first, but 10 tables per database is the constraint a schema hits sooner; unlimited clusters per organization is the workaround and it partitions the data by hand.
- binding note: the same as limits note
- interface detail: MySQL client and SingleStore Endpoints as command line clients, plus an HTTP Data API, reached from the Cloud Portal Connect menu; documented at docs.singlestore.com/cloud/getting-started-with-singlestore-helios/
- tooling: MySQL client, SingleStore Endpoints, the SingleStore Python client, Node.js, Ruby on Rails, Perl and Java/JDBC connectors, and the HTTP Data API
- composes with: unlimited Shared clusters per organization turns a 1 GB per-cluster cap into an N-times-1 GB allowance if the schema can be partitioned, which no other free tier among documented hosts allows.
- reliability: no reliability event recorded
- notes: CREATE DATABASE and DROP DATABASE are disabled on Shared clusters, so a schema change means terminating and rebuilding the cluster. Shared clusters are reachable from anywhere with no firewall configuration and are stated as not for production. The pricing page no longer prints a free plan card, so the docs are the only current source.
- extras:
  - facets.class: sql-free-tier
  - facets.free_tier_kind: perpetual-free
  - facets.shape.disk_gib: 4
- evidence:
  - [1] 2026-10-22: 'Data Size | 1 GB of compressed data', '# of Tables per Database | 10', '# of Databases per Shared Cluster | 1', '# of Shared Clusters | Unlimited', quoted
  - [2] 2026-10-22: 'SingleStore allows you to build your applications for free with the Free Shared Edition ... The Free Shared Edition offers a free Shared cluster with one attached database', quoted
  - [2] 2026-11-03: an HTTP Data API is a connection route | capture: sha256:a5c7fc9f1648e4119a2c0d347f5bd03a9a7b00b2bb1b8c321cc019e4c830631c | quote: | HTTP | Select Your App > HTTP. Refer to [Data API](https://docs.singlestore.com/cloud/reference/data-api/) for more information. |
  - [2] 2026-11-03: a MySQL command line client is a connection route | capture: sha256:a5c7fc9f1648e4119a2c0d347f5bd03a9a7b00b2bb1b8c321cc019e4c830631c | quote: | MySQL Client | Select CLI Client > MySQL Client. Refer to [Connect with MySQL Client](https://docs.singlestore.com/cloud/connect-to-singlestore/connect-with-mysql/connect-with-mysql-client/) for more information. |
  - [2] 2026-11-04: an HTTP Data API is documented as a connection route | capture: sha256:a5c7fc9f1648e4119a2c0d347f5bd03a9a7b00b2bb1b8c321cc019e4c830631c | quote: | HTTP | Select Your App > HTTP. Refer to [Data API](https://docs.singlestore.com/cloud/reference/data-api/) for more information. |
  - [2] 2026-11-04: the page lists MySQL Client as a CLI client route | capture: sha256:a5c7fc9f1648e4119a2c0d347f5bd03a9a7b00b2bb1b8c321cc019e4c830631c | quote: | MySQL Client | Select CLI Client > MySQL Client.
- sources:
  - [1] https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/about-singlestore-helios/singlestore-helios-editions/shared-edition/
  - [2] https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/
