# Theuser.cloud

> theuser.cloud | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/theuser/ | JSON https://fshy.ajam.dev/api/v1/entity/theuser.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Theuser.cloud

- `debrid/theuser-cloud` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (free, registered, premium tiers) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://theuser.cloud/
- free tier: Free tier: 5120 Mb maximum upload, 20 GB of downloads in 1 days, files deleted 15 days after the last download; a Registered tier lists 10240 Mb uploads, 200 GB of storage and 30 GB in 1 days. | unit: mixed | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 5120 Mb per file on Free; 10240 Mb Registered; Unlimited on Premium and Premium Pro | source: [1]
- retention: 15 days after the last download on Free; 45 days Registered; 120 days Premium; never on Premium Pro | days: 15 | source: [1]
- egress: Download volume: 20 GB in 1 days on Free, 30 GB Registered, 50 GB Premium, 100 GB Premium Pro. | metered: yes | free allowance: 20 GB in 1 days | source: [1]
- identity: email | detail: The home page states that uploading is for registered members, with a one-minute free sign-up; the form fields were not read.
- interface: unknown
- limits:
  - per-object-cap: 5120 Mb per file on Free, 10240 Mb on Registered [1]
  - volume-quota (binding): 20 GB in 1 days on Free, 30 GB on Registered, 50 GB on Premium, 100 GB on Premium Pro [1]
  - retention-clamped: files are deleted 15 days after the last download on Free [1]
- binding note: 20 GB a day on Free is the first ceiling for retrieval; the 5120 Mb per-file cap is second.
- interface detail: Web upload; the home page says uploading is for registered members. No API was read.
- tooling: Browser upload; Premium lists remote URL upload and download-accelerator support.
- composes with: Premium is 50 GB per day and Premium Pro 100 GB per day with unlimited upload size; the price of either tier is not on the pages read.
- reliability: No status page was read.
- notes: The page lists an affiliate payout table for 1000 downloads, which means the host pays uploaders.
- evidence note: Tiers read on the vendor premium page and home page. Cheapest paid tier: unverified: the price list is not on the pages read.
- evidence:
  - [1] 2026-11-03: per-file cap by tier: 5120 Mb Free, 10240 Mb Registered, Unlimited Premium | capture: sha256:d34ae38e239b72554bccec0399f468139b3005ee0be5495b31b228bf7d03e643 | quote: Max upload file size 5120 Mb 10240 Mb Unlimited Unlimited
  - [1] 2026-11-03: download volume by tier: 20 GB in 1 days on Free | capture: sha256:d34ae38e239b72554bccec0399f468139b3005ee0be5495b31b228bf7d03e643 | quote: Download volume **20 GB in 1 days ** **30 GB in 1 days ** **50 GB in 1 days ** **100 GB in 1 days **
  - [1] 2026-11-03: retention by tier: 15 days after last download on Free | capture: sha256:d34ae38e239b72554bccec0399f468139b3005ee0be5495b31b228bf7d03e643 | quote: When are your files deleted? 15 days after last download 45 days after last download 120 days after last download Never
  - [1] 2026-11-03: storage by tier: none listed on Free, 200 GB Registered | capture: sha256:d34ae38e239b72554bccec0399f468139b3005ee0be5495b31b228bf7d03e643 | quote: Storage space - 200 GB Unlimited Unlimited
  - [2] 2026-11-03: uploading needs a free account | capture: sha256:a3142199bf36794948bc903de8bbd416166b5bc1c39204c88c0fe7bc54de7e91 | quote: Sign up free in one minute, or log in to start uploading.
- sources:
  - [1] https://theuser.cloud/premium/
  - [2] https://theuser.cloud/
