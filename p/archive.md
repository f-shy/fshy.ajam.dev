# Archive.by

> archive.by | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive/ | JSON https://fshy.ajam.dev/api/v1/entity/archive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Archive.by (Белорусский цифровой архив)

- `debrid/archive-by` | qualifies-with-caveat | evidence documented | binding per-object-cap | category Belarusian file archive with a PayPal-only premium tier | tier premium account
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:27:03.166Z (live) | stale on 2026-11-23
- url https://archive.by/upgrade
- price USD 9.99 per month at the 1-month term; USD 59.99 per year for unlimited storage | parsed USD 9.99/mo
- free tier: 'загрузки и скачивания 100% Бесплатно для всех пользователей' with unlimited storage and unlimited retention; the free per-file cap is 100 MB, premium raises it to 1 GB. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: Free accounts: 'хранятся файлы для неограниченный дней'.
- per-object cap: 'Каждый файл вы загружаете должно быть меньше, чем 100 MB в размере для свободных / не счетов или меньше, чем 1 GB в размере для премиум-аккаунтов.' | bytes: 1073741824 | source: [1] | note: The byte value treats the vendor's 1 GB premium cap as 1 GiB.
- retention: 'Free / не счета хранятся файлы для неограниченный дней. Премиум счета хранятся файлы для неограниченный дней.' | source: [1] | note: Indefinite for both tiers
- egress: Premium removes the wait and the ads and allows 'Неограниченное количество одновременных загрузок' and 'Никаких ограничений на количество загрузок'. No byte quota published. | metered: no | free allowance: unlimited downloads at free-tier speed | source: [2]
- identity: card | detail: A premium purchase is completed through PayPal, so the identity is a PayPal account and the card behind it; no Russian or Belarusian local rail is offered on the page. | country: Belarus
- interface: unknown
- limits:
  - per-object-cap (binding): 100 MB per file free, 1 GB per file premium [1]
  - per-ip-shaping: free tier: wait and ads, limited concurrent downloads; premium removes them [2]
- limits note: Payment is a single gateway: each term's form posts to /paypal/pay and the only button is 'Pay with PayPal'.
- binding note: At 1 TiB a month on the premium tier, the 1 GB per-file ceiling is the first thing a large archive meets; storage and download count are unlimited, and there is no rate limit published.
- interface detail: Web upload/download; premium advertises download-manager support ('Загрузка ... поддержка менеджера загрузок'). No API documented.
- tooling: Browser; the premium checkout is a PayPal form posting to archive.by/paypal/pay.
- composes with: A Belarusian place to park a public archive; it fetches from nowhere, so it is storage in the stack, not retrieval.
- reliability: The interface is machine-translated Russian with visible artefacts ('100% Safe &Amp; Anonymous', 'премия Account'), which is a quality signal rather than a capacity one; a PayPal-only gateway means a buyer without PayPal cannot pay at all.
- notes: The Belarusian equivalent the sector asked for, and the inverse of bedrive: a BY service that takes only PayPal while a RU service takes only YooMoney. That pairing is the evidence that the payment wall follows the acquirer, not the language of the site. Whether a Belarusian buyer can actually complete a PayPal payment was not tested.
- evidence note: All five prices, both file caps, the unlimited-retention statement and the single PayPal gateway are quoted from live pages and raw HTML read.
- evidence:
  - [2] 2026-10-23: 7 days $4.99, 1 month $9.99, 3 months $19.99, 6 months $34.99, 1 year $59.99, 'Неограниченное хранение', 'Загрузка файлов до 1.00 GB'
  - [1] 2026-10-23: 100 MB free / 1 GB premium per-file cap, unlimited storage and unlimited retention on both tiers
  - probe:https://archive.by/upgrade 2026-10-23: the payment HTML: five forms posting to https://archive.by/paypal/pay with days=7/31/... and a single 'Pay with PayPal' image button - no card fields, no local gateway
- sources:
  - [1] https://archive.by/faq
  - [2] https://archive.by/upgrade
