# PureVPN

> purevpn.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/purevpn/ | JSON https://fshy.ajam.dev/api/v1/entity/purevpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PureVPN

- `debrid/purevpn` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category commercial VPN: the approved egress class for debrid services that whitelist VPN ranges | tier Standard
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:50.411Z (live) | stale on 2026-11-18
- url https://www.purevpn.com/order
- price USD 2.15/month (2-year) to USD 12.95/month (monthly), no byte meter published | parsed USD 2.15/mo
- free tier: No free plan on the order page; a 31-day money-back guarantee is the only trial-shaped offer: 'All plans are covered by a 31-day money-back guarantee.' | unit: none | metered on: wall-clock | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a tunnel, not an object | source: [1]
- retention: not applicable | source: [1]
- egress: Standard plan: $12.95 per month on the monthly term ('Billed $12.95 for 1 month'), 'Billed $40.80 for 1 year' on the 1-year term, $2.15 per month on the 2-year term ('Billed $58.20 for 2 year', marked '+3 months'), and $1.69 per month on a Black Friday 5-year term ('Billed $101.55 for 5 year', renewing at $1.69/mo after 60 months). The order page states '6,000+ VPN servers' and does not state a bandwidth cap; the plan table sells features, not bytes. | metered: no | source: [1]
- identity: card | detail: Checkout with card; the order page says 'Accepting Credit Cards, PayPal, Bitcoin, and other Crypto payments'. No identity document was mentioned on the page read.
- interface: cli
- limits:
  - per-ip-shaping (binding): the exit address is shared and can change between sessions; each debrid service whitelists or blacklists whole ranges, and a shared exit that someone else abused can be blacklisted [2]
- limits note: A commercial VPN is a server IP, so it fails the same class test as a VPS unless the debrid service has whitelisted the range. The whitelist is by range and by provider, not by customer.
- binding note: Nothing in the VPN's own product limits 1 TiB of monthly transfer; what fails is the debrid side's range check, which returns a block for the whole exit regardless of how much was paid.
- interface detail: Vendor apps and OpenVPN/WireGuard-style configs depending on platform; the order page sells the subscription, not the protocol list.
- tooling: vendor client on desktop and mobile; a VM would run the Linux client or a WireGuard config. The exit address is shared with other customers, which is the point and the risk.
- composes with: The approved egress class for Real-Debrid, AllDebrid and Mega-Debrid, which refuse servers and proxies but authorize VPN ranges: at $2.15-$12.95 a month for unlimited bytes it is the only egress product among those read that is cheaper than the debrid subscription it carries.
- reliability: Shared exits attract abuse, and one debrid service's range check is answered per address: the same subscription can work from one server and be refused from the next.
- notes: It is here only as the price of the approved egress class, and the egress topic owns VPN records; if promoted, merge the pricing with that topic's VPN set rather than keeping two homes. The affiliate pages that rank for 'real-debrid vpn' (vpnalert, vpncompare, vpntrends) all assert cooperative status for NordVPN, Surfshark, ExpressVPN and PIA; they are affiliate content and none of them was treated as evidence.
- evidence note: The price is documented from the vendor order page read. The compatibility claim is a 2020 vendor press release, and the vendor's own live list at real-debrid.com/vpn rendered zero cooperative rows today, so the claim is reported and contradicted rather than confirmed.
- extras:
  - monthly: USD 12.95
  - two_year: USD 2.15/month, billed USD 58.20 for 27 months
  - servers: 6,000+
  - cooperative_claim: 2020 vendor press release; live RD list empty on 2026-10-23
  - sanctioned_for: Real-Debrid; AllDebrid; Mega-Debrid; Deepbrid (premium)
  - bandwidth: not stated on the order page
- evidence:
  - [3] 2026-10-23: vendor press release: 'PureVPN is one of the few "cooperative" VPNs listed on their website', dated 2020-07-28.
  - [1] 2026-11-03: the Standard 2-year term is billed $58.20 | capture: sha256:e851d75095ac8f482cb88ff4b8195c6ffd9db4923230d215caf4536b4a6c140d | quote: Billed $58.20 for 2 year
  - [2] 2026-11-03: PureVPN is a row of the 'Cooperative VPN providers - Recommended' table on the Real-Debrid VPN page | capture: sha256:7c3ab70b8413f29b13a57d9811644c8c123419c2cbab64486f08aa13783b46dc | quote: <td class="t-left">PureVPN</td>
  - [1] 2026-11-03: payment is by card, PayPal or crypto; the order page states 6,000+ VPN servers and a 31-day money-back guarantee | capture: sha256:e851d75095ac8f482cb88ff4b8195c6ffd9db4923230d215caf4536b4a6c140d | quote: Accepting Credit Cards, PayPal, Bitcoin, and other Crypto payments. KPMG proven no-log policy. Gain instant access to 6,000+ VPN servers. All plans are covered by a 31-day money-back guarantee
- sources:
  - [1] https://www.purevpn.com/order
  - [2] https://real-debrid.com/vpn
  - [3] https://www.webnewswire.com/2020/07/28/purevpn-is-now-a-cooperative-vpn-service-for-real-debrid/
