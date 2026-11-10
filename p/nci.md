# NCI Gadi /g/data

> nci.org.au | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nci/ | JSON https://fshy.ajam.dev/api/v1/entity/nci.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NCI Gadi /g/data (Australia) — 110+ PB persistent parallel filesystem, allocation-gated

- `storage/nci-gadi-g-data-110-pb-persistent-parallel-filesystem-al` | fails-quota | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.nci.org.au/infrastructure/storage-systems
- free tier: Infrastructure is huge. '/g/data4-7 | 110+ PB | Persistent Storage', 'Massdata | 70+ PB'. But there is no free self-service quota: bytes come from the merit-based Adapter scheme or a share of a funded project. Adapter is 'temporarily closed. It is scheduled to reopen in Q4 2026'. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not documented as metered, but access is via NCI systems and Globus rather than public HTTP; there is no public-bucket download path like Allas or OSN. | metered: yes
- identity: institution
- interface: s3, sftp
- limits:
  - write-gated (binding): review [1]
- limits note: per-object-cap: n/a (POSIX). Retention: /scratch is job-scoped, /g/data is persistent for the project. request-rate: n/a. Gate: Australian institution + merit review; Adapter currently CLOSED until Q4 2026.
- interface detail: sftp
- tooling: POSIX/Lustre on Gadi, Globus for transfer. No S3 endpoint in the storage-systems page.
- composes with: Adapter is quarterly and 'designed to identify meritorious research projects which need flexible compute access over a short period'. The short period is the anti-multiplier; you would be re-applying every quarter.
- reliability: Closed allocation scheme with access restricted to approved Australian research projects.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Infrastructure is huge — '/g/data4-7 | 110+ PB | Persistent Storage', 'Massdata | 70+ PB' — but there is no free self-service quota: bytes come from the merit-based Adapter scheme or a share of a funded project. Adapter is 'temporarily closed. It is scheduled to reopen in Q4 2026'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: '/g/data4-7 | 110+ PB | Persistent Storage', '/scratch | 20 PB', 'Massdata | 70+ PB'
  - [1] 2026-10-21: 'The Adapter scheme is temporarily closed. It is scheduled to reopen in Q4 2026.'
- sources:
  - [1] https://nci.org.au/users/how-access-nci/adapter-scheme
  - [2] https://www.nci.org.au/infrastructure/storage-systems
