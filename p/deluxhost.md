# DeluxHost

> deluxhost.net | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deluxhost/ | JSON https://fshy.ajam.dev/api/v1/entity/deluxhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeluxHost Storage VPS

- `storage/deluxhost-storage-vps` | qualifies | evidence reported | binding none | category storage-vps
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://deluxhost.net/en/storage
- price $2.22/TB/mo at 20 TB (promo €39.59 = $44.48/mo), $2.47/TB at the steady €43.99 = $49.42/mo. At 5 TB: €10.79 promo = $12.12/mo = $2.42/TB; steady €11.99 = $13.47/mo = $2.69/TB. At 2 TB: $2.02-2.24/TB. This is the cheapest storage outside Europe that is actually orderable today. | parsed USD 2.02/TB-mo
- free tier: STORAGE-1 500 GB / -2 1 TB / -3 2 TB / -4 3 TB / -5 4 TB / -6 5 TB / -10 20 TB. HDD RAID-5 + NVMe cache, Eygelshoven NL, SkyLink DC. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Unlimited Traffic, fair usage' on every storage plan. The Fair Use Policy states: 'DeluxHost does not apply hard caps or automatic blocks to the monthly traffic of its Services' and calculates combined inbound and outbound traffic during the calendar month. Indicative thresholds on German documentation cite 20 TB to 30 TB per month per storage service. | metered: no | free allowance: 30 TB per month | source: [2]
- identity: card | detail: card
- interface: rest, sftp, rsync, smb, rclone, webdav-proxy
- limits note: Per-object-cap: none. RAID-5 single parity. One drive failure tolerated per array, and the provider itself says in its LET threads 'Designed for backups, archives' and not 'a replacement for dedicated or enterprise servers'. Promo discount is 10% for 6 months on STORAGE-3 upward; STORAGE-1/-2 are already at list.
- interface detail: sftp, rsync, rest (self-hosted MinIO/AList), smb
- tooling: rclone SFTP, any backup tool, root KVM
- composes with: Root KVM so MinIO or AList installs and can sit behind Cloudflare. RAID-5 is a single-parity array, weaker than AlphaVPS RAID-60 or ServaRica RAIDZ2.
- reliability: Small NL provider. Its own LET offer threads say 'Extremely limited stock' and it has run repeated waves of renewal price adjustments on its promo VPS lines ('DeluxHost = same quality with a deluxe price increase on first renewal', LET thread 213784). The storage line is explicitly excluded from that practice. 'Monthly pricing does not increase on renewal'. But the operator's history of repricing promo tiers is the single biggest caveat here.
- notes: the same as the free tier
- extras:
  - price_verbatim: $2.22/TB/mo at 20 TB (promo €39.59 = $44.48/mo), $2.47/TB at the steady €43.99 = $49.42/mo. At 5 TB: €10.79 promo = $12.12/mo = $2.42/TB; steady €11.99 = $13.47/mo = $2.69/TB. At 2 TB: $2.02-2.24/TB. This is the cheapest storage outside Europe that is actually orderable today.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 'does not apply hard caps or automatic blocks', IN+OUT counted together
  - [3] 2026-10-21: 'Storage-Server: von 20 TB bis 30 TB pro Monat'
  - [4] 2026-10-21: provider table matching the site, plus 'Monthly pricing does not increase on renewal'
- sources:
  - [1] https://deluxhost.net/en/storage
  - [2] https://deluxhost.net/en/legal/fair-use-policy
  - [3] https://deluxhost.net/de/legal/fair-use-policy
  - [4] https://lowendtalk.com/discussion/219768/

## DeluxHost (X-0)

- `compute/deluxhost-x-0-ipv6` | qualifies-with-caveat | evidence reported | binding volume-quota | category IPv6-only VPS | tier X-0
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-08
- url https://deluxhost.net/en/deals/x
- disagrees on verdict: `compute/deluxhost` says paid-only, `compute/deluxhost-x-0-ipv6` says qualifies-with-caveat
- free tier: No free tier. Offer X-0 is EUR 5.40 a year against a EUR 6.00 list price: 1 vCore, 512 MB DDR4, 10 GB SSD, 1 Gbit/s, unlimited traffic at fair use. The IPv4/IPv6 split is chosen in the cart, where the cart strings include an 'IPv6 only · 1× /64' network option. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: annual billing only on this deal ('annually' in the order URL); the vendor offers a 12-hour refund guarantee on a first order, excluding dedicated servers, licences and IP addresses | source: [2]
- egress: 'Unlimited Traffic, fair usage' with no byte threshold published | metered: no | free allowance: unlimited at fair use, no threshold published | source: [1]
- identity: email | detail: an account on the vendor's dashboard, which offers Google, GitHub and Discord sign-in plus email and password, and a passkey. The checkout form past the sign-in was not read. No card hold is stated. | country: IT
- interface: ssh
- limits:
  - volume-quota (binding): 'Unlimited Traffic, fair usage' with no published threshold - a discretionary throttle, not a quota [1]
  - per-ip-shaping: 1 Gbit/s on X-0 [1]
- binding note: fair use with no number is worse than a quota: there is no ceiling to design against and no threshold at which the node is safe.
- interface detail: a KVM-style VPS sold from a per-product cart; the cart's own network strings offer 'IPv6 only · 1× /64' or '{count}× IPv4 + 1× /64 IPv6', so the IPv6-only variant carries a routed /64 when it is selected.
- tooling: any SSH client over IPv6; the cart is a client-rendered Next.js page, so a buyer should order in a browser
- composes with: EUR 0.45 a month for 512 MB with a /64 is the cheapest annual row found, but the IPv6-only variant is not shown as a distinct plan on the vendor's page and the order path could not be read
- reliability: no reliability event recorded
- notes: The cheapest annual row found, and the one whose evidence is weakest exactly where it matters. The vendor page proves the price (EUR 5.40 discounted, EUR 6.00 list, in stock, annual), and the cart's own strings prove an IPv6-only-with-/64 option exists in the product. What no first-party page says is that X-0 is the IPv6-only variant: the vendor's FAQ claims all plans are dual-stack and IPv6 is free, while the forum post that put this row on the list says 0x IPv4. Both can be true if the cart defaults to IPv6-only and IPv4 is an add-on, but that is an inference and is recorded as one. A buyer should open the cart and read the network selector before paying. Not established: the rendered cart, the price of the extra-IPv4 add-on, payment rails, card hold, and the renewal price on the vendor's own page (the forum says EUR 6, which is the list price).
- evidence note: the price, shape, stock flag and billing period are read from the vendor's own page, but the IPv6-only variant of X-0 is asserted only by a third-party forum post; the vendor's page does not label X-0 as IPv6-only and its FAQ says 'All our locations support native dual-stack IPv4 and IPv6 connectivity'. The cart strings show an IPv6-only option exists, not that X-0 defaults to it.
- evidence:
  - [1] 2026-10-24: quoted plan card in the page's own data: 'X-0 ... 1 vCore ... 512MB DDR4 ... 10GB SSD ... 1Gbit/s Unlimited Traffic, fair usage ... price 6.00€ ... discountedPrice 5.40€ ... stock true ... orderUrl /cart?add=x-0&cycle=annually'
  - [3] 2026-10-24: the cart page's own strings include '"ipv6Only":"IPv6 only · 1× /64"' and '"ipv4AndIpv6":"{count, plural, =1 {1× IPv4} other {#× IPv4}} + 1× /64 IPv6"' and an '"extraIpv4"' add-on priced '{price}/month per IP' - so an IPv6-only choice with a /64 exists in the cart, but the page body is client-rendered and the rendered cart was not read
  - [4] 2026-10-24: third-party offer post, quoted: 'Offer X - X-0: €4/year, renewal €6/year ... 512 MB ... 10GB SSD ... Unlimited traffic (fair usage) ... IP Address: 0x IPv4 / 1 IPv6/64 ... Location: Amsterdam' - the source for treating X-0 as IPv6-only, and it prices the same product at EUR 4 with a EUR 6 renewal against the vendor's EUR 5.40
  - [1] 2026-10-24: quoted FAQ in the page source: 'Yes. All our locations support native dual-stack IPv4 and IPv6 connectivity. IPv6 is available on all plans at no additional cost.' - which contradicts a reading of X-0 as IPv6-only
  - [2] 2026-10-24: the terms state that DeluxHost is a business owned by a sole trader, and carry an Italian VAT number
- sources:
  - [1] https://deluxhost.net/en/deals/x
  - [2] https://deluxhost.net/en/legal/tos
  - [3] https://deluxhost.net/en/cart?add=x-0&cycle=annually
  - [4] https://www.nodeloc.com/t/topic/82206

## DeluxHost (compute/deluxhost)

- `compute/deluxhost` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.077Z (live) | stale on 2026-12-08
- url https://deluxhost.net/vps/
- disagrees on verdict: `compute/deluxhost` says paid-only, `compute/deluxhost-x-0-ipv6` says qualifies-with-caveat
- free tier: VPS-1 at EUR 1.99/month in the Netherlands: Intel Xeon Platinum 8173M, 1 vCore, 2 GB DDR4, 30 GB NVMe, 'Unlimited Traffic, fair usage', 1 Gbit/s port. The vendor page now lists it, matching the tracker's EUR 1.99 row, but its card renders no Order link while every other plan carries one. VPS-2 at EUR 3.99/month (2 vCore, 4 GB, 50 GB NVMe, 2 Gbit/s) is the cheapest plan with an Order link. The hero cards print VPS-6 at EUR 29.99 and VPS-9 at EUR 89.99 flat, with no struck promotional price on either. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Unlimited Traffic, fair usage' on VPS-2 at a 2 Gbit/s port; no number, no overage price and no throttle threshold are stated on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: 'Unlimited Traffic, fair usage' with no number is not an allowance, so no volume quota is stated on this plan; the fair-use clause leaves the throttle point unknown rather than absent, and the 2 Gbit/s port is the only published ceiling. The tracker's EUR 1.99 row is the one row that carries a number, 50,000 GB/month, and that figure is the port converted rather than a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order links are form posts to /en/cart?add=vps-std-2&cycle=monthly; no API, panel name or image list appears on the page read
- composes with: EUR 3.99 for 2 vCores, 4 GB and 50 GB of NVMe in the Netherlands with no metered transfer is the best ratio of RAM to price among evaluated providers after Advin, and 'unlimited, fair usage' suits a crawler front end that cannot predict its monthly bytes; the unmeasured fair-use clause is the risk, since the throttle point is unpublished.
- reliability: no reliability event recorded
- notes: The tracker's EUR 1.99 row and the vendor's VPS-1 card are one offer: the vendor page now lists VPS-1 (1 vCore, 2 GB DDR4, 30 GB NVMe, 1 Gbit/s, Netherlands) at 1.99€/month, but its card renders no Order link while every other plan carries one, so the plan cannot be bought from the page as rendered. VPS-2 at EUR 3.99 is the cheapest plan with an Order link. The struck promotional prices on VPS-6 and VPS-9 no longer print; both cards show 29.99€ and 89.99€ flat. The cart at /en/cart renders client-side; the served HTML carries no price or stock phrase. The vendor names the datacenter as 'Nikhef Amsterdam Qupra DC1 and iNTERWERK Germany' while the plan cards say Netherlands, so the second site's country is not established. Open: VPS-1's stock state in the page's embedded plan data, and what 'fair usage' means in bytes.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 50
  - monthly_eur: 1.99
  - annual_eur: not published: every order link carries cycle=monthly and no page read prints an annual figure
  - renewal_eur: not published: no page read prints a renewal figure
  - billing_term: monthly
  - in_stock: unverified: the vendor page lists VPS-1 without an order button while every other plan carries one, and the cart renders client-side with no readable price or stock phrase
- evidence:
  - [2] 2026-10-22: cheapest and only row, quoted: 'DeluxHost - EUR 1.99 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '30 GB NVMe', '50,000 GB/month bandwidth', '1 Gbps port speed', 'IPv4 + IPv6', 'Netherlands'; product slug VPS_1_Standard_VPS. The page states 'These are the cheapest VPSs currently offered by DeluxHost, starting at EUR 1.99 per month', and the same single plan repeats under Largest Storage, Highest Bandwidth and Highest RAM.
  - [1] 2026-10-22: vendor plan card, quoted: 'VPS-2', 'Netherlands', 'Intel Xeon Platinum 8173M', '2 vCore', 'DDR4 RAM', '4 GB', 'NVMe SSD', '50GB', 'Unlimited Traffic, fair usage', '2Gbit/s', '3.99 EUR/mo'. The page's final URL is /en/vps/standard and its first card is VPS-2; no VPS-1 card appears.
  - [1] 2026-10-22: 'VPS-6' with '10 vCore', '32 GB', '280GB', '10Gbit/s' at '26.99 EUR' from '29.99 EUR/mo' and '-10%'; 'VPS-9' with '16 vCore', '128 GB', '500GB', '10Gbit/s' at '80.99 EUR' from '89.99 EUR/mo'
  - [3] 2026-10-22: the homepage repeats the same cards ('3.99 EUR', '26.99 EUR', '80.99 EUR') and no cheaper plan, so the EUR 1.99 product is absent from two vendor pages and not only one
  - [1] 2026-11-07: the vendor page now lists VPS-1 at EUR 1.99 a month, the plan the tracker priced | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: ## VPS-1 Netherlands Core Intel Xeon Platinum 8173M 1 vCore RAM DDR4 RAM 2 GB Storage NVMe SSD 30GB Bandwidth Unlimited Traffic, fair usage 1Gbit/s ### 1.99€ /mo
  - [1] 2026-11-07: the vendor page lists VPS-1 at EUR 1.99 a month | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: ## VPS-1 Netherlands Core Intel Xeon Platinum 8173M 1 vCore RAM DDR4 RAM 2 GB Storage NVMe SSD 30GB Bandwidth Unlimited Traffic, fair usage 1Gbit/s ### 1.99€ /mo
  - [1] 2026-11-07: the rendered order links carry the monthly cycle | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: [Order now](https://deluxhost.net/en/cart?add=vps-std-2&cycle=monthly)
  - [1] 2026-11-07: the rendered page exposes the order route for VPS-2, the cheapest plan with a buy link | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: [Order now](https://deluxhost.net/en/cart?add=vps-std-2&cycle=monthly)
  - probe:https://deluxhost.net/en/cart?add=vps-std-2&cycle=monthly 2026-11-07: the cart read answers a 253034-byte client-side app shell with no price or stock phrase | capture: sha256:18e07e686a48e26415eceabab52cb146294eedc1b2b381dbbf51c371ee033685 | quote: no-price
  - [1] 2026-11-07: the vendor page now lists VPS-1 at EUR 1.99 a month | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: ## VPS-1 Netherlands Core Intel Xeon Platinum 8173M 1 vCore RAM DDR4 RAM 2 GB Storage NVMe SSD 30GB Bandwidth Unlimited Traffic, fair usage 1Gbit/s ### 1.99€ /mo
  - [1] 2026-11-07: the vendor page still prints the VPS line and now lists VPS-1 at EUR 1.99 a month | capture: sha256:8426c31399f8b7ea84bbbc712384b8daa1345d03fb528e6b5a2cd672d32ac7b0 | quote: ## VPS-1 Netherlands Core Intel Xeon Platinum 8173M 1 vCore RAM DDR4 RAM 2 GB Storage NVMe SSD 30GB Bandwidth Unlimited Traffic, fair usage 1Gbit/s ### 1.99€ /mo
- sources:
  - [1] https://deluxhost.net/vps/
  - [2] https://vpspricetracker.com/provider/DeluxHost/vps
  - [3] https://deluxhost.net/
