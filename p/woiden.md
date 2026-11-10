# Woiden.id

> woiden.id | Egress and tunnels, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/woiden/ | JSON https://fshy.ajam.dev/api/v1/entity/woiden.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Woiden

- `egress/woiden` | qualifies-with-caveat | evidence documented | binding retention-clamped | category free nat vps | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://woiden.id/
- price USD 0
- free tier: Unmetered Bandwidth: all data centers provide unlimited bandwidth. Shared IPv4: a NAT VPS shares one IPv4 and assigns a different port for each user. [vendor page] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unmetered bandwidth, stated on the vendor page.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: any-phone | detail: Registration plus a Telegram account for the renewal code; the renewal flow sends a code through Telegram and adds an arithmetic captcha. | country: None
- interface: ssh, cli
- limits:
  - request-rate: 8 to 10 shared IPv4 ports [2]
  - retention-clamped (binding): 7-day life, renewed by hand [3]
- binding note: Unmetered bandwidth means no byte quota exists, so nothing in the volume sense fails at 1 TiB/month. What stops a month-long run is the 7-day instance life: miss one renewal and the machine and its address are gone. The vocabulary has no kind for instance lifetime, so retention-clamped carries it, with the caveat that the vendor discloses the 7 days rather than clamping silently.
- interface detail: SSH with root and a web panel with console, reinstall and port request.
- tooling: ssh, wg-quick; the panel issues the public port range
- composes with: Full root means WG terminates here and a conf is generated locally, so this is an ingress endpoint plus relay in one free box.
- reliability: Third-party write-ups record the provider's NAT VPS being unusable during outages; a missed 7-day renewal deletes the instance and its address.
- notes: The best volume story in the sweep: unlimited bandwidth, full root, no card. Against it: 7-day manual renewal through a Telegram code, a 8-10 port shared IPv4, and a history of the provider's servers going down. The no-hardware premise is satisfied because this is a rented-free VM, not owned iron.
- evidence note: Unmetered bandwidth and the shared-IPv4 model are on the vendor page today; the port count and 7-day renewal come from third-party write-ups.
- extras:
  - wg_path: native-conf
  - wg_detail: A full root VPS with a dedicated IPv6 and a DNAT port range on a shared IPv4; WireGuard can be installed and a peer conf generated on the box. The vendor panel forwards 'data from public ip address to your vps' by iptables without naming a protocol.
  - ingress: udp
  - volume_stated: Unmetered bandwidth, stated on the vendor page.
  - bytes_transit: yes
  - transit_note: The provider's European hosts carry the traffic.
- evidence:
  - [1] 2026-10-23: unmetered bandwidth at all data centers, shared IPv4 with a port per user
  - [2] 2026-10-23: public port request uses iptables to pass data from the public IP to the VPS
  - [4] 2026-10-23: a shared-IPv4 port range is issued per VPS
- sources:
  - [1] https://woiden.id/
  - [2] https://woiden.id/vps-nat
  - [3] https://woiden.id/vps-renew/
  - [4] https://wiki.woiden.id/2022/04/12/how-to-connect-nat-vps-via-android/

## Woiden.id

- `compute/woiden-id` | qualifies-with-caveat | evidence documented | binding retention-clamped | category cloud VM | tier free NAT VPS
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T05:24:47.109Z (live) | stale on 2026-12-05
- url https://woiden.id/
- free tier: A free NAT VPS with a shared IPv4 and a dedicated IPv6: 'NAT VPS is almost similar to other VPS but uses the NAT method so that a single IPv4 can be shared to many VPS and then assigns a different port for each user.' The site states 'Full SSH access', 'Unmetered Bandwidth — All data centers provide Unlimited bandwidth' and 'Shared IPv4 — VPS comes with Shared IPv4 and Dedicated IPv6'. No CPU, RAM or disk figure is published on any page read. | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: a third-party review from 2022 reports 450 MB RAM, 3 GB disk and 8 forwarded ports; that is reported, not documented, and is four years old
- per-object cap: not applicable: the unit is a virtual machine, not an object
- retention: 'You can renew your VPS at least 3 days before it expires'. The site describes itself as 'Renewable — Extend your server duration to keep your free server online'. The interval a renewal adds is not stated on any page read; a third-party review of 2022 says 'Must renew every 7 days'. | source: [2] | note: the renewal window is documented as opening 3 days before expiry; the period added is reported only
- egress: 'Unmetered Bandwidth — All data centers provide Unlimited bandwidth' | metered: no | free allowance: unlimited | source: [1]
- identity: any-phone | detail: Registration requires a Telegram ID obtained via bot interaction. No email, card, authorization hold, or identity document is required on the registration form.
- interface: ssh
- limits:
  - retention-clamped (binding): the VPS expires and must be renewed, with the renewal window opening 3 days before expiry; the period added is not published [2]
  - write-gated: registration requires a Telegram numeric ID, obtained by messaging @HaxTG_bot with /getid [3]
- limits note: The instance is reclaimed unless renewed daily, so the server is only always-on while a human logs in every day; a missed weekend loses the machine and its data.
- binding note: the machine expires on a short clock that only a human can reset, so it cannot be an always-on node
- interface detail: The register page documents SSH access to the VPS, plus a web panel (VPS info, reinstall, reset password, power control) and a web-based terminal at ssh.hax.co.id.
- tooling: No CLI, SDK or API library is named: the woiden.id register page was read and lists the web panel and web terminal beside plain SSH.
- composes with: Same composition as Hax: an IPv6-only root box needs an IPv4 front, and the daily renewal is the part that cannot be automated without an external scheduler and stored credentials.
- reliability: no reliability event observed; the vendor routes support through a Telegram group and channel
- notes: Woiden.id provides free NAT IPv4 and IPv6 VPS hosting accounts managed through Telegram bot authentication, requiring active renewal validation.
- evidence note: the interface list, the renewal rule, the unlimited-bandwidth statement and the Telegram-ID form are quoted from first-party pages read. The shape is not published by the vendor at all, so it is left null rather than filled from a 2022 review
- extras:
  - facets.class: perpetual-renewal-gated
  - facets.free_tier_kind: perpetual-renewable
  - facets.shape.ram_gib: 1
  - billing_model: free
  - term: renewable, period unstated
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no price: the service is free and the register form collects no payment detail
  - free_tier_kind: renewable-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: shared IPv4 with per-user port mapping; the count is not published
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: expires; renewal opens 3 days before expiry
  - shape_reported: 450 MB RAM, 3 GB disk, 8 forwarded ports and 5 reinstalls a month, from a LowEndSpirit review of April 2022 — reported, four years old, not used in the record's fields
- evidence:
  - [1] 2026-10-22: the vendor page advertises a free Nat VPS, a web panel with reinstall and usage monitoring, and a renew action to keep the server online, quoted
  - [4] 2026-10-22: comparison table gives Woiden.id at 1000 MB RAM, 8 GB disk, OpenVZ, IPv6 only, with a daily renewal requirement, and describes the instant-reclaim mechanism on a missed day
  - [1] 2026-10-24: quoted: 'NAT VPS is almost similar to other VPS but uses the NAT (Network Address Translation) method so that a single IPv4 can be shared to many VPS and then assigns a different port for each user.', 'Full SSH access', 'Unmetered Bandwidth', 'Shared IPv4'
  - [2] 2026-10-24: quoted: 'You can renew your VPS at least 3 days before it expires'
  - [3] 2026-10-24: the served markup: one input, name='telegram_id', placeholder='12345678', required; label 'Telegram ID:'; and the instruction 'Send private message to @HaxTG_bot, type this command: /getid'
  - [1] 2026-10-24: the sibling service is named on the register page: 'Create a free IPv6 only VPS at HAX.co.id'
  - [5] 2026-10-24: reported, third party, April 2022: '-450MB RAM -3GB Disk -Unlimited Data Transfer -Dedicated IPv6 -Shared IPv4+8 Ports -5 OS Reinstalls/Month' and '-Must renew every 7 days'
  - [3] 2026-11-03: SSH is an access interface | capture: sha256:afbfd73408aafc42c37aaec69f3271b7d6966c6f8a1ccdeea88187815e89d674 | quote: Full SSH access to manage and install your application
  - [3] 2026-11-03: egress is unmetered, no overage price | capture: sha256:afbfd73408aafc42c37aaec69f3271b7d6966c6f8a1ccdeea88187815e89d674 | quote: All data centers provide Unlimited bandwidth
  - [3] 2026-11-04: SSH access is the documented interface | capture: sha256:afbfd73408aafc42c37aaec69f3271b7d6966c6f8a1ccdeea88187815e89d674 | quote: Full SSH access to manage and install your application
  - [3] 2026-11-04: a web panel and a web-based terminal are listed beside SSH | capture: sha256:afbfd73408aafc42c37aaec69f3271b7d6966c6f8a1ccdeea88187815e89d674 | quote: [Web Base Terminal](https://ssh.hax.co.id/)
- sources:
  - [1] https://woiden.id/
  - [2] https://woiden.id/vps-renew/
  - [3] https://woiden.id/register/
  - [4] https://misc.zz.ac/2026/01/26/hax-woiden-%e5%85%8d%e8%b4%b9vps/
  - [5] https://lowendspirit.com/discussion/4045/free-nat-vps-dedicated-ipv6-shared-ipv4
