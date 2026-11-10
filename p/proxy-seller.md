# Proxy-Seller

> proxy-seller.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxy-seller/ | JSON https://fshy.ajam.dev/api/v1/entity/proxy-seller.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxy-Seller

- `ip-proxy/proxyseller-isp-proxy` | qualifies-with-caveat | evidence documented | binding none | category per-address ISP proxy | tier isp
- needs card yes, phone no, ID no, institution no | verified 2026-10-24T10:07:11.000Z (live) | stale on 2026-11-24
- url https://proxy-seller.com/isp/
- price not a per-byte product: priced per IP per term. $0.98/IP in the page title and in the /price/ JSON-LD offer, $3/IP as the ISP page's structured-data minimum price, $0 in the served form. The whole 45 GB a month fits inside one IP's 100 GB default allowance, so one IP is the unit of purchase.
- free tier: No free tier: 'A standard free trial is not available'. The only figure the anonymous page states is its title, 'Buy ISP Proxy - Static Residential Proxies from $0.98/IP', repeated in the meta description; the order form is rendered client-side and the served HTML carries 'Price for 1 IP : $0' and 'Total cost : $0'. Minimum order 1 IP, term 1 week to 12 months. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: The price is a page title, not a price. Three figures exist and none is a checkout price: $0.98/IP in the title and in the /price/ JSON-LD offer, $3/IP as the page's own structured-data 'Minimum Price', and $0 in the unhydrated form. The ladder between them is drawn by JavaScript from the selected country, quantity and period.
- per-object cap: not applicable | source: [1]
- retention: not applicable: an address, not an object | source: [1] | note: What is retained is the address itself, for the rental term: 'a persistent IP that remains unchanged throughout long-running workflows', and 'Static, non-rotating IP addresses'. The address does not rotate per request or per interval, which is the opposite of the residential product the same vendor sells.
- egress: 'Traffic is uncapped at any volume, so web scraping jobs and data collection pipelines scale without hitting a ceiling.' the provider answer qualifies it: 'each IP comes with 100 concurrent threads and 100 GB of traffic by default', and 'To scale your capacity, add more ISP proxies: each new IP brings its own threads and traffic allowance.' No per-GB price is published and no traffic can be bought separately from an IP. | metered: yes | free allowance: no free allowance and no free trial; 100 GB of traffic per IP by default with the counting period unstated on the page | source: [1]
- identity: card | detail: Payment is by card: 'pick a location, enter the required number of IPs, choose a rental term in the calculator, and pay by card, PayPal, or crypto'. Wire is by arrangement rather than at checkout: 'Contact support for wire transfers.' No free trial: 'A standard free trial is not available'. An account is also what unlocks the API key, and the API is the only anonymous-free route to the price ladder.
- interface: rest
- limits:
  - per-ip-shaping: 100 concurrent connections (threads) per ISP proxy IP; a 429 means that IP has hit its connection limit, and only that IP is affected [1]
  - volume-quota: 100 GB of traffic per IP by default; capacity scales by adding IPs, not by buying bytes [1]
  - per-ip-shaping: up to 1 Gbps channel bandwidth per IP, stated elsewhere on the same page as varying by peer [1]
- limits note: Unclassified prose that names no vocabulary kind: minimum order 1 IP for 1 week; quantity steps 1, 25, 50, 100, 250, 500; period steps 1w, 2w, 1mo, 2mo, 3mo, 6mo, 9mo, 12mo; geo-targeting is country at checkout, with city or region by arrangement; 'No monthly lock-ins'; the calculator carries a Customer/Enterprise and a Per IP/Per GB toggle, and the Per GB mode is marked 'Soon', so a byte-priced ISP product is announced but not on sale. Limits are stated to fire 'only by abnormally high load, so most customers never reach them'.
- binding note: Nothing in the vocabulary fails at the scale: 45 GB a month sits under the 100 GB default traffic allowance of a single IP, and 599,000 requests a month is about 0.23 a second averaged against 100 concurrent threads per IP. The first limit that would arrive is a growth limit rather than a scale limit, and the answer to it is a second IP, not a different provider.
- interface detail: HTTP, HTTPS and SOCKS5 forward proxy: 'Any HTTP, HTTPS, or SOCKS5 connects natively, secured by credentials or IP allowlisting.' Authentication is 'username/password or IP allowlist for each order'. A JSON API is documented through five official SDKs (PHP, Node.js, Python, Java, GoLang) reached with an account API key; its base URL and auth header were not read here. A web dashboard handles order, authentication and address listing.
- tooling: Any client that speaks an HTTP or SOCKS5 proxy with credentials or an allowlisted source address: curl -x, python requests, rclone --socks5 or --http-proxy, or a host-side hop for a runtime that cannot dial a proxy itself. The vendor's official Python SDK exposes balance(), referenceList(type='isp'), orderCalcIsp(countryId, periodId, quantity) and proxyList(type='isp'), so both the ISP price ladder and the delivered addresses are readable from an account without a browser.
- composes with: The Worker calls the host, the host calls the ISP endpoint, and the upstream sees an AT&T, Windstream or Frontier eyeball address instead of AS13335. At 45 GB a month one 1-IP order covers the whole traffic.
- reliability: Orders are processed automatically and 'The IP address selection process may take a few minutes', with support to be contacted if the proxies have not arrived within 30 minutes; the location is fixed at purchase and a change needs support. The vendor publishes 99.7% uptime, a 99.5% success rate and about 0.35s response time, all unverified here, and states no address-replacement policy on the ISP page.
- notes: Reading the ladder from https://proxy-seller.com/price/ was tried and ruled out: that page's ISP tab is drawn client-side and the table in the served HTML is the Residential per-GB ladder. The SDK makes this a scripted read rather than a browser session. The provider contradicts the marketing card and both are quoted rather than reconciled: 'Traffic is uncapped at any volume' against '100 GB of traffic by default' per IP, with no period stated and no way to buy traffic without buying an IP, which is why egress.metered is true while binding stays none at 45 GB a month. The schema's interface enum carries no proxy token, so interface holds 'rest' for the documented JSON API and the proxy protocols are in interface_detail, the shape storage/proxyrack-unlimited-residential already uses for a SOCKS5 product.
- evidence note: Every field the verdict rests on is read from the vendor's own pages, and the three upstream ASN holders were checked against RIPE, which is the measured part. The claim the verdict cannot carry is the one the vendor makes loudest: that the delivered addresses sit in those eyeball networks across 200+ Class B and 600+ Class C subnets. No sample address is published, so that stays the vendor's sentence.
- extras:
  - rung: 5
  - rung_note: The product is an address in an ISP-registered network, which is the rung-5 defence exactly; the vendor's 200+ Class B and 600+ Class C subnet claim would also reach rung 3, but it is unverified and no sample address is published, so only rung 5 is claimed.
  - price_signals.title_and_price_index: $0.98/IP (page title, meta description, /price/ JSON-LD Offer with referenceQuantity 1 IP)
  - price_signals.structured_data_minimum: $3/IP (ISP page JSON-LD specification, name 'Minimum Price')
  - price_signals.served_order_form: $0 for 1 IP and $0 total, before hydration
  - price_signals.ladder_readable_anonymously: no
  - upstream_asns[0].asn: AS7018
  - upstream_asns[0].holder: ATT-INTERNET4 - AT&T Enterprises, LLC
  - upstream_asns[0].announced: yes
  - upstream_asns[0].checked: 2026-10-24
  - upstream_asns[1].asn: AS7029
  - upstream_asns[1].holder: WINDSTREAM - Windstream Communications LLC
  - upstream_asns[1].announced: yes
  - upstream_asns[1].checked: 2026-10-24
  - upstream_asns[2].asn: AS5650
  - upstream_asns[2].holder: FRONTIER-FRTR - Frontier Communications of America, Inc.
  - upstream_asns[2].announced: yes
  - upstream_asns[2].checked: 2026-10-24
  - subnet_claim: 200+ Class B and 600+ Class C subnets, vendor's sentence, unverified
  - sample_address_published: no
  - protocols: HTTP/HTTPS/SOCKS5, credentials or IP allowlisting
  - address_behaviour: static and non-rotating for the rental term
  - quantity_steps: 1, 25, 50, 100, 250, 500
  - period_steps: 1w, 2w, 1mo, 2mo, 3mo, 6mo, 9mo, 12mo
  - fair_usage: 100 concurrent threads and 100 GB of traffic per IP by default; 429 on the offending IP only
  - geo_targeting: country at checkout; city or region by arrangement
  - per_gb_mode: announced as 'Soon' in the calculator, not on sale
  - api_methods: orderCalcIsp, referenceList(type='isp'), proxyList(type='isp'), balance
- evidence:
  - [1] 2026-10-24: The price exists only as the title and meta description 'from $0.98/IP'; the served order form carries 'Price for 1 IP : $0' and 'Total cost : $0'; quantity options are 1, 25, 50, 100, 250, 500 IP and period options 1w, 2w, 1mo, 2mo, 3mo, 6mo, 9mo, 12mo, so the minimum order is 1 IP for 1 week.
  - [1] 2026-10-24: The decisive sentence verbatim: 'IPs are distributed across 200+ Class B and 600+ Class C subnets, preventing IP clustering in a single range.' The same page names the upstream carriers as 'Real ASN IPs from AT&T, Windstream, and Frontier' without publishing an AS number or a sample address.
  - [1] 2026-10-24: The provider: 'each IP comes with 100 concurrent threads and 100 GB of traffic by default'; a 429 affects only that IP; 'each new IP brings its own threads and traffic allowance'. This is the sentence that qualifies the 'Traffic is uncapped at any volume' card.
  - [1] 2026-10-24: Access and payment: 'Any HTTP, HTTPS, or SOCKS5 connects natively, secured by credentials or IP allowlisting'; 'pay by card, PayPal, or crypto'; 'Contact support for wire transfers'; 'A standard free trial is not available'.
  - [1] 2026-10-24: The page's own structured data states a 'Minimum Price' of '$3/IP' beside 'Minimum Order Size' '1 IP' and 'Minimum Order Period' '1 week' and 'Traffic' 'Unlimited' — a third price signal, $2.02 above the $0.98 in the title, which is why neither figure can be read as a checkout price.
  - [2] 2026-10-24: The price index lists 'ISP proxies Starts from $0.98' and its JSON-LD carries an Offer of 0.98 USD with referenceQuantity 1 IP; the table rendered in the served HTML is the Residential per-GB ladder, so the ISP per-IP ladder is drawn client-side and is absent from the HTML.
  - probe:https://stat.ripe.net/data/as-overview/data.json?resource=AS7018 2026-10-24: Holder 'ATT-INTERNET4 - AT&T Enterprises, LLC', announced true, ARIN-assigned. Confirms the vendor's AT&T naming resolves to a genuine eyeball carrier.
  - probe:https://stat.ripe.net/data/as-overview/data.json?resource=AS7029 2026-10-24: Holder 'WINDSTREAM - Windstream Communications LLC', announced true, ARIN-assigned. Confirms the vendor's Windstream naming resolves to a genuine eyeball carrier.
  - probe:https://stat.ripe.net/data/as-overview/data.json?resource=AS5650 2026-10-24: Holder 'FRONTIER-FRTR - Frontier Communications of America, Inc.', announced true, ARIN-assigned. Confirms the vendor's Frontier naming resolves to a genuine eyeball carrier.
  - [3] 2026-10-24: The vendor's official SDK defines orderCalcIsp(countryId, periodId, quantity, authorization, coupon, customTargetName), referenceList(type='isp') returning country[] and period[], and proxyList(type='isp'), so the ISP ladder and the delivered addresses are both reachable from an account with an API key.
- sources:
  - [1] https://proxy-seller.com/isp/
  - [2] https://proxy-seller.com/price/
  - [3] https://raw.githubusercontent.com/proxy-seller/user-api-python/v2/proxy_seller_user_api/__init__.py
