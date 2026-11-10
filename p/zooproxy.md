# ZooProxy

> zooproxy.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zooproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/zooproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZooProxy

- `ip-proxy/zooproxy-isp-proxy` | trial-only | evidence documented | binding per-ip-shaping | category per-address ISP proxy (native and broadcast) with a residential GB product | tier ISP Proxy, per IP, from $1.80/IP
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T00:30:29.989Z (live) | stale on 2026-12-05
- url https://zooproxy.com/
- price not applicable: an address, not a byte; from USD 1.80 per IP at the entry price
- free tier: A free trial is offered ("Start Free Trial") but its size is not stated on the pages read: unverified, the trial allowance. ISP Proxy is sold per IP "Starting from $1.80/IP"; Residential Proxies from $0.38/GB; Unlimited Traffic - Port from $0.38/Port/Day at 6 Mbps per port; Unlimited Traffic - Bandwidth from $19.67/Day. A cumulative top-up discount of 5 to 30 % applies to static items at $100 to $5000 of recharge. | unit: mixed | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The unit is mixed because the trial allowance is not stated; the true unit would be named by the trial page, which was not read.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [1]
- retention: not applicable: an address, not stored bytes. The vendor states "ZooProxy supports long-term renewal" for the same IP. | source: [2] | note: days is null because no bytes are stored.
- egress: Static ISP plans: Unlimited Bandwidth and "No Extra Traffic Fees"; the plan is priced by region, rental period and number of IPs. | metered: no | free allowance: unlimited for the static ISP product | source: [2]
- identity: email | detail: The sign-up page offers Login with Google or a password form (8-20 characters, letters and numbers) with a Verification code; where the code is sent (email or phone) is unverified: unverified, the code channel. The vendor lists a Telegram contact and an email address for support.
- interface: cli
- limits:
  - per-ip-shaping (binding): one dedicated static IP per unit, unlimited bandwidth, unlimited session duration, term chosen at order [2]
  - volume-quota: none for the static ISP product; the Port plan is 6 Mbps per port [1]
- binding note: Bandwidth is unlimited, so the address and its registration class are what bind; the vendor itself prices Native above Broadcast because they differ in registration versus egress location.
- interface detail: HTTP(S) and SOCKS5, stated in the Static ISP FAQ. No API is named on the pages read.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy, reached from a Worker through a relay that dials SOCKS5. No vendor SDK or CLI is published on the pages read; that is a note on tooling, not a reason to reject.
- composes with: The upstream sees the leased address. The vendor labels each sample as Native ISP or Broadcast ISP and defines the difference as whether the IP registration location matches its internet egress; the Broadcast sample is announced by a US hosting network, which does not match its stated Malaysian location.
- reliability: The vendor shows a risk score of 8% and 5% for its two samples; no throughput, ban or replacement measurement was made.
- notes: The domain fluxisp.com answers HTTP 301 to https://zooproxy.com/, so the vendor named FluxISP on the forum source is this vendor under its present name. The two ISP samples on the pricing page are masked (64.93.*.205 and 162.141.*.52), so they cannot be looked up as addresses; the ASN holders were measured instead. AS7361 is held by DataZone Networks LLC and is announced; the vendor shows it under Johor Bahru, Malaysia with the type Broadcast ISP, so the registration holder and the shown location differ.
- evidence note: Prices, terms and the two ISP samples are read from the vendor pages on 2026-11-03 and the ASN holders are measured through RIPE. The sold addresses are masked, so no delivered address was looked up.
- extras:
  - rung: 5
  - rung_note: The vendor sells registration class explicitly (Native ISP versus Broadcast ISP) and the sample ASNs were checked with RIPE.
  - former_name: FluxISP
  - sample_asns.AS7361: DATAZONE - DataZone Networks LLC (RIPE as-overview, announced)
  - sample_asns.AS9848: SejongTelecom-AS-KR-KR - SEJONG NETWORKS (RIPE as-overview, announced)
- evidence:
  - [1] 2026-11-03: ISP Proxy is sold per IP from $1.80. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Starting from $1.80/IP
  - [1] 2026-11-03: Unlimited Traffic - Port starts at $0.38 per port per day. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Starting from $0.38/Port/Day
  - [1] 2026-11-03: A free trial is offered through the sign-up page. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Start Free Trial
  - [2] 2026-11-03: Native ISP versus Broadcast ISP differ by whether registration location matches egress. | capture: sha256:9d0aed10e272e0375922a8e341022260386b4e36a1a970c4d04f3b3a6a8ff699 | quote: The difference is whether the IP registration location matches its internet egress, affecting account risk control and cost.
  - [2] 2026-11-03: The static ISP plan has no traffic charge. | capture: sha256:9d0aed10e272e0375922a8e341022260386b4e36a1a970c4d04f3b3a6a8ff699 | quote: No. Static ISP plans are priced by IP and rental period, with no additional charges based on traffic usage.
  - [2] 2026-11-03: Protocols HTTP(S) and SOCKS5. | capture: sha256:9d0aed10e272e0375922a8e341022260386b4e36a1a970c4d04f3b3a6a8ff699 | quote: Static ISP proxies support HTTP(S) and SOCKS5 protocols.
  - [2] 2026-11-03: Two samples, a Broadcast ISP one in Johor Bahru under AS7361 and a Native ISP one in Seoul under AS9848. | capture: sha256:9d0aed10e272e0375922a8e341022260386b4e36a1a970c4d04f3b3a6a8ff699 | quote: Broadcast ISP Native ISP IP Address 64.93.*.205 162.141.*.52 Location ZooProxyJohor Bahru, Johor, Malaysia ZooProxySeoul, South Korea ASN AS7361 AS9848
  - [3] 2026-11-03: The sign-up form takes a password; it also offers Login with Google and a Verification code. | capture: sha256:46a76389528447fcca76a1d54ee551cc33d128d4f7390d686a1d69cb24df75c9 | quote: Password length 8-20 characters
  - probe:stat.ripe.net/AS7361/body 2026-11-03: RIPE as-overview on 2026-11-03: AS7361 is held by DataZone Networks LLC and is announced. | capture: sha256:6f40fd5871c89ea728d802009c9bda46d0e1f723b4c011a57e03a9c6d6f63cd1 | quote: "holder":"DATAZONE - DataZone Networks LLC"
  - probe:stat.ripe.net/AS9848/body 2026-11-03: RIPE as-overview on 2026-11-03: AS9848 is held by Sejong Networks and is announced. | capture: sha256:9f662f31ee2d3c5f3bb599dc310d3c161ebafd63aa3f7de9e92952d5d6c47f68 | quote: "holder":"SejongTelecom-AS-KR-KR - SEJONG NETWORKS"
  - probe:www.fluxisp.com 2026-11-03: A probe of www.fluxisp.com on 2026-11-03 ended at https://zooproxy.com/ after an HTTP 301. | capture: sha256:6cacbc1a9e313eb3b02dd82879bb0d336fac343c9c22cf5cfdd1e38b74ecdf20 | quote: "final_url": "https://zooproxy.com/"
  - [4] 2026-11-04: The trial is claimed by contacting support; the FAQ does not say which plans include it. | capture: sha256:c3e1a944ec5c69fcaffd5db9010b21c8e4eba22180c449bf44877cf49f54d3b2 | quote: Some plans include a free trial. You can contact our online support to claim it for free.
  - [1] 2026-11-04: The home page offers a free trial with one sign-up button for the whole product range. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Start with a free trial, or get a custom proxy solution for larger-scale needs.
  - [4] 2026-11-04: The trial is by request to support, as the record states. | capture: sha256:c3e1a944ec5c69fcaffd5db9010b21c8e4eba22180c449bf44877cf49f54d3b2 | quote: Some plans include a free trial. You can contact our online support to claim it for free.
- sources:
  - [1] https://zooproxy.com/
  - [2] https://zooproxy.com/pricing/isp-proxy/
  - [3] https://zooproxy.com/sign-up/
  - [4] https://zooproxy.com/faq/

## ZooProxy (formerly FluxISP)

- `ip-proxy/zooproxy-fluxisp` | paid-only | evidence documented | binding volume-quota | category rotating residential and static ISP proxy | tier Residential Proxies (per GB) and Static ISP (per IP)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-12-04
- url https://zooproxy.com/
- duplicate of `ip-proxy/zooproxy-isp-proxy`
- free tier: Residential from $0.38/GB and ISP proxy from $1.80/IP on the home page, with 'Start Free Trial' on the sign-up button. The FAQ limits that: 'Some plans include a free trial. You can contact our online support to claim it for free.' | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The trial size is not stated on any page read: unverified: behind a contact.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [2]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [2]
- egress: Residential traffic is billed per GB with larger plans cheaper per GB and custom pricing above 10 TB; static ISP plans are 'priced by IP and rental period, with no additional charges based on traffic usage'. | metered: yes | free allowance: trial on request, size unverified | source: [3]
- identity: email | detail: The sign-up page asks for a password of 8 to 20 characters and an emailed 'Verification code', with a Google sign-in alternative; no phone, card or identity document is on the form. Payment is by card, cryptocurrency, Alipay or bank transfer.
- interface: rest
- limits:
  - volume-quota (binding): Residential from $0.38/GB; contact sales above 10 TB [3]
  - per-ip-shaping: Unlimited Traffic - Port plan: 6 Mbps per port from $0.38/port/day; Unlimited Traffic - Bandwidth plan from $19.67/day [2]
- limits note: Static ISP sample rows on the pricing page show a 'Broadcast ISP' address in Johor Bahru, Malaysia under AS7361 (DataZone Networks LLC) and a 'Native ISP' address in Seoul under AS9848 (Sejong Networks), both labelled 'Home Bandwidth IP' with a 'Risk Score' of 8% and 5%; the addresses are masked, so no registry lookup of an address was possible. A RIPE Stat lookup of the two ASNs gave holders DATAZONE - DataZone Networks LLC (ARIN) and SejongTelecom-AS-KR-KR - SEJONG NETWORKS (APNIC).
- binding note: The residential product is metered per GB; the static ISP product is per IP and rental period with no traffic fee.
- interface detail: HTTPS, HTTP and SOCKS5; residential sessions are sticky for 1 to 120 minutes or rotate on every request; static ISP plans support HTTP(S) and SOCKS5.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: https://www.fluxisp.com/ resolves to zooproxy.com, so the FluxISP name now maps to this vendor. The 'Broadcast ISP' sample is registered to a hosting-style AS (DataZone Networks) while its 'IP Category' reads 'Home Bandwidth IP'; the registration class of any live exit was not checked (rung 5).
- notes: Named on a Chinese-language proxy forum as FluxISP ('动态住宅低至$0.4/GB, 静态ISP独享IP'); the vendor now trades as ZooProxy.
- evidence note: Prices, session rules, sign-up fields and payment methods are from the vendor's pages; the pool and class labels are vendor statements; the two ASN holders are a registry lookup of the vendor's published sample rows.
- extras:
  - rung: 5
  - rung_note: The static ISP line claims to clear rung 5 (registration class); only the two sample ASNs were looked up, not a live exit.
- evidence:
  - [2] 2026-11-03: Residential proxies start at $0.38 per GB. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Starting from $0.38/GB
  - [2] 2026-11-03: The static ISP proxy starts at $1.80 per IP. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: Starting from $1.80/IP
  - [4] 2026-11-03: The FluxISP domain serves the ZooProxy site: its final URL is zooproxy.com, so both names are one vendor. | capture: sha256:9ee2cd55153be046d87e3c57dc13420a3fb2d1ce051dd9778a7d34be3b811fe4 | quote: ZooProxy helps businesses collect data, maintain stable sessions, and handle high-traffic workloads with reliable proxy access across different markets.
  - [1] 2026-11-03: A trial exists by request to support. | capture: sha256:c3e1a944ec5c69fcaffd5db9010b21c8e4eba22180c449bf44877cf49f54d3b2 | quote: Some plans include a free trial. You can contact our online support to claim it for free.
  - [1] 2026-11-03: Payment rails are card, crypto, Alipay and bank transfer. | capture: sha256:c3e1a944ec5c69fcaffd5db9010b21c8e4eba22180c449bf44877cf49f54d3b2 | quote: We support payment methods such as credit cards, cryptocurrencies, Alipay, and bank card transfers.
  - [1] 2026-11-03: Sticky sessions last 1 to 120 minutes. | capture: sha256:c3e1a944ec5c69fcaffd5db9010b21c8e4eba22180c449bf44877cf49f54d3b2 | quote: Sticky IP: The IP remains fixed for 1–120 minutes and rotates automatically upon expiration.
  - [5] 2026-11-03: The sign-up form asks for an emailed verification code. | capture: sha256:46a76389528447fcca76a1d54ee551cc33d128d4f7390d686a1d69cb24df75c9 | quote: Verification code
  - [6] 2026-11-03: The vendor separates 'Native ISP' from 'Broadcast ISP' by whether registration and egress locations match. | capture: sha256:9d0aed10e272e0375922a8e341022260386b4e36a1a970c4d04f3b3a6a8ff699 | quote: The difference is whether the IP registration location matches its internet egress, affecting account risk control and cost.
  - [3] 2026-11-03: Residential pricing is custom above 10 TB. | capture: sha256:679bd96a3dd53d55fb0aab1a55a0dbd2d250ad533574bf9c190654a845a08cb2 | quote: If you need more than 10TB of traffic, contact our sales team for custom pricing based on your traffic requirements.
- sources:
  - [1] https://zooproxy.com/faq/
  - [2] https://zooproxy.com/
  - [3] https://zooproxy.com/pricing/residential-proxy/
  - [4] https://www.fluxisp.com/
  - [5] https://zooproxy.com/sign-up/
  - [6] https://zooproxy.com/pricing/isp-proxy/
