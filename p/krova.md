# Krova Cloud

> krova.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/krova/ | JSON https://fshy.ajam.dev/api/v1/entity/krova.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Krova Cloud

- `compute/krova-cube` | qualifies-with-caveat | evidence documented | binding none | category microVM (Firecracker) with root SSH | tier a-la-carte 1 vCPU / 2 GiB RAM / 10 GiB disk (the beefiest shape under USD 5 at 730 h)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T03:05:00.000Z (live) | stale on 2026-11-24
- url https://krova.cloud/pricing/cube
- price parsed USD 4.75/mo
- free tier: Claim $5 in free credit - one-time, per account, and nothing is charged for it. Signing up is free and takes no payment details. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit, not hours: USD 5 of prepaid balance
- per-object cap: not applicable
- retention: Power off a Cube and its disk is kept exactly as you left it; only the disk keeps billing, at USD 0.00005/GB/hour on the full provisioned size. | source: [1]
- egress: Unmetered. Krova does not bill per gigabyte and sets no monthly transfer allowance; the network is shared and sustained heavy traffic can be rate-limited. Outbound TCP 25 is blocked. | metered: no | free allowance: unmetered | source: [2]
- identity: email | detail: Email link or 6-digit code, or Google; 'No credit card to sign up'. The USD 5 credit is granted at account activation with nothing charged, and the Welcome tier unlocks with it, so a card is needed only to top up (one-time Stripe Checkout) or to enable auto-recharge. No hold is stated. Debit acceptance is not stated.
- interface: ssh, rest, cli
- limits:
  - per-ip-shaping: no UDP ingress and no public IPv4: services are exposed as on-demand TCP port mappings with an optional allowlist, or through Krova's HTTPS proxy [2]
  - volume-quota: outbound TCP port 25 blocked on every Cube; other ports open [2]
- limits note: Two hard limits that the seven-kind vocabulary cannot name. (1) There is no public IPv4 and no UDP ingress: 'Outbound: everything. Inbound: your call' is implemented as on-demand TCP port mappings with IP allowlists plus an HTTPS proxy for web traffic, so a WireGuard or QUIC listener cannot be reached from outside. (2) Concurrency is tiered: 3 Cubes running at once on Welcome, 10 after USD 15 of lifetime top-ups, 25 after USD 50, uncapped after USD 300. Cube size is the same on every tier: up to 16 vCPU, 32 GB RAM, 100 GB disk.
- binding note: What fails first is not one of the seven kinds: there is no UDP ingress and no public IPv4, so a WireGuard or QUIC listener cannot be reached. Recorded in limits[] as per-ip-shaping with the protocol limit spelled out rather than mislabelled as a quota.
- interface detail: Root SSH on a per-Cube hostname and port, a REST API with API keys, and a dashboard. 'You log in as ubuntu ... Run sudo su for a root shell.'
- tooling: any SSH client; rsync/scp over the SSH mapping; the REST API for create/start/stop; no vendor rclone backend needed because it is a plain Linux box
- composes with: A USD 2.92 a month always-on Linux box with root, unmetered egress and no card at signup: the cheapest credible always-on target among evaluated offerings, usable as a monitor, a small web app behind Krova's HTTPS proxy, or a Docker host, but not as a WireGuard endpoint because only TCP can be published.
- reliability: domain registered 2026-03-14; prepaid credit is not refundable in cash; the disk is deleted 7 days after the balance reaches zero
- notes: The nearest published preset, Micro at 1 / 2 / 20, is USD 5.11 and therefore over the line. 15 GiB of disk instead of 10 would be USD 4.93. Its credit is non-refundable in cash and its disk is deleted seven days after the balance hits zero, so it is a prepaid bet rather than a subscription. The domain is seven months old. Against that: a status page on UptimeRobot reports 99.996%, which is better evidence than most hosts in this price band publish.
- evidence note: Rate card, presets, the 730-hour convention, the stopped-disk billing and the signup terms are quoted from the pricing page read; root/sudo, the TCP-only port mappings and port 25 from the cubes documentation read.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 10
  - billing_model: per-minute
  - term: prepaid credit, no commitment
  - m10h_usd: 1.95
  - m24h_usd: 4.75
  - price_arithmetic: 730 h x (1 x 0.0010 + 2 x 0.0025 + 10 x 0.00005) = 730 x 0.0065 = USD 4.745. 10 h/day = 300 x 0.0065 = USD 1.95. The published 1/1/10 preset is 730 x 0.004 = USD 2.92; the published 1/2/20 preset is 730 x 0.007 = USD 5.11. Powered off, only disk bills: 10 GB x 0.00005 x 730 = USD 0.365 a month.
  - free_tier_kind: credit
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: TCP only, via on-demand port mappings with an optional IP allowlist; no public IPv4 and no UDP; HTTPS through Krova's proxy for custom domains
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: no lifetime cap; it is an always-on microVM
  - aggregator_gross_usd_month: 1.065
  - aggregator_note: sandboxprices.com models 0.25 vCPU / 0.47 GiB / 4.66 GiB at 200 active hours and rounds up to this 1 vCPU / 1 GB / 10 GB preset; its USD 1.065 is not the 24/7 price of the machine, which is USD 2.92.
- evidence:
  - [1] 2026-10-24: quoted: 'Sandbox | 1 | 1 GB | 10 GB | - | $0.004 | $2.92' and 'Per-month estimate = hourly rate × 730 hours, running 24/7'
  - [1] 2026-10-24: quoted: 'vCPU $0.0010/hr per vCPU', 'RAM $0.0025/hr per GB', 'Disk $0.00005/hr per GB', 'Billed by the minute - run 5 minutes, pay 5 minutes'
  - [1] 2026-10-24: identity: 'Signing up is free, and creating an account takes no payment details. Claim $5 in free credit - one-time, per account'
  - [3] 2026-10-24: egress: 'Bandwidth is unmetered: Krova Cloud does not bill per gigabyte and does not set a monthly transfer allowance', and the inbound model: 'A Cube is not reachable from outside at all until you decide it should be'
  - [4] 2026-10-24: access: 'You log in as ubuntu ... Run sudo su for a root shell', images Ubuntu 24.04 or Debian 13, REST API keys for automation
  - [1] 2026-10-24: quoted: 'vCPU $0.0010/hr per vCPU', 'RAM $0.0025/hr per GB', 'Disk $0.00005/hr per GB'; and 'Per-month estimate = hourly rate × 730 hours, running 24/7'
  - [1] 2026-10-24: presets quoted: 'Sandbox | 1 | 1 GB | 10 GB | - | $0.004 | $2.92' and 'Micro | 1 | 2 GB | 20 GB | - | $0.007 | $5.11'
  - [5] 2026-10-24: quoted: 'A Cube is a Firecracker microVM, not a full virtual machine that spends minutes booting'; 'You get full root access, systemd, your own kernel modules, Docker, any package manager'; 'Power a Cube off and compute charges stop — only its disk keeps billing at the disk rate'
  - [2] 2026-10-24: quoted: 'It has passwordless sudo, so `sudo su` gives you a root shell. Root SSH login is disabled.' and 'To expose other services, add TCP port mappings from the Cube's networking tab'
  - [2] 2026-10-24: quoted: 'Outbound TCP port 25 is blocked on every Cube ... Every other outbound port is open'
  - [4] 2026-10-24: identity, resolved: 'Top up from Billing with a card (one-time, via Stripe Checkout). Activating your account credits you $5 to start (one-time, per account) and unlocks the Welcome tier automatically — nothing is charged for it.'
  - [6] 2026-10-24: 
- sources:
  - [1] https://krova.cloud/pricing/cube
  - [2] https://krova.cloud/docs/cubes
  - [3] https://krova.cloud/
  - [4] https://krova.cloud/docs/getting-started
  - [5] https://krova.cloud/cube
  - [6] https://krova.cloud/terms
