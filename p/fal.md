# fal

> fal.ai | Compute, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fal/ | JSON https://fshy.ajam.dev/api/v1/entity/fal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## fal Research Grants

- `compute/fal-research-grants` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:43.734Z (live) | stale on 2026-12-04
- url https://fal.ai/grants
- free tier: Free compute on fal's inference platform. The eligibility sentence, quoted: 'The fal Research Grants program is open to anyone passionate about advancing AI through open source projects. [...] No formal degree is required - your ideas and dedication are what matter most.' The page states '$50k' as the 'average grant check' and gives no amount for an individual award. The route is an email to grants@fal.ai with a project description, goals, and 'any relevant work or GitHub repositories'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the award has no published amount, cap, duration or expiry, so the only thing bounding it is a discretionary reply to an email. [1]
- limits note: the award has no published amount, cap, duration or expiry, so the only thing bounding it is a discretionary reply to an email.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The grant is platform credit, so it composes only with fal's own models; it is a supplement for an inference-heavy step, not a training allowance. fal Serverless GPU price list on the pricing page, separate from the grant (whether grant credit applies to Serverless GPUs is not stated): H100 80GB at $4.50/h list price and $2.49/h in the 'As low as' column ($0.00125/s and $0.000692/s), billed per second while a runner is alive, with no minimum bill stated; the page does not say what 'As low as' requires. RTX PRO 6000 96GB, H200, B200, GB200 and B300 are listed; A100, L40S, L4 and GeForce cards are not listed.
- reliability: no reliability event recorded
- notes: Recorded for the door rather than the number, and it is honest to say so: the page states an average grant of $50k and no per-award amount, so the finding ranks only on the average. What makes it worth a line is the explicit removal of the degree requirement in a class where nearly every other program gates on it, plus the fact that the application is an email rather than a form. The page also states $2m in total grants and two named testimonials. Whether the credits are GPU-seconds on fal's inference endpoints or spend on the platform is not stated, and that distinction decides whether a training run is possible at all - it probably is not, which is the caveat.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: 'open to anyone passionate about advancing AI through open source projects'; 'simply reach out to us at grants@fal.ai'; quoted; page 200
  - [1] 2026-10-22: the page publishes no amount, no duration and no expiry; the only evidence of awards is two named testimonials (for the Moondream and BiRefNet projects), which show the program paid out to identifiable people but carry no figure
  - [1] 2026-11-03: the grants page states $50k as the average grant check | capture: sha256:b53f73f61e1cc903b49cf2c28cf3dc9bc613a4a82cf30ceec0019a0f31a701c3 | quote: $50k average grant check
  - [1] 2026-11-03: the grants page shows $2m as the total grants | capture: sha256:b53f73f61e1cc903b49cf2c28cf3dc9bc613a4a82cf30ceec0019a0f31a701c3 | quote: $2m total grants
  - [2] 2026-11-03: the pricing page lists H100 80GB at $4.50/h list and $2.49/h as low as, per second prices $0.00125 and $0.000692 | capture: sha256:d1eee5b9048de2ad1777fae1afd4153b6160815a625b3877b0e8efbe52a1347f | quote: | H100 | 80GB | $4.50/h ($0.00125/s) | $2.49/h ($0.000692/s) |
  - [2] 2026-11-03: fal Serverless GPUs are billed per second while a runner is alive; no minimum bill appears on the page | capture: sha256:d1eee5b9048de2ad1777fae1afd4153b6160815a625b3877b0e8efbe52a1347f | quote: Runners are billed per second while they are alive: in the SETUP, IDLE, RUNNING, DRAINING and TERMINATING states.
  - [1] 2026-11-03: the application route is an email to grants@fal.ai | capture: sha256:b53f73f61e1cc903b49cf2c28cf3dc9bc613a4a82cf30ceec0019a0f31a701c3 | quote: To apply for a fal Research Grant, simply reach out to us at grants@fal.ai.
- sources:
  - [1] https://fal.ai/grants
  - [2] https://fal.ai/pricing

## fal

- `compute/fal` | paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:51.498Z (live) | stale on 2026-11-22
- url https://fal.ai/pricing
- free tier: free tier published without a credit amount | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: per-second and per-token model rates, from $0.007 per 1,000 tokens to $1.20 per million tokens on the rows shown [1]
  - write-gated (binding): no machine to rent and no free tier: the product answers model calls, so capacity is per request [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and carries per-second and per-token model rates. There is no free tier and no machine to rent, so the verdict moves to paid-only on the correct grounds: this is an inference API, not compute
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the unit is a second of generated video or a token; there is no session
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and is a model price table: 'FLUX 3 Max, seconds, $0.085, $0.425' and similar per-second and per-token rates. It prices inference, not machines, and states no free tier
- sources:
  - [1] https://fal.ai/pricing

## fal.ai

- `storage/fal-ai` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fal.ai/pricing
- free tier: none reachable: Same shape as Replicate and worse-documented for storage: the platform is per-second GPU billing for model APIs and Serverless deploys, with a 'fal CDN' for request media that is a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: Same shape as Replicate and worse-documented for storage: the platform is per-second GPU billing for model APIs and Serverless deploys, with a 'fal CDN' for request media that is a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Same shape as Replicate and worse-documented for storage: the platform is per-second GPU billing for model APIs and Serverless deploys, with a 'fal CDN' for request media that is a…
  - [2] 2026-10-21: cited as the basis of the rejection: Same shape as Replicate and worse-documented for storage: the platform is per-second GPU billing for model APIs and Serverless deploys, with a 'fal CDN' for request media that is a retention
- sources:
  - [1] https://fal.ai/pricing
  - [2] https://docs.fal.ai/model-apis/model-endpoints/storage

## fal.ai persistent /data volume

- `storage/fal-ai-persistent-data-volume` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://fal.ai
- free tier: No published byte quota on the /data volume. The docs state only 'Files written to /data persist between requests, across runner restarts, and across deployments' and 'Files you write there persist until you delete them. Runner shutdown does not delete these files.' Capacity is bounded only by what you pay to keep a runner alive; there is no free storage allowance and no documented ceiling. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 GB per file | bytes: 100000000000 | source: [1] | note: not stated
- retention: No published byte quota on the /data volume. The docs state only 'Files written to /data persist between requests, across runner restarts, and across deployments' and 'Files you write there persist until you delete them. | source: [1] | note: not stated
- egress: NOT free and NOT anonymous: '/data' files are 'not URL-accessible'. There is no public download URL, so the egress question does not arise. Bulk in/out is via `fal files` CLI or the REST storage API. | metered: no
- identity: email
- interface: rest, cli
- limits:
  - per-object-cap (binding): 100 GB per file [1]
  - write-gated: approval (request at fal [1]
- limits note: Per-object-cap is upload-method-dependent (this is the useful part): `fal files upload` CLI ~100 GB per file (10 MB parts, max 10,000 parts); dashboard drag-and-drop 1 GB; upload-from-URL 5 GB and must complete in 10 minutes; POST /serverless/files/file/local/{path} ~4.5 MB per request; writes from inside a running app are exempt ('Not subject to these limits. The runner writes straight to the volume'). Retention: indefinite, self-managed. Billing: you are billed per second for every runner state except PENDING, DOCKER_PULL and TERMINATED. SETUP and IDLE are both billed, so holding storage open costs GPU-time.
- interface detail: rest
- tooling: `fal` Python CLI (`fal files upload/download/list/remove`), @fal-ai/client JS storage API, `fal.download_file(url, target_dir='/data/...')` in-app. Chunked at 4 MB into a global object store; parallel reads hit a distributed cache (docs claim 6-8 GB/s distributed, 10-15 GB/s local NVMe).
- composes with: Storage is tied to paid compute workloads rather than standalone storage. Serverless deployments require approved account access and compute runtime fees apply.
- reliability: Serverless access is gated by per-account approval (request at fal.ai/dashboard/serverless-get-started), so this is not a self-serve multiplier. Docs warn that streaming a multi-GB artifact in small chunks to /data is much slower than one bulk copy.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: No published byte quota on the /data volume — the docs state only 'Files written to /data persist between requests, across runner restarts, and across deployments' and 'Files you write there persist until you delete them. Runner shutdown does not delete these files.' Capacity is bounded only by what you pay to keep a runner alive; there is no free storage allowance and no documented ceiling.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Files written to /data persist between requests, across runner restarts, and across deployments'; no quota stated
  - [2] 2026-10-21: upload size table: CLI ~100 GB, dashboard 1 GB, from-URL 5 GB/10 min, local API ~4.5 MB
  - [3] 2026-10-21: billed states table (SETUP/IDLE/RUNNING billed; PENDING/DOCKER_PULL not)
- sources:
  - [1] https://fal.ai/docs/documentation/development/use-persistent-storage
  - [2] https://fal.ai/docs/documentation/development/file-storage
  - [3] https://fal.ai/docs/documentation/serverless/pricing
