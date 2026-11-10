# Storage Portal

> storage-portal.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storage-portal/ | JSON https://fshy.ajam.dev/api/v1/entity/storage-portal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Storage Portal

- `debrid/storage-portal-com` | qualifies | evidence documented | binding volume-quota | category pay-per-GB premium link generator (multi-host) | tier traffic packs, no subscription
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:07:08.778Z (live) | stale on 2026-11-23
- url https://www.storage-portal.com/ru/
- price USD 75 per TB at the 600 GB pack ($0.075/GB); USD 200 per TB at the 5 GB pack
- free tier: No free tier. The smallest pack is 5 GB for $1.00; the page says 'Без ежемесячной платы - оплата по факту использования' (no monthly fee, pay per use) and 'Трафик ... можно накапливать, трафик действителен постоянно' (traffic accumulates, never expires). | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Packs: 5 GB $1.00; 20+5 GB $2.90 (listed $4.00); 100+20 GB $11.00 (listed $20.00); 200+40 GB $20.00 (listed $30.00); 500+100 GB $45.00 (listed $60.00). The lower figure is the current promo price on the same page.
- per-object cap: not applicable: it forwards a link to the source host, it does not store the object; no maximum file size published | source: [1] | note: unstated
- retention: Generated links are time-limited: 'Сгенерированные ссылки для скачивания действительны до 24 часов' on the home page; the Turbobit page says '~36h direct links'. The purchased traffic balance itself never expires. | days: 1 | source: [1] | note: Two of the vendor's own pages disagree (24 h vs ~36 h); this record keeps the shorter figure.
- egress: Traffic is the product. Each generated link draws down the purchased balance; the vendor sells 'high-throughput international transit' and publishes no per-link speed figure. | metered: yes | free allowance: none | price per TB: USD 75 per TB at the 600 GB pack ($45.00 for 500 GB + 100 GB bonus); USD 0.075/GB | source: [1]
- identity: email | detail: Account at storage-portal.com; email is the minimum the purchase flow implies. No card is required to hold an account.
- interface: webdav, rest
- limits:
  - volume-quota (binding): every download draws down a prepaid traffic balance; no monthly allowance [1]
  - request-rate: batch links are processed in parallel; no published concurrency number [1]
- limits note: The host list is large (32 named on the home page: Rapidgator, FileJoker, Keep2share, Fileboom, UploadGig, NitroFlare, Turbobit, Upstore, 1fichier, Katfile, Hotlink, Depositfiles, DDownload, Extmatrix, FileFactory, Emload, Filespace, Ubiqfile, HitFile, Jumploads, Xubster, Alfafile, Takefile, Kshared, NovaFile, Fastfile, Hot4Share, Loadme, Filefox, Dailyuploads and others). Per-host coefficients are not published on the pages read.
- binding note: There is no subscription and no rate to hit: the prepaid balance is the only constraint, and at 1 TiB/month it costs $75 (at the 600 GB pack rate). It never expires, so unused traffic is not lost.
- interface detail: 'Монтируйте через протокол WebDAV для просмотра и управления файлами прямо в файловом менеджере.' Links can be handed to IDM or aria2 ('send it to IDM / aria2'). A REST endpoint is implied by the mounting and the purchase flow; no public API documentation page was read, so the rest token is the weaker of the two.
- tooling: Browser form plus WebDAV mount; generated links work with aria2/IDM because they are plain HTTP with resume.
- composes with: The per-GB balance replaces a monthly debrid subscription: a 600 GB pack at $45 covers 1 TiB of monthly transfer twice over and never expires, so it pairs with a cheap seedbox for the torrent half.
- reliability: A generated link dies after 24 h and must be regenerated from the balance; the vendor states Russian cards do not work and routes Russian users through WebMoney WMZ/WMT with a RUB bank transfer, which is a payment path, not a download limit.
- notes: The best card-payable price found among debrid providers and the answer to the sector question: a foreigner pays $1-$60 by Visa/Mastercard/Apple Pay, a Russian pays the same packs through WebMoney with a RUB transfer. The RU interface plus the RUB article is evidence of targeting, not of incorporation, and no ownership claim is made here. The about page advertises sister brands, one of which is CoolDebrid.
- evidence note: Pack prices, the payment-method list and the Russian-card statement are quoted from live pages read. A generated link actually downloaded would raise it to measured.
- evidence:
  - [1] 2026-10-23: the five traffic packs with prices, 'Трафик ... действителен постоянно', 'Ссылки действуют 24 часа', the WebDAV mount, and the 32-host list
  - [2] 2026-10-23: checkout for the 500 GB + 100 GB pack at $45.00 with the methods: Card (Visa, Mastercard, American Express, Discover, JCB, Diners Club), Apple Pay, Google Pay, WebMoney (also bank transfer, crypto, Alipay), Alipay, WeChat Pay, USDT (TRC, ERC, BEP)
  - [3] 2026-10-23: 'российские пользователи не могут использовать основные функции оплаты картами'; the RUB route is WebMoney WMZ/WMT then a bank transfer in RUB to a local account
  - [4] 2026-10-23: per-GB positioning against 'Turbobit premium ~$10.95/mo typical' and '~36h direct links' (the second link-lifetime figure)
- sources:
  - [1] https://www.storage-portal.com/ru/
  - [2] https://www.storage-portal.com/ru/purchase/69b38c86a9d358fa0cc858f2
  - [3] https://www.storage-portal.com/ru/articles/how-to-pay-with-rub
  - [4] https://www.storage-portal.com/ru/turbobit
