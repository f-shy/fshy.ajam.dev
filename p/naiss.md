# NAISS Arrhenius Disk

> naiss.se | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/naiss/ | JSON https://fshy.ajam.dev/api/v1/entity/naiss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NAISS Arrhenius Disk / SENS Storage (Sweden) — 25 PB and 10 PB project storage, applied in GiB

- `storage/naiss-arrhenius-disk-sens-storage-25-pb-and-10-pb-projec` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://supr.naiss.se/round/2026medium/
- free tier: Project storage is applied for in GiB through SUPR, with generous upper limits: Arrhenius Disk shows 'Upper Limit 50,000', 'Default Storage 250', 'Available 4,000,000' (GiB. So 50,000 GiB ≈ 48.8 TiB ceiling, 250 GiB default); Klemming 'Upper Limit 100,000' with 'Available 5,850,000' GiB. Arrhenius SENS Storage is a 10 PB system for sensitive data, 'only available as when applying for a related compute resource'. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 48.8 TiB ceiling | bytes: 53656167435468 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free national e-infrastructure; no egress meter documented. | metered: no
- identity: institution
- interface: s3, sftp, scp, rsync
- limits:
  - per-object-cap (binding): 48.8 TiB ceiling [1]
- limits note: Per-object-cap: not applicable (POSIX/Lustre). Retention: 'There is no backup of Arrhenius Disk' and storage is tied to the project; NAISS Large requires prior PI status on a Medium project. request-rate: not published. Gate: heavy. 'you must be a scientist in Swedish academia, at least at the level of assistant professor' for Medium, PhD student + 20% appointment for Small, and Large requires 'an appointment of at least 60 percent at a Swedish university'.
- interface detail: sftp
- tooling: Lustre/POSIX on Arrhenius Disk (rsync/scp/sftp from a login node), no published S3 endpoint for the Disk resource. SUPR is the application portal.
- composes with: Small allocations are reviewed WEEKLY. 'Proposals are reviewed weekly throughout the year'. So a Swedish-affiliated PI can iterate to the ceiling in weeks rather than waiting for an annual round. Medium is the tier that carries the 50 TB-class ceilings.
- reliability: No backup on Arrhenius Disk or SENS Storage. Several listed resources (Alvis, Mimer) are mid-decommission with allocations being migrated. Check resource status before requesting.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: resource table: 'Arrhenius Disk | NAISS | 50 000 | 250 | 4 000 000' (GiB), 'Klemming | PDC | 100 000 | 500 | 5 850 000'; Alvis and Mimer flagged as decommissioned/migrating
  - [2] 2026-10-21: 'The total size of Arrhenius Disk is 25 PB. There is no backup of Arrhenius Disk.' Eligibility by tier.
  - [3] 2026-10-21: 'The total size of Arrhenius SENS Storage is 10 PB. There is no backup'; 'only available as when applying for a related compute resource'
  - [4] 2026-10-21: 'Proposals are reviewed weekly throughout the year'; 'at least a PhD student and hold an appointment of at least 20 percent at a Swedish university'
- sources:
  - [1] https://supr.naiss.se/round/2026medium/
  - [2] https://supr.naiss.se/resource/arrhenius-disk/
  - [3] https://supr.naiss.se/resource/arrhenius-sens-storage/
  - [4] https://user.naiss.se/allocations/small/
