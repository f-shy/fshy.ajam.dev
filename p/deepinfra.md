# DeepInfra

> deepinfra.com | Inference, Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deepinfra/ | JSON https://fshy.ajam.dev/api/v1/entity/deepinfra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeepInfra

- `inference/deepinfra` | paid-only | evidence documented | binding none | category inference endpoint, keyed free tier
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:38:58.774Z (live) | stale on 2026-12-05
- url https://api.deepinfra.com/v1/openai
- free tier: no free allowance: a card or a prepaid balance is required before any use ('You have to add a card or pre-pay or you won't be able to use our services') | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: a promotional USD 20 in free credits is offered to viewers of the Two Minute Papers channel, claimed through a login link carrying deal=2mpapers; whether a card is needed to spend it is not stated on that page (unverified)
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the pricing page states a card or a prepaid balance is required before any use
- interface: rest
- limits:
  - request-rate: 200 concurrent requests per model, default per account; HTTP 429 'Rate limited' above the limit; an increase is requested from the Dashboard Account page [2]
- limits note: the limit is on concurrent requests, not per-minute volume: at 200 concurrent requests, a 1 second request gives approximately 12,000 RPM
- tooling: any OpenAI-compatible client
- composes with: pairs with an agent after a signup; the scarce link is the account and the unread allowance is the gap
- reliability: No reliability events were recorded. API keys were not provisioned during testing on 2026-11-04.
- notes: The weakest record in this topic and it says so. It exists to stop a name becoming a rediscovery. The pricing page states the opposite in one sentence, and the only free balance is a channel promotion. Paid-only is the correct verdict and documented is the correct rung.
- evidence note: the card-or-prepay requirement is quoted from the pricing page, the concurrency limit from the rate-limits documentation and the promotional credit from the Two Minute Papers page; all three are first-party pages
- extras:
  - checked.verdict_change: qualifies-with-caveat -> paid-only on 2026-10-22
- evidence:
  - [3] 2026-10-22: 'You have to add a card or pre-pay or you won't be able to use our services. Pre-paid accounts draw down their balance as they go', quoted
  - [4] 2026-10-22: 'we're thrilled to offer you $20 in free credits to explore DeepInfra's AI inference cloud', claimed through a login deal link, quoted
  - [3] 2026-10-28: a card or a prepaid balance is required before any use | capture: sha256:d7dd624d93783f5ba68f1f9b6b87184b185ac17a77d772ab51692f14c17a93b4 | quote: You have to add a card or pre-pay or you won't be able to use our services. Pre-paid accounts draw down their balance as they go, and invoiced accounts are billed once at the beginning of the following month.
  - [4] 2026-10-28: DeepInfra offers USD 20 in free credits to viewers of Two Minute Papers through a Claim link to its login page with deal=2mpapers | capture: sha256:80f3628f1fffa009552c3f46e002c83e0edda1c8fb3684a679bf35b8be364076 | quote: As a valued viewer of Two Minute Papers, we’re thrilled to offer you $20 in free credits to explore DeepInfra’s AI inference cloud.
  - [2] 2026-10-28: the default limit is 200 concurrent requests per model for every account | capture: sha256:74ce39bcc7cd4debc03938310e771321d27a7db3486017a5f6888a2e2d2523da | quote: Every account has a default limit of 200 concurrent requests per model.
  - [2] 2026-10-28: at a 1 second average duration the 200 concurrent limit corresponds to approximately 12,000 RPM | capture: sha256:74ce39bcc7cd4debc03938310e771321d27a7db3486017a5f6888a2e2d2523da | quote: | 1 second | 200 | 12,000 RPM |
  - [3] 2026-11-03: the pricing page still states a card or a prepaid balance is required before use | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: You have to add a card or pre-pay or you won't be able to use our services. Pre-paid accounts draw down their balance as they go, and invoiced accounts are billed once at the beginning of the following month.
  - [4] 2026-11-03: the USD 20 offer is still published; the page lists Register, Dashboard, run a command, and names no card or prepaid balance | capture: sha256:09e93d4784cc3f095a9bbf36560ca7939fccf456b2f533a76a2d63a4a56ff4be | quote: As a valued viewer of Two Minute Papers, we’re thrilled to offer you $20 in free credits to explore DeepInfra’s AI inference cloud.
- sources:
  - [1] https://api.deepinfra.com/v1/openai
  - [2] https://deepinfra.com/docs/advanced/rate-limits
  - [3] https://deepinfra.com/pricing
  - [4] https://deepinfra.com/papers

## DeepInfra GPU

- `compute/deepinfra-gpu` | paid-only | evidence documented | binding none | category GPU cloud | tier Dedicated GPUs: private deployments and GPU instances
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:36:21.466Z (live) | stale on 2026-12-04
- url https://deepinfra.com/pricing
- free tier: No free GPU allowance. Dedicated GPU rates on the pricing page, billed in minute granularity: A100 80 GB USD 1.49 per GPU-hour, H100 80 GB USD 2.90, H200 141 GB USD 3.49, B200 180 GB USD 4.89, B300 270 GB USD 5.89. These are the price list for deploying a custom model on dedicated GPUs and paying for uptime; the SSH GPU-instance page lists B200 (1x at USD 4.89 per hour, 8x at USD 39.12 per hour). L40S, RTX 4090 and L4 are not listed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: GPU instances are sold as 1, 4 or 8 B200 cards; private deployments as dedicated SXM-connected GPUs
- retention: All container data is permanently lost when a GPU-instance container is terminated; save work before stopping. | source: [2] | note: a machine record: what is lost is the container's data
- egress: 'Pay by the minute with no egress fees.' on the GPU-instances page | metered: no | source: [3]
- identity: card | detail: 'You have to add a card or pre-pay or you won't be able to use our services.' Sign-in is Google, GitHub, or email and password, and an email-and-password account gets a verification email.
- interface: ssh, rest
- limits note: no quota is stated for GPU rental on the pages read; the pages state a pre-paid or card requirement and a spending limit setting
- binding note: no usage quota is stated for GPU rental; the constraint is the card or pre-pay requirement and that SSH instances are listed only for B200 and B300
- interface detail: stated by the vendor docs, not probed: SSH to a container as the ubuntu user with a pasted public key, and an HTTP API at api.deepinfra.com/v1/containers
- tooling: dashboard 'New Container' with a pasted SSH public key, or the HTTP API with a bearer API key; private deployments from the dashboard Deployments page. The docs list B200 and B300 for SSH instances; A100, H100 and H200 are named for private deployments.
- composes with: the A100 and H100 rates are deployment rates for serving a custom model, billed while the GPUs run; whether they can be rented as plain SSH instances is unverified: behind a sign-up. The vendor's serverless token API is the inference topic.
- reliability: unverified: no status page or incident history was read for this offer
- notes: Listed by computeprices.com with 5 GPUs from USD 1.49 per hour. Distinct from the serverless inference API (inference/deepinfra), the DeepStart grant and the sandboxes, which other records hold.
- evidence:
  - [1] 2026-11-03: A100 80 GB dedicated rate of USD 1.49 per GPU-hour | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: | A100 | 80GB | $1.49 / GPU-hour |
  - [1] 2026-11-03: H100 80 GB dedicated rate of USD 2.90 per GPU-hour | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: | H100 | 80GB | $2.90 / GPU-hour |
  - [1] 2026-11-03: the rate table is the price list for custom model deployments, billed for uptime | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: You can deploy your own model on our hardware and pay for uptime.
  - [1] 2026-11-03: dedicated GPUs are billed per minute | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: * Billed in minute granularity
  - [1] 2026-11-03: a card or a pre-payment is required to use the service | capture: sha256:0289de89e60d43a7e4fd29b3322a33af62c983a8349e1e7010d04d68afb8268a | quote: You have to add a card or pre-pay or you won't be able to use our services.
  - [3] 2026-11-03: the GPU-instances page prices 1x B200 at USD 4.89 per hour | capture: sha256:5cee63e904ed3d6d1ec2b0d3a90008d49bea2ecdee1ab948702584f1aa797ce9 | quote: 180GB1xB200NVIDIA B200 GPU -$4.89/hour
  - [3] 2026-11-03: per-minute billing and no egress fees on GPU instances | capture: sha256:5cee63e904ed3d6d1ec2b0d3a90008d49bea2ecdee1ab948702584f1aa797ce9 | quote: Access high-power GPUs when you need them. Pay by the minute with no egress fees.
  - [2] 2026-11-03: SSH GPU instances are B200 instances | capture: sha256:4648d595de7d9a7f57fd9287067525dde128ab3f3720193cca8443c8dd94467d | quote: Rent dedicated B200 GPU instances with SSH access for training, fine-tuning, and custom workloads.
  - [2] 2026-11-03: container data is lost on termination | capture: sha256:4648d595de7d9a7f57fd9287067525dde128ab3f3720193cca8443c8dd94467d | quote: > All container data is permanently lost when terminated. Save your work before stopping.
  - [4] 2026-11-03: private deployments are billed per GPU-hour | capture: sha256:9aab7ed44834b7834f73edfb018ca139ff34a33f481f4f758941c38850b25099 | quote: Unlike shared inference (pay per token), private deployments are billed per GPU-hour.
  - [5] 2026-11-03: email-and-password sign-up exists beside Google and GitHub sign-in | capture: sha256:02aa0af9d31fe46ac160c3318d1334ebd1afe225708a03cd5060ce96bebc03d2 | quote: Create an account at [deepinfra.com/signup](https://deepinfra.com/signup).
  - [6] 2026-11-03: third-party listing agrees on H100 USD 2.90 per hour, collected 2026-11-03 | capture: sha256:69efb7a18462af259cfed3049df5a173ccc5e90f443193a83275f4f751763354 | quote: | [H100 SXM](https://computeprices.com/providers/deep-infra/gpus/h100) | $2.90/hr | 80GB | 1× | 11/3/2026 |
  - [6] 2026-11-03:  | capture: sha256:69efb7a18462af259cfed3049df5a173ccc5e90f443193a83275f4f751763354 | quote: Deep Infra offers various GPU types including A100 SXM, H100 SXM, H200, HGX B300, B200.
- sources:
  - [1] https://deepinfra.com/pricing
  - [2] https://docs.deepinfra.com/gpu-instances/overview
  - [3] https://deepinfra.com/gpu-instances
  - [4] https://docs.deepinfra.com/private-models/overview
  - [5] https://docs.deepinfra.com/account/signing-in.md
  - [6] https://computeprices.com/providers/deep-infra

## DeepInfra Sandboxes

- `compute/deepinfra-sandboxes` | paid-only | evidence documented | binding retention-clamped | category microVM (Kata on QEMU/KVM) sandbox | tier nano
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T01:54:08.000Z (live) | stale on 2026-11-24
- url https://deepinfra.com/blog/sandboxes
- price parsed USD 39.42/mo
- free tier: no free tier: 'the nano plan starts at just $0.054/hour, billed by the second'; no credit or trial is offered for sandboxes on the pages read | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable: the unit is a sandbox, not an object. Each command defaults to a 60-second timeout with a 30-minute hard cap.
- retention: Stopping keeps /workspace and resets everything else; 'you've got up to 7 days to start() it again before it's permanently deleted'. Only /workspace survives a stop, and failed sandboxes lose /workspace. | days: 7 | source: [1]
- egress: Not published. The overview page and the blog post state the compute and lifecycle meters and say nothing about a traffic allowance or a per-GB egress rate. | metered: no | source: [2]
- identity: card | detail: A DeepInfra account is required and sandboxes draw on DeepInfra billing; the catalog endpoint refuses an unauthenticated caller, so plan shapes and prices are visible only to a signed-in account. Card types, any authorisation hold, and whether a debit or prepaid card is accepted were not established.
- interface: rest, cli
- limits:
  - retention-clamped (binding): auto-stop after 24 continuous running hours, a default 1-hour idle timeout that cannot be disabled, and 7 days of stopped retention before deletion [1]
  - volume-quota: 25 non-stopped sandboxes per account; 'shared-fleet capacity can temporarily prevent creation' [2]
- limits note: Billing runs while a sandbox is creating, starting, running or stopping, so 'per-second' includes boot and the disk save on stop. The plan shapes and rates are behind an authenticated catalog: GET /v1/sandboxes/catalog returned {"detail":"User is not authorized to access this resource"} to an unauthenticated request on 2026-10-24, and the docs say explicitly not to hardcode the numbers.
- binding note: The 24-hour auto-stop is the first hard wall: no configuration on the pages read lifts it, so the machine cannot be an always-on monitor or VPN node even before the price matters.
- interface detail: Python SDK ('Sandbox.create(plan="medium")') and an HTTP API, with a dashboard at deepinfra.com/dash/sandboxes.
- tooling: The vendor's Python SDK and REST API; commands run inside the microVM and files move only through /workspace.
- composes with: USD 0.054 an hour for the nano plan is USD 39.42 a month if never stopped, and a sandbox auto-stops after 24 hours of continuous running, so it is not an always-on machine. It belongs in the stack as a scratch executor next to earlier inference accounts, not as an answer to the cheap-VM questions.
- reliability: Two documented loss paths: a failed sandbox loses /workspace, and everything outside /workspace is discarded on stop. Shared-fleet capacity can refuse creation.
- notes: Arithmetic: USD 0.054 an hour × 730 = USD 39.42 a month if the auto-stop did not exist; × 300 h = USD 16.20. The auto-stop makes the 730-hour figure hypothetical, and it is recorded as the price of the meter rather than the price of a machine. What the nano shape actually contains is unverified because the catalog is authenticated.
- evidence note: The nano rate, the per-second meter and the whole lifecycle are quoted from DeepInfra's own blog and docs, read. The rate-to-shape mapping is not documented publicly: the vendor directs readers to an authenticated catalog, so the shape fields stay null rather than guessed. What would raise it: a signed-in read of /v1/sandboxes/catalog, which would give the exact vCPU/RAM/disk of the nano plan.
- extras:
  - billing_model: hourly
  - term: per-second metering, no commitment
  - m10h_usd: 16.2
  - m24h_usd: 39.42
  - price_arithmetic: 0.054/hr × 730 h = USD 39.42; × 300 h = USD 16.20. Both assume the sandbox is never auto-stopped, which the vendor's 24-hour rule makes impossible in practice.
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.ports: not published; the docs describe command execution and file transfer, not an inbound listener
  - session_cap.wall_clock_min: 1440
  - session_cap.idle_reap_s: 3600
  - session_cap.restart_required: yes
  - session_cap.note: auto-stop at 24 h continuous; 1 h default idle timeout; 7-day stopped retention
  - aggregator_note: sandboxprices.com has a DeepInfra Sandboxes row marked unverified with no total, for the same reason recorded here: the shape-to-rate mapping is behind the authenticated catalog.
- evidence:
  - [1] 2026-10-24: quoted: 'the `nano` plan starts at just $0.054/hour, billed by the second' and 'Leave one running and it auto-stops after 24 hours'
  - [1] 2026-10-24: retention: 'Stopping just pauses it: /workspace sticks around, everything else resets to a clean image. From there you've got up to 7 days to start() it again before it's permanently deleted.'
  - [2] 2026-10-24: billing: 'Billing is per-second with no minimum, and only runs while a sandbox is creating, starting, running, or stopping - a stopped sandbox costs nothing'
  - [2] 2026-10-24: no public shape/rate table: 'For current plan specs (vCPU, RAM, disk) and hourly pricing, don't hardcode numbers - check the live catalog'
- sources:
  - [1] https://deepinfra.com/blog/sandboxes
  - [2] https://docs.deepinfra.com/sandboxes/overview

## DeepInfra DeepStart

- `compute/deepinfra-deepstart` | fails-identity | evidence documented | binding retention-clamped | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://deepinfra.com/deepstart
- free tier: 50,000,000,000 free inference tokens for an approved startup, priced at DeepSeek V4 Flash rates and expiring one year after approval. At the DeepSeek-V4-Flash-0731 rate of USD 0.06 per million input tokens the grant is worth USD 3,000 of input, or USD 9,000 at the USD 0.18 output rate. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: the funding gate fails before the tokens do: 'Have raised between 250K and 10M USD' and 'Founded in the last 2 years' are company facts, and the credits also expire one year after approval. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - retention-clamped (binding): the funding gate fails before the tokens do: 'Have raised between 250K and 10M USD' and 'Founded in the last 2 years' are company facts, and the credits also expire one year after approval. [1]
- limits note: the funding gate fails before the tokens do: 'Have raised between 250K and 10M USD' and 'Founded in the last 2 years' are company facts, and the credits also expire one year after approval.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: a grant needs a funded company, so it cannot compose with anything a single person holds.
- reliability: no reliability event recorded
- notes: 50,000,000,000 tokens / 1,000,000 = 50,000 units of a million tokens; 50,000 x USD 0.06 = USD 3,000 input-equivalent; 50,000 x USD 0.18 = USD 9,000 output-equivalent. A third-party list circulating on 2026-10-22 states the grant is 1,000,000,000 tokens, which the vendor page contradicts by a factor of 50; the vendor figure is recorded. This is the largest per-entity inference credit found among evaluated providers and it is closed to a person without a funded company. It is a separate programme from the signup record above: the same provider carries both a closed grant and a card-gated API.
- extras:
  - facets.class: startup-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'DeepStart ~50,000,000,000 free tokens*' with 'To qualify your startup needs to meet the following: Have raised between 250K and 10M USD; Founded in the last 2 years; * at DeepSeek V4 Flash prices; Credits expire 1 year after approval', quoted
  - [2] 2026-10-22: DeepSeek-V4-Flash-0731 at USD 0.06 per 1M input and USD 0.18 per 1M output tokens, used for the conversion, quoted
- sources:
  - [1] https://deepinfra.com/deepstart
  - [2] https://deepinfra.com/pricing
