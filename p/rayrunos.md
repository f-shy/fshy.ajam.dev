# Rayrun

> rayrunos.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rayrunos/ | JSON https://fshy.ajam.dev/api/v1/entity/rayrunos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rayrun

- `compute/rayrun` | qualifies-with-caveat | evidence documented | binding volume-quota | category microVM sandbox | tier Pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:55:06.271Z (live) | stale on 2026-12-26
- url https://rayrunos.com/docs/pricing/
- free tier: 注册时赠送 ¥50 初始余额 (CNY 50 starting balance on registration). Charges are per second with no monthly fee and no minimum spend. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The CNY 50 balance is one-time. The vendor's own rate card prices a 2 vCPU / 4 GiB sandbox at CNY 0.10 an hour, so the credit is 500 hours of that size. Paused and stopped sandboxes incur storage only, with 32 GiB free per sandbox.
- per-object cap: The default workspace is 32 GiB and each sandbox gets 32 GiB of storage free; storage past 32 GiB is CNY 0.50 per GiB-month at the declared workspace size. | source: [1]
- retention: A paused or stopped sandbox keeps its process state, workspace and IP; a terminated sandbox is irreversible and deletes the disk. When the balance is exhausted sandboxes are cold-stopped with data kept, then destroyed after a grace period of 3 days, or 1 day for trial organisations. | days: 3 | source: [1]
- egress: 出向流量 ¥0.60 / GB (CNY 0.60 per GB of outbound traffic), billed per second and settled hourly. Egress is denied by default and each attempt is logged; an allowlist is set at create or changed at runtime. | metered: yes | source: [1]
- identity: email | detail: The dashboard registration form asks for email, username, password and confirmation password. No phone number or ID document is shown. Creating an account creates an organisation and grants the CNY 50 balance.
- interface: rest, cli, ssh
- limits:
  - volume-quota (binding): CNY 50 one-time starting balance; pay-as-you-go with no minimum spend [1]
  - volume-quota (binding): CNY 0.03 per vCPU-hour and CNY 0.01 per GiB-hour; a 2 vCPU / 4 GiB sandbox is CNY 0.10 an hour [1]
  - volume-quota (binding): CNY 0.60 per GB outbound traffic and CNY 0.50 per GiB-month above 32 GiB per sandbox [1]
- limits note: Memory is rounded up to whole GiB; compute and egress are metered by the second and settled hourly; storage is metered by the second and billed monthly. Trial organisations have 1 day of arrears grace instead of 3.
- binding note: The one-time CNY 50 balance is the first limit reached: at CNY 0.10 an hour it is 500 hours of a 2 vCPU / 4 GiB sandbox, before outbound traffic or storage above 32 GiB is charged.
- interface detail: A web console, a downloaded CLI binary and a REST API at api.rayrunos.com/v1; an E2B-compatible endpoint uses E2B_API_URL and E2B_API_KEY. A web terminal and SSH are documented.
- tooling: rayrun CLI binary for Linux, macOS and Windows; REST API; E2B SDK compatibility for create, list and delete.
- composes with: A sandbox can be created from the CLI, console or API with an egress allowlist; keys are injected by the platform rather than stored in the image, and files persist across stops until the sandbox is destroyed.
- reliability: Egress is denied by default so package installs need an explicit allowlist; when balance runs out sandboxes are cold-stopped and destroyed after a 1-day grace period for trial organisations, and destruction deletes workspace data irreversibly.
- notes: The per-unit rates are CNY 0.03 per vCPU-hour and CNY 0.01 per GiB-hour, so the 2 vCPU / 4 GiB box is CNY 0.10 an hour; the vendor quotes USD 1 to CNY 6.82, which is about USD 0.0147 an hour. CNY 50 buys 500 hours of that box. Outbound traffic is CNY 0.60 per GB and storage above 32 GiB is CNY 0.50 per GiB-month. The pricing page documents a hosted microVM service; a self-hosted CLI mode is mentioned for E2B compatibility but is not the offer priced here.
- evidence note: The per-unit rates, starting balance, storage and egress terms, registration fields and lifecycle rules were read from first-party Chinese pages.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 32
  - billing_model: per-second, prepaid balance
  - free_tier_kind: one-time-credit
  - term: no monthly fee, no minimum spend
  - price_arithmetic: 2 x CNY 0.03 + 4 x CNY 0.01 = CNY 0.10/hour; CNY 50 / CNY 0.10 = 500 hours
  - status: live hosted service
  - network_out.allow_outbound: yes
  - network_out.ports: not stated; egress allowlist and a web terminal are documented
  - session_cap.restart_required: no
  - session_cap.note: pause and stop preserve process memory and files; pause resumes in 7 ms; destroyed sandboxes delete the workspace
- evidence:
  - [1] 2026-11-25: vCPU price is CNY 0.03 per vCPU-hour | capture: sha256:94231b91f802bf61e8abb7d7ac6d155ee16c4374fbee0d4993d1bb076a64243d | quote: vCPU | ¥0.03 / vCPU · 小时
  - [1] 2026-11-25: outbound traffic price is CNY 0.60 per GB | capture: sha256:94231b91f802bf61e8abb7d7ac6d155ee16c4374fbee0d4993d1bb076a64243d | quote: 出向流量 | ¥0.60 / GB
  - [1] 2026-11-25: registration grants a one-time CNY 50 initial balance | capture: sha256:94231b91f802bf61e8abb7d7ac6d155ee16c4374fbee0d4993d1bb076a64243d | quote: 注册时赠送 ¥50 初始余额。
  - [1] 2026-11-25: a 2 vCPU / 4 GiB sandbox costs CNY 0.10 an hour and each sandbox has 32 GiB of storage free | capture: sha256:94231b91f802bf61e8abb7d7ac6d155ee16c4374fbee0d4993d1bb076a64243d | quote: 每沙盒 32 GiB 内免费
  - [1] 2026-11-25: the trial organisation's arrears grace period is 1 day | capture: sha256:94231b91f802bf61e8abb7d7ac6d155ee16c4374fbee0d4993d1bb076a64243d | quote: 宽限期（默认 3 天，自助注册/试用组织 1 天）内补足余额后
  - [2] 2026-11-25: the registration page asks for email, username, password and confirmation password | capture: sha256:dd9e15e371b9c6b0b4dd49deaef9ae1d6417aeb7f67ce753882788ab294d18e2 | quote: 注册即代表已阅读并同意我们的
  - [2] 2026-11-25: registration grants CNY 50 to spend on sandboxes and trial data is kept 1 day after arrears | capture: sha256:dd9e15e371b9c6b0b4dd49deaef9ae1d6417aeb7f67ce753882788ab294d18e2 | quote: 注册即送 ¥50 体验金，可直接用于创建沙箱；试用期欠费后数据保留 1 天
  - [3] 2026-11-25: egress is denied by default and every attempt is logged | capture: sha256:052685ec1d821e0f625fec557a4362dcb29afb1c97fe0288744ba78395933858 | quote: 联网默认全拒，每笔都记账
  - [4] 2026-11-25: the CLI creates sandboxes and a REST API at api.rayrunos.com/v1 is available | capture: sha256:577ff271379897fd64cba1493409a4f2162585207339e6c5ad7ced1d5254b169 | quote: curl -sS https://api.rayrunos.com/v1/sandboxes
  - [5] 2026-11-24: the Free plan is $0 with no card and no expiry for one developer | capture: sha256:1d82273775a2c106cf53b15f7431484a46040ae73488f00c43bde7a8b8106f80 | quote: - Free $0No card, no expiry. For one developer.
  - [5] 2026-11-24: Free includes 50,000 tool calls a month and then charges $0.20 per thousand | capture: sha256:1d82273775a2c106cf53b15f7431484a46040ae73488f00c43bde7a8b8106f80 | quote: 50,000 tool calls a month, then $0.20 per thousand
  - [5] 2026-11-24: Free includes 25 source-built services, 50 builds a day and 5 GiB of retained images | capture: sha256:1d82273775a2c106cf53b15f7431484a46040ae73488f00c43bde7a8b8106f80 | quote: 50 isolated builds a day and 5 GiB of retained images
  - [5] 2026-11-24: Free keeps 30 days of activity history | capture: sha256:1d82273775a2c106cf53b15f7431484a46040ae73488f00c43bde7a8b8106f80 | quote: 30 days of activity history
  - [5] 2026-11-24: Team is $25 per developer a month and Enterprise starts at $1,500 a month | capture: sha256:1d82273775a2c106cf53b15f7431484a46040ae73488f00c43bde7a8b8106f80 | quote: $25per developer, per month
  - [6] 2026-11-24: sign-up uses GitHub OAuth and the free plan requires no card | capture: sha256:7b2537a51fabf046e3b6b2b9bc637e3c112f28ef192bb0ac512dcbe0bbb90df4 | quote: Sign up with GitHub
  - [7] 2026-11-24: the service runs MCP servers behind one URL and holds credentials | capture: sha256:b55f7da4e93c2672e3e90baabe7a9262cbbd178c0016ab24aec80cc9b52780ad | quote: Your coding agent builds the servers. Rayrun runs them behind one URL and holds the credentials. Each call is decided per client, tool, and argument, then recorded.
  - [7] 2026-11-24: clients connect through a single MCP endpoint and no card is required | capture: sha256:b55f7da4e93c2672e3e90baabe7a9262cbbd178c0016ab24aec80cc9b52780ad | quote: Free for one developer · No card required
- sources:
  - [1] https://rayrunos.com/docs/pricing/
  - [2] https://dashboard.rayrunos.com/register
  - [3] https://rayrunos.com/
  - [4] https://rayrunos.com/docs/quickstart/
  - [5] https://ray.run/pricing
  - [6] https://ray.run/home
  - [7] https://ray.run/
