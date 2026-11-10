# Leaseweb

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leaseweb/ | JSON https://fshy.ajam.dev/api/v1/entity/leaseweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leaseweb

- `compute/leaseweb` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.serverhunter.com/offer/leaseweb-vps-s-ams/
- free tier: EUR 4.99/month for VPS S in Amsterdam: 1 core at 2 GHz, 1 GB RAM, 40 GB SSD, 1,000 Mbit uplink, 4 TB traffic, KVM, monthly billing, no setup fee. The provider's own line is present on the tracker as thirty offers, VPS S to VPS XXL in six locations (AMS, FRA, IAD, LHR, SFO, SIN) plus a dedicated-server list. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 4 TB a month per the tracker row. No overage price and no post-allowance throttle are stated, and the vendor pricing page was not read | metered: yes | free allowance: 4 TB per month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 4 TB a month is the allowance the tracker row states, and it is the wall: the same row sells a 1,000 Mbit port, which passes 4 TB in about nine hours at line rate if the 4 TB is decimal and the port is sustained, so the byte counter binds long before the port does. Arithmetic, not a quoted vendor sentence. No overage price and no post-allowance throttle are stated on the row, so what happens at the cap is unverified. [1]
- limits note: 4 TB a month is the allowance the tracker row states, and it is the wall: the same row sells a 1,000 Mbit port, which passes 4 TB in about nine hours at line rate if the 4 TB is decimal and the port is sustained, so the byte counter binds long before the port does. Arithmetic, not a quoted vendor sentence. No overage price and no post-allowance throttle are stated on the row, so what happens at the cap is unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the pages read: the tracker row carries the feature tags '24/7 Support, API access, DDoS Protection, Instant Setup, Phone Support, SSD cached' and no control-panel or image list
- composes with: EUR 4.99 for 1 GB in Amsterdam is a control-plane host, not a byte mover: 4 TB a month is about 12 GB a day, which is a scheduler, a DNS secondary or a webhook receiver. The same provider's VPS XXL rows are the ones to price if the job is serving rather than scheduling
- reliability: no reliability event recorded
- notes: Found via serverhunter, which listed it among its 971 provider names.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 40
- evidence:
  - [1] 2026-10-22: row quoted: 'Monthly price EUR 4.99', 'Billing interval Monthly', 'Setup fee EUR 0.00', 'Product type VPS', 'Virtualization type KVM', 'Stock In stock', 'Processor cores 1 core', 'Processor speed 2 GHz', 'Memory amount 1 GB', 'Total SSD Capacity 40 GB', 'Uplink 1,000 Mbit', 'Traffic 4 TB', 'Location Amsterdam, Noord-Holland, The Netherlands'
  - [2] 2026-10-22: the provider page lists 30 VPS offers at three sizes in six regions plus a dedicated-server table; the offer names are 'VPS S - AMS' through 'VPS XXL - SIN' and 'Dell R210-II 1x Intel Xeon E3-1230V2' upward
  - [3] 2026-10-22: the vendor pricing path was attempted twice and both attempts returned 404: https://www.leaseweb.com/en/vps and https://www.leaseweb.com/en/virtual-servers. The homepage returned 200 but its extracted body carries no plan table, so no first-party plan price was read
- sources:
  - [1] https://www.serverhunter.com/offer/leaseweb-vps-s-ams/
  - [2] https://www.serverhunter.com/company/leaseweb/
  - [3] https://www.leaseweb.com/en/vps
