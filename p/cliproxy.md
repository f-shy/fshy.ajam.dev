# Cliproxy

> cliproxy.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cliproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/cliproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cliproxy

- `ip-proxy/cliproxy-static-isp` | paid-only | evidence documented | binding per-ip-shaping | category per-address static ISP proxy (native residential and home-broadband broadcast) with a residential GB product | tier Static ISP, per IP, 7, 30 or 90 days
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:32.366Z (live) | stale on 2026-12-04
- url https://cliproxy.com/pricing/static-isp/
- price not applicable: an address, not a byte; from USD 3.0 per IP (home-broadband broadcast, Germany) and USD 3.8 per IP (Residential Native, United States)
- free tier: No free tier is stated on the pages read. Static ISP is sold per IP: Residential Native from $3.8/IP (United States) to $10.0/IP (Thailand, Dubai $8.0/IP), and Home broadband broadcast from $3.0/IP (Germany). Dynamic residential traffic is "As Low as $0.58/GB" and does not expire. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The page lists validity columns 7 day, 30 day and 90 day and up to two prices per location, but the read does not keep the column of each price, so the term that a printed price buys is unverified.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [1]
- retention: not applicable: an address, not stored bytes. Lease terms are 7, 30 and 90 days. | source: [1] | note: days is null because no bytes are stored.
- egress: Static ISP: Unlimited Traffic, no charge for unused IPs; the unit sold is an address for a term. | metered: no | free allowance: unlimited for the static ISP product | source: [1]
- identity: email | detail: No phone, card or ID document is asked on that page; a card may be asked at checkout, which was not read.
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): one dedicated address per unit, unlimited traffic, terms of 7, 30 and 90 days [1]
  - volume-quota: none for the static ISP product; dynamic residential traffic is sold by the GB and never expires [2]
- binding note: Traffic is unlimited; the single address and its registration class bind, and the page itself prices the broadcast class lower than the native one.
- interface detail: Proxy endpoints with sub-accounts, managed through a control panel or an API (documentation at help.cliproxy.com); the residential product supports fixed and rotating sessions.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy, reached from a Worker through a relay that dials SOCKS5. An API with language samples for C/C++, Go, Node.js, PHP, Java and Python is named on the vendor page.
- composes with: The upstream sees the leased address. The page separates Residential Native from Home broadband broadcast, the latter a lower price class; no delivered address was seen, so the registration class is unverified.
- reliability: The vendor states 99% success and 99% uptime; no throughput, ban or replacement measurement was made.
- notes: Named on the Chinese-language forum source as a static-residential lead; the forum is the lead and the evidence is the vendor page.
- evidence note: Prices and labels read from vendor pages on 2026-11-03; no IP was bought and no address was published, so the delivered class is unmeasured.
- extras:
  - rung: 5
  - rung_note: Native versus broadcast is the registration-class claim; nothing was looked up.
  - dynamic_from_usd_per_gb: 0.58
- evidence:
  - [1] 2026-11-03: The static ISP product is labelled Native Residential IP. | capture: sha256:9c83d711af18b3fa9116f9019483d47bf6d3c4b7eb1577e6d0556aa79a88904a | quote: Native Residential IP
  - [1] 2026-11-03: The static ISP product states unlimited traffic. | capture: sha256:9c83d711af18b3fa9116f9019483d47bf6d3c4b7eb1577e6d0556aa79a88904a | quote: Unlimited Traffic
  - [1] 2026-11-03: The static ISP terms are 7, 30 and 90 days. | capture: sha256:9c83d711af18b3fa9116f9019483d47bf6d3c4b7eb1577e6d0556aa79a88904a | quote: Validity period 7 day 30 day 90 day
  - [1] 2026-11-03: The United States Residential Native price points are $3.8 and $5.0 per IP. | capture: sha256:9c83d711af18b3fa9116f9019483d47bf6d3c4b7eb1577e6d0556aa79a88904a | quote: United States $3.8/IP $5.0/IP
  - [1] 2026-11-03: Home broadband broadcast Germany is $3.0 per IP. | capture: sha256:9c83d711af18b3fa9116f9019483d47bf6d3c4b7eb1577e6d0556aa79a88904a | quote: Germany $3.0/IP
  - [2] 2026-11-03: Dynamic residential traffic starts at $0.58 per GB. | capture: sha256:9467fb30ef545e9106ff09661a504f18009b9f58becdf774dbf58dab4978133e | quote: As Low as $0.58/GB
  - [3] 2026-11-03: The sign-up page takes an email address, a password and an optional invitation code. | capture: sha256:e31484721c91f5f0e562186fde027037603884de5c79f547e083f34c8dc3faee | quote: Invitation Code(optional)
- sources:
  - [1] https://cliproxy.com/pricing/static-isp/
  - [2] https://cliproxy.com/traffic-introduct/
  - [3] https://cliproxy.com/sign-up/
