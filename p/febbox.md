# febbox

> febbox.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/febbox/ | JSON https://fshy.ajam.dev/api/v1/entity/febbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## febbox / feb

- `storage/febbox-feb` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-12-05
- url https://www.febbox.com/plan
- free tier: 10GB basic space on the Free Plan at $0/Year, with 10GB/day high-speed traffic; the paid Personal Plan is 1 TB Basic Storage | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Beyond the high-speed traffic allowance, large-file downloads are limited to 100KB/s; viewing small files such as photos has no speed limit; buying Premium lifts the limit. The plan page and the FAQ give different allowances (see limits). | metered: yes
- identity: email
- interface: webdav
- limits:
  - volume-quota (binding): 10GB basic space on the Free Plan; 1 TB Basic Storage on the Personal Plan [1]
  - volume-quota (binding): 10GB/day high-speed traffic on the Free Plan; 100GB/day on the Personal Plan (the FAQ says 100GB per month for free users) [1]
- binding note: the free space is 10GB, a stored-bytes quota far below the need; space above 1 TB is a priced purchase
- interface detail: webdav at https://webdav.febbox.com, per-account credentials with a chosen authorization directory and a read-only option
- tooling: WebDAV access is enabled in the account settings (server address https://webdav.febbox.com), usable from rclone and WinSCP; the site also lists an Open Platform.
- composes with: not recorded
- reliability: Per the FAQ, a downgrade to the free plan leaves existing files readable, allows no new uploads while over the free storage limit, and deletes files if usage stays over the limit for 3 months.
- notes: Free Plan: 10GB basic space at $0/Year. Personal Plan: 1 TB Basic Storage at $26.39/Year ($2.20 / Month), additional space can be purchased. Family Plan: $35.99/Year ($2.99 / Month), up to 5 users share the storage. The FAQ states there is no limit on the capacity that can be purchased; the price of space above 1 TB is not on the plan page (unverified).
- evidence note: Documented from vendor pages re-read on 2026-11-04: https://www.febbox.com/plan (free 10GB basic space; Personal Plan 1 TB), https://www.febbox.com/faq (throttle, 3-month deletion over the limit, purchasable capacity) and https://www.febbox.com/article/detail/id/34 (WebDAV server).
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The 'free 1TB' figure is stale marketing. The 2024 press release still says 'free 1TB storage', but the live plan page now reads 'Free Plan ... 10GB basic space', and the FAQ confirms a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 'free 1TB' figure is stale marketing. The 2024 press release still says 'free 1TB storage', but the live plan page now reads 'Free Plan ... 10GB basic space', and the FAQ confirms a…
  - [2] 2026-10-21: cited as the basis of the rejection: The 'free 1TB' figure is stale marketing. The 2024 press release still says 'free 1TB storage', but the live plan page now reads 'Free Plan ... 10GB basic space', and the FAQ confirms a down
  - [3] 2026-10-21: cited as the basis of the rejection: The 'free 1TB' figure is stale marketing. The 2024 press release still says 'free 1TB storage', but the live plan page now reads 'Free Plan ... 10GB basic space', and the FAQ confirms a down
  - [1] 2026-11-03: the free plan includes 10GB basic space | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-03: the free allowance is stated in GB | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-03: the free allowance is basic space, a stored-bytes quota | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-03: the Personal Plan with 1 TB Basic Storage costs $26.39 a year | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: $ 26.39/Year
  - [3] 2026-11-03: a free user over the traffic limit is throttled to 100KB/s on large downloads | capture: sha256:f3b096a4b997086be0d0ee7b0f03b83bfcb3a867376711a6fa35393ac7f64121 | quote: when downloading large files, the speed will be limited to 100KB/s.
  - [2] 2026-11-03: the account settings expose a WebDAV server for clients such as rclone | capture: sha256:bfbc223c684095de583dd58ea14805eb86f7bc9a5b73dd51f35d7525cfeecf3d | quote: You can use the above information to configure access in clients that support the WebDAV protocol, such as Rclone, WinSCP, etc.
  - [2] 2026-11-03: the WebDAV server address | capture: sha256:bfbc223c684095de583dd58ea14805eb86f7bc9a5b73dd51f35d7525cfeecf3d | quote: https://webdav.febbox.com
  - [1] 2026-11-03: the free plan is capped at 10GB of space | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-03: the binding constraint is the 10GB free allowance | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-03: the free space is 10GB | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [3] 2026-11-03: files over the free storage limit are deleted after 3 months | capture: sha256:f3b096a4b997086be0d0ee7b0f03b83bfcb3a867376711a6fa35393ac7f64121 | quote: If you remain over this limit for 3 months, your files will be deleted.
  - [3] 2026-11-03: the FAQ states purchasable capacity has no upper limit | capture: sha256:f3b096a4b997086be0d0ee7b0f03b83bfcb3a867376711a6fa35393ac7f64121 | quote: There is no limit, you can expand your maximum space by continuously purchasing additional storage capacity packages.
  - [1] 2026-11-03: the free plan is 10GB basic space | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
  - [1] 2026-11-04: the free plan includes 10GB basic space | capture: sha256:ef0ceb9128678ca423feca1bd8ea230cab31d5e505107bd2acb92ab0c2c07f5e | quote: 10GB basic space
- sources:
  - [1] https://www.febbox.com/plan
  - [2] https://www.febbox.com/article/detail/id/34
  - [3] https://www.febbox.com/faq

## febbox / feb 1 tb free

- `storage/febbox-feb-1-tb-free` | fails-quota | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:13.492Z (live) | stale on 2026-12-05
- url https://www.febbox.com/faq
- free tier: 10 GB of free storage since the end of February 2026 (previously 1 TB). Files above the new quota are not deleted; only new uploads are restricted. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [2] | note: not applicable
- retention: A free account that stays inactive for 3 consecutive months can have its files removed after prior notification. | source: [2]
- egress: Free accounts get 10 GB of traffic per day (previously 100 GB per month). | metered: yes
- identity: email
- interface: webdav
- limits:
  - volume-quota (binding): 10 GB free storage; new uploads are restricted above the quota, existing files are kept [1]
- limits note: The App Store lists Premium at 3,99 EUR monthly or 28,49 EUR yearly (in-app purchase); the price of extra storage is unverified: not published on a captured page.
- binding note: the 10 GB free quota is far below the need; paid Premium starts at 1 TB + 10 GB
- interface detail: WebDAV (beta, announced May 2025), enabled on the website; directories can be read-only or read/write.
- tooling: not documented
- composes with: not recorded
- reliability: Free storage was cut from 1 TB to 10 GB in February 2026 and free traffic from 100 GB per month to 10 GB per day; each file is stored in 2-3 copies.
- notes: Paid Premium includes 1 TB + 10 GB base storage and 100 GB per day of high-speed traffic; more storage can be purchased with no stated upper limit.
- evidence note: Documented from the vendor notice https://www.febbox.com/channel/article/LZTNZcZu (free storage 1TB to 10GB, uploads restricted above the quota, 3-month inactivity rule, 1TB + 10GB paid base) and the WebDAV announcement https://www.febbox.com/channel/article/S1g7Chu0, re-read on 2026-11-04; the Premium price is from the App Store listing, a third-party page.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: BAIT AND SWITCH, ALREADY EXECUTED. The 1 TB free offer circulated on Chinese forums in January 2026 (nodeloc thread 75566, '1T免费网盘febbox'). By March 2026 linux.do thread 1753000 was titled '
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: BAIT AND SWITCH, ALREADY EXECUTED. The 1 TB free offer circulated on Chinese forums in January 2026 (nodeloc thread 75566, '1T免费网盘febbox'). By March 2026 linux.do thread 1753000 was titled '
  - [3] 2026-10-21: cited as the basis of the rejection: BAIT AND SWITCH, ALREADY EXECUTED. The 1 TB free offer circulated on Chinese forums in January 2026 (nodeloc thread 75566, '1T免费网盘febbox'). By March 2026 linux.do thread 1753000 was titled '
  - [1] 2026-11-03: free storage is 10 GB from end of February 2026, down from 1 TB | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: unit is GB | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: quota is on stored bytes | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: the dated notice is the current statement of the free quota | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: free traffic allowance | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Now: 10GB per day
  - [1] 2026-11-03: free traffic is metered per day | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Now: 10GB per day
  - [1] 2026-11-03: inactivity removal | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: A free account remains inactive for 3 consecutive months, after prior notification.
  - [4] 2026-11-03: a WebDAV endpoint is announced (beta), enabled from the website | capture: sha256:271ccb68c9659a5705979b20b52a11442d41d68221bf72edbf3dee102b8485da | quote: FEB introduces another powerful feature for professional users! We are excited to announce full WebDAV protocol support.
  - [4] 2026-11-03: WebDAV directory permissions | capture: sha256:271ccb68c9659a5705979b20b52a11442d41d68221bf72edbf3dee102b8485da | quote: Define custom directories with **read-only or read/write access as needed.
  - [1] 2026-11-03: free policy was reduced; replication is stated | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Each file stored in 2–3 copies
  - [1] 2026-11-03: paid tier contents | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Paid users may purchase additional storage
  - [1] 2026-11-03: paid Premium base storage | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: - 1TB + 10GB base storage
  - [1] 2026-11-03: above the quota only uploads are restricted | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Only new uploads will be restricted
  - [5] 2026-11-03: Premium monthly price on the App Store listing | capture: sha256:8eb0d85f1ed1dffedf4930ae473eff02f2c6eaa5cdd2e075b64c73c115b6e6db | quote: Premium · Monthly 3,99 €
  - [1] 2026-11-03: the quota is the binding limit | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: quota is binding | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-03: free storage is 10 GB since the end of February 2026 | capture: sha256:fcb6ae10b37bfcbdbe24d4825bafa7d1f309468cc290ada11471855042f400c6 | quote: Free storage changes from 1TB to 10GB
  - [1] 2026-11-04: free storage is 10 GB, down from 1 TB | capture: sha256:66cf8a1999d8a86b0594fe7a6509b6717663007274ce1a3572a93327c4c0a1b8 | quote: Free storage changes from 1TB to 10GB
- sources:
  - [1] https://www.febbox.com/channel/article/LZTNZcZu
  - [2] https://www.febbox.com/faq
  - [3] https://linux.do/t/topic/1753000
  - [4] https://www.febbox.com/channel/article/S1g7Chu0
  - [5] https://apps.apple.com/be/app/feb-febbox-no-ads-1tb/id1543861870
