# ProxyEmpire

> proxyempire.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxyempire/ | JSON https://fshy.ajam.dev/api/v1/entity/proxyempire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ProxyEmpire

- `debrid/proxyempire` | qualifies-with-caveat | evidence documented | binding volume-quota | category residential egress: rotating residential, static residential, dedicated mobile | tier Rotating residential
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:21:34.000Z (live) | stale on 2026-11-23
- url https://proxyempire.io/pricing/
- price USD 1,536 per TiB metered; USD 2 per static ISP IP per month
- free tier: 'Try residential and mobile proxies for $1.97' - a paid trial, not a free allowance. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: a byte stream and an address, not an object | source: [1]
- retention: not applicable: a live endpoint, not stored bytes | source: [1]
- egress: The page title states the three headline rates: 'Residential $1.50/GB, Mobile $2/GB, ISP $2/IP'; the body adds 'unused GB roll over' and, for dedicated mobile, 'unlimited bandwidth and unlimited IP changes on demand'. | metered: yes | free allowance: none | price per TB: USD 1.50/GB residential, i.e. USD 1,536 per TiB; USD 2.00/IP/month for static ISP; mobile metered at $2/GB or unlimited on a dedicated port | source: [1]
- identity: card | detail: Self-service account with card; the trial costs $1.97 rather than requiring a free registration.
- interface: rest
- limits:
  - volume-quota (binding): rotating products are metered and roll unused GB over; the static ISP and dedicated mobile products are sold per address or port with no meter [1]
- limits note: Unused GB rolling over changes the arithmetic for a bursty workload but not for a steady 1 TiB month, which spends the allowance every month by construction.
- binding note: For the metered product the allowance is the binding constraint at USD 1,536 a TiB; for the $2 static ISP address nothing in the vocabulary binds and the terms of the debrid service become the limit.
- interface detail: HTTP(S) and SOCKS5 with country, region, city, ZIP, ISP, ASN and OS targeting on the rotating products; a fixed address on the static residential and dedicated mobile products.
- endpoint: https://dashboard.proxyempire.io/
- tooling: any HTTP/SOCKS5 client
- composes with: The cheapest credible metered residential rate found ($1.50/GB) and, separately, a $2/month static ISP address and a dedicated mobile port with unlimited bandwidth: one vendor showing all three price shapes side by side, which is why the 'residential egress' question cannot be answered with a single $/GB number.
- notes: Included because it is the only vendor read that prices all three shapes on one page: metered residential, static ISP and unlimited dedicated mobile. That is the evidence that 'what a residential IP costs' has three answers, not one.
- evidence note: The three headline rates are in the page title and the body, read. The per-product detail pages were not opened, so the exact terms behind 'unlimited bandwidth' on the mobile port are untested.
- extras:
  - rates: residential $1.50/GB, mobile $2/GB, ISP $2/IP
  - rollover: unused GB roll over
  - static_residential_countries: 24
  - dedicated_mobile: unlimited bandwidth, unlimited IP changes
- evidence:
  - [1] 2026-10-23: title 'Proxy Pricing: Residential $1.50/GB, Mobile $2/GB, ISP $2/IP'; 'Try residential and mobile proxies for $1.97'; 'unused GB roll over'; dedicated mobile 'unlimited bandwidth and unlimited IP changes on demand'; '30M+ ... residential IPs' and '24 Countries' for static residential
- sources:
  - [1] https://proxyempire.io/pricing/
