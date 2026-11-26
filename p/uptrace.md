# Uptrace Cloud

> uptrace.dev | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uptrace/ | JSON https://fshy.ajam.dev/api/v1/entity/uptrace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Uptrace Cloud

- `databases-kv/uptrace-cloud` | qualifies | evidence documented | binding volume-quota | category managed OpenTelemetry traces, metrics and logs (observability database on ClickHouse) | tier Cloud Free / pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:18.052Z (live) | stale on 2026-12-20
- url https://uptrace.dev/pricing
- free tier: Uptrace Cloud is free up to 50 GB and 5,000 timeseries per month, then from $0.075/GB with automatic volume discounts; unlimited users, services and hosts. A separate free trial offers 1 TB of storage and 100,000 timeseries with no card required. | unit: GB | metered on: uploaded-bytes | read on: 2026-11-19 | source: [1] | note: The ongoing free allowance is 50 GB per month and 5,000 timeseries; the 1 TB / 100,000-timeseries figure is a signup trial. Metrics are billed per million ingested datapoints from $0.025 per 1M.
- per-object cap: unverified: no single-object cap is published; the free Cloud allowance is 50 GB per month of ingested spans/logs plus 5,000 timeseries, which are volume quotas rather than a per-object cap. | source: [1]
- retention: Uptrace Cloud keeps all data for 4 weeks (28 days) by default; longer cold storage on S3 or HDD is available for up to 100 weeks at $0.01 per GB-month for spans and $0.20 per 1,000 timeseries-month for metrics. | days: 28 | source: [1] | note: 28 days is the default retention; it can be extended via paid cold storage.
- egress: Sending data from AWS or GCP incurs outbound fees; the vendor says OTel Arrow cuts bandwidth 30-70% versus standard OTLP and compresses telemetry 15-30x. Ingestion above the free allowance is charged per GB, not egress from Uptrace. | metered: no | free allowance: 50 GB per month included | source: [1]
- identity: email | detail: Cloud signup is a free account with no card required for the trial; billing is handled by Paddle by credit card or bank transfer after signup. A public live demo can be explored without any account.
- interface: rest, cli, browser, chat
- limits:
  - volume-quota (binding): 50 GB free per month and 5,000 timeseries per month on Uptrace Cloud Free; beyond that from $0.075/GB [1]
  - request-rate: Metrics billing starts at $0.025 per 1M ingested datapoints and decreases with volume; minimum supported collection interval is 10 seconds [1]
  - retention-clamped: default retention 4 weeks (28 days); longer storage only via paid cold storage up to 100 weeks [1]
- binding note: The 50 GB/month and 5,000-timeseries free allowance is the first ceiling a free user hits; retention is a fixed 28-day default and per-object caps are not published.
- interface detail: OpenTelemetry OTLP ingest for traces, metrics and logs; Prometheus, Vector, FluentBit and CloudWatch ingest; a built-in MCP server queryable from AI assistants using the existing Uptrace session token; UQL and PromQL-compatible query engines and a web UI.
- tooling: OpenTelemetry SDKs and Collector, Prometheus, Vector, FluentBit, Grafana data-source support; the self-hosted Community Edition that the user installs and runs is the last resort
- composes with: A hosted Uptrace Cloud endpoint takes OTLP telemetry from existing OpenTelemetry instrumentation; self-hosting the AGPL Community Edition on a rented or free machine is the last-resort path when the hosted free allowance is insufficient.
- reliability: Cloud data is stored in Hetzner's Germany datacenters with backups in Finland; 99.9% uptime is listed. Sending from AWS or GCP incurs outbound fees; dropped sampled data costs $0.01 per GB.
- notes: Uptrace Cloud has a genuine ongoing free tier of 50 GB and 5,000 timeseries per month with no card, plus a separate 1 TB / 100k-timeseries signup trial. Paid usage starts at $0.075/GB and data is kept 28 days by default. Self-hosted Community Edition is the last resort, not the offer this record describes.
- evidence note: All stated values come from first-party Uptrace pricing, homepage and signup pages captured on 2026-11-19. The exact signup form fields were not visible in the browser capture and identity is recorded at the level the page shows.
- self hosted: no
- evidence:
  - [1] 2026-11-19: the ongoing Cloud free allowance is 50 GB and 5,000 timeseries per month | capture: sha256:971121d569512a0e178fa4a527c31bb5a02ac239638b5528f3682ce7ad74406b | quote: Or use Uptrace Cloud free up to 50 GB and 5,000 timeseries per month.
  - [1] 2026-11-19: metrics are billed from $0.025 per million datapoints | capture: sha256:971121d569512a0e178fa4a527c31bb5a02ac239638b5528f3682ce7ad74406b | quote: The rate starts at $0.025 per 1M datapoints and decreases with volume.
  - [1] 2026-11-19: default Cloud retention is 28 days | capture: sha256:971121d569512a0e178fa4a527c31bb5a02ac239638b5528f3682ce7ad74406b | quote: Uptrace Cloud keeps all data for 4 weeks (28 days) by default.
  - [1] 2026-11-19: ingest from other clouds incurs outbound fees | capture: sha256:971121d569512a0e178fa4a527c31bb5a02ac239638b5528f3682ce7ad74406b | quote: Sending from AWS or GCP? Outbound fees apply, but observability data compresses well.
  - [2] 2026-11-19: the signup trial offers 1 TB and 100k timeseries with no card | capture: sha256:b7b4c65a3ec8659e1d7d4a36253cd0311b1867beb0452bc3aa05b4540c722713 | quote: 1TB free storage and 100k timeseries No card required
  - [3] 2026-11-19: the Cloud signup page states the 1 TB / 100k-timeseries trial with a free account | capture: sha256:c98f60fb5f3adbf38df4d6ae27b06390eb378d7a93237dcc85cd34254eaae8eb | quote: Sign up for a free account and get 1TB of storage and 100,000 timeseries.
- sources:
  - [1] https://uptrace.dev/pricing
  - [2] https://uptrace.dev/
  - [3] https://app.uptrace.dev/join
