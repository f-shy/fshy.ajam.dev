# vds.guru

> vds.guru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vds/ | JSON https://fshy.ajam.dev/api/v1/entity/vds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vds.guru

- `compute/vds-guru-trial` | trial-only | evidence documented | binding retention-clamped | category VPS | tier Free 24-hour trial on any VPS plan
- needs card no, phone yes, ID no, institution no | verified 2026-10-24T06:33:00.000Z (live) | stale on 2026-11-24
- url https://vds.guru/trial/
- free tier: 'The trial gets the same resources as the paid plan: KVM virtualization, NVMe disks, full root on VPS and a 1 Gbps port. No cut-down demo.' Trial terms table: 'Length | 24 hours', 'Cost | Free, no credit card needed', 'What you need to do | Sign up and verify your phone number via Telegram or WhatsApp — 30 seconds at most'. | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: one trial per account; the vendor 'reserves the right to refuse a trial period without providing a reason', citing suspicious account activity, resource shortage or staff workload
- retention: 'If you don't renew, the server is blocked automatically after 24 hours.' Renewing keeps the data: 'If the server suits you, renew the plan in the client area and it keeps running with the same data and settings'.
- egress: '10 TB of traffic per month on every VPS plan, from KVM-1 to KVM-MEGA. Once you exceed the limit, the port speed is limited to 100 Mbps; the server keeps running.' | metered: yes | free allowance: 10 TB per month | source: [2]
- identity: any-phone | detail: no card, no document, no email-only path: 'Sign up and verify your phone number via Telegram or WhatsApp — 30 seconds at most'. The page states 'No. Sign up in the client area, verify your phone number via Telegram or WhatsApp (30 seconds), then open a ticket asking for a trial.' It does not say which countries' numbers are accepted, so the kind is any-phone rather than country-phone.
- interface: ssh
- limits:
  - retention-clamped (binding): 24 hours, then the server is blocked automatically [1]
  - volume-quota: 10 TB a month of traffic on every plan, then the port is shaped to 100 Mbps [2]
  - write-gated: a support ticket must be opened after phone verification, and the vendor may refuse [1]
  - per-ip-shaping: SMTP ports 25, 465 and 587 blocked by default on the trial [1]
- binding note: Twenty-four hours is the whole offer; the machine is blocked automatically at the end and there is no free continuation.
- interface detail: KVM guest with full root over SSH, a 1 Gbps port, one IPv4; the trial carries the same resources as the plan chosen. SMTP ports 25, 465 and 587 are blocked by default and unblocked only on request.
- tooling: any SSH client; a billing panel for the ticket and the trial request
- composes with: A real KVM guest with root and 1 Gbps for one day, no card, obtained by opening a ticket: enough to benchmark a host or run a migration rehearsal, not enough to be a node.
- reliability: no reliability event observed. The vendor states the trial can be refused without a reason, which is a capacity and staffing statement rather than an observed outage.
- notes: A genuine no-card VPS trial: full KVM, root, 1 Gbps, one day, no payment instrument at all. It is ranked below the always-free options because 24 hours is a benchmark window, not a machine. Two things are unverified. First, the trial's shape depends on which plan the ticket names, and the ticket is a human gate that can be refused. Second, whether the phone check accepts a number outside the vendor's home region is not stated. The vendor's own FAQ answers 'Can I get a free VPS forever?' with 'No, the free option is a 24-hour trial', so there is no free tier to be had here beyond the day.
- evidence note: The 24-hour term, the no-card statement, the phone verification, the ticket route, the SMTP block and the 10 TB traffic term are all quoted from vds.guru's own trial and VPS pages read. The KVM-1 shape is quoted from the VPS page; the trial page does not repeat the shape, so the trial's exact allocation depends on which plan the ticket names.
- extras:
  - shape.ram_gib: 1
  - shape.disk_gib: 15
  - shape.note: the KVM-1 paid plan, which the trial page says it mirrors; the VPS page lists RAM and disk but no vCPU count for KVM-1
  - billing_model: free
  - term: 24 hours, then blocked unless renewed at USD 10 a month
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: USD 0.00 for 24 hours; renewal is USD 10.00 a month for KVM-1, which is the first paid month, not a free continuation
  - free_tier_kind: trial
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: 1 Gbps port, one IPv4, all ports except SMTP 25/465/587
  - network_out.static_ip: yes
  - network_out.per_session_bytes: 10 TB per month, then shaped to 100 Mbps
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: hard 24-hour block, no idle reap published
  - signup_url: https://vds.guru/trial/
  - payment_methods: none for the trial; the page states 'there's no card on your account'
- evidence:
  - [1] 2026-10-24: quoted: 'The trial gets the same resources as the paid plan: KVM virtualization, NVMe disks, full root on VPS and a 1 Gbps port. No cut-down demo.'
  - [1] 2026-10-24: trial terms table, quoted: '| Length | 24 hours |', '| Cost | Free, no credit card needed |', '| What you need to do | Sign up and verify your phone number via Telegram or WhatsApp - 30 seconds at most |'
  - [1] 2026-10-24: quoted: 'If you don't renew, the server is blocked automatically after 24 hours. Nothing is charged: there's no card on your account, so the trial commits you to nothing.'
  - [1] 2026-10-24: quoted: 'SMTP Ports Blocked ... email sending ports (25, 465, 587) are blocked by default. Unblocking is possible only upon request with justification.'
  - [1] 2026-10-24: quoted: 'the company reserves the right to refuse a trial period without providing a reason. This typically occurs due to suspicious account activity, a shortage of available resources, or high workload on our technical staff.'
  - [2] 2026-10-24: quoted: 'KVM-1 $ 10 /mo ✓ 1 GB RAM ✓ 15 GB NVMe SSD ✓ 1 Gbps port' and '10 TB of traffic per month on every VPS plan, from KVM-1 to KVM-MEGA. Once you exceed the limit, the port speed is limited to 100 Mbps; the server keeps running.'
  - [2] 2026-10-24: quoted: 'Every plan comes with DDoS protection up to 20 Gbit/s, a 1 Gbps port with 10 TB of traffic, one IPv4 address and 24/7 support.'
  - [1] 2026-10-24: trial terms table, quoted: '| Length | 24 hours |', '| Cost | Free, no credit card needed |', '| What you need to do | Sign up and verify your phone number via Telegram or WhatsApp — 30 seconds at most |'
- sources:
  - [1] https://vds.guru/trial/
  - [2] https://vds.guru/vds/
