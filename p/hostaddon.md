# HostAddon

> hostaddon.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostaddon/ | JSON https://fshy.ajam.dev/api/v1/entity/hostaddon.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostAddon

- `compute/hostaddon` | paid-only | evidence documented | binding volume-quota | category cloud VM | tier MVPS 1 (10 Gbit metered, USA)
- identity a placeholder: card and phone unknown | verified 2026-10-28T04:25:21.642Z (live) | stale on 2026-11-28
- url https://www.hostaddon.com/budget-10gbps-metered-vps/
- price parsed USD 3.99/mo
- free tier: No free tier. Cheapest paid offer: MVPS 1 on the 10 Gbit metered NVMe KVM line, 1 vCPU, 512 MB RAM, 10 GB NVMe, 10 Gbit shared port, 3 TB bandwidth, 1 IPv4 and 1 IPv6, USD 3.99 per month, with 10% off on a 1-year plan. Locations: USA, Canada, France, Germany, Netherlands, UK, Turkey, Hong Kong and India, plus an OFFSHORE entry. | unit: none | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: MVPS 2 is 1 vCPU, 1 GB RAM, 20 GB NVMe, 5 TB at USD 6.99 per month; MVPS 3 is 2 vCPU, 2 GB RAM, 40 GB NVMe, 8 TB at USD 9.99 per month; the 1 Gbps Budget NVMe NANO is 2 vCPU, 2 GB RAM, 30 GB NVMe, 3 TB at USD 6.49 per month
- per-object cap: not applicable | source: [1]
- retention: not applicable: the unit is a machine, not stored bytes; no deletion or suspension term was read | source: [1] | note: a machine record: what is lost is the running process and its disk
- egress: 3 TB a month of bandwidth on MVPS 1 over a 10 Gbit port connected to the node as a common channel; the Turkey location has reduced bandwidth quotas; no overage price was read | metered: yes | free allowance: 3 TB a month on MVPS 1 | source: [1]
- identity: email | detail: unverified: the order form fields were not read. The client area states an account is created by placing an order. The vendor lists cards, PayPal and cryptocurrency as payment methods and states there is no KYC for crypto, and says orders using its forum coupon get manual fraud review; a buyer in the same thread reports being refused with a fraud flag.
- interface: unknown
- limits:
  - volume-quota (binding): 3 TB a month of bandwidth on MVPS 1; Turkey has reduced bandwidth quotas [2]
  - per-ip-shaping: 10 Gbit port shared as a common channel to the server node [1]
  - per-object-cap: 10 GB of NVMe and 512 MB of RAM on MVPS 1 [1]
- limits note: The vendor states its infrastructure is rented dedicated servers, leases and resale.
- binding note: 3 TB a month on a shared 10 Gbit port is the number that runs out first on this plan.
- interface detail: a WHMCS client area at hostaddon.com/clients; no API or CLI was read
- tooling: client-area panel and support tickets; no API, CLI or Terraform provider was read on the pages fetched
- composes with: A 10 Gbit shared port with 3 TB a month at USD 3.99 across 9 locations, including Hong Kong, India and Turkey, gives a low-priced exit point in regions that few budget hosts cover.
- reliability: unverified: no outage history was read; a buyer reported a fraud-flagged payment refusal on a new account using the forum coupon.
- notes: The vendor also lists a 10 Gbit unmetered line from USD 9.99, a 1 Gbps budget line, high-capacity HDD storage VPS, Ryzen 9 and 25 Gbps lines, and offshore VPS in Sweden, Netherlands, Malaysia, Bulgaria and Switzerland; those pages were not read. The page prices are in USD with an INR currency selector in the client area.
- evidence note: Identity fields remain unverified against checkout pages.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 0.5
  - shape.disk_gib: 10
  - shape_derived: ram_gib 0.5 = 512 MB / 1024
  - billing_model: allocated
  - monthly_usd: 3.99
  - price.amount: 3.99
  - price.currency: USD
  - price.term: month
  - price.annual_discount: 10% on a 1-year plan
  - location: USA (plan code HAUS), Canada, France, Germany, Netherlands, UK, Turkey, Hong Kong, India
  - payment_methods.card: listed
  - payment_methods.paypal: listed
  - payment_methods.crypto: BTC, ETH and others; the vendor states no KYC for crypto
  - payment_methods.source_url: https://lowendtalk.com/discussion/220041/hostaddon-vps-1-2-10gbps-nvme-from-3-99-mo-25-off-30-locales-storage-streaming-vpn
  - payment_methods.read_on: 2026-10-28
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-28: the 10 Gbit metered line starts at USD 3.99 per month | capture: sha256:ed107fbbc70f5c77ba90ba1a3e41eac152f75da22c3a59837decdf9be635d2a9 | quote: ### Starting @ Just $3.99/mo
  - [1] 2026-10-28: MVPS 1 is 1 vCPU, 512 MB RAM, 10 GB NVMe, a 10 Gbit port, 3 TB bandwidth, 1 IPv4 and 1 IPv6 | capture: sha256:ed107fbbc70f5c77ba90ba1a3e41eac152f75da22c3a59837decdf9be635d2a9 | quote: * 1 Core CPU * 512 MB RAM * 10 GB SSD NVMe * 10 Gbit Port\* * 3 TB Bandwidth * 1 Free IPv4 * 1 Free IPv6
  - [1] 2026-10-28: a 1-year plan takes 10% off | capture: sha256:ed107fbbc70f5c77ba90ba1a3e41eac152f75da22c3a59837decdf9be635d2a9 | quote: Save 10% with 1 Year Plan
  - [1] 2026-10-28: the page lists USA, Canada, France, Germany, Netherlands, UK, Turkey, HK, India and OFFSHORE | capture: sha256:ed107fbbc70f5c77ba90ba1a3e41eac152f75da22c3a59837decdf9be635d2a9 | quote: #### USA #### Canada #### France #### Germany #### Netherlands #### UK #### Turkey #### HK #### India #### OFFSHORE
  - [1] 2026-10-28: the 10 Gbit port is a common channel to the node, not a dedicated one | capture: sha256:ed107fbbc70f5c77ba90ba1a3e41eac152f75da22c3a59837decdf9be635d2a9 | quote: \*10 Gbps Port Speed Connected as Common Channel to the Server Node.
  - [2] 2026-10-28: the vendor's own post gives the same MVPS 1 shape at USD 3.99 per month, 3 TB per month, and USD 2.99 on the first invoice with its coupon | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: | MVPS 1 | 1 | 512MB | 10GB | 10Gbps shared | 3TB/mo | $3.99/mo | $2.99/mo first invoice or $43/Year |
  - [2] 2026-10-28: locations for the metered line, with reduced bandwidth quotas in Turkey | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: Locations: USA, Canada, France, Germany, Netherlands, UK, Turkey, Hong Kong, India (TR has reduced bandwidth quotas — ask me and I'll post the exact numbers).
  - [2] 2026-10-28: the vendor calls the metered 10 Gbit line its lowest entry point | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: [10Gbps-port NVMe KVM (metered)](https://www.hostaddon.com/budget-10gbps-metered-vps/) — our lowest entry point
  - [2] 2026-10-28: the 1 Gbps Budget NVMe NANO plan is USD 6.49 per month | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: | NANO | 2 | 2GB | 30GB | $6.49/mo | $4.87 first invoice |
  - [2] 2026-10-28: accepted payments are cards, PayPal and crypto, with no KYC for crypto | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: - Payments: cards, PayPal, BTC/ETH + other crypto. No KYC for crypto.
  - [2] 2026-10-28: orders using the forum coupon get manual fraud review | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: - Fraud screening: LET signups with code LET25 get manual review.
  - [2] 2026-10-28: the infrastructure is rented dedicated servers, leases and resale | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: - Infrastructure: Rented Dedis/Lease/Reselling.
  - [2] 2026-10-28: a buyer reports that a new account was refused with a fraud flag | capture: sha256:8a63c7f7d492527d480c8b52dc51a3915f3e5c1ac9783208bea5e7dcb988aa76 | quote: New users can't use the LET25 discount, registered accounts can't buy VPS, and payment shows fraud.
  - [3] 2026-10-28: the client area has no standalone sign-up; an account is created when an order is placed | capture: sha256:051bf5e1de845d4ea6ac86aefe2a600fe50d0dd7d1ccf0c99e49071573c8556d | quote: To create an account, please place an order with us
  - [4] 2026-10-28: the offers feed lists the same starting price of USD 3.99 per month | capture: sha256:a81634ee720527577633ad596d622494e62345d37e8729b0246a1522923386f6 | quote: [HostAddon VPS - 1/2/10Gbps | NVMe | From $3.99/mo | 25% Off | 30 Locales | Storage | Streaming | VPN]
- sources:
  - [1] https://www.hostaddon.com/budget-10gbps-metered-vps/
  - [2] https://lowendtalk.com/discussion/220041/hostaddon-vps-1-2-10gbps-nvme-from-3-99-mo-25-off-30-locales-storage-streaming-vpn
  - [3] https://www.hostaddon.com/clients/register.php
  - [4] https://lowendtalk.com/categories/offers
