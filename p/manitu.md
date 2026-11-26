# manitu

> manitu.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/manitu/ | JSON https://fshy.ajam.dev/api/v1/entity/manitu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## manitu (manitu.de) root servers

- `storage/manitu-root-servers` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:54.246Z (live) | stale on 2026-12-04
- url https://www.manitu.de/root-server/vergleich/
- free tier: none: dedicated root servers only; Root-Server M is 67,22 € per month excluding VAT plus a 500 € setup fee, with 2 x 2 TB SSD SATA | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: 10 TB per month of transfer is included on Root-Server L, XL and XXL; the transfer allowance of Root-Server M is not shown in the captured table (unverified) | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): largest disk configuration 2 x 4 TB NVMe (Root-Server XXL); 2 x 2 TB SSD SATA on Root-Server M [1]
- limits note: Root-Server M: 67,22 € per month excl. VAT for 2 x 2 TB = about 16.81 € per TB per month (raw disk capacity), plus a 500 € setup fee and a 12-month minimum term
- binding note: no root server exceeds 2 x 4 TB of disk; Root-Server M is the cheapest per TB
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Dedicated servers only. Root-Server M is €67.22 per month excluding VAT for 2x 2 TB SSD SATA (€16.81/TB), with a €500 setup fee. No high-capacity HDD storage product is offered.
- notes: the same as reliability
- evidence note: documented: the monthly price, disks and setup fee of each Root-Server are quoted from the comparison table https://www.manitu.de/root-server/vergleich/, and the 10 TB per month transfer of L, XL and XXL from https://www.manitu.de/root-server/ (vendor pages read 2026-11-03); the transfer of Root-Server M and the order steps were not read
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: VAT for 2× 2 TB SSD SATA = €16.81/TB, with a €500 setup fee. No high-capacity HDD storage product. Not a storage…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: VAT for 2× 2 TB SSD SATA = €16.81/TB, with a €500 setup fee. No high-capacity HDD storage product. Not a storage…
  - [1] 2026-11-03: Root-Server M costs 67,22 € per month excluding VAT | capture: sha256:960f35ea6e523dd78858daed7f14aadf54efacd2e20ac43ac6a647a889cfcd74 | quote: | Preis pro Monat ohne MwSt. | 67,22 € | 84,03 € | 126,04 € | 151,25 € |
  - [1] 2026-11-03: disks range from 2 x 2 TB SSD SATA to 2 x 4 TB NVMe | capture: sha256:960f35ea6e523dd78858daed7f14aadf54efacd2e20ac43ac6a647a889cfcd74 | quote: | Festplatten | 2 x 2 TB SSD SATA | 2 x 2 TB SSD SATA | 2 x 2 TB NVMe NVMe | 2 x 4 TB NVMe NVMe |
  - [2] 2026-11-03: L, XL and XXL include 10 TB per month of transfer | capture: sha256:8255b4beaa293e97035b54d8efbab8e7523af28c1d7e37f80a1ddb1a14d973a7 | quote: | Datentransfer | 10 TB pro Monat | 10 TB pro Monat | 10 TB pro Monat |
  - [1] 2026-11-03: the comparison page lists the 500 € setup fee of Root-Server M | capture: sha256:960f35ea6e523dd78858daed7f14aadf54efacd2e20ac43ac6a647a889cfcd74 | quote: | Einrichtungsgebühr ohne MwSt. | 500 € | 750 € | 2.500 € | 3.000 € |
  - [1] 2026-11-03: the vendor page was read and quoted on 2026-11-03: Root-Server M costs 67,22 € per month excluding VAT | capture: sha256:960f35ea6e523dd78858daed7f14aadf54efacd2e20ac43ac6a647a889cfcd74 | quote: | Preis pro Monat ohne MwSt. | 67,22 € | 84,03 € | 126,04 € | 151,25 € |
- sources:
  - [1] https://www.manitu.de/root-server/vergleich/
  - [2] https://www.manitu.de/root-server/
