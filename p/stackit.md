# STACKIT Compute Engine

> stackit.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stackit/ | JSON https://fshy.ajam.dev/api/v1/entity/stackit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## STACKIT Compute Engine

- `compute/stackit` | paid-only | evidence unverified | category cloud VM
- needs card yes, phone yes, ID no, institution yes | verified 2026-10-28T04:48:00.559Z (live) | stale on 2026-11-12
- url https://pim.api.stackit.cloud/v1/skus
- price parsed USD 36.95/mo
- free tier: none: Compute Engine is billed pay-as-you-go by the hour or month; no free tier or trial credit appears on the product page or in its price table | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1] | note: smallest listed server Tiny Server-t1.1-EU01 (1 vCPU) is EUR 0.00304791667 per hour in EU01; Marketplace Free Trials apply to Marketplace products and need a customer account with valid payment details
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: institution | detail: a customer account needs contact person name and phone number, company name and address, VAT ID, Commercial Register number and a payment method (invoice or credit card); self-service in Germany, Austria and Switzerland, other countries go through the sales contact form; a Marketplace free trial also needs valid payment details
- interface: rest
- interface detail: STACKIT portal (web UI) and the STACKIT IaaS API
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The SKU feed is machine-readable price data with no free-tier field. A session that wants to settle this record has to join the SKU rows to a product page, which is a different job from a re-read.
- evidence note: documented from the first-party product page, customer account guide and Marketplace FAQ; the SKU price feed lists no zero-priced Compute Engine row
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: allowance
  - m10h_usd: 14.78
  - m24h_usd: 36.95
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - granularity.min_billed_s: 3600
  - burst_x: 2.0
  - burst_bill: min 1 h
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: The firecrawl route returned 820,875 bytes of JSON, which carries SKU rows but not a free-tier statement, so the free-tier claim is still unsettled
  - [2] 2026-10-28: Compute Engine is pay-as-you-go with no free allowance listed | capture: sha256:6507f9c11d87e3b1eb12842f42e66b002104bd29508702142303dc1f680d1b39 | quote: Transparent and cost-effective: you only pay for the systems that use or reserve the corresponding resources (pay-as-you-go).
  - [2] 2026-10-28: the smallest listed server is priced hourly at EUR 0.00304791667 | capture: sha256:6507f9c11d87e3b1eb12842f42e66b002104bd29508702142303dc1f680d1b39 | quote: | Tiny Server-t1.1-EU01 | 1 | 0 | Hourly | 0.00304791667 € |
  - [3] 2026-10-28: a customer account needs the company VAT ID and Commercial Register number | capture: sha256:b90f4227ce80294a4c5316edc3cc7162aacbda73290f4a3fb5e9879a21da3816 | quote: 4. Provide the company’s VAT ID and Commercial Register number.
  - [3] 2026-10-28: registration requires choosing a payment method, invoice or credit card | capture: sha256:b90f4227ce80294a4c5316edc3cc7162aacbda73290f4a3fb5e9879a21da3816 | quote: 5. Choose a payment method. Currently, STACKIT offers payments via invoice and credit card.
  - [2] 2026-10-28: VMs are automatable through the STACKIT IaaS API | capture: sha256:6507f9c11d87e3b1eb12842f42e66b002104bd29508702142303dc1f680d1b39 | quote: With the STACKIT IaaS API, system deployments can be automated and reproduced.
  - [4] 2026-10-28: free trials need a customer account with valid payment details | capture: sha256:195e3519842ab48d0481e3392eb09be26d89d38efb4c8d8e0e0ecbc976354dcf | quote: Yes, you must have an active STACKIT customer account with valid payment details to start a free trial.
  - [2] 2026-10-28: usage is billed on the systems used or reserved, hourly or monthly, unchanged | capture: sha256:6507f9c11d87e3b1eb12842f42e66b002104bd29508702142303dc1f680d1b39 | quote: Transparent and cost-effective: you only pay for the systems that use or reserve the corresponding resources (pay-as-you-go).
- sources:
  - [1] https://pim.api.stackit.cloud/v1/skus
  - [2] https://stackit.com/en/products/compute-engine/stackit-compute-engine
  - [3] https://docs.stackit.cloud/platform/customer-accounts/how-tos/create-a-customer-account/
  - [4] https://docs.stackit.cloud/marketplace/faq/
