# Dukea Bilişim

> dukea.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dukea/ | JSON https://fshy.ajam.dev/api/v1/entity/dukea.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dukea Bilişim

- `debrid/dukea-com` | qualifies-with-caveat | evidence documented | binding none | category premium-account reseller (Turkish: TRY pricing, card or FAST/EFT) | tier reseller
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://magaza.dukea.com/30-gunluk-rapidgator-premium-urun31.html
- price TRY 1,000 per 30 days for Rapidgator; TRY 6,500 for 365 days | parsed USD 20.11/mo
- free tier: No free tier. Prices in lira: '30 Günlük Rapidgator Premium ... 1,000.00 TL', '180 Günlük Rapidgator Premium ... 3,200.00 TL', '365 Günlük Rapidgator Premium ... 6,500.00 TL'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The struck-through '0.00 TL' before each price is a template artefact; the charged figure is the one after it.
- per-object cap: not applicable; the host's cap applies | source: [1]
- retention: not applicable: a licence code, not storage | source: [1]
- egress: The host's own terms; the reseller states only delivery: '7/24 Otomatik Teslimat' by mail and SMS when stock is shown. | metered: yes | free allowance: host-defined | source: [1]
- identity: card | detail: Rails named on the page: 'Kredi Kartı (Banka/Kredi/Sanal Kartlar)' including virtual cards, mobile payment, and 'HAVALE/EFT' bank transfer. A card works, and a virtual card is offered as the workaround for cards that fail, which is the practical answer for a foreign buyer too. | country: Turkey
- interface: rest
- limits:
  - write-gated: stock-dependent manual/automatic delivery; 'Aktif olarak stok yoksa ya da HAVALE/EFT ile ödeme yapıldıysa ... ortalama 15 dakika' [1]
- limits note: No technical cap of its own. The reseller's page is explicit that digital codes are non-refundable after delivery.
- binding note: Nothing in the vocabulary binds at the reseller: the host's own quota applies after redemption.
- interface detail: Web store; the code arrives by email/SMS and is redeemed on the host.
- tooling: Nothing to install; redeem the code at the host, then use IDM or the host's web download.
- composes with: Turkey's route to the global hosts is a lira-priced reseller that settles by card or FAST/EFT. It is a payment adapter, not a retrieval layer: it does not aggregate hosts and does not cache.
- reliability: Delivery is stock-dependent: in-stock items ship 7/24 automatically, out-of-stock or bank-transfer orders wait on a human; codes are non-refundable and non-exchangeable once sent.
- notes: Turkey's market is almost entirely resale of foreign hosts in lira plus FAST/EFT settlement; no Turkish-owned multi-hoster surfaced in the Turkish-language queries. Caveat is that the price is a reseller markup and the code is single-host. Trigger condition: the store stops shipping virtual-card orders.
- evidence note: Product page read with prices, delivery terms and the payment table. A successful purchase from outside Turkey with a foreign card would raise this to measured.
- extras:
  - rails: bank/credit/virtual card, mobile payment, HAVALE/EFT, FAST
  - delivery: email plus SMS
  - refund: none after delivery
- evidence:
  - [1] 2026-10-23: '1,000.00 TL' for 30 days; 'Stoktan hemen teslim! Kredi kartıyla satın aldığınızda ürününüz hemen teslim edilir'; '7/24 Otomatik Teslimat'
  - [1] 2026-10-23: payment table: 'Kredi Kartı (Banka/Kredi/Sanal Kartlar)' and the HAVALE/EFT clause 'Aktif olarak stok yoksa ya da HAVALE/EFT ile ödeme yapıldıysa'
  - [2] 2026-10-23: '365 Günlük Rapidgator Premium ... 6,500.00 TL' and 'Kredi kartı veya FAST ile hemen sipariş verebilirsiniz' (FAST = Turkish instant transfer)
- sources:
  - [1] https://magaza.dukea.com/30-gunluk-rapidgator-premium-urun31.html
  - [2] https://magaza.dukea.com/365-gunluk-rapidgator-premium-urun35.html
