# Degoo

> degoo.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/degoo/ | JSON https://fshy.ajam.dev/api/v1/entity/degoo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## degoo

- `storage/degoo` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:11.233Z (live) | stale on 2026-12-05
- url https://degoo.com/
- free tier: 20 GB of cloud space on the free plan, 3 devices, 90 days account inactivity; paid plans: Pro 500 GB at $2.99 / 1 month, Ultimate 5000 GB at $9.99 / 1 month | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: free plan: 90 days account inactivity; Pro and Ultimate plans: files stored forever | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 20 GB of cloud space on the free plan [1]
  - retention-clamped: 90 days account inactivity on the free plan [1]
- binding note: the free plan holds 20 GB; Pro is 500 GB and Ultimate is 5000 GB on paid plans
- interface detail: not documented
- tooling: rclone feature request 4424 asks for a Degoo backend and its maintainer would support a contributor who maintains a reverse-engineered backend; the vendor offers a web app at app.degoo.com
- composes with: not recorded
- reliability: free plan: 20 GB of cloud space, 3 devices, 90 days account inactivity
- notes: free plan: 20 GB of cloud space, 3 devices, 90 days account inactivity; Pro 500 GB at $2.99 / 1 month; Ultimate 5000 GB at $9.99 / 1 month
- evidence note: https://degoo.com/, re-read on 2026-11-03, lists the 20 GB free plan, 90 days account inactivity, and Ultimate at 5000 GB. The rclone issue page was re-read on the same date. The identity_cost row remains a default, not a page reading.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free tier is 20 GB today (was 100 GB), 3 devices, 90-day inactivity deletion. No rclone backend — feature request issue #4424 has been open since 2020; only third-party cligoo/degoo-api-js.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free tier is 20 GB today (was 100 GB), 3 devices, 90-day inactivity deletion. No rclone backend — feature request issue #4424 has been open since 2020; only third-party cligoo/degoo-api-js.
  - [2] 2026-10-21: cited as the basis of the rejection: Free tier is 20 GB today (was 100 GB), 3 devices, 90-day inactivity deletion. No rclone backend — feature request issue #4424 has been open since 2020; only third-party cligoo/degoo-api-js.
  - [1] 2026-11-03: the Free plan holds 20 GB of cloud space | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: # 20 GB
  - [1] 2026-11-03: the free plan lists 90 days account inactivity | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: 90 days account inactivity
  - [2] 2026-11-03: the rclone maintainer would accept a reverse-engineered Degoo backend that a contributor maintains | capture: sha256:9e7abc90fb547e80fc2c02caf3ab90ade778f1043985ee9beceda48b94f72454 | quote: If someone wants to have a go then I'd be supportive, but with the caveat that that person would need to maintain the backend indefinitely as reverse engineered backends are much harder work to look after.
  - [1] 2026-11-03: the paid plans list files stored forever | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: Files stored forever
  - [1] 2026-11-04: the free plan lists 90 days account inactivity | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: 90 days account inactivity
  - [1] 2026-11-04: the largest plan on the vendor page is Ultimate at 5000 GB | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: Ultimate 5000 GB cloud space Unlimited devices
  - [2] 2026-11-04: the rclone maintainer would accept a maintained reverse-engineered Degoo backend | capture: sha256:9e7abc90fb547e80fc2c02caf3ab90ade778f1043985ee9beceda48b94f72454 | quote: If someone wants to have a go then I'd be supportive, but with the caveat that that person would need to maintain the backend indefinitely
- sources:
  - [1] https://degoo.com/
  - [2] https://github.com/rclone/rclone/issues/4424

## Degoo Ultimate 5 TB

- `storage/degoo-ultimate-5-tb` | fails-quota | evidence reported | binding per-object-cap | category Encrypted backup drive
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T01:24:11.232Z (live) | stale on 2026-11-19
- url https://degoo.com/
- price $2.00/TB-month on Ultimate ($9.99 / 1 month for 5000 GB); Pro is $5.98/TB-month ($2.99 for 500 GB). No plan above 5000 GB is listed, so 10 TiB is not reachable on one account. | parsed USD 2/TB-mo
- free tier: Free 20 GB cloud space; Pro 500 GB ($2.99 / 1 month); Ultimate 5000 GB ($9.99 / 1 month). No plan above 5000 GB is listed. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: unverified: the vendor page lists no transfer or egress term for any plan. | metered: no
- identity: card | detail: card
- interface: unknown
- limits:
  - per-object-cap (binding): 5 TB cap [1]
  - write-gated: review Documented history of revoked lifetime deals and lost data [1]
- limits note: Constraint type: write-gated/pull-count. Upload and restore speeds are the complaint in every review.
- interface detail: Web/app only. No WebDAV, no rclone, no S3 found.
- tooling: None. This is the disqualifier for a programmatic workload.
- composes with: none
- reliability: Documented history of revoked lifetime deals and lost data. r/DataHoarder: 'DO NOT GIVE THEM ANY OF THEIR MONEY'; the 10 TB/$99 StackSocial lifetime is cited as the canonical example of the model failing. A 5 TB cap also makes it useless for 20 TB.
- notes: Free 20 GB; Pro 500 GB; Ultimate 5 TB. Third-party trackers put Ultimate at $9.99/mo.
- evidence note: https://degoo.com/, re-read on 2026-11-03, lists Ultimate at 5000 GB for $9.99 a month as the largest plan. The card identity cost and the 5 TB per-object cap are not stated on that page, and the write-gated limit row cites no quote, so the rung stays reported.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free 20 GB; Pro 500 GB; Ultimate 5 TB. Third-party trackers put Ultimate at $9.99/mo.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $2.00/TB at 5 TB ($9.99). No 20 TB tier exists — hard ceiling at 5 TB.
- evidence:
  - [1] 2026-10-21: 'Free 20 GB ... Pro 500 GB ... Files stored forever'
  - [2] 2026-10-21: 'DO NOT GIVE THEM ANY OF THEIR MONEY'
  - [3] 2026-10-21: 10 TB Degoo lifetime at $99 via StackSocial, community reaction
  - [1] 2026-11-03: the Ultimate 5000 GB plan is $9.99 per month | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: $9.99 / 1 month
  - [1] 2026-11-03: the largest plan on the vendor page is Ultimate at 5000 GB, below the 10 TiB stored need | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: Ultimate 5000 GB cloud space Unlimited devices
  - [1] 2026-11-03: the plan features list only the app and web app as access routes | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: Access and manage your files in our web app.
  - [1] 2026-11-04: the largest plan on the vendor page is Ultimate at 5000 GB | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: Ultimate 5000 GB cloud space Unlimited devices
  - [1] 2026-11-04: the Ultimate 5000 GB plan is $9.99 per month | capture: sha256:798883fb383daac2481c4b0e874bb0c2a919c3075bab650f283cc77aa4ccf034 | quote: $9.99 / 1 month
- sources:
  - [1] https://degoo.com/
  - [2] https://www.reddit.com/r/DataHoarder/comments/cb2x1j/
  - [3] https://www.reddit.com/r/DataHoarder/comments/138xb40/

## Degoo — 20 GB free + referral ladder

- `storage/degoo-20-gb-free-referral-ladder` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://degoo.com
- free tier: 20 GB free, plus 5 GB referral bonus and 250 MB per referred friend. Paid: 500 GB $2.99/mo, 5000 GB Ultimate. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: '90 days account inactivity' listed as a free-plan term. Inactive accounts are reclaimed. | days: 90 | source: [1] | note: not stated
- egress: Not stated on the plan page. Free tier is ad-supported. | metered: no
- identity: email | detail: email
- interface: rest, rclone
- limits note: 20 GB free. '90 days account inactivity' listed as a free-plan term. Inactive accounts are reclaimed. 1,000-file warning threshold on free.
- interface detail: rest
- tooling: No mainline rclone backend. Third-party desktop client only; web + mobile apps.
- composes with: Storage allowance is 20 GB per registered account, requiring account multiplication to aggregate capacity.
- reliability: Actively dangerous reputation: Cloudwards documents 'plenty of users have reported losing data or having their accounts deactivated — even if they have the old lifetime subscription'. Do not put anything here you cannot lose.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 20 GB free, plus 5 GB referral bonus and 250 MB per referred friend. Paid: 500 GB $2.99/mo, 5000 GB Ultimate.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free 20 GB cloud space ... 5 GB referral bonus, 250 MB per referred friend ... 90 days account inactivity', fetched 2026-10-21
  - [2] 2026-10-21: 'plenty of users have reported losing data or having their accounts deactivated — even if they have the old lifetime subscription'
- sources:
  - [1] https://degoo.com/
  - [2] https://www.cloudwards.net/review/degoo/
