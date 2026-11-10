# Icedrive

> icedrive.net | Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/icedrive/ | JSON https://fshy.ajam.dev/api/v1/entity/icedrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Icedrive 3 TB

- `storage/icedrive-3-tb` | qualifies-with-caveat | evidence reported | binding none | category E2E-encrypted cloud drive (lifetime option)
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://icedrive.net/plans
- price $3.33/TB/mo at 3 TB ($9.99). Lifetime 2 TB at $499 one-time = $1.04/TB/mo over 20 years, $2.08/TB/mo over 10 years, $4.16/TB/mo over 5 years. 20 TB is not offered — the ladder stops at 3 TB, so this cannot host the archive. | parsed USD 3.33/TB-mo
- free tier: 3 TB; $9.99/mo or $119.88/yr | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered on the plan page; 'Larger public transfers' is listed as a paid-tier feature without a published cap. | metered: yes
- identity: card | detail: card via Stripe (GBP/USD/EUR)
- interface: webdav, rclone
- limits note: 'Larger public transfers' implies a public-transfer cap that is not published numerically. Unverifiable.
- interface detail: rclone (Icedrive is a supported backend), WebDAV via third party
- tooling: part of interface detail
- composes with: rclone; lifetime plans
- reliability: Twofish client-side encryption means every read costs local CPU. Public-transfer cap unpublished.
- notes: the same as the free tier
- extras:
  - price_verbatim: $3.33/TB/mo at 3 TB ($9.99). Lifetime 2 TB at $499 one-time = $1.04/TB/mo over 20 years, $2.08/TB/mo over 10 years, $4.16/TB/mo over 5 years. 20 TB is not offered — the ladder stops at 3 TB, so this cannot host the archive.
- evidence:
  - [1] 2026-10-21: '3 TB … Save $36.00 / year … $9.99/mo … $119.88 billed yearly … Secure checkout powered by Stripe'; 'Larger public transfers' as a paid feature
  - [2] 2026-10-21: 'Lifetime Personal 500 GB … $344 $229 One-time payment'; 'Lifetime Personal+ 2 TB … $749 $499 One-time payment'
- sources:
  - [1] https://icedrive.net/plans
  - [2] https://icedrive.net/lifetime-plans

## Icedrive Lifetime Personal+ 2 TB

- `storage/icedrive-lifetime-personal-2-tb` | qualifies-with-caveat | evidence reported | binding retention-clamped | category E2EE cloud drive, lifetime one-time
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://icedrive.net/lifetime-plans
- price One-time $249.50/TB at 2 TB ($499). Over 5 years: $4.16/TB/mo. Over 10 years: $2.08/TB/mo. Expensive relative to pCloud at the same capacity.
- free tier: Lifetime Personal 500 GB $229 (list $344); Lifetime Personal+ 2 TB $499 (list $749). Growth is by 'stack' add-ons (1 TB / 5 TB) or by attaching a subscription. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Refund terms disagree between the lifetime page (30 days) and the provider (14 days). | days: 30 | source: [1] | note: not stated
- egress: No egress fee published. Vendor explicitly frames lifetime as 'Made for casual use — ideal for everyday uploads and access. Power users and heavier workloads may be better suited to a flexible subscription plan', which is a soft fair-use brake rather than a number. | metered: no
- identity: card | detail: card
- interface: webdav, rclone
- limits:
  - retention-clamped (binding): lifetime page (30 days [1]
- limits note: Stacks cannot be combined with each other arbitrarily. Icedrive community staff: 'Its not possible to stack lifetime plans on top of one another. Only by purchasing Stacks .. can you add more storage.' So the 2 TB entry point is a ceiling unless you buy 5 TB stacks.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: WebDAV + rclone generic; desktop/mobile apps; virtual drive on Windows
- tooling: WebDAV; no first-party rclone backend
- composes with: WebDAV -> local -> CDN
- reliability: No mass data-loss event documented. Pricing has churned violently across 2024-2026 (Black Friday $349 for 3 TB, then a $389 2 TB Core, now $499) which is a signal about unit economics, not integrity. Refund terms disagree between the lifetime page (30 days) and the provider (14 days).
- notes: the same as the free tier
- extras:
  - price_verbatim: One-time $249.50/TB at 2 TB ($499). Over 5 years: $4.16/TB/mo. Over 10 years: $2.08/TB/mo. Expensive relative to pCloud at the same capacity.
- evidence:
  - [1] 2026-10-21: 'Lifetime Personal+ 2 TB ... $749 $499 One-time payment'; '30-day money-back guarantee'; 'Ideal for everyday uploads and access. Power users and heavier workloads may be better suited to a flexible subscription plan'
  - [2] 2026-10-21: stacking restriction confirmed by staff
- sources:
  - [1] https://icedrive.net/lifetime-plans
  - [2] https://community.icedrive.net/t/lifetime-plans-should-not-stack-just-let-us-add-as-if-we-were-first-time/11031

## Icedrive — lifetime plans (direct)

- `storage/icedrive-lifetime-plans` | fails-egress | evidence reported | binding retention-clamped | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://icedrive.net/lifetime-plans
- disagrees on verdict: `storage/icedrive` says fails-quota, `storage/icedrive-lifetime-plans` says fails-egress
- free tier: Lifetime Personal 500 GB $229 (from $344); Lifetime Personal+ 2 TB $499 (from $749). One-time, 'No recurring renewal'. Live on the vendor page 2026-10-21. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 2 sync devices on lifetime, 14 days file versioning | days: 14 | source: [1] | note: not stated
- egress: Free-tier bandwidth is capped (TechRadar: 3 GB/day on free). Lifetime paid tiers not metered per-GB; sync-limited to 2 devices on lifetime. | metered: no
- identity: email | detail: email
- interface: rest, webdav, rclone
- limits:
  - retention-clamped (binding): lifetime, 14 days [1]
  - retention-clamped (binding): lifetime page but 14 days [1]
- limits note: 2 sync devices on lifetime, 14 days file versioning. Vendor explicitly says heavy sync/NAS workloads belong on subscriptions. I.e. the lifetime tier is throttled by device count, not bytes.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: rclone backend `icedrive`. Third-party clients exist; WebDAV is not native.
- composes with: $250/TB at 2 TB. No stacking. Lifetime tiers are fixed capacity.
- reliability: Gibraltar-registered ICE PRIVACY LTD, 30-day guarantee on the lifetime page but 14 days. Decide inside 14. Price discrepancy vs the 2026-10-17 audit ($699 for 2 TB) suggests the vendor page is running a deeper promo than third parties track.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Lifetime Personal 500 GB $229 (from $344); Lifetime Personal+ 2 TB $499 (from $749). One-time, 'No recurring renewal'. Live on the vendor page 2026-10-21.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Lifetime Personal+ 2 TB ... $749 $499 One-time payment', fetched 2026-10-21
  - [2] 2026-10-21: 'Icedrive, for example, has a 3GB per day limit' on free
- sources:
  - [1] https://icedrive.net/lifetime-plans
  - [2] https://www.techradar.com/pro/grab-1-54tb-free-cloud-storage-for-life-but-you-will-need-to-sign-up-43-services

## icedrive

- `storage/icedrive` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:03:51.459Z (live) | stale on 2026-12-04
- url https://icedrive.net/
- disagrees on verdict: `storage/icedrive` says fails-quota, `storage/icedrive-lifetime-plans` says fails-egress
- free tier: 10 GB of storage on a free account | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: free accounts inactive for 12 consecutive months may be removed, including content and data | source: [1]
- egress: free plan: a 50 GB 'Public transfer' allowance (a third-party tracker reports the September 2025 change from a 50 GB monthly bandwidth cap) | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 10 GB of storage on a free account [2]
- binding note: a free account holds 10 GB; larger capacity is on paid plans
- interface detail: not documented
- tooling: native Icedrive apps (desktop, mobile, web) are the vendor-recommended route; WebDAV was disabled for new users on 15 April 2026 and is being sunset for existing users; a third-party tracker lists no dedicated rclone backend; a third-party directory lists an S3 endpoint: unverified
- composes with: not recorded
- reliability: free accounts that remain inactive for 12 consecutive months may be removed, including content and data
- notes: 10 GB of storage on a free account; larger capacity is on paid plans
- evidence note: the egress allowance, rclone and S3 statements rest on the third-party pages https://www.mrplanb.com/storage/icedrive-free-plan and https://tech-from-europe.eu/product/icedrive
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: 10 GB free. Failed on both quota and the programmatic path: there is no rclone backend at all (generic webdav only, via a separately-issued WebDAV Access Key), and WebDAV was discontinued…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 10 GB free. Failed on both quota and the programmatic path: there is no rclone backend at all (generic webdav only, via a separately-issued WebDAV Access Key), and WebDAV was discontinued…
  - [3] 2026-10-21: cited as the basis of the rejection: 10 GB free. Failed on both quota and the programmatic path: there is no rclone backend at all (generic webdav only, via a separately-issued WebDAV Access Key), and WebDAV was discontinued fo
  - [4] 2026-10-21: cited as the basis of the rejection: 10 GB free. Failed on both quota and the programmatic path: there is no rclone backend at all (generic webdav only, via a separately-issued WebDAV Access Key), and WebDAV was discontinued fo
  - [1] 2026-11-03: the vendor home page offers 10GB free cloud storage at sign-up | capture: sha256:c8217b5e1913717742164e1599c25c058d320fd70675f79a3f72171b840ab740 | quote: And get 10GB FREE Cloud Storage
  - [2] 2026-11-03: a free account includes 10 GB of storage | capture: sha256:424ee8cb9926bc7f2b5682ffed4754124def87f85e6b3bdff3f96e86c14a4eb3 | quote: A free Icedrive account includes 10 GB of storage so you can try the service before choosing a paid plan.
  - [5] 2026-11-03: free accounts inactive for 12 consecutive months may be removed | capture: sha256:9137e3e8a567a3588da2b314613c198f992e2d6c7fa53174bc48f440b1cf1990 | quote: Free accounts that remain inactive for a period of 12 consecutive months may be removed from our system, including any associated content and data.
  - [4] 2026-11-03: a third-party tracker reports a 50 GB public transfer allowance on the free plan | capture: sha256:dad5013fde373adc6959e0d4e8736ea889bd0827461a113af2213b0a0340c469 | quote: Icedrive changed the free plan's stated allowance from a general 50 GB monthly bandwidth cap to a 50 GB 'Public transfer' allowance
  - [6] 2026-11-03: WebDAV is disabled for new users from 15 April 2026 | capture: sha256:a978b22f881199083efb439daa2169be48e78b3ced28ed4a554f502b029aa594 | quote: Important update (15 April 2026): WebDAV has been disabled for all new users as of this date and is being gradually sunset for existing users.
  - [4] 2026-11-03: a third-party tracker reports no dedicated rclone backend | capture: sha256:dad5013fde373adc6959e0d4e8736ea889bd0827461a113af2213b0a0340c469 | quote: | rclone | No dedicated backend [docs](https://rclone.org/) |
  - [3] 2026-11-03: a third-party directory lists an S3 endpoint and WebDAV discontinued for new users | capture: sha256:87cd1b3bc2d771cddfde7d5f16ad4fdaee4559852c0cb934ce6778bd1376f544 | quote: - WebDAV and S3 endpoint support (WebDAV discontinued for new users as of April 2026)
- sources:
  - [1] https://icedrive.net/
  - [2] https://icedrive.net/plans
  - [3] https://tech-from-europe.eu/product/icedrive
  - [4] https://www.mrplanb.com/storage/icedrive-free-plan
  - [5] https://icedrive.net/legal/terms-of-service
  - [6] https://icedrive.net/help/account/does-icedrive-support-webdav
