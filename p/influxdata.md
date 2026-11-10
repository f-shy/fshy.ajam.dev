# InfluxDB Cloud Serverless

> influxdata.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/influxdata/ | JSON https://fshy.ajam.dev/api/v1/entity/influxdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InfluxDB Cloud Serverless

- `compute/influxdb-cloud-serverless` | qualifies-with-caveat | evidence documented | binding request-rate | category managed database
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:19:14.181Z (live) | stale on 2026-12-05
- url https://www.influxdata.com/influxdb-pricing/
- free tier: Two offers on one page. The Free Plan, quoted from the docs: 'New InfluxDB Cloud Serverless accounts start with the Free Plan that provides a limited number of resources and data usage' with 'Data-in: Rate of 5 MB per 5 minutes (average of 17 kb/s)', 'HTTP response payload rate: 300 MB data per 5 minutes', '2 buckets', and '30 days of data retention'. The paid path adds 'a $250 credit for 30 days upon upgrade'. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card: the pricing page lists 'No credit card required' beside the Cloud Serverless offer, and the sign-up docs limit a Free Plan user to one organization. No hold exists because no payment method is taken for the free plan. The signup fields are not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: unknown
- limits:
  - request-rate (binding): the ingest rate is the ceiling, not a volume: 5 MB per 5 minutes is about 1.4 GiB a day and cannot be burst, so a backfill of historical measurements fails at the rate limit even though the plan has no monthly volume cap. [1]
- limits note: the ingest rate is the ceiling, not a volume: 5 MB per 5 minutes is about 1.4 GiB a day and cannot be burst, so a backfill of historical measurements fails at the rate limit even though the plan has no monthly volume cap.
- binding note: the same as limits note
- interface detail: HTTP API (v2-compatible /api/v2/write for writes, v1-compatible /query for InfluxQL) and Flight+gRPC clients for SQL and InfluxQL queries
- tooling: Flight+gRPC clients for SQL and InfluxQL queries and the HTTP API for writes; the API reference page names no client library
- composes with: a perpetual 30-day-retention time series with 2 buckets is the metrics sink for a free-tier application estate, and 17 kb/s is enough for a few hundred gauges at scrape intervals of a minute.
- reliability: no reliability event recorded
- notes: The page advertises the USD 250 credit prominently and buries the perpetual Free Plan in the docs, which inverts the usual pattern and is notable. Retention is 30 days, so this cannot hold history. The vendor states the rate limits suit 5 to 10 sensors.
- extras:
  - facets.class: timeseries-free-tier
  - facets.free_tier_kind: perpetual-free
- evidence:
  - [2] 2026-10-22: Free Plan: 'Data-in: Rate of 5 MB per 5 minutes (average of 17 kb/s)', 'HTTP response payload rate: 300 MB data per 5 minutes', '2 buckets', '30 days of data retention', quoted
  - [1] 2026-10-22: Cloud Serverless lists '- $250 free credit to start', 'No minimum commitment', 'Multi-tenant - Service quotas apply - No HA' and 'No credit card required', quoted
  - [3] 2026-10-22: 'Use it as much and as long as you like within the plan rate-limits. Limits are designed to let you monitor 5-10 sensors, stacks or servers comfortably. Users on the Free Plan are limited to one organization.', quoted
  - [4] 2026-11-04: the documented query interfaces are HTTP /query and Flight+gRPC | capture: sha256:35f17a7e583d3788802a6f2c06690a62cab72efcd8d2e259bf6720e7d0c1165a | quote: Query data stored in InfluxDB 3 Cloud Serverless using InfluxQL via the v1-compatible `/query` endpoint, or using SQL and InfluxQL via Flight+gRPC clients.
  - [4] 2026-11-04: clients are Flight+gRPC, none named | capture: sha256:35f17a7e583d3788802a6f2c06690a62cab72efcd8d2e259bf6720e7d0c1165a | quote: Query data stored in InfluxDB 3 Cloud Serverless using InfluxQL via the v1-compatible `/query` endpoint, or using SQL and InfluxQL via Flight+gRPC clients.
- sources:
  - [1] https://www.influxdata.com/influxdb-pricing/
  - [2] https://docs.influxdata.com/influxdb3/cloud-serverless/admin/billing/limits/
  - [3] https://docs.influxdata.com/influxdb3/cloud-serverless/sign-up/
  - [4] https://docs.influxdata.com/influxdb3/cloud-serverless/reference/api/
