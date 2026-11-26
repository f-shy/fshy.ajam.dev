# AlaVPS

> alavps.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alavps/ | JSON https://fshy.ajam.dev/api/v1/entity/alavps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AlaVPS

- `compute/alavps` | dead | evidence reported | binding write-gated | category free VPS | tier Free VPS (No Credit Card)
- needs card no, phone yes, ID no, institution no | verified 2026-10-24T04:09:20.000Z (live) | stale on 2026-11-08
- url https://alavps.com/vps.html
- free tier: The marketing page sells a USD 0 tier with no payment information: 'Free VPS (No Credit Card)', '$0 / ongoing*', '2 vCPU cores (dedicated KVM threads)', '8 GB DDR5 ECC RAM', '128 GB NVMe SSD (RAID-protected)', '1 dedicated IPv4 + IPv6 subnet', 'No billing info ever requested', with the asterisk explained as a capacity gate: 'Free VPS capacity is limited. If slots are full, you'll be waitlisted'. The page also promises permanence: 'Zero Cost Forever' and 'Remain free indefinitely under fair-use compliance'. BUT the order system the page's own button leads to names the product 'Free VPS Server - 120 Days Beta' and heads the category 'Free VPS Server For Trial', and the page's own FAQ row concedes 'promotional duration limits'. The duration is therefore not 'forever'. | unit: none | metered on: identity-count | read on: 2026-10-24 | source: [1] | note: the plan card says forever; the order system says 120 days beta; the order is never fulfilled
- per-object cap: 128 GB of NVMe on the free tier; no per-object cap, the unit is a machine | bytes: 137438953472
- retention: Contradicted by the vendor's own order system: the product is listed as 'Free VPS Server - 120 Days Beta' under the heading 'Free VPS Server For Trial', while the FAQ on the same site says 'Forever, under fair-use compliance' and 'promotional duration limits'. Nothing was provisioned, so no retention was observed. | source: [2] | note: the 120-day figure is the order system's own product name, not a marketing claim
- egress: The order system lists '20 TB Bandwidth (1Gbps Port)' on the free product; the marketing page says 'Generous unmetered bandwidth with fair-use policies'. The two disagree, and neither is a published allowance with a throttle rule. | metered: no | source: [2]
- identity: email | detail: No card and no hold - 'No billing info ever requested' - but the registration form at manage.alavps.com/register.php requires 'First Name *', 'Last Name *', 'Email Address', 'Street Address *', 'City *', 'State/Region *', 'Postcode *', a country and a password, with company name and phone present and not marked required. So the price of trying it is a full name and postal address, not a card.
- interface: ssh, rest
- limits:
  - write-gated (binding): the order is accepted and then never fulfilled: multiple independent accounts report it sitting at 'pending' indefinitely, and one reports an 'online' status that cannot be connected to [3]
  - retention-clamped: the order system's own product name is 'Free VPS Server - 120 Days Beta', against the page's 'Zero Cost Forever' [2]
- limits note: the binding is delivery, not capacity: the plan is free and the slot is open, and the server does not arrive
- binding note: the offer fails after the data is handed over: the order is accepted, the price is USD 0.00, and no machine is ever provisioned, which makes the cost of trying it the personal data in the signup form
- interface detail: the page promises 'Full Admin/Root SSH & RDP access' on a KVM guest; no server was ever issued, so no interface was reached
- tooling: any SSH or RDP client, if a server is ever issued; nothing was reachable on 2026-10-24.
- composes with: at 8 GiB and 128 GB with a dedicated IPv4 this would be the strongest no-card machine in earlier readings if it delivered, which is exactly why the record cannot rest on the vendor's page alone.
- reliability: no server was ever observed to exist. Trustpilot reports a 1.9 'Poor' TrustScore across 13 reviews for alavps.com, including one reading 'scammers, free vps stays pending forever' and one 'If you get a vps from them it'll show like its online but you're never able to connect and they just collect your data'; LowEndTalk's list of self-declared free-VPS providers that only harvest data names alavps.com first; and the order page's own product name calls it a 120-day beta.
- notes: REFUTED 2026-10-24. One does exist now, in quantity, and it is unanimous: the order is accepted at USD 0.00 and never fulfilled. The sharpest evidence is not the reviews, it is AlaVPS against itself - the marketing page says 'Zero Cost Forever' while the order system its own button leads to names the product 'Free VPS Server - 120 Days Beta' under the heading 'Free VPS Server For Trial'. The 'forever' claim is not merely unproven, it is contradicted by the vendor's own shop. The verdict is dead rather than qualifies-with-caveat: a free machine that never provisions is worth less than nothing, because trying it costs a full name and postal address and returns no capacity. Nothing was signed up for.
- evidence note: the plan terms are documented from the vendor's own pages; the verdict rests on independent third-party reports of non-delivery and on the vendor's order system contradicting the vendor's marketing page, which is the weakest rung among the fields the verdict depends on
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 8
  - shape.disk_gib: 128
  - billing_model: free
  - term: free indefinitely per the vendor, subject to capacity
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 by the vendor's plan card; unverified, so the zero is a claim and not a measurement
  - free_tier_kind: free-forever
  - payment_methods: none taken on the free tier
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none stated; the vendor sells the plan as permanent
- evidence:
  - [1] 2026-10-24: quoted: 'Free VPS (No Credit Card)', '$0 / ongoing*', '2 vCPU cores (dedicated KVM threads)', '8 GB DDR5 ECC RAM', '128 GB NVMe SSD (RAID-protected)', '1 dedicated IPv4 + IPv6 subnet', 'No billing info ever requested'
  - [1] 2026-10-24: quoted, the permanence claim: 'Zero Cost Forever' and 'Remain free indefinitely under fair-use compliance'; and, contradicting it on the same page, 'Free VPS may have periodic re-verification (email confirmation) or promotional duration limits to prevent abandoned servers.'
  - [2] 2026-10-24: the order system's own product name, read from the page's product element: 'Free VPS Server - 120 Days Beta', under the heading 'Free VPS Server For Trial', priced '$0.00 USD', with '20 TB Bandwidth (1Gbps Port)' - the vendor's shop says 120 days where the vendor's marketing page says forever
  - [4] 2026-10-24: the live registration form requires First Name, Last Name, Street Address, City, State/Region and Postcode, with email, phone and company present; no card field appears anywhere on the form
  - [3] 2026-10-24: another: 'If you get a vps from them it'll show like its online but you're never able to connect and they just collect your data'; the page renders a TrustScore of 1.9 'Poor' across '13 reviews'
  - [5] 2026-10-24: quoted, naming alavps.com first in a list of 'self-declared free VPS providers that are just phishing your data, without any further information after you have ordered their free VPS plans. Under the service section your order is always in the status of "pending"'
  - [6] 2026-10-24: quoted, a hands-on attempt: 'And this is where I'm still at. My personal information is gone, I have no free VPS hosting and support is non-existent. At least no one has asked for my credit card information.' with the table row 'Scam | ✔'
  - [7] 2026-10-24: a competing host's comparison, which is a third party but not an independent one: 'The limited-term nature means you shouldn't rely on it as a permanent solution' - corroborated by AlaVPS's own order page calling the product a 120-day beta
- sources:
  - [1] https://alavps.com/vps.html
  - [2] https://manage.alavps.com/index.php?rp=/store/free-vps-hosting
  - [3] https://www.trustpilot.com/review/alavps.com
  - [4] https://manage.alavps.com/register.php
  - [5] https://lowendtalk.com/discussion/163646/list-of-scammers
  - [6] https://hightechblogging.com/blog/best-free-vps-hosting-providers/
  - [7] https://vpswala.org/blog/best-free-vps-usa/
