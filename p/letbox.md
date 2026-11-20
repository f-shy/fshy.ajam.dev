# letbox storage kvm

> letbox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/letbox/ | JSON https://fshy.ajam.dev/api/v1/entity/letbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## letbox storage kvm

- `storage/letbox-storage-kvm` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:17.079Z (live) | stale on 2026-12-04
- url https://my.letbox.com/index.php?rp=%2Fstore%2Flos-angeles-storage-sbox
- free tier: No free allowance. Priced KVM storage VPS plans on the Los Angeles store, every plan marked Out of Stock: E5-250 from $3.00/mo, E5-500GB from $5.70/mo, E5-1TB (1 TB SAS RAID10, 8TB/Month) from $6.75/mo, E5-SBox-1.5TB (1.5 TB, 10TB/Month) from $15.00/mo. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Monthly transfer allowance per plan: 8TB/Month on E5-1TB, 10TB/Month on E5-SBox-1.5TB; 1Gbps uplink burstable. | metered: yes
- identity: email | detail: unverified: behind a sign-up; no plan can be ordered because every plan is Out of Stock.
- interface: unknown
- limits:
  - volume-quota (binding): 1.5 TB disk on the largest plan (E5-SBox-1.5TB) [1]
  - volume-quota (binding): 8TB/Month transfer on E5-1TB; 10TB/Month on E5-SBox-1.5TB [1]
- binding note: the largest listed plan holds 1.5 TB of disk; every plan reads Out of Stock.
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Every plan on the Los Angeles storage store reads Out of Stock on 2026-11-03. The earlier per-TB price claim is unverified: http://letbox.com/page/box answered HTTP 404 on 2026-11-03.
- notes: the same as the free tier
- evidence note: documented: plan disks, prices, monthly transfer and the Out of Stock marking are quoted from the vendor store page https://my.letbox.com/index.php?rp=%2Fstore%2Flos-angeles-storage-sbox read on 2026-11-03; http://letbox.com/page/box returned an error status in a probe the same day, so the earlier per-TB price claim stays unverified
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Correct product, wrong availability and wrong price. The LA storage store shows every rung 'Out of Stock', and the 1 TB rung is $6.75 for 8 TB of transfer. Its '$2.50/TB' claim in the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Correct product, wrong availability and wrong price. The LA storage store shows every rung 'Out of Stock', and the 1 TB rung is $6.75 for 8 TB of transfer. Its '$2.50/TB' claim in the…
  - [2] 2026-10-21: cited as the basis of the rejection: Correct product, wrong availability and wrong price. The LA storage store shows every rung 'Out of Stock', and the 1 TB rung is $6.75 for 8 TB of transfer. Its '$2.50/TB' claim in the market
  - [1] 2026-11-03: the 1 TB plan is $6.75 per month with 8 TB per month of transfer and is out of stock | capture: sha256:e2933ec995ada3453e043033315d67ed050502eaa66bcd511f94f2167955f676 | quote: 2 CPU 50% cores 2GB Dedicated RAM 1TB SAS Raid10 1Gbps Uplink burstable 8TB/Month 1 IPv4 Address From $6.75/mo Out of Stock
  - probe:letbox.com 2026-11-03: http://letbox.com/page/box answered HTTP 404 | capture: sha256:404d9cf45498ec558b93f27ab3acf5bf3b748cc46887c6b56f0cef4f0f99e9c7 | quote: "status": 404
  - [1] 2026-11-03: the vendor page was read and quoted on 2026-11-03: the 1 TB plan is $6.75 per month with 8 TB per month of transfer and is out of stock | capture: sha256:e2933ec995ada3453e043033315d67ed050502eaa66bcd511f94f2167955f676 | quote: 2 CPU 50% cores 2GB Dedicated RAM 1TB SAS Raid10 1Gbps Uplink burstable 8TB/Month 1 IPv4 Address From $6.75/mo Out of Stock
- sources:
  - [1] https://my.letbox.com/index.php?rp=%2Fstore%2Flos-angeles-storage-sbox
  - [2] http://letbox.com/page/box
