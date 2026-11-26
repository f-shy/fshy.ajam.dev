# IpStar

> ipstar.io | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipstar/ | JSON https://fshy.ajam.dev/api/v1/entity/ipstar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IpStar

- `ip-proxy/ipstar-residential` | paid-only | evidence documented | binding volume-quota | category rotating residential, static residential and mobile proxy | tier Residential Proxies (per GB) and Static Residential (per IP)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:30:31.078Z (live) | stale on 2026-12-05
- url https://ipstar.io/
- free tier: No free tier stated on the plan pages. The home page lists residential from $0.33/GB, mobile from $1.61/GB, unlimited residential from $7.91/hour, datacenter from $0.6/IP and static residential from $1/IP, and offers a free web-proxy page. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A second landing page lists different from-prices (residential $0.35/GB, mobile $3.2/GB, datacenter $1/IP, static $1.9/IP), so the from-prices vary by page.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Residential is per GB ('Never Expires' on the home-page tile); static residential is 'Per-IP pricing, no traffic fees'. | metered: yes | free allowance: none stated | source: [2]
- identity: email | detail: The login page says 'Unverified emails will be auto-registered upon verification', with Google sign-in as an alternative, so an email and its verification code open the account; no phone, card or identity document is asked at that step. Payment methods are shown as icons and were not readable.
- interface: rest
- limits:
  - volume-quota (binding): residential from $0.33/GB (home page), $0.35/GB (second landing page); static residential from $1/IP, no traffic fees [1]
- limits note: The pool figure (90M+ residential IPs, 190+ countries) is a vendor claim. The pool is described as 'sourced from carefully selected partners', so supply comes from third-party partners, not from the vendor's own networks.
- binding note: Residential traffic is metered per GB; the static line is per IP with unlimited traffic.
- interface detail: HTTP(S) and SOCKS5; API and username and password extraction; targeting by country, city, state, zip code, coordinates and ASN on the residential line.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: /pricing answers a bot challenge to a page reader and /register returns no content; the static price page is readable through a second reader. unverified: the registration class of the exits (rung 5): no address was looked up.
- notes: Named on a Chinese-language proxy forum as 'IPStar 海外住宅IP代理' with '$0.33/GB' and a referral link.
- evidence note: Prices and the sign-up behaviour are from the vendor's pages; the pool and ISP labels are vendor claims.
- extras:
  - rung: 2
  - rung_note: Rotating residential traffic is rung 2; the static line claims rung 5 and was not looked up.
- evidence:
  - [1] 2026-11-03: Residential proxies start at $0.33 per GB. | capture: sha256:e3b024187fd676582759bdf402bab58aac6fd0dce8b88bae2c69da254ff57a7f | quote: Starting from $0.33 /GB
  - [1] 2026-11-03: Static residential proxies start at $1 per IP. | capture: sha256:e3b024187fd676582759bdf402bab58aac6fd0dce8b88bae2c69da254ff57a7f | quote: Starting from $1 /IP
  - [1] 2026-11-03: The vendor claims a 90M+ residential pool. | capture: sha256:e3b024187fd676582759bdf402bab58aac6fd0dce8b88bae2c69da254ff57a7f | quote: Over 90 million premium residential proxies
  - [3] 2026-11-03: The pool is sourced from partners. | capture: sha256:31647619f86c2bf50ceeea1378bef760f6bc2f85421c919ab9f0acbf8a1b189d | quote: IpStar's residential proxy pool is sourced from carefully selected partners who adhere to business ethics and strict compliance guidelines.
  - [2] 2026-11-03: Static residential is billed per IP with no traffic fee. | capture: sha256:b107993cd0c0c3f6948ccf1be3f2c23050cd504723a37c247021ef3f8d2f65aa | quote: Per-IP pricing, no traffic fees
  - [4] 2026-11-03: An email and its verification create the account. | capture: sha256:ed161838f3cfddbf015dd52dcfaea679e8fcdd46fb0d3d664d1a32da3fe21f7e | quote: Unverified emails will be auto-registered upon verification.
  - [5] 2026-11-03: A second landing page quotes a different from-price. | capture: sha256:c6940b51248c4307638fe3a499c42b9b167689a21380d244e6cfa3158fcedb56 | quote: $0.35/GB
  - [2] 2026-11-04: Static residential is priced per IP with no traffic fee, and the page offers a free trial with no credit card. | capture: sha256:affad6b836e7be99cfe77fa14b85a4f4cc4736f0c911fa067cf9031a2a6bd314 | quote: Per-IP pricing, no traffic fees
  - [2] 2026-11-04: The static trial does not ask for a credit card. | capture: sha256:affad6b836e7be99cfe77fa14b85a4f4cc4736f0c911fa067cf9031a2a6bd314 | quote: No credit card required
  - [2] 2026-11-04: The vendor's own page says static residential addresses are more likely to be identified as proxies by strictly monitored sites. | capture: sha256:affad6b836e7be99cfe77fa14b85a4f4cc4736f0c911fa067cf9031a2a6bd314 | quote: Static residential proxy IPs can bypass standard proxy detection but cannot bypass advanced detection systems. They are more likely to be identified as proxies by strictly monitored websites.
  - [6] 2026-11-04: Residential sessions are unlimited in number; the page shows 0.33 per GB, SOCKS5 and HTTP(S), and the 90M+ pool. | capture: sha256:de2fc60523d0913dc9425d614d3286f21e01061efc64ce045cd29eed30c69cbb | quote: Create unlimited concurrent sessions without worrying about any limits.
- sources:
  - [1] https://ipstar.io/
  - [2] https://ipstar.io/pricing/static
  - [3] https://www.ipstar.io/product/rotating/
  - [4] https://ipstar.io/login
  - [5] https://ipstar.io/unlimited-residential-proxy
  - [6] https://ipstar.io/pricing/residential
