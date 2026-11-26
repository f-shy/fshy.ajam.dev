# SuperHQ

> nanite.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nanite/ | JSON https://fshy.ajam.dev/api/v1/entity/nanite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SuperHQ (Nanite)

- `compute/superhq-nanite` | paid-only | evidence documented | binding volume-quota | category sandbox | tier Nanite hosted microVM sandboxes (prepaid credit)
- identity a placeholder: card and phone unknown | verified 2026-11-25T02:12:34.813Z (live) | stale on 2026-12-26
- url https://nanite.run/
- free tier: unverified: no free tier, free credit or trial is stated on https://nanite.run/ or https://superhq.ai/; both pages price the hosted sandbox only by component usage drawn down from prepaid credits ('One credit is one US dollar'), with 'No seats, no plans, no minimums' | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The sign-up pages superhq.ai/signup and nanite.run/signup answered HTTP 404 on 2026-11-25, so no new-user credit could be confirmed either way. The shuru runtime under the sandbox is Apache 2.0 software the user installs and runs on a Mac or Linux ARM64 machine; Nanite is the hosted service and is the offer priced here.
- per-object cap: not applicable: the unit is a microVM with a disk and files, not a single object; uploads are written through the filesystem API | note: New sandboxes get a 20 GiB disk; no per-file cap is published on the pages read.
- retention: unverified: no retention period for sandboxes or checkpoints is stated on the pages read; a sleeping sandbox keeps its disk and files, and when credits run out running sandboxes stop and their disks are kept | source: [1]
- egress: $0.15 per GB out: data sent to the internet is billed, data coming in is free; outbound traffic works out of the box | metered: yes | source: [1]
- identity: email | detail: unverified: no public sign-up form was read on 2026-11-25; superhq.ai/signup and nanite.run/signup both answered HTTP 404. An API key is issued by the hosted console, so an email is the nearest kind; whether registration also asks for a card is unverified.
- interface: rest
- limits:
  - volume-quota (binding): 25 concurrent sandboxes per organisation, 100 kept; 4 vCPU, 8 GiB memory and a 20 GiB disk per new sandbox [1]
  - retention-clamped: a sandbox goes to sleep after 30 seconds with nothing running against it; CPU and memory billing stop while asleep [1]
- limits note: Compute is billed per second on actual CPU and memory in use, minimum 0.125 cores in a container is not stated here; arm64 only, x86 binaries are not supported yet, and the service runs in Sydney, Australia for now.
- binding note: No free allowance exists, so the first limit a user meets is the paid prepaid-credit balance and the 25-sandbox concurrency cap; idle sandboxes sleep, so wall-clock runtime is not the binding constraint.
- interface detail: Plain HTTP calls with a bearer key; POST /v1/sandboxes, POST /v1/sandboxes/{name}/exec, PUT /v1/sandboxes/{name}/fs/write, POST /v1/sandboxes/{name}/checkpoint, PUT /v1/sandboxes/{name}/secrets/{key}; interactive sessions use the same routes over a WebSocket. Every endpoint lives under https://api.nanite.run/v1 and takes an API key in the Authorization header.
- endpoint: https://api.nanite.run/v1/sandboxes
- tooling: curl and any HTTP client; a shell over a WebSocket; the shuru CLI is the open-source runtime the user can install and run on their own Mac or Linux ARM64 machine, listed last and not the hosted offer priced here.
- composes with: Prepaid credits draw down per second across sandboxes; a sleeping sandbox costs only its disk, so an agent that parks between messages keeps its files for later calls, and secrets are injected by the proxy only to hosts the user names.
- reliability: A sandbox sleeps after 30 seconds idle and wakes on the next request with its files intact; when prepaid credits run out, running sandboxes stop and keep their disks until the user tops up.
- notes: Hosted compute only: a Nanite microVM with root, 2 vCPU, 2 GiB memory and a 20 GiB disk, or 4 vCPU, 8 GiB and 20 GiB for a new sandbox, billed per second from prepaid credits. Component prices are $0.072/vCPU-hour, $0.0432/GB-hour memory, $0.15/GB-month storage and $0.15/GB out. The 30-second idle sleep makes an idle agent cheap but not free. The self-hosted shuru runtime is listed last and is not the offer priced here.
- evidence note: The prices, sandbox size, concurrency cap, sleep rule and credit terms are quoted from the first-party nanite.run page and the SuperHQ home page read on 2026-11-25; the identity gate and retention period are unverified because the sign-up pages are gone.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 20
  - shape.note: new sandboxes get 4 vCPU, 8 GiB memory and a 20 GiB disk; the home page also mentions a 2 vCPU, 2 GiB, 20 GiB configuration
  - billing_model: prepaid credits, per-second component metering
  - free_tier_kind: none
  - term: no seats, no plans, no minimums
  - price_arithmetic: $0.072 per vCPU hour + $0.0432 per GB hour + $0.15 per GB month storage + $0.15 per GB out
  - status: hosted and priced; sign-up URL answered 404 on 2026-11-25
  - network_out.allow_outbound: yes
  - network_out.ports: preview URLs through the authenticated proxy
  - session_cap.idle_reap_s: 30
  - session_cap.restart_required: no
  - session_cap.note: the sandbox sleeps after 30 seconds idle and wakes with its files intact
- evidence:
  - [1] 2026-11-25: the hosted sandbox bills CPU at $0.072 per vCPU hour, metered per second | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: $0.072per vCPU hour
  - [1] 2026-11-25: memory, storage and outbound network each have a stated usage price, and inbound data is free | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: $0.15per GB out
  - [1] 2026-11-25: a new sandbox is a 4 vCPU, 8 GiB RAM, 20 GiB disk machine, with 25 concurrent sandboxes and 100 kept per organisation | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: New sandboxes get 4 vCPU, 8 GiB of memory and a 20 GiB disk. An organisation can run 25 sandboxes at once and keep 100.
  - [1] 2026-11-25: the sandbox sleeps after 30 seconds idle and only storage is billed while asleep | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: a sandbox goes to sleep after 30 seconds with nothing running against it.
  - [1] 2026-11-25: pricing uses prepaid credits with no seats, plans or minimums | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: +No seats, no plans, no minimums
  - [1] 2026-11-25: the API is plain HTTP over a bearer key, with exec, filesystem, checkpoint and secrets routes | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: * POST/v1/sandboxes/{name}/exec
  - [2] 2026-11-25: the hosted service is Nanite microVMs billed by the second, and shuru is the Apache 2.0 runtime the user can run on their own machine | capture: sha256:cb695c504bdb4e846bac468a3f70348588b143e7065833e708bf17bea9c559c4 | quote: The microVM runtime under every Nanite sandbox, Apache 2.0. Run it on your own Mac to give agents a disposable machine with sane defaults.
  - [3] 2026-11-25: no public sign-up form was available at this URL; the identity gate is unverified | capture: sha256:ec45dec1a7bcb95535810d411e53c4cb63ffc7695d9007090f66b62e42d9c8a4 | quote: Nothing out here.This page does not exist.
  - [4] 2026-11-24: the four published metered rates: USD 0.072 per vCPU hour, USD 0.0432 per GB hour, USD 0.15 per GB month storage and USD 0.15 per GB out | capture: sha256:cf6980301548adb6206fbdce956f3faaf9fe098dee4c1d1623e3ae667587591d | quote: | CPU | $0.072 per vCPU hour | $0.00002 per CPU second | CPU time your code uses. An idle core costs nothing. |
  - [4] 2026-11-24: egress is metered at USD 0.15 per GB out and inbound data is free | capture: sha256:cf6980301548adb6206fbdce956f3faaf9fe098dee4c1d1623e3ae667587591d | quote: Data the sandbox sends to the internet. Data coming in is free.
  - [4] 2026-11-24: a workspace needs at least 0.01 credits to start or wake a sandbox | capture: sha256:cf6980301548adb6206fbdce956f3faaf9fe098dee4c1d1623e3ae667587591d | quote: A workspace needs at least 0.01 credits to start or wake a sandbox.
  - [5] 2026-11-24: a sandbox stops by itself after 30 seconds idle | capture: sha256:98251fefbe4a3282771067ff41292be2b7dac1c4b5e2112fe17274a692f82e54 | quote: A running sandbox stops on its own after 30 seconds with nothing using it.
  - [5] 2026-11-24: creating more than 30 sandboxes in a minute is refused with 429 | capture: sha256:98251fefbe4a3282771067ff41292be2b7dac1c4b5e2112fe17274a692f82e54 | quote: 429 | `sandbox_creation_rate_limited` | 30 sandboxes were created in the last minute.
  - [1] 2026-11-24: an organization can run 25 sandboxes at once and keep 100 | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: An organisation can run 25 sandboxes at once and keep 100. Need more? Write to us.
  - [1] 2026-11-24: the service charges one US dollar per credit, billed by the second, with no seats, plans or minimums | capture: sha256:999fc9c16924ffe0e457b174fb40e73fe64c61a31c8267e23a86dcad3352cdc6 | quote: One credit is one US dollar. Buy credits in the console and usage draws them down by the second. When they run out, running sandboxes stop and their files stay; top up and carry on.
  - [6] 2026-11-24: an API key is created in the console at app.superhq.ai and credits are bought on the Billing page there | capture: sha256:d52be2e0f4e4dba4f2a8f24b898fc62631aeeee0cc57db095f2141ad0c5e8f07 | quote: Sign in to the [console](https://app.superhq.ai/), open API keys in your workspace and create a key.
- sources:
  - [1] https://nanite.run/
  - [2] https://superhq.ai/
  - [3] https://superhq.ai/signup
  - [4] https://nanite.run/docs/billing
  - [5] https://nanite.run/docs/sandboxes
  - [6] https://nanite.run/docs/quickstart
