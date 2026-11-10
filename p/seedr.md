# Seedr

> seedr.cc | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedr/ | JSON https://fshy.ajam.dev/api/v1/entity/seedr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedr — free tier

- `storage/seedr-free-tier` | fails-quota | evidence reported | binding none | category iaas
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T11:21:43.945Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.seedr.cc/pricing/
- free tier: Free tier: 2GB of storage (FAQ: 'Free: 2GB'), 480p streaming, no daily or monthly transfer limits. Paid plans start at Lite, $3.95/mo for 10GB. | unit: GB | metered on: stored-bytes | read on: 2026-11-04 | source: [1]
- per-object cap: source: [2] | note: not stated
- retention: Files remain in storage until deleted; free and paid accounts keep files indefinitely. | source: [2] | note: The FAQ states retention: 'Both free and paid accounts keep files indefinitely.'
- egress: No daily or monthly limits for free users (the vendor says this can change at any time); paid plans have no monthly limits either. The storage limit is the binding constraint. | metered: no
- identity: card | detail: Free tier is 2GB ('Free: 2GB'). Paid tiers start at Lite $3.95/mo for 10 GB; the FAQ lists 'Credit/debit cards (Visa, Mastercard, Amex)' as payment methods for paid plans. What a free sign-up asks for: unverified: behind a sign-up.
- interface: rest, webdav, sftp, ftps, ftp
- limits note: per-object-cap: the FAQ says 'The maximum file size equals your available storage space.' Request-rate: 'no daily or monthly limits for free users'. Retention: 'Both free and paid accounts keep files indefinitely.' Free storage is 2GB ('Free: 2GB'); FTP/SFTP/WebDAV are paid-plan features.
- interface detail: rest
- tooling: Browser + browser extension + a 'Seedr Connector' desktop agent. FTP/FTPS/SFTP access is a paid feature (listed on Basic and above: 'FTP, FTPS & SFTP access'), and WebDAV appears only at Pro ('FTP, SFTP & WebDAV storages'). So on the free tier there is no programmatic transport at all.
- composes with: Free quota is 2GB ('Free: 2GB') and the useful transports (FTP/SFTP/WebDAV) are paid-plan features; referral bonus is 500MB per signup, up to 2GB total. Per-account 2GB makes multiplying accounts a low-yield route.
- reliability: Quota is intentionally hidden, which is itself the finding. You cannot size a workload against an unpublished number.
- notes: Free accounts get 2GB (FAQ: 'Free: 2GB'); paid tiers now start at Lite $3.95/mo for 10 GB (the home page: 'Start Now With 10GB Only $3.95').
- evidence note: The FAQ page was read on 2026-11-04 and states the free quota ('Free: 2GB') and retention ('Both free and paid accounts keep files indefinitely.'); the free sign-up requirements stay unverified: behind a sign-up.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Free tier exists but is deliberately unspecified: 'You can try Seedr for free, with a low storage limit.' Paid tiers start at Basic $7.95/mo for 50 GB. No free GB figure is published anywhere on the site.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'You can try Seedr for free, with a low storage limit. There are no daily or monthly limits for free users'
  - [3] 2026-10-21: Basic $7.95/mo = 50 GB; 'FTP, FTPS & SFTP access' listed as a plan feature, not a free one; Pro adds 'FTP, SFTP & WebDAV storages'
  - [4] 2026-11-03: referral bonus space is 500MB per signup, up to 4 signups, 2GB total | capture: sha256:d37618e8848c16b0d72e3f59ca81e3ed4f1e02c0640be7dd133fdee54d608117 | quote: Share that link, and when someone signs up from it, both you and them will get 500MB. This is limited to 4 signups with your link, so you can get up to 2GB total.
  - [2] 2026-11-03: the free allowance is described only as a low storage limit, with no daily or monthly limits for free users | capture: sha256:208e9eb16bd72eae1bbf3813cc4739d9a2f5b656d715f7f99c2f186bf67c2683 | quote: You can try Seedr for free, with a low storage limit. There are no daily or monthly limits for free users, and this can change at any time.
  - [5] 2026-11-03: the cheapest paid entry point is 10GB for $3.95 | capture: sha256:5d583adbd5e879fdbee10c042a79706988eced42c3bb227356667f9edc90340c | quote: ## Start Now With 10GB Only $3.95
  - [3] 2026-11-03: the Lite plan is $3.95/mo for 10G storage | capture: sha256:1fc004e4036a05bb4417dad2cd74fc79fa89027b048de22857e6286c4e294c86 | quote: #### Lite $3.95/ mo Perfect for quick one-offs 10G Storage
  - [3] 2026-11-03: Basic is $7.95/mo | capture: sha256:1fc004e4036a05bb4417dad2cd74fc79fa89027b048de22857e6286c4e294c86 | quote: #### Basic $7.95/ mo Perfect for steady weekend use
  - [6] 2026-11-03: paid plans have no monthly limits | capture: sha256:573df09a87a1b68f956b087070931f08baa317bbd8b75b259f1dab9f67096153 | quote: Paid plans give you more storage, higher video quality and more transfers at once. There are no monthly limits on paid plans.
  - [1] 2026-11-04: the FAQ states 2GB of storage for a free account | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB
  - [1] 2026-11-04: free accounts keep files indefinitely | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: Both free and paid accounts keep files indefinitely.
  - [3] 2026-11-04: Lite is $3.95 a month for 10G storage | capture: sha256:1fc004e4036a05bb4417dad2cd74fc79fa89027b048de22857e6286c4e294c86 | quote: #### Lite $3.95/ mo Perfect for quick one-offs 10G Storage
  - [1] 2026-11-04: the free plan is 2GB, read on 2026-11-04 | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB
  - [1] 2026-11-04: the page that publishes the free quota | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB
  - [1] 2026-11-04: free plan 2GB storage with 480p streaming | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB storage, 480p streaming, basic features
  - [1] 2026-11-04: free accounts keep files indefinitely; free quota is 2GB | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: Both free and paid accounts keep files indefinitely.
  - [1] 2026-11-04: the free quota is 2GB | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB
  - [1] 2026-11-04: cards are accepted as payment for paid plans | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Credit/debit cards (Visa, Mastercard, Amex)
  - [1] 2026-11-04: the free quota is published on the FAQ page | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: • Free: 2GB
  - [1] 2026-11-04: free accounts keep files indefinitely; free is 2GB per the sibling quote | capture: sha256:1552ee55d271c9255aeafb9a4b3ee62a18e39cbd852fc71caceb135b93130fac | quote: Both free and paid accounts keep files indefinitely.
- sources:
  - [1] https://www.seedr.cc/faq/
  - [2] https://www.seedr.cc/help/pricing/
  - [3] https://www.seedr.cc/pricing/
  - [4] https://www.seedr.cc/pulse/articles/67483e182f1468b50cf50f72-invite-friends-and-get-free-space/
  - [5] https://www.seedr.cc/
  - [6] https://www.seedr.cc/help/more-storage/
