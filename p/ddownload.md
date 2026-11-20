# DDownload

> ddownload.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ddownload/ | JSON https://fshy.ajam.dev/api/v1/entity/ddownload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DDownload

- `storage/ddownload` | paid-only | evidence documented | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:15.277Z (live) | stale on 2026-12-04
- url https://ddownload.com
- free tier: Free registered accounts have a limited storage allowance of unpublished size. Ultimate (paid): EUR 39.99 for 365 days (EUR 3.33/month), advertised as 'Unlimited Storage' on the pricing page while the terms state Ultimate has a maximum storage allowance per account. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Files are deleted after no access for 5 days (upload without an account), 7 days (app guest account without an email address), 60 days (registered account without Ultimate) or 120 days (Ultimate). | days: 60 | source: [1] | note: not stated
- egress: Ultimate 200 GB/day download traffic (195 GB/account/day ); free is speed-limited, gated by a human-verification step, single-stream, with daily limits. No per-GB price. | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota: 195 GB/day per account (Ultimate) [1]
  - volume-quota: Ultimate has a maximum storage allowance per account; the figure is not published [1]
  - retention-clamped (binding): delete after 7 days without access (app guest account without an email address); 60 days registered; 120 days Ultimate [1]
- limits note: Free: unpublished storage allowance, 60-day deletion after no access. Ultimate: unlimited storage, 120-day retention, 195-200 GB/day download. Guest accounts (app, no email) delete after 7 days. Copy/import throttles: 1,000 files/hour, torrent 4 jobs/hour, 25 GB/job.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: wrapper-only
- composes with: Only the paid tier reaches unlimited, so this is a EUR 40/year route to unlimited storage rather than a free one. Email-only signup.
- notes: Ultimate (paid, EUR 3.33-14.99/mo): 'Unlimited Storage' and 'Unlimited File Size'. Free registered accounts are explicitly limited: 'Free accounts have a limited storage allowance'. The number is not published on the pricing page.
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://ddownload.com/pricing, https://ddownload.com/tos, https://ddownload.com/faq); every field that decides the verdict cites one of those captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Ultimate (paid, EUR 3.33-14.99/mo): 'Unlimited Storage' and 'Unlimited File Size'. Free registered accounts are explicitly limited: 'Free accounts have a limited storage allowance' — the number is not published on the pricing page.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Ultimate €39.99/yr: 'Unlimited Storage', 'Unlimited Download', '200Gb daily download traffic'
  - [2] 2026-10-21: '3.1 ... Free accounts have a limited storage allowance'; '10.1 ... 5 days for uploads without an account; 60 days for registered accounts without Ultimate; 120 days for Ultimate'
  - [3] 2026-10-21: 'Files from free or inactive accounts are removed automatically after longer periods of inactivity'
  - [1] 2026-11-03: the 12-month Ultimate plan costs EUR 39.99 (EUR 3.33/month on the page) | capture: sha256:73e9b30693913eca4e911b784989990b9b9cc082296821d24b69bfb687293647 | quote: Total price €39.99
  - [2] 2026-11-03: the free allowance is a limit of unpublished size, not unlimited | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: Free accounts have a limited storage allowance
  - [2] 2026-11-03: section 10.1 lists the inactivity deletion periods for each account type | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: 5 days for uploads without an account; 7 days for app guest accounts without an email address; 60 days for registered accounts without Ultimate; 120 days for Ultimate accounts.
  - [3] 2026-11-03: a registered account needs an email address that is confirmed; uploads without an account are kept 5 days only | capture: sha256:f844a3ac3964c3e278596024b1f0970f351aee4aea2b559a4c3f6e6fa0aabf5b | quote: enter your email address and a strong password, then confirm your email
  - [2] 2026-11-03: the only offer priced as large storage is paid Ultimate, and its storage allowance is capped per account at an unpublished figure | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: (d) a maximum file size and a maximum storage allowance per account.
  - [2] 2026-11-03: the daily download volume is a per-account quota | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: (a) a daily download volume per account of 195 GB (200,000 MB)
  - [2] 2026-11-03: the terms put the daily download volume at 195 GB per account | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: (a) a daily download volume per account of 195 GB (200,000 MB)
  - [2] 2026-11-03: a storage allowance per account applies | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: (d) a maximum file size and a maximum storage allowance per account.
  - [2] 2026-11-03: Ultimate storage is not unlimited | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: Ultimate does not include unlimited bandwidth, unlimited storage or unlimited downloads.
  - [2] 2026-11-03: 7 days applies to guest accounts only | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: 5 days for uploads without an account; 7 days for app guest accounts without an email address; 60 days for registered accounts without Ultimate; 120 days for Ultimate accounts.
  - [3] 2026-11-03: the monthly Ultimate subscription starts at EUR 4.99 per month | capture: sha256:f844a3ac3964c3e278596024b1f0970f351aee4aea2b559a4c3f6e6fa0aabf5b | quote: Ultimate is available as a monthly subscription from €4.99 per month, or as an annual subscription with a lower monthly price.
  - [2] 2026-11-03: the terms re-read state that Ultimate storage is capped per account and free storage is limited | capture: sha256:858ba60b2805d158880766116746b2421347ba0efe15f2fdba6820f4d119efa5 | quote: Ultimate does not include unlimited bandwidth, unlimited storage or unlimited downloads.
- sources:
  - [1] https://ddownload.com/pricing
  - [2] https://ddownload.com/tos
  - [3] https://ddownload.com/faq
