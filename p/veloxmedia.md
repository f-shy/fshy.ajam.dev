# VeloxMedia

> veloxmedia.co.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/veloxmedia/ | JSON https://fshy.ajam.dev/api/v1/entity/veloxmedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VeloxMedia

- `compute/veloxmedia` | paid-only | evidence documented | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T17:40:47.141Z (live) | stale on 2026-12-08
- url https://veloxmedia.co.uk/vps/
- price parsed USD 5/mo
- free tier: Micro at USD 5.00 per month: 1 vCPU, 2 GB RAM, 20 GB SSD, unmetered data transfer, one dedicated IPv4, full root access, in four regions (London from USD 5, Amsterdam from USD 6). Six uniform plans up to USD 26; annual billing includes two months free and there is no setup fee. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unmetered data transfer stated on the plan page, with no byte allowance and no overage price published | metered: no | free allowance: no cap published: 'unmetered data transfer' | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: no monthly byte allowance is stated: the vendor sells 'unmetered data transfer'. The tracker's card quantifies it at 50,000 GB a month on a 10 Gbps port, which is the tracker's figure and not the vendor's, so no cap is asserted here.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read; the vendor documents a client portal and a deploy button, no client or API
- composes with: unmetered transfer at USD 5 with 2 GB of RAM is the cheapest shape among documented hosts for a relaying or proxying workload where bytes matter more than disk; it would sit in front of a metered storage host
- reliability: the tracker marks every card for this provider with the flag 'Reliability problems were reported for this service'; that is the tracker's claim and was not verified against the vendor or against an operator report
- notes: Unmetered and unlimited are different claims and the vendor uses only the first, so the absence of a cap here is the vendor's wording rather than a measured absence of enforcement. The reliability flag is the strongest reason to probe this provider before trusting it with anything that must stay up.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - price_on_page: USD 5.00/month for Micro
  - renewal_usd: not published: the plan page prices the six plans monthly and gives two months free on annual billing; no renewal price appears on the page
- evidence:
  - [1] 2026-10-22: 'Every plan is uniform, so you choose capacity and nothing else changes. Micro: 1 vCPU, 2 GB RAM, 20 GB NVMe. Small: 2 vCPU, 4 GB RAM, 40 GB NVMe...' with plan prices '$5 $7 $12 $14 $20 $26'
  - [1] 2026-10-22: 'Pricing is in USD and starts at $5 per month, with Amsterdam from $6. There are no setup fees on any plan, and annual billing includes two months free.'
  - [2] 2026-10-22: tracker card carries class 'card fire' with title 'Reliability problems were reported for this service': '$5.00 / month 1 Intel Cores (shared) 2,048 MB RAM 20 GB NVMe 50,000 GB/month bandwidth 10 Gbps port speed IPv4 United Kingdom'
  - [1] 2026-11-07: the plan table's Micro row pairs 1 vCPU, 2 GB RAM, 20 GB SSD and unmetered transfer with $5/mo | capture: sha256:328347ff4fbcd41bf0d54444b755cb07bb064e4e84205f76c1f5d227f93cb15d | quote: MicroDev boxes and small services | 1 | 2 GB | 20 GB | Unmetered | $5/mo
  - [1] 2026-11-07: the plan list reads Micro at 1 vCPU, 2 GB RAM and 20 GB SSD, where the record's text said NVMe | capture: sha256:328347ff4fbcd41bf0d54444b755cb07bb064e4e84205f76c1f5d227f93cb15d | quote: Micro: 1 vCPU, 2 GB RAM, 20 GB SSD. Small: 2 vCPU, 4 GB RAM, 40 GB SSD.
  - [1] 2026-11-07: the pricing paragraph states monthly prices, no setup fees and two months free on annual billing; the page prints no renewal price | capture: sha256:328347ff4fbcd41bf0d54444b755cb07bb064e4e84205f76c1f5d227f93cb15d | quote: Pricing is in USD and starts at $5 per month, with Amsterdam from $6. There are no setup fees on any plan, and annual billing includes two months free.
- sources:
  - [1] https://veloxmedia.co.uk/vps/
  - [2] https://vpspricetracker.com/provider/VeloxMedia/vps
