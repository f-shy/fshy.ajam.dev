# lex.st free

> lex.st | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lex/ | JSON https://fshy.ajam.dev/api/v1/entity/lex.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## lex.st free 150 gb storage box

- `storage/lex-st-free-150-gb-storage-box` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lex.st/
- free tier: none reachable: Endpoints /, /storagebox/, and /storagebox/signup/ returned HTTP 530 origin unreachable on 2026-10-21. The advertised 150 GB free tier is unreachable. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The LET thread is still the top hit for 'free…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The LET thread is still the top hit for 'free st
  - [2] 2026-10-21: The LET thread is still the top hit for 'free st
  - [3] 2026-10-21: The LET thread is still the top hit for 'free st
- sources:
  - [1] https://lex.st/
  - [2] https://lex.st/storagebox/
  - [3] https://lex.st/storagebox/signup/

## Lex.st — 150 GB free storage box 'for the life of the service'

- `storage/lex-st-150-gb-free-storage-box-for-the-life-of-the-servi` | fails-quota | evidence reported | binding none | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lex.st/storagebox/
- free tier: 150 GB HDD RAID-6 (NVMe cached), 1000 GB bandwidth, 2 domains, jailed SSH, DirectAdmin, Salt Lake City. Free permanently. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 1000 GB/month included. Metered and small; this is the binding limit, not the 150 GB. | metered: yes | free allowance: 1000 GB per month
- identity: email | detail: email
- interface: sftp, rsync, ssh, rclone
- limits note: Fixed storage quota is 150 GB with 1 TB per month bandwidth.
- interface detail: sftp
- tooling: Jailed SSH explicitly 'for rsync and the likes', plus DirectAdmin, plus NextCloud optionally available. rclone sftp works against jailed SSH if the jail exposes the storage path.
- composes with: Application-gated, so not repeatable: signups go through a Google-Form review and the host states users with '~1-100 comments and that have recently signed up can expect to be rejected'. The filter targets the several-accounts pattern.
- reliability: The offer is unreachable with endpoints /, /storagebox/, and /storagebox/signup/ returning HTTP 530 origin unreachable on 2026-10-21.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 150 GB HDD RAID-6 (NVMe cached), 1000 GB bandwidth, 2 domains, jailed SSH, DirectAdmin, Salt Lake City — free permanently.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'FREE USA DA Storage Boxes with 150GB of space, absolutely free for the life of the service! … 150GB HDD RAID-6 (NVMe Cached) … 1000GB Bandwidth … Jailed SSH Access (for rsync and the likes)'
  - [2] 2026-10-21: 
- sources:
  - [1] https://lowendtalk.com/discussion/203759/introducing-lex-st-free-150gb-usa-storage-boxes
  - [2] https://lex.st/
