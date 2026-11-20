# Faable

> faable.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/faable/ | JSON https://fshy.ajam.dev/api/v1/entity/faable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Faable

- `compute/faable` | qualifies-with-caveat | evidence documented | binding retention-clamped | category platform host
- needs card no, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://faable.com/docs/deploy/pricing
- free tier: Free plan, quoted: 'up to 3 projects per account (2 in your first 48 hours) - apps run on bi.xs (0.6 vCPU - 512 MB) - managed Node, Python and PHP buildpacks only - up to 50 successful deployments per day per project - build artifacts up to 512 MB - 10 GB egress / month included (1 GB / day)'. Idle apps 'scale to zero' after '30 minutes' on Free. Paid Hobby is EUR 15 a month for bi.small '1 vCPU - 1.5 GB' and 'always-on: apps under traffic never sleep'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: a Free app sleeps after 30 minutes idle, and the vendor has announced a mandatory '4 hours out of every 24' rest window that will apply even under traffic. | source: [1]
- egress: Free row: 'apps run on bi.xs (0.6 vCPU - 512 MB)', 'managed Node, Python and PHP buildpacks only', '50 successful deployments per day per project', '10 GB egress / month included (1 GB / day)'… | metered: no | source: [1]
- identity: email | detail: no card: the platform pricing row reads 'Free | 0 EUR | ... no credit card', so no payment method is taken on Free and no hold exists. The signup form's own fields are not described in any evidence row, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: rest
- limits:
  - retention-clamped (binding): a Free app sleeps after 30 minutes idle, and the vendor has announced a mandatory '4 hours out of every 24' rest window that will apply even under traffic. [1]
- limits note: a Free app sleeps after 30 minutes idle, and the vendor has announced a mandatory '4 hours out of every 24' rest window that will apply even under traffic.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free Node, Python or PHP app that tolerates a 30-minute sleep plus an external waker gives a near-continuous endpoint without the EUR 15 Hobby fee; the 1 GB daily egress cap is the wall for anything that serves files.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'one 0.5 CPU / 1 GB RAM instance per project, 10 GB bandwidth, 10 successful deploys per day ... Apps sleep after 2 hours without traffic'. Three of those four claims are wrong against the vendor: the instance is 0.6 vCPU and 512 MB, the deploy cap is 50 a day, and the idle timer is 30 minutes, not 2 hours. Omitted by the aggregator: Dockerfile deploys are paid-only, and external uptime monitors are answered by the platform so they do not keep a Free app awake.
- extras:
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.6
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: Free row: 'apps run on bi.xs (0.6 vCPU - 512 MB)', 'managed Node, Python and PHP buildpacks only', '50 successful deployments per day per project', '10 GB egress / month included (1 GB / day)'…
  - [1] 2026-10-22: 'Idle before it sleeps' table with 'Free | 30 minutes', quoted; and 'An idle app scales to zero and starts again on the next real request'
  - [1] 2026-10-22: 'Coming to the Free plan: a daily rest window. Free apps will be required to sleep for 4 hours out of every 24, including under traffic. This is not in effect yet', quoted
  - [2] 2026-10-22: 'Free | 0 EUR | ... Up to 3 projects per account, 1 free instance, up to 50 successful deployments per day ... no credit card' and 'Hobby | 15 EUR | ... 1 vCPU - 1.5 GB per app', quoted
- sources:
  - [1] https://faable.com/docs/deploy/pricing
  - [2] https://faable.com/docs/platform/pricing
