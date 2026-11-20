# MEGA

> mega.io | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mega/ | JSON https://fshy.ajam.dev/api/v1/entity/mega.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MEGA S4 (object storage)

- `storage/mega-s4` | qualifies | evidence reported | binding none | category S3-compatible object storage, pay-as-you-grow
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-10T00:50:25.162Z (live) | stale on 2026-11-25
- url https://mega.io/objectstorage
- price $4.94/TB at 5 TB (EUR 22.00 = $24.71); $4.18/TB at 20 TB (EUR 74.50 = $83.69) | parsed USD 4.18/TB-mo
- free tier: €3.50 per TB a month on our pay-as-you-grow plan, with 3 TB included from €15. | unit: TB | metered on: unstated | read on: 2026-11-09 | source: [1] | note: Grow from gigabytes to petabytes, with no upper limit.
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Vendor terms state: '5x free egress, no API charges and no minimum storage period.' Documentation specifies that MEGA S4 allows up to 5x the average monthly stored data as free egress. | metered: no | free allowance: 100 TB per month
- identity: card | detail: the MEGA account is created with an email address and a password, confirmed by a link MEGA emails, and the vendor's guide lists no phone field, so whether the form asks a phone number is unverified. MEGA S4 is sold on the Pro Flexi plan, and the upgrade takes Visa or Mastercard, Google Pay, Bitcoin or a UnionPay bank card
- interface: s3-compatible, rclone, cli
- limits note: None on object size published. Egress beyond 5x stored is metered and charged.
- interface detail: S3-compatible (SigV4). Endpoint probed live: https://s3.eu-amsterdam-1.megas4.com/ returns HTTP 400 with {Code:InvalidRequest, Message:'Please use AWS Signature Version 4 for authentication'}. A real, correctly-implemented S3 endpoint, not a marketing page.
- tooling: rclone (first-party guide), AWS CLI, Synology Hyper Backup, TrueNAS, Duplicacy, MSP360, Cyberduck, Terraform
- composes with: Native S3 -> any S3 client; first-party Cloudflare CDN guide documented at help.mega.io/megas4/setup-guides/cloudflare-setup-guide-for-mega-s4
- reliability: MEGA has run since 2013; S4 is a newer product line (2025) so the durability record on S4 itself is short. Brand-level: no mass data-loss event. Note the 2013 MEGA breach was credential/architecture, not storage loss.
- notes: No upper limit. Base 3 TB included from EUR 15/mo; EUR 3.50 per additional TB.
- evidence note: the same as the free tier
- extras:
  - price_verbatim: $4.94/TB at 5 TB (EUR 22.00 = $24.71); $4.18/TB at 20 TB (EUR 74.50 = $83.69)
- evidence:
  - [1] 2026-10-21: 'EUR 3.50 per TB a month on our pay-as-you-grow plan, with 3 TB included from EUR 15. 5x free egress, no API charges and no minimum storage period.'
  - [2] 2026-10-21: HTTP 400 SigV4 error, endpoint live
  - [3] 2026-10-21: first-party rclone guide
  - [4] 2026-10-21: 'MEGA S4 allows up to 5x of the average monthly stored data as free egress'
  - [5] 2026-11-01: the paid plan is bought with a Visa or Mastercard, whatever the free account needs | capture: sha256:fea7a7fa62c0b74d0d838ae3df770839e9019458757221ffc0486f6670d7520b | quote: - Visa and Mastercard (If you don’t see this option, then it is not available in your country)
  - [6] 2026-11-01: the MEGA account is created with an email address and a confirmation link | capture: sha256:dc2bc16ed134c8cb045193a0d35d62e36f8257f8ef9335a1c1a2085219e9dd56 | quote: Please use an email address where you can receive our confirmation link
  - [1] 2026-11-01: S4 is sold on the Pro Flexi plan, so the paid rail is the identity cost | capture: sha256:5c85afe545e831793d950dc6c3eea690a10ff0f845d23c85e43cadd33a1cda66 | quote: €3.50 per TB a month on our pay-as-you-grow plan, with 3 TB included from €15.
  - [1] 2026-11-09: the pricing page states €3.50 per TB a month with 3 TB included from €15 | capture: sha256:5c85afe545e831793d950dc6c3eea690a10ff0f845d23c85e43cadd33a1cda66 | quote: €3.50 per TB a month on our pay-as-you-grow plan, with 3 TB included from €15.
  - [1] 2026-11-09: the page states the service grows with no upper limit | capture: sha256:5c85afe545e831793d950dc6c3eea690a10ff0f845d23c85e43cadd33a1cda66 | quote: Grow from gigabytes to petabytes, with no upper limit.
- sources:
  - [1] https://mega.io/objectstorage
  - [2] https://s3.eu-amsterdam-1.megas4.com/
  - [3] https://help.mega.io/megas4/setup-guides/rclone-setup-guide-for-mega-s4
  - [4] https://mega.io/objectstorage/developer-automation-storage
  - [5] https://help.mega.io/plans-storage/payments-billing/how-to-upgrade
  - [6] https://help.mega.io/accounts/create-account/how-to-create-a-mega-account

## MEGA

- `storage/mega` | qualifies-with-caveat | evidence reported | binding retention-clamped | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:01.147Z (live) | stale on 2026-12-04
- url https://mega.io/
- free tier: MEGA offers 20 GB of free encrypted cloud storage. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: With MEGA’s unlimited file size, no file is ever too big. | source: [1] | note: not stated
- retention: Achievements are valid for 365 days. | days: 365 | source: [1] | note: not stated
- egress: For non-MEGA users, or those with a free account, the amount of data that can be downloaded from your IP address in six hours is limited. | metered: yes
- identity: email
- interface: s3-compatible, rest, rclone, cli
- limits:
  - per-ip-shaping: The limit is based on the amount of data downloaded from your IP address over the past six hours. [1]
  - retention-clamped (binding): Achievements are valid for 365 days. [1]
  - write-gated: Complete one of the following actions to earn more free storage. [1]
- limits note: Transfer quota is calculated per IP address over 6-hour windows on free accounts. Bonus storage achievements expire after 365 days. Client-side encryption is enforced across uploads.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Native rclone backend 'mega' (Tier 2, v1.41+); official MEGAcmd CLI; MEGA S4 (S3-compatible) is the paid object store.
- composes with: 20 GB + N x 5 GB achievements per account, x unlimited free accounts. Achievement bonuses are per-account and do NOT compound within one account beyond one of each, so the multiplication is accounts, not achievements.
- reliability: Does not lose data; throttles hard per IP and per link. Accounts with no login for ~3 months are at risk of quota cuts.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Get 20 GB free storage with MEGA's secure encrypted cloud storage' (meta description) and body 'MEGA offers 20 GB of free storage'
  - [2] 2026-10-21: (archive 20260215) — 'Get 5 GB of free storage when you install our MEGA app... Valid for 365 days' for each of desktop, mobile, invite, VPN trial, Pass trial; 'Achievement bonuses stack'
  - [3] 2026-10-21: (archive 20250519) — 'For free account holders or non-MEGA users... The limit is based on the amount of data downloaded from your IP address over the past six hours.'
  - [4] 2026-10-21: native Mega backend, Tier 2
  - [1] 2026-11-09: the storage page states 20 GB of free storage | capture: sha256:64ff926559dc859024a3167ed474af0807c7b3c66f1a0ac2c6a19d6915a5b917 | quote: MEGA offers 20 GB of free encrypted cloud storage.
  - [1] 2026-11-09: the storage page states there is no file-size cap | capture: sha256:64ff926559dc859024a3167ed474af0807c7b3c66f1a0ac2c6a19d6915a5b917 | quote: With MEGA’s unlimited file size, no file is ever too big.
  - [2] 2026-11-09: the achievements page states the 365-day validity | capture: sha256:d6874d7cbf74e83b11e6520f02d957cee1e486aea0ff2f249aba0b0be9d4830b | quote: Achievements are valid for 365 days.
  - [3] 2026-11-09: the help page states the per-IP six-hour basis of the transfer limit | capture: sha256:d51c59dcfb62da5896a6a72002bebd61fbc5cf20c01b97863bbb177c2446dde4 | quote: The limit is based on the amount of data downloaded from your IP address over the past six hours.
  - [2] 2026-11-09: the achievements page states the actions that add free storage | capture: sha256:d6874d7cbf74e83b11e6520f02d957cee1e486aea0ff2f249aba0b0be9d4830b | quote: Complete one of the following actions to earn more free storage.
  - [3] 2026-11-09: the help page states the download limit for free and non-account users | capture: sha256:d51c59dcfb62da5896a6a72002bebd61fbc5cf20c01b97863bbb177c2446dde4 | quote: For non-MEGA users, or those with a free account, the amount of data that can be downloaded from your IP address in six hours is limited.
  - [1] 2026-11-19: the storage page states the 20 GB free tier | capture: sha256:64ff926559dc859024a3167ed474af0807c7b3c66f1a0ac2c6a19d6915a5b917 | quote: MEGA offers 20 GB of free encrypted cloud storage.
  - [1] 2026-11-19: the storage page states there is no file-size cap | capture: sha256:64ff926559dc859024a3167ed474af0807c7b3c66f1a0ac2c6a19d6915a5b917 | quote: With MEGA’s unlimited file size, no file is ever too big.
  - [2] 2026-11-19: the achievements page states the 365-day validity | capture: sha256:d6874d7cbf74e83b11e6520f02d957cee1e486aea0ff2f249aba0b0be9d4830b | quote: Achievements are valid for 365 days.
  - [2] 2026-11-19: the achievements page lists the actions that add free storage | capture: sha256:d6874d7cbf74e83b11e6520f02d957cee1e486aea0ff2f249aba0b0be9d4830b | quote: Complete one of the following actions to earn more free storage.
  - [3] 2026-11-19: the help page states the per-IP six-hour basis of the transfer limit | capture: sha256:d51c59dcfb62da5896a6a72002bebd61fbc5cf20c01b97863bbb177c2446dde4 | quote: The limit is based on the amount of data downloaded from your IP address over the past six hours.
  - [3] 2026-11-19: the help page states the download limit for free and non-account users | capture: sha256:d51c59dcfb62da5896a6a72002bebd61fbc5cf20c01b97863bbb177c2446dde4 | quote: For non-MEGA users, or those with a free account, the amount of data that can be downloaded from your IP address in six hours is limited.
  - [4] 2026-11-19: rclone documents a native Mega backend | capture: sha256:17764d26cd5daa08f20e87c048484d063eeb7d5dd1d64d4edf0abadd1ab2598c | quote: This is an rclone backend for Mega which supports the file transfer features of Mega using the same client side encryption.
- sources:
  - [1] https://mega.io/storage
  - [2] https://mega.io/achievements
  - [3] https://help.mega.io/plans-storage/space-storage/transfer-quota
  - [4] https://rclone.org/mega/

## mega pro i/ii/iii as a per-tb play

- `storage/mega-pro-i-ii-iii-as-a-per-tb-play` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:14.243Z (live) | stale on 2026-12-04
- url https://mega.io/pricing
- free tier: none reachable: Pro III plan provides 16 TB storage for EUR 29.99 per month. MEGA S4 line provides object storage pricing separately. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Pro III is 16 TB for EUR 29.99/mo, and MEGA's own comparison strip advertises 'MEGA 1.25*…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Pro III is 16 TB for EUR 29.99/mo, and MEGA's own comparison strip advertises 'MEGA 1.25* pe
  - [2] 2026-10-21: Pro III is 16 TB for EUR 29.99/mo, and MEGA's own comparison strip advertises 'MEGA 1.25* pe
  - [1] 2026-11-19: MEGA still prices Pro III per TB, now at 1.25 per TB per month | capture: sha256:bef944f215466e03f3952c7706b47c69a2c123b78addbf756418999e524a343f | quote: 1.25 * per TB per month *Based on the Pro III yearly plan
  - [1] 2026-11-19: the paid Pro plans top out at 20 TB, so the paid per-TB record is still accurate | capture: sha256:bef944f215466e03f3952c7706b47c69a2c123b78addbf756418999e524a343f | quote: Up to 20 TB
- sources:
  - [1] https://mega.io/pricing
  - [2] https://www.capterra.com/p/232384/MEGA/pricing/
