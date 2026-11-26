# Clicknupload

> clicknupload.click | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clicknupload/ | JSON https://fshy.ajam.dev/api/v1/entity/clicknupload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clicknupload

- `debrid/clicknupload` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category file host (premium one-time, crypto-friendly) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:41.071Z (live) | stale on 2026-12-26
- url https://clicknupload.click/premium.html
- price USD 15 per 30 days, no volume figure published | parsed USD 15/mo
- free tier: Free account exists; the current comparison table lists 2048 Mb maximum upload, unlimited download volume, 'Very Limited' download speed and files deleted 10 days after the last download. Premium removes the wait, ads and captcha: 'No Waiting | No Ads | No Captcha | Fast Download'. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: The free tier's real download allowance was not published on the page read.
- per-object cap: 10240 Mb premium and registered, 2048 Mb free | source: [1]
- retention: Premium: 60 days after last download. Registered: 30 days after last download. Free: 10 days after last download. | source: [1]
- egress: The current comparison table lists 'Unlimited' download volume on premium, registered and free tiers, and maximum download speed on premium against limited speed on registered and very limited on free. Premium removes waiting, ads and captcha. | metered: no | free allowance: unstated | source: [1]
- identity: card | detail: Payment options on the premium page: Visa/MasterCard, Way2Bill, PayPal, Bitcoin, Litecoin, USDT (TRC20), ETH. A premium key can also be bought from resellers for the same four prices.
- interface: browser
- limits:
  - per-ip-shaping (binding): free downloads carry a wait and a captcha per file; premium removes both [1]
  - volume-quota: unstated: the account bar's traffic field renders as empty template text [1]
- limits note: Neither the free nor the paid transfer ceiling is published. The only quantified thing on the page is the price.
- binding note: With no published byte ceiling, the wait and captcha on the free tier is the only constraint that can be named from the evidence. $15 removes it; what remains unknown is whether a byte cap appears behind it.
- interface detail: Web upload and link checker. No API or FTP on the page read.
- tooling: Browser only as read; the site is on the Leechall generator list. Clicknupload also runs an affiliate programme ('Make Money'), so many links in the wild are placed to earn rather than shared.
- composes with: The cheapest paid month of the file hosts swept at $15, with a $50 year. Because free traffic is already unlimited per day, the $15 buys time rather than bytes - which is the only case in tested services where a host's paid tier is worth it for a small pull.
- reliability: The site states 'Different fees are applied by payment providers', so the listed $15 is not what a card is charged; the reseller key route avoids the processor fee and adds a reseller's margin.
- notes: The $50 annual plan equals $4.17 per month. Cryptocurrency payment without cards is supported. Account dashboard displays 'Traffic available today: Unlimited'. No programmatic path found: Web upload and link checker. No API or FTP on the page read.
- evidence note: Prices and payment methods read on the vendor premium page. The free tier's allowance, speed and per-file cap are all unpublished, so the 'unlimited' text in the account bar is recorded as template, not evidence.
- extras:
  - plans: 30 days $15; 90 days $25; 180 days $40; 365 days $50
  - payments: Visa/MasterCard, Way2Bill, PayPal, Bitcoin, Litecoin, USDT TRC20, ETH
  - resellers: same four prices as premium keys
  - annual_effective_monthly: USD 4.17
- evidence:
  - [1] 2026-10-23: the four prices ($15 30 days, $25 90 days, $40 180 days, $50 365 days), the identical reseller key prices, 'No Waiting | No Ads | No Captcha | Fast Download', and the payment list including USDT TRC20, Litecoin and ETH
  - [2] 2026-10-23: the site now serves from clicknupload.click; .org redirects to the .click login page, which is why the record cites .click
  - [1] 2026-11-25: the free tier now publishes a 2048 Mb upload cap, unlimited download volume and 10-day lifetime | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Free * Very Limited * 2048 Mb * - * Unlimited * 10 days after last download
  - [1] 2026-11-25: premium maximum upload is 10240 Mb | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Premium * Maximum * 10240 Mb * Unlimited * Unlimited * 60 days after last download
  - [1] 2026-11-25: the free row of the tier table publishes a 10-day lifetime after the last download | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Free * Very Limited * 2048 Mb * - * Unlimited * 10 days after last download
  - [1] 2026-11-25: the registered row now publishes unlimited download volume and a limited speed | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Registered * Limited * 10240 Mb * Unlimited * Unlimited * 30 days after last download
  - [1] 2026-11-25: premium has a 10240 Mb file cap and unlimited download volume | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Premium * Maximum * 10240 Mb * Unlimited * Unlimited * 60 days after last download
  - [1] 2026-11-25: the free tier's cap, speed and 10-day lifetime are as set | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: Free * Very Limited * 2048 Mb * - * Unlimited * 10 days after last download
  - [1] 2026-11-25: the premium queue-removal claim is unchanged | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: No Waiting | No Ads | No Captcha | Fast Download
  - [1] 2026-11-25: the four premium prices are unchanged | capture: sha256:a4a528a81ae40305c61549af6f48118f90cbc25d1254208f56627014cc378363 | quote: $15 30 Days $25 90 Days $40 180 Days $50 365 Days
- sources:
  - [1] https://clicknupload.click/premium.html
  - [2] https://clicknupload.org/

## clicknupload / filespace / dosya.co / hostize / storage.to / anon.cat

- `storage/clicknupload-filespace-dosya-co-hostize-storage-to-anon` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:07.787Z (live) | stale on 2026-12-04
- url https://clicknupload.click/faq.html
- free tier: none reachable: Clicknupload FAQ states unlimited storage for active files but a 2 GB per-file cap for guests and 3 GB for registered users, with inactive files purged after 20 to 30 days for members and a week for guests. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Clicknupload offers unlimited total storage for active files, but limits files to 2 GB for guests and 3 GB for registered users, purging inactive files in 7 to 30 days. FileSpace FAQ provides no distinct terms.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
  - [2] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
  - [3] 2026-10-21: Clicknupload: unlimited-for-active-files but 2 GB guest / 3 GB registered per file, inactive purged in 7-30 days. FileSpace: FAQ renders as the upload form
  - [1] 2026-11-19: the FAQ states a 2 GB guest and 3 GB registered per-file cap | capture: sha256:e4671bcde07ba648433ee9972b45bf8b5d43cd26bff54d89ad02a46a7ff0865c | quote: Free/Guest users can upload max 2GB per file. Registered users can upload max 3GB per file. For special condition 15GB per file.
  - [1] 2026-11-19: the FAQ now states inactive files are purged after 20 to 30 days for members and a week for guests | capture: sha256:e4671bcde07ba648433ee9972b45bf8b5d43cd26bff54d89ad02a46a7ff0865c | quote: Files are hosted forever unless they are inactive. Inactive files will be remove after 20 to 30 days as member & guest uploaded inactive files will remove in a week.
  - [1] 2026-11-19: the FAQ confirms unlimited storage applies only to active files | capture: sha256:e4671bcde07ba648433ee9972b45bf8b5d43cd26bff54d89ad02a46a7ff0865c | quote: Unlimited storage for active files but you cannot used it to backup huge numbers of inactive files.
- sources:
  - [1] https://clicknupload.click/faq.html
  - [2] https://www.dosya.co/faq.html
  - [3] https://www.hostize.com/
