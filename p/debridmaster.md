# DebridMaster

> debridmaster.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debridmaster/ | JSON https://fshy.ajam.dev/api/v1/entity/debridmaster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DebridMaster

- `debrid/debridmaster` | qualifies-with-caveat | evidence documented | binding volume-quota | category multi-hoster download service (debrid), pay-as-you-go | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-25T09:46:55.565Z (live) | stale on 2026-12-26
- url https://debridmaster.com/status
- price USD 500/TB pay-as-you-go; USD 4.99/mo for 15 GB | parsed USD 332.67/TB-mo
- disagrees on identity_kind: `debrid/debridmaster` says email, `debrid/telegram-debridmasterbot` says any-phone
- free tier: Free: '$0 / forever', '2 files a day, up to 512 MB each', 'Standard hosts only'. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: 512 MB per file on the free tier; no per-link cap is published for a paid plan | bytes: 512000000 | source: [1]
- retention: not applicable: links are generated on demand | source: [1]
- egress: Billed per byte: '$0.50 per GB on standard hosts', plus hosts count x3. Plans carry a monthly quota - Pro 15 GB/month, Premium 40 GB/month - with overage at $0.40 and $0.30/GB. A per-host daily bandwidth is also published for five hosts. | metered: yes | free allowance: Pro 15 GB/month, Premium 40 GB/month; pay-as-you-go credits from $2 | price per TB: USD 500/TB (0.50/GB standard; Plus hosts at 3x) | source: [1]
- identity: email | detail: Not read: no signup form was opened. Free plan needs no payment; credits are bought with a card.
- interface: browser
- limits:
  - volume-quota (binding): Pro 15 GB/month, Premium 40 GB/month, overage USD 0.40-0.30/GB [1]
  - per-object-cap: 512 MB per file on the free tier [1]
  - volume-quota (binding): per host per day: NitroFlare 100 GB, FileBoom 50 GB, Keep2Share 50 GB, Upstore 20 GB, FileJoker 15 GB [2]
- limits note: The status table has a Daily bandwidth column for 61 hosts and only 5 carry a number; the rest print an em dash, which the vendor leaves undefined.
- binding note: 40 GB/month on Premium is 1.3 GB/day, or 3.6% of the 36.7 GB/day 1 TiB of monthly transfer needs; the plan quota binds about 27x before any host cap does.
- interface detail: No public API documentation was found: /api answers 404. The service is a web flow, and the per-host table is published as an HTML status page.
- endpoint: https://debridmaster.com/status
- tooling: No documented API, no rclone backend; automation would need a browser session. That is a note about tooling, not a verdict.
- composes with: The only service here that prices egress per byte, so it can absorb a one-off overflow when a capped host blocks elsewhere on a flat-rate plan.
- reliability: Five hosts are marked 'Partner network' rather than 'Own account', and two Plus hosts (FileJoker, Upstore) have 'never' in the last-checked column, so the published cap is a policy figure rather than an observed one for those.
- notes: The site is new enough that its own comparison guides are the clearest statement of the cap policy; the status table is the machine-readable version. No programmatic path found: No public API documentation was found: /api answers 404. The service is a web flow, and the per-host table is published as an HTML status page.
- evidence note: Both tables are the vendor's own pages read. The 5 published caps are policy statements; a paid download would be needed to confirm enforcement.
- extras:
  - host_matrix.published_daily_caps: yes
  - host_matrix.source: https://debridmaster.com/status
  - host_matrix.hosts_listed: 61
  - host_matrix.rows[0].host: filejoker.net
  - host_matrix.rows[0].daily_gb: 15.0
  - host_matrix.rows[1].host: upstore.net
  - host_matrix.rows[1].daily_gb: 20.0
  - host_matrix.rows[2].host: fileboom.me
  - host_matrix.rows[2].daily_gb: 50.0
  - host_matrix.rows[3].host: keep2share.cc
  - host_matrix.rows[3].daily_gb: 50.0
  - host_matrix.rows[4].host: nitroflare.com
  - host_matrix.rows[4].daily_gb: 100.0
  - classes.standard: 60
  - classes.plus_x3: 2
- evidence:
  - probe:https://debridmaster.com/status 2026-10-23: 61-row table with Host, Availability, Served by, Status, 7-day success, Class, Daily bandwidth; 5 numeric caps, the rest em dash
  - [1] 2026-10-23: '2 files a day, up to 512 MB each' free, '$0.50 per GB', Pro '$4.99 per month 15 GB', Premium '$9.99 40 GB'
  - probe:https://debridmaster.com/api 2026-10-23: no public API page: HTTP 404
  - [3] 2026-10-23: 'every host has its own published daily bandwidth per user, reset at 00:00 UTC'
  - [1] 2026-11-25: the free tier still allows two files a day up to 512 MB each | capture: sha256:10f99d66d81afa2616460fd59963d7bbb30a800d4c76278d76098adf792fbb6a | quote: 2 files a day, up to 512 MB each
  - [1] 2026-11-25: the Pro plan still carries a 15 GB monthly quota | capture: sha256:10f99d66d81afa2616460fd59963d7bbb30a800d4c76278d76098adf792fbb6a | quote: 15 GB per month
  - [1] 2026-11-25: the pay-as-you-go rate is unchanged at USD 0.50 per GB on standard hosts | capture: sha256:10f99d66d81afa2616460fd59963d7bbb30a800d4c76278d76098adf792fbb6a | quote: $0.50 per GB on standard hosts
  - [1] 2026-11-25: generated links expire after 24 hours, so the record's 'generated on demand' retention statement needs no change | capture: sha256:10f99d66d81afa2616460fd59963d7bbb30a800d4c76278d76098adf792fbb6a | quote: Free links unlock after a short wait and stay valid for 24 hours.
  - [4] 2026-11-25: access uses an emailed one-time link to an email address, so identity costs an email | capture: sha256:abb0b6708db470b6708c0df5e1bb0ead7091b39061bd65cd392b491b914724ef | quote: We email you a one-time link. Your wallet and downloads live behind it.
  - [2] 2026-11-25: the published per-host daily caps are unchanged, with NitroFlare at 100 GB/day | capture: sha256:6c3047fb0035c7f7526be3303011728fc7735780ed5a5bc852331a720c97085e | quote: | [NitroFlare](https://debridmaster.com/nitroflare-downloader)nitroflare.com | ■ Ready | Own account | Live | 100.0% · 1 download (7d) | Standard | 100 GB/day | 4 days ago |
  - [1] 2026-11-25: the Premium plan still carries a 40 GB monthly quota alongside the unchanged free tier | capture: sha256:10f99d66d81afa2616460fd59963d7bbb30a800d4c76278d76098adf792fbb6a | quote: 40 GB per month
- sources:
  - [1] https://debridmaster.com/pricing
  - [2] https://debridmaster.com/status
  - [3] https://debridmaster.com/guides/keep2share-filejoker-daily-download-limits
  - [4] https://debridmaster.com/login?next=/app

## DebridMaster (@debridmasterbot)

- `debrid/telegram-debridmasterbot` | qualifies-with-caveat | evidence documented | binding request-rate | category hosted debrid bot (file-host link to download link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:49.251Z (live) | stale on 2026-12-26
- url https://debridmaster.com/telegram-bot
- price USD 500 (pay-as-you-go, 0.50/GB); USD 250 effective on Premium (40 GB for 9.99)
- disagrees on identity_kind: `debrid/debridmaster` says email, `debrid/telegram-debridmasterbot` says any-phone
- free tier: The pricing page's Free column: '2 files a day, up to 512 MB each', 'Standard hosts only', 'Same verified downloads as paid'. | unit: MB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: 512 MB is a per-file cap, so the free ceiling is at most 2 x 512 MB a day
- per-object cap: 512 MB per file on the free tier; a paid plan has no published per-file cap on this page. | bytes: 512000000 | source: [1]
- retention: 'Paid links last 72 hours, free ones 24 hours.' The linked copy itself is deleted on that clock; nothing is stored in Telegram. | days: 1 | source: [2] | note: the day count is the free-link lifetime, the shortest published one
- egress: No Telegram traffic at all: 'Does the bot send the file through Telegram? No. It sends a download link to our verified copy, which works in a browser or a download manager and supports resume.' | metered: yes | free allowance: none: every byte past the free allowance is billed | price per TB: $0.50/GB standard hosts; $0.40/GB overage on Pro; $0.30/GB on Premium | source: [2]
- identity: any-phone | detail: The account is created by pressing Start in Telegram; an email is optional and there is no card at signup. Paying needs crypto or Telegram Stars, 'The minimum top-up in the bot is $5'.
- interface: rest
- limits:
  - request-rate (binding): 2 files/day on the free tier [1]
  - per-object-cap: 512 MB per file on the free tier [1]
- binding note: A two-per-day count fails first: two 512 MB files is about 1 GB/day, and the counter stops it before any byte quota could.
- interface detail: A Telegram chat plus a Mini App; the same account also has a website and an API.
- tooling: Any Telegram client. No token: 'Starting @debridmasterbot creates your DebridMaster account - no email or password needed.'
- composes with: Fetches a file-host link and hands back a resumable direct URL, so the byte path bypasses Telegram; useful when the object is on Keep2Share or FileJoker and useless as a Telegram store.
- reliability: Plus hosts (FileJoker, FilesMonster, Upstore) count triple against quota, and dead links are not charged; the bot's copy is deleted with the link, so a re-download after 24 hours costs again.
- notes: The important fact for debrid is negative: this class of bot is a debrid front-end in a chat and moves zero bytes through Telegram. Abandon if the free column changes or if the bot starts uploading files into the chat.
- evidence note: Prices, free allowance and the no-Telegram-delivery answer are all on the vendor's own pages read. Nothing was purchased or measured.
- evidence:
  - [1] 2026-10-23: '2 files a day, up to 512 MB each' on the free column; '$0.50 per GB' pay-as-you-go; Pro '$4.99 per month' with '15 GB per month'; Premium '$9.99 per month' with '40 GB per month'
  - [2] 2026-10-23: 'Does the bot send the file through Telegram? No. It sends a download link to our verified copy' and 'Paid links last 72 hours, free ones 24 hours.'
  - [2] 2026-10-23: 'Starting @debridmasterbot creates your DebridMaster account - no email or password needed.' and 'The minimum top-up in the bot is $5'
  - [1] 2026-11-25: the Free column still states 2 files a day up to 512 MB each | capture: sha256:dde2c6cadb98df4d00367a60e495c3a8605cafda857e0857a0029a91714c2b56 | quote: 2 files a day, up to 512 MB each
  - [1] 2026-11-25: the free download link stays valid for 24 hours | capture: sha256:dde2c6cadb98df4d00367a60e495c3a8605cafda857e0857a0029a91714c2b56 | quote: Free links unlock after a short wait and stay valid for 24 hours.
  - [1] 2026-11-25: the free allowance resets on a rolling 24 hours and is shared per network | capture: sha256:dde2c6cadb98df4d00367a60e495c3a8605cafda857e0857a0029a91714c2b56 | quote: The allowance resets on a rolling 24 hours and is shared by everyone on the same network.
  - [2] 2026-11-25: the bot sends a resumable download link, not a Telegram file; free links last 24 hours | capture: sha256:96ebc4fea442f832d0c79b823b078993f7c9ed9d801e335ece607af701d2d68b | quote: No. It sends a download link to our verified copy, which works in a browser or a download manager and supports resume. Paid links last 72 hours, free ones 24 hours.
  - [2] 2026-11-25: pressing Start in Telegram creates the account without an email or password | capture: sha256:96ebc4fea442f832d0c79b823b078993f7c9ed9d801e335ece607af701d2d68b | quote: That creates your DebridMaster account — no email or password needed.
  - [2] 2026-11-25: the bot's minimum top-up is USD 5 and credit does not expire | capture: sha256:96ebc4fea442f832d0c79b823b078993f7c9ed9d801e335ece607af701d2d68b | quote: The minimum top-up in the bot is $5; credit never expires.
- sources:
  - [1] https://debridmaster.com/pricing
  - [2] https://debridmaster.com/telegram-bot
