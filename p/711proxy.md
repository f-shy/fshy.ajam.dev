# 711Proxy

> 711proxy.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/711proxy/ | JSON https://fshy.ajam.dev/api/v1/entity/711proxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 711Proxy (Residential Proxies-GB)

- `ip-proxy/711proxy-residential-gb` | paid-only | evidence documented | binding volume-quota | category rotating residential proxy (per GB) and static residential (per IP) | tier Residential Proxies-GB
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-12-04
- url https://www.711proxy.com/
- free tier: No free tier stated. The pricing index lists Residential Proxies-GB from $0.55/GB, Static Residential Proxies from $3.5/IP (Native), Mobile Proxies from $1.45/GB, Residential Proxies-IP from $0.03/IP, Unlimited Proxies by port from $1/port with a 'Trial' badge, and SOCKS5 Proxies from $30/15 days. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The 'Trial' badge on the by-port unlimited product is the only trial marker on the index; its terms were not readable.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Residential Proxies-GB is 'Pay per GB' with 'Rotating & sticky sessions'; the unlimited by-port product does not restrict traffic volume or the number of IPs, with bandwidth fixed by plan tier. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: The sign-up page titled 'Create an account' offers Google sign-in; the form fields were not rendered in the capture, so whether an email code, phone or card is asked is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): Residential Proxies-GB from $0.55/GB, '+5% GB' bonus badge [1]
  - per-ip-shaping: Unlimited Proxies by port: 5 Mbps per port, 3 to 30 minute rotation, from $1/port [2]
- limits note: Static residential per-IP prices from the static page: $3.50/IP for most US cities, $3.90/IP for 'Dual NTT' lines, $4.90/IP for the California Comcast line, with quantity discounts of 2% at 5-9 IPs up to 20% at 200-499 IPs. The pool size (100M+ IPs, 200+ countries) is the vendor's claim.
- binding note: The GB product is metered per GB; the by-port unlimited product swaps the quota for a 5 Mbps per-port ceiling.
- interface detail: HTTP(S) and SOCKS5 forward proxy; residential, unlimited and SOCKS5 products accept username and password or IP whitelisting, static residential accepts username and password only; 'API reselling support' is listed on the GB product.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: unverified: payment methods and refund rules were not readable on the pages captured. The /pricing path resolves to a page whose final URL is /404 while still returning the price index. unverified: no address was looked up, so the 'Native' and 'Dual NTT' registration classes of the static line are not checked (rung 5).
- notes: Named on a Chinese-language proxy forum with the headline '1亿+纯净住宅IP/低至$0.55/GB'. Static, mobile, per-IP and per-port products are on one price index and are held in this one record.
- evidence note: Prices, products and authentication methods are read from the vendor's own pages; pool size and class labels are vendor statements.
- extras:
  - rung: 2
  - rung_note: Rotating residential traffic is rung 2; the static 'Native' lines claim rung 5 and were not looked up.
- evidence:
  - [1] 2026-11-03: The per-GB residential product starts at $0.55 per GB. | capture: sha256:6d47ab63eb4e72c3789c6872e2d1eeaeaa0890989c65aa254bf6ec4e2e62fdd8 | quote: Residential Proxies-GB Genuine residential IPs in 200+ countries/ regions, efficient rotation. From: $0.55 /GB
  - [1] 2026-11-03: The static residential product starts at $3.5 per IP. | capture: sha256:6d47ab63eb4e72c3789c6872e2d1eeaeaa0890989c65aa254bf6ec4e2e62fdd8 | quote: Static Residential Proxies High- performance IP with 99.9 % uptime, exclusive to individuals. From: $3.5 /IP
  - [2] 2026-11-03: The vendor claims a 100M+ residential pool in 200+ countries. | capture: sha256:8df334050da3d89f8b6f91a49984d84c94c518e800d05b67515b8740c2aa18a0 | quote: Over 100M residential IPs from 200+ countries, designed for large-scale data scraping.
  - [2] 2026-11-03: Authentication is username and password or IP whitelisting. | capture: sha256:8df334050da3d89f8b6f91a49984d84c94c518e800d05b67515b8740c2aa18a0 | quote: Our Residential Proxies, Unlimited Proxies and SOCKS5 Proxies support both username/password and IP Whitelisting authentication methods.
  - [3] 2026-11-03: The sign-up page offers account creation with Google sign-in; the field list is not rendered. | capture: sha256:fac6af0660db102804090159840c958461b55b0c936839f16dfe69787e3b11f4 | quote: Create an account
- sources:
  - [1] https://www.711proxy.com/pricing
  - [2] https://www.711proxy.com/
  - [3] https://www.711proxy.com/signup

## 711Proxy (static residential)

- `ip-proxy/711proxy-static-residential` | paid-only | evidence documented | binding per-ip-shaping | category per-address static residential proxy (native and broadcast) | tier Static Residential Proxies, per IP, 7, 30 or 90 days
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-03T07:35:32.366Z (live) | stale on 2026-12-04
- url https://www.711proxy.com/pricing
- price not applicable: an address, not a byte; from USD 3.50 per IP for the Native locations and USD 3.90 per IP for the Dual NTT locations
- free tier: No free tier for the static product. Static Residential Proxies are sold per IP from $3.5 /IP, and the location list prices Native IPs at $3.50/IP, with the Dual NTT locations at $3.90/IP and a Comcast location at $4.90/IP; terms come in 7, 30 or 90 days. Volume discount: 5-9 IPs 2% off, 10-49 IPs 5% off, 50-199 IPs 10% off, 200-499 IPs 20% off. The same vendor also sells Residential Proxies-GB from $0.55 /GB (packs of 5 GB at $15 up to 500 GB+25 GB at $400), Mobile Proxies from $1.45 /GB and Unlimited Proxies by port from $1 /port. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The term-to-price mapping of the static list is not recoverable from the read: the page prints one $/IP figure for each location and the 7, 30 and 90 day durations are named only in the FAQ, so which term the printed price buys is unverified.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [2]
- retention: not applicable: an address, not stored bytes. The lease term is 7, 30 or 90 days and an IP can be renewed before expiry to keep the same address. | source: [1] | note: days is null because no bytes are stored.
- egress: Unlimited bandwidth for static residential IPs: "no bandwidth or session limitations". The unit sold is an address for a term, not a byte. | metered: no | free allowance: unlimited, stated as no bandwidth or session limitations | source: [1]
- identity: email | detail: An account is needed before checkout; the sign-up page offers Google login and a form whose fields the reader did not render, so the exact identifiers (email, phone) are unverified: unverified, the sign-up form fields. Payment by PayPal, cryptocurrency, Alipay, credit card or UnionPay, so a card is not the only rail.
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): one dedicated address per unit, unlimited traffic and sessions, with the term fixed at 7, 30 or 90 days and renewal before expiry to keep the address [1]
  - volume-quota: none for the static product: bandwidth is stated as unlimited; the GB product is sold in packs from 5 GB to 500 GB+25 GB with validity of 30, 90 or 180 days [3]
- binding note: Traffic is unlimited, so no byte quota fails first; what binds is the single address that carries everything and the registration class of that address, which the page labels but does not show.
- interface detail: HTTP(S) and SOCKS5 proxy endpoints; static residential IPs authenticate by username and password only. The home page lists API access for the GB product and API reselling support; whether the static product has an API is unverified.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy. A Cloudflare Worker fetch() takes no proxy option, so the endpoint is reached through a relay that dials SOCKS5 for it. No vendor SDK or rclone backend; that is a note on tooling, not a reason to reject.
- composes with: The upstream sees the leased address instead of a Cloudflare range. The Native label and the Dual NTT location names are the vendor's own words about registration; no delivered address was seen, so the registration class is unverified.
- reliability: Static IPs are dedicated for the term and the vendor states 99.9 % uptime. No throughput, ban or replacement measurement was made.
- notes: The location list marks 50+ regions with the type Native, and names Dual NTT and Comcast carriers in some location labels; it states Native and broadcast residential networks. The Dual NTT label also appears on the IPPeak ISP proxy list. The vendor is named on the Chinese-language forum source; the forum is only the lead, the evidence is the vendor page.
- evidence note: Price, terms, payment rails and the label are read from the vendor pages on 2026-11-03. The step from the label to the delivered address is not tested: no address was bought.
- extras:
  - rung: 5
  - rung_note: The product is sold as a registration-class claim (Native residential); nothing was delivered or looked up, so the class is unverified.
  - dynamic_gb_from_usd: 0.55
  - static_from_usd_per_ip: 3.5
  - payment_rails: PayPal; cryptocurrency; Alipay; credit card; UnionPay
- evidence:
  - [2] 2026-11-03: Static Residential Proxies are sold from $3.5 per IP, type Native, with 99.9 % uptime. | capture: sha256:6d47ab63eb4e72c3789c6872e2d1eeaeaa0890989c65aa254bf6ec4e2e62fdd8 | quote: Static Residential Proxies High- performance IP with 99.9 % uptime, exclusive to individuals. From: $3.5 /IP Native
  - [2] 2026-11-03: The GB residential product starts at $0.55 per GB. | capture: sha256:6d47ab63eb4e72c3789c6872e2d1eeaeaa0890989c65aa254bf6ec4e2e62fdd8 | quote: Residential Proxies-GB Genuine residential IPs in 200+ countries/ regions, efficient rotation. From: $0.55 /GB
  - [1] 2026-11-03: The static list covers 50+ regions and offers both native and broadcast residential networks. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: Covering 50+ regions worldwide. Enjoy exclusive, clean residential IPs, including both native residential and broadcast residential networks.
  - [1] 2026-11-03: Static terms are 7, 30 or 90 days and bandwidth is unlimited. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: packages come with either 7, 30 or 90 days of validity) and enjoy unlimited bandwidth
  - [1] 2026-11-03: Payment rails: PayPal, cryptocurrency, Alipay, credit card and UnionPay. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: You can purchase proxies using PayPal, cryptocurrency, Alipay, credit card and Unionpay.
  - [1] 2026-11-03: The static volume discount ladder: 2, 5, 10 and 20 percent from 5 IPs up to 200-499 IPs. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: Quantity Discount 5-9 IPs 2% off 10-49 IPs 5% off 50-199 IPs 10% off 200-499 IPs 20% off
  - [1] 2026-11-03: A static IP can be renewed before expiry to keep the same address. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: Yes, you can renew your static residential proxy before its expiration, and thus keep the same IP address.
  - [1] 2026-11-03: Static residential proxies authenticate by username and password. | capture: sha256:2406004cabee4a4e6efddd936e1505683099bae6729d6b931c26a93fb933e20b | quote: Our static residential proxies support the authentication method of username and password.
  - [3] 2026-11-03: A 100 GB residential pack costs $99, $0.99 per GB. | capture: sha256:d6e48d8f706328474908ab501e25ced7e327fa0eba4cf734a9e4c2b7d0d0535d | quote: 100 GB Total:$99 $0.99/GB $2/GB
  - [4] 2026-11-03: The sign-up page offers account creation with Google; the other form fields were not rendered in the read. | capture: sha256:fac6af0660db102804090159840c958461b55b0c936839f16dfe69787e3b11f4 | quote: ## Create an account
- sources:
  - [1] https://www.711proxy.com/pricing/regular/static-residential-proxies
  - [2] https://www.711proxy.com/pricing
  - [3] https://www.711proxy.com/pricing/regular/residential-proxies-gb
  - [4] https://www.711proxy.com/signup
