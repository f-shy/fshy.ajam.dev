# Cocoleech

> cocoleech.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cocoleech/ | JSON https://fshy.ajam.dev/api/v1/entity/cocoleech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cocoleech

- `debrid/cocoleech` | paid-only | evidence documented | binding volume-quota | category multi-hoster (premium link generator, JDownloader integration) | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:39:03.000Z (live) | stale on 2026-11-23
- url https://members.cocoleech.com/pricing
- price USD 14.99/month; USD 6.66/month on the annual term | parsed USD 6.66/mo
- free tier: A Free plan exists on the members dashboard ('Your Plan - Free - No active plan') with 'higher daily quotas' reserved for Premium. The free allowance itself is not published on any public page read. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1] | note: Per-host pages publish one number, e.g. 'Daily limit: 30 GB' for Rapidgator, without saying which tier it belongs to. A JDownloader board post from a user reports 1 GB/day as a guest; a 2018 review reports 13 hosts for free users. Both are third-party and old, so the free number stays unverified.
- per-object cap: not applicable: Cocoleech does not host files ('Cocoleech does not host files.') | source: [1]
- retention: not applicable: temporary links only. 'Create a temporary accelerated link'. | source: [1]
- egress: Transfers run over a '10 Gbps backbone'; per-host daily limits apply and are shown per host. No total monthly byte allowance is published. | metered: yes | free allowance: unpublished; per-host 'Daily limit' figures such as 30 GB on Rapidgator | source: [2]
- identity: email | detail: Premium is a voucher key emailed after payment; checkout is Paddle (card, Apple Pay, Google Pay, iDEAL), PayPal, CoinPayments crypto, Difmark or Paysafecard. No phone and no card are needed for a free account.
- interface: rest
- limits:
  - volume-quota (binding): per-host daily limits, e.g. 'Daily limit: 30 GB' on Rapidgator and 'Daily limit: 5 GB' on Filefox [2]
  - request-rate: free plan is queued behind premium; 'Higher Quotas' is the advertised premium delta [1]
- limits note: The generator reports 'Maintenance' and 'Daily limit: 30 GB' side by side on the Rapidgator page, so a host can be both limited and degraded.
- binding note: The per-host daily cap is the only published number and it differs per host, so 1 TiB of monthly transfer depends on spreading files across hosts; the 30 GB/day Rapidgator cap alone is 900 GB/month.
- interface detail: Web generator, Chrome and Firefox extensions, and a JDownloader 2 plugin. No public API documented on the pages read.
- tooling: JDownloader 2 plugin, Chrome and Firefox extensions. That is the widest first-party tooling of the small providers among debrid providers.
- composes with: Its JDownloader plugin makes it the least-friction free generator for a headless client, but at USD 14.99/month it is three to five times the sub-USD-5 providers, so it is a fallback for tooling, not for price.
- reliability: A 2021 test by multihosts.de reported that Cocoleech 'completely discontinued its free service' and later pages still show a Free plan, so the free tier's existence has been unstable across years; per-host limits and 'Maintenance' states change without notice.
- notes: Above the debrid USD 5 bar on every term except the annual equivalent, which is still USD 6.66. Included because it is the most-cited small multi-hoster in the JDownloader ecosystem and because its per-host daily caps are a worked example of the shape: a total 'unlimited' claim paired with per-host GB/day numbers. Free tier is asserted by the dashboard and contradicted by a 2021 report; both are kept.
- evidence note: Prices, the plan structure and the per-host daily limits are from the vendor's own pages. The free allowance is unverified, so the free half of the claim rests on a third-party 2021 report.
- extras:
  - hosts_claimed: 50+
  - per_host_caps.rapidgator: 30 GB/day
  - per_host_caps.filefox: 5 GB/day
  - tooling: JDownloader 2 plugin, Chrome extension, Firefox extension
- evidence:
  - [3] 2026-10-23: USD 14.99 / 1 month (31 days), USD 29.99 / 3 months ('$9.99/mo equivalent'), USD 79.99 / 1 year ('$6.66/mo equivalent'), one-time payment, no automatic renewals, '10 Gbps backbone'
  - [2] 2026-10-23: 'Maintenance Daily limit: 30 GB' for Rapidgator, 'Auth: No Rapidgator.net account needed', and the 'Limit reached - Daily quota hit for this host' error text
  - [4] 2026-10-23: 'Daily limit: 5 GB' on a second host, confirming the cap is per host and not per account
  - [5] 2026-10-23: third-party report that in April 2021 'the provider has completely discontinued its free service' (reported, not observed)
  - [6] 2026-10-23: user report that a Cocoleech guest can download 'bis zu 1GB/Tag' across hosts (reported)
- sources:
  - [1] https://members.cocoleech.com/
  - [2] https://members.cocoleech.com/premium-link-generator/rapidgator
  - [3] https://members.cocoleech.com/pricing
  - [4] https://members.cocoleech.com/premium-link-generator/filefox
  - [5] https://multihosts.de/en/premium-link-generator/
  - [6] https://board.jdownloader.org/showthread.php?t=89923
