# Raff Technologies

> rafftechnologies.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rafftechnologies/ | JSON https://fshy.ajam.dev/api/v1/entity/rafftechnologies.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Raff Technologies

- `compute/raff-technologies` | paid-only | evidence reported | binding per-object-cap | category cloud VM | tier General Purpose 1 vCPU / 1 GB
- needs card yes, phone yes, ID no, institution no | verified 2026-11-06T18:37:36.022Z (live) | stale on 2026-11-21
- url https://rafftechnologies.com/pricing
- free tier: no free tier; the cheapest plan is General Purpose 1 vCPU, 1 GB DDR5, 25 GB NVMe, 3 Gbps port, unmetered bandwidth, KVM, at USD 4.99 a month (USD 3.49 for the first month on a first server), USD 49.90 a year or USD 89.82 for 24 months; location Virginia, USA | unit: none | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: the next rung is Cost-Optimized 2 vCPU, 4 GB DDR4, 40 GB local NVMe, 1 Gbps at USD 9.99 a month; General Purpose 1 vCPU / 2 GB is USD 8.99 a month with 50 GB NVMe
- per-object cap: not applicable
- retention: not applicable: the unit is a machine, not stored bytes; billed in advance for a monthly, yearly or 24-month period | source: [2]
- egress: bandwidth is stated as unmetered on every plan, over a 3 Gbps port on General Purpose and a 1 Gbps port on Cost-Optimized | metered: no | free allowance: unmetered | source: [3]
- identity: card | detail: email address and password at signup; phone number verified by SMS before the first purchase ('Raff requires phone verification for security'); payment by card saved with the payment provider (USD 1.00 check charge credited to the account balance) or by a payment link when no card is saved; wire transfer and crypto through support; minimum age 18; no identity document named on the pages read
- interface: rest, cli, ssh
- limits:
  - per-object-cap (binding): 25 GB NVMe on the 1 vCPU / 1 GB plan, 50 GB on 1 vCPU / 2 GB [4]
  - per-ip-shaping: 3 Gbps port on General Purpose, 1 Gbps on Cost-Optimized [3]
- binding note: the 25 GB disk of the cheapest plan fills before bandwidth does, since bandwidth is unmetered
- interface detail: Raff API, CLI, Terraform provider and MCP server; browser terminal and SSH with root access
- tooling: Raff API, CLI and Terraform provider; 20+ OS templates; the page documents no third-party client
- composes with: one location, Virginia, so it adds a US-east vantage with free private networking between a customer's own Raff servers
- reliability: no outage or suspension event recorded; General Purpose carries a 99.9% SLA with 3x replicated NVMe, Cost-Optimized has local NVMe and no SLA
- notes: USD, billing terms monthly, yearly and 24 months. Cheapest plan USD 4.99 a month; USD 3.49 applies to the first month only. Whether tax is added at checkout is unverified. Each account may have one free managed database, which belongs to the databases-kv topic.
- evidence note: the 1 vCPU / 1 GB / 25 GB shape and the 3 Gbps port come from the provider's own offer post on a forum; the product page states the USD 4.99 price but its General Purpose plan table is not in the page text, so the shape has no first-party quote yet
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 25
  - free_tier_kind: none
  - location: Virginia, USA (us-east)
  - price.amount: 4.99
  - price.currency: USD
  - price.term: monthly
  - plans[0].plan: General Purpose 1 vCPU / 1 GB / 25 GB NVMe
  - plans[0].usd_month: 4.99
  - plans[0].usd_year: 49.9
  - plans[0].usd_24_months: 89.82
  - plans[1].plan: General Purpose 1 vCPU / 2 GB / 50 GB NVMe
  - plans[1].usd_month: 8.99
  - plans[1].usd_year: 89.9
  - plans[1].usd_24_months: 161.82
  - plans[2].plan: Cost-Optimized 2 vCPU / 4 GB / 40 GB NVMe
  - plans[2].usd_month: 9.99
  - plans[2].usd_year: 99.9
  - plans[2].usd_24_months: 179.82
- evidence:
  - [1] 2026-10-28: the provider's own product page states the entry price: USD 3.49 for the first month, then USD 4.99 a month | capture: sha256:db6dd9594c8d76a2bc6ab3c99a6a7e44543db8ca1765baad43cbe58c46938089 | quote: Plans start at $3.49 for your first month, then $4.99 a month, with no hidden fees.
  - [4] 2026-10-28: General Purpose Plan 1 is 1 vCPU, 1 GB DDR5, 25 GB NVMe, 3 Gbps, unmetered, KVM at USD 4.99 a month, USD 49.90 a year or USD 89.82 for 24 months (provider's offer post) | capture: sha256:dfd90aaf5d991fbddac81d741bf127ec94868bc35edc19198f5b6cc84c7cf234 | quote: 1 vCPU · 1 GB DDR5 · 25 GB NVMe · 3 Gbps · Unmetered · KVM - $4.99/month (first month $3.49) - $49.90/year - $89.82/24 months
  - [4] 2026-10-28: servers are in Virginia, USA | capture: sha256:dfd90aaf5d991fbddac81d741bf127ec94868bc35edc19198f5b6cc84c7cf234 | quote: Raff Technologies is a US-registered cloud company running AMD EPYC™ servers with NVMe storage in Virginia.
  - [4] 2026-10-28: General Purpose is shared vCPU on DDR5 with 3x replicated storage and a 99.9% SLA | capture: sha256:dfd90aaf5d991fbddac81d741bf127ec94868bc35edc19198f5b6cc84c7cf234 | quote: General Purpose — shared vCPU, DDR5, 3x replicated storage, 99.9% SLA
  - [3] 2026-10-28: the Cost-Optimized entry plan is 2 vCPU, 4 GB, 40 GB NVMe, unmetered, USD 9.99 a month billed monthly | capture: sha256:c24016c87455455161765730aabf3ec27d3e80bc5cfaf9c1ae5ab2d7131c1cc4 | quote: | 2 vCPU · 4 GB | 2 vCPU | 4 GB | 40 GB | Unmetered | $9.99/mo Billed monthly |
  - [3] 2026-10-28: Cost-Optimized is previous-generation hardware with local NVMe, a 1 Gbps port, and is not covered by the SLA | capture: sha256:c24016c87455455161765730aabf3ec27d3e80bc5cfaf9c1ae5ab2d7131c1cc4 | quote: Previous-generation hardware with local NVMe, a 1 Gbps public port and DDR4 memory, for budget needs. Linux and FreeBSD, not covered by the SLA.
  - [3] 2026-10-28: bandwidth on Cost-Optimized plans is stated as unlimited with no caps | capture: sha256:c24016c87455455161765730aabf3ec27d3e80bc5cfaf9c1ae5ab2d7131c1cc4 | quote: Unlimited, no caps, never billed
  - [5] 2026-10-28: the signup form takes an email address and a password and states that phone verification is required | capture: sha256:53e65ce577088e2f9ebd0bee26a3f24267b92633351b200994364e7ddef43d4d | quote: Raff requires phone verification for security. By accepting our terms you agree to receive verification and notification texts.
  - [2] 2026-10-28: the phone number is verified by SMS before the first purchase | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: We verify your phone number by SMS before your first purchase, through our provider Prelude.
  - [2] 2026-10-28: a saved card is checked with a USD 1.00 charge that is credited to the account balance | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: You can save a card with our payment provider. To check a new card we charge $1.00, which is added to your account balance.
  - [2] 2026-10-28: an account without a saved card is sent a payment link at renewal | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: Without a saved card, we send you a payment link.
  - [2] 2026-10-28: minimum account age is 18; no identity document is named | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: You must be at least 18 years old and able to enter into a binding contract.
  - [4] 2026-10-28: accepted payment: cards and wallets, with wire transfer and crypto through support | capture: sha256:dfd90aaf5d991fbddac81d741bf127ec94868bc35edc19198f5b6cc84c7cf234 | quote: Visa, Mastercard, Amex, Discover, UnionPay, Apple Pay, Google Pay. Wire transfer (USD, EUR, TRY) and crypto via support.
  - [2] 2026-10-28: the terms name an API, a CLI, a Terraform provider and an MCP server | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: the Raff API, CLI, Terraform provider and MCP server
  - [3] 2026-10-28: live console and SSH with full root access are included | capture: sha256:c24016c87455455161765730aabf3ec27d3e80bc5cfaf9c1ae5ab2d7131c1cc4 | quote: Browser terminal, full root access
  - [2] 2026-10-28: servers can be billed monthly, yearly or every 24 months | capture: sha256:b1c0b4cdf908fd99fe27dce286858e86dbc8472b52fe10775e174afe8ab8cf4e | quote: Servers, volumes, reserved IP addresses and Raff Keep stacks can be billed monthly, yearly or every 24 months.
- sources:
  - [1] https://rafftechnologies.com/products/raff-vm
  - [2] https://rafftechnologies.com/legal/terms-of-service
  - [3] https://rafftechnologies.com/pricing
  - [4] https://lowendtalk.com/discussion/222597/raff-technologies-kvm-vps-from-4-99-mo-managed-databases-amd-epyc-nvme-unmetered
  - [5] https://rafftechnologies.com/auth/sign-up
