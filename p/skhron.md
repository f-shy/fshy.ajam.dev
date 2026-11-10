# Skhron

> skhron.eu | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/skhron/ | JSON https://fshy.ajam.dev/api/v1/entity/skhron.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Skhron (XSIG-SE-0)

- `compute/skhron-xsig-se-0` | qualifies | evidence documented | binding volume-quota | category IPv6-only VPS | tier XSIG-SE-0
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://skhron.eu/services/sweden
- disagrees on verdict: `compute/skhron` says paid-only, `compute/skhron-xsig-se-0` says qualifies
- free tier: No free tier. XSIG-SE-0 is EUR 1.69 a month: 1 shared vCPU, 512 MiB RAM, 6 GiB SSD, 1 TiB traffic, a routed /64 IPv6 prefix and no IPv4 unless the EUR 0.65 a month add-on is bought. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the plan is billed per period and the disk persists while it is paid; no deletion grace period is printed on the page read | source: [1]
- egress: 1 TiB included on XSIG-SE-0, counted as the sum of inbound and outbound traffic | metered: yes | free allowance: 1 TiB | source: [1]
- identity: email | detail: the vendor states 'No KYC is required to order or use our services'. Payment rails are Bitcoin, Bitcoin Lightning, Monero, Tron, Bitcoin Cash and other crypto through a self-hosted processor, plus Visa, Mastercard and SEPA. No card hold is stated on any page read. The checkout form itself was not reached: the store host skhron.com.ua returns a Cloudflare Bot Fight Mode challenge (HTTP 402) to a non-browser client.
- interface: ssh
- limits:
  - volume-quota (binding): 1 TiB a month, inbound and outbound summed, on the cheapest rung [1]
  - per-ip-shaping: 0.06 vCPU guaranteed on the 1-core rung, bursting to 1 vCPU under the fair-use policy [1]
- binding note: 1 TiB a month counted in both directions is the first thing a WireGuard node or a busy monitor will exhaust; the CPU guarantee is second.
- interface detail: KVM guest with full root access and custom ISO support; a routed /64 (and a free /56 on request) means every port on any address in the prefix is reachable with no NAT layer and no port mapping.
- tooling: any SSH client over IPv6; the vendor's own store runs on skhron.com.ua, which is behind a bot challenge to a non-browser client
- composes with: the cleanest cheap WireGuard or monitor node among documented hosts: a routed /64 means the guest holds real addresses rather than a forwarded port, and NAT64 gives outbound reach to IPv4-only destinations
- reliability: no reliability event observed; the vendor publishes a 99.95% uptime claim and states services that draw sustained attacks may be filtered or null-routed
- notes: The best IPv6-only row in the band on the two properties that matter: a routed /64 rather than a single address, and a NAT64 gateway so the guest can still reach IPv4-only destinations outbound. EUR 1.69 a month is EUR 20.28 a year if billed monthly; the vendor also advertises an annual discount but the annual figure was not read on this page. The EUR 0.65 a month IPv4 add-on is the cheapest conversion to a reachable dual-stack box documented: EUR 2.34 a month total, which is still under the line. Not established: the checkout form's fields, whether the card rail takes a debit or prepaid card, any card hold, the renewal price, and stock. The store host being a different TLD from the marketing site is worth knowing before buying, and its bot challenge means a buyer should expect to complete the order in a real browser.
- evidence note: price, shape, traffic term, the routed /64 statement, the NAT64 statement and the EUR 0.65 IPv4 add-on are quoted from the vendor's own Sweden page read. The order URL is the one the page's own Order button targets but it was not followed to a rendered checkout because the store host challenges non-browser clients, so the cart is unverified while the price is documented.
- evidence:
  - [1] 2026-10-24: quoted plan card: 'XSIG-SE-0 ... CPU Cores 1 (shared) 0.06 vCPU is guaranteed, bursts up to 1 vCPU according to FUP ... Memory 512 MiB ... Disk space 6 GiB SSD ... Traffic incl. 1 TiB ... Price € 1.69'
  - [1] 2026-10-24: quoted: 'Every VPS includes a routed /64 IPv6 prefix at no extra cost. A routed /56 prefix is available free of charge upon request.'
  - [1] 2026-10-24: quoted: 'IPv4 address is not included, but it is available as an add-on at €0.65 per month per address. Each IPv4 address you add is dedicated to your server.'
  - [1] 2026-10-24: quoted: 'Yes. Your server can reach IPv4-only services like GitHub through our NAT64 gateway.' and 'IPv4-only networks can't reach your server without a dedicated IPv4 address.'
  - [2] 2026-10-24: quoted: 'No KYC is required to order or use our services.' and 'Founded in Ukraine and registered in Estonia, Skhron has served hundreds of customers since 2023'; payment rails listed as Bitcoin, Bitcoin Lightning, Monero, Tron, Bitcoin Cash, 'Traditional payments via Visa, Mastercard, and SEPA'
  - [3] 2026-10-24: the Order button's target, read from the page source. Following it returned 'Bot Fight Mode: skhron.com.ua' at HTTP 402 with an 8-word body, so the checkout was not read; skhron.eu/store/... returns 404, so the .com.ua host is the live store
- sources:
  - [1] https://skhron.eu/services/sweden
  - [2] https://skhron.eu/
  - [3] https://skhron.com.ua/store/sweden-kvm-vps/xsig-se-0

## Skhron (compute/skhron)

- `compute/skhron` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T06:08:41.346Z (live) | stale on 2026-12-08
- url https://skhron.eu/services/sweden
- price parsed USD 1.9/mo
- disagrees on verdict: `compute/skhron` says paid-only, `compute/skhron-xsig-se-0` says qualifies
- free tier: XSIG-SE-0: the store cart read 2026-11-07 prices the order form's only billing cycle (12-month pre-pay) at EUR 1.35/month, EUR 16.20 due today; 1 shared Intel Xeon Skylake core (continuous usage of 6% for FUP), 512 MiB RAM, 6 GiB SSD, 1 TiB traffic inbound plus outbound counted together, 1 Gbps shared uplink, Stockholm Sweden; the services page prints EUR 1.69/month with no billing term; renewal price not published; in stock. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TiB per month, inbound and outbound summed; overage is not priced on the page read | metered: yes | free allowance: 1 TiB per month, both directions counted | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 1 TiB a month with inbound and outbound summed, so a mirror that pulls as much as it serves spends the allowance twice as fast [1]
- limits note: 1 TiB a month with inbound and outbound summed, so a mirror that pulls as much as it serves spends the allowance twice as fast
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with custom ISO, a billing portal, and payment in BTC, Lightning, XMR, TRC and BCH through a self-hosted processor, plus Visa, Mastercard and SEPA
- composes with: the only host among documented hosts that states no KYC and takes Monero, so it is the identity-cheapest small box here; 512 MiB and 1 TiB suit a relay or a Tor bridge
- reliability: no reliability event observed; the CPU is 0.06 vCPU guaranteed with burst to 1 under a fair-use policy, so a sustained build will be shaped
- notes: The cart read 2026-11-07 prices the order form's only billing cycle at EUR 1.35/month (EUR 16.20 due today), which matches the tracker's EUR 1.35; the services page still prints EUR 1.69/month with no billing term. Traffic is counted in both directions, which halves the usable 1 TiB for a mirror.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 0.5
  - facets.shape.disk_gib: 6
  - monthly_eur: 1.35
  - annual_eur: not published: the cart prices the 12-month term at EUR 1.35 a month and its summary shows EUR 16.20 due today, with no annual total printed as a separate figure
  - renewal_eur: not published: the cart prices the 12-month term at EUR 1.35 a month and no page names a renewal rate
  - stock: in stock: the cart priced the plan and accepted it
  - price_on_page: EUR 1.69/month (the services page's plan row)
  - term: 12-month pre-pay only: the order form offers no monthly cycle
- evidence:
  - [1] 2026-10-22: XSIG-SE-0 row: 'CPU Cores 1 (shared), 0.06 vCPU is guaranteed, bursts up to 1 vCPU according to FUP, Memory 512 MiB, Disk space 6 GiB SSD, Traffic incl. 1 TiB, Uplink 1 Gbps (shared), Stockholm, Price EUR 1.69', quoted
  - [1] 2026-10-22: XSIG-SE-1 at EUR 2.90 with 1 GiB and 12 GiB; ER-SE-0 on AMD EPYC at EUR 3.00 with 512 MiB, 7 GiB NVMe and a 5 Gbps shared uplink
  - [2] 2026-10-22: 'No KYC is required to order or use our services', quoted; and the Warsaw location is marked 'Out of stock' on the services list
  - [3] 2026-10-22: tracker row 'EUR 1.35 / month, 1 Intel Cores (shared), 512 MB RAM, 6 GB SSD, 1,024 GB/month bandwidth, 1 Gbps port speed, IPv6, Stockholm Sweden', which is EUR 0.34 below the vendor page
  - [4] 2026-11-07: the store cart prices XSIG-SE-0's only billing cycle (12-month pre-pay) at EUR 1.35/month | capture: sha256:124a1fdd6873d140befc51be4af61573914bda77b2be1868f945a11d0ad58657 | quote: 12 Month Price - €1.35
  - [1] 2026-11-07: the services page prints EUR 1.69 for XSIG-SE-0 on 2026-11-07 | capture: sha256:2633667588f795c43a1a6f9f8fa66a47ab9296397c4c0cb0d4371b6da39b2e4e | quote: € 1.69
- sources:
  - [1] https://skhron.eu/services/sweden
  - [2] https://skhron.eu/
  - [3] https://vpspricetracker.com/provider/Skhron/vps
  - [4] https://skhron.com.ua/store/sweden-kvm-vps/xsig-se-0
