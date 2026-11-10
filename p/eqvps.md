# EQVPS

> eqvps.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eqvps/ | JSON https://fshy.ajam.dev/api/v1/entity/eqvps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EQVPS

- `compute/eqvps-nat-nano` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category NAT VPS, outbound only | tier Nano
- needs card no, phone no, ID no, institution no | verified 2026-10-24T02:55:00.000Z (live) | stale on 2026-11-24
- url https://eqvps.com/en/nat
- price parsed USD 3/mo
- free tier: no free tier; Nano is USD 3.00 a month | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the server persists while paid; the page states no deletion clock | source: [1]
- egress: 'Outbound unrestricted - reach any API, registry, chain or site'. No byte cap is stated on the page | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: 'Pay in crypto, no card, no KYC.' Payment is in USDC, USDT, BTC or XMR across nine chains; no card and no ID.
- interface: ssh, cli
- limits:
  - per-ip-shaping (binding): no arbitrary inbound ports; inbound is not yours [1]
  - per-object-cap: 15 GB of NVMe on Nano [1]
  - volume-quota: no byte quota stated; outbound is described as unrestricted [1]
- binding note: inbound is the constraint and it is not a quota: the vendor states there are no arbitrary inbound ports, so nothing on the internet can open a UDP session to this machine.
- interface detail: SSH on a forwarded high port, 20000 plus the VM number, shown in the panel; no port 22
- tooling: any SSH client; the vendor also advertises ordering over MCP
- composes with: the reference example of a cheap machine that is outbound-only: right for a health monitor, wrong for a tunnel endpoint
- reliability: no reliability event recorded
- notes: The page says 'No arbitrary inbound ports - you can't host a public server', and the NAT line separately states inbound on 'your personal port'. That is one forwarded port, not none, so a WireGuard endpoint is not impossible here: it is one port, which is exactly what WireGuard needs. The vendor names no company and the domain was created 2026-05-27.
- evidence note: price, shape, the no-inbound rule and the payment terms are all quoted from the vendor page read
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 1
  - shape.disk_gib: 15
  - billing_model: monthly
  - term: monthly
  - m10h_usd: 3.0
  - m24h_usd: 3.0
  - price_arithmetic: USD 3.00 a month billed monthly; a VPS bills whether it runs
  - free_tier_kind: none
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: one personal inbound port on the NAT line; no arbitrary inbound ports
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: none; it is a container or VM
  - ipv6_prefix: none stated
  - renewal_usd: USD 3.00 a month
  - renewal_note: the vendor states prices are live from its API and marks no first-term promo
  - payment_rails: not read
- evidence:
  - [1] 2026-10-24: quoted plan: 'Nano $3.00/mo - 2 vCPU, 1 GB RAM, 15 GB NVMe, NAT, SSH via a personal port'
  - [1] 2026-10-24: quoted: 'No arbitrary inbound ports - you can't host a public server'
  - [1] 2026-10-24: quoted: 'Pay in USDC, USDT, BTC, XMR on Base, Ethereum, Solana, Bitcoin, Tron, BNB Chain, Polygon or Monero - no card, no ID.'
  - [1] 2026-10-24: quoted: 'On a NAT plan your server sits behind network address translation, and the outgoing IPv4 isn't your own. Outbound is unrestricted; inbound isn't yours.'
  - [2] 2026-10-24: quoted: the NAT line states inbound on 'your personal port' alongside 'No arbitrary inbound ports'
- sources:
  - [1] https://eqvps.com/en/nat
  - [2] https://eqvps.com/
