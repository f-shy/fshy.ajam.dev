# Proxy001

> proxy001.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxy001/ | JSON https://fshy.ajam.dev/api/v1/entity/proxy001.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxy001 (residential)

- `ip-proxy/proxy001-residential` | paid-only | evidence documented | binding volume-quota | category per-GB rotating and sticky residential proxy | tier Residential proxies, per GB, from $0.55/GB
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:21:45.722Z (live) | stale on 2026-12-05
- url https://www.proxy001.com/pricing
- price not applicable: sold by the GB with no monthly term; USD 0.7 per GB at the 500 GB pack (USD 350) and USD 1.2 per GB at the 5 GB pack (USD 6)
- free tier: No free allowance on the pricing page. Regular residential packs: 5 GB at $6 on the first recharge only (list $12, $2.4/GB); 20 GB $24, 50 GB $55, 100 + 20 GB $100, 200 GB $180, 500 GB at $350 (list $480); the Regular/Business tabs show $0.55/GB. Purchased traffic does not expire. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The metered direction (downloaded versus both ways) is not stated on the page; downloaded-bytes is the nearest term and is unverified.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [1]
- retention: purchased traffic is valid indefinitely: "your purchased traffic is valid indefinitely". | source: [1] | note: The vendor states no expiry for purchased traffic; days is null because nothing is deleted.
- egress: GB-based billing, SOCKS5/HTTP(S), "Unlimited Bandwidth & Concurrency", unlimited IP extraction; the unit sold is traffic. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: The register page asks for an email address, a verification code sent to it ("Send Code"), a password and agreement to terms, and also offers Sign up with Google. No phone, card or ID document is asked on that page.
- interface: cli, rest
- limits:
  - volume-quota (binding): traffic bought by the GB: 5 GB at $6 on the first recharge only (list $12); 500 GB at $350 (list $480); purchased traffic does not expire [1]
  - request-rate: none stated: Unlimited Bandwidth & Concurrency and unlimited IP extraction [1]
- binding note: Bytes are the unit sold, so the price per GB is what binds: $0.70 per GB at the 500 GB pack and $1.20 per GB at the 5 GB pack.
- interface detail: SOCKS5 and HTTP(S) endpoints; sticky sessions of 1 to 180 minutes or rotation on every request; filtering by country, state, province or city. The vendor supports reseller sub-accounts through CDKey and API; a general API was not otherwise read.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy, reached from a Worker through a relay that dials SOCKS5. No SDK was seen on the pages read.
- composes with: A rotating residential pool: the upstream sees a different home address per request or per sticky session of up to 180 minutes. The pool is sold as real residential broadband IPs; the registration class of a delivered address was not looked up. A different address is not a different registration class.
- reliability: The vendor states 99.8% connectivity and a response time under 0.3 s for its residential pool; no measurement was made here.
- notes: Named on the Chinese-language forum source as a vendor giving away 500M of residential traffic; the forum is the lead and the evidence is the vendor page. The page title also names datacenter proxies.
- evidence note: Price table, protocols, non-expiry and the registration form are read from vendor pages on 2026-11-03. No traffic was bought, so the pool, speed and registration class are unmeasured.
- extras:
  - rung: 6
  - rung_note: A rotating pool changes address, not registration class, so it defeats rung 2 and at most rung 3, not rung 5 by assertion alone.
  - cheapest_listed_usd_per_gb: 0.55
- evidence:
  - [1] 2026-11-03: The Business tier headline price is $0.55 per GB. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: $ 0.55/GB
  - [1] 2026-11-03: The 500 GB pack costs $350, $0.7 per GB. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: 28% 500 GB Unit Price $0.96 → $0.7/GB $350 $480
  - [1] 2026-11-03: Purchased traffic does not expire. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: No, your purchased traffic is valid indefinitely.
  - [1] 2026-11-03: Sticky sessions run 1 to 180 minutes. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: Sticky IPs: Supports setting the online time of an IP from (1-180) minutes.
  - [1] 2026-11-03: Protocols SOCKS5 and HTTP(S). | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: Protocols: SOCKS5/HTTP(S)
  - [2] 2026-11-03: Registration asks for a verification code; the form also has an email address, a password, and Sign up with Google. | capture: sha256:8aeece5f09531808d77585ba300e72ace92b05d78607f6b46715d672d2daf8ce | quote: Verification Code
  - [1] 2026-11-04: The 5 GB pack is $6 against a $12 list, $2.4 per GB list, $1.2 per GB offered, under the First Recharge Offer heading. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: 5 GB Unit Price $2.4 → $1.2/GB $6 $12
  - [1] 2026-11-04: The 500 GB pack is $350 against a $480 list. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: 500 GB Unit Price $0.96 → $0.7/GB $350 $480
  - [1] 2026-11-04: The pack prices sit under a First Recharge Offer heading, so the discounted price applies to the first recharge. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: First Recharge Offer
  - [1] 2026-11-04: The Regular and Business tabs show a $0.55 per GB headline rate. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: $ 0.55/GB
  - [1] 2026-11-04: Purchased traffic does not expire. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: No, your purchased traffic is valid indefinitely.
  - [1] 2026-11-04: The residential plan advertises unlimited bandwidth and concurrency. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: Unlimited Bandwidth & Concurrency
  - [1] 2026-11-04: The vendor claims over 100 million residential IPs with city-level targeting. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: Over 100 million residential lPs, city-level targeting, 99.8% connectivity, response time <0.3s.
  - [1] 2026-11-04: Reseller partnerships by CDKey and API sub-account are offered. | capture: sha256:ec075d5ea19e23cbc61cebafaf975ea7002b34a62e71e000fc2af5546d47cb04 | quote: Proxy001 is recruiting resellers globally, supporting both CDKey and API sub-account partnerships.
  - [3] 2026-11-04: The vendor claims 100M+ IPs in 200+ regions across static, dynamic, residential and mobile. | capture: sha256:41e6b26451bf012040a7e079985e518c759c7ca8f9ec5aa34d6213722ed60ee5 | quote: Access 100M+ premium IPs in 200+ regions—static, dynamic, residential, and mobile—for fast, scalable, and globally reliable connections.
  - probe:www.proxy001.com/signup 2026-11-04: The shorter /signup path answers HTTP 404; sign-up is at /register. | capture: sha256:7f70af24a3143b728207a4b8125ae12ae75582ae57cfdd039604852a7639580e | quote: "status": 404
- sources:
  - [1] https://www.proxy001.com/pricing
  - [2] https://www.proxy001.com/register
  - [3] https://www.proxy001.com/

## Proxy001 (Rotating residential, pay per GB)

- `ip-proxy/proxy001-rotating-residential` | paid-only | evidence documented | binding volume-quota | category rotating residential proxy (per GB) | tier Rotating residential, pay per GB
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-12-04
- url https://www.proxy001.com/
- duplicate of `ip-proxy/proxy001-residential`
- free tier: No free tier on the pricing page. The page prices rotating residential traffic from $0.55/GB (the 'Regular' tab) and sells first-recharge bundles from 5 GB at $6 to 500 GB at $350. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The vendor's forum posts mention a 500 MB trial redemption code; no first-party page read states it, so no trial is recorded.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Billed per GB of traffic: 'GB-based Billing', 'Unlimited Bandwidth & Concurrency', and 'No, your purchased traffic is valid indefinitely. The traffic plan only consumes the allocated traffic quota.' | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: The sign-up form asks for an email address, an emailed verification code and a password, with a Google sign-in alternative; no phone, card or identity document appears on it. Payment methods are shown as icons on the pricing page and were not readable.
- interface: rest
- limits:
  - volume-quota (binding): billed per GB: 'Regular' tab from $0.55/GB; first-recharge bundles 5 GB $6, 20 GB $24, 50 GB $55, 200 GB $180, 500 GB $350; purchased traffic has no expiry [1]
- limits note: The vendor states unlimited bandwidth and concurrency; the binding quantity is the purchased GB. The pool size (100M+ residential IPs, 3,635,214 daily IPs shown) is the vendor's claim and was not measured.
- binding note: Every byte through the pool is metered per GB, so the quota is the purchase size; no request-rate or per-IP limit is stated.
- interface detail: HTTP(S) and SOCKS5 forward proxy (the pricing page lists 'Protocols: SOCKS5/HTTP(S)'); the home page lists APIs and SDKs for Python, Node.js, Puppeteer and Selenium. Sticky sessions of 1 to 180 minutes or a new IP on every request.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself. The vendor offers an API and SDK examples; no client wrapper is needed.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: The pricing page and the sign-up page answered 200; the shorter /signup path answered 404. The pool figures are vendor claims with no independent measurement. unverified (rung 5): whether the exits are registered to a residential ISP; no published address was looked up.
- notes: Named on a Chinese-language proxy forum with a 500 MB trial code and a $0.55/GB headline. The 711Proxy home page quotes the same $0.55/GB headline, a 100M+ pool and 200+ countries with the same wording; whether the two share a backend is unverified.
- evidence note: Price, billing unit, session rule and sign-up fields come from the vendor's own pages; the pool size and the residential claim are vendor statements.
- extras:
  - rung: 2
  - rung_note: A rotating residential pool presents a different single address per request, which is rung 2; no registration class was checked.
- evidence:
  - [1] 2026-11-03: The 'Regular' residential tab starts at $0.55 per GB. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: $ 0.55/GB
  - [1] 2026-11-03: Purchased traffic has no expiry; billing is per GB. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: No, your purchased traffic is valid indefinitely. The traffic plan only consumes the allocated traffic quota.
  - [1] 2026-11-03: Sticky sessions last 1 to 180 minutes; rotating mode changes the IP on every request. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: proxy001 supports sticky IPs and rotating IPs. Sticky IPs: Supports setting the online time of an IP from (1-180) minutes.
  - [1] 2026-11-03: The vendor claims 100 million residential IPs with city-level targeting. | capture: sha256:80e61220c46f5616aa5593bfe61d2f798a61ce70f3ebdba60ac52639f2859433 | quote: Over 100 million residential lPs, city-level targeting, 99.8% connectivity, response time <0.3s.
  - [2] 2026-11-03: The sign-up form asks for an email address, a verification code and a password. | capture: sha256:8aeece5f09531808d77585ba300e72ace92b05d78607f6b46715d672d2daf8ce | quote: Verification Code
  - [3] 2026-11-03: The vendor sells through CDKey distribution and API sub-accounts. | capture: sha256:41e6b26451bf012040a7e079985e518c759c7ca8f9ec5aa34d6213722ed60ee5 | quote: Proxy001 recruits global resellers with two cooperation options: CDKey distribution and API sub-accounts.
  - probe:www.proxy001.com/signup 2026-11-03: The shorter /signup path answers HTTP 404, as the note states. | capture: sha256:034f49985ed471a33ffa93550d70d47941b386eef66ab66260f8b35b9ed31027 | quote: "status": 404
- sources:
  - [1] https://www.proxy001.com/pricing
  - [2] https://www.proxy001.com/register
  - [3] https://www.proxy001.com/
