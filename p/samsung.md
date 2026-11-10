# Samsung Cloud

> samsung.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/samsung/ | JSON https://fshy.ajam.dev/api/v1/entity/samsung.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Samsung Cloud (storage, discontinued)

- `netdisk-pan/samsung-cloud-storage` | dead | evidence reported | binding retention-clamped | category phone-vendor cloud, dead
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.samsung.com/us/support/answer/ANS10003437/
- free tier: None. It was 15 GB for early Galaxy buyers, cut to 5 GB for new accounts, then discontinued. Gallery Sync and Drive migrated to Microsoft OneDrive | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: Not applicable, the service closed | source: [1]
- retention: Two-phase shutdown: Gallery Sync and Drive migrated by 2021-09-30, then the remaining sync. Samsung matched the old quota on OneDrive for one year only, after which OneDrive's 5 GB applies | days: 0 | source: [2]
- egress: Not applicable | metered: no | source: [1]
- identity: email | detail: a Samsung account, which now gives OneDrive and not Samsung storage
- interface: unknown
- limits:
  - retention-clamped (binding): the storage product was discontinued and migrated to OneDrive by 2021-09-30 [2]
- binding note: The storage product ended, so the retention clamp is total and there is no offer to test.
- tooling: none usable. Samsung's own support pages redirect the user to their personal OneDrive account
- composes with: Nothing to chain: it is now literally OneDrive on a 5 GB free tier. The 15 GB that older guides quote is a number that no longer exists
- reliability: Do not count this as a live 15 GB. The quota Samsung matched on OneDrive lasted one year and OneDrive's own 5 GB applied afterwards
- notes: Covers consumer Samsung Cloud device gallery storage, distinct from Samsung SDS enterprise cloud. Consumer file drive services and gallery sync were officially decommissioned in 2021 with data migrated to Microsoft OneDrive.
- extras:
  - access_mode: none
  - closed: 2021-09-30
  - replaced_by: OneDrive
  - aliases: Samsung Cloud
  - reserved_slug: samsung-cloud
  - cross_topic_record: compute/samsung-cloud
  - cross_topic_note: a different product from the same company: compute/samsung-cloud.json covers Samsung SDS Cloud Platform
- evidence:
  - [1] 2026-10-21: 'Your Gallery app can only be synced to your personal OneDrive account', so the Samsung-side storage is gone
  - [2] 2026-10-21: the migration deadline of 2021-09-30
  - [3] 2026-10-21: Samsung's own notice page, 'Sync with OneDrive ending soon'
  - [4] 2026-10-21: 'dozens of cloud storage companies have either given up on free cloud storage (e.g Samsung, Amazon and Ionos)'
- sources:
  - [1] https://www.samsung.com/us/support/answer/ANS10003437/
  - [2] https://www.androidcentral.com/samsung-cloud-users-have-until-september-30-migrate-data-onedrive
  - [3] https://www.samsungcloud.com/en/about/sync-with-onedrive-ending-soon
  - [4] https://www.techradar.com/pro/grab-1-54tb-free-cloud-storage-for-life-but-you-will-need-to-sign-up-43-services
