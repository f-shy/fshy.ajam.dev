# shellbox

> shellbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shellbox/ | JSON https://fshy.ajam.dev/api/v1/entity/shellbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## shellbox

- `compute/shellbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier x1 slot: 2 vCPU / 4 GB RAM / 50 GB SSD, keepalive mode
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:09.967Z (live) | stale on 2026-12-05
- url https://shellbox.dev/
- price parsed USD 14.6/mo
- free tier: No free tier; a prepaid balance with a USD 10 minimum top-up. First SSH creates the account from the key fingerprint. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: Parked (stopped) boxes keep their disk and a memory snapshot at USD 0.50/month per x1 slot; boxes auto-stop when the balance drops below USD 5 and are deleted at USD 0. Unused funds are refundable within 3 months. | source: [1]
- egress: Not metered on the page read: no traffic allowance and no per-GB price is stated; the box gets a public IPv6 address and a managed HTTPS endpoint. | metered: no | free allowance: not stated | source: [1]
- identity: anonymous | detail: No card, no email, no signup form: 'your SSH key fingerprint is your account'. Payment is a prepaid Paddle balance with a USD 10 minimum top-up, refundable within 3 months; no card is stored by Shellbox. No hold.
- interface: ssh, scp, sftp
- limits:
  - volume-quota (binding): prepaid balance only; boxes auto-stop below USD 5 and are deleted at USD 0 [1]
- binding note: The price is the wall, not a quota: USD 0.02/hour per x1 slot is USD 14.60 a month, and there is no smaller slot than x1.
- interface detail: SSH to shellbox.dev for control commands (create, list, duplicate, keepalive, cron, funds) and SSH to a box; scp, sftp and mosh work
- tooling: not stated
- composes with: not established
- reliability: Stopped boxes resume from a memory snapshot in about 3 seconds; auto-stop and deletion are triggered by the prepaid balance, not by time.
- notes: Arithmetic at 24/7: USD 0.02/hour x 730 = USD 14.60 for 2 vCPU, 4 GB and 50 GB SSD. 10 h/day at 22 days = 220 h = USD 4.40, which is inside the budget only if the box is allowed to sleep. The default mode pauses 120 seconds after the last SSH session disconnects, so a 24/7 workload must be put in keepalive mode explicitly. Runs on bare metal in Hetzner Finland, one region. Not established: the x2 to x8 per-slot prices, whether an IPv4 address exists at all, and the egress terms.
- evidence note: Price, slot shape, parked rate, keepalive mode, the IPv6/UDP statement and the key-fingerprint signup are all quoted from the single product page read. The per-slot price table rendered without its rows, so only the x1 price (USD 0.02/hour) is known; the x2-x8 prices are unverified.
- extras:
  - keep_rate: 1.0
  - billing_model: per-minute
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 50
  - session_cap.idle_reap_s: 120
  - session_cap.restart_required: no
  - session_cap.note: in the default stop mode the box pauses 120 seconds after the last SSH session disconnects; keepalive mode removes that and runs 24/7
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: any port over the box's public IPv6, raw TCP and UDP; managed HTTPS endpoint on a shellbox.dev subdomain; no IPv4 address was stated
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.gib: 50
  - ps.price: $0.50 a month per slot while stopped
  - ps.durability: SSD survives a stop
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the slot exists
  - net.out: yes
  - net.in: yes
  - net.ports: a public URL and an email endpoint on creation, with auto-start on HTTP
  - net.static_ip: no
  - term: prepaid balance, no commitment
  - m10h_usd: 4.4
  - m24h_usd: 14.6
  - price_arithmetic: 0.02/hour x 730 h = USD 14.60 at 24/7 for one x1 slot (2 vCPU / 4 GB / 50 GB). 8 h/day over 22 days = 176 h = USD 3.52; 10 h/day = 300 h = USD 6.00. Parked: USD 0.50/month.
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Pay per minute for what you actually use. No subscription, no login - your SSH key fingerprint is your account.' with '$0.02/hr per x1 slot, billed per minute', '$0.50/mo per x1 slot when stopped' and 'ssh shellbox.dev wakeup <name>' for auto-start on HTTP, quoted
  - [1] 2026-10-24: quoted: 'x1 base 2 vCPU · 4 GB RAM · 50 GB SSD. Scale to x8.' and '$0.02/hr per x1 slot, billed per minute.' and 'parked $0.50/mo per x1 slot when stopped.'
  - [1] 2026-10-24: quoted: 'Boxes are real microVMs — each with its own kernel and disk. Every new box gets direct public IPv6 for ssh / mosh / raw TCP-UDP.'
  - [1] 2026-10-24: quoted: 'First time you SSH, an account is created from your key fingerprint. No email, no password, no dashboard.' and 'Payments via Paddle (merchant of record). No card stored by Shellbox. Pre-paid balance, refundable within 3 months.'
  - [1] 2026-10-24: quoted: 'keepalive ... Stay running regardless of connections. For Gitea, n8n, bots, daemons — anything you want up 24/7.' and 'Boxes auto-stop when balance drops below $5 and are deleted at $0.'
  - [1] 2026-11-03: the interface is SSH, with scp and sftp | capture: sha256:eb4481e1d5a6fe3395713344f1bf37792f1c0ecd760852c9bae290d86ff1069d | quote: Pure SSH. Works with VS Code Remote, Zed, mosh (with direct IPv6), scp, sftp.
- sources:
  - [1] https://shellbox.dev/
