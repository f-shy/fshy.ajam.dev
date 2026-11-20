# XS News

> xsnews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xsnews/ | JSON https://fshy.ajam.dev/api/v1/entity/xsnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XS News (Abavia backbone)

- `debrid/xs-news` | paid-only | evidence documented | binding none | category usenet backbone and provider (Abavia, independent, NL) | tier Unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.xsnews.com/plans.html
- price EUR 4.95 (Unlimited, monthly); EUR 11.99 per TB on the 5000 GB block
- free tier: No free tier and no free trial on the plans or block pages read. A 14-day money-back guarantee is the only risk reversal. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: Retention is not stated on the plans page or the block page. The r/usenet map records 4,000+ days with a 2,600-day backfill via Newshosting. | days: 4000 | source: [2]
- egress: Unlimited data on both plans; Unlimited tier has unlimited speed and 100 connections | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: No free path exists. Payment options read from the vendor page are cards (Visa, Mastercard, Maestro, Amex, Postepay, Carte Bancaires) and direct bank transfer or wallets (iDEAL, Sofort, Trustly, Giropay, EPS, Przelewy24, Multibanco, Bancontact). No crypto is listed anywhere on that page.
- interface: nntp
- limits:
  - request-rate: 50 connections on Basic 50, 100 on Unlimited, 200 on any block [3]
  - per-ip-shaping: 50 Mbit/s on Basic 50, unlimited on the Unlimited plan [1]
  - volume-quota: block accounts are one-time byte allowances that never expire [3]
  - retention-clamped: 4,000+ days, reported; not stated on the pages read [2]
  - request-rate: 200 connections [3]
  - volume-quota: 100 GB to 5,000 GB blocks [3]
- limits note: Plans: Basic 50 EUR 2.95/mo (50 Mbit, 50 connections), Unlimited EUR 4.95/mo against a EUR 9.95 regular price (unlimited speed, 100 connections). Blocks: 100 GB EUR 9.95, 250 GB EUR 14.95, 1000 GB EUR 29.95, 5000 GB EUR 59.95 against a EUR 119.95 regular price. All blocks carry 200 connections and 'Data never expires'. Upload is not included on a block.
- binding note: The Unlimited plan publishes no volume, speed or connection ceiling beyond 100 connections, so at 1 TiB/month nothing binds. The fixed allowance binds on the block tier, where a 1 TB block is exhausted in month one; that is recorded in limits[] rather than here because the tier this record prices is Unlimited.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: An Abavia block is the fill account beside an Omicron unlimited primary: two independent spools mean an article missing on one is likely present on the other, and the block never expires.
- reliability: Abavia is the backbone (AS48345, Amsterdam) that also carries Bulknews, Cheapnews, UsenetAgency, Hitnews, UsenetDiscount, NewsGrabber, NewsXS, Stingy, TurboUsenet, UseNight and Usenet.on 2026-10-23. The 5,000 GB block at EUR 59.95 is the cheapest per-TB block found among debrid providers.
- notes: Two figures matter here and they pull in opposite directions: EUR 4.95/mo unlimited is the cheapest subscription on an independent backbone, and EUR 59.95 for 5 TB is the cheapest block. Both are vendor-stated on 2026-10-23. Cheapest per byte in the sector by a factor of three over the debrids, and the least conditional. Trigger condition: if 'Data never expires' is removed from the block page, the record falls back to the subscription terms.
- evidence note: Plan and block prices, speeds and connection counts are on the vendor pages read. Retention is only third-party, which is why the record is documented rather than measured and why the retention limit carries a reported source.
- extras:
  - backbone: Abavia, AS48345
  - resellers: Bulknews; Cheapnews; UsenetAgency; Hitnews; UsenetDiscount; NewsGrabber; NewsXS; Stingy Usenet; TurboUsenet; UseNight; Usenet.today; Usenet-Server
  - payment_methods: card, iDEAL, Sofort, Trustly, Giropay, EPS, Przelewy24, Multibanco, Bancontact; no crypto
  - block_price_tb_eur: 11.99
  - retention_map.block_balance.stated: data never expires
  - retention_map.block_balance.source_url: https://www.xsnews.com/block.html
  - retention_map.article_retention.stated: 4,000+ days
  - retention_map.article_retention.days: 4000
  - retention_map.article_retention.source_url: https://www.xsnews.com/
  - retention_map.money_back.stated: 14-day money-back guarantee
  - retention_map.money_back.days: 14
  - retention_map.money_back.source_url: https://www.xsnews.com/block.html
  - account_deletion.stated: not published
  - account_deletion.source_url: https://www.xsnews.com/block.html
  - reactivation: nothing to reactivate: the balance is the account
  - storage_model: prepaid download block over NNTP
- evidence:
  - [1] 2026-10-23: Basic 50 EUR 2.95/mo 50 Mbit 50 connections; Unlimited EUR 4.95/mo against EUR 9.95, unlimited speed, 100 connections, unlimited data
  - [3] 2026-10-23: Block 100 GB EUR 9.95; 250 GB EUR 14.95; 1000 GB EUR 29.95; 5000 GB EUR 59.95 (was EUR 119.95); EUR 1.20 per 100 GB at the top size; 200 connections; data never expires; upload not included
  - [4] 2026-10-23: cards and bank transfer/wallets only; no cryptocurrency listed
  - [2] 2026-10-23: Abavia backbone, AS48345; 'Backfill: 2600 days (via Newshosting)'; reseller list
  - [3] 2026-10-23: 'Pay once, use whenever you want... pure Usenet access that never expires', 'Data never expires' per block, and the 100 GB to 5,000 GB ladder with EUR 59.95 for 5,000 GB
  - [5] 2026-10-23: '4.000+ Days Retention', '99,8% Completeness', '100 Gb/s Backbone Speed', 20+ years operating
  - [1] 2026-10-23: subscription plans from EUR 2.95/month alongside the block product, so blocks are a choice rather than the only offer
- sources:
  - [1] https://www.xsnews.com/plans.html
  - [2] https://www.reddit.com/r/usenet/wiki/providers
  - [3] https://www.xsnews.com/block.html
  - [4] https://www.xsnews.com/payment-options.html
  - [5] https://www.xsnews.com/
