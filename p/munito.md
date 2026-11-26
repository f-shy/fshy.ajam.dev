# Munito AI

> munito.ai | Inference, Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/munito/ | JSON https://fshy.ajam.dev/api/v1/entity/munito.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Munito AI

- `inference/munito` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.munito.ai/pricing
- disagrees on verdict: `inference/munito` says qualifies-with-caveat, `inference/munito-eu` says fails-identity
- free tier: A free tier open to a new account with a verified phone number, when capacity is available; at a zero balance the account continues on the free tier, and paid routes start at USD 0.099 per 1M input tokens. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: the free tier requires a verified phone number on the account
- interface: rest
- limits:
  - request-rate (binding): free-tier use depends on available capacity [1]
- endpoint: https://api.munito.ai/inference/v1
- composes with: capacity is the scarce link, so a free-tier plan cannot be depended on at a fixed hour
- reliability: the free tier is explicitly capacity-gated, so a request can be refused while the account is in good standing
- evidence:
  - [1] 2026-11-18: a phone-verified account can use the free tier when capacity is available, and a zero balance falls back to it | capture: sha256:2cc7770abad2e9b625d84f4b344044ff05fe8f3a72b839e87bb968923f6ecf2a | quote: - Free tier. A new account with a verified phone number can use the free tier, when capacity is available.
- sources:
  - [1] https://docs.munito.ai/pricing

## Munito

- `compute/munito-sandboxes-trial` | trial-only | evidence documented | binding volume-quota | category sandbox compute (Linux microVM) | tier Sandboxes Trial
- needs card yes, phone yes, ID no, institution no | verified 2026-11-24T10:11:14.932Z (live) | stale on 2026-12-25
- url https://munito.ai/pricing
- free tier: The trial gives $0.90 of sandbox time for 7 days; during it the organization runs 2 sandboxes at once, each at most 4 vCPUs and 8 GiB with a timeout of at most 7,200 seconds. A card is added to start and is not charged then. Separate from sandboxes, the inference service has a free tier on spare capacity for a new account with a verified phone number, with daily token limits. | unit: credits | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: USD 0.90 of time at USD 0.018 an hour for the default 2 vCPU / 4 GiB size is 50 hours; quota is in credits and metered by the second. The inference free tier belongs to the separate inference offer and its daily cap is 2,000,000 tokens for four named chat models and 4,000,000 for each other chat model.
- per-object cap: not applicable: the unit is a machine, not an object; the largest custom size is 16 vCPUs and 32,768 MiB, and a file write is at most 100 MiB
- retention: A sandbox runs until its timeout or a delete and its files go with a delete; a persistent sandbox keeps files and processes across a pause and its saved state is priced at $0.0002 per GiB-hour while the sandbox runs and while it is paused. | source: [2]
- egress: A new sandbox has no outbound internet access; setting "internet": true enables it, and SMTP mail is not available. Inbound connections come only through ports and SSH. No outbound volume allowance or per-TB price is published. | metered: no | source: [2]
- identity: card | detail: Adding a card on the Billing page starts the trial and is not charged then; the card requires 3D Secure in some jurisdictions. Registration offers email, Google and GitHub sign-in. The separate inference free tier requires a verified phone number, which the sandbox trial does not state.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): $0.90 of sandbox time over 7 days; usage past the card-free trial needs a plan [1]
  - request-rate: 2 sandboxes at once during the trial; each at most 4 vCPUs and 8 GiB and a timeout of at most 7,200 seconds; 8,000 API requests a minute from one IP [2]
- limits note: A sandbox runs for 10 to 86,400 seconds and 7,200 at most during the trial. A command runs at most 1,800 seconds, writes a file of at most 100 MiB and returns at most 1 MiB per stream.
- binding note: The USD 0.90 credit, 50 hours at the default size, ends within the 7-day window and stops the sandboxes when used up, before the concurrency and per-command caps bind a single job.
- interface detail: An OpenAI-compatible REST API creates sandboxes, runs commands and reads and writes files; a CLI runs a coding agent in a sandbox with one command; SSH takes public keys and no password, and public ports are exposed at a URL per port.
- endpoint: https://console.munito.ai/registration
- tooling: the REST API, the Python and TypeScript SDKs and the munito command line tool; a sandbox starts from a base, ubuntu, agent or desktop template or a custom container image
- composes with: A paid plan after the trial sets how many sandboxes run at once (50 for Starter, 2,000 for Fleet) and pays its price back as credits; the same credit balance pays the open-model inference API, so a job chain can run code and call a model without a second vendor, and outputs must be written to another record's storage to survive a sandbox delete.
- reliability: A sandbox that reaches its timeout or whose credits run out stops; with automatic top-up off, the sandboxes stop when the balance is spent. Sandboxes on one host share its vCPUs, so a busy host slows a command, and a create above the plan's concurrency gets 429.
- notes: The sandbox trial is $0.90 of time for 7 days over two sandboxes, and a paid plan is required when it ends. From 2026-11-21 the global standard rate of DeepSeek-V4-Flash is $0.099 per million input tokens, $0.019 cached and $0.25 output; the sandbox default size costs $0.018 an hour. A hosted sandbox service; the software is run by the vendor, not installed by the user.
- evidence note: The credit, 7 days, two sandboxes, sizes and timeouts, card gate, sign-in options, network default and the per-size rates are quoted from the vendor's pricing pages read on 2026-11-24. The signup page quote establishes the email and social options.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 10
  - shape.gpu_class: NVIDIA L4 optional at $0.78 per hour
  - shape.note: the default sandbox preset; tiny, small, large and custom sizes are published
  - billing_model: 7-day card-gated trial with a fixed credit, then a monthly plan plus per-second usage
  - free_tier_kind: time-boxed-trial
  - term: 7 days
  - price_arithmetic: $0.018 per hour for the default 2 vCPU / 4 GiB size; $0.90 is about 50 hours
  - status: published trial
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 16 public ports per sandbox
  - network_out.note: outbound is off by default and enabled with internet: true; no volume price is published
  - session_cap.wall_clock_min: 120
  - session_cap.restart_required: no
  - session_cap.note: a sandbox timeout is at most 7,200 seconds during the trial
- evidence:
  - [1] 2026-11-24: the trial gives $0.90 of sandbox time for 7 days | capture: sha256:1304e1c10b1f9e7bf68c3fbc25c09c0e3062f72fbcda6882e236c914fce63b98 | quote: The trial gives $0.90 of sandbox time for 7 days. After it, sandboxes need a plan.
  - [2] 2026-11-24: the trial starts with a card that is not charged, runs two sandboxes at once and caps their size and timeout | capture: sha256:ebb5a66112f66d76a3c7234a1c98ee468ddd53251ab7b2ca858b96c292fae69f | quote: During the trial, your organization runs 2 sandboxes at once. Each one has at most 4 vCPUs and 8 GiB, and a `timeout` of at most 7,200 seconds.
  - [2] 2026-11-24: a new sandbox has no outbound internet access and inbound connections come only through ports and SSH | capture: sha256:ebb5a66112f66d76a3c7234a1c98ee468ddd53251ab7b2ca858b96c292fae69f | quote: A new sandbox has no outbound internet access. Set
  - [3] 2026-11-24: registration offers email, GitHub and Google as sign-in options | capture: sha256:2ece91464a89561cab8b1083617b9556e1adfabf61d3b283be5cb3c6b726f42d | quote: Continue with GitHubContinue with Google
  - [4] 2026-11-24: the inference free tier is limited to 2,000,000 tokens a day for four chat models and 4,000,000 for each other chat model | capture: sha256:535cb8df8b4b02f756ef824fda2e19bb5a1cd5d50713f16d6254df25a19c194d | quote: `deepseek-ai/deepseek-v4.1-flash-1017`, `munito/deepseek-v4.1-flash-1017-abliterated`, `zai-org/glm-5.3-flash` and `deepseek-ai/deepseek-v4-flash`: 2,000,000 tokens a day each.
  - [4] 2026-11-24: each other chat model has a daily cap of 4,000,000 tokens | capture: sha256:535cb8df8b4b02f756ef824fda2e19bb5a1cd5d50713f16d6254df25a19c194d | quote: Each other chat model: 4,000,000 tokens a day.
  - [5] 2026-11-24: the standard global price of DeepSeek-V4-Flash is $0.099 input, $0.019 cached input and $0.25 output per million tokens | capture: sha256:a3aaf91612179a381a8619d30be6418b503807c136c61b44c0da26cd7fc24b4f | quote: Global | `standard` | $0.099 | $0.019 | $0.25
- sources:
  - [1] https://munito.ai/pricing
  - [2] https://docs.munito.ai/sandboxes/pricing
  - [3] https://console.munito.ai/registration
  - [4] https://docs.munito.ai/rate-limits
  - [5] https://docs.munito.ai/pricing

## Munito AI Sandboxes

- `compute/munito-sandboxes` | trial-only | evidence documented | binding volume-quota | category container and VM sandbox | tier Trial ($0 for 7 days)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.610Z (live) | stale on 2026-12-26
- url https://munito.ai/pricing
- duplicate of `compute/munito-sandboxes-trial`
- free tier: A trial of $0 for 7 days with 2 sandboxes at once, giving $0.90 of sandbox time, 25 hours of 4 vCPUs and 8 GiB, that needs a card to start; after the trial every sandbox needs a paid plan. | unit: hours | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The $0.90 credit at the default 2 vCPU and 4 GiB rate of $0.018 an hour is 50 hours; the docs quote 25 hours of the larger 4 vCPU and 8 GiB size. The free tier for model inference on spare capacity with a verified phone is a separate offer and is recorded under inference/munito.
- per-object cap: 100 MiB per file written through the sandbox file API | bytes: 104857600 | source: [1] | note: The unit is a machine, not a stored object; the file limit is the closest published per-item ceiling.
- retention: A sandbox lives 10 to 86,400 seconds and defaults to 3,600 seconds; at most 7,200 seconds during the trial. A paused persistent sandbox keeps files and processes while its saved state bills at $0.0002 per GiB-hour. | source: [1]
- egress: unverified: no egress price or allowance is published for sandboxes; a new sandbox has no outbound internet access until internet is set to true, and inbound reaches it only through ports and SSH | metered: no | source: [1]
- identity: card | detail: Sign-up offers GitHub, Google or email (https://console.munito.ai/registration). The sandbox trial needs a card saved on the Billing page: 'Add a card to start' and 'To start, add a card on the Billing page of the console. The card is not charged then.' No phone or identity document is asked for to start a sandbox; a verified phone appears only on the separate model-inference free tier.
- interface: cli, ssh, rest
- limits:
  - volume-quota (binding): $0.90 of sandbox time for 7 days, or 25 hours of 4 vCPUs and 8 GiB, then a paid plan [1]
  - request-rate: API requests from one IP address are limited to 8,000 a minute [1]
  - per-object-cap: 100 MiB per file; command output 1 MiB for each stream when waiting for the result [1]
  - retention-clamped: a sandbox runs 10 to 86,400 seconds, at most 7,200 seconds during the trial, default 3,600 [1]
- limits note: During the trial an organization runs 2 sandboxes at once, each at most 4 vCPUs and 8 GiB; command runs last 1 to 1,800 seconds. A new sandbox starts with no outbound internet access.
- binding note: The $0.90 credit for 7 days runs out before the 8,000-per-minute IP rate or the per-file cap does.
- interface detail: A TypeScript client and an npm CLI create sandboxes, run commands and write files through a REST API; shells, SSH, open ports and a desktop are available inside a sandbox.
- endpoint: https://console.munito.ai
- tooling: npm install -g @munitoai/cli, then munito login, munito create, munito exec and munito rm; the TypeScript client is @munitoai/cli.
- composes with: A 2 vCPU and 4 GiB sandbox at $0.018 an hour supplies an isolated Linux machine for agents; a paused persistent sandbox keeps a warmed toolchain for forks, and files must be copied to a separate object-storage record for long-term retention.
- reliability: A create, resume, fork or new timeout is refused with 402 if there is no card, no plan or no credit; when the trial credit runs out, running sandboxes stop with end_reason credits. Sandboxes on one host share its vCPUs, so a busy host slows commands.
- notes: The hosted sandbox is billed by the second, with a card-gated 7-day trial and monthly plans from $15 to $1,995 a month. The model-inference free tier, which needs a verified phone, is a separate offer recorded under inference/munito.
- evidence note: The plan table, trial credit, rates, limits and card gate are read from the vendor's pricing and sandbox-pricing pages on 2026-11-25 and quoted below. The egress price was not published and is left unverified.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 10
  - shape.gpu_class: NVIDIA L4 add-on at $0.78 an hour
  - billing_model: per-second usage against a trial credit, then a monthly plan whose price returns as credits
  - free_tier_kind: trial-credit
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: the trial lasts 7 days; a sandbox may run 10 to 86,400 seconds and defaults to 3,600
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 16 public ports for each sandbox
- evidence:
  - withheld 2026-11-25: the operator's list places Munito at $0.018 an hour with a 50-hour one-time free tier; a lead, not the basis for the record's values | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: 15. Munito → $0.018/h · billed per second
  - [2] 2026-11-25: the sandbox rate is $0.018 an hour for 2 vCPUs and 4 GiB, billed each second | capture: sha256:1304e1c10b1f9e7bf68c3fbc25c09c0e3062f72fbcda6882e236c914fce63b98 | quote: Every plan pays the same rates, $0.018 an hour for 2 vCPUs and 4 GiB, for each second that a sandbox runs.
  - [2] 2026-11-25: the trial lasts 7 days, gives $0.90 of sandbox time and needs a card to start | capture: sha256:1304e1c10b1f9e7bf68c3fbc25c09c0e3062f72fbcda6882e236c914fce63b98 | quote: The trial gives $0.90 of sandbox time for 7 days. After it, sandboxes need a plan.
  - [2] 2026-11-25: the paid sandbox plans start at $15 a month after the trial | capture: sha256:1304e1c10b1f9e7bf68c3fbc25c09c0e3062f72fbcda6882e236c914fce63b98 | quote: - ### Starter $15 a month 50 sandboxes at once
  - [1] 2026-11-25: the card starts a trial of $0.90 of sandbox time, 25 hours of 4 vCPUs and 8 GiB, over 7 days | capture: sha256:41f35c5a42f586769c3ba00660ed8d1cd65a3777e43aeefad8da1f165efd291f | quote: The card starts a trial: $0.90 of sandbox time, 25 hours of 4 vCPUs and 8 GiB, for 7 days.
  - [1] 2026-11-25: the default preset is 2 vCPUs and 4 GiB at $0.018 an hour, and the sizes are published | capture: sha256:41f35c5a42f586769c3ba00660ed8d1cd65a3777e43aeefad8da1f165efd291f | quote: | `default` | 2 | 4 GiB | $0.018 |
  - [1] 2026-11-25: one IP address is limited to 8,000 API requests a minute | capture: sha256:41f35c5a42f586769c3ba00660ed8d1cd65a3777e43aeefad8da1f165efd291f | quote: Creates | No limit. API requests from one IP address are limited to 8,000 a minute
  - [1] 2026-11-25: a sandbox has no outbound internet access until internet is set to true | capture: sha256:41f35c5a42f586769c3ba00660ed8d1cd65a3777e43aeefad8da1f165efd291f | quote: - A new sandbox has no outbound internet access. Set `"internet": true` to enable it.
  - [1] 2026-11-25: the file limit is 100 MiB and the sandbox life is 10 to 86,400 seconds, at most 7,200 during the trial | capture: sha256:41f35c5a42f586769c3ba00660ed8d1cd65a3777e43aeefad8da1f165efd291f | quote: | File | 100 MiB
  - [3] 2026-11-25: the sign-up page offers GitHub, Google or email and no phone or card field | capture: sha256:c0f0eeb06a1c90e89c829537bbdaa2a31899ed70a8354834e4c497b7729134ea | quote: Continue with GitHubContinue with Google Or Email
  - [4] 2026-11-25: the sandbox product is hosted and is reached through a TypeScript client, an npm CLI, a shell and SSH | capture: sha256:f983876525d102e2cca218a179550ff55faab40035c9306e089324c52eae5712 | quote: A shell, a browser, SSH, open ports and a desktop. Give an agent the machine, and the agent works the way a person would.
- sources:
  - [1] https://docs.munito.ai/sandboxes/pricing
  - [2] https://munito.ai/pricing
  - [3] https://console.munito.ai/registration
  - [4] https://munito.ai/sandboxes

## Munito AI (EU)

- `inference/munito-eu` | fails-identity | evidence documented | binding volume-quota | category inference gateway (EU region)
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.munito.ai/pricing
- disagrees on verdict: `inference/munito` says qualifies-with-caveat, `inference/munito-eu` says fails-identity
- free tier: A new account with a verified phone number can use the free tier, when capacity is available. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: a verified phone number is required to enter the free tier; capacity must also be available
- interface: rest
- limits:
  - volume-quota (binding): free tier usage when capacity is available; at a zero balance the account continues on the free tier [1]
- endpoint: https://api.eu.munito.ai/inference/v1
- composes with: This is the EU-hosted variant of Munito AI (api.eu.munito.ai); the free tier and its phone gate are documented on the shared pricing page. The /regions page fetched for this id only lists base URLs.
- reliability: the free tier is capacity-dependent; 421 if a data-region request goes to the wrong regional host
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: the Munito AI free tier is open to a new account with a verified phone number, subject to capacity | capture: sha256:2cc7770abad2e9b625d84f4b344044ff05fe8f3a72b839e87bb968923f6ecf2a | quote: A new account with a verified phone number can use the free tier, when capacity is available.
- sources:
  - [1] https://docs.munito.ai/pricing
