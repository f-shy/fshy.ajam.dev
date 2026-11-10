# InfiniCLOUD

> infini-cloud.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/infini-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/infini-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InfiniCLOUD (formerly TeraCLOUD)

- `storage/infinicloud` | fails-quota | evidence reported | binding retention-clamped | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://infini-cloud.net
- free tier: 20 GB free account; referral bonus up to 1,000 GB for the referrer (+5 GB once for the referee). No file size limit | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 'Writing Feature' is disabled on the free plan (no version history); 2 years of inactivity deletes the account; referrer bonuses are valid one year only; 'Malicious or spam referrals may lead to account suspension or deletion' | days: 730 | source: [1] | note: not stated
- egress: no per-GB egress charge or transfer quota published on the plan table; free tier capped at 200 Mbps | metered: no
- identity: email
- interface: webdav, rclone
- limits:
  - per-ip-shaping: speed capped at 200 Mbps per account [1]
  - retention-clamped (binding): expire after 2 years [1]
- limits note: 'Writing Feature' is disabled on the free plan (no version history); 2 years of inactivity deletes the account; referrer bonuses are valid one year only; 'Malicious or spam referrals may lead to account suspension or deletion'
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: webdav
- tooling: WebDAV endpoint (rclone/webdav, davfs, any WebDAV client); recurring 20 GB plan is free forever, 2-year inactivity expiry
- composes with: 20 GB + 5 GB per account is small, but the referrer side scales to 1,000 GB per account, so a group of accounts that refer each other accumulates ~1 TB per account. The allowance is per account, so N accounts hold N x ~1 TB
- reliability: referral bonuses expire after a year for the referrer; free accounts silently expire after 2 years idle; Japanese-operated, speed capped at 200 Mbps per account
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB free account; referral bonus up to 1,000 GB for the referrer (+5 GB once for the referee). No file size limit
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Capacity 20GB | Free', 'File Size Limit None', 'Referral Bonus 〇 (Up to 1,000GB)', 'Account Expiration 2 Years of inactivity'
  - [2] 2026-10-21: 'Referring User Up to 1TB (1,000GB)... Earn 2GB for each person you refer. Bonus storage is valid for one year', referred user 5 GB, last updated 2025-06-20
  - [3] 2026-10-21: probe: PROPFIND (Depth: 0, no creds) -> 405 Method Not Allowed (WebDAV listener live, rejects unauthenticated PROPFIND)
- sources:
  - [1] https://infini-cloud.net/en/pricing.html
  - [2] https://infini-cloud.net/en/about_introduce.html
  - [3] https://webdav.infini-cloud.net/
