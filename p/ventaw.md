# Ventaw

> ventaw.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ventaw/ | JSON https://fshy.ajam.dev/api/v1/entity/ventaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ventaw

- `compute/ventaw` | qualifies-with-caveat | evidence documented | binding volume-quota | category sandbox | tier Pay as you go
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:55:06.337Z (live) | stale on 2026-12-26
- url https://www.ventaw.com/pricing
- free tier: R500 of welcome credit after the first card payment, once per card; credits never expire. Free accounts can run 2 sandboxes at a time, each with up to 2 vCPU, 2 GB of memory and 5 GB of disk. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1]
- per-object cap: not applicable: the unit is a sandbox with up to 5 GB of disk on a free account, not a stored object
- retention: Files, installed packages and browser logins live on persistent disks and survive restarts; when credits run out, running sandboxes are paused rather than deleted. | source: [1]
- egress: Sandboxes cannot reach each other, private networks or cloud metadata; egress is limited to the public internet. Managed internet transfer is not separately priced on the pricing page. | metered: no | source: [2]
- identity: card | detail: Sign-up asks for first name, surname, email and password, or a third-party sign-in; usage is charged in rand from a prepaid balance topped up by card through Paystack, and the R500 credit is released only after the first card payment. | country: South Africa
- interface: rest, ssh
- limits:
  - volume-quota (binding): R500 of welcome credit after the first card payment, once per card; credits never expire [1]
  - request-rate: free accounts run at most 2 sandboxes at a time, each with up to 2 vCPU, 2 GB of memory and 5 GB of disk [1]
  - volume-quota (binding): first 5 GB of storage free, then R3.00 per GB-month; when credits are used up, sandboxes are paused [2]
- limits note: unverified: the LangChain execute_command tool has a 30-second command timeout and a 180-second default wait for a sandbox or database to start, but no published quota, rate or concurrency cap was readable.
- binding note: The R500 welcome credit is spendable only after a first card payment and bounds how long a sandbox runs; the two-sandbox cap bounds concurrency, not the balance.
- interface detail: A public HTTPS address per sandbox, SSH access, file APIs, a Python SDK and a hosted MCP server at api.ventaw.com/mcp.
- endpoint: https://ventaw.mmogomedia.com/v1
- tooling: Python SDK, REST API, hosted MCP server, SSH and file APIs; noVNC for browser and desktop templates.
- composes with: R0.45 per vCPU-hour and R0.15 per GB-hour put a two-vCPU, 4 GB sandbox near R1.50 an hour; a public HTTPS URL lets an agent hand results to a separate object-storage record.
- reliability: When the prepaid balance reaches zero, running sandboxes are paused; the vendor states it does not promise that the service will never be interrupted and does not promise data restoration from backups.
- notes: Prices are published in South African rand: R0.45 per vCPU-hour, R0.15 per GB-hour and R3.00 per GB-month give about R1.50 an hour at two vCPU and 4 GB, which is roughly the operator list's $0.091 an hour at the rand exchange rate; no first-party USD price is published. The R500 welcome credit follows a card payment, so the free usage is card-gated. There is also an R100 per 30 days always-on plan for one 512 MB VM.
- evidence note: Prices, the welcome credit, the free-account caps and the signup fields are quoted from the vendor's own pricing page, terms and sign-up page read on 2026-11-25.
- extras:
  - shape.vcpu: 2
  - shape.ram_gb: 4
  - shape.disk_gb: 5
  - shape.note: free accounts are capped at 2 vCPU, 2 GB of memory and 5 GB of disk per sandbox
  - billing_model: per-second prepaid wallet in rand, topped up by card through Paystack
  - free_tier_kind: card-gated-welcome-credit
  - term: credits never expire; welcome credit once per card
  - price_arithmetic: R0.45 per vCPU-hour x 2 plus R0.15 per GB-hour x 4 is R1.50 an hour at 2 vCPU and 4 GB
  - derived: R0.45 x 2 + R0.15 x 4 = R1.50 per hour; the operator list's $0.091 per hour is a USD conversion of that rand figure, for which no first-party rate was captured
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a public HTTPS URL per sandbox; no inbound port charge is stated
  - session_cap.restart_required: no
  - session_cap.note: a sandbox can be paused to keep state without paying for CPU; pause stops CPU and memory charges but disk continues
- evidence:
  - [2] 2026-11-25: usage is billed per second and creating sandboxes is free | capture: sha256:5e3aaca19b11698c244186d0325260b8a15288d00e715cba5106e56d401a27d4 | quote: Pay for what runs, billed per second. Creating sandboxes is free.
  - [2] 2026-11-25: compute is R0.45 per vCPU-hour, memory R0.15 per GB-hour and storage R3.00 per GB-month with the first 5 GB free | capture: sha256:5e3aaca19b11698c244186d0325260b8a15288d00e715cba5106e56d401a27d4 | quote: Compute R0.45 per vCPU-hour Memory R0.15 per GB-hour Storage R3.00 per GB-month · first 5 GB free
  - [2] 2026-11-25: each sandbox is a Firecracker microVM with a public HTTPS address, SSH and file APIs | capture: sha256:5e3aaca19b11698c244186d0325260b8a15288d00e715cba5106e56d401a27d4 | quote: Every sandbox gets an HTTPS address you can open or share, plus SSH access and file APIs.
  - [2] 2026-11-25: egress is limited to the public internet and sandboxes cannot reach each other or private networks | capture: sha256:5e3aaca19b11698c244186d0325260b8a15288d00e715cba5106e56d401a27d4 | quote: Sandboxes cannot reach each other, your private networks or cloud metadata. Egress is limited to the public internet.
  - [1] 2026-11-25: usage is charged per second in rand from a prepaid balance topped up by card through Paystack | capture: sha256:c8b2a6171103c09991fa82ca979c521d308fa83eedf7a4048402297ecaa15595 | quote: Usage is charged in South African rand, per second, from a prepaid balance that you top up by card through Paystack.
  - [1] 2026-11-25: the R500 credit follows the first card payment and a free account runs 2 sandboxes with 2 vCPU, 2 GB and 5 GB | capture: sha256:c8b2a6171103c09991fa82ca979c521d308fa83eedf7a4048402297ecaa15595 | quote: You get R500 of welcome credit after your first card payment, once per card. Free accounts can run 2 sandboxes at a time, each with up to 2 vCPU, 2 GB of memory and 5 GB of disk.
  - [3] 2026-11-25: the sign-up page asks for a first name and offers the welcome credit after a first card payment | capture: sha256:e25a4a16a5269567660ea619fd698a8df22cf07798bd7ea9e3758023fc25e6ad | quote: Get R500 of welcome credit after your first card payment.
  - [3] 2026-11-25: the sign-up form asks for a first name and a surname | capture: sha256:e25a4a16a5269567660ea619fd698a8df22cf07798bd7ea9e3758023fc25e6ad | quote: First name
  - [3] 2026-11-25: the sign-up form asks for an email and a password | capture: sha256:e25a4a16a5269567660ea619fd698a8df22cf07798bd7ea9e3758023fc25e6ad | quote: Password
  - [3] 2026-11-25: the sign-up page offers a third-party sign-in option | capture: sha256:e25a4a16a5269567660ea619fd698a8df22cf07798bd7ea9e3758023fc25e6ad | quote: Or sign up with
  - [4] 2026-11-25: the always-on plan is R100 a month for 1 shared vCPU, 512 MB and 5 GB, and credits never expire | capture: sha256:574b3a15872a9850e9a854f293a324139b580fff9066e7cf9a5cce3808ffa0fb | quote: Credits that never expire.
  - probe:ventaw.mmogomedia.com/pricing 2026-11-24: the pricing page answered a 302 redirect to a parked domain, so no price or free tier could be read | capture: sha256:c050b7d1e42ea030b9fd78443a3f1386bb5b405b11f5379a77fcba0dda432edd | quote: "status": 302
  - probe:ventaw.mmogomedia.com/v1/templates 2026-11-24: the API host answered a 302 redirect to a parked domain, so the offer could not be exercised or its limits read | capture: sha256:f839807c20e12fbdfc3192a21878f7ae5baf9e806a5a6906d0185d482b41eaf5 | quote: "status": 302
  - [5] 2026-11-24: the JavaScript SDK requires an API key and drives sandboxes over an API at ventaw.mmogomedia.com/v1 | capture: sha256:eb9220cf1d6a09141fb87a618d189ac405fb508aea79b409234c7b0ef2e306fd | quote: config.apiKey = "your-api-key";
  - [6] 2026-11-24: the LangChain toolkit uses VENTAW_API_KEY to create sandboxes and PostgreSQL or Valkey databases | capture: sha256:76ee78d07ee33bb1014b9ad772a04f6b6d60d870333b961605a8e98cb4a0a4af | quote: export VENTAW_API_KEY=...
  - [7] 2026-11-24:  | capture: sha256:13db4539040c908422bb4bf0c10d29cd8cabc606bd89ce3751bff4dd3d826d19 | quote: x-web-final-url: https://www.hugedomains.com/domain_profile.cfm?d=mmogomedia.com
- sources:
  - [1] https://www.ventaw.com/terms
  - [2] https://www.ventaw.com/
  - [3] https://www.ventaw.com/accounts/signup
  - [4] https://www.ventaw.com/pricing
  - [5] https://github.com/ventaw/nodejs
  - [6] https://github.com/ventaw/langchain-ventaw
  - [7] https://ventaw.mmogomedia.com/pricing
