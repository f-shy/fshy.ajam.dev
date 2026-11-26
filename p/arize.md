# arize ax

> arize.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arize/ | JSON https://fshy.ajam.dev/api/v1/entity/arize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## arize ax / phoenix cloud free tier

- `storage/arize-ax-phoenix-cloud-free-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:55.372Z (live) | stale on 2026-12-04
- url https://arize.com/docs/ax/security-and-settings/pricing-and-usage
- free tier: none reachable: AX Free is 25k spans/month, 1 GB storage and 15-day retention; Pro is 50k spans/month, 10 GB storage and 30-day retention. Spans are telemetry, not objects, and there is no bulk-blob path. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the plan table denominates limits in spans and GB of ingestion and states no per-object size cap | source: [1] | note: not applicable
- retention: AX Free retains traces for 15 days; AX Pro for 30 days. | days: 15 | source: [1]
- egress: stated-absent: the plan table states no egress terms for stored data | metered: no
- identity: email | detail: email: no credit card is required for the AX Free plan; signup is through the join link
- interface: unknown
- interface detail: OpenTelemetry-compliant span ingestion; no S3 or REST object interface stated
- tooling: not documented
- composes with: stated-absent: the plan table lists telemetry spans and storage in GB but no bulk-object chaining; self-hosted deployment is listed only on Enterprise
- reliability: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
  - [2] 2026-10-21: cited as the basis of the rejection: AX Free is 25k spans/month with 1 GB ingestion and 7-15 day retention; Pro is 10 GB/30 days. Spans are telemetry, not objects, and there is no bulk-blob path.
  - [1] 2026-11-19: AX Free is 25k spans, 1 GB and 15 days; Pro is 50k spans, 10 GB and 30 days | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: > | Span volume | Included 25k/month | Included 50k/month | Custom | > | Storage (GB) | 1 GB | 10 GB | Custom | > | Retention | 15 days | 30 days | Custom |
  - [1] 2026-11-19: the first-party plan table states OpenTelemetry-compliant ingestion, not an object API | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: | OpenTelemetry compliant | ✓ | ✓ | ✓ |
  - [1] 2026-11-19: the first-party plan table states 15-day retention on AX Free | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: | Retention | 15 days | 30 days | Custom |
  - [1] 2026-11-19: the plan table states a storage volume in GB, not a per-object cap | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: | Storage (GB) | 1 GB | 10 GB | Custom |
  - [1] 2026-11-19: the free plan is SaaS and self-hosting appears only on Enterprise; no byte-store chaining is stated | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: | Deployment | SaaS | SaaS | SaaS or Self-Hosted |
  - [1] 2026-11-19: the AX Free card states no card is required at signup | capture: sha256:3d3a92ee729f59dab3639d1395537a176c069d9b0fecbb9d49883cbee6505bd4 | quote: No credit card required.
- sources:
  - [1] https://arize.com/docs/ax/security-and-settings/pricing-and-usage
  - [2] https://markaicode.com/pricing/arize-phoenix-pricing/
