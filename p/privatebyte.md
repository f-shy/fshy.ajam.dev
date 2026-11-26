# PrivateByte

> privatebyte.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privatebyte/ | JSON https://fshy.ajam.dev/api/v1/entity/privatebyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PrivateByte

- `compute/privatebyte` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T17:40:53.066Z (live) | stale on 2026-12-08
- url https://privatebyte.com/
- price parsed USD 5.99/mo
- free tier: USD 5.99/month for Flare: 1 vCPU, 2 GB RAM, 25 GB SSD, a 100 Mbps port, unmetered traffic, a dedicated IPv4, daily backups with 7-day retention, DDoS protection and full root. Orbit is USD 7.99/month for 2 vCPU, 4 GB (GB is the unit the page prints), 50 GB and a 250 Mbps port; Comet is USD 15.99 for 4 vCPU, 8 GB, 100 GB and 500 Mbps; Pulsar is USD 27.99 for 6 vCPU, 16 GB, 200 GB and 1 Gbps. Unmetered traffic on every plan, monthly billing, no setup fee, and the page says six plans exist against the four it lists. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unmetered traffic on every plan; the port speed is the only stated limit and it rises with the plan | metered: no | free allowance: unmetered at 100 Mbps on Flare | source: [1]
- identity: email | detail: registration requires an email address and a password, with Google and GitHub sign-in offered; no phone or card (read 2026-11-07)
- interface: ssh, rest, cli
- limits:
  - per-ip-shaping (binding): unmetered traffic on every plan, so the port is the wall and it climbs with the price: 100 Mbps on Flare, 250 Mbps on Orbit, 500 Mbps on Comet and 1 Gbps on Pulsar. A 100 Mbps port sustained is about 32 TB a month, which is the largest effective monthly allowance among documented hosts even though no byte counter exists. [1]
- limits note: unmetered traffic on every plan, so the port is the wall and it climbs with the price: 100 Mbps on Flare, 250 Mbps on Orbit, 500 Mbps on Comet and 1 Gbps on Pulsar. A 100 Mbps port sustained is about 32 TB a month, which is the largest effective monthly allowance among documented hosts even though no byte counter exists.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor advertises an order-configure endpoint per plan at my.privatebyte.com/order/configure/<plan>, SSH and console access, daily backups and snapshots; no API or CLI is documented on the page read
- composes with: USD 5.99 for 2 GB with unmetered traffic on a 100 Mbps port is the cheapest unmetered row among documented hosts, and 100 Mbps sustained is a larger monthly byte budget than any metered plan here states; that makes it the record to test first when the job is serving rather than storing, and the three locations give a European and a US point on one invoice
- reliability: no reliability event recorded
- notes: The vendor table prints '4 GB' and '8 GB' under a column headed 'Memory' while the record's shape field is in GiB; the numbers are carried as printed and no conversion was made. The page says 'Explore all six plans' and lists four, so two plans exist that this record does not price. Unverified: those two plans, and whether LET25 stacks with the listed price or only applies at checkout.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 25
  - monthly_price: USD 5.99 per month for Flare (1 vCPU / 2 GB / 25 GB SSD / 100 Mbps), no setup fee; the order page's summary totals USD 5.99 due today at the monthly cycle
  - annual_price: USD 4.79 per month on the annual term, printed as 'USD 57.50 billed yearly · Save 20%'
  - renewal_price: not published: no page read prints a renewal price; the order page states 'cancel any time'
  - billing_term: monthly or annual: the order page offers exactly two cycles, Monthly at USD 5.99 and Annually at USD 4.79/mo (USD 57.50 billed yearly)
  - stock: in stock: the order page renders the full configurator with payment options (Card, PayPal, Crypto, Add to cart)
  - cart_price: USD 5.99 per month due today at the monthly cycle, from the order page's cart summary (FLARE · monthly, 1 vCPU · 2 GB · 25 GB · Unmetered · 100 Mbps)
  - price_on_page: USD 5.99/month for Flare
  - renewal_usd: not published: the order page names no renewal figure and states the plan can be cancelled
- evidence:
  - [1] 2026-10-22: vendor plan table quoted row by row: 'Flare ... 1 ... 2 GB ... 25 GB ... 100 Mbps ... $5.99/mo'; 'Orbit ... 2 ... 4 GB ... 50 GB ... 250 Mbps ... $7.99/mo'; 'Comet ... 4 ... 8 GB ... 100 GB ... 500 Mbps ... $15.99/mo'; 'Pulsar ... 6 ... 16 GB ... 200 GB ... 1 Gbps ... $27.99/mo'; below the table: 'Unmetered traffic on every plan'; page description: 'Unmetered traffic, full root access and a dedicated IPv4 from $5.99 a month'
  - [2] 2026-10-22: the offer thread, posted October 7, 2026, titles the offer 'PrivateByte | KVM VPS from $5.99/mo | 2-4GB Unmetered | London, Amsterdam, Dallas | 25% off: LET25', naming the three locations and a discount code the vendor page does not carry
  - [3] 2026-11-07: the order page's cart summary totals USD 5.99 due today | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: Total today $5.99/month
  - [3] 2026-11-07: the order page prices the annual cycle USD 57.50 billed yearly, 4.79 per month | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: Annually $4.79/mo $57.50 billed yearly · Save 20%
  - [3] 2026-11-07: the order page names no renewal figure and states the plan can be cancelled | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: cancel any time
  - [3] 2026-11-07: the order page prints the two billing cycles and their prices | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: Monthly $5.99 Annually $4.79/mo $57.50 billed yearly · Save 20%
  - [3] 2026-11-07: the order page offers the payment paths; no out-of-stock marker | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: Pay with Card Pay with PayPal Pay with Crypto Add to cart instead
  - [3] 2026-11-07: the cart summary names the plan, its cycle and its shape | capture: sha256:a014405d895872d2e65e5348378b9e38c985fa85e81aaad7ee626a84d0a8cae3 | quote: FLARE · monthly 1 vCPU · 2 GB · 25 GB · Unmetered · 100 Mbps
  - [4] 2026-11-07: the register form's required fields | capture: sha256:4707885b7cb98ef6abfb82f3f8aadea3fc51cbe3786f3fe7630c4dc054410094 | quote: or continue with email Email Password
  - [1] 2026-11-07: the entry plan's price and term are unchanged on 2026-11-07 | capture: sha256:c52f30c98dbe6bf3c4d0f9ec20fe5d24c1f8e6ede8c74eb097b610bb384a3ae1 | quote: $5.99/ month Billed monthly. No setup fee.
  - [1] 2026-11-07: the vendor's own marketing page prices the entry plan at USD 5.99 a month | capture: sha256:c52f30c98dbe6bf3c4d0f9ec20fe5d24c1f8e6ede8c74eb097b610bb384a3ae1 | quote: $5.99/ month Billed monthly. No setup fee.
- sources:
  - [1] https://privatebyte.com/
  - [2] https://lowendtalk.com/discussion/221826/privatebyte-kvm-vps-from-5-99-mo-2-4gb-unmetered-london-amsterdam-dallas-25-off-let25
  - [3] https://my.privatebyte.com/order/configure/flare
  - [4] https://my.privatebyte.com/register
