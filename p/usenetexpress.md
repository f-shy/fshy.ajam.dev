# UsenetExpress

> usenetexpress.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetexpress/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetexpress.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetExpress

- `debrid/usenetexpress` | paid-only | evidence reported | binding none | category usenet backbone and provider (independent) | tier Unlimited yearly
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:55.822Z (live) | stale on 2026-11-18
- url https://usenetexpress.com/plans/
- price USD 7.50 (unlimited, annual at $90/yr)
- free tier: No free tier and no free trial; '30 Days Risk Free' on every plan is a money-back guarantee. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: The vendor homepage states 'Many Articles Over 4000 Days Old' and 'Exceptional Binary and Text Retention'; no binary retention depth in days is stated. The r/usenet map records a 3,000-day backfill; that third-party figure is the recorded number. | days: 3000 | source: [2]
- egress: Unlimited, with 50 connections included and an upgrade path to 150 | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Email plus a paid plan. No trial exists. Payment methods listed by the vendor: PayPal, UK/EU/USA debit and Bitcoin; accounts are provisioned after payment.
- interface: nntp
- limits:
  - request-rate: 50 connections, upgradeable to 150 [1]
  - retention-clamped: 3,000-day backfill, reported by the r/usenet map; not stated by the vendor [2]
- limits note: Monthly $10, 6 months $50, yearly $90 (USD 7.50/mo equivalent), block 500 GB $20. All unlimited plans include free headers, free posting, header compression and a VPN account.
- binding note: Unlimited volume and speed; the vendor publishes no fair-use figure, so nothing in the vocabulary binds at 1 TiB/month.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Direct access buys the 150-connection upgrade no reseller sells, and the 500 GB block stacks as a fill under any other primary.
- reliability: Own Tier-1 backbone with US and NL farms, AS62296 in the US and AS50673 in Amsterdam. Sells to resellers (NewsDemon, NewsgroupDirect, CubeNet, ThunderNews, UsenetPrime, UsenetNews) and directly.
- notes: Second independent backbone after Omicron by retention depth, and the only one whose resellers publish blocks under $50/TB.
- evidence note: Prices and connections are from the vendor's plans page read. Retention is not stated by the vendor anywhere read, so the r/usenet backfill figure is used and the record drops to the reported rung because retention decides the retrieval verdict.
- extras:
  - backbone: UsenetExpress, AS62296 (US) / AS50673 (NL)
  - resellers: NewsDemon; NewsgroupDirect; CubeNet; ThunderNews; UsenetPrime; UsenetNews
  - connections_max: 150
- evidence:
  - [1] 2026-10-23: Monthly unlimited $10; 6 months $50; yearly $90; 500 GB block $20; 50 connections; 256-bit SSL; 30 days risk free
  - [3] 2026-10-23: '$7.50/mth subscribe yearly and save'; 'Exceptional Binary and Text Retention'; 50 SSL connections; VPN account included
  - [2] 2026-10-23: backbone table records UsenetExpress US full spool, NL cached, 'Backfill: 3000 days'
  - [2] 2026-11-03: the map records a 3000-day backfill; the vendor's own statement is a separate evidence row | capture: sha256:ce68343303ed49e39a8c4c999a557b78a25d3f976eb44da979781c00dd669f2c | quote: | | | | Backfill: 3000 days | NTD |
  - [3] 2026-11-03: the vendor states many articles over 4000 days old | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: - Many Articles Over 4000 Days Old
  - [3] 2026-11-03: debit accepted, with PayPal and Bitcoin on adjacent lines | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: - UK/EU/USA debit: YES
  - [3] 2026-11-03: PayPal accepted | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: - Paypal™ accepted: YES
  - [3] 2026-11-03: Bitcoin accepted | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: - Bitcoin accepted: YES
  - [3] 2026-11-03: 50 connections upgradeable to 150 | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: All plans include 50 hi-speed connections, upgradeable to 150 connections!
  - [1] 2026-11-03: yearly unlimited plan $90 with 50 connections, unchanged | capture: sha256:355581c489edb3bbb69346f9fa8378c69a87ce4f435bdbdbc365d497323f4ed8 | quote: Yearly UNLIMITED 50 Connections 256-bit SSL (TLS1.2) 30 Days Risk Free VPN Account Included $90
  - [3] 2026-11-03: money-back guarantee, not a trial, unchanged | capture: sha256:5a0578df404fb9126c6394379f10222745c199627c740d1ecf71ae8a3b7e0d87 | quote: 30 Day Money Back Guarantee
- sources:
  - [1] https://usenetexpress.com/plans/
  - [2] https://www.reddit.com/r/usenet/wiki/providers
  - [3] https://www.usenetexpress.com/
