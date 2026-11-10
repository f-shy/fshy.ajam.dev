# Usenet.farm

> usenet.farm | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenet-2/ | JSON https://fshy.ajam.dev/api/v1/entity/usenet-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Usenet.farm

- `debrid/usenet-farm` | qualifies | evidence documented | binding volume-quota | category usenet provider (prepaid block, subscription) | tier block
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:20:00.000Z (live) | stale on 2026-11-23
- url https://usenet.farm/faq.html
- price EUR 30.00 per TB one-time (500 GB block)
- free tier: A free trial is offered before purchase ('You can select a product after your free trial'); its size is not published on the pricing page. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: the trial is real but unpriced and unsized on the public page
- per-object cap: Not applicable: usenet articles, not objects. | source: [1]
- retention: A block is prepaid and carries over: 'If you pay for a subscription while having a block active we'll move your remaining GBs to get activated once your subscription is finished', and two blocks merge. The account itself never closes: 'it remains active and after +- 1month all your traffic details are removed and the account remains available for future use'. Article retention: '3000+days on text completion' on the site and '3500+days' in the FAQ, with binaries kept 'as long as possible' rather than for a stated period. | source: [2] | note: null is indefinite for the block balance; the two article-retention figures disagree (3000 vs 3500 days) and both are text-completion claims, not binary-retention claims
- egress: Block: 500 GB for EUR 15.00, unlimited speed, 50 connections. Subscriptions are fair-use capped at 5 TB or 10 TB per month, then throttled to 6,144 KB/s for the rest of the month. | metered: yes | free allowance: the purchased block | price per TB: EUR 30.00 per TB one-time (500 GB block at EUR 15.00) | source: [1]
- identity: email | detail: email only, no password: 'Enter your e-mail, click the link in the e-mail and you're ready to go.'
- interface: nntp
- limits:
  - request-rate: 50 connections on a block [2]
  - volume-quota (binding): 500 GB block; 5 TB or 10 TB fair-use per month on subscriptions [1]
  - per-ip-shaping: throttle to 6,144 KB/s after the monthly fair-use cap [1]
  - request-rate: 40 connections on both plans, 50 on the prepaid block [1]
  - volume-quota (binding): 5 TB fair use on Stingy, 10 TB on To the max [1]
  - per-ip-shaping: 'we will lower your download speed to 6144 KB/s (48 Mbits) for the remaining days of the month' on exceeding fair use [1]
  - retention-clamped: 3,000 days text completion; binary depth not quantified by the vendor [1]
  - volume-quota (binding): 10 GB on the free trial [1]
  - request-rate: 40 connections on the paid plans [1]
- limits note: Account sharing is explicitly allowed on blocks (unlimited users) and on TTM (two users), which is unusual in this market.
- binding note: At 1 TiB/month a 500 GB block is half a month; the balance then waits indefinitely, which is the property that matters here.
- interface detail: NNTP at news.usenet.farm (IPv4 at news4.usenet.farm, EU at news.usenetfarm.eu), 50 connections on a block
- endpoint: part of interface detail
- tooling: standard NNTP clients; the vendor documents its own dashboard but offers no API beyond NNTP
- composes with: blocks merge and survive subscription gaps, so a client can buy 500 GB now, add another later, and never lose the balance between paid months
- reliability: Binaries are stored by a proprietary policy ('as long as possible') rather than a guaranteed window, so old binaries can be absent even inside the text-retention window.
- notes: The weakest of the four usenet blocks on paper (one size, the least precise retention, the smallest balance) and the only one that explicitly allows sharing. Trigger condition: a stated binary-retention window would replace the 'as long as possible' note. 10 GB is a fifth of the 50 GiB monthly bar, so the trial alone does not clear it. What makes the record qualify is that the trial needs nothing but an email. The step survives, and the reason it needed checking is the finding: four plausible sub-paths (/pricing, /plans, /signup, /register) all answer 404, and the text reader drops the offer, so a verifier who used one route would have recorded this trial as gone. The 10 GB is real and the signup form asks for nothing but an email.
- evidence note: The block carry-over, the account survival and the connection counts are vendor text read. The article retention is inconsistent between two of the vendor's own pages, and the block's own expiry is implied by 'prepaid' rather than stated in one sentence.
- extras:
  - retention_map.block_balance.stated: prepaid, merges and carries over
  - retention_map.block_balance.source_url: https://usenet.farm/faq.html
  - retention_map.article_retention_text.stated: 3000+ days on the site, 3500+ in the FAQ
  - retention_map.article_retention_text.days: 3000
  - retention_map.article_retention_text.source_url: https://usenet.farm/
  - retention_map.traffic_detail_removal.stated: traffic details removed after about a month of no payment; account stays
  - retention_map.traffic_detail_removal.days: 30
  - retention_map.traffic_detail_removal.source_url: https://usenet.farm/faq.html
  - account_deletion.stated: account remains available for future use; no deletion published
  - account_deletion.source_url: https://usenet.farm/faq.html
  - reactivation: buy another block; balances merge
  - storage_model: prepaid download block over NNTP
  - backbone: UsenetFarm, AS50655
  - fair_use_penalty: 48 Mbit for the rest of the month
  - trial_payment: none required
  - routes_tried: read https://usenet.farm/ (no trial text); read https://www.usenet.farm/ (no trial text); fetch https://usenet.farm/ (trial text present); read /pricing, /plans, /signup, /register (all 404)
  - ladder_gb_month_one: 10
- evidence:
  - [2] 2026-10-23: 'If you pay for another block both will be merged to one'; 'we'll move your remaining GBs to get activated once your subscription is finished'; 'it remains active and after +- 1month all your traffic details are removed and the account remains available for future use'; '3500+days on text completion'
  - [1] 2026-10-23: Block EUR 15.00 prepaid 500 GB, 50 connections, account sharing; '3000+days on text completion and we store frequently requested binaries as long as possible'; the 5 TB and 10 TB fair-use caps
  - [1] 2026-10-23: no registration form and no password: the login is an emailed link
  - [1] 2026-10-23: '10GB Free trial for everyone! No gotchas!'; 'No creditcard or other payment info required, try without pay!'
  - [1] 2026-10-23: Stingy EUR 4.95 12.5 MB/s 40 connections 5TB fair use; To the max EUR 7.95 unlimited speed 40 connections 10TB fair use; Block EUR 15.00 500 GB
  - [1] 2026-10-23: 'we will lower your download speed to 6144 KB/s (48 Mbits) for the remaining days of the month'; '3000+days on text completion'
  - [3] 2026-10-23: UsenetFarm backbone, AS50655; cached 3,000 days, backfill 3,000 days; reseller of Frugal Usenet as its bonus server with a 1 TB monthly cap
  - [1] 2026-10-23: raw HTML contains '10GB Free trial for everyone!', 'Start your free trial (10GB)', 'No creditcard or other payment info required, try without pay!' and a form action '/action/trial/begin' with a single email field
  - [1] 2026-10-23: the text-extraction route returns 79 words with no trial, no plan and no price: the same URL read twice by two routes disagrees with itself
- sources:
  - [1] https://usenet.farm/
  - [2] https://usenet.farm/faq.html
  - [3] https://www.reddit.com/r/usenet/wiki/providers
