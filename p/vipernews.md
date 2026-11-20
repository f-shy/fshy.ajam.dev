# ViperNews

> vipernews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vipernews/ | JSON https://fshy.ajam.dev/api/v1/entity/vipernews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ViperNews

- `debrid/vipernews` | paid-only | evidence documented | binding none | category usenet backbone and provider (independent, NL) | tier entry plan
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T11:28:57.796Z (live) | stale on 2026-12-04
- url https://www.vipernews.com/
- price USD 1.79 (entry plan)
- free tier: No ongoing free tier. The sign-up page offers a 7-day free trial on the periodic plans: 'Your 7-day free trial is completely risk free - no payment information needed.' The home page also states a 7-day money-back guarantee. The trial's own limits are not stated. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The FAQ states that free trial accounts cannot post to Usenet; posting is enabled on paid packages.
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: The vendor FAQ states 4,500+ days: 'Our platform currently retains Usenet messages that are more than 4,500 days old.' The third-party r/usenet map gives a lower figure, which does not match the vendor. | days: 4500 | source: [2]
- egress: No download limit on the periodic plans; block accounts carry a download limit; with one friend or family member; posting enabled by default on paid packages | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: Email address and password. The sign-up page states 'Your 7-day free trial is completely risk free - no payment information needed.' Paid plans take a credit card, PayPal or cryptocurrencies; automatic renewal is not supported with cryptocurrencies.
- interface: nntp
- limits:
  - request-rate: 5 connections on VIPER10 (10 Mbit/s), 20 on VIPER50 (50 Mbit/s), 40 on VIPERUNL (unlimited speed) and on the block accounts [1]
  - volume-quota: soft 5 TB/month on unlimited plans, reset on request via support - reported, not on the vendor page [3]
  - retention-clamped: 4,500+ days per the vendor FAQ; the third-party r/usenet map gives a lower figure [2]
- limits note: Periodic plans start at $1.79/mo (VIPER10), $2.69/mo (VIPER50) and $3.59/mo (VIPERUNL) when billed yearly. Block accounts do not expire: 500GB $13.99, 1000GB $23.99 and 2000GB $42.99, each a one-time payment.
- binding note: The vendor publishes no volume cap; the reported soft ceiling is 5 TB/month, which 1 TiB/month does not reach.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Stacks as a cheap fill or as a low-cost primary for recent content; the ASN it shares with UsenetExpress makes it a weaker second feed than its independence suggests.
- reliability: Independent Dutch platform (ViperNews B.V., formerly mapped as Uzo Reto) that has shared an ASN with UsenetExpress since 2023, which makes it a less independent second feed than it looks.
- notes: The vendor states 4,500+ days of retention, about 12.3 years; the r/usenet map lists 1,500-day primary and 1,500-day secondary backfill, so the two sources disagree.
- evidence note: Prices, plan limits, retention and the free trial are vendor-stated and were read on 2026-11-03. Only the monthly soft cap is third-party (r/usenet); the vendor publishes no download limit on the periodic plans.
- extras:
  - backbone: ViperNews / Uzo Reto, AS62296 shared with UsenetExpress
  - soft_cap: 5 TB/month, reported
- evidence:
  - [1] 2026-10-23: 'starting at $1.79/mo'; 'try it risk-free for 7 days'; '7-day money-back guarantee'; posting enabled by default
  - [3] 2026-10-23: ViperNews backbone: full, cached, primary backfill 1,500 days, secondary backfill 1,500 days; 'soft limits (5tb per month) on their unlimited plans'
  - [4] 2026-11-03: the sign-up page offers a 7-day free trial that needs no payment information | capture: sha256:292f4a83c68242d44a2390098c59fda4c618a50b9e8428ae82287344796c99f9 | quote: Your 7-day free trial is completely risk free - no payment information needed.
  - [2] 2026-11-03: trial accounts exist and cannot post | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Free trial accounts are not allowed to post to prevent abuse.
  - [2] 2026-11-03: the vendor states a retention of more than 4,500 days | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Our platform currently retains Usenet messages that are more than 4,500 days old.
  - [2] 2026-11-03: vendor retention is 4,500+ days | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Our platform currently retains Usenet messages that are more than 4,500 days old.
  - [2] 2026-11-03: the retention figure is on the vendor FAQ | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Our platform currently retains Usenet messages that are more than 4,500 days old.
  - [1] 2026-11-03: the plan list gives 5, 20 and 40 connections with the speed caps 10 Mbit/s, 50 Mbit/s and unlimited | capture: sha256:efff088dacaacf04bfe1771251af9da007064f1cbd9eeca0e79a094e072ff5e9 | quote: 20 connections
  - [1] 2026-11-03: the vendor lists block accounts with one-time prices; the plan and block prices are on the same page | capture: sha256:efff088dacaacf04bfe1771251af9da007064f1cbd9eeca0e79a094e072ff5e9 | quote: Just $42.99once
  - [2] 2026-11-03: sharing is allowed with one friend or family member | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Yes, you are allowed to share your account with one friend or family member.
  - [4] 2026-11-03: the sign-up form asks for an email address; the trial needs no payment information and paid plans also take PayPal or cryptocurrencies | capture: sha256:292f4a83c68242d44a2390098c59fda4c618a50b9e8428ae82287344796c99f9 | quote: Email address
  - [4] 2026-11-03: cryptocurrencies are a payment method and cannot auto-renew; the same page lists credit card and PayPal | capture: sha256:292f4a83c68242d44a2390098c59fda4c618a50b9e8428ae82287344796c99f9 | quote: Automatic renewal with this payment method is not supported, but you can save an additional 10% when you enable automatic renewal with another payment method.
  - [2] 2026-11-03: retention, which decided the rung, is now vendor-stated | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Our platform currently retains Usenet messages that are more than 4,500 days old.
  - [2] 2026-11-03: retention is vendor-stated | capture: sha256:ffa34d9cf2429b382c0a0fa1e682a74d42faa31a9c29357bdb9c397084efb0fd | quote: Our platform currently retains Usenet messages that are more than 4,500 days old.
  - [1] 2026-11-03: the periodic plans VIPER10, VIPER50 and VIPERUNL state no download limit | capture: sha256:efff088dacaacf04bfe1771251af9da007064f1cbd9eeca0e79a094e072ff5e9 | quote: No download limit
  - [5] 2026-11-03: the vendor's retention page gives 4500+ for messages | capture: sha256:4b95b8c9a4c0f6863ab8e60e79fc195e8dcf3e8ff4fa673216c581232526b134 | quote: In ons geval is de retentie 4500+ voor berichten.
  - [3] 2026-11-03: third-party: soft 5 TB/month limit on the unlimited plans, still listed | capture: sha256:ce68343303ed49e39a8c4c999a557b78a25d3f976eb44da979781c00dd669f2c | quote: Vipernews/NovaUsenet have soft limits(5tb per month) on their unlimited plans you need to contact support if you encounter data cap on unlimited plans to get it reset.
  - [1] 2026-11-03: the entry price of USD 1.79 per month is unchanged | capture: sha256:efff088dacaacf04bfe1771251af9da007064f1cbd9eeca0e79a094e072ff5e9 | quote: Packages from only $1.79/mo.
- sources:
  - [1] https://www.vipernews.com/
  - [2] https://www.vipernews.com/faq/
  - [3] https://www.reddit.com/r/usenet/wiki/providers
  - [4] https://www.vipernews.com/sign-up/?plan=68
  - [5] https://www.vipernews.com/nl/usenet/begrippen/retentie/
