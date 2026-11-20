# VPSWala

> vpswala.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vpswala/ | JSON https://fshy.ajam.dev/api/v1/entity/vpswala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VPSWala

- `compute/vpswala` | dead | evidence reported | binding write-gated | category free VPS | tier Starter (free forever)
- needs card no, phone yes, ID no, institution yes | verified 2026-10-24T04:09:20.000Z (live) | stale on 2026-11-08
- url https://vpswala.org/
- free tier: An 'Always Free' Starter plan at '$0.00 Always Free' with '1 vCPU Core (ARM64)', '2 GB DDR4 ECC RAM', '500 MB NVMe SSD', '10 GB Bandwidth', 'Linux OS Only' and 'SSH Root Access', sold as permanent: 'Yes! The Starter tier (1 vCPU ARM64, 2GB RAM, 500MB NVMe) is genuinely no-cost with no expiry and no credit card ever required.' The plan is still offered today - the order page lists 'Free Linux VPS Starter' with no out-of-stock marker - but four independent accounts, one of them hands-on, report the server never arriving. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: the plan is a machine, not a metered allowance; the binding constraint is that it is not delivered
- per-object cap: not applicable | note: Disk storage limit is 500 MB NVMe.
- retention: The vendor states no expiry, but adds a login condition on another page: 'Your free Linux VPS will remain active as long as you use it regularly. We require at least one login every 30 days to keep free servers active.' Nothing was observed, because nothing was provisioned. | days: 30 | source: [2] | note: the 30-day figure is the vendor's own inactivity rule, not a trial length
- egress: '10 GB Bandwidth' on the Starter plan; what happens above it is not published | metered: yes | free allowance: 10 GB | source: [1]
- identity: institution | detail: No card - 'No credit card required' - but the registration form at client.vpswala.org/register.php requires 'First Name *', 'Last Name *', 'Email Address', 'Street Address *', 'City *', 'State/Region *', 'Postcode *', a country and a password, with company name and phone present. A verification gate of '.edu or .ac email, a linked GitHub profile, or a company email' is advertised on the Hindi page. A GitHub profile is producible, so the gate is passable; the obstacle is that passing it did not produce a machine for the reporters. Nothing was signed up for.
- interface: ssh, rest
- limits:
  - write-gated (binding): the order is accepted and then never fulfilled; independent accounts report 'pending' indefinitely, an 'online' instance that cannot be logged into, and a redirect to a third-party affiliate instead of a server [3]
  - volume-quota: '10 GB Bandwidth' a month [1]
  - retention-clamped: 'We require at least one login every 30 days to keep free servers active' [2]
- limits note: the binding is delivery: the plan is cardless and open, and no server is issued to anyone who has written about it
- binding note: the plan is not refused at the price or the identity step, it is refused after them: the order and the support ticket both sit at 'pending', which is the same failure mode documented records already records for GratisVPS
- interface detail: the plan card promises 'SSH Root Access' and a client panel at client.vpswala.org; no login was attempted and no credentials were requested
- tooling: any SSH client, if a server is ever issued; nothing was reachable in verification
- composes with: would be a WireGuard or health-monitor node at 500 MB of disk and 10 GB of transfer, if the plan provisioned
- reliability: no server was ever observed to exist. A hands-on account reports the order and the ticket both 'pending' after almost three weeks; a forum account reports an instance that cannot be logged into; two Trustpilot reviewers in 2026 report no VPS and a redirect to a Kamatera affiliate link; and the LowEndTalk list of data-harvesting free-VPS providers names vpswala.org.
- notes: STILL TRUE, AND WORSE 2026-10-24. The failure is delivery, so the verdict is dead. Nothing has changed for the better. The plan is still advertised at '$0.00 Always Free' and the order page still lists 'Free Linux VPS Starter' with no out-of-stock marker, so it is not withdrawn - it is simply never fulfilled. The reports now run from 2023 to 2026 and include a 2026 reviewer describing a redirect to a Kamatera affiliate link rather than a server. A vendor that contradicts itself about the gate is not a source for whether the gate was passed. It stays out of the shortlist. Nothing was signed up for.
- evidence note: the plan terms are documented from the vendor's own pages; the verdict rests on independent third-party reports of non-delivery, which is the weakest rung among the fields the verdict depends on
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 2
  - shape.disk_gib: 0.5
  - billing_model: free
  - term: free forever per the vendor
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 by the vendor's plan card; the figure is not a price until a server exists
  - free_tier_kind: free-forever
  - payment_methods: no card, per 'No credit card required'; the paid tiers take PayPal only according to a 2020 review
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - session_cap.restart_required: no
  - session_cap.note: none stated; the plan is sold as permanent, so the clock is not the constraint and delivery is
- evidence:
  - [1] 2026-10-24: quoted: '$0.00 Always Free', '1 vCPU Core (ARM64)', '2 GB DDR4 ECC RAM', '500 MB NVMe SSD', '10 GB Bandwidth', 'SSH Root Access'
  - [1] 2026-10-24: quoted, the permanence claim: 'Yes! The Starter tier (1 vCPU ARM64, 2GB RAM, 500MB NVMe) is genuinely no-cost with no expiry and no credit card ever required.'
  - [4] 2026-10-24: the order page still lists the product today: 'Free Linux VPS Starter' with no out-of-stock marker, alongside 'Linux VPS Professional (FREE TRIAL)', 'WordPress Pro' and 'Enterprise VPS'
  - [5] 2026-10-24: the live registration form requires First Name, Last Name, Street Address, City, State/Region and Postcode, with email, phone and company present; no card field appears anywhere on the form
  - [2] 2026-10-24: quoted, contradicting the homepage: 'Credit Card Required' appears three times on this page ('- Credit Card Required', 'Credit Card Required Instant Activation Free Migration Support 30-Day Free Trial', 'Try out your free Linux VPS with credit card required'), against the homepage's 'no credit card ever required'; and the inactivity rule: 'We require at least one login every 30 days to keep free servers active.'
  - [6] 2026-10-24: quoted, a hands-on attempt: 'I signed up for the free plan. To do so, they asked me for tons of information like name, email, phone, & full billing address' then 'Almost 3 weeks later, the services and the ticket are still comfortably "pending"', with the table row 'Free VPS Plan Works ✘' and 'Scam ✔'
  - [7] 2026-10-24: quoted, a second account: '虽然给信息了，实际不能用啊登陆不上去' - the information was given but the server cannot be used and cannot be logged into
  - [8] 2026-10-24: and on 2026-04-25: 'shell company redirects to try.kamatera.com ... This is not a trial VPS. The paid VPS does not exist either.'
  - [9] 2026-10-24: quoted, vpswala.org is listed among 'self-declared free VPS providers that are just phishing your data ... your order is always in the status of "pending"'
- sources:
  - [1] https://vpswala.org/
  - [2] https://vpswala.org/linux-vps.html
  - [3] https://www.trustpilot.com/review/vpswala.org
  - [4] https://client.vpswala.org/index.php?rp=/store/linux-vp-hosting
  - [5] https://client.vpswala.org/register.php
  - [6] https://hightechblogging.com/blog/best-free-vps-hosting-providers/
  - [7] https://www.nodeloc.com/t/topic/38373
  - [8] https://ca.trustpilot.com/review/vpswala.org
  - [9] https://lowendtalk.com/discussion/163646/list-of-scammers
