# Spice.ai Cloud

> spice.ai | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spice/ | JSON https://fshy.ajam.dev/api/v1/entity/spice.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## spice.ai

- `storage/spice-ai-see-candidate-entry` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://spice.ai/pricing
- free tier: none reachable: The free tier is an Apache-2.0 runtime you host yourself. There are no free hosted bytes; the 'free datasets' are Spice's own samples, read-only. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: The free tier is an Apache-2.0 runtime you host yourself. There are no free hosted bytes; the 'free datasets' are Spice's own samples, read-only.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The free tier is an Apache-2.0 runtime you host yourself. There are no free hosted bytes; the 'free datasets' are Spice's own samples, read-only.
- sources:
  - [1] https://spice.ai/pricing

## Spice.ai Cloud (Community Edition)

- `storage/spice-ai-cloud` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category data-platform
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://spice.ai/pricing
- free tier: No storage quota published, because the product is not storage. The free Community edition is the self-hosted OSS runtime under Apache 2.0 with community-only support; the hosted Cloud tier is 'subscription and usage-based pricing with tiered plans'. The datasets it serves are 'free, ready-to-query sample datasets' hosted by Spice, not by you. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Usage-based on Cloud; unmetered only if you self-host and pay your own egress. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: fails-quota: no free hosted bytes at all. Per-app request rate limits exist on Cloud per the management API docs.
- interface detail: rest
- tooling: A SQL query endpoint over the Spice runtime, and a Data Connector model that federates to external sources. Self-hosting gives full control but on your own hardware.
- composes with: None for capacity. The free tier is software, so the bytes land wherever you point it (S3, GCS, local). It is a query layer, and a useful one, but it multiplies nothing.
- reliability: Service provides analytical data infrastructure and query endpoints rather than general raw object storage.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: No storage quota published, because the product is not storage. The free Community edition is the self-hosted OSS runtime under Apache 2.0 with community-only support; the hosted Cloud tier is 'subscription and usage-based pricing with tiered plans'. The datasets it serves are 'free, ready-to-query sample datasets' hosted by Spice, not by you.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: opened: 'Free under Apache 2.0 with community-only support' (OSS) / 'Subscription and usage-based pricing with tiered plans' (Cloud) / Enterprise licensing; 'Single-node engine' for Community vs 'Multi-node with clustering' for Cloud.
  - [2] 2026-10-21: surfaced: 'The Spice.ai Cloud Platform includes a comprehensive set of free, ready-to-query sample datasets' — read-only samples, not user hosting.
  - [3] 2026-10-21: surfaced: 'Spice.ai OSS — the open-source Spice runtime. Self-hosted, free, Apache 2.0.'
- sources:
  - [1] https://spice.ai/pricing
  - [2] https://spiceai.org/docs/getting-started/spiceai
  - [3] https://spice.ai/docs/faq
