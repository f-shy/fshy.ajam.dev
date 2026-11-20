# Proxy-Cheap

> proxy-cheap.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxy-cheap/ | JSON https://fshy.ajam.dev/api/v1/entity/proxy-cheap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Proxy-Cheap

- `debrid/proxy-cheap` | qualifies-with-caveat | evidence documented | binding none | category residential egress: static residential IPv4, per IP per month | tier Static Residential IPv4
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:21:34.000Z (live) | stale on 2026-11-23
- url https://www.proxy-cheap.com/pricing
- price USD 2.71 per IP per month, unlimited bytes
- free tier: No free allowance read; the cheapest entry is '1 week' at $1.99, then $2.71 per month. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an address and a byte stream, not an object | source: [1]
- retention: not applicable: a live endpoint, not stored bytes | source: [1]
- egress: The static residential plan's three published bullets are 'Unlimited Bandwidth', '100+ Threads' and '100+ Mbps'; the price is $2.71 per month per IP (7 days for $1.99, 12 months at the same $2.71 monthly rate). | metered: no | free allowance: none | source: [1]
- identity: card | detail: Checkout at app.proxy-cheap.com; card. No identity document was mentioned on the page read.
- interface: rest
- limits:
  - per-ip-shaping: 100+ Mbps per address, 100+ threads, no byte counter published [1]
- limits note: 100 Mbit/s is 12.5 MB/s, or 1 TiB in 23.9 hours of saturated transfer; that is a throughput ceiling, not a volume ceiling, and it does not bind 1 TiB of monthly transfer.
- binding note: Nothing in the vocabulary fails at 1 TiB/month on this product: no byte meter, no concurrency limit below 100, and 100 Mbit/s clears the 3.24 Mbit/s 1 TiB of monthly transfer needs by a factor of 30.
- interface detail: HTTP(S) proxy endpoint on a fixed address, ordered per IP from the app.proxy-cheap.com checkout.
- endpoint: https://app.proxy-cheap.com/
- tooling: any HTTP proxy client; nothing debrid-specific is needed beyond pointing the downloader at it
- composes with: At $2.71 a month for an address with no byte meter and 100 Mbit/s, this is the cheapest residential-class egress in the set: it makes the total for a prohibited debrid service about $7 a month instead of $1,800.
- reliability: A static residential address is the class a debrid service is least equipped to refuse by inspection, and the class its terms most plainly name as a proxy.
- notes: The single most important number among debrid providers: it is the counter-example to 'a residential proxy costs $2/GB and therefore debrid is pointless'. The metered market is $1.40-$6.00/GB; the static market is $0.30-$2.71 per IP per month with no meter. The two markets are different products and published records should never quote one as the price of the other.
- evidence note: Price, throughput and the unlimited-bandwidth bullet are on the vendor's pricing page read. Whether the address is accepted by a given debrid service is inferred and untested.
- extras:
  - static_residential_monthly: USD 2.71
  - static_mobile: 'from $3.50/proxy' and '$5.99/GB' on the same page
  - rotating_residential: not priced on this page
  - throughput: 100+ Mbps
  - byte_meter: none published
- evidence:
  - [1] 2026-10-23: '$2.71 PER MONTH' with 'Unlimited Bandwidth', '100+ Threads', '100+ Mbps' on the static-residential-ipv4 plans; a 7-day plan at $1.99; datacenter IPv4 at $1.49/proxy and IPv6 at $0.15/proxy for comparison
- sources:
  - [1] https://www.proxy-cheap.com/pricing
