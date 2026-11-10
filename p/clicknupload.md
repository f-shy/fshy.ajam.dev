# Clicknupload

> clicknupload.click | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clicknupload/ | JSON https://fshy.ajam.dev/api/v1/entity/clicknupload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clicknupload

- `debrid/clicknupload` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category file host (premium one-time, crypto-friendly) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://clicknupload.click/premium.html
- price USD 15 per 30 days, no volume figure published | parsed USD 15/mo
- free tier: Free account exists ('Sign Up'). What premium removes is the queue, not a quota: 'No Waiting | No Ads | No Captcha | Fast Download'. The account bar renders 'Traffic available today: Unlimited' with an empty balance and an empty used-space field, which is unpopulated template text and not a statement of the free allowance. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: The free tier's real download allowance was not published on the page read.
- per-object cap: not stated on the page read | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Premium is sold as speed and queue removal only; no byte allowance is printed for either tier. The account bar's 'Traffic available today' field is a template with no value behind it, so neither tier's transfer cap is established. | metered: no | free allowance: unstated | source: [1]
- identity: card | detail: Payment options on the premium page: Visa/MasterCard, Way2Bill, PayPal, Bitcoin, Litecoin, USDT (TRC20), ETH. A premium key can also be bought from resellers for the same four prices.
- interface: unknown
- limits:
  - per-ip-shaping (binding): free downloads carry a wait and a captcha per file; premium removes both [1]
  - volume-quota: unstated: the account bar's traffic field renders as empty template text [1]
- limits note: Neither the free nor the paid transfer ceiling is published. The only quantified thing on the page is the price.
- binding note: With no published byte ceiling, the wait and captcha on the free tier is the only constraint that can be named from the evidence. $15 removes it; what remains unknown is whether a byte cap appears behind it.
- interface detail: Web upload and link checker. No API or FTP on the page read.
- tooling: Browser only as read; the site is on the Leechall generator list. Clicknupload also runs an affiliate programme ('Make Money'), so many links in the wild are placed to earn rather than shared.
- composes with: The cheapest paid month of the file hosts swept at $15, with a $50 year. Because free traffic is already unlimited per day, the $15 buys time rather than bytes - which is the only case in tested services where a host's paid tier is worth it for a small pull.
- reliability: The site states 'Different fees are applied by payment providers', so the listed $15 is not what a card is charged; the reseller key route avoids the processor fee and adds a reseller's margin.
- notes: The $50 annual plan equals $4.17 per month. Cryptocurrency payment without cards is supported. Account dashboard displays 'Traffic available today: Unlimited'.
- evidence note: Prices and payment methods read on the vendor premium page. The free tier's allowance, speed and per-file cap are all unpublished, so the 'unlimited' text in the account bar is recorded as template, not evidence.
- extras:
  - plans: 30 days $15; 90 days $25; 180 days $40; 365 days $50
  - payments: Visa/MasterCard, Way2Bill, PayPal, Bitcoin, Litecoin, USDT TRC20, ETH
  - resellers: same four prices as premium keys
  - annual_effective_monthly: USD 4.17
- evidence:
  - [1] 2026-10-23: the four prices ($15 30 days, $25 90 days, $40 180 days, $50 365 days), the identical reseller key prices, 'No Waiting | No Ads | No Captcha | Fast Download', and the payment list including USDT TRC20, Litecoin and ETH
  - [2] 2026-10-23: the site now serves from clicknupload.click; .org redirects to the .click login page, which is why the record cites .click
- sources:
  - [1] https://clicknupload.click/premium.html
  - [2] https://clicknupload.org/

## clicknupload / filespace / dosya.co / hostize / storage.to / anon.cat

- `storage/clicknupload-filespace-dosya-co-hostize-storage-to-anon` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://clicknupload.click/faq.html
- free tier: none reachable: Clicknupload offers unlimited total storage for active files, but limits files to 2 GB for guests and 3 GB for registered users, purging inactive files in 7 to 30 days. FileSpace FAQ provides no distinct terms. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
  - [2] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
  - [3] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
- sources:
  - [1] https://clicknupload.click/faq.html
  - [2] https://www.dosya.co/faq.html
  - [3] https://www.hostize.com/
