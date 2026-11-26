# Buildfunctions

> buildfunctions.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/buildfunctions/ | JSON https://fshy.ajam.dev/api/v1/entity/buildfunctions.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Buildfunctions

- `compute/buildfunctions` | qualifies-with-caveat | evidence documented | binding volume-quota | category serverless CPU and GPU sandbox | tier Free plan, usage over $5 monthly CPU credit
- needs card unknown, phone no, ID no, institution no | verified 2026-11-25T11:55:06.399Z (live) | stale on 2026-12-26
- url https://www.buildfunctions.com/pricing
- free tier: The Free plan is $0 and includes $5.00 a month of CPU Functions and CPU Sandboxes usage, with GPU Functions and GPU Sandboxes, custom domains and 3 cron jobs; detailed compute and storage rates are in the estimator. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The $5 monthly CPU credit is the recurring free allowance. CPU Functions and CPU Sandboxes are $0.00001667 per GB-second plus $0.20 per million requests and $0.09 per GB of bandwidth out. GPU Sandboxes are $0.0000126 per vCPU-second, $0.00000137 per GB-second and $0.00013067 per GPU-second. The Pro plan is $20 a month with $20 of usage and 20 GB of model storage; the operator's price list puts Buildfunctions at $0.24 an hour.
- per-object cap: not applicable: the unit is a machine, not an object. GPU Sandboxes can be raised to 75 GB memory and 50 vCPUs on the Free and Pro plans; model storage beyond the included amount is $0.39 per GB-month. | source: [1]
- retention: A sandbox can run for up to 24 hours; retention of files after a run ends is not stated on the pricing or introduction pages and is unverified: behind a sign-up. | source: [2]
- egress: CPU Functions and CPU Sandboxes bill bandwidth out at $0.09 per GB, and GPU Functions and GPU Sandboxes bill bandwidth out at $0.09 per GB; inbound traffic is not priced on the page. The estimator exposes bandwidth out as a billable input for both sandbox classes. | metered: yes | source: [1]
- identity: email | detail: The signup form at www.buildfunctions.com/signup shows a 'Create account' link with Email, Password and 'Show password', plus 'Or continue with' for other providers. No phone or document field appears; the page does not show a card field, and the card gate inside the dashboard is unverified: behind a sign-up.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): $5.00 a month of CPU Functions and CPU Sandboxes usage on Free, then $0.00001667 per GB-second and $0.20 per million requests [1]
  - volume-quota (binding): 3 cron jobs on Free, and 3 on Pro; GPU Sandboxes bill $0.0000126 per vCPU-second, $0.00000137 per GB-second and $0.00013067 per GPU-second [1]
  - per-ip-shaping: bandwidth out is $0.09 per GB for both CPU and GPU Functions and Sandboxes [1]
- limits note: Sandboxes run for up to 24 hours. Pro adds dedicated resources and 20 GB of model storage; storage above that is $0.39 per GB-month. The signup page reads 'Buildfunctions · v0.1.8 · Beta'.
- binding note: The $5 monthly CPU usage credit binds first on Free: GPU Sandboxes have no stated free allowance, so any GPU run is paid from the start.
- interface detail: Sandboxes are created through an SDK and deployed from the dashboard; the docs describe CPUSandbox and GPUSandbox primitives and an SDK for sandboxing agent actions. No SSH endpoint is published on the read pages.
- endpoint: unverified: behind a sign-up
- tooling: the Buildfunctions SDK with CPUFunction, GPUFunction, CPUSandbox and GPUSandbox primitives, plus the dashboard and CLI; no rclone backend is documented.
- composes with: A top-level CPU or GPU Function spawns nested CPU or GPU Sandboxes for untrusted agent actions, with runtime controls for retries, budgets and loop breakers around the call.
- reliability: The service labels itself beta (v0.1.8) on the signup page; bandwidth out is metered at $0.09 per GB and model storage beyond the included amount at $0.39 per GB-month. Post-run sandbox file retention is unpublished.
- notes: Hosted serverless CPU and GPU sandboxes at $0.00001667 per GB-second for CPU and $0.0000126 per vCPU-second plus $0.00000137 per GB-second plus $0.00013067 per GPU-second for GPU, with $5 of monthly CPU usage free on the Free plan. Bandwidth out is metered at $0.09 per GB. Self-hosting of the SDK runtime is not presented as an offer on these pages, and is not recommended while the hosted Free plan exists.
- evidence note: All rates, the $5 free monthly CPU usage, the 24-hour sandbox limit and the signup fields are quoted from first-party pages read on 2026-11-25. Sandbox retention, endpoint and in-dashboard card terms are unverified: behind a sign-up.
- extras:
  - shape.gpu_class: unnamed GPU, model not published
  - shape.gpu_count: 1
  - shape.note: the operator's GPU list gives Buildfunctions $0.47 an hour for an unnamed GPU; GPU Sandboxes can be raised to 50 vCPU and 75 GB
  - billing_model: per-second usage against a $5 monthly CPU credit on Free, $20 monthly Pro subscription with $20 of usage
  - free_tier_kind: recurring usage credit
  - term: month-to-month, beta
  - price_arithmetic: $0.00001667 per GB-second x 3600 seconds x 4 GiB = $0.24 an hour for a 4 GiB CPU sandbox, matching the operator's $0.24 an hour list price
  - status: beta v0.1.8
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: custom domains can be assigned to Functions and Sandboxes
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: sandboxes can run up to 24 hours; post-run file retention is unpublished
- evidence:
  - withheld 2026-11-25: the operator's price list gives Buildfunctions at USD 0.24 per hour, billed per second | capture: sha256:4d220f8008ed2a6126e4b7f8bc4639bd9e625605ec428846fde2bdf593cc5c95 | quote: Buildfunctions → $0.24/h · billed per second (new)
  - [1] 2026-11-25: the Free plan is $0 and includes $5 of monthly CPU usage with CPU and GPU Sandboxes and 3 cron jobs | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: - Build, deploy, and scale CPU Functions, GPU Functions, CPU Sandboxes, and GPU Sandboxes. - Choose from multiple languages and runtimes. - Increase GPU Functions and GPU Sandboxes memory (CPU) to 75 GB. - Increase GPU Functions and GPU Sandboxes vCPU count to 50. - Assign custom domains to Functions. - 3 cron jobs.
  - [1] 2026-11-25: CPU Sandboxes bill $0.00001667 per GB-second, $0.20 per million requests and $0.09 per GB bandwidth out, with $5 of monthly CPU usage included on Free | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Included amount | $5.00 /month
  - [1] 2026-11-25: GPU Sandboxes bill $0.0000126 per vCPU-second, $0.00000137 per GB-second, $0.00013067 per GPU-second and $0.09 per GB bandwidth out | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: | GPU | $0.00013067 /GPU-s | | Bandwidth Out | $0.09 /GB |
  - [1] 2026-11-25: model storage costs $0.39 per GB-month with 20 GB included on Pro; Pro is $20 a month and $192 a year | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: | Storage | $0.39 /GB-month | | Pro Included | 20 GB |
  - [2] 2026-11-25: CPUSandbox and GPUSandbox execute untrusted dynamic agent actions and can run for up to 24 hours | capture: sha256:3c137e5ff583661ea2c2520bb3f956d48a95179ead731a03578fb13606f4e883 | quote: Sandboxes (`CPUSandbox`, `GPUSandbox`): Execute untrusted and dynamic agent actions with full GPU access, automatic model mounting, built-in AI frameworks, runtime dependency installs, and more. They start quickly for isolated tasks and can run for up to 24 hours.
  - [3] 2026-11-25: the signup form asks for Email and Password and offers 'Or continue with' for other providers | capture: sha256:af8b05c9618aa1a4600e70853127bf31fff435becd3f8a2250ffed9408535ed0 | quote: Password
  - [3] 2026-11-25: the signup page labels the service beta at version 0.1.8 | capture: sha256:af8b05c9618aa1a4600e70853127bf31fff435becd3f8a2250ffed9408535ed0 | quote: Buildfunctions · v0.1.8 · Beta
  - [4] 2026-11-25: the login page shows 'Create account' with Email and Password fields | capture: sha256:216e8c4effc474823a77d71172291bdacdf03786ba0c24709ee84bcc0e18cbd5 | quote: Create account
  - [1] 2026-11-24: CPU Functions and Sandboxes are billed at USD 0.00001667 per GB-s | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Memory | $0.00001667 /GB-s
  - [1] 2026-11-24: requests are billed at USD 0.20 per million | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Requests | $0.20 /1M req
  - [1] 2026-11-24: GPU Functions and Sandboxes are billed at USD 0.00013067 per GPU-s | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: GPU | $0.00013067 /GPU-s
  - [1] 2026-11-24: egress is metered at USD 0.09 per GB | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Bandwidth Out | $0.09 /GB
  - [1] 2026-11-24: the included amount of free monthly CPU usage is USD 5.00 per month | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Included amount | $5.00 /month
  - [1] 2026-11-24: the Pro plan is USD 20 per month with 20 GB of model storage included and USD 0.39 per GB-month overage | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Pro includes 20 GB, then $0.39 per GB-month.
  - [1] 2026-11-24: the Free plan includes 3 cron jobs | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: 3 cron jobs.
  - [1] 2026-11-24: additional usage and model storage overage are billed separately from the subscription | capture: sha256:08150b913a1842eeb234dcc28f5303ab50757eaeb0c8e58d300dafcbd918b247 | quote: Additional usage and model storage overage are billed separately and appear as separate invoices.
  - [3] 2026-11-24: the sign-up form asks for Email, Username and Password | capture: sha256:af8b05c9618aa1a4600e70853127bf31fff435becd3f8a2250ffed9408535ed0 | quote: PasswordShow password
  - [3] 2026-11-24: the sign-up page labels the service beta | capture: sha256:af8b05c9618aa1a4600e70853127bf31fff435becd3f8a2250ffed9408535ed0 | quote: Buildfunctions · v0.1.8 · Beta
  - [5] 2026-11-24: an unconfigured sandbox is destroyed after a default timeout of 1 minute | capture: sha256:f8b14ba165cc57fa41d933d151f808a2ed449a4696616ae6dbac9338c023e5c7 | quote: Default Timeout**: If you don't set a `timeout` argument, the default is 1 minute.
  - [2] 2026-11-24: sandboxes can run for up to 24 hours | capture: sha256:3c137e5ff583661ea2c2520bb3f956d48a95179ead731a03578fb13606f4e883 | quote: They start quickly for isolated tasks and can run for up to 24 hours.
- sources:
  - [1] https://www.buildfunctions.com/pricing
  - [2] https://www.buildfunctions.com/docs/introduction
  - [3] https://www.buildfunctions.com/signup
  - [4] https://www.buildfunctions.com/login
  - [5] https://www.buildfunctions.com/docs/sandboxes
