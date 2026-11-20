# vps1

> vps.one | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vps/ | JSON https://fshy.ajam.dev/api/v1/entity/vps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## vps1

- `compute/vps1` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-07T17:40:47.146Z (live) | stale on 2026-12-08
- url https://vps.one/
- price parsed USD 7.1/mo
- free tier: VPS 1 at $7.10 per month on the homepage, under Day / Month / Year terms (the site also names payment three years ahead): 15 GB SSD, 1 CPU, 1 GB RAM, 1 dedicated IP, Linux (AlmaLinux, CentOS, Debian, Ubuntu), in the Netherlands, Slovakia or Serbia. The billing panel's guest order view prices the plan per day (see the evidence rows); its full price list and any month or year cart prices sit behind registration, so the annual and renewal prices are not published on any page read; the plan is orderable (Order buttons, no out-of-stock marker). The vendor's KVM page states 'Traffic for your VPS is unlimited. This means you can host services or applications that require a high bandwidth at no extra cost.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic in the vendor's words on the KVM page, with no allowance and no overage price stated; the tracker instead lists a 5,120 GB monthly figure | metered: no | free allowance: unlimited, as stated on the vendor's KVM page | source: [2]
- identity: any-phone | detail: Registration at the billing panel requires name, email address, password, phone number, plus payer status and full postal address (country, region, ZIP, city, street); read 2026-11-07.
- interface: rest
- limits note: No monthly byte allowance is stated on either vendor page read; the KVM page states unlimited traffic outright. That conflicts with the tracker's 5,120 GB/month and 0.24 Gbps, and the conflict is left standing rather than averaged into a figure neither source gave. If the vendor's unlimited claim holds, the wall is the 15 GB disk and whatever port rate the plan actually has, which no vendor page read states.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with billing at bill.vps1.net; the site exposes a status page and an IP-pool page. No API was read.
- composes with: Fifteen gigabytes of SSD, 1 GB of RAM and a claimed unlimited transfer for $7.10 across three central-European countries is a plausible always-on egress or relay point if the unlimited claim survives a test; the 15 GB disk is the wall that stops it being anything more.
- reliability: no reliability event recorded
- notes: VPS.one provides virtual servers with unlimited traffic on 500 Mbps ports according to vendor specifications. Daily and monthly billing options are available.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - price_on_page: USD 7.10/month for VPS 1
  - renewal_usd: not published: the homepage prices the plan monthly and the billing panel's month and year cart prices sit behind registration
- evidence:
  - [1] 2026-10-22: VPS 1 plan card, quoted cell by cell: '15 Gb SSD', '1 CPU', '1 Gb RAM', '1 dedicated IP', 'Linux operating systems', with the price block reading the dollar sign, '7.10', '/', 'mo'; the location selector offers the three options 'Netherlands', 'Slovakia', 'Serbia' and the page describes 'Tier III data centers in the Netherlands, Slovakia, and Serbia'
  - [2] 2026-10-22: quoted: 'Traffic for your VPS is unlimited. This means you can host services or applications that require a high bandwidth at no extra cost.'
  - [3] 2026-10-22: tracker row, cells in page order: '1 Intel Cores (shared)', '1,024 MB RAM', '15 GB SSD', '5,120 GB/month bandwidth', '0.24 Gbps port speed', 'IPv4', 'Netherlands', price '$7.10 / month'; repeated at the same price for Bratislava Slovakia and Belgrade Serbia
  - [1] 2026-11-07: the homepage prices VPS 1 at $7.10 per month | capture: sha256:06610696da6108aa101e0e6cc833607647f3bb3be642001afe1eb76b43b82ed3 | quote: $7.10/mo
  - [1] 2026-11-07: the vendor states the available billing terms: daily, monthly, yearly | capture: sha256:06610696da6108aa101e0e6cc833607647f3bb3be642001afe1eb76b43b82ed3 | quote: VPS can be paid daily, monthly or for a year at a discount.
  - [1] 2026-11-07: the vendor names the longest prepay term: three years | capture: sha256:06610696da6108aa101e0e6cc833607647f3bb3be642001afe1eb76b43b82ed3 | quote: You can choose daily payment, payment for a month, a year, three years in advance.
  - [4] 2026-11-07: the panel's guest order view prices VPS 1 at $0.30 per day with an Order button, no out-of-stock marker | capture: sha256:45dced53b18814c14b2f545adbee0ed91038d9c22a533a212bf39103305210b7 | quote: VPS 1 0.30$/day Order
  - [5] 2026-11-07: the full order price list answers a login and register page for guests, so cart prices beyond the guest view sit behind registration | capture: sha256:0984c950e6838b77e193beac1481c60d4273ec5353af6e2a792ff98b17b13844 | quote: If you don't have an account
  - [6] 2026-11-07: registration requires a phone number alongside name, email and password | capture: sha256:f634fb829febcc8b7156df872b6b148bea22bd08c1d9369afedfd49ba937d7dd | quote: Name* Email address * Password* Re-enter the password Phone number *
  - [6] 2026-11-07: the register form's required fields | capture: sha256:f634fb829febcc8b7156df872b6b148bea22bd08c1d9369afedfd49ba937d7dd | quote: Name* Email address * Password* Re-enter the password Phone number *
  - [1] 2026-11-07: the entry plan price is unchanged on the homepage | capture: sha256:06610696da6108aa101e0e6cc833607647f3bb3be642001afe1eb76b43b82ed3 | quote: $7.10/mo
- sources:
  - [1] https://vps.one/
  - [2] https://vps.one/kvm-vps
  - [3] https://vpspricetracker.com/provider/vps1/vps
  - [4] https://bill.vps1.net/billmgr?func=showroom.redirect&redirect_to=desktop&startform=service.order.itemtype&newwindow=yes&showroom_id=1
  - [5] https://bill.vps1.net/billmgr?func=v2.vds.order.pricelist
  - [6] https://bill.vps1.net/?func=register&lang=en
