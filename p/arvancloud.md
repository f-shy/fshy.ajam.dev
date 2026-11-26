# Arvan Cloud

> arvancloud.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arvancloud/ | JSON https://fshy.ajam.dev/api/v1/entity/arvancloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Arvan Cloud

- `compute/arvan-cloud` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T11:17:21.728Z (live) | stale on 2026-12-26
- url https://www.arvancloud.ru/pricing/free
- free tier: Quoted and translated from Russian: choosing the Basic Plan lets the user use the provider's free products and functions with no extra charge. Basic packages of the various products are intended to meet basic needs in a limited volume and are recommended for new enterprises and startups. Basic packages renew automatically after a 30-day period, and higher packages can be bought at any time. Free services exclude dedicated support, an SLA and compensation for breach; a Basic Support package is offered for free cloud services. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: The Basic Plan renews automatically after a 30-day period; higher Growth or Professional packages can be bought at any time.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 500 GB of free traffic on a paid server is a useful egress term and belongs in an egress record, not this one. | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits note: There is no free compute lane at all: the free plan covers CDN, object storage, video and support, while the cloud server product is hourly and paid.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The free CDN tier is real and can front a paid or free origin, but it is not compute. Its value is in fronting, not in running anything.
- reliability: no reliability event recorded
- notes: The site previously carried a URL at /products/vps/free which now redirects to the marketing homepage, which is why some lists still attribute a free VPS to Arvan. 500 GB of free traffic on a paid server is a useful egress term and belongs in an egress record, not this one. The registration identity step was not verified on 2026-10-22.
- extras:
  - facets.class: refutation-no-free-vm
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: translated: base plans renew automatically after a 30-day period at no cost, and free services are named as CDN, Object Storage, Video Platform and Support, quoted
  - [2] 2026-10-22: translated: "you can use the free services in four products: ArvanCloud CDN, Object Storage, Video Platform and Support Services", with cloud servers absent from the list, quoted
  - [3] 2026-10-22: cloud servers are promoted with a 40 percent discount, free traffic up to 500 GB and hourly or daily billing, which is a paid product
  - [1] 2026-11-25: the free-tier page states that Basic packages renew automatically after 30 days | capture: sha256:7fbf250a5e45ff017a228ca60e1a80c68b4b98e51245e5de6e27d6dcbb8f23f3 | quote: Да, базовые пакеты автоматически продляются после 30-дневного периода.
  - [1] 2026-11-25: the page states the 30-day renewal and that higher packages can be bought at any time | capture: sha256:7fbf250a5e45ff017a228ca60e1a80c68b4b98e51245e5de6e27d6dcbb8f23f3 | quote: Да, базовые пакеты автоматически продляются после 30-дневного периода. Но вы можете купить более высокие пакеты в любое время.
- sources:
  - [1] https://www.arvancloud.ru/pricing/free
  - [2] https://www.arvancloud.ru/pricing
  - [3] https://t.me/s/arvancloud/1629
