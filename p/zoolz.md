# zoolz

> zoolz.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zoolz/ | JSON https://fshy.ajam.dev/api/v1/entity/zoolz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zoolz Cloud Backup 12 TB

- `storage/zoolz-cloud-backup-12-tb` | qualifies-with-caveat | evidence reported | binding none | category Cold-storage backup, subscription (lifetime SKUs exist via deal sites)
- needs card yes, phone no, ID no, institution no | verified 2026-11-01T18:05:08.101Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zoolz.com/pricing/
- price $2.78/TB at 12 TB ($399.99/yr = $33.33/mo); $2.86/TB at 7 TB ($239.99/yr); $2.67/TB at 2.5 TB ($79.99/yr). Cold tier only. | parsed USD 2.67/TB-mo
- free tier: 2.5 TB (2 TB cold + 500 GB hot) $79.99/yr; 7 TB (6 TB cold + 1 TB hot) $239.99/yr; 12 TB (10 TB cold + 2 TB hot) $399.99/yr; 24 TB (20 TB cold + 4 TB hot) $759.99/yr | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published as a fee; cold-tier retrieval is the practical cost and is not quantified on the pricing page | metered: no
- identity: card | detail: the sign-up form asks for a full name, email address, password, company name, country and a license key, and the trial it opens is 14 days. Payment is a card through a Stripe checkout, and the terms say a card on file is charged automatically on renewal. No phone field is on the form.
- interface: s3, webdav, rclone
- limits note: Constraint type: write-gated. Cold storage means the restore is a request workflow. File upload size 20 GB on the small tier.
- interface detail: Windows client, S3-ish 'Instant Vault' for the hot portion
- tooling: no rclone/WebDAV found for the cold tier
- composes with: Poor. Cold tier is restore-on-request, not a filesystem.
- reliability: Same corporate family as Polarbackup, which revoked paid lifetime deals outright. Zoolz's own $34.99-$49.99 '1 TB lifetime' SKUs sold through Cult of Mac / BleepingComputer / Mashable stacks are the classic revocable instrument.
- notes: 2.5 TB (2 TB cold + 500 GB hot) $79.99/yr; 7 TB (6+1) $239.99/yr; 12 TB (10 cold + 2 hot) $399.99/yr
- extras:
  - price_verbatim: $2.78/TB at 12 TB ($399.99/yr = $33.33/mo); $2.86/TB at 7 TB ($239.99/yr); $2.67/TB at 2.5 TB ($79.99/yr). Cold tier only.
- evidence:
  - [1] 2026-10-21: 'Zoolz Cloud Backup 12 TB ... 10 TB Cold Storage + 2 TB Hot Storage ... $399.99 Yearly'
  - [2] 2026-10-21: sister-brand lifetime revocation
  - [3] 2026-10-21: '$34.99 ... 1TB Lifetime'
  - [4] 2026-11-01: the sign-up form's fields, and that the trial it opens runs 14 days | capture: sha256:1a6693bb39845f3ac2e35905724837ba9c0036eb4a73288ac85c462ba61d4e25 | quote: To start your FREE 14-day trial, please fill in the form: ... Full Name ... Email Address ... Password ... Company Name ... License Key
  - [1] 2026-11-01: the cold and hot split of the 12 TB plan and the price of the 24 TB plan | capture: sha256:2d13b4d550ffe7dd64e07eafc00b9ef670a3f7b78bdc41a6d44ab3775571bf9f | quote: 10 TB Cold Storage + 2 TB Hot Storage ... $ 399.99 Yearly ... 20 TB Cold Storage + 4 TB Hot Storage ... $ 759.99 Yearly
  - [1] 2026-11-01: the 12 TB plan is still listed at $399.99 a year, 10 TB cold and 2 TB hot | capture: sha256:2d13b4d550ffe7dd64e07eafc00b9ef670a3f7b78bdc41a6d44ab3775571bf9f | quote: Zoolz Cloud Backup 12 TB ... 10 TB Cold Storage + 2 TB Hot Storage ... $ 399.99 Yearly
- sources:
  - [1] https://zoolz.com/pricing/
  - [2] https://consumerrights.wiki/w/PolarBackup_-_Cloud_Storage
  - [3] https://deals.cultofmac.com/sales/zoolz-1tb-cold-storage-lifetime-subscription
  - [4] https://cloud2.zoolz.com/Signup

## zoolz

- `storage/zoolz` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zoolz.com/pricing/
- free tier: none reachable: no free tier remains; the pricing page opens directly on paid plans (2.5 TB at $79.99/year). Same corporate family as PolarBackup; its own 'important message for Zoolz Home users' blog post | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: paid
  - dead_end.why: no free tier remains; the pricing page opens directly on paid plans (2.5 TB at $79.99/year). Same corporate family as PolarBackup; its own 'important message for Zoolz Home users' blog post
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: no free tier remains; the pricing page opens directly on paid plans (2.5 TB at $79.99/year). Same corporate family as PolarBackup; its own 'important message for Zoolz Home users' blog post
  - [2] 2026-10-21: cited as the basis of the rejection: no free tier remains; the pricing page opens directly on paid plans (2.5 TB at $79.99/year). Same corporate family as PolarBackup; its own 'important message for Zoolz Home users' blog post
- sources:
  - [1] https://zoolz.com/pricing/
  - [2] https://blog.zoolz.com/.../an-important-message-for-zoolz-home-users/

## zoolz lifetime

- `storage/zoolz-lifetime` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://zoolz.com/pricing/
- free tier: None reachable: No lifetime product survives on the pricing page. zoolz.com/pricing/ now shows only Monthly/Yearly toggles with a '30% Off Yearly Plans' banner. No one-time option. Zoolz's historical lifet. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: No lifetime product survives on the pricing page. zoolz.com/pricing/ now shows only Monthly/Yearly toggles with a '30% Off Yearly Plans' banner — no one-time option. Zoolz's historical…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No lifetime product survives on the pricing page. zoolz.com/pricing/ now shows only Monthly/Yearly toggles with a '30% Off Yearly Plans' banner — no one-time option. Zoolz's historical…
- sources:
  - [1] https://zoolz.com/pricing/
