# Roundfleet

> roundfleet.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/roundfleet/ | JSON https://fshy.ajam.dev/api/v1/entity/roundfleet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Roundfleet

- `compute/roundfleet` | paid-only | evidence documented | binding volume-quota | category rented Mac (bare metal) | tier Mac Mini M4, 16 GB / 256 GB, monthly
- identity a placeholder: card and phone unknown | verified 2026-11-25T02:12:34.858Z (live) | stale on 2026-12-26
- url https://www.roundfleet.com/pricing
- free tier: No free tier is published: the Mac Mini M4 with 16 GB RAM and 256 GB SSD is $99.00 per month before tax, with an hourly rate of $0.14 shown but a one-month minimum allocation. Free credits are offered only in exchange for a G2 review after subscribing to a plan. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The provider list's $0.14 an hour is the hourly rate printed on the pricing page; the $99 a month divided by 730 hours is $0.136 an hour. The M4 Pro is $199 a month and an M6 at $215 a month is marked Soon.
- per-object cap: not applicable: the unit is a dedicated Mac Mini, not an object; the base configuration has a 256 GB SSD with optional 1 TB or 2 TB storage | source: [1]
- retention: unverified: no data retention or deletion term for a released machine was stated on the pages read | source: [1]
- egress: 10 Gbps on all plans with a dedicated IPv4 address; the homepage says high bandwidth bursting to 1 GB/second. No data cap, free allowance or overage price is stated on the pages read. | metered: no | source: [2]
- identity: email | detail: unverified: the signup form was not read, so email is the assumed kind because an account is needed; the features page says 'Create your account and choose the subscription that fits your needs' and links to a contact form, and no registration form or payment rail was reachable on the pages read. Whether a phone number, card or identity document is asked for is unverified: behind a sign-up. The contact route asks the user to get in touch with the team.
- interface: ssh, browser
- limits:
  - volume-quota (binding): $99.00 a month for the base M4; an hourly rate of $0.14 is shown but the minimum allocation is one month [1]
- limits note: storage options are 1 TB for +$17 a month with a $10 setup fee and 2 TB for +$28 a month with an $8 setup fee; the M6 tier is listed as Soon with first units on 22 September 2026.
- binding note: the one-month minimum at $99 is the first limit a caller meets despite an hourly rate being printed; no request-rate or byte quota is stated.
- interface detail: remote control with VNC and SSH, plus a native Roundfleet Desktop Client for macOS, Windows and Linux; a support ticketing system is at app.roundfleet.com
- tooling: an SSH client, a VNC viewer or the Roundfleet desktop client; the user installs and runs CI runner agents on the rented Mac. The Mac itself is the hosted offer.
- composes with: the dedicated Apple silicon Mac runs GitHub Actions, GitLab CI or other runners and MLX-based model work, reached over SSH or VNC from any client; the one-month minimum makes it unsuitable for a short single job.
- reliability: unverified: no status page, uptime history or throttle policy was read; the pricing page marks the M6 tier as Soon with first units on 22 September 2026.
- notes: No free tier: the base Mac Mini M4 is USD 99 a month with a one-month minimum; the provider list's USD 0.14 an hour is the hourly rate printed beside it, and USD 99 divided by 730 hours is USD 0.136 an hour. The M6 tier is marked Soon and the identity gate was not readable.
- evidence note: prices, storage options, access methods and the M6 status are quoted from first-party pages read on 2026-11-25; the identity requirement was not on a page that could be read, so it stays unverified.
- extras:
  - shape.ram_gib: 16
  - shape.disk_gib: 256
  - shape.gpu_class: Apple M4, 10-core CPU and 10-core GPU
  - shape.note: dedicated bare-metal Mac Mini M4; 10 Gbps network and dedicated IPv4
  - billing_model: monthly with one-month minimum; hourly rate shown
  - free_tier_kind: none
  - price_arithmetic: USD 99 / 730 hours = USD 0.136 an hour; printed hourly rate USD 0.14
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: VNC and SSH; port numbers not stated
  - network_out.static_ip: dedicated IPv4 included
  - session_cap.restart_required: no
  - session_cap.note: one-month minimum allocation; cancel anytime after it
- evidence:
  - [1] 2026-11-25: the base Mac Mini M4 is USD 99 a month with an hourly rate of USD 0.14 | capture: sha256:c6bcf45fd2797d7836e80436ca9b8122077add3a869054da5eeda327ea055118 | quote: $99.00Hourly rate: $0.14
  - [1] 2026-11-25: the M6 tier at USD 215 a month is marked Soon with first units on 22 September 2026 | capture: sha256:c6bcf45fd2797d7836e80436ca9b8122077add3a869054da5eeda327ea055118 | quote: Mac Mini M6 on Roundfleet from €200/month. First units 22 September 2026.
  - [2] 2026-11-25: the Macs are reachable with VNC and SSH and run on Apple silicon without emulation | capture: sha256:8e3bc5bfea694cb5ea317e7a2b11ceb6fabe948554f18b4126f63f72c056cb7c | quote: Latest Apple OS (Sonoma or Sequoia). Remote control with VNC + SSH offered.
  - [3] 2026-11-25: getting started requires creating an account and choosing a subscription | capture: sha256:428924a1a528026168d7d0782d03871ebb46d31831aeb91c47ebddbc4bdfd163 | quote: Create your account and choose the subscription that fits your needs.
  - [4] 2026-11-25: the machines are bare metal M4 and M4 Pro Mac Minis in a Toulouse data center with VNC and SSH access | capture: sha256:04ef64538aede26f9766b3a5c2db0e95a424ddf2343f4919a2f68f0f5b24b942 | quote: Roundfleet offers bare metal Apple silicon servers (M4 and M4 Pro) accessible remotely via VNC and SSH. Our datacenter is located in Toulouse, France.
  - [1] 2026-11-24: the cheapest Mac Mini M4 plan is $99.00 per month or $0.14 hourly with 16 GB RAM and 256 GB SSD | capture: sha256:c6bcf45fd2797d7836e80436ca9b8122077add3a869054da5eeda327ea055118 | quote: $99.00Hourly rate: $0.14
  - [1] 2026-11-24: the M4 Pro is $199.00 a month and the M6 $215.00 a month but marked Soon | capture: sha256:c6bcf45fd2797d7836e80436ca9b8122077add3a869054da5eeda327ea055118 | quote: $215.00Hourly rate: $0.30
  - [2] 2026-11-24: the machines are reached with VNC and SSH | capture: sha256:8e3bc5bfea694cb5ea317e7a2b11ceb6fabe948554f18b4126f63f72c056cb7c | quote: Latest Apple OS (Sonoma or Sequoia). Remote control with VNC + SSH offered.
  - [2] 2026-11-24: the published network claim is burst bandwidth to 1 GB/second with a fixed IPv4 address | capture: sha256:8e3bc5bfea694cb5ea317e7a2b11ceb6fabe948554f18b4126f63f72c056cb7c | quote: High bandwidth bursting to 1 GB/second. Fixed IP Address with IPv4 support.
  - [5] 2026-11-24: registration asks the user to select a paid or free Plan and supplies an email address | capture: sha256:f0d0630b6c7e40bde2084e713ff3fa6a35d37a03e92e19a984c93d6e24710199 | quote: During the registration process, you will be asked to select a package to access the Services
  - [5] 2026-11-24: canceled content is deleted and cannot be recovered | capture: sha256:f0d0630b6c7e40bde2084e713ff3fa6a35d37a03e92e19a984c93d6e24710199 | quote: All of your Content will be deleted from the Services within a reasonable time period from when you cancel your account/pricing. Deleted Content cannot be recovered once your account/pricing is cancelled.
  - [3] 2026-11-24: free credits are gated behind subscribing to a paid plan and writing a review | capture: sha256:428924a1a528026168d7d0782d03871ebb46d31831aeb91c47ebddbc4bdfd163 | quote: Subscribe to any plan first before submitting your review.
- sources:
  - [1] https://www.roundfleet.com/pricing
  - [2] https://www.roundfleet.com/
  - [3] https://www.roundfleet.com/features
  - [4] https://www.roundfleet.com/llms.txt
  - [5] https://www.roundfleet.com/terms
