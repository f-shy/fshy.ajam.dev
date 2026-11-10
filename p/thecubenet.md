# theCubeNet

> thecubenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thecubenet/ | JSON https://fshy.ajam.dev/api/v1/entity/thecubenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## theCubeNet

- `debrid/cubenet` | paid-only | evidence documented | binding none | category usenet provider (UsenetExpress reseller) | tier Unlimited yearly
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://www.thecubenet.com/
- price USD 4.17 (unlimited, $50/year)
- free tier: No free tier and no free trial on the site read; blocks start at 500 GB for $25, with a 1 TB block at $45. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: Up to 5,912+ days retention, in the specials banner | days: 5912 | source: [1]
- egress: Unlimited speed, SSL servers in US and EU, 100 connections | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Email plus a paid order; the site is a WHMCS storefront whose cart requires payment. No trial.
- interface: nntp
- limits:
  - request-rate: 100 connections [1]
  - volume-quota: soft 10 TB/month on unlimited plans, reset on request via support - reported, not on the vendor page [2]
  - retention-clamped: up to 5,912+ days [1]
- limits note: 2026 specials: unlimited $50/year (100 connections), monthly unlimited $7.99, 250 GB/month $10 per 6 months. Blocks: 500 GB $25, 1 TB $45, 2 TB $75, all one-time.
- binding note: The vendor publishes no volume cap. The r/usenet map records a soft 10 TB/month ceiling that support resets on request; at 1 TiB/month that does not bind.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: A cheap unlimited layer on the UsenetExpress spool that stacks under an Omicron primary when a client wants 100 connections at the lowest monthly rate.
- reliability: UsenetExpress reseller (news.thecubenet.com and europe.thecubenet.com). The 2 TB block at $75 is $37.50/TB, the cheapest UsenetExpress block found on a vendor page.
- notes: The yearly unlimited at $50 is cheaper per month than UsenetExpress's own $90, which is the normal shape of reseller pricing on this backbone.
- evidence note: Prices and limits from the vendor home page read on 2026-10-23. The 10 TB soft cap is a third-party report.
- extras:
  - backbone: UsenetExpress
  - soft_cap: 10 TB/month, reported
- evidence:
  - [1] 2026-10-23: 'Unlimited Usenet $50/year 100 Connections'; '$1TB Block $45/one-time'; '500GB Block $25'; '2TB Big Block $75'; 'Monthly Unlimited $7.99'; up to 5,912+ days
  - [2] 2026-10-23: Thundernews/Thecubenet have soft limits (10TB per month) on their unlimited plans, reset on request by support
- sources:
  - [1] https://www.thecubenet.com/
  - [2] https://www.reddit.com/r/usenet/wiki/providers
