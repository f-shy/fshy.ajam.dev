# Savannaa

> savannaa.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/savannaa/ | JSON https://fshy.ajam.dev/api/v1/entity/savannaa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Savannaa

- `compute/savannaa` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.savannaa.com/pricing/free-tier
- free tier: 750 hours a month of a t2.micro (1 vCPU, 1 GiB RAM, 10 GB SSD) or t3.micro (2 vCPU, 1 GiB RAM, 10 GB SSD) free for the first 12 months in Lagos and Abuja, hours pooled across both types and regions, plus NGN 10,000 of trial credit with no expiry and no payment method needed to start. Egress is not charged until 2026-12-31; from 2027-01-01 the account gets 5 TB a month included, then NGN 15.00 per GB. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: time-boxed-hourly
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Egress not charged until 31 Dec 2026; from 1 Jan 2027: 5 TB / month included, then NGN 15.00/GB', and the Pro plan at 'NGN 25,000.00 / month' for 20 vCPU and 80 GB RAM total, quoted | metered: no | source: [2]
- identity: email | detail: a valid email address for account verification: the docs state signup needs only 'a valid, accessible email address for account verification'. The onboarding wizard additionally asks an organisation name and a mobile number from Nigeria, Ghana, Kenya or South Africa for recovery, and states 'No payment method is needed to start' with the payment method 'optional during trial'. No card, no hold, no national ID. Debit and prepaid acceptance are not stated.
- interface: rest
- limits:
  - volume-quota (binding): The 750 free hours cover compute only: the rate card bills public IPs at NGN 4,360 a month and the free tier page excludes volumes, public IPs and egress, so a reachable instance costs about NGN 4,360 a month even while the compute is free. [1]
- limits note: The 750 free hours cover compute only: the rate card bills public IPs at NGN 4,360 a month and the free tier page excludes volumes, public IPs and egress, so a reachable instance costs about NGN 4,360 a month even while the compute is free.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The free 750 hours on a Nigerian cloud with free egress until the end of 2026 composes with a global free tier: the micro instance holds state and serves traffic in Africa at zero egress while a hyperscaler free tier does the compute.
- reliability: no reliability event recorded
- notes: This is the closest thing found to an unlisted regional equivalent of the AWS micro free tier, and it is absent from every English roundup checked. The identity gate is unusually light for a regional provider: an email plus a phone number from one of four African countries for recovery, with no card and no national ID stated on the signup page. Two caveats: the hour pool is 12 months only, and the free tier page says 'Always free: Not offered yet', so the operator is explicit that this is introductory. The NGN 10,000 credit converts to roughly USD 7.5 at the published rate of NGN 1,327.24 per USD, which the vendor itself states is an estimate and not a price. The rate card lets the allowance be priced exactly: t2.micro is listed at NGN 32,438.35 a month, so the 750 free hours are about NGN 389,000 of compute across the twelve months, before the pooled egress allowance. That is a small number in absolute terms and a complete one: an always-on micro instance in Lagos for a year at zero cost, from a provider that appears in no English roundup checked. The exclusion that decides the verdict is the public IP: the free hours are compute hours, and a reachable server also needs an address billed at NGN 4,360 a month. That is a small sum, and it is the difference between a free tier and a free tier that works. The one recorded is the better-evidenced.
- extras:
  - facets.class: regional-free-tier
  - facets.free_tier_kind: time-boxed-hourly
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: '750 hours a month of t2.micro (1 vCPU, 1 GiB RAM, 10 GB SSD) or t3.micro (2 vCPU, 1 GiB RAM, 10 GB SSD) free for your first 12 months, in Lagos and Abuja', 'Hours are pooled across both types and regions', 'New accounts get NGN 10,000.00 of credit ... It does not expire', 'Always free: Not offered yet', quoted; probed 200, 948 bytes, sha256 e81375bc8fe527d5608d54318393f30ea6a0e769c528c303088b6411ca57a7ac
  - [2] 2026-10-22: 'Egress not charged until 31 Dec 2026; from 1 Jan 2027: 5 TB / month included, then NGN 15.00/GB', and the Pro plan at 'NGN 25,000.00 / month' for 20 vCPU and 80 GB RAM total, quoted
  - [3] 2026-10-22: signup needs only 'a valid, accessible email address for account verification'; the onboarding wizard asks an organisation name and a mobile number from Nigeria, Ghana, Kenya or South Africa for recovery, and states 'No payment method is needed to start' with the payment method 'optional during trial', quoted
  - [4] 2026-10-22: the rate card prices the same instance the free tier gives away: 't2.micro | 1 | 1 GB | 10 GB | NGN 32,438.35', so 750 free hours a month is worth about NGN 32,438 a month, or roughly NGN 389,000 across the 12 free months, quoted Also: 'Public IPs | NGN 5.9726 per IP per hour | NGN 4,360.00' a month, and 'Network egress | NGN 0.00 per GB | From 1 January 2027: 5 TB a month included per account, then NGN 15.00 per GB', quoted; the free tier page states 'Hours beyond 750 in a month, and volumes, public IPs and egress, bill at the rate card'
  - [1] 2026-10-22: quoted: '750 hours a month ... free for your first 12 months'; 'Hours beyond 750 in a month, and volumes, public IPs and egress, bill at the rate card'; 'Always free: Not offered yet.'
  - [4] 2026-10-22: quoted: 'Rate card v3 takes effect 1 November 2026. Rate card v5 takes effect 1 January 2027 in place of rate card v4, announced earlier for the same date'; prices fixed at NGN 1,327.24 per USD as of 2026-09-30 and 'Naira prices don't move with the exchange rate'
  - [3] 2026-10-22: quoted: 'New accounts start with trial credit, spent on any resource before your wallet balance; it doesn't expire ... No payment method is needed to start'
  - [5] 2026-10-22: free-tier API limits: 60 requests a minute with a burst of 10 a second, at NGN 0 a month
- sources:
  - [1] https://www.savannaa.com/pricing/free-tier
  - [2] https://www.savannaa.com/pricing/plans
  - [3] https://www.savannaa.com/docs?section=getting-started
  - [4] https://www.savannaa.com/pricing/rates
  - [5] https://www.savannaa.com/docs?section=api-reference
