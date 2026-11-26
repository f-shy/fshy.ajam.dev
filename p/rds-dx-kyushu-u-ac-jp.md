# gakunin rdm

> rds.dx.kyushu-u.ac.jp | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rds-dx-kyushu-u-ac-jp/ | JSON https://fshy.ajam.dev/api/v1/entity/rds-dx-kyushu-u-ac-jp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gakunin rdm (nii, japan) standard storage

- `storage/gakunin-rdm-standard-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:39.184Z (live) | stale on 2026-12-04
- url https://rds.dx.kyushu-u.ac.jp/en/gakunin_rdm
- disagrees on identity_kind: `storage/gakunin-rdm` says institution, `storage/gakunin-rdm-standard-storage` says email
- disagrees on verdict: `storage/gakunin-rdm` says dead, `storage/gakunin-rdm-standard-storage` says fails-quota
- free tier: none reachable: 100 GB per user and <5 GB per file on NII Storage, consumed from the project creator's allowance, and access requires a Japanese institutional GakuNin account ('本学構成員（広大IDを有する方）'). Below… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 100 GB per user and <5 GB per file on NII Storage, consumed from the project creator's allowance, and access requires a Japanese institutional GakuNin account ('本学構成員（広大IDを有する方）'). Below…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 100 GB per user and <5 GB per file on NII Storage, consumed from the project creator's allowance, and access requires a Japanese institutional GakuNin account ('本学構成員（広大IDを有する方）'). Below…
  - [2] 2026-10-21: cited as the basis of the rejection: 100 GB per user and <5 GB per file on NII Storage, consumed from the project creator's allowance, and access requires a Japanese institutional GakuNin account ('本学構成員（広大IDを有する方）'). Below the
  - [1] 2026-11-19: the first-party page still states the 100 GB per user / <5 GB per file NII Storage limits | capture: sha256:8ac8fc3886cd84f79751b2b81f4b7ded118cc7bf578c98b6caeca5ad9b6ef7b2 | quote: NII Storage is limited to 100 GB per user and less than 5 GB per file
- sources:
  - [1] https://rds.dx.kyushu-u.ac.jp/en/gakunin_rdm
  - [2] https://support.rdm.nii.ac.jp/en/faq/

## gakunin rdm (nii, japan)

- `storage/gakunin-rdm` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:44.552Z (live) | stale on 2026-12-04
- url https://rds.dx.kyushu-u.ac.jp/en/gakunin_rdm
- disagrees on identity_kind: `storage/gakunin-rdm` says institution, `storage/gakunin-rdm-standard-storage` says email
- disagrees on verdict: `storage/gakunin-rdm` says dead, `storage/gakunin-rdm-standard-storage` says fails-quota
- free tier: none reachable: Allocation is 100 GB per user with a 5 GB per-file cap on NII Storage. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: re-checked in Japanese and the numbers…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: re-checked in Japanese and the numbers ar
  - [2] 2026-10-21: re-checked in Japanese and the numbers ar
  - [2] 2026-11-19: access requires an institutional authentication account | capture: sha256:d0ba89c10ef91405aa867e1b47a730b0c0d55708c718b799a43e1cfa8340ab81 | quote: You can log in to GakuNin RDM from your institution's common authentication system by accessing https://rdm.nii.ac.jp/ and selecting your institution's name from the pull-down menu in the upper right corner
  - [1] 2026-11-19: the storage allocation is 100 GB per user with a 5 GB per-file cap | capture: sha256:8ac8fc3886cd84f79751b2b81f4b7ded118cc7bf578c98b6caeca5ad9b6ef7b2 | quote: NII Storage is limited to 100 GB per user and less than 5 GB per file.
- sources:
  - [1] https://rds.dx.kyushu-u.ac.jp/en/gakunin_rdm
  - [2] https://support.rdm.nii.ac.jp/en/faq/
