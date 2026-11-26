# Mandala Computer

> mandala.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mandala/ | JSON https://fshy.ajam.dev/api/v1/entity/mandala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mandala Computer

- `compute/mandala-computer` | paid-only | evidence documented | binding volume-quota | category container and vm sandbox | tier Pay as you go
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T11:55:06.371Z (live) | stale on 2026-12-26
- url https://mandala.computer/pricing
- free tier: No free tier: a paid plan or prepaid credits are required to launch a computer. Without a subscription, credits are bought in USD 10, 25 or 50 packs, expiring 12 months after purchase, and a standard computer runs at USD 0.12/hour billed by the second; starting anything needs at least USD 0.25 of credit. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The operator list's $0.12/h is the pay-as-you-go Standard computer rate for 2 vCPU / 4 GB. The Solo plan is $29/month for a pool of 4 vCPU, 8 GB RAM and 80 GB across up to 4 computers.
- per-object cap: not applicable: the metered unit is a running virtual machine, not a stored object; files up to 2 GiB can be uploaded into a computer, and a pay-as-you-go computer allows up to 4 vCPU, 8 GB RAM and 80 GB each | source: [1]
- retention: Scheduled snapshots are opt-in and bounded by the plan's window: 7 days on Solo, 7 daily plus 4 weekly on Studio, adding 12 monthly on Swarm. A computer out of credit for 30 days may be deleted, with an email warning at least seven days before. | days: 30 | source: [1]
- egress: Each computer can serve a port on its own HTTPS address under mandala.dev, open to anyone with the link or private to signed-in account users; the pricing page states no separate egress volume allowance or per-GB traffic price. | metered: no | source: [1]
- identity: email | detail: The sign-up page offers an email field, a password of at least 8 characters, and Continue with GitHub or Continue with Google. Credits and plans require payment; the terms and payment page are not gated by a phone number or ID document on the pages read.
- interface: rest, cli, ssh, browser, chat
- limits:
  - volume-quota (binding): No free tier: prepaid credits in $10, $25 or $50 packs, expiring 12 months after purchase; $0.12/hour for a Standard 2 vCPU / 4 GB computer, $0.03 per vCPU-hour plus $0.015 per GB-hour and $0.10 per GB-month of disk [1]
  - request-rate: Pay as you go runs up to 8 computers sharing 8 vCPU / 16 GB RAM and 160 GB storage, up to 4 vCPU / 8 GB RAM / 80 GB per computer, 1 seat [1]
- limits note: Monthly plans: Solo $29 (4 computers, 4 vCPU / 8 GB / 80 GB pool), Studio $99 (16 computers, 16 vCPU / 32 GB / 320 GB), Swarm $399 (32 computers, 64 vCPU / 128 GB / 640 GB). A built-in computer-agent run stops after 60 minutes.
- binding note: Prepaid credits are required before any computer starts and are what run out first; at zero credit running computers are suspended or stopped with disks kept, and nothing new starts.
- interface detail: A REST API with Python and TypeScript SDKs, a mandala CLI, an MCP server for coding agents, a graphical Linux desktop with screenshot/click/type controls and an embeddable live view.
- endpoint: https://app.mandala.computer/docs
- tooling: The user installs the Python or TypeScript SDK or the mandala CLI, or connects an agent over MCP; each computer is a hardware-isolated Linux VM.
- composes with: Persistent desktop VMs let an agent use a browser and desktop applications across sessions, with snapshots for recovery, alongside inference records that supply the model calls.
- reliability: Out-of-credit computers are suspended with sessions saved or stopped with disks kept; a computer out of credit for 30 days may be deleted with an email warning at least 7 days before. Snapshots count against snapshot storage, so a long schedule can leave less room for manual snapshots.
- notes: Cloud Linux desktop VMs for agents, priced per plan or by the second; no free tier or sign-up credit is published. The built-in agent is a separate metered add-on billed through Mandala AI credits.
- evidence note: Prices, credit expiry, per-computer caps, snapshot windows and sign-up fields are quoted from first-party pages read on 2026-11-25. Egress volumes are not published.
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.disk_gib: 80
  - shape.note: Solo pool of 4 vCPU, 8 GB RAM and 80 GB storage split across up to 4 computers; 40 GB disk per computer
  - billing_model: monthly plan or prepaid credits by the second
  - free_tier_kind: none
  - term: monthly, cancel at period end
  - price_arithmetic: USD 29 a month for Solo, or USD 0.03 per vCPU-hour plus USD 0.015 per GB-hour of RAM and USD 0.10 per GB-month of disk on pay as you go
  - status: live hosted paid service
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: up to 2 public URLs per computer on Solo under mandala.dev
  - network_out.static_ip: no
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: no
  - session_cap.note: a built-in agent run stops after 60 minutes; a computer can be stopped and resumed with its disk kept
- evidence:
  - [1] 2026-11-25: the pay-as-you-go Standard computer is $0.12 per hour, matching the operator list | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: $0.12 / hour for a Standard computer
  - [1] 2026-11-25: disk costs $0.10 per GB-month while a computer exists, snapshots included | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: $0.10 per GB-month of disk while a computer exists; snapshots included
  - [2] 2026-11-25: the starting price is $29/month for up to 4 computers or $0.12/hour as you go | capture: sha256:b7f2cdadb2d26ff0be61edc7c14e07d17f5487ce960ccbb6aa5ab49e39d41889 | quote: | From | $29 / month · up to 4 computers, or $0.12 an hour as you go |
  - [3] 2026-11-25: sign-up asks for an email and password and offers GitHub or Google sign-in | capture: sha256:28fb2df689f6951dddbe891851994b68feeac16a2aaa05315b3c1d1570b11652 | quote: <input type="email" placeholder="Email" autofocus="" value=""/></div><div class="field"><input type="password" placeholder="Password (min 8 characters)" value=""/></div>
  - [1] 2026-11-24: Solo costs $29 a month | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: $29 / month
  - [1] 2026-11-24: pay as you go is $0.12 an hour for a Standard computer | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: $0.12 / hour for a Standard computer
  - [1] 2026-11-24: the Solo pool is 4 vCPU, 8 GB RAM and 80 GB storage | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: 4 vCPU · 8 GB RAM · 80 GB storage pool
  - [1] 2026-11-24: the per-computer storage ceiling on Solo is 40 GB | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: Storage per computer | 40 GB
  - [1] 2026-11-24: files uploaded into a computer are capped at 2 GiB | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: Files of up to 2 GiB go into a computer as a resumable upload
  - [1] 2026-11-24: a paid plan or prepaid credits are required to launch computers | capture: sha256:9ac437c50bb81e9bdf0ced7d8ef6ea090e5a853e7d380ca1c4a7b290ab866efc | quote: A paid plan or prepaid credits are required to launch computers: without a plan, pay as you go.
  - [3] 2026-11-24: sign-up offers GitHub and Google as registration methods | capture: sha256:2f766f68baf38fe1051045840339ebbc6693a39a9e50cc441b73993d3239a661 | quote: [Continue with GitHub](https://app.mandala.computer/api/auth/github/start?intent=login) [Continue with Google](https://app.mandala.computer/api/auth/google/start?intent=login)
  - [4] 2026-11-24: registration requires the user to be 18 or older and to provide a working email address | capture: sha256:d5a7c317d124009c505c1dc4e40f1c0142541f986289fb868bd4ca7edaac465f
  - [4] 2026-11-24: outbound traffic shares one address with other customers | capture: sha256:d5a7c317d124009c505c1dc4e40f1c0142541f986289fb868bd4ca7edaac465f | quote: Your computers reach the internet through an address shared with other customers.
  - [5] 2026-11-24: the computer is reachable over a REST API, SDKs and an MCP server | capture: sha256:b7f2cdadb2d26ff0be61edc7c14e07d17f5487ce960ccbb6aa5ab49e39d41889 | quote: Access | REST API, Python and TypeScript SDKs, MCP server
- sources:
  - [1] https://mandala.computer/pricing
  - [2] https://mandala.computer/
  - [3] https://app.mandala.computer/signup
  - [4] https://mandala.computer/terms
  - [5] https://mandala.computer
