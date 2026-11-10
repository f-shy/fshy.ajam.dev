# Together AI

> together.ai | Compute, Inference, Storage; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/together/ | JSON https://fshy.ajam.dev/api/v1/entity/together.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CodeSandbox SDK

- `compute/codesandbox-sdk` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:05.602Z (live) | stale on 2026-12-05
- url https://docs.together.ai/docs/together-code-sandbox-legacy
- free tier: catalogue documentation records a free monthly credit; the rate card it carries is labelled legacy. | unit: mixed | metered on: wall-clock | read on: 2026-10-02 | source: [1] | note: Together recommends its successor for new integrations
- per-object cap: not applicable
- retention: hibernation stops compute billing; the disk term was not read
- egress: not published: https://docs.together.ai/docs/together-code-sandbox-legacy states no egress allowance or overage price; the legacy offer is sold on custom plans | metered: no | source: [1]
- identity: email | detail: an account; the tier gate was not read
- interface: cli
- limits:
  - request-rate: Build allows 10 concurrent VMs
  - retention-clamped (binding): the published rates are labelled legacy [1]
- limits note: 10, 20 and 40 VM credits an hour at USD 0.01486 each on the legacy card
- binding note: the rate card is labelled legacy and Together points at a successor, so the product's own future ends the offer before any quota does
- interface detail: the @codesandbox/sdk JavaScript SDK with an API token, and a CLI to build templates; no REST or SSH interface is documented
- tooling: the CodeSandbox SDK, now legacy under Together
- composes with: none for new work: the rates are legacy and the product has a successor
- reliability: no reliability event recorded
- notes: Documented so a reader does not build on a legacy rate card. The credit is real and the product is being replaced.
- evidence note: re-read live on 2026-10-22 for the free-tier and limit figures
- extras:
  - billing_model: allocated
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: the rate card is labelled legacy and Together recommends its successor for new integrations
  - [1] 2026-10-22: read live: the rate card is deprecated and a successor SDK is named
  - [1] 2026-11-03: the legacy offer is sold on custom plans; no egress allowance or price is published | capture: sha256:7fd68d6cac5980e8f20797e49e200f268336807cad10b8fd54846f70bba98f37 | quote: The legacy code sandbox is available on Together's [custom plans](https://www.together.ai/contact-sales).
  - [1] 2026-11-03: the SDK is an npm package | capture: sha256:7fd68d6cac5980e8f20797e49e200f268336807cad10b8fd54846f70bba98f37 | quote: npm install @codesandbox/sdk
- sources:
  - [1] https://docs.together.ai/docs/together-code-sandbox-legacy

## Together AI (gpu)

- `compute/together-gpu` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:36.650Z (live) | stale on 2026-12-04
- url https://www.together.ai/pricing
- free tier: no free GPU allowance. The pricing page lists one card of the five, the NVIDIA HGX H100, per GPU per hour: GPU Clusters preemptible $1.99, on-demand $3.99, reserved $3.69 for 3-30 days, $3.45 for 31-90 days and $3.19 for 91-180 days, and Dedicated Inference on demand $5.49. No A100, L40S, GeForce RTX or L4 card is listed. GPU Clusters are described as 'on an hourly basis', post-training is billed per minute, and the cluster and dedicated tables state no billing granularity or minimum bill; the platform needs a $15 first credit purchase. Inference bills per million tokens from $0.00 on Ternary Bonsai to $15.00 an output MTok. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): GPU capacity priced per GPU per hour, on demand or reserved; reserved capacity is sold in throughput units [1]
  - request-rate (binding): inference bills per million input and output tokens, from $0.00 to $15.00 an output MTok [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and its GPU section prices per GPU per hour. It publishes no free GPU allowance, so the record's free-tier claim is not established and the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.note: priced per GPU per hour with on-demand and reserved rates
  - session_cap.restart_required: no
  - session_cap.note: a GPU instance bills per hour; the page states no reap
  - free_tier_kind: none
  - ps.price: managed storage is a separate section
  - ps.durability: managed storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and its GPU section states 'All prices are per GPU per hour' with on-demand and reserved columns, alongside per-million-token model rates from 'Ternary Bonsai 27B $0.00' to 'Kimi K3 $3.00 / $15.00'
  - [1] 2026-11-03: GPU Clusters H100 per GPU per hour: preemptible 1.99, on-demand 3.99, reserved 3.69 (3-30 days), 3.45 (31-90), 3.19 (91-180), 181+ by quote | capture: sha256:b2c1ae6ef7e72332b9b273c6c99361612d9068716caa47324a236909b42794af | quote: | NVIDIA HGX H100 | $1.99 | $3.99 | $3.69 | $3.45 | $3.19 | [Contact us](https://www.together.ai/gpu-cluster-request) |
  - [1] 2026-11-03: column order of the GPU clusters rate table | capture: sha256:b2c1ae6ef7e72332b9b273c6c99361612d9068716caa47324a236909b42794af | quote: | Hardware | Preemptible Compute | ON-Demand | Reserved | | | |
  - [1] 2026-11-03: Dedicated Inference lists an H100 at 5.49 per GPU per hour on demand | capture: sha256:b2c1ae6ef7e72332b9b273c6c99361612d9068716caa47324a236909b42794af | quote: | NVIDIA HGX H100 | $5.49 | [Contact sales](https://www.together.ai/monthly-reserved) |
  - [1] 2026-11-03: the on-demand GPU clusters are described as hourly pay as you go | capture: sha256:b2c1ae6ef7e72332b9b273c6c99361612d9068716caa47324a236909b42794af | quote: Pay as you go GPU capacity on an hourly basis.
  - [1] 2026-11-03: post-training GPUs bill per minute; the cluster and dedicated tables state no granularity | capture: sha256:b2c1ae6ef7e72332b9b273c6c99361612d9068716caa47324a236909b42794af | quote: On-demand training infrastructure, billed per minute for each active model resource.
  - [2] 2026-11-03: the platform needs a USD 15 first credit purchase and offers no trial | capture: sha256:142dd66fe6b27a1f44b33ac810b94bd4a8de55101eac54c618b5d911b65f65fb | quote: Together AI does not currently offer free trials. Access to the Together platform requires a minimum \$15 credit purchase.
- sources:
  - [1] https://www.together.ai/pricing
  - [2] https://docs.together.ai/docs/billing

## Together AI (Inference)

- `inference/together` | paid-only | evidence documented | binding none | category inference endpoint
- needs card yes, phone no, ID no, institution no | verified 2026-10-28T09:47:54.947Z (live) | stale on 2026-11-28
- url https://docs.together.ai/docs/billing
- free tier: No free trial: 'Together AI does not currently offer free trials. Access to the Together platform requires a minimum $15 credit purchase.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: an account, then a credit purchase of at least USD 15 with a default payment method (a credit or debit card, or a US bank account via ACH); the platform is fully prepaid and API access is suspended at a zero balance
- interface: rest
- limits note: no numeric rate limit is published: serverless performance is best-effort, a 429 or 503 response may be returned when demand is high, and Together may apply custom rate limits to a model in high demand; Enterprise and Scale contracts carry purchased rate limits
- binding note: no numeric rate limit or quota is published for serverless inference; rate limiting may occasionally occur with high request volumes or large bursts of traffic
- tooling: any OpenAI-compatible client
- composes with: no free lane: the platform requires a minimum USD 15 purchase, so there is no trial credit to pair with an agent
- reliability: No reliability events were recorded. API keys were not provisioned during testing on 2026-10-28.
- notes: The compute topic also carries this provider under separate slugs. The vendor denies a free trial in its own billing documentation, so the record is paid-only.
- evidence note: the billing documentation was read on 2026-10-23 and states that Together offers no free trial and requires a USD 15 minimum purchase. The unauthenticated 401 probe from 2026-10-22 establishes only that the endpoint exists and gates on a key
- evidence:
  - probe:https://api.together.xyz/v1/chat/completions 2026-10-22: an unauthenticated POST returned 401 with a 372-byte body, {"error":{"message":"Missing API key..."}}. The endpoint exists and gates on a key; no key existed here, so no quota was read
  - [2] 2026-10-22: the rate-limits page returned 200 with 388051 bytes and describes dynamic per-model limits and throughput guarantees; no free-tier allowance was found in the served text
  - [1] 2026-10-23: 'Together AI does not currently offer free trials. Access to the Together platform requires a minimum $15 credit purchase.', quoted
  - [2] 2026-10-28: the rate-limits page publishes no numeric limit and says serverless inference is usually used without encountering rate limits | capture: sha256:57afde9c3b47356f54f3ebcc80dfce32d4b7d9d54d7d525b76bc4dc17fbe9586 | quote: In most cases, you can use Together AI [serverless inference](https://docs.together.ai/docs/serverless/overview.md) without encountering rate limits. Rate limiting may occasionally occur with high request volumes or large bursts of traffic.
  - [2] 2026-10-28: no numeric limit is published; demand-based limiting returns 429 or 503 | capture: sha256:57afde9c3b47356f54f3ebcc80dfce32d4b7d9d54d7d525b76bc4dc17fbe9586 | quote: When demand is high, Together may limit requests to maintain these performance goals. You may receive a `429 Too Many Requests` or `503 Service Unavailable` response.
  - [1] 2026-10-28: the platform is fully prepaid and a positive balance is needed before API calls | capture: sha256:142dd66fe6b27a1f44b33ac810b94bd4a8de55101eac54c618b5d911b65f65fb | quote: Together AI is fully prepaid. You need a positive credit balance to use the platform. Add credits from your [billing settings](https://api.together.ai/settings/organization/~current/billing) before making API calls.
  - [1] 2026-10-28: no free trial; access needs a minimum USD 15 credit purchase | capture: sha256:142dd66fe6b27a1f44b33ac810b94bd4a8de55101eac54c618b5d911b65f65fb | quote: Together AI does not currently offer free trials. Access to the Together platform requires a minimum \$15 credit purchase.
- sources:
  - [1] https://docs.together.ai/docs/billing
  - [2] https://docs.together.ai/docs/rate-limits

## Together Code Sandbox

- `compute/together-code-sandbox` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:15.000Z (live) | stale on 2026-11-22
- url https://www.together.ai/pricing
- free tier: no separate sandbox allowance: model inference bills per million tokens from $0.00 on Ternary Bonsai to $15.00 an output MTok, and a code sandbox draws on the same account | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): per million input and output tokens, from $0.00 on Ternary Bonsai to $15.00 an output MTok [1]
  - per-object-cap: dedicated capacity is reserved in throughput units, where tokens a minute depends on the model [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and carries model and audio rates. It publishes no sandbox-specific free allowance, so the record's free-tier claim is not established and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a sandbox draws on the same token and audio meters; the page states no sandbox clock
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 2.0
  - burst_bill: min 1 h
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the pricing page was read on 2026-10-22 and is a per-million-token model table with 'Kimi K3 $3.00 input, $15.00 output', 'GLM-5.3 $1.40 / $4.40', 'Ternary Bonsai 27B $0.00', and 'Price per audio minute'; the sandbox product is billed through the same meters
- sources:
  - [1] https://www.together.ai/pricing

## Together AI Files API (with 100 GB fine-tune objects)

- `storage/together-ai-files-api` | fails-identity | evidence reported | binding none | category LLM provider /v1/files
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.together.ai/docs/fine-tuning/data-preparation
- price $163.84 (Managed Storage at $0.16/GiB/mo) — 40-80x the cheap-paid floor; egress free | parsed USD 149.01/TB-mo
- free tier: 100 GB per training file (JSONL or Parquet); SDK constant MAX_FILE_SIZE_GB = 50.1 and MULTIPART_THRESHOLD_GB = 5.0. No published total-storage quota. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 100 GB | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress fee on the Files API. Their separate Managed Storage product is explicitly advertised with 'zero egress fees'. | metered: no
- identity: card | detail: card
- interface: unknown
- limits:
  - per-object-cap: per-object-cap 100 GB [1]
- limits note: per-object-cap 100 GB. Multipart kicks in above 5 GB; per-part upload timeout 300 s. A client-side check (`check_file`) validates JSONL structure before upload, which is a soft write gate for the fine-tune purpose.
- interface detail: POST https://api.together.xyz/v1/files/upload (and /v1/files/{id}/content); OpenAI-ish, `purpose` in {fine-tune, calibration, eval, batch-api}
- tooling: together-python (`tg files upload`), curl multipart
- composes with: 100 GB single objects are the largest per-object cap found in the entire LLM-provider lane — 200x OpenAI's 512 MB. Unverified.
- reliability: Together has no free tier — 'no free trials', $5 minimum prepaid credit required. That already fails the constraint. Read path unverified: /v1/files/{id}/content exists but every probe returns 401.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 100 GB per training file (JSONL or Parquet); SDK constant MAX_FILE_SIZE_GB = 50.1 and MULTIPART_THRESHOLD_GB = 5.0. No published total-storage quota.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $163.84 (Managed Storage at $0.16/GiB/mo) — 40-80x the cheap-paid floor; egress free
- evidence:
  - [1] 2026-10-21: 'The file size limit for either format is 100 GB.'
  - [2] 2026-10-21: 'MAX_FILE_SIZE_GB = 50.1', 'MULTIPART_THRESHOLD_GB = 5.0', 'MULTIPART_UPLOAD_TIMEOUT = 300'
  - [3] 2026-10-21: 'Object storage and parallel filesystems optimized for AI, provisioned and fully managed … with zero egress fees'
  - [4] 2026-10-21: 'storage ($0.16/GiB/month for the parallel filesystem used by GPU Clusters)'
  - [5] 2026-10-21: 'Together AI does not currently offer free trials … minimum $5 purchase'
  - [6] 2026-10-21: PROBE: curl -D - -> 401, Content-Length 148, {"error":{"message":"No API key provided…"}}; /v1/files/abc/content -> 401/148
- sources:
  - [1] https://docs.together.ai/docs/fine-tuning/data-preparation
  - [2] https://github.com/togethercomputer/together-python/blob/main/src/together/constants.py
  - [3] https://www.together.ai/managed-storage
  - [4] https://markaicode.com/pricing/together-ai-pricing/
  - [5] https://www.flowtools.co/alternatives/openrouter
  - [6] https://api.together.xyz/v1/files
