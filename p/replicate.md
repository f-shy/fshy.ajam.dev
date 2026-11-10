# Replicate

> replicate.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/replicate/ | JSON https://fshy.ajam.dev/api/v1/entity/replicate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Replicate

- `compute/replicate` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:47.926Z (live) | stale on 2026-11-22
- url https://replicate.com/pricing
- free tier: no free tier: hardware bills per second from $0.09 an hour for small CPU to $5.49 an hour for an H100, and a fast-booting fine-tune is billed only while it processes a request | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): per-second billing from $0.09 an hour for CPU Small to $40.32 an hour for eight A100s [1]
  - retention-clamped: a fast-booting fine-tune bills only while it is processing; other private models bill for idle time [1]
  - per-object-cap: multi-GPU A100 and H100 capacity beyond two GPUs requires a committed-spend contract [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the full hardware ladder with per-second rates and the idle-billing rule. There is no free tier on it, so the verdict moves to…
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 8
  - shape.gpu_count: 1
  - shape.note: CPU Small is 1x CPU and 2 GB at $0.09; an H100 is 13x CPU, 144 GB of RAM and 80 GB of VRAM at $5.49
  - session_cap.restart_required: no
  - session_cap.note: a fast-booting fine-tune stops billing between requests; the page contrasts this with models that bill for idle time
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'You'll only be billed for the time the model is active and processing your requests, so you won't pay for idle time' with the hardware ladder: 'CPU (Small) $0.09/hr', 'Nvidia T4 $0.81/hr', 'Nvidia L40S $3.51/hr', 'Nvidia A100 (80GB) $5.04/hr', 'Nvidia H100 $5.49/hr', quoted
- sources:
  - [1] https://replicate.com/pricing

## replicate (model hosting)

- `storage/replicate-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://replicate.com/docs/topics/predictions/output-files
- disagrees on identity_kind: `storage/replicate` says institution, `storage/replicate-2` says email
- free tier: none reachable: Output files are ephemeral by design: 'output files are automatically deleted after an hour' for API-created predictions, and replicate.delivery URLs 'expire after one hour'. Custom models… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Output files are ephemeral by design: 'output files are automatically deleted after an hour' for API-created predictions, and replicate.delivery URLs 'expire after one hour'. Custom models…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Output files are ephemeral by design: 'output files are automatically deleted after an hour' for API-created predictions, and replicate.delivery URLs 'expire after one hour'. Custom models…
  - [2] 2026-10-21: cited as the basis of the rejection: Output files are ephemeral by design: 'output files are automatically deleted after an hour' for API-created predictions, and replicate.delivery URLs 'expire after one hour'. Custom models a
- sources:
  - [1] https://replicate.com/docs/topics/predictions/output-files
  - [2] https://replicate.com/pricing

## Replicate (r8.im + Files API)

- `storage/replicate` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://replicate.com
- disagrees on identity_kind: `storage/replicate` says institution, `storage/replicate-2` says email
- free tier: Files API is a workspace scratch space with no advertised total; documented behaviour is expiry, not quota. r8.im is a private-ish OCI registry for cog models. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Per-prediction output files are served from Replicate's CDN, but only for the retention window. | metered: no
- identity: institution
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap 100 MB [1]
- limits note: per-object-cap 100 MB via the client library ('This will work for files up to 100MB'); data-URI path recommended only <1 MB. Retention is the killer: 'For predictions created through the API, all input parameters, output values, output files, and logs are automatically removed after an hour, by default.' Files API objects carry an explicit `expires_at`.
- interface detail: rest
- tooling: `cog push r8.im/<owner>/<model>`, replicate-python Files API (files.create/list/get/delete).
- composes with: No viable chain: 100 MB per object x 1-hour retention. This is the textbook 'big per-file cap lives where retention is shortest' inverse. Here small cap AND short retention.
- reliability: Container registry r8.im requires authentication. Anonymous requests to `/v2/` return HTTP 401 and manifest queries redirect to account login pages.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Files API is a workspace scratch space with no advertised total; documented behaviour is expiry, not quota. r8.im is a private-ish OCI registry for cog models.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'all input parameters, output values, output files, and logs are automatically removed after an hour, by default'
  - [2] 2026-10-21: 'This will work for files up to 100MB'
  - withheld 2026-10-21: probe: GET r8.im/v2/ -> 401; GET r8.im/v2/token -> 404 {'error':'Endpoint not found'}; GET r8.im/replicate/cog-hello-world/manifests/latest -L -> 307 -> 404 HTML
- sources:
  - [1] https://replicate.com/docs/topics/predictions/data-retention
  - [2] https://replicate.com/docs/topics/predictions/input-files
