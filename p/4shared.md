# 4shared paid

> 4shared.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/4shared/ | JSON https://fshy.ajam.dev/api/v1/entity/4shared.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 4shared

- `storage/4shared` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:01.217Z (live) | stale on 2026-12-04
- url https://www.4shared.com/
- free tier: 15 GB free per account | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2048 MB per file | bytes: 2048000000 | source: [1] | note: not stated
- retention: 15 GB per account; 2048 MB per file (split larger files); max 30 subfolders per folder; free accounts deleted if not logged into for 180 days. | days: 180 | source: [1] | note: not stated
- egress: Free accounts get ad-supported downloads and no direct/hotlink embedding; direct downloads are a Premium feature ('Direct downloads (file embedding)' starts at the 100 GB / $14.99 per year tier). | metered: no
- identity: email
- interface: rest, webdav, rclone
- limits:
  - per-object-cap (binding): 2048 MB per file [1]
  - retention-clamped: deleted if not logged into for 180 days [1]
  - retention-clamped: deletes the account and all files after 180 days [1]
- limits note: 15 GB per account; 2048 MB per file (split larger files); max 30 subfolders per folder; free accounts deleted if not logged into for 180 days.
- interface detail: webdav
- tooling: WebDAV endpoint live at webdav.4shared.com; REST API at api.4shared.com / upload.4shared.com (v1_2, JSON+XML); rclone's generic webdav backend has a 4shared-specific fix upstream (commit 65eee67 'webdav: fix Open Range requests to fix 4shared mount').
- composes with: 15 GB x unlimited free accounts. Legacy accounts carry stored files; new-account free space is 15 GB.
- reliability: Free tier deletes the account and all files after 180 days of inactivity. That alone disqualifies it for a growing archive. Downloads are ad-gated unless you pay.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 15 GB free per account
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The space limit is 15 GB per account. Currently 4shared sets a 2048 MB size limitation per file'
  - [1] 2026-10-21: 'Your free account and all your files will only be removed from 4shared if you don't log into your account for 180 days'
  - [2] 2026-10-21: 'Direct downloads (file embedding)' only on paid plans (100 GB $14.99/yr)
  - [3] 2026-10-21: probe: OPTIONS -> 200, Allow: OPTIONS,PROPFIND,MKCOL,MOVE,PUT,DELETE,LOCK,UNLOCK — DAV is genuinely mounted
  - [3] 2026-10-21: probe: PROPFIND Depth:0 -> 405 (method accepted by Allow but rejected unauthenticated; auth required)
  - [4] 2026-10-21: REST API v1_2 with upload/search/api host split
  - [1] 2026-11-19: the first-party FAQ still states 15 GB per free account | capture: sha256:c020a6b2899557b8a984085bf59f8922abecd2958c53725f5cc17475636a8f42 | quote: The space limit is 15 GB per account.
  - [1] 2026-11-19: the first-party FAQ still states a 2048 MB per-file cap | capture: sha256:c020a6b2899557b8a984085bf59f8922abecd2958c53725f5cc17475636a8f42 | quote: Currently 4shared sets a 2048 MB size limitation per file. Your files must not exceed the limit, or they will be rejected.
  - [1] 2026-11-19: the first-party FAQ still states the 180-day inactivity deletion | capture: sha256:c020a6b2899557b8a984085bf59f8922abecd2958c53725f5cc17475636a8f42 | quote: Your free account and all your files will only be removed from 4shared if you don't log into your account for 180 days.
  - [1] 2026-11-19: the first-party FAQ states no transfer restriction on the free service | capture: sha256:c020a6b2899557b8a984085bf59f8922abecd2958c53725f5cc17475636a8f42 | quote: There are no restrictions on the amount of data that can be transferred.
  - [1] 2026-11-19: signup needs an email address and password, no card details | capture: sha256:c020a6b2899557b8a984085bf59f8922abecd2958c53725f5cc17475636a8f42 | quote: Registration is free, easy, and takes seconds to complete. There's no need to enter your credit card details.
- sources:
  - [1] https://www.4s.io/faq.jsp
  - [2] https://e.4shared.com/premium.jsp
  - [3] https://webdav.4shared.com/
  - [4] https://www.4s.io/developer/docs/

## 4shared paid

- `storage/4shared-paid` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.014Z (live) | stale on 2026-12-04
- url https://e.4shared.com/linkerror.jsp
- free tier: Paid tiers, now readable on the first-party premium page: Premium 100 GB at 14.99 $ /year, Premium 500 GB at 29.99 $ /year, Premium 1 TB at 39.99 $ /year; the free tier is 15 GB. The former claim that no price page could be obtained no longer holds. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on https://e.4shared.com/linkerror.jsp | source: [1] | note: not applicable
- retention: not stated on https://e.4shared.com/linkerror.jsp | source: [1]
- egress: not stated on https://e.4shared.com/linkerror.jsp | metered: no
- identity: email
- interface: browser
- interface detail: Web sign-up and download flow; no programmatic interface is documented on the page.
- tooling: not documented
- composes with: Not stated on https://e.4shared.com/linkerror.jsp; the price page could not be obtained.
- reliability: Paid tiers are priced on the first-party premium page: Premium 100 GB at 14.99 $ /year, 500 GB at 29.99 $ /year, 1 TB at 39.99 $ /year. Payment is through Stripe.
- notes: Could not verify. https://www.4shared.com/upgrade/ and /upgrade both 302 to https://e.4shared.com/linkerror.jsp and render 'linkerror' content; /plans.jsp likewise. No price page obtainable
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Could not verify. https://www.4shared.com/upgrade/ and /upgrade both 302 to https://e.4shared.com/linkerror.jsp and render 'linkerror' content; /plans.jsp likewise. No price page obtainable
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Could not verify. https://www.4shared.com/upgrade/ and /upgrade both 302 to https://e.4shared.com/linkerror.jsp and render 'linkerror' content; /plans.jsp likewise. No price page obtainable
  - [2] 2026-11-19: the first-party premium page now publishes a 100 GB paid tier at USD 14.99 per year | capture: sha256:b8cc90d62e9093195fbf554d72cb9d14e6786a593f28e1113ba8c93eb9a896d5 | quote: Premium 100 GB 14.99 $ /year
  - [2] 2026-11-19: the first-party page states Stripe payment and cancellation at any time | capture: sha256:b8cc90d62e9093195fbf554d72cb9d14e6786a593f28e1113ba8c93eb9a896d5 | quote: Cancel anytime. Secure payment through Stripe.
  - [1] 2026-11-19: the page states a free space allowance and download ability but no egress traffic terms | capture: sha256:1a7e08c939e56c62d7be1eff63fdc630d0d5a073d66b6401c5d7314f8cb14650 | quote: Get 15 GB free space and ability to download files
  - [1] 2026-11-19: the page shows a link-error notice with no retention period, per-object cap or chaining terms | capture: sha256:1a7e08c939e56c62d7be1eff63fdc630d0d5a073d66b6401c5d7314f8cb14650 | quote: The file link that you requested is not valid.
  - [1] 2026-11-19: a sign-up asks for email verification | capture: sha256:1a7e08c939e56c62d7be1eff63fdc630d0d5a073d66b6401c5d7314f8cb14650 | quote: Verify your email address to access all 4shared features.
- sources:
  - [1] https://e.4shared.com/linkerror.jsp
  - [2] https://e.4shared.com/premium.jsp
