# Chunkserve

> chunkserve.com | Egress and tunnels, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chunkserve/ | JSON https://fshy.ajam.dev/api/v1/entity/chunkserve.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ChunkServ

- `egress/chunkserve-xeon-standard-2` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS: KVM VPS with a metered monthly allowance and a 1 Gbps port | tier Xeon Standard 2
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T12:11:58.416Z (live) | stale on 2026-12-05
- url https://chunkserve.com/offers/vps
- free tier: No free tier. Xeon Standard 2 is EUR 2.49 monthly: 2 vCPU, 2GB RAM, 25GB NVMe, 1Gbit at 10TB network, KVM. | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 1Gbit at 10TB of network; the period of the allowance, the overage action and the byte tolerance are not published on the plan page read. | metered: yes | free allowance: 10 TB, period not stated | source: [1]
- identity: any-phone | detail: The registration form asks for first and last name, email address, phone number and billing address, and the terms say personal information must be provided to top up the wallet; whether the phone number is verified is unverified: behind a sign-up.
- interface: ssh
- limits:
  - volume-quota (binding): 10TB network on a 1Gbit port; overage action not published [1]
- binding note: 10 TB is the only countable figure and is above 1 TiB a month; its overage action is not published, so no first-failing quota is shown.
- interface detail: Root KVM VPS in the Netherlands or Poland.
- tooling: Any SSH client.
- composes with: A 10 TB, 1Gbit KVM box in the Netherlands or Poland. Port and protocol restrictions are not published on the page read.
- reliability: The terms give a trial of 3 hours, extendable to 24 hours, after which files are deleted.
- notes: The page lists a monthly price; the serverdeals yearly price was not found on the vendor pages.
- evidence note: Plan row, registration form and terms read on 2026-11-04. The serverdeals listing Yearly Deal NVMe (EUR 9.99 a year, 10 TB, 2Gbps) was not found on the vendor pages read.
- extras:
  - ipv6: unverified: not listed on the plan
  - term: monthly
  - virtualization: KVM
- evidence:
  - [1] 2026-11-04: the Xeon Standard 2 plan is listed | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: ### Xeon Standard 2
  - [1] 2026-11-04: the plan costs EUR 2.49 monthly | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: #### €2.49 monthly
  - [1] 2026-11-04: the plan has a 1Gbit port at 10TB of network | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: - 1Gbit @ 10TB Network
  - [1] 2026-11-04: locations are the Netherlands and Poland | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: Currently, we operate in The Netherlands and Poland.
  - [2] 2026-11-04: registration asks for name, email, phone number and billing address | capture: sha256:bf85779ef4335b164505ae97999e07751d62fd1589a3b5e47bef310cfbcc76b6 | quote: Personal Information First Name Last Name Email Address Phone Number Billing Address
  - [3] 2026-11-04: topping up the wallet needs personal information | capture: sha256:8b120fc7ba8d6bf4b0dc2e58cba1a9767e45b39ee6594d8a81e25938e3fea0ac | quote: In order to top up the virtual wallet in the user panel, personal information must be provided.
  - [4] 2026-11-04: serverdeals lists a ChunkServ Yearly Deal NVMe at EUR 9.99 a year with 10 TB and a 2Gbps port, a listing not found on the vendor pages read | quote: ###### Yearly Deal NVMe
  - [1] 2026-11-04: the plan row states 10TB of network on a 1Gbit port with no period | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: - 1Gbit @ 10TB Network
- sources:
  - [1] https://chunkserve.com/offers/vps
  - [2] https://billing.chunkserve.com/register.php
  - [3] https://chunkserve.com/terms.pdf
  - [4] https://serverdeals.cc/

## Chunkserve

- `compute/chunkserve` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:30.075Z (live) | stale on 2026-12-08
- url https://chunkserve.com/offers/vps
- free tier: Xeon Standard 1 at EUR 1.30/month: 1 vCPU Xeon E5-2690v4, 1 GB RAM, 15 GB NVMe, '1Gbit @ 5TB Network', KVM with instant deployment. The tracker instead lists EUR 1.49/month for a 2 GB RAM, 20 GB HDD plan with 51,200 GB/month on a 10 Gbps port in the Netherlands, which this page does not show. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB of network included with a 1 Gbit port on Xeon Standard 1, with no period printed on the card and no overage price published on the offers page | metered: yes | free allowance: 5 TB on Xeon Standard 1 (the card prints no period) | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 5 TB of network on a 1 Gbit port is what the vendor page states for Xeon Standard 1, with no period printed on the card; the tracked EUR 1.49 plan is listed with 51,200 GB/month at 10 Gbps, so the two rows are bound by numbers that differ by an order of magnitude [1]
- limits note: 5 TB of network on a 1 Gbit port is what the vendor page states for Xeon Standard 1, with no period printed on the card; the tracked EUR 1.49 plan is listed with 51,200 GB/month at 10 Gbps, so the two rows are bound by numbers that differ by an order of magnitude
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: order links point at a WHMCS store at billing.chunkserve.com with product paths such as /store/netherlands-vps/standard; no API is documented
- composes with: EUR 1.30 for 1 GB and 15 GB of NVMe is the cheapest per-GB RAM in this slice and suits a scheduler or a small relay; 5 TB of transfer is the small part and the 15 GB disk rules out any storage role
- reliability: no reliability event recorded
- notes: The vendor page's cheapest plan is both cheaper and smaller than the tracker's cheapest row, so the recorded offer is the vendor's and the tracked row stays in evidence. The site links a Polish CEIDG business-register entry and a policy PDF at chunkserve.com/policy.pdf. verification criteria: whether the tracked EUR 1.49 HDD plan at 10 Gbps is still orderable, since it is a materially different offer from anything on the offers page.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 15
  - monthly_eur: 1.3
  - annual_eur: not published: the offers page prints a monthly figure only
  - renewal_eur: not published: no page read prints a renewal or month-13 sentence
  - in_stock: no
  - billing_term: monthly
- evidence:
  - [1] 2026-10-22: plan card quoted: 'Xeon Standard 1', 'EUR1.30 monthly', '1 vCPU (Xeon E5-2690v4)', '1GB RAM', '15GB NVMe', '1Gbit @ 5TB Network', 'Instant Deployment', 'KVM Virtualization'
  - [1] 2026-10-22: the next tiers are quoted 'Xeon Standard 2' at 'EUR2.49 monthly' with '2 vCPU', '2GB RAM', '25GB NVMe', '1Gbit @ 10TB Network'; payment methods listed in the FAQ include PayPal, Stripe, Crypto and Cards
  - [2] 2026-10-22: tracker row quoted: 'Chunkserve - EUR1.49 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '20 GB HDD', '51,200 GB/month bandwidth', '10 Gbps port speed', 'Netherlands'; info page marks it 'In stock now' and lists port 25 'Open by default'
  - [1] 2026-11-07: the vendor's offers page lists Xeon Standard 1 at EUR 1.30 monthly | capture: sha256:0b2ac35d023eca0a92b51e940b67cb16d48a0b9f1721dc0901069bcc85fbef0e | quote: Xeon Standard 1
  - [3] 2026-11-07: the vendor cart answers Out of Stock for Xeon Standard 1 | capture: sha256:3c085dd7939abdbe616287d5bcc575961ce20688cab30bdd0e841d8c8af43de2 | quote: Out of Stock
  - [1] 2026-11-07: the vendor's offers page still lists Xeon Standard 1 at EUR 1.30 monthly with 1 vCPU, 1 GB RAM and 15 GB NVMe | capture: sha256:0b2ac35d023eca0a92b51e940b67cb16d48a0b9f1721dc0901069bcc85fbef0e | quote: Xeon Standard 1
  - [1] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:0b2ac35d023eca0a92b51e940b67cb16d48a0b9f1721dc0901069bcc85fbef0e | quote: Xeon Standard 1
  - [1] 2026-11-07: the offers page prints Xeon Standard 1 at EUR 1.30 monthly with the same shape and no annual or renewal figure | capture: sha256:44445d42eac88aab4bd20984d641e53f91539f8527e1fec645422c6acea5f93a | quote: ### Xeon Standard 1 #### €1.30 monthly - 1 vCPU (Xeon E5-2690v4) - 1GB RAM - 15GB NVMe - 1Gbit @ 5TB Network
  - probe:https://billing.chunkserve.com/index.php?rp=/store/netherlands-vps/standard 2026-11-07: the cart read of the Netherlands standard store route carries the out-of-stock phrase with no price | capture: sha256:1adb7c15918bffac46aa2e096eb4ab9a78193e33125679ee49787c1b06cac3fe | quote: out of stock
- sources:
  - [1] https://chunkserve.com/offers/vps
  - [2] https://vpspricetracker.com/provider/Chunkserve/vps
  - [3] https://billing.chunkserve.com/index.php?rp=/store/netherlands-vps/standard
