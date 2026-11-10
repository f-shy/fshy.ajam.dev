# Blocknews

> blocknews.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blocknews/ | JSON https://fshy.ajam.dev/api/v1/entity/blocknews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blocknews

- `debrid/blocknews` | qualifies | evidence documented | binding volume-quota | category usenet provider (non-expiring block accounts) | tier block
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:20:00.000Z (live) | stale on 2026-11-23
- url https://www.blocknews.net/
- price USD 39.99 per TB one-time
- free tier: No free tier and no trial: block accounts only, 5 GB for USD 1.99 up to 3,072 GB for USD 99.99. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: the block is the product; there is no monthly plan on the page
- per-object cap: Not applicable: usenet articles are capped by the poster's segment size, not by the provider. | source: [1]
- retention: The block never expires: 'No Expiration! Keep Your Gigs Until Used!' and 'Pay Only ONCE! Never Any Rebilling!' Article retention is described only as 'leading retention, increasing day by day' with no number on the page. | source: [1] | note: null is indefinite for the prepaid bytes; the article retention has no published figure, so the two clocks must not be confused
- egress: Downloaded bytes are drawn from the purchased block; there is no monthly allowance to renew and no rebilling. | metered: yes | free allowance: the purchased block only | price per TB: USD 39.99 per TB in the 1,024 GB block | source: [1]
- identity: email | detail: email and password at the billing portal; no identity document
- interface: nntp
- limits:
  - request-rate: up to 200 connections [1]
  - volume-quota (binding): the purchased block, 5 GB to 3,072 GB [1]
  - request-rate: up to 200 connections [2]
  - volume-quota (binding): blocks from 5 GB to 3,072 GB, one-time and non-expiring [2]
- limits note: Article retention is the real ceiling and it is unpublished, which is the one gap in an otherwise clean offer.
- binding note: At 1 TiB/month the block is spent in about a month; that is the point - it is spent, not expired, and an unspent balance waits indefinitely.
- interface detail: NNTP with SSL; up to 200 connections; seven server locations (two USA, one Europe, plus Africa, Asia, Australia, South America)
- endpoint: news.blocknews.net
- tooling: any NNTP client or downloader (SABnzbd, NZBGet, nzbget-compatible tooling); no API beyond NNTP
- composes with: the cleanest 'fetch now, read later' primitive in the whole corpus: a prepaid byte balance that survives any pause, and articles that sit on the provider's spool independent of the account's payment state
- reliability: Completeness depends on the poster's propagation; the FAQ page answered a bot challenge to the reader, so no completeness figure could be read.
- notes: The block is the answer to the debrid question in its purest form: nothing to renew, nothing to lapse. What it does not give is storage of a chosen file - it gives access to articles the provider happens to hold. Trigger condition: a published article-retention figure, or a change to the non-expiry claim. At $32.55/TB it is cheaper than every UsenetExpress block except CubeNet's 2 TB tier, and it sits on a different backbone, which is what a fill account needs.
- evidence note: The non-expiring claim is on the vendor's own front page in two places. Article retention has no number there and the FAQ was challenge-walled, so one figure is missing rather than guessed.
- extras:
  - retention_map.block_balance.stated: keep your gigs until used
  - retention_map.block_balance.source_url: https://www.blocknews.net/
  - retention_map.article_retention.stated: not published ('increasing day by day')
  - retention_map.article_retention.source_url: https://www.blocknews.net/
  - account_deletion.stated: not published
  - account_deletion.source_url: https://www.blocknews.net/
  - reactivation: nothing to reactivate: the balance is the account
  - storage_model: prepaid download block over NNTP
  - backbone: NetNews, AS6450
  - block_price_tb_usd: 32.55
  - server_locations: 7
- evidence:
  - [1] 2026-10-23: 'No Expiration! Keep Your Gigs Until Used!', 'Pay Only ONCE! Never Any Rebilling!', the 5 GB to 3,072 GB price ladder, 200 connections, seven server locations
  - [3] 2026-10-23: the FAQ returned a 403 bot challenge to every reader route tried (extractor, exa, contextdev, hyperbrowser, tinyfish, cfbr), so its retention figure is unread
  - [2] 2026-10-23: 5 GB $1.99 through 3,072 GB $99.99; 'Pay Only ONCE! Never Any Rebilling!'; 'No Expiration!'; 'up to 200 connections'; seven server locations
  - [4] 2026-10-23: BlockNews on NetNews, AS6450; reseller of the same backbone as Frugal Usenet
- sources:
  - [1] https://www.blocknews.net/
  - [2] https://blocknews.net/
  - [3] https://blocknews.net/faq/
  - [4] https://www.reddit.com/r/usenet/wiki/providers
