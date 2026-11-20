# LokiProxy

> lokiproxy.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lokiproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/lokiproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LokiProxy

- `ip-proxy/lokiproxy-rotating-residential` | paid-only | evidence documented | binding volume-quota | category rotating residential proxy (per GB) | tier Rotating Residential Proxy, Premium Plan
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-12-04
- url https://www.lokiproxy.com/
- duplicate of `ip-proxy/lokiproxy`
- free tier: No free tier. The FAQ states 'The LokiProxy Premium Plan offers prices as low as $0.48/GB' and a trial by request: 'Yes, you can contact our online support to test our residential proxies.' | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The trial is granted through a support chat on Telegram, so its size is unverified: behind a contact.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Traffic-billed. 'No, it doesn't. Unlike the basic plan, the traffic purchased with the Premium Plan has no expiration date before allocation.' The Basic plan's traffic is valid 30 days and a high-purity line sells GB bundles valid 90 days. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: The sign-up form was not readable. The terms say registration 'requires you to provide us with your personal data via a dedicated form' and list failure to 'comply with our KYC requests' among grounds to suspend, so a KYC step may be asked; its trigger and documents are unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): Premium Plan from $0.48/GB with no expiry before allocation; Basic plan traffic valid 30 days; high-purity line bundles 5 GB $3.9/GB, 25 GB $2.5/GB, 500 GB $1.5/GB, 1 TB $1.2/GB, valid 90 days [2]
- limits note: Pool claims on the home page: 35M+ residential IPs (rotating), 10M+ (high-purity line), 1,900+ IPv6 blocks as written ('1,900+ OCT unique IPs'). Static residential leases run up to 90 days. All are vendor claims, not measured.
- binding note: All lines are metered per GB or per IP lease; the expiry of purchased traffic differs by plan (none on Premium, 30 days on Basic).
- interface detail: HTTP(S) and SOCKS5; username and password for all products, an IP-allowlist ('API') method for rotating residential and unlimited products only; sticky sessions of 5 to 180 minutes or a new IP per request.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself. The vendor also ships a client app for its short-term residential IPs.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: The /pricing and /register paths returned no content to a page reader; the product page and terms are readable. unverified: payment methods, and the registration class of the exits (rung 5): no address was looked up.
- notes: Named on a Chinese-language proxy forum as '35M+真实住宅IP, 低至0.48美元/GB, 1GB免费试用'. The 1 GB trial is a forum claim; the vendor's own page says only that a trial is available through support.
- evidence note: Price and plan expiry are from the vendor's FAQ and price pages; identity detail is partial.
- extras:
  - rung: 2
  - rung_note: Rotating residential traffic is rung 2; no registration class was checked.
- evidence:
  - [1] 2026-11-03: The Premium Plan starts at $0.48 per GB. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: The LokiProxy Premium Plan offers prices as low as $0.48/GB
  - [1] 2026-11-03: Premium traffic does not expire before allocation; the Basic plan's traffic does. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: No, it doesn't. Unlike the basic plan, the traffic purchased with the Premium Plan has no expiration date before allocation.
  - [1] 2026-11-03: A trial exists by request to support. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: Yes, you can contact our online support to test our residential proxies. Telegram: @lokiproxy
  - [3] 2026-11-03: The vendor claims a 35M+ rotating residential pool. | capture: sha256:01f96e67e3c2c839c6dad88d2b0179cb31e0a500669cf8762441581fe23042b0 | quote: Access 35M+ residential IPs with automatic rotation for seamless web scraping and data extraction.
  - [4] 2026-11-03: The vendor reserves a KYC request step. | capture: sha256:344dc837e79142842a7680446ed365f7f3396d393870bad854c041291b4104b8 | quote: You fail to provide accurate information or comply with our KYC requests
- sources:
  - [1] https://www.lokiproxy.com/product/rotating-residential-proxy
  - [2] https://www.lokiproxy.com/pricing/high-purity-residential-proxies
  - [3] https://www.lokiproxy.com/
  - [4] https://www.lokiproxy.com/TermsOfService.html

## LokiProxy (mingdi Network Technology Research Institute Group, Hong Kong)

- `ip-proxy/lokiproxy` | paid-only | evidence documented | binding volume-quota | category rotating residential proxy | tier Rotating Residential Proxy Premium Plan (per GB)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:30:27.190Z (live) | stale on 2026-12-05
- url https://www.lokiproxy.com/
- price not a per-TB-month product: rotating residential from 0.48 USD per GB (Premium Plan), static residential from 0.12 USD per IP per day.
- free tier: No self-service free tier. 'Do you offer trials? Yes, you can contact our online support to test our residential proxies.' | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A trial exists only through the vendor's support chat; its size is not stated on the pages read.
- per-object cap: not applicable: a traffic pack or an address, not an object | source: [1]
- retention: Premium Plan traffic 'has no expiration date before allocation', unlike the basic plan. Static residential IPs are leased for a period (up to 90 days on the home page) and 'You simply need to extend the validity period before the IP expires' to keep the same address. | source: [1] | note: The short-term residential product is 'Pay per IP. Unused IP credits never expire.'
- egress: Rotating residential and mobile products are billed per GB; static residential 'is billed by time period with no traffic limits'; the unlimited residential product is priced per hour with 'No traffic limits'. | metered: yes | free allowance: none stated; a trial on request through support | source: [2]
- identity: email | detail: The sign-up page offers 'Sign up with Google' or 'Create account' and states 'Ready-to-use upon registration, no complex verification.' The terms also list failure to comply with KYC requests among grounds for suspension, so a KYC step may be requested. The account form fields beyond that were not readable. The refund policy says no refunds are issued after order completion or proxy use.
- interface: unknown
- limits:
  - volume-quota (binding): rotating residential billed per GB from 0.48 USD per GB; high-purity pool from 1.2 USD per GB; mobile from 0.91 USD per GB [3]
  - per-ip-shaping: sticky IP stays for at least 5 to 180 minutes, then until the server restarts; random IP rotates every request [1]
- limits note: Other price points on the navigation: short-term residential IP from 0.02 USD per IP; unlimited residential from 12 USD per hour; static residential from 0.12 USD per IP per day; IPv6 from 1.9 USD per IP. Pool claims: 35 million residential IPs and a 10 million high-purity pool, 190+ countries.
- binding note: The purchased GB is the quantity that runs out; the 0.48 USD per GB floor belongs to the Premium Plan, whose traffic does not expire before allocation.
- interface detail: HTTP and SOCKS5 forward proxy with username-password or IP-allowlist authentication; an API, a client app with port forwarding and a web dashboard are documented. Sticky sessions run 5 to 180 minutes on the rotating product.
- tooling: Any client that speaks an HTTP or SOCKS5 proxy with credentials or an allowlisted source address, or the vendor's client app. Documentation is hosted at docs.lokiproxy.com.
- composes with: The vendor's gateway is an HTTP or SOCKS5 forward proxy, so it is dialled from a host that can open outbound proxy connections (a rented or free virtual machine); the upstream then sees an address from the vendor's pool instead of the host's own.
- reliability: No refunds after order completion or proxy utilisation. The vendor publishes 99.9% success rate and under 0.5 s response, unverified here. The footer logo image on the vendor's pages carries the alt text IPPeak, the name of another proxy vendor with its own record (ip-proxy/ippeak-dual-ntt); whether the two are one operator is not established.
- notes: Seven product lines on one pricing menu: rotating residential, high-purity residential, short-term residential IPs, unlimited residential, static residential, mobile and IPv6. The vendor's own FAQ routes trials through support.
- evidence note: Prices, plan names, trial and registration lines are quoted from the vendor's pages read on 2026-11-03. No address was sampled, so the registration class of the delivered addresses is unverified; the identity-form fields beyond Google or email sign-up were not readable.
- extras:
  - rung: 2
  - rung_note: A rotating residential pool presents a different single address per session (rung 2); the static residential product would reach rung 5 only if its addresses are registered to an access network, which the page states as 'choice of ISP or native IP' without a sample address.
  - pool_claim: 35M+ residential IPs; 10M+ high-purity pool; 190+ countries (vendor claims)
  - possible_same_operator: footer logo alt text IPPeak; see ip-proxy/ippeak-dual-ntt (https://www.ippeak.com/pricing); not established
- evidence:
  - [3] 2026-11-03: The rotating residential product is priced from 0.48 USD per GB on a pool of 35 million+ residential IPs. | capture: sha256:97cf5125682635c1ed8cde26e47ef2ff0bc03935868513c04d6da795fe250f26 | quote: 35 million+ fresh and active residential lPs From$0.48 /GB
  - [3] 2026-11-03: The static residential product is priced from 0.12 USD per IP per day; the same navigation lists mobile from 0.91 USD per GB and unlimited residential from 12 USD per hour. | capture: sha256:97cf5125682635c1ed8cde26e47ef2ff0bc03935868513c04d6da795fe250f26 | quote: Genuine dedicated static residential proxies From$0.12 /IP/Day
  - [1] 2026-11-03: The 0.48 USD per GB price belongs to the Premium Plan, which also supports CDKey allocation and resale. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: <p>The LokiProxy Premium Plan offers prices as low as $0.48/GB, providing a more competitive advantage. It also supports CDKey allocation and resale functions, balancing cost control with usage flexibility.</p>
  - [1] 2026-11-03: A trial exists only by contacting support; there is no self-service free tier. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: <p>Yes, you can contact our online support to test our residential proxies. Telegram: @lokiproxy</p>
  - [2] 2026-11-03: Static residential is billed by time period with no traffic limit. | capture: sha256:9e850742bac5342d5d0a6a97ecfa7aea6855cf2ffe13d7662765cd4c5fb454e8 | quote: <p>LokiProxy's Static Residential Proxy is billed by time period with no traffic limits. It provides stable bandwidth to meet the needs of long-term projects requiring continuous operation.</p>
  - [4] 2026-11-03: Registration offers Google sign-up or account creation and states no complex verification. | capture: sha256:a78096c04bf1993f9241514058d3ab9b2f6373ac690f7a4e02e5eb7f49a0d58d | quote: Ready-to-use upon registration, no complex verification.
  - [5] 2026-11-03: Paid proxy products are not refundable after order completion or use. | capture: sha256:68494e20d9ce3f80b150f3d0bc0421940c603e5d30f5ae9278bf7cf6b69a8aae | quote: No refunds shall be issued upon order completion or proxy utilization.
  - [6] 2026-11-03: The operator is a Hong Kong company; the page claims over 10 million real residential IPs and 35M+ residential IPs. | capture: sha256:d827a0411b7abcea02c2842268db9c13732c591ca86b66793d71b6bb1209fac6 | quote: LokiProxy is developed by mingdi Network Technology Research Institute Group Limited, a Hong Kong-based company.
  - [7] 2026-11-04: Premium Plan traffic has no expiration date before allocation, unlike the basic plan. | capture: sha256:a666a5ecf33680c0f30150290a0f61ed25de9770453288965e9dcf71c8bf5159 | quote: No, it doesn't. Unlike the basic plan, the traffic purchased with the Premium Plan has no expiration date before allocation.
  - [8] 2026-11-04: The terms list failure to comply with KYC requests among grounds for action, so a KYC step may be requested. | capture: sha256:344dc837e79142842a7680446ed365f7f3396d393870bad854c041291b4104b8 | quote: You fail to provide accurate information or comply with our KYC requests
  - [9] 2026-11-04: The high-purity line sells a 1 TB bundle at 1.2 USD per GB valid for 90 Days. | capture: sha256:92fc104cacdaac11def1c940a173a59f64aaf45647d535aa2b7dc33acd923825 | quote: 1 TB $1.2 /GB Total:$1200 Valid for 90 Days
  - [8] 2026-11-04: The terms list failure to comply with KYC requests among grounds for suspension, so a KYC step may be requested. | capture: sha256:344dc837e79142842a7680446ed365f7f3396d393870bad854c041291b4104b8 | quote: You fail to provide accurate information or comply with our KYC requests
- sources:
  - [1] https://www.lokiproxy.com/pricing/rotating-residenial-proxy
  - [2] https://www.lokiproxy.com/pricing/static-proxy
  - [3] https://www.lokiproxy.com/
  - [4] https://www.lokiproxy.com/signup
  - [5] https://www.lokiproxy.com/RefundPolicy.html
  - [6] https://www.lokiproxy.com/aboutus
  - [7] https://www.lokiproxy.com/product/rotating-residential-proxy
  - [8] https://www.lokiproxy.com/TermsOfService.html
  - [9] https://www.lokiproxy.com/pricing/high-purity-residential-proxies
