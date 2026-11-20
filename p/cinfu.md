# Cinfu

> cinfu.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cinfu/ | JSON https://fshy.ajam.dev/api/v1/entity/cinfu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cinfu (Closco Ltd)

- `compute/cinfu-ex2de-ipv6` | dead | evidence documented | binding per-ip-shaping | category IPv6-only VPS | tier EX2DE
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://www.cinfu.com/ipv6-vps
- free tier: No free tier. The German IPv6-only ladder starts at EX0DE, USD 1.11 a month for 256 MB and 20 GB; EX2DE is EUR 2.99 a month for 2 vCPU, 2 GB and 75 GB. Every rung is unmetered bandwidth on a 500 Mbps shared line and includes 5 IPv6 addresses. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: billed monthly through triennially with 5, 10 and 20 percent discounts for the longer terms; no deletion grace period is printed | source: [1]
- egress: 'Unmetered' bandwidth on a 500 Mbps shared network line, for every rung of the IPv6-only ladder | metered: no | free allowance: unmetered, per the plan table | source: [1]
- identity: email | detail: a WHMCS account on panel.cinfu.com with a register.php form; the form's fields were not read. No card hold is stated. Payment rails were not read. | country: SC
- interface: ssh
- limits:
  - per-ip-shaping (binding): 500 Mbps shared network line; 'Unmetered' with no threshold published [1]
  - volume-quota: 5 IPv6 addresses per server, and no IPv4 connectivity from inside the guest [1]
- binding note: the row is unreachable rather than constrained: every 'ORDER NOW' link on the IPv6 page redirects to the bare storefront, so nothing can be bought at the printed price today.
- interface detail: OpenVZ containers per the store's own category listing ('OpenVZ' on every EX card), 5 IPv6 addresses per server, and a free IPv4-to-IPv6 SSH tunnel so an IPv4-only admin can reach the box. The vendor's knowledgebase also says the guest cannot reach IPv4 destinations at all.
- tooling: any SSH client over IPv6, or the vendor's IPv4-to-IPv6 SSH tunnel from an IPv4-only network
- composes with: the cheapest shape-per-dollar on paper in the whole band (2 GB and 75 GB for EUR 2.99) but not under the line, and not buyable: every cart link on the page is dead
- reliability: no reliability event recorded
- notes: Classified as dead rather than as a cheap row because the purchase path does not work: every order link on the IPv6 page carries a pid that the store bounces to the bare storefront, and five of them were fetched individually with the same result. The prices also disagree between the marketing page (USD 1.11 to 11.18) and the store category (EUR 2.99 to 5.99 on monthly), which is a second signal that the page is stale. Two things are worth keeping if the line comes back: the free IPv4-to-IPv6 SSH tunnel is the only admin workaround for an IPv4-only operator found among evaluated providers, and the guest cannot reach IPv4 destinations at all, which is stated plainly in the vendor's own FAQ. The EX range is OpenVZ, so the guest does not get its own kernel, which matters for WireGuard.
- evidence note: the price ladder, shapes, the unmetered line, the 5 IPv6 addresses, the IPv4-tunnel FAQ and the Seychelles company details are all quoted from vendor pages read. The cart is the defect: the pid in every order link redirects to /cart.php with no product, so the price is documented and the purchase path is broken.
- evidence:
  - [1] 2026-10-24: quoted table: 'EX0DE | 1GHz | 256MB | 20 GB | Unlimited | $ 1.11' through 'EX2DE | 2x2GHz | 2GB | 75 GB | Unlimited | $ 3.35', each row linking to…
  - [2] 2026-10-24: the store category the IPv6 page belongs to prices the same products differently: 'EX2DE ... 2048MB RAM ... 2.99EUR Monthly', 'EX1DE ... 5.97EUR Quarterly', 'EX0DE ... 5.94EUR Semi-Annually' - so the marketing page's USD figure and the store's EUR figure are two different views of one product
  - [3] 2026-10-24: fetched 2026-10-24: HTTP 200 with 'x-web-final-url: https://panel.cinfu.com/cart.php' and redirects=followed(2), body 50028 bytes rendering the generic storefront. The same fetch for pid=19 (a shared-hosting product) also redirects. pids 189, 190, 191, 207 and 208 were each fetched and each landed on the bare /cart.php, so the IPv6 order links are…
  - [1] 2026-10-24: quoted: 'Yes, we providing free IPv4 to IPv6 SSH tunneling service.' and 'No, you cannot access IPv4 only servers and websites.'
  - [4] 2026-10-24: quoted: 'Our EX range servers is IPv6 Only VPS servers' and the free IPv4-to-IPv6 SSH tunnel described in the same article
  - [5] 2026-10-24: quoted: 'CINFU Company Details Closco Ltd Reg. Number: 087749 306 Victoria House Victoria, Mahe Seychelles'
- sources:
  - [1] https://www.cinfu.com/ipv6-vps
  - [2] https://panel.cinfu.com/cart.php?gid=20
  - [3] https://panel.cinfu.com/cart.php?a=add&pid=189
  - [4] https://panel.cinfu.com/index.php/knowledgebase/32/What-is-IPv6-Only-VPS-Server-How-to-connect-to-IPv6-Only-VPS-Server-FAQ-about-IPv6-Only-VPS-Servers.html
  - [5] https://www.cinfu.com/company
