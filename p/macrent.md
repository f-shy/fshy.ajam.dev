# MacRent

> macrent.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/macrent/ | JSON https://fshy.ajam.dev/api/v1/entity/macrent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MacRent

- `compute/macrent` | paid-only | evidence documented | binding volume-quota | category rented Mac | tier Monthly dedicated Mac mini M4
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.878Z (live) | stale on 2026-12-26
- url https://www.macrent.cloud/rent-a-mac
- free tier: no free tier: a dedicated Mac mini M4 is sold at USD 15/day, USD 89/week or USD 159/month, and access is granted after successful payment; all three plan cards showed sold out on 2026-11-25 | unit: none | metered on: none | read on: 2026-11-25 | source: [1] | note: none-published
- per-object cap: not applicable: the unit is a whole dedicated machine, not an object | source: [1]
- retention: the machine is wiped when a rental ends or is cancelled and data is not recoverable afterwards; a 24-hour daily rental that is not renewed ends with the machine and all its data permanently deleted | source: [2]
- egress: a 1Gb/s internet connection and a static IP are included; no transfer allowance or egress price is published | metered: no | source: [1]
- identity: card | detail: access is granted after successful payment, prices are processed via Stripe, and the login asks for the email used at checkout to receive a secure link; the terms say the operator may require verification of identity or intended use at any time
- interface: ssh
- limits:
  - volume-quota (binding): a minimum rental of 24 hours under Apple's macOS Software License Agreement; no shorter rental is available and cancelling inside the first 24 hours does not shorten or refund that period [2]
- limits note: no monthly compute hours are included: every plan is a paid rental that renews until cancelled; all shown plan cards were sold out on 2026-11-25.
- binding note: the 24-hour minimum and the absence of any included free hours bind first: the cheapest entry is a non-refundable 24-hour paid rental, and no machine was in stock on 2026-11-25.
- interface detail: a remote desktop connection or SSH to a dedicated bare-metal Mac mini M4 with full-admin access and a static IP; no API is documented
- tooling: a remote desktop client or an SSH client; the machine can be registered as a self-hosted GitHub Actions, GitLab or Buildkite runner
- composes with: a whole dedicated Mac with full admin can serve as a permanent macOS build box for Xcode, signing and notarization, or as a self-hosted CI runner; it composes with any CI that accepts a self-hosted runner, but no free allowance exists and no machine was in stock on 2026-11-25, so it cannot be started without a paid order and available stock.
- reliability: no uptime guarantee; the machines are hosted by third-party infrastructure providers, and all plans showed sold out on 2026-11-25, so delivery depends on stock.
- notes: A hosted dedicated Mac, not an iOS Simulator-only rental: the whole machine is delivered with full admin over remote desktop or SSH, at USD 159/month for the monthly tier (USD 0.218/hour at 730 hours). No free tier is published. Every plan card read on 2026-11-25 was sold out. The USD 0.218/hour figure is the listed USD 159/month divided by 730 hours.
- evidence note: prices, hardware, access method and egress speed are quoted from the vendor's own rent-a-mac and mac-mini-cloud pages read on 2026-11-25; the 24-hour minimum, Stripe payment, wipe-on-end and identity-verification clause are quoted from the vendor's terms; the login email gate is quoted from the vendor's login page.
- extras:
  - shape.vcpu: 10-core CPU and GPU
  - shape.ram_gib: 16
  - shape.disk_gib: 256
  - shape.gpu_class: Apple M4
  - shape.note: a dedicated bare-metal Mac mini M4, macOS 26 or 27, static IP, 1Gb/s network
  - billing_model: paid daily, weekly or monthly rental with automatic renewal; a 24-hour minimum applies
  - free_tier_kind: none-published
  - term: 24-hour minimum; weekly and monthly renew until cancelled
  - price_arithmetic: USD 159/month ÷ 730 hours = USD 0.218/hour; USD 15/day is the daily plan price
  - status: sold out on all plans on 2026-11-25
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: full-admin, remote desktop and SSH to a static IP
  - network_out.static_ip: yes
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: a 24-hour minimum under Apple's macOS license; monthly plans renew until cancelled
- evidence:
  - [1] 2026-11-25: the daily plan costs USD 15 for 24 hours of access | capture: sha256:7f4e985dfd5db7c80ccd47c7f8049589228dc3545b56fdbd11e84f36384054b3 | quote: ### Daily $15/day 24 hours of access You choose: 24 hours only or renew daily
  - [1] 2026-11-25: the weekly plan is USD 89 and the monthly plan is USD 159 | capture: sha256:7f4e985dfd5db7c80ccd47c7f8049589228dc3545b56fdbd11e84f36384054b3 | quote: ### Weekly $89/week 7 days of access only $12.71 per day
  - [1] 2026-11-25: the monthly plan is sold out and the next machine is not available | capture: sha256:7f4e985dfd5db7c80ccd47c7f8049589228dc3545b56fdbd11e84f36384054b3 | quote: Sold out. Join the list and we email you when one frees up.
  - [3] 2026-11-25: the rental includes a dedicated Mac with full-admin access | capture: sha256:5d95da6a269b66e15f4df64a5c792f8c69803413596c693b08d1f4b2cd871557 | quote: You get a dedicated Mac with full-admin access - no one else has access to the machine
  - [3] 2026-11-25: the headline plans are USD 15 a day, USD 89 a week or USD 159 a month with 16GB RAM, 256GB SSD, static IP and full-admin access | capture: sha256:5d95da6a269b66e15f4df64a5c792f8c69803413596c693b08d1f4b2cd871557 | quote: Plans start at $15/day, $89/week, or $159/month. Every plan includes a dedicated Mac Mini M4 with 16GB RAM, 256GB SSD, a static IP and full-admin access.
  - [2] 2026-11-25: payment through Stripe is required before access | capture: sha256:3ddb9eb6f9e0c802d0f3bd4df8671fe675c4e761395030c88576f0fd24f98993 | quote: Prices are listed in USD unless stated otherwise and are processed via Stripe. Access is granted after successful payment.
  - [2] 2026-11-25: a 24-hour minimum applies to every rental under Apple's macOS Software License Agreement | capture: sha256:3ddb9eb6f9e0c802d0f3bd4df8671fe675c4e761395030c88576f0fd24f98993 | quote: Apple's macOS Software License Agreement requires that Mac computers be leased for a minimum period of 24 hours. Every rental therefore has a minimum duration of 24 hours.
  - [4] 2026-11-25: login uses the email address from checkout and delivers a secure link | capture: sha256:7e0f3354c5c9bf691238bb654aadc8655c67d5d9ae5aa58ed82282744b5d7390 | quote: Enter the email you used at checkout and we'll send you a secure link to your connection details.
  - [1] 2026-11-24: the Daily plan is USD 15 for 24 hours of access | capture: sha256:6410474f64af785e7802dac601ad8983940f9f4709b1f3d78a5fb2f36d0f8538 | quote: $15/day 24 hours of access
  - [1] 2026-11-24: each plan is a dedicated Mac Mini M4 or M6 | capture: sha256:6410474f64af785e7802dac601ad8983940f9f4709b1f3d78a5fb2f36d0f8538 | quote: Every plan is a dedicated Mac Mini M4 or M6. Pay only for what you need, cancel anytime.
  - [1] 2026-11-24: remote desktop is a connection method | capture: sha256:6410474f64af785e7802dac601ad8983940f9f4709b1f3d78a5fb2f36d0f8538 | quote: Remote desktop connection
  - [1] 2026-11-24: SSH is included on the plan | capture: sha256:6410474f64af785e7802dac601ad8983940f9f4709b1f3d78a5fb2f36d0f8538 | quote: SSH access
  - [1] 2026-11-24: the machine has a 1Gb/s internet connection | capture: sha256:6410474f64af785e7802dac601ad8983940f9f4709b1f3d78a5fb2f36d0f8538 | quote: 1Gb/s internet speed
  - [4] 2026-11-24: the email address used at checkout receives the connection link | capture: sha256:7e0f3354c5c9bf691238bb654aadc8655c67d5d9ae5aa58ed82282744b5d7390 | quote: Enter the email you used at checkout and we'll send you a secure link to your connection details.
  - [2] 2026-11-24: access requires successful payment through Stripe | capture: sha256:3ddb9eb6f9e0c802d0f3bd4df8671fe675c4e761395030c88576f0fd24f98993 | quote: Prices are listed in USD unless stated otherwise and are processed via Stripe. Access is granted after successful payment.
  - [2] 2026-11-24: Apple's license requires a minimum 24-hour lease | capture: sha256:3ddb9eb6f9e0c802d0f3bd4df8671fe675c4e761395030c88576f0fd24f98993 | quote: Apple's macOS Software License Agreement requires that Mac computers be leased for a minimum period of 24 hours. Every rental therefore has a minimum duration of 24 hours.
  - [2] 2026-11-24: data on the machine is wiped at the end of the rental | capture: sha256:3ddb9eb6f9e0c802d0f3bd4df8671fe675c4e761395030c88576f0fd24f98993 | quote: Machines are wiped when a rental ends, is cancelled, or is terminated, and data is not recoverable afterwards.
- sources:
  - [1] https://www.macrent.cloud/rent-a-mac
  - [2] https://www.macrent.cloud/terms
  - [3] https://www.macrent.cloud/
  - [4] https://www.macrent.cloud/login
