# Chalk Compute

> chalk.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chalk/ | JSON https://fshy.ajam.dev/api/v1/entity/chalk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chalk Compute (Sandboxes)

- `compute/chalk-compute-sandboxes` | paid-only | evidence documented | binding volume-quota | category agent sandbox platform | tier Standard, per-second runtime
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:55:06.399Z (live) | stale on 2026-12-26
- url https://chalk.ai/capabilities/sandboxes
- free tier: None stated: the pricing page says 'Get started today and only pay for what you use, at per-second granularity. No up-front costs.' Runtime, including sandboxes, is billed by requested resources at $0.0249 per vCPU-hour and $0.0080 per GiB-hour preemptible, with GPUs from $0.54 an hour for a T4 and $4.29 an hour for an H100. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: There is no free monthly allowance or trial allowance on the read pages; the billing docs say Context nodes are billed by uptime and Runtime and Learning by per-second resource requests. The sign-up page shows no card field, and the card gate inside the dashboard is unverified: behind a sign-up.
- per-object cap: not applicable: the unit is a machine, not an object. Volumes are $0.09 per GiB-month and a sandbox mounts versioned volumes for repos, datasets or model weights. | source: [1]
- retention: A Sandbox is an isolated environment for a single ephemeral task, torn down when the task finishes; no post-run file retention period is published on the read pages and is unverified: behind a sign-up. | source: [2]
- egress: Network egress is $0.04 per GiB and ingress has no charge. Sandboxes inside a customer cloud account default-deny egress with hostname, CIDR and port allowlists; a hosted lane routes tool calls through the Chalk MCP gateway. | metered: yes | source: [1]
- identity: email | detail: The self-service signup page is titled 'Get started with Chalk'; its browser-rendered form shows 'Email' beside an 'or' selector and a 'Log in' link, with no phone, document or card field in the rendered page. The plain HTML fetch renders only a loading spinner, which is why the field was missed earlier. The hosted serverless lane says 'Sign up and your environment is ready.' The card gate inside the dashboard is unverified: behind a sign-up.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): runtime is metered by the second as (vCPU x CPU rate + GiB x memory rate + GPUs x GPU rate) x runtime, with no free runtime allowance stated [1]
  - write-gated: non-preemptible workloads run for up to 24 hours; custom non-preemptible durations require Enterprise [1]
  - per-ip-shaping: network egress is $0.04 per GiB, with default-deny egress controlled by hostname, CIDR and port allowlists [1]
- limits note: Not every GPU type is available in every environment; quotas are listed in the Chalk dashboard. Committed-use contracts unlock volume discounts and self-hosted deployment options on Enterprise.
- binding note: No free runtime allowance is published and the meter starts at the per-second resource rate, so usage cost binds before the 24-hour non-preemptible duration or the egress price.
- interface detail: A Sandbox is defined and invoked in Python through the chalkcompute SDK; the docs also describe a REST API and a chalk CLI usage command, and a hosted serverless lane reached by signup.
- endpoint: https://api.chalk.ai
- tooling: the chalkcompute Python SDK, the chalk CLI and the dashboard; no SSH endpoint or rclone backend is published for the sandbox.
- composes with: A sandbox can be given a knowledge cutoff so the MCP gateway replays tools and context against a consistent historical snapshot, and versioned volumes let parallel sandboxes mount the same repo, dataset or model.
- reliability: Preemptible rates apply unless non-preemptible workloads are explicitly requested, and they run at most 24 hours; Context node cost is independent of load and the branch server shuts down after a default idle period of 1 hour. Sandboxes are torn down when a task finishes, so unsaved work is lost.
- notes: Hosted serverless Chalk Sandboxes bill per second at $0.0249 per vCPU-hour plus $0.0080 per GiB-hour preemptible with no free allowance; the operator's list prices the 2 vCPU/4 GB shape at $0.245 an hour. A separate enterprise lane deploys the same software inside the customer's own cloud; that deployment is self-hosted and is not recommended while the hosted paid lane exists. No public free tier or trial was found on the read pages.
- evidence note: Rates, egress price, the per-second billing formula, the ephemeral sandbox definition and the two deployment lanes are quoted from first-party pages read on 2026-11-25. The signup Email field was read from a browser-rendered capture of the same URL; the in-dashboard card gate is unverified: behind a sign-up.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.gpu_class: NVIDIA H100 80 GB, T4 16 GB, L4 24 GB and others
  - shape.gpu_count: 1
  - shape.note: the operator's price list uses a 2 vCPU / 4 GB shape at $0.245 an hour and lists an NVIDIA T4 16 GB sandbox at $0.54 an hour
  - billing_model: pay as you go per second for requested resources; committed-use contracts on Enterprise
  - free_tier_kind: none published
  - term: month-to-month, no up-front cost
  - price_arithmetic: $0.0249 per vCPU-hour x 2 + $0.0080 per GiB-hour x 4 = $0.0818 an hour preemptible for 2 vCPU / 4 GiB; the operator's list price is $0.245 an hour
  - status: public serverless tier plus sales-led private-cloud deployment
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: hostnames, CIDRs and ports can be allowlisted; default-deny egress in private-cloud sandboxes
  - session_cap.restart_required: no
  - session_cap.note: a sandbox is torn down when its task finishes; non-preemptible workloads run up to 24 hours
- evidence:
  - withheld 2026-11-25: the operator's price list gives Chalk Compute (Sandboxes) at USD 0.245 per hour, billed per second | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: Chalk Compute (Sandboxes) → $0.245/h · billed per second
  - [1] 2026-11-25: preemptible compute is $0.0249 per vCPU-hour and $0.0080 per GiB-hour, with non-preemptible at $0.0747 and $0.0240, and non-preemptible runs are capped at 24 hours | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: CPU | $0.0249 / vCPU / hr | $0.0747 / vCPU / hr
  - [1] 2026-11-25: GPU rates include $4.29 an hour for an H100 80 GB, $0.54 an hour for a T4 16 GB and $0.74 an hour for an L4 24 GB | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: | NVIDIA H100 (80 GB) | $4.29 / hr |
  - [1] 2026-11-25: network egress is $0.04 per GiB, ingress is free and volumes are $0.09 per GiB-month | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: Network egress | $0.04 / GiB
  - [1] 2026-11-25: Runtime workloads including sandboxes bill by requested vCPU, memory and GPUs per second with no up-front cost | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: Get started today and only pay for what you use, at per-second granularity. No up-front costs.
  - [2] 2026-11-25: a Sandbox is an ephemeral task torn down when the task finishes, and Chalk offers managed or self-hosted infrastructure | capture: sha256:dfbac255113947e931e374a6b630d28c29b042393bb955c1d06bddc64ba1ebb7 | quote: Sandbox: an isolated environment for a single ephemeral task, torn down when the task finishes.
  - [3] 2026-11-25: Chalk Compute is a hosted control plane that deploys sandboxes entirely inside the customer's private cloud | capture: sha256:c204995852fab7ef3e6c0ea9ce73ed58a9ecdcc531591a849cbb36818366b3a6 | quote: Chalk Compute is an enterprise-grade agent runtime that deploys sandboxes directly inside your private cloud.
  - [4] 2026-11-25: a fully managed serverless lane exists with no cloud account to connect and signup-based access | capture: sha256:ce0bee7f3f006580f2900d42d897d5c6897238da248961cc50ae3d3bb9d8ae23 | quote: No cloud account to connect and no cluster to configure. Chalk runs the infrastructure, so you go straight to building agents, LLM applications and real-time decision systems.
  - [4] 2026-11-25: the hosted lane lets a user sign up and get an environment ready without provisioning a cluster | capture: sha256:ce0bee7f3f006580f2900d42d897d5c6897238da248961cc50ae3d3bb9d8ae23 | quote: Sign up and your environment is ready.
  - [5] 2026-11-25: form fields load client-side | capture: sha256:34873b9e3dc69eb288006c62a349d1cb31d5718689d6951291d4b00e2f47d38f | quote: Get started with Chalk
  - [5] 2026-11-25: the browser-rendered signup form names an Email field, so email identity is stated | capture: sha256:7c3dbbfa8de11612deb06ec4a13d78635a7707d8182bd56ea3047a975d54efb8 | quote: Get started with Chalk or Email
  - [1] 2026-11-24: the Standard Runtime CPU rate is $0.0249 per vCPU-hour preemptible and $0.0747 non-preemptible | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: | CPU | $0.0249 / vCPU / hr | $0.0747 / vCPU / hr |
  - [1] 2026-11-24: network egress is $0.04 per GiB and network ingress has no charge | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: | Network egress | $0.04 / GiB |
  - [1] 2026-11-24: the Standard tier is pay as you go with per-second granularity and no up-front cost, with no stated free allowance | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: Get started today and only pay for what you use, at per-second granularity. No up-front costs.
  - [1] 2026-11-24: preemptible is the default and non-preemptible workloads run for up to 24 hours | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: Preemptible rates apply unless you request non-preemptible workloads, which run for up to 24 hours.
  - [1] 2026-11-24: volumes are billed at $0.09 per GiB per month on the Standard tier | capture: sha256:958f58f7a7663853d25f193b2cc818d8a7bc294f18a7be0282d2e5a38420985d | quote: | Volumes | $0.09 / GiB / mo |
  - [6] 2026-11-24: login offers an email option and a demo is the offered way to try Chalk; no card field appears on the login page | capture: sha256:2b7659048fe1925b39c18f3ed88add654ac6b12e321b62c77d0ae98971df50ec | quote: Not yet using Chalk? [Book a demo to take a test drive →](https://chalk.ai/book-demo)
  - [7] 2026-11-24: creating a sandbox requires the deploy.create permission held by Admin, Owner or Team Manager roles | capture: sha256:689d74641c3db46c20bf76ce76f64c9c359ae45c841c9ab278e8fa8a4f4462da | quote: | Create a sandbox, function, or scaling group | `deploy.create` | Admin, Owner, Team Manager |
  - [3] 2026-11-24: Chalk Compute deploys sandboxes inside the customer's own cloud, so it is not a hosted capacity service | capture: sha256:c204995852fab7ef3e6c0ea9ce73ed58a9ecdcc531591a849cbb36818366b3a6 | quote: Chalk Compute is an enterprise-grade agent runtime that deploys sandboxes directly inside your private cloud.
  - [2] 2026-11-24: a sandbox is an ephemeral task torn down when the task finishes | capture: sha256:dfbac255113947e931e374a6b630d28c29b042393bb955c1d06bddc64ba1ebb7 | quote: Sandbox: an isolated environment for a single ephemeral task, torn down when the task finishes.
- sources:
  - [1] https://chalk.ai/pricing
  - [2] https://docs.chalk.ai/docs/compute/overview
  - [3] https://chalk.ai/blog/chalk-compute
  - [4] https://chalk.ai/deployments/chalk-hosted
  - [5] https://chalk.ai/signup
  - [6] https://chalk.ai/login
  - [7] https://docs.chalk.ai/docs/setup-guide
