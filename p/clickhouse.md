# ClickHouse Cloud

> clickhouse.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clickhouse/ | JSON https://fshy.ajam.dev/api/v1/entity/clickhouse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ClickHouse Cloud

- `compute/clickhouse-cloud` | trial-only | evidence documented | binding volume-quota | category managed database
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:20:54.117Z (live) | stale on 2026-12-05
- url https://clickhouse.com/pricing
- free tier: Pricing page, quoted: 'Start free with $300 in credits for 30 days' and, in the FAQ, 'ClickHouse Cloud starts with $300 in credits over 30 days, no credit card required. ClickHouse open source is free forever.' The page adds: 'The trial ends after 30 days or once the credits are consumed, whichever comes first; the account then converts to pay-as-you-go.' Trial credits expire at the end of the 30-day trial period, even after a payment method has been added. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: egress is billed per GB and varies by region (public internet USD 0.115 per GB in AWS us-east-1); ingress is not charged; no free egress allowance is published on the pricing page | metered: no | source: [1]
- identity: email | detail: the pricing FAQ states no credit card is required; the signup console is JavaScript-only and was not exercised, so the gate is the vendor's sentence and not a completed signup
- interface: unknown
- limits:
  - volume-quota (binding): the 30-day clock ends the free window before the USD 300 does for an idle service, because compute scales to zero when the service is idle; a service left running continuously for the 30 days is about 732 compute-unit-hours and the USD 300 has to cover those plus storage, backups and egress. [1]
- limits note: the 30-day clock ends the free window before the USD 300 does for an idle service, because compute scales to zero when the service is idle; a service left running continuously for the 30 days is about 732 compute-unit-hours and the USD 300 has to cover those plus storage, backups and egress.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 300 of ClickHouse time is the cheapest route to scanning a multi-hundred-gigabyte corpus once; the same query then re-runs on the free open-source binary on rented compute, because the SQL is identical.
- reliability: no reliability event recorded
- notes: Compute scales to zero when idle, which stretches the credit if the service is not left running. Single-replica services are limited to 8 to 12 GiB of memory. Compute is billed per compute-unit-hour at a region-specific rate where 1 compute unit is 8 GiB RAM and 2 vCPU, and the page lists a separate rate per instance family, so no single per-hour figure is quoted here. No probe was run.
- extras:
  - facets.class: analytics-trial-credit
  - facets.free_tier_kind: trial-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 8
- evidence:
  - [1] 2026-10-22: 'Start free with $300 in credits for 30 days' and 'The trial ends after 30 days or once the credits are consumed, whichever comes first; the account then converts to pay-as-you-go', quoted
  - [1] 2026-10-22: FAQ: 'ClickHouse Cloud starts with $300 in credits over 30 days, no credit card required. ClickHouse open source is free forever.', quoted
  - [1] 2026-10-22: Basic plan includes 'Up to 1 TB storage', '8-12 GiB total memory', '1 availability zone', backups every 24h retained for 1 day
  - [2] 2026-10-23: 'Trial credits expire at the end of the 30-day trial period, even after a payment method has been added.', quoted; the pricing page states 'Start free with $300 in credits for 30 days'
  - [1] 2026-11-04: public internet egress in AWS us-east-1 is USD 0.115 per GB | capture: sha256:f9c3a0bbd02118b53605d22b1e337b92c20176a533e59f25168c3877eb500d80 | quote: | AWS | us-east-1 | $0.115 | $0.031 |
  - [1] 2026-11-04: egress is billed per GB and varies by region; ingress is not charged | capture: sha256:f9c3a0bbd02118b53605d22b1e337b92c20176a533e59f25168c3877eb500d80 | quote: _Egress is billed per GB and varies by region. Ingress is not charged. Inter-region is billed on the source region's rate._
- sources:
  - [1] https://clickhouse.com/pricing
  - [2] https://clickhouse.com/docs/cloud/manage/billing
