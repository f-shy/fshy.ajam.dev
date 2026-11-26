# velixir

> velixir.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/velixir/ | JSON https://fshy.ajam.dev/api/v1/entity/velixir.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## velixir

- `compute/velixir` | qualifies-with-caveat | evidence documented | binding retention-clamped | category platform host
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T02:24:26.167Z (live) | stale on 2026-12-05
- url https://velixir.net/pricing
- free tier: Free plan, quoted: '0.25 vCPU', '256 MB RAM', '1 GB Disk', 'Isolated compute', 'Wakes on the next request', '1 deployment slot per app', 'Custom domains'. The app 'sleeps when idle' and there is 'No card to deploy'. Paid Hobby is 'EUR 3.49 /mo per replica' for 0.5 vCPU, 512 MB RAM and 5 GB disk; a EUR 14.99 credit follows when a payment method is added. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: the free app sleeps when idle and wakes on the next request, so a cold start of seconds sits in front of the first request after every idle period. | source: [1]
- egress: Bandwidth is unmetered: no egress fees and no per-GB data-transfer meter; a soft fair-use guideline of around 10 TB of outbound per app per month is not a charge | metered: no | free allowance: unmetered; soft fair-use guideline of around 10 TB outbound per app per month | source: [2]
- identity: email | detail: no card: the homepage states 'Your first app sleeps when idle and wakes on the next request, so keeping it live costs nothing. No card to deploy.', so no payment method is taken to deploy and no hold exists; the EUR 14.99 credit follows only when a payment method is added. The signup form's own fields are not described, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: rest, cli
- limits:
  - retention-clamped (binding): the free app sleeps when idle and wakes on the next request, so a cold start of seconds sits in front of the first request after every idle period. [1]
- limits note: the free app sleeps when idle and wakes on the next request, so a cold start of seconds sits in front of the first request after every idle period.
- binding note: the same as limits note
- interface detail: REST API with an OpenAPI document and X-Api-Key header; the velixir CLI installs as a standalone binary or a.NET global tool; no SSH or SDK documented on the pages read
- tooling: the velixir CLI (login, deploy, apps, env, db, cache, volume, access-logs) and a REST API with API keys
- composes with: a free 0.25 vCPU app that serves an API and a cron trigger costs nothing while idle, and the EUR 3.49 Hobby replica is the smallest paid step when a second always-on process is needed.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'one app (0.25 vCPU, 256 MB RAM) that sleeps when idle, custom domains with TLS, and no credit card'. The vendor matches, so the gap is zero. Omitted by the aggregator: the 1 GB disk, the one-deployment-slot limit per app, and the EUR 3.49 paid floor. Region is fixed to EU Central by policy, not by a setting the user changes.
- extras:
  - facets.class: aggregator-confirmed
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.25
  - facets.shape.ram_gib: 0.25
- evidence:
  - [1] 2026-10-22: Free column: '0.25 vCPU', '256 MB RAM', '1 GB Disk', 'Isolated compute', 'Wakes on the next request', quoted
  - [1] 2026-10-22: 'Hobby EUR 3.49 /mo per replica' with '0.5 vCPU', '512 MB RAM', '5 GB Disk', quoted
  - [3] 2026-10-22: 'Your first app sleeps when idle and wakes on the next request, so keeping it live costs nothing. No card to deploy.', quoted
  - [2] 2026-11-03: no egress fee and no per-GB meter | capture: sha256:0edb2c5ad8b97a92a9c1ebe37735ca39027d9b32c6163ec53b6fe1fa1e15c9b7 | quote: Bandwidth is unmetered: there are no egress fees and no per-GB data-transfer meter, so inbound and outbound traffic are both free of usage charges.
  - [2] 2026-11-03: soft fair-use guideline about 10 TB outbound per app per month, not billed | capture: sha256:0edb2c5ad8b97a92a9c1ebe37735ca39027d9b32c6163ec53b6fe1fa1e15c9b7 | quote: There's a soft fair-use guideline of around 10 TB of outbound per app per month, there to keep one workload from crowding out shared capacity, not to bill you.
  - [4] 2026-11-03: a CLI exists and is the main deploy path | capture: sha256:1c3eefb6313d0a42d6c3a378003ee563b32a8253a74da8e16648474499a5a0a2 | quote: `velixir` is the canonical way to ship code to velixir.
  - [5] 2026-11-03: a public REST API with API keys exists | capture: sha256:262dfca406e75d8ff0c4ba7fdf731c622b1c161e8fd038caf98580da5a4b988a | quote: The velixir public API. Manage apps, deployments, databases, caches, and projects programmatically.
- sources:
  - [1] https://velixir.net/pricing
  - [2] https://velixir.net/docs/billing
  - [3] https://velixir.net/
  - [4] https://velixir.net/docs/cli
  - [5] https://velixir.net/docs/api
