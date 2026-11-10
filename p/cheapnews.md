# Cheapnews

> cheapnews.eu | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cheapnews/ | JSON https://fshy.ajam.dev/api/v1/entity/cheapnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cheapnews

- `debrid/cheapnews` | trial-only | evidence documented | binding volume-quota | category usenet provider (Abavia reseller, NL) | tier Flat Unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.cheapnews.eu/
- price EUR 9.75 (Flat Unlimited, monthly); EUR 20.98 per TB on the 2000 GB block
- free tier: A 20 GB / 7-day trial is advertised as free: 'We are happy to offer all first time users a free trial of 20GB, no credit card needed!'. The same trial is priced at EUR 3.90 in the plan table on the same page. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: 3000+ days of binary and text retention, stated twice on the page | days: 3000 | source: [1]
- egress: Unlimited downloads on every flat plan; speed and connections are tiered | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: The vendor says the 20 GB trial needs no credit card, but the plan card prices the same trial at EUR 3.90, so the honest reading is that something is charged. Crypto and SEPA are accepted for paid plans, which is the card-free route to a block.
- interface: nntp
- limits:
  - request-rate: 10 connections on Flat Basic 20 up to 48 on Flat Unlimited [1]
  - per-ip-shaping: 20 Mbit on Basic 20 up to unlimited on Flat Unlimited [1]
  - volume-quota (binding): blocks from 50 GB to 2000 GB, never expiring [1]
  - retention-clamped: 3000+ days of binary retention [1]
  - request-rate: 24 connections on block products [2]
  - volume-quota (binding): 50 GB to 2,000 GB blocks [2]
- limits note: Flats: Basic 20 EUR 3.50/mo (20 Mbit, 10 connections), Premium 60 EUR 6.25, Ultimate 120 EUR 8.50, Stellar 160 EUR 8.75, Legacy 250 EUR 9.25, Flat Unlimited EUR 9.75 (48 connections). Blocks: 50 GB EUR 2.95, 100 GB EUR 4.95, 500 GB EUR 14.95, 1000 GB EUR 24.95, 2000 GB EUR 41.95, all 'Never Expires'. Payment: SEPA, card, iDEAL, Sofort, crypto, Bancontact, Belfius, Giropay and others.
- binding note: On the flats the speed tier binds before any volume, because downloads are unlimited; on the blocks the byte allowance is the whole product and a 2 TB block is 24 months at 1 TiB/month.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: A prepaid Abavia block stacks as fill under any primary and needs no renewal; the flats duplicate the XS News spool behind a lower speed ceiling.
- reliability: Abavia reseller operated by Bulk News B.V. (Bulknews), AS48345 upstream, 135,000 newsgroups. The EUR 3.90 trial line and the 'no credit card needed' sentence present an unverified contradiction in published terms.
- notes: Cheaper than its own parent brand at every block size except the 5 TB tier, which only XS News sells. Same shape as Blocknews with a published retention figure and a free 20 GB trial. Trigger condition: if the block sentence acquires a time limit, the null becomes a number.
- evidence note: Every price is from the vendor page read on 2026-10-23. The free-trial claim is contradicted by the same page's price table and is documented as trial-only rather than free.
- extras:
  - backbone: Abavia
  - payment_methods: SEPA, card, iDEAL, Sofort, crypto, Bancontact, Belfius, Giropay
  - block_price_tb_eur: 20.98
  - retention_map.block_balance.stated: without any time-limits
  - retention_map.block_balance.source_url: https://www.cheapnews.eu/en/usenet-packages
  - retention_map.article_retention.stated: 3000+ days binary
  - retention_map.article_retention.days: 3000
  - retention_map.article_retention.source_url: https://www.cheapnews.eu/
  - retention_map.trial.stated: 20 GB or 7 days, whichever first
  - retention_map.trial.days: 7
  - retention_map.trial.source_url: https://www.cheapnews.eu/faq/
  - account_deletion.stated: not published
  - account_deletion.source_url: https://www.cheapnews.eu/faq/
  - reactivation: nothing to reactivate: the balance is the account
  - storage_model: prepaid download block over NNTP
- evidence:
  - [1] 2026-10-23: 'Free 20GB Trial, no credit card needed'; 'Free trial ... 20GB downloads, 7 days /20GB' priced 'EUR 3,90' in the plan card
  - [1] 2026-10-23: blocks 50 GB EUR 2.95, 100 GB EUR 4.95, 500 GB EUR 14.95, 1000 GB EUR 24.95, 2000 GB EUR 41.95, never expires; flats EUR 3.50 to EUR 9.75; 3000+ days
  - [3] 2026-10-23: 'Get 20GB completely free - no credit card needed! Use it for 7 days or until you reach 20GB'; payment methods SEPA, card, iDEAL, Sofort, crypto, Bancontact, Belfius, Giropay
  - [2] 2026-10-23: 'You buy a package Gigabytes and download till you used it all without any time-limits!', the block ladder 50 GB to 2,000 GB, 24 connections, and the 20 GB / 7-day trial
  - [4] 2026-10-23: 'Läuft nie ab' on the Block Starter 50 listing, and '3000+ Tage binäre Aufbewahrung'
  - [1] 2026-10-23: '3000+ days binary retention' and 'Free 20GB Trial, no credit card needed'
- sources:
  - [1] https://www.cheapnews.eu/
  - [2] https://www.cheapnews.eu/en/usenet-packages
  - [3] https://www.cheapnews.eu/faq/
  - [4] https://www.cheapnews.eu/de/usenet-tarife/
