# GoAnywhere MFT

> goanywhere.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/goanywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/goanywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GoAnywhere MFT / GoDrive

- `storage/goanywhere-mft-godrive` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category iaas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.goanywhere.com/products/goanywhere-free/efss
- free tier: GoDrive EFSS is 'completely free' but only as a component of on-premises GoAnywhere MFT. Capacity is your server's disk; there is no hosted free storage. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A. On-premises. | metered: no
- identity: card | detail: inferred from the category 'iaas'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, webdav, sftp, ftp
- limits note: Bounded by your hardware. No per-object or retention cap stated.
- interface detail: sftp / ftp / webdav / rest (GoDrive web UI)
- tooling: GoAnywhere MFT installer + GoDrive module; FileCatalyst Service as an accelerator
- composes with: Same shape as ExaVault: free software that runs on hardware the service does not provide, so it is not an option here. 'Unlimited users' multiplies nothing that costs the vendor money, which is why the software is free. The vendor's own 'your hardware' phrasing is quoted in limits_verbatim, not repeated as advice.
- reliability: On-prem only; the 'free' page is really a lead-gen page for the paid MFT platform.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: GoDrive EFSS is 'completely free' but only as a component of on-premises GoAnywhere MFT. Capacity is your server's disk; there is no hosted free storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'A completely free file sharing solution, GoDrive is included with GoAnywhere MFT', 'GoDrive ... is an on-premises managed file transfer sharing solution'
- sources:
  - [1] https://www.goanywhere.com/products/goanywhere-free/efss
