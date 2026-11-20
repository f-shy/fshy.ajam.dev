# Webtor.io

> webtor.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webtor/ | JSON https://fshy.ajam.dev/api/v1/entity/webtor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webtor.io

- `debrid/webtor-io` | qualifies | evidence documented | binding per-ip-shaping | category browser torrent streamer and cloud torrent client | tier free + Patreon tiers (Bronze, Silver, Gold)
- needs card no, phone no, ID no, institution no | verified 2026-10-30T13:12:00.568Z (live) | stale on 2026-11-30
- url https://webtor.io/ru/
- price USD 0 at free-tier speed; USD 2 for 50 GB Vault, USD 5 for 250 GB, USD 15 for 1 TB
- free tier: 'Webtor.io полностью бесплатен для базового использования. Смотреть и скачивать торренты можно без регистрации.' Paid tiers add speed and Vault capacity. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No byte counter on the free tier; the paid tiers are denominated in Vault Points (1 point = 1 GB).
- per-object cap: no maximum file size published; each torrent is fetched by the vendor's servers and served as HTTP | source: [1] | note: unstated
- retention: Direct links and streaming sessions are temporary: 'прямые ссылки и стриминг-сессии временные. Вы всегда можете обновить или пересоздать их из интерфейса библиотеки.' Vault keeps a torrent available with zero seeders for as long as Vault Points are spent on it. | source: [1] | note: Link lifetime not specified in days
- egress: Download is served over HTTPS from the vendor's servers; the free tier is throttled and the FAQ says 'Премиум-пользователи получают более высокую скорость'. No byte quota is published. | metered: no | free allowance: unlimited downloads at free-tier speed | source: [1]
- identity: anonymous | detail: Free use needs no account at all ('без регистрации'); a paid tier is bought through Patreon, so the identity is a Patreon account or a crypto payment from the donate page.
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): free tier is throttled; 'Премиум-пользователи получают более высокую скорость' with no published number [1]
  - volume-quota: Vault capacity by tier: Bronze $2 = 50 GB, Silver $5 = 250 GB, Gold $15 = 1 TB [2]
  - per-ip-shaping (binding): free downloads run at an unstated bandwidth tier below Premium; the only number on the page is the card-gated 50 Mbps trial [3]
  - retention-clamped: download links and streaming sessions expire after a short time, unstated [3]
  - per-ip-shaping (binding): free downloads run at a lower bandwidth tier than paid; no number is published [3]
- limits note: Live transcoding is on demand, so an unusual codec starts slower; the FAQ blames seeders, format, connection, server load and account type in that order.
- binding note: At 1 TiB a month nothing is counted, but the free tier's unstated throttle is what a client meets first; $2/month is the cheapest published way past it, and $15 buys 1 TB of Vault for retention rather than for throughput.
- interface detail: Web player plus a documented Stremio addon, Torznab/Jackett/Prowlarr integration ('Добавьте Torznab-ссылку своего индексера в профиле'), and an embeddable player SDK. The whole stack is MIT-licensed ('Все компоненты Webtor.io распространяются под лицензией MIT'), so a client can run the player or talk to the same API surface.
- tooling: Browser; Stremio addon; Torznab feed for Jackett/Prowlarr; open-source components under MIT. The Torznab integration means a client's existing indexer stack can drive it.
- composes with: It removes local BitTorrent exposure: the vendor's servers join the swarm and hand back HTTPS. That composes with a seedbox for private trackers and with a debrid for file hosts, and its Vault covers the zero-seeder case a debrid cache often misses.
- reliability: Payments run through Patreon, and the vendor's own announcement warns that backers who signed in with Apple ID must log in with the Patreon account or the perks do not attach; crypto payment was added later from the donate page.
- notes: A service with a real free tier that needs no account and no card, which makes it the default first hop when no payment method is available. It is RU-language and Patreon-monetised; Candidate explanations for why a Russian-facing product bills through Patreon: (1) card acquiring for a RU entity is closed - consistent with the Storage Portal and Turbobit statements; (2) Patreon is simply the operator's existing channel. Not decided; the record states only the rail. The verdict is 'qualifies-with-caveat' for one reason: the free path is real and account-free, but it publishes no speed, /pricing is now a 404, and the one number a reader would grab (50 Mbps) is a card-gated Patreon trial. The ladder lists Webtor among the five steps that carry the bytes; it carries none, because it has no counter. If the 50 Mbps trial were card-free it would be 3.78 TB in 7 days at line rate (6.25 MB/s x 604,800 s), 3.9x the whole ladder; the Patreon checkout is what makes it group-3 rather than group-1. It claims no per-file cap on a free, account-free path. That claim is what makes it the candidate for a 20 GiB fetch with no payment, and it is unmeasured: a 20 GiB pull was not attempted, because an interactive magnet session cannot be driven by a page fetch. /pricing and /faq are 404, so every number here comes from the landing page or the operator's blog. A ~USD 12 floor is not a monthly price, so this is not comparable with TorBox's USD 3/month. It is the cheapest crypto purchase that buys anything at all in the sample only if the plan behind it is small; otherwise it is the largest first payment.
- evidence note: The free tier, the open-source claim, the Torznab/Stremio integrations and the tier prices are quoted from the vendor's own pages and blog read. A real download through the free tier would raise it to measured.
- extras:
  - trial_line_rate_gb_7d: 3780
  - trial_gate: Patreon account plus payment method
  - pricing_page_status: 404
  - vault_points: 1 point = 1 GB; Bronze 50, Silver 250, Gold 1000
  - free_account: none required
  - paid_path: Patreon subscription
  - payment_group: crypto
  - payment.card: unverified
  - payment.paypal: unverified
  - payment.crypto: popular coins or stablecoins, unnamed
  - payment.crypto_processor: not published
  - payment.voucher: no
  - payment.entry_price: crypto minimum roughly USD 12
- evidence:
  - [1] 2026-10-23: 'полностью бесплатен для базового использования', the throttled-free-tier sentence, the temporary-link sentence, the MIT licence, and the Torznab/Stremio integrations
  - [2] 2026-10-23: 'Bronze ($2) - 50 Vault Points (50 GB) - Silver ($5) - 250 Vault Points (250 GB) - Gold ($15) - 1000 Vault Points (1 TB)' and '1 Vault Point = 1 GB'
  - [4] 2026-10-23: 'You can now get a Webtor membership with cryptocurrency - straight from the donate page.'
  - [5] 2026-10-23: the trial route redirects to patreon.com/checkout/pavel_tatarskiy - the paid rail is Patreon, not a card form on webtor.io
  - [3] 2026-10-23: 'Yes, Webtor.io is completely free for basic use. You can stream and download torrents without creating an account.', 'No size limit' under the drop box, and the banner 'Up to 50 Mbps - free for 7 days!'
  - [6] 2026-10-23: the 50 Mbps trial resolves to a Patreon checkout, /checkout/pavel_tatarskiy?is_free_trial=true, behind a Patreon login wall: a Patreon account and payment method, not an anonymous free tier
  - [3] 2026-10-23: free use with no account, 'No size limit' on the drop box, 'Your IP never joins the swarm', and direct HTTP download links
  - [2] 2026-10-23: 'Bronze ($2) - 50 Vault Points (50 GB); Silver ($5) - 250 Vault Points (250 GB); Gold ($15) - 1000 Vault Points (1 TB)' and that funded torrents stay while the subscription is active
  - [6] 2026-10-23: the paid path is the operator's Patreon checkout; the request was redirected to a Patreon login wall
  - [4] 2026-10-23: 'You can now get a Webtor membership with cryptocurrency ... Pick a plan, choose crypto at checkout, and pay with popular coins or stablecoins. The minimum depends on the coin, roughly from $12.' dated August 9, 2026
  - [3] 2026-10-23: the free tier ('completely free for basic use ... without creating an account') and that paid plans exist
  - [7] 2026-10-23: a managed alternative: USD 9/month with a 7-day trial and a USD 1 sign-up fee, from the search index, not opened
  - [8] 2026-10-30: https://webtor.io/pricing answered HTTP/1.1 404 Not Found on 2026-10-30, with x-robots-tag noindex; the 404 body is the landing-page template, with no paid-plan price on it | capture: sha256:40ae5e845a9f69adc3a24e2888f70b85284f98063e9fc52c9deb1367ef5e5a7c | quote: HTTP/1.1 404 Not Found
- sources:
  - [1] https://webtor.io/ru/
  - [2] https://blog.webtor.io/en/post/vault-is-live/
  - [3] https://webtor.io/
  - [4] https://blog.webtor.io/en/post/crypto-payments-partial-downloads-and-stremio-fixes/
  - [5] https://webtor.io/ru/trial
  - [6] https://webtor.io/trial
  - [7] https://store.elfhosted.com/product/webtor/
  - [8] https://webtor.io/pricing
