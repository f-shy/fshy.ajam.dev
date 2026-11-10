# VPSPioneer

> vpspioneer.com | Compute, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpspioneer/ | JSON https://fshy.ajam.dev/api/v1/entity/vpspioneer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPSPioneer (Compute)

- `compute/vpspioneer` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-06T17:42:12.769Z (live) | stale on 2026-12-07
- url https://vpspioneer.com/
- free tier: Two product lines. Cloud VPS S is USD 8.49/month including VAT (USD 84.90/year): 2 vCores, 4 GB, 40 GB NVMe, 1 Gbps port, unlimited traffic, IPv4 plus IPv6, root access. M is USD 15.99/month for 4 vCores, 8 GB and 75 GB; L is USD 22.99 for 6 vCores, 12 GB and 100 GB; XL is USD 43.99 for 8 vCores, 24 GB and 200 GB. Shared hosting runs from Pioneer Start at USD 2.49/month (USD 24.90/year): 5 GB SSD, 50 GB monthly traffic on the vendor page, 1 website, LVE limit 100 percent CPU and 1 GB RAM, 200 outbound messages a day. Every plan carries a 30-day money-back guarantee and the offer post adds a 3-day free trial. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unlimited traffic on the Cloud VPS line behind a 1 Gbps port; the shared line is metered at 50 GB a month for Pioneer Start on the vendor page and 250 GB on the offer post | metered: yes | free allowance: unlimited on Cloud VPS; 50 GB per month on the Pioneer Start shared plan | source: [1]
- identity: email | detail: email: the registration form requires an email address ('placeholder="Email Address"') and the account also collects a name, a postal address, a phone number and an optional company name ('Name, email address, postal address, phone number, and company name if you provide one.'). Phone: not published: the form carries a 'Phone Number' field and no page read states that it is required. Card: not published: the form carries no card field, and the terms state 'If you have provided card details, we will attempt to take payment automatically from three days before the due date.'. Country: not published: the form's country selector offers a full country list and no page read restricts the account to one country.
- interface: rest, cli
- limits:
  - volume-quota (binding): the Cloud VPS line is unlimited traffic on a 1 Gbps port, so there the port binds. The shared line carries a monthly allowance that is the wall on the cheapest plan: the vendor page states 50 GB a month for Pioneer Start against 250 GB for Grow and 500 GB for Pro, and the offer post states 250 GB for every one of the three, so the ceiling on the entry plan is disputed between the two pages. The trial is 3 days. [1]
- limits note: the Cloud VPS line is unlimited traffic on a 1 Gbps port, so there the port binds. The shared line carries a monthly allowance that is the wall on the cheapest plan: the vendor page states 50 GB a month for Pioneer Start against 250 GB for Grow and 500 GB for Pro, and the offer post states 250 GB for every one of the three, so the ceiling on the entry plan is disputed between the two pages. The trial is 3 days.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: a customer portal at customer.vpspioneer.com is named; no API, CLI or rclone backend is documented on the page read
- composes with: the useful row here is the shared line rather than the VPS: USD 2.49/month for 5 GB, 50 GB of traffic, 5 mailboxes and 200 outbound messages a day is the cheapest way among documented hosts to get a mailbox and a small site on one invoice, and the 3-day trial makes it testable without paying
- reliability: no reliability event recorded
- notes: The record covers a shared-hosting product as well as a VPS one, which is why the shape describes the Cloud VPS S rather than the cheaper shared plan: the shared plan's RAM is an LVE limit and not a machine. Unverified: whether Pioneer Start carries 50 GB or 250 GB of monthly traffic, since the two pages read on the same day disagree, and whether the 3-day trial is self-serve or ticket-gated.
- extras:
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 40
- evidence:
  - [1] 2026-10-22: Cloud VPS block quoted: 'Cloud VPS S ... 2 vCores ... 4 GB ... 40 GB NVMe ... 1 Gbps ... Unlimited ... IPv4 + IPv6 ... $8.49 /mo inc. VAT, $84.90/year'; shared block: 'Pioneer Start ... 5 GB SSD Storage ... 50 GB Monthly Traffic ... $2.49 /mo $24.90/year, two months free'; page description: 'DirectAdmin-managed web hosting on NVMe SSDs from $2.49/month'
  - [2] 2026-10-22: third-party offer post, published 2026-10-11: shared table gives 'Monthly traffic 250 GB | 250 GB | 500 GB' and 'NVMe storage 5 GB | 10 GB | 25 GB'; body text: 'Every plan has a 3-day free trial and a 30-day money-back guarantee'; 'Annual billing includes two months free'; code 'LET10PERCENT' takes 10 percent off
  - [3] 2026-11-04: opening an account collects a name, an email address, a postal address, a phone number and an optional company name | capture: sha256:9a817d8d8ded7cf3a2093c26746263ba31c4d8eceb72cb5ed0bb1e72efefa283 | quote: Name, email address, postal address, phone number, and company name if you provide one.
  - [4] 2026-11-04: the registration form marks the company name optional and carries a phone number field, a billing address and a Google sign-in button | capture: sha256:f4df6c3fef4a0dcb618bc4479d6e38d95e2fd6a7a8d05cb9a5e455ce7d73f960 | quote: placeholder="Company Name (Optional)"
  - [5] 2026-11-04: the account's contact channel is its email address | capture: sha256:d5bc81d1df799ca4c30d01e44683c19a7df47e706c853c1f85af526426016812 | quote: We send important notices, including suspension warnings, to the email address on your account.
  - [4] 2026-11-04: the registration form requires an email address and needs no company, which is the email kind | capture: sha256:f4df6c3fef4a0dcb618bc4479d6e38d95e2fd6a7a8d05cb9a5e455ce7d73f960 | quote: placeholder="Email Address"
  - [4] 2026-11-06: the registration form requires an email address, carries a phone field and no card field, and offers a full country list | capture: sha256:a7f6dd0cfb1f7d96d3bc864823314459b19f023e947b1f79cb49a60a0014a722 | quote: placeholder="Email Address"
- sources:
  - [1] https://vpspioneer.com/
  - [2] https://lowendbox.com/blog/vpspioneer-directadmin-cloudlinux-hosting-in-france-starting-at-2-49-month/
  - [3] https://vpspioneer.com/legal/privacy-policy
  - [4] https://customer.vpspioneer.com/register.php
  - [5] https://vpspioneer.com/legal/terms-of-service

## VPSPioneer (Cloud VPS S)

- `egress/vpspioneer-cloud-vps-s` | paid-only | evidence documented | binding per-ip-shaping | category vps (hosted, France, root access, IPv4 and IPv6) | tier Cloud VPS S
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:18.335Z (live) | stale on 2026-12-05
- url https://vpspioneer.com/
- price USD 8.49 per month including VAT for unlimited traffic on a 1 Gbps port | parsed USD 8.49/mo
- free tier: No free plan; a 3-day free trial and a 30-day money-back guarantee are stated on the offer post. Cloud VPS S is USD 8.49 a month including VAT or USD 84.90 a year: 2 vCores, 4 GB, 40 GB NVMe, 1 Gbps port, unlimited traffic, IPv4 plus IPv6. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a rented server, not an object store | source: [1]
- retention: not applicable: a live server, not stored bytes | source: [1]
- egress: unlimited traffic with no transfer cap and no overage bill on the 1 Gbps port; outbound SMTP 25, 465 and 587 is blocked by default | metered: no | free allowance: no transfer cap on the Cloud VPS line, paid, no free tier | source: [1]
- identity: email | detail: unverified: the registration page read renders only sign-in status messages and no form fields; no card, phone or ID requirement is stated on a page read
- interface: ssh
- limits:
  - per-ip-shaping (binding): 1 Gbps port with unlimited traffic [2]
  - request-rate: outbound SMTP (ports 25, 465 and 587) is blocked by default on Cloud VPS and Managed VPS and opened on request [2]
- binding note: No byte allowance is published, so the 1 Gbps port and the fair-share clause of the provider are the stated limits; no number is given for the throttle.
- interface detail: a root server with a choice of Ubuntu, Debian, AlmaLinux or Rocky Linux, delivered about a minute after payment
- tooling: any SSH client; a customer portal at customer.vpspioneer.com
- composes with: a plain root VPS with IPv4 and IPv6 on a 1 Gbps port and no transfer cap; outbound mail ports are blocked until a request, every other port is not stated as filtered
- reliability: no reliability event recorded
- notes: Not free. The Cloud VPS S is a paid root VPS on a 1 Gbps port with no stated transfer cap; the cheaper shared-hosting plans from USD 2.49 a month carry 50 to 500 GB monthly traffic and are not a machine.
- evidence note: Traffic, port and price are on the vendor's own pages. The offer post's trial and refund statement is third-party and the Cloud VPS is not the product the offer post advertises (shared hosting).
- extras:
  - nat: not stated; the plan lists IPv4 plus IPv6
  - ipv6: IPv4 plus IPv6 is listed on the Cloud VPS plans; prefix size not stated
  - inbound: not stated beyond the default block on outbound SMTP
  - udp: not stated; a root server
  - volume_stated: Unlimited
  - bytes_transit: yes
  - transit_note: bytes leave from the guest's own address on the provider's network
- evidence:
  - [1] 2026-11-04: the Cloud VPS line has unlimited traffic | capture: sha256:8e4ff7ea2cc18c260f8b031a301c06e27f3edbdeb4343b716ec1d04db02ad309 | quote: Fair-share vCores and reserved RAM on NVMe SSDs, unlimited traffic and Anti-DDoS.
  - [1] 2026-11-04: there is no transfer cap and no overage bill | capture: sha256:8e4ff7ea2cc18c260f8b031a301c06e27f3edbdeb4343b716ec1d04db02ad309 | quote: No transfer cap and no overage bill.
  - [1] 2026-11-04: the Cloud VPS starts at USD 8.49 a month with root access | capture: sha256:8e4ff7ea2cc18c260f8b031a301c06e27f3edbdeb4343b716ec1d04db02ad309 | quote: A Cloud VPS with root access and your choice of Linux. Instant delivery, about a minute after payment. *02 · from***$8.49*/mo***
  - [1] 2026-11-04: the Cloud VPS S annual price is USD 84.90 | capture: sha256:8e4ff7ea2cc18c260f8b031a301c06e27f3edbdeb4343b716ec1d04db02ad309 | quote: $84.90/year
  - [3] 2026-11-04: the post states a 3-day free trial and a 30-day money-back guarantee | capture: sha256:cc6f7f613ecade644b4be64821b1c8f93b83b3fa415014820c2491c034141cd7 | quote: Every plan has a 3-day free trial and a 30-day money-back guarantee.
  - [2] 2026-11-04: outbound SMTP is blocked by default | capture: sha256:03896928ae4fd7cd1b759b2078787bdc329f57ff5d49dc3db6478e4370a02849 | quote: Outbound SMTP (ports 25, 465 and 587) is blocked by default on Cloud VPS and Managed VPS accounts.
  - [2] 2026-11-04: usage that affects others can be throttled or suspended | capture: sha256:03896928ae4fd7cd1b759b2078787bdc329f57ff5d49dc3db6478e4370a02849 | quote: We may throttle, suspend or ask you to upgrade if your usage affects other customers.
- sources:
  - [1] https://vpspioneer.com/
  - [2] https://vpspioneer.com/legal/acceptable-use-policy
  - [3] https://lowendbox.com/blog/vpspioneer-directadmin-cloudlinux-hosting-in-france-starting-at-2-49-month/
