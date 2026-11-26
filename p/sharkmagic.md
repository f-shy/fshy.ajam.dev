# Shark Magic

> sharkmagic.si | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sharkmagic/ | JSON https://fshy.ajam.dev/api/v1/entity/sharkmagic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shark Magic

- `compute/shark-magic` | paid-only | evidence documented | binding volume-quota | category microVM sandbox | tier Shark Pro ($5/month, $5 included usage)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.709Z (live) | stale on 2026-12-26
- url https://sharkmagic.si/
- free tier: No separate free plan: Shark Pro is $5/month and includes $5 of usage; the first 5 GiB of storage and the first 10 GiB of egress per Space per billing cycle are free, overage only. Promotions, when offered, are shown at checkout. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Included usage is spent first, then prepaid credits, and unused included usage does not roll over. Compute is $0.12 per compute-hour billed per second only while a command runs; services $0.03/h (2 vCPU/2 GiB) or $0.06/h (4 vCPU/4 GiB); storage $0.08/GiB-month and egress $0.03/GB above the free allowances.
- per-object cap: not applicable: the billed unit is command time and files in a Space, with a 512 MiB single-file upload limit and a 2 GiB archive upload limit; 50 GiB of disk per account on the hosted node | source: [2]
- retention: A Space's files persist between commands; Space commits replicate in the background to an object store, and op results and output are kept 7 days. | source: [3] | note: A Space hibernates into about 57 KB on disk and wakes on the next request; at zero credit balance Spaces are hibernated but files stay readable.
- egress: First 10 GiB free per Space per billing cycle, overage at $0.03 per GB; egress is metered as bytes sent and received by commands, file reads are free, and the hosted default is an allowlist with package registries and GitHub (private ranges always blocked). | metered: yes | free allowance: 10 GiB per Space per billing cycle | price per TB: USD 30 per TB (from USD 0.03 per GB) | source: [3]
- identity: email | detail: The signup page says 'Start with your work email' and asks for an account shared with the CLI and the API; the plans are paid through Stripe Checkout, so a card is needed to buy a plan or top up credits, but none is named as a signup requirement.
- interface: rest, cli
- limits:
  - volume-quota (binding): $5 of included usage per month on Shark Pro, with $5/month plans and $0.12 per compute-hour of command time beyond it [3]
  - volume-quota (binding): first 5 GiB of storage free per Space per billing cycle, then $0.08 per GiB-month [3]
  - volume-quota (binding): first 10 GiB of egress free per Space per billing cycle, then $0.03 per GB [3]
  - request-rate: 100 requests/s per credential, burst 500; 4 commands running at once on a new account [2]
  - retention-clamped: op results and output retained 7 days; sync command timeout max 900 s, streaming or async max 7200 s [2]
- limits note: A synchronous exec has a default 120 s timeout and a 900 s maximum; a streaming or async exec defaults to 30 min with a 7200 s maximum. Disk per account on the node is 50 GiB, and a Space holds 8 vCPU / 4 GiB for a command. GPUs, non-Linux guests and a published SLA are not available.
- binding note: The $5 of included monthly usage buys about 42 command-hours at $0.12/hour, so the included allowance runs out before the 50 GiB disk cap or the 4-concurrent-command limit for a single agent.
- interface detail: An HTTP API at https://api.sharkmagic.si (hosted node https://hel1.sharkmagic.si), Python and TypeScript SDKs, and a CLI with shark run, shark cp, shark expose and shark connect; shark connect is not served on the hosted node.
- endpoint: part of interface detail
- tooling: the shark CLI (pip install sharkmagic) and the Python and TypeScript SDKs; the agent runs its commands through shark run against a hosted Space.
- composes with: A persistent Space gives an agent files and services that sleep between commands; the credential proxy keeps API keys outside the microVM, and forks give O(1) copies for parallel jobs. The hosted service is the answer; a self-hosted node (Shark(base_url=..., api_key=...)) is a last resort for readers who run their own node.
- reliability: Node admission answers 503 out_of_capacity when memory or CPUs are short; at zero balance new work answers 402 credits_exhausted and Spaces hibernate; concurrent writes to the same file conflict and the later commit is not published; no published SLA and no GPUs.
- notes: Hosted microVM-per-command sandboxes: a Space persists files and services, and every command runs in a fresh Firecracker microVM billed only while it runs. The $5/month Shark Pro plan includes $5 of usage, so it is paid-only with no free plan; self-hosting a node is a last resort.
- evidence note: The plan prices, per-use rates, free allowances and signup gate are quoted from the vendor's own site and docs read 2026-11-25; the no-free-plan statement is from the vendor FAQ on the same day.
- extras:
  - shape.vcpu: 8
  - shape.ram_gib: 4
  - shape.gpu_class: none: no GPUs
  - shape.gpu_count: 0
  - shape.note: the standard compute shape is 8 vCPU / 4 GiB; there is no 2 vCPU / 2 GiB compute shape
  - billing_model: monthly plan with included usage, then prepaid credits; per-second command billing
  - free_tier_kind: included-usage-and-allowances
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not stated; exposed processes get preview URLs
  - session_cap.wall_clock_min: 120
  - session_cap.restart_required: no
  - session_cap.note: sync commands max 900 s, streaming or async max 7200 s; Spaces hibernate when idle
- evidence:
  - [4] 2026-11-25: Shark devbox is $5/month with $5 of usage included and commands bill at $0.12 per compute-hour per second only while they run | capture: sha256:6eb32ca17e8098e36306ab5ac36b291f033a0103b311eeb8931fb102fb12029d | quote: Shark devbox: plan $5/month; we include $5 of usage. Commands bill at $0.12 per compute-hour, per second, only while they run.
  - [3] 2026-11-25: storage has a first 5 GiB free allowance per Space per billing cycle with overage only | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: first 5 GiB free per Space per billing cycle, overage only
  - [3] 2026-11-25: egress has a first 10 GiB free allowance per Space per billing cycle with overage only | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: first 10 GiB free per Space per billing cycle, overage only
  - [1] 2026-11-25: there is no separate free plan and promotions are shown at checkout | capture: sha256:f00cc6c186140d65eabb2b7b8713bf3c4687f33dde2a03ec979dcaf5304f8d07 | quote: There is no separate free plan; promotions, when offered, are shown at checkout.
  - [5] 2026-11-25: the signup asks for a work email | capture: sha256:191c2cdf2017d5c6010c9baeeebb0411a504cadbd300337fd91d22b3a806a4ed | quote: Start with your work email. You can invite your team after.
  - [2] 2026-11-25: the hosted node enforces 100 requests/s per credential with a burst of 500 | capture: sha256:0b6cad6fa176178c5a13ac21b3cf35bf4f629210c2f48608d4ba3d4f5276ec33 | quote: request rate per credential | 100/s, burst 500 (`429 rate_limited` with `Retry-After`)
  - [3] 2026-11-24: compute is USD 0.12 per compute-hour on the standard 8 vCPU / 4 GiB shape, billed per second only while a command runs | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: | Compute, standard 8 vCPU / 4 GiB | $0.12 per compute-hour | none; billed per second only while a command runs |
  - [3] 2026-11-24: egress is USD 0.03 per GB with the first 10 GiB free per Space per billing cycle | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: | Egress | $0.03 per GB | first 10 GiB free per Space per billing cycle, overage only |
  - [3] 2026-11-24: storage is USD 0.08 per GiB-month with the first 5 GiB free per Space per billing cycle | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: | Storage | $0.08 per GiB-month | first 5 GiB free per Space per billing cycle, overage only |
  - [3] 2026-11-24: Shark Pro is USD 5 a month and includes USD 5 of usage | capture: sha256:3cbb2db8be1af3f43ce9a0bca2dbd08ae533cca6235104e889db971ca5d5bf00 | quote: | Shark Pro | $5/month | $5 |
  - [1] 2026-11-24: there is no separate free plan; the Pro plan's included usage and the storage and egress allowances are the only free capacity | capture: sha256:f00cc6c186140d65eabb2b7b8713bf3c4687f33dde2a03ec979dcaf5304f8d07 | quote: Is there a free tier? The Shark Pro plan includes $5 of usage each month, and storage and egress each have a free monthly allowance per Space. There is no separate free plan; promotions, when offered, are shown at checkout.
  - [5] 2026-11-24: the signup gate asks for a work email address | capture: sha256:191c2cdf2017d5c6010c9baeeebb0411a504cadbd300337fd91d22b3a806a4ed | quote: Start with your work email. You can invite your team after.
  - [2] 2026-11-24: the request rate per credential is 100 per second with a burst of 500 | capture: sha256:0b6cad6fa176178c5a13ac21b3cf35bf4f629210c2f48608d4ba3d4f5276ec33 | quote: | request rate per credential | 100/s, burst 500 (`429 rate_limited` with `Retry-After`) |
  - [2] 2026-11-24: op results and output are kept for 7 days before 410 op_expired | capture: sha256:0b6cad6fa176178c5a13ac21b3cf35bf4f629210c2f48608d4ba3d4f5276ec33 | quote: | op retention (result and output) | 7 days | `410 op_expired`; the commit stays in `audit` |
  - [6] 2026-11-24: the hosted node endpoint and the signup route | capture: sha256:9f89798c1568c98c377fc0f2c40f9e22fae37bc0fcc07152d79c954e39f1f073 | quote: Hosted node: `https://hel1.sharkmagic.si`. Sign up at [app.sharkmagic.si](https://app.sharkmagic.si/#/signup).
- sources:
  - [1] https://sharkmagic.si/docs/faq
  - [2] https://sharkmagic.si/docs/limits
  - [3] https://sharkmagic.si/docs/billing
  - [4] https://sharkmagic.si/
  - [5] https://app.sharkmagic.si/#/signup
  - [6] https://sharkmagic.si/docs/
