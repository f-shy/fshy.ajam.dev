# Webshare

> webshare.io | Debrid, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webshare/ | JSON https://fshy.ajam.dev/api/v1/entity/webshare.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webshare (Debrid)

- `debrid/webshare` | qualifies-with-caveat | evidence documented | binding volume-quota | category residential egress: static residential (ISP) and rotating residential | tier Static Residential (ISP)
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:21:34.000Z (live) | stale on 2026-11-23
- url https://webshare.io/pricing
- price USD 0.30 per static ISP proxy per month within a 20-proxy plan, 250 GB included; rotating residential USD 1.40-3.50/GB
- free tier: A free plan exists: 'Yes. Webshare's free plan includes 10 shared proxies and 1GB of monthly bandwidth, with HTTP and SOCKS5 support. There's no time limit and no credit card required.' | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The free plan is datacenter shared proxies, not residential; the 1 GB applies to the free plan's bandwidth.
- per-object cap: not applicable: an address and a byte stream, not an object | source: [1]
- retention: not applicable: a live endpoint, not stored bytes | source: [1]
- egress: Static residential is priced per proxy with a byte allowance on the plan, not per proxy: 'Static Residential (ISP) is priced per proxy. It starts at $6/month for 20 proxies ($0.30/proxy) and drops to $0.225/proxy at 10,000 proxies.' and 'Proxy Server and Static Residential (ISP) plans include 250GB of bandwidth, and you can upgrade to unlimited bandwidth,.' | metered: yes | free allowance: 250 GB per plan, upgradable to unlimited subject to a fair-use policy | source: [1]
- identity: card | detail: Account at the dashboard; card. The free plan needs no card, the paid plans do.
- interface: rest
- limits:
  - volume-quota (binding): 250 GB per plan included [1]
- limits note: The $0.30 figure is per proxy inside a 20-proxy plan, and the 250 GB is per plan, so the byte allowance does not multiply with the address count.
- binding note: 250 GB is a quarter of 1 TiB of monthly transfer, so the included allowance fails first unless the unlimited upgrade is bought and its fair-use ceiling turns out to be above 1 TiB.
- interface detail: HTTP and SOCKS5 proxy endpoints, authenticated per plan, with a dashboard API for listing the proxies.
- endpoint: https://proxy.webshare.io/
- tooling: any HTTP or SOCKS5 client; the per-plan proxy list is an API call
- composes with: The cheapest address in the set at $0.30 per proxy per month, but the plan carries 250 GB, which is a quarter of the month: the unlimited upgrade clause is the only thing that makes it usable at 1 TiB.
- reliability: The 250 GB plan is the only hard number.
- notes: The rotating ladder is the reference for the metered market and the static price is the reference for the flat market; both are on one page, which makes Webshare the cheapest illustration of the split between the two products.
- evidence note: Prices, the 250 GB allowance and the rotating ladder are on the vendor's pricing page read on 2026-10-23. The fair-use ceiling on the unlimited upgrade is the unknown that decides whether the product survives 1 TiB of monthly transfer.
- extras:
  - static_isp: $0.30/proxy in a $6/month 20-proxy plan, 250 GB per plan, unlimited upgrade by fair use
  - rotating_residential: $3.50/GB (1 GB) down to $1.40/GB (3,000 GB)
  - datacenter: from $0.0179/proxy at scale
  - free_plan: 10 shared proxies, 1 GB/month, no card
- evidence:
  - [1] 2026-10-23: '$6/month for 20 proxies ($0.30/proxy)', 'drops to $0.225/proxy at 10,000 proxies', 'plans include 250GB of bandwidth, and you can upgrade to unlimited bandwidth, ', and 'Rotating Residential... starts at $3.50/GB for a 1GB plan and drops to $1.40/GB at 3,000GB'
- sources:
  - [1] https://webshare.io/pricing

## Webshare (static residential)

- `ip-proxy/webshare-static-residential` | paid-only | evidence documented | binding volume-quota | category per-address ISP proxy | tier Static Residential (ISP)
- needs card yes, phone no, ID no, institution no | verified 2026-10-31T00:42:08.715Z (live) | stale on 2026-12-01
- url https://www.webshare.io/pricing
- price USD 6.00 per month for 20 static ISP proxies (USD 0.30 per address per month), falling to USD 0.225 per address per month at 10,000 addresses; 250 GB included per plan. Priced per address, not per byte. | parsed USD 6/mo
- free tier: No free tier for the Static Residential (ISP) product: its plans start at USD 6 a month for 20 proxies. The account’s free plan, 10 shared proxies with 1 GB a month and no card, is listed in the Proxy Server (datacenter) price table and is a separate offer. | unit: none | metered on: none | read on: 2026-10-31 | source: [1] | note: The free plan’s proxies are datacenter proxies from a pool kept apart from every paid plan, so they are neither a tier nor a trial of this product: the vendor offers '10 datacenter proxies free of charge' and states 'These proxies are not included in any of our paid plans.'
- per-object cap: not applicable | source: [1] | note: The comparable ceiling for this product is the number of addresses bought and the bytes the plan carries, both recorded in limits[], not a per-object size.
- retention: not applicable: an address, not stored bytes. The address itself is static for the life of the plan: 'These proxies are static by default, meaning they keep the same IP address for as long as you need.' | source: [2] | note: Address persistence is the product. The same article names two ways to change it: an Auto-Refresh add-on, and a Replace Proxies feature for a wrong location or a high fraud score.
- egress: Proxy Server and Static Residential (ISP) plans include 250GB of bandwidth, and you can upgrade to unlimited bandwidth,. No overage price per TB appears on either page read 2026-10-24. | metered: yes | free allowance: 250 GB per month included in a Static Residential (ISP) plan; nothing without a paid plan | source: [1]
- identity: card | detail: Card: a plan is paid with a card (Visa, Mastercard, American Express, Discover, Diners, China UnionPay, JCB, Cartes Bancaires or Interac) or with Google Pay or Apple Pay on a mobile device, and the vendor names no other payment method. The account is opened with an email and a password or with a Google account. An ID check through Stripe Identity is not a purchase gate, but it may be requested later to confirm the payment method or a use case. The account’s free plan needs no card, but it is a separate datacenter offer and not this product.
- interface: rest, cli
- limits:
  - volume-quota (binding): 250 GB of bandwidth a month per Static Residential (ISP) plan, with 1000 GB, 5000 GB and unlimited as the other options; unlimited is offered from 100 proxies on shared and private plans and from 50 on dedicated. The limit covers the whole plan, and past it the proxies stop working until the plan changes or the next billing cycle starts. [3]
  - volume-quota (binding): Unlimited-bandwidth plans fall: each is guaranteed at least 10 TB a month, 1 TB per USD 10 of plan price up to USD 1,000 and 1 TB per USD 20 above it; well past the threshold the speed may be throttled from 300-400 Mbps to about 100 Mbps and down to 10 Kbps. [4]
  - per-ip-shaping: Threads 500 - 3,000, listed as a plan spec beside Bandwidth and IP Authorization; the page does not say whether the range is per plan or per address [5]
- limits note: The address count is the unit of purchase, not a limit: 20 addresses at the entry tier, 10,000 at the top, and the byte allowance does not multiply with it, because the 250 GB is included per plan.
- binding note: The 250 GB included allowance is the only ceiling in the vocabulary this product imposes, and it is the one that would fail first: the per-plan thread ceiling and the address count impose nothing at 599,000 requests a month, while 250 GB is about 5.5 times the gateway's inferred ~45 GB a month, so the quota binds only if volume grows past 250 GB or a second workload shares the plan.
- interface detail: The address is reached as an HTTP proxy or a SOCKS5 proxy endpoint: 'Webshare provides static residential proxies with ISP-issued static IPs, up to unlimited bandwidth, and HTTP/SOCKS5 support'. The plan also exposes a dashboard API and a downloadable proxy list (TXT), and lists IP Authorization among its connection controls. The schema's interface tokens carry no value for a proxy protocol, so the two tokens recorded here mean: rest for the control API, cli for any HTTP or SOCKS5 client.
- tooling: Any HTTP or SOCKS5 client connects directly to the proxy address using curl -x, standard language HTTP libraries, or intermediate proxy relays. Proxy endpoint lists can be retrieved programmatically via the dashboard API without panel scraping.
- composes with: It is the rung-5 move for the gateway: the 102 relay Workers supply geographic spread and a per-connection address that are still Cloudflare's, and one Webshare static ISP address supplies an ISP-registered prefix in a non-Cloudflare ASN for the upstreams that refuse Cloudflare's ranges. At $6.00/month for 20 addresses it is the cheapest way to hold several distinct ISP-registered exits at once, and the addresses are static, so a per-upstream choice of exit is possible rather than a per-request draw.
- reliability: The address is static per plan, and the vendor offers a Replace Proxies feature and an Auto-Refresh add-on, so a burned address costs a replacement rather than a new plan; the same help article states that hosting-environment checkers may label the address datacenter and that fraud scores differ between tools, and the product page claims 99.97% uptime.
- notes: Paid-only: the Static Residential (ISP) product has no free tier, trial or recurring credit, and the account’s free plan is a separate datacenter offer. A purchase buys an address whose ASN is a residential ISP, not a residential hosting environment: the vendor states that the IP address belongs to a residential ISP while the server it runs on sits in a datacenter, so a check of the ASN shows a residential ISP such as AT&T or Comcast, and a check of the hosting environment may show datacenter or hosting. Which of the two signals a refusing upstream reads is unverified without a bought address. The same provider is also filed as debrid/webshare, priced there as an egress path. The interface vocabulary has no token for an HTTP or SOCKS5 proxy endpoint, so the protocols are recorded in interface_detail.
- evidence note: Every field the verdict rests on was read on the vendor's own pages on 2026-10-24 and none was measured: the per-address ladder, the 250 GB allowance, the free plan's terms, and the registration-class split.
- extras:
  - rung: 5
  - rung_note: Rung 5 is the registration class, and this is the one vendor in the topic whose own documentation states that the class and the hosting environment disagree, which makes the purchase a test of which signal an upstream reads rather than a guarantee of either.
  - decisive_quote: An ISP proxy lives in two worlds at once: the IP address belongs to a residential ISP, but the server it runs on sits in a datacenter. Tools that check the ASN will correctly show a residential ISP like AT&T or Comcast. Tools that check the hosting environment may label the IP as datacenter or hosting, because, technically, that is where the server is.
  - per_address_usd_month: $0.30 at 20-250 addresses; $0.285 at 500; $0.27 at 1,000; $0.255 at 2,000; $0.24 at 3,000-5,000; $0.225 at 10,000
  - free_plan_class: datacenter, shared: the 10 free proxies are not the static residential product
  - address_replacement: Replace Proxies on demand, plus an Auto-Refresh add-on for automatic changes
  - cheapest_note: $0.30 per address per month is the cheapest verified per-address ISP rate found in this topic, and it is priced per address rather than per gigabyte, which is the unit this topic compares on.
  - read_path: the pricing page also returned the same figures to a direct fetch
- evidence:
  - [1] 2026-10-24: Static Residential (ISP) is priced per proxy: $6/month for 20 proxies ($0.30/proxy), dropping to $0.225/proxy at 10,000 proxies, with the monthly ladder 20 $0.30, 500 $0.285, 1,000 $0.27, 2,000 $0.255, 3,000 $0.24, 5,000 $0.24, 10,000 $0.225. Also: Proxy Server and Static Residential (ISP) plans include 250GB of bandwidth, and you can upgrade to unlimited bandwidth,. Also the free plan: 10 shared proxies, 1GB of monthly bandwidth, HTTP and SOCKS5, no time limit, no credit card.
  - [5] 2026-10-24: The product page's own framing of the same split: Residential trust, datacenter speed, and an IP that never changes; Registered to real internet providers, not hosting companies, so sites treat your traffic like a home connection with datacenter-level speed. Specs: Bandwidth Up to Unlimited* with the footnote * Threads 500 - 3,000, IP Authorization, up to 1 Gbps, 100K+ proxies, 99.97% uptime, HTTP and SOCKS5 endpoints, ISPs named as AT&T, Sprint, Cox Communications, Comcast, RCN and Lumen.
  - [2] 2026-10-24: The vendor states the two-worlds split in its own words: An ISP proxy lives in two worlds at once: the IP address belongs to a residential ISP, but the server it runs on sits in a datacenter. Tools that check the ASN will correctly show a residential ISP like AT&T or Comcast. Tools that check the hosting environment may label the IP as datacenter or hosting, because, technically, that is where the server is. Same article: static by default, same IP for as long as you need, with Auto-Refresh and Replace Proxies as the two ways to change it.
  - [1] 2026-10-31: The cheapest Static Residential (ISP) plan is paid: USD 6 a month for 20 proxies; no free or trial tier of this product is named. | capture: sha256:6f4a1929363f642d80f52cc8f2e10b4888ee92c60ef976b2aa2d14dbcac8c02a | quote: Static Residential (ISP) plans start at $6/month for 20 proxies.
  - [6] 2026-10-31: The free plan's proxies are a pool of their own, outside every paid plan, the Static Residential plans included. | capture: sha256:ee26c007a0c76210389e53a46f47de18a72110fd1e72b0b74a5bedadd9efbab7 | quote: These proxies are not included in any of our paid plans.
  - [3] 2026-10-31: Shared Static Residential plans take 250 GB, 1000 GB, 5000 GB or unlimited bandwidth, unlimited from 100 proxies; the same page sets dedicated at from 50 proxies and says past the limit the proxies stop. | capture: sha256:c572206dbcfa2038ca2834b5639dec3835fe9048865ad9583ea75b90c99a2a01 | quote: Shared: 250 GB, 1000 GB, 5000 GB, unlimited (from 100 proxies)
  - [4] 2026-10-31: The provider, which covers Static Residential plans, guarantees an unlimited-bandwidth plan at least 10 TB a month before throttling. | capture: sha256:beae67a91eb4251011be8fc46e9e8d04685f1c25b9ff33c4faac67d6ea65be86 | quote: All of our Unlimited Bandwidth plans include a guaranteed minimum threshold of 10 TB.
  - [1] 2026-10-31: Static Residential (ISP) is priced per proxy, from 20 proxies at USD 0.30 each to USD 0.225 each at 10,000 proxies. | capture: sha256:6f4a1929363f642d80f52cc8f2e10b4888ee92c60ef976b2aa2d14dbcac8c02a | quote: It starts at $6/month for 20 proxies ($0.30/proxy) and drops to $0.225/proxy at 10,000 proxies.
  - [1] 2026-10-31: A Static Residential (ISP) plan includes 250 GB of bandwidth, with unlimited bandwidth as an upgrade. | capture: sha256:6f4a1929363f642d80f52cc8f2e10b4888ee92c60ef976b2aa2d14dbcac8c02a | quote: Proxy Server and Static Residential (ISP) plans include 250GB of bandwidth, and you can upgrade to unlimited bandwidth,.
  - [5] 2026-10-31: A plan is paid by card, or by Google Pay or Apple Pay on mobile; the same FAQ says no other payment method is supported. | capture: sha256:8682ad1d2b19a7053f2446847999e01dba1173d1c9c9f631ce5bfccef075b094 | quote: Card-based payment methods such as Visa, Mastercard, American Express, Discover and Diners, China UnionPay, JCB, Cartes Bancaires, and Interac
  - [2] 2026-10-31: The vendor states the address's ASN is a residential ISP while its server sits in a datacenter, so ASN checks and hosting checks can disagree. | capture: sha256:f08fe9b537adb4834f529ba52c088fe7343296d4880d8233b42617f3aa8e4a6e | quote: An ISP proxy lives in two worlds at once: the IP address belongs to a residential ISP, but the server it runs on sits in a datacenter.
  - [6] 2026-10-31: The free plan's 10 proxies are datacenter proxies, not static residential (ISP) addresses. | capture: sha256:ee26c007a0c76210389e53a46f47de18a72110fd1e72b0b74a5bedadd9efbab7 | quote: We're excited to offer you 10 datacenter proxies free of charge with Webshare!
  - [7] 2026-10-31: An ID check is not asked of every account, but may be requested to confirm the payment method or a use case. | capture: sha256:eb6afa530b1f7a3d9ca92011eb968a160285b1969195c1c5db2b886fc1b098bd | quote: ID verification isn’t required for all users, but it may be requested in certain situations, such as confirming your payment method or verifying your use case.
  - [8] 2026-10-31: The account is opened with an email address and a password, or with Sign up with Google, and the page states no card is required to register. | capture: sha256:19823a0337c0692c60817cf5d16699cec1d41db8a56e31a358e9d81fcee229cb | quote: Sign Up With Email
  - [5] 2026-10-31: The plan spec still lists Threads 500 - 3,000 beside Bandwidth Up to Unlimited and IP Authorization, and the product's price table starts at 20 proxies for USD 6.00 a month with no free row. | capture: sha256:a5d3b100861657b66a3bf33069d42a958152001fd2992f94d5d42238c5d7fa1c | quote: Threads 500 - 3,000
  - [5] 2026-10-31: The product is still sold as static ISP-issued addresses with up to unlimited bandwidth and HTTP and SOCKS5 endpoints. | capture: sha256:a5d3b100861657b66a3bf33069d42a958152001fd2992f94d5d42238c5d7fa1c | quote: Webshare provides static residential proxies with ISP-issued static IPs, up to unlimited bandwidth, and HTTP/SOCKS5 support for scraping, account management, ad verification, and long-running sessions that require consistent identity.
- sources:
  - [1] https://www.webshare.io/pricing
  - [2] https://help.webshare.io/en/articles/15518733-what-is-a-static-residential-proxy-isp-proxy
  - [3] https://help.webshare.io/en/articles/8370524-how-does-the-bandwidth-limit-work
  - [4] https://help.webshare.io/en/articles/10599445-fair-usage-policy
  - [5] https://www.webshare.io/static-residential-proxy
  - [6] https://help.webshare.io/en/articles/8375287-do-you-offer-proxies-for-free
  - [7] https://help.webshare.io/en/articles/10165357-what-is-id-verification
  - [8] https://dashboard.webshare.io/register
