# Replicate

> replicate.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/replicate/ | JSON https://fshy.ajam.dev/api/v1/entity/replicate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Replicate

- `compute/replicate` | paid-only | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:51.316Z (live) | stale on 2026-12-26
- url https://replicate.com/pricing
- free tier: For fast booting fine-tunes you'll only be billed for the time the model is active and processing your requests, so you won't pay for idle time like with other private models. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: anonymous | detail: Sign in is through a GitHub account; the first-party sign-in page asks for no email, phone, card or ID document. An account is required and a card is needed only once paid hardware is used.
- interface: unknown
- limits:
  - request-rate (binding): per-second billing from USD 0.36 an hour for the 4x-CPU plan to USD 43.92 an hour for eight H100s; eight A100s are USD 40.32 an hour [1]
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
  - [1] 2026-11-25: fast-booting fine-tunes bill only while processing; other private models bill for idle time | capture: sha256:58a0d28ae9649cd790feb17ac5e8d27ea8c28c47c70e6f9a1d4959ea93f44fdd | quote: For fast booting fine-tunes you'll only be billed for the time the model is active and processing your requests, so you won't pay for idle time like with other private models.
  - [1] 2026-11-24: the lowest CPU hardware rate is USD 0.36 an hour, not USD 0.09 | capture: sha256:58a0d28ae9649cd790feb17ac5e8d27ea8c28c47c70e6f9a1d4959ea93f44fdd | quote: CPU cpu | $0.000100/sec $0.36/hr | - | 4x | - | 8GB
  - [1] 2026-11-24: the most expensive listed hardware is the eight-H100 plan at USD 43.92 an hour | capture: sha256:58a0d28ae9649cd790feb17ac5e8d27ea8c28c47c70e6f9a1d4959ea93f44fdd | quote: 8x Nvidia H100 GPU gpu-h100-8x | $0.012200/sec $43.92/hr
  - [2] 2026-11-24: the sign-in page offers GitHub authentication and states no email, phone, card or ID field | capture: sha256:bc02259f0ad93814c1d21673d990a5687bc2c06e1c3a54acd631f1d959506a7e | quote: [Sign in with GitHub](https://replicate.com/login/github/)
  - [1] 2026-11-24: the fast-booting fine-tune idle-billing rule is unchanged | capture: sha256:58a0d28ae9649cd790feb17ac5e8d27ea8c28c47c70e6f9a1d4959ea93f44fdd | quote: For fast booting fine-tunes you'll only be billed for the time the model is active and processing your requests, so you won't pay for idle time like with other private models.
- sources:
  - [1] https://replicate.com/pricing
  - [2] https://replicate.com/signin

## replicate (model hosting)

- `storage/replicate-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:03.329Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: API-created output files are deleted after an hour, so the service cannot hold bytes as storage | capture: sha256:e2d4a5679bc730f8baee74e3dc4ae1717391309ea825b945f7c9556e81e1c509 | quote: For predictions created through the API, output files are automatically deleted after an hour. You must save a copy of any files in the output if you'd like to continue using them.
- sources:
  - [1] https://replicate.com/docs/topics/predictions/output-files
  - [2] https://replicate.com/pricing

## Replicate (r8.im + Files API)

- `storage/replicate` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.552Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: Replicate still documents automatic removal of prediction files after one hour by default | capture: sha256:00c4f1a7e8c59cfa1745d940bfbd24981e78844170c0465b6cec4c8aa07f49a3 | quote: For predictions created through the API, all input parameters, output values, output files, and logs are automatically removed after an hour, by default.
  - [2] 2026-11-19: Replicate's first-party input-files doc still states the 100 MB local-file upload limit | capture: sha256:ffd81c2697cce1d4e70e0b2273a7d4abbdd75cd88577ee4acee6a9ad08fbcdbc | quote: This will work for files up to 100MB:
  - probe:r8.im/v2/ 2026-11-19: a fresh probe of r8.im/v2/ still returns HTTP 401, confirming the registry requires authentication | capture: sha256:617793f27663a6eefad94c1b2b1ade1553029db5bc3736f6fe6d31fe5cd992eb | quote: "status": 401
- sources:
  - [1] https://replicate.com/docs/topics/predictions/data-retention
  - [2] https://replicate.com/docs/topics/predictions/input-files
