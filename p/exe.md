# exe.dev

> exe.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exe/ | JSON https://fshy.ajam.dev/api/v1/entity/exe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## exe.dev

- `compute/exe-dev` | paid-only | evidence documented | binding volume-quota | category dev environment | tier Personal: USD 15/month pool of 2 vCPU / 4 GiB, up to 50 VMs
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T02:11:00.000Z (live) | stale on 2026-11-24
- url https://exe.dev/pricing
- price parsed USD 15/mo
- free tier: No free tier; a 7-day trial with a paid ChatGPT subscription. Minimum monthly spend USD 15. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Persistent disks are included; 100 GiB of filesystem usage per 2 vCPUs, and additional disk at USD 0.08/GiB/month. | source: [1]
- egress: 200 GiB of network bandwidth included on Personal; additional bandwidth USD 0.05/GiB. | metered: yes | free allowance: 200 GiB | source: [1]
- identity: card | detail: A paid plan implies a card; the pricing page states no card, hold or debit terms. The 7-day trial is gated on a paid ChatGPT subscription. Unverified.
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
  - [1] 2026-10-24: quoted: 'Personal ... $15 / month ... Pool size 2 vCPUs / 4 GiB memory ... 50 VMs ... 100 GiB of filesystem usage included ... 200 GiB of network bandwidth'
  - [1] 2026-10-24: quoted: 'Minimum Monthly Spend | $15'; 'Additional disk | $0.08 / GiB / month'; 'Additional bandwidth | $0.05 / GiB'; 'KVM-isolated VMs | Included'; 'Persistent disks | Included'
- sources:
  - [1] https://exe.dev/pricing
  - [2] https://exe.dev/
  - [3] https://boat.dev/compare
