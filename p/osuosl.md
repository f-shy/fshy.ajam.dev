# OSU Open Source Lab

> osuosl.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/osuosl/ | JSON https://fshy.ajam.dev/api/v1/entity/osuosl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OSU Open Source Lab - FTP mirroring (ftp.osuosl.org / ftp2.osuosl.org)

- `storage/osu-open-source-lab-ftp-mirroring` | qualifies-with-caveat | evidence reported | binding write-gated | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://osuosl.org
- free tier: No published per-project quota, but an explicit capacity statement and an allocation policy: 'Because space on the main mirrors is limited, we also host projects on ftp2.osuosl.org. It runs in Salem and stores its content on our Ceph cluster instead of copying it to every server. We currently host about 100 projects using around 37 TB of disk space, about 16 TB on the main mirrors and 21 TB on ftp2.' Mean is therefore ~370 GB per hosted project. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: The binding constraint is the request/review process ('Please give us a few days or a week to discuss and respond') and the statement that main-mirror space is limited. retention: indefinite for accepted projects | source: [1] | note: not stated
- egress: Free and genuinely high-capacity: 'Three servers sit behind ftp.osuosl.org with a combined bandwidth capacity of 60 gigabits per second. They are located in Salem, Chicago and New York, and each one carries a full copy of the content.' No billing. | metered: no
- identity: email
- interface: rest, ftp, rsync
- limits:
  - write-gated (binding): review process ('Please give us a few days or a week to discuss and respond') and the [1]
- limits note: per-object-cap: none published. The binding constraint is the request/review process ('Please give us a few days or a week to discuss and respond') and the statement that main-mirror space is limited. retention: indefinite for accepted projects. request-rate: N/A (mirror serves static files).
- interface detail: rest
- tooling: FTP/HTTP mirror distribution plus rsync from the mirror ring; no self-service upload API - content is placed by arrangement. Request flow is a form at osuosl.org/services/hosting/request/ asking for project name, URL, source repo, and role.
- composes with: Not multiplicable - it is an allocation, not a tier. The value is scale per allocation: ~370 GB mean, 60 Gbps aggregate egress, three-city replication, and a Ceph-backed second tier (ftp2) with 21 TB already in use.
- reliability: Human-gated and OSS-only in practice (the form asks for a source code repository and a role such as maintainer). It is a good home for a legitimately large OSS release corpus and a bad fit for arbitrary bulk - there is no self-service path and capacity is finite and publicly rationed.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Three servers sit behind ftp.osuosl.org with a combined bandwidth capacity of 60 gigabits per second'; 'about 100 projects using around 37 TB of disk space, about 16 TB on the main mirrors and 21 TB on ftp2'
  - [2] 2026-10-21: request form requires project name, URL, source code repository, and role; 'Please give us a few days or a week to discuss and respond'
  - [3] 2026-10-21: 'Release files and package repositories served from mirrors in three cities'
- sources:
  - [1] https://osuosl.org/services/hosting/details/
  - [2] https://osuosl.org/services/hosting/request/
  - [3] https://osuosl.org/services/hosting/
