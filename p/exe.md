# exe.dev

> exe.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exe/ | JSON https://fshy.ajam.dev/api/v1/entity/exe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## exe.dev

- `compute/exe-dev` | paid-only | evidence documented | binding volume-quota | category dev environment | tier Personal: USD 15/month pool of 2 vCPU / 4 GiB, up to 50 VMs
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:03:54.715Z (live) | stale on 2026-12-26
- url https://exe.dev/pricing
- price parsed USD 15/mo
- free tier: $15 / monthTry free for 7 days | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Persistent disks are included; 100 GiB of filesystem usage per 2 vCPUs, and additional disk at USD 0.08/GiB/month. | source: [1]
- egress: 200 GB of outbound bandwidth included on Personal; additional bandwidth is billed at the rates on the pricing page, USD 0.05/GiB on that page. | metered: yes | free allowance: 200 GB of outbound bandwidth | source: [1]
- identity: institution | detail: New accounts can link a paid ChatGPT subscription during signup for a free 7-day trial, with no card. Otherwise an active subscription is needed to create and manage VMs, paid through Stripe checkout. The site states sign-in works with a Google account.
- interface: ssh, cli
- limits:
  - volume-quota (binding): 200 GiB of network bandwidth a month on Personal; USD 0.05/GiB beyond [1]
- limits note: The pool model means the bill is a floor plus hourly overage, not a machine price.
- binding note: The binding constraint is the USD 15 minimum monthly spend, which no shape reduces; bandwidth is the metered wall behind it.
- interface detail: SSH into the VM as root, with apt and systemd; sign-in is through a Google account in the browser
- tooling: ssh, apt, systemd, and a web agent named Shelley for coding; a pool of vCPUs is reserved and shared by the VMs
- composes with: the pool model is the unusual part: 50 VMs share one 2 vCPU / 4 GiB reservation, so a fleet of idle sandboxes costs the same as one. It composes with a scheduler that starts many short-lived workers
- reliability: no reliability event observed; the trial is time-boxed at 7 days.
- notes: USD 15 a month is the floor and it buys 2 vCPU / 4 GiB spread over up to 50 VMs, so the per-VM cost is near zero but the bill is three times the budget. Standalone VMs are priced at USD 0.105/hour per 2 vCPU / 4 GiB for accounts above the minimum, which is USD 76.65 at 730 h. Egress arithmetic: USD 0.05/GiB x 1000 GB = USD 50 per TB beyond the 200 GiB allowance. Not established: the payment method and hold.
- evidence note: Plan price, pool size, VM count, disk and bandwidth allowances and the additional-disk and bandwidth rates are quoted from the pricing page read. Payment method and SSH details beyond the table are not on that page.
- extras:
  - facets.class: vendor-trial
  - crosscheck.boat_compare_2026-09-26: USD 0.280/h at 4 vCPU / 8 GB
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.note: a pool of 2 vCPU / 4 GiB shared across up to 50 VMs, 100 GiB of filesystem included
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 15.0
  - m24h_usd: 15.0
  - price_arithmetic: USD 15.00 a month minimum, billed monthly, so 24/7 = USD 15.00 and 10 h/day = USD 15.00. The metered alternative is USD 0.105/hour per 2 vCPU / 4 GiB = USD 76.65 at 730 h.
  - credit_usd: 0
  - credit_hours_at_shape: 0
  - free_tier_kind: trial
  - credit_expiry: not applicable
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: managed HTTPS and TLS with custom domains included; raw-port ingress terms not stated on the pricing page
  - session_cap.restart_required: no
  - session_cap.note: none stated; VMs persist with their disks
- evidence:
  - [1] 2026-10-22: '7-day trial with a paid ChatGPT subscription', quoted; Personal plan USD 15 a month for 2 vCPUs / 4 GiB, 50 VMs, 100 GiB of filesystem and 200 GiB of bandwidth
  - [2] 2026-10-22: 'You reserve a pool of vCPUs and memory, and your VMs share it', 'SSH in, you are root, you have apt and systemd', quoted
  - [3] 2026-10-22: a competitor's comparison table lists exe.dev at USD 0.280 per hour for a 4 vCPU / 8 GB / 50 GB machine, with list prices dated 2026-09-26; this is a reported rate about a third party and not a reading of the vendor's own page
  - [1] 2026-10-24: quoted: '$15/month', '7-day trial with a paid ChatGPT subscription', 'Minimum Monthly Spend | $15', 'Cost | $0.105 per 2 vCPUs / 4 GiB per hour', 'Additional bandwidth | $0.05 / GiB'.
  - [1] 2026-11-25: the pricing page states the Personal plan at USD 15 a month and a 7-day free trial | capture: sha256:1f614d9f3769e837637c1c444c2c5089d6f33778041f8ba054c3efff82db060b | quote: $15 / monthTry free for 7 days
  - [4] 2026-11-24: the trial needs a paid ChatGPT subscription and no card; the paid path uses Stripe checkout | capture: sha256:be871216380e2295fb6bea2b193fb0b0b91333e5bcf0a596e36965e0252202ee | quote: An active subscription is needed to create and manage VMs. New accounts can link a paid ChatGPT subscription during signup for a free 7-day trial, with no card. The trial starts when you create your first VM. Otherwise, subscribe with Stripe checkout.
  - [5] 2026-11-24: the allowance is 200 GB of outbound bandwidth shared by all VMs | capture: sha256:c67a515ccabb66a2410486355a6f1a580868dd485b316ca0307de6ede836b751 | quote: Every capacity includes 200 GB of outbound bandwidth and up to 50 VMs.
  - [4] 2026-11-24: the no-card trial is gated on an existing paid subscription rather than a card at signup | capture: sha256:be871216380e2295fb6bea2b193fb0b0b91333e5bcf0a596e36965e0252202ee | quote: New accounts can link a paid ChatGPT subscription during signup for a free 7-day trial, with no card.
  - [1] 2026-11-24: the Personal plan still lists 200 GiB of network bandwidth | capture: sha256:1f614d9f3769e837637c1c444c2c5089d6f33778041f8ba054c3efff82db060b | quote: * 200 GiB of network bandwidth
  - [6] 2026-11-24: the VM is reachable by SSH with root | capture: sha256:a2d725da65df3614954b249b4113680bd8e37a8927bf3b71ebdb20c571288dc0 | quote: SSH in, and you’ve got root.
- sources:
  - [1] https://exe.dev/pricing
  - [2] https://exe.dev/
  - [3] https://boat.dev/compare
  - [4] https://exe.dev/docs/billing/overview
  - [5] https://exe.dev/docs/billing/personal
  - [6] https://exe.dev
