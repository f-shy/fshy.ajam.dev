# Oblivus

> oblivus.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oblivus/ | JSON https://fshy.ajam.dev/api/v1/entity/oblivus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Oblivus

- `compute/oblivus` | paid-only | evidence documented | binding none | category GPU cloud
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://www.oblivus.com/pricing/
- free tier: no free GPU tier is published; on-demand rates per GPU-hour on the pricing page read on 2026-11-03: H200 141GB SXM5 USD 3.99, H100 80GB SXM5 USD 4.312, H100 80GB NVLINK USD 3.64, H100 80GB PCIE USD 3.5, A100 80GB NVLINK USD 1.57, A100 80GB PCIE USD 1.47, L40 USD 1.05, RTX 4090 USD 0.64, RTX A6000 USD 0.55. The page lists no L40S and no L4. Reservations are published beside each rate, from USD 2.919 (H100 80GB SXM5), USD 0.95 (A100 80GB PCIE) and USD 0.44 (RTX 4090). Per-minute billing; a top-up of at least USD 5 funds the balance. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: the listed prices are all-in: vCPU, RAM and storage are included in the instance price
- per-object cap: not applicable | source: [1] | note: the ceiling is the instance shape listed beside each GPU, for example 24 vCPU, 225GB RAM and 4013GB NVMe for the H100 80GB SXM5
- retention: not applicable | source: [1] | note: a machine record: storage is billed according to its state when an instance is not running
- egress: Data egress per GB is listed as FREE and data ingress per GB as FREE | metered: no | free allowance: unmetered | source: [1]
- identity: email | detail: The sign-up asks for first name, last name, email address, password and country, a terms checkbox and a robot verification, then an email verification link. Balance top-ups start at USD 5 and the payment step is a redirect to Revolut or Binance; no phone or ID document is stated on the pages read. Whether the payment step needs a card is unverified: behind a sign-up.
- interface: rest
- limits note: No quota is stated: the page publishes per-GPU hourly rates and instance shapes. The prepaid balance, topped up from USD 5, is what binds.
- binding note: the same as limits note
- interface detail: inferred from the documentation index, which links an API documentation page; not probed
- tooling: web console and an API documented at docs.oblivus.com/api/documentation; Ubuntu 22.04-based OblivusAI images preloaded with machine-learning tools
- composes with: Published on-demand single-GPU rates for H100 80GB PCIE, A100 80GB PCIE and RTX 4090 with free egress make it a price comparison point for hosted GPU rentals; multi-tenant capacity is in Montreal and Oslo.
- reliability: The documentation pages read on 2026-11-03 are marked 'Last updated 1 year ago'; multi-tenant capacity is limited to two sites (Montreal, Canada and Oslo, Norway); H200 is by reservation request and GH200 by waitlist per the aggregator profile. No outage was observed.
- notes: Found via computeprices.com (provider slug oblivus). Legal entity on the index profile: Skyportal Inc. The aggregator shows the same H100 SXM at USD 4.31, A100 PCIe 80GB at USD 1.47 and RTX 4090 at USD 0.640, matching the provider page. Not read: whether the top-up page accepts a card.
- evidence:
  - [1] 2026-11-03: on-demand rate of the H100 80GB SXM5 card is USD 4.312 an hour | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: H100 80GB SXM5 On-Demand: $4.312/hr
  - [1] 2026-11-03: on-demand rate of the H100 80GB PCIE card is USD 3.5 an hour | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: H100 80GB PCIE On-Demand: $3.5/hr
  - [1] 2026-11-03: on-demand rate of the A100 80GB PCIE card is USD 1.47 an hour | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: A100 80GB PCIE On-Demand: $1.47/hr
  - [1] 2026-11-03: the page lists an L40 at USD 1.05 an hour and no L40S | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: L40 On-Demand: $1.05/hr
  - [1] 2026-11-03: on-demand rate of the RTX 4090 card is USD 0.64 an hour | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: RTX 4090 On-Demand: $0.64/hr
  - [1] 2026-11-03: data egress is listed free | capture: sha256:94a5716e520c785e8d1d4666b3220d20d2622d3f6ff8c5ce6536d6cc0d404c4f | quote: Data Egress (per GB) FREE
  - [2] 2026-11-03: sign-up fields are name, email and password, then country, terms and a robot check | capture: sha256:15cf19d05770405afda323bac50ad9e45b84c381b73d9b1f02f82b949aacfc9e | quote: You can sign up by entering your first name, last name, email address, and password.
  - [3] 2026-11-03: the minimum balance top-up is USD 5 | capture: sha256:adf8c3cdf3e047ccc387345c11ed21ad9dc15f30cdc109bf7ce1df880acdb4d3 | quote: which should be a minimum of $5
  - [3] 2026-11-03: top-up payment goes through Revolut or Binance | capture: sha256:adf8c3cdf3e047ccc387345c11ed21ad9dc15f30cdc109bf7ce1df880acdb4d3 | quote: redirected to the necessary steps for payment using Revolut or Binance
  - [4] 2026-11-03: listed on the computeprices index with 7 GPU models | capture: sha256:a67be04804b1ba0f7fb50613575535310eff6e57b96dab390be3b3a98a4056ee | quote: Oblivus is under the market median on 1 of its 7 GPUs today.
- sources:
  - [1] https://www.oblivus.com/pricing/
  - [2] https://docs.oblivus.com/getting-started/
  - [3] https://docs.oblivus.com/billing/billing-system/
  - [4] https://computeprices.com/providers/oblivus
