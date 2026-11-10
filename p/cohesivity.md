# Cohesivity

> cohesivity.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cohesivity/ | JSON https://fshy.ajam.dev/api/v1/entity/cohesivity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cohesivity

- `compute/cohesivity` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T11:01:15.546Z (live) | stale on 2026-12-05
- url https://cohesivity.ai/offerings/railway-hosting
- free tier: Free tier is a metered monthly bucket on hosting Cohesivity provisions inside its own Railway account. Quoted for a claimed Free account: 'projects: 10 max total', 'deploys: 60 per month', 'uploaded bytes: 2 GB per month', 'vCPU-seconds: 100000 per month', 'memory GB-seconds: 400000 per month', 'egress bytes: 5 GB per month', with the compute shape 'Claimed Free: 0.5 vCPU, 1 GB RAM, 1 replica, sleep enabled'. An unclaimed ephemeral tenant needs no signup at all and lasts 72 hours with 50,000 vCPU-seconds. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: monthly-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Claimed Free bucket: 'projects: 10 max total', 'deploys: 60 per month', 'vCPU-seconds: 100000 per month', 'memory GB-seconds: 400000 per month', 'egress bytes: 5 GB per month', quoted | metered: no | free allowance: 5 GB per month (claimed Free) | price per TB: not published as a per-TB figure: claimed overage auto-purchases fluid blocks at Railway's published rates plus 10% | source: [1]
- identity: email | detail: anonymous for the ephemeral lane: 'the quickstart mints the ephemeral tenant with no signup and no payment ... the tenant self-expires in 72 hours under hard caps', so no identity is checked there. The claimed Free bucket is a different lane and the evidence does not say what claiming it requires - email, phone or card: unknown. No hold is stated, and no card is needed to keep an app up: 'claimed overage draws from fluid at provider cost plus 10%' and 'Hosting is never deleted for non-payment'.
- interface: rest
- limits:
  - volume-quota (binding): 100,000 vCPU-seconds a month is 27.8 vCPU-hours, so at the 0.5 vCPU cap the bucket buys about 55 hours of running time a month, while the 400,000 GB-seconds buys 111 hours at 1 GB, so the CPU bucket runs out first. [1]
- limits note: 100,000 vCPU-seconds a month is 27.8 vCPU-hours, so at the 0.5 vCPU cap the bucket buys about 55 hours of running time a month, while the 400,000 GB-seconds buys 111 hours at 1 GB, so the CPU bucket runs out first.
- binding note: the same as limits note
- interface detail: HTTP API, per the offering page: "POST `multipart/form-data` to `/api/railway/deploy`: each project file is a `files` part."
- tooling: curl requests, per the offering page: "curl -s -X POST https://cohesivity.ai/api/resources/railway-hosting"
- composes with: the tenant is created by the agent rather than by a person, so one session can provision hosting, Postgres and a Redis-compatible cache and hand over an approval link only if the result is worth keeping; that composes with a planner running on another free tier.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says the free tier includes '10 projects, 100K edge requests, 10 GB object storage, 100 emails, and 5 USD/month in credits'. The project count matches; the vCPU and memory buckets, the 60-deploy monthly cap and the 0.5 vCPU / 1 GB shape are on the offering page and absent from the aggregator. Railway's own free trial is gone, so this is one of the few remaining routes to Railway compute at no cost, and it holds the account rather than the user: 'Cohesivity creates and owns the Railway project/service/environment/domain'.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: monthly-allowance
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 1
- evidence:
  - [1] 2026-10-22: 'Claimed Free: 0.5 vCPU, 1 GB RAM, 1 replica, sleep enabled', quoted
  - [1] 2026-10-22: Claimed Free bucket: 'projects: 10 max total', 'deploys: 60 per month', 'vCPU-seconds: 100000 per month', 'memory GB-seconds: 400000 per month', 'egress bytes: 5 GB per month', quoted
  - [1] 2026-10-22: overage and pause behaviour: 'claimed overage draws from fluid at provider cost plus 10%' and 'Hosting is never deleted for non-payment', quoted
  - [2] 2026-10-22: 'the quickstart mints the ephemeral tenant with no signup and no payment ... the tenant self-expires in 72 hours under hard caps', quoted
  - [1] 2026-11-03: the claimed Free bucket includes 5 GB of egress a month | capture: sha256:c3e1db18186adfeb67a2106899acb09126c46a863517142865b905e85e69fa94 | quote: - egress bytes: 5 GB per month
  - [1] 2026-11-03: overage is bought at Railway's rates plus 10%, with no per-TB figure on the page | capture: sha256:c3e1db18186adfeb67a2106899acb09126c46a863517142865b905e85e69fa94 | quote: Claimed overage auto-purchases fluid blocks at Railway's published rates plus 10%.
  - [1] 2026-11-03: deploys go through an HTTP API | capture: sha256:c3e1db18186adfeb67a2106899acb09126c46a863517142865b905e85e69fa94 | quote: POST `multipart/form-data` to `/api/railway/deploy`: each project file is a `files` part.
  - [1] 2026-11-04: the page documents a deploy endpoint | capture: sha256:c3e1db18186adfeb67a2106899acb09126c46a863517142865b905e85e69fa94 | quote: POST `multipart/form-data` to `/api/railway/deploy`: each project file is a `files` part.
  - [1] 2026-11-04: the page shows a curl request to the provisioning endpoint | capture: sha256:c3e1db18186adfeb67a2106899acb09126c46a863517142865b905e85e69fa94 | quote: curl -s -X POST https://cohesivity.ai/api/resources/railway-hosting
- sources:
  - [1] https://cohesivity.ai/offerings/railway-hosting
  - [2] https://cohesivity.ai/llms.txt
