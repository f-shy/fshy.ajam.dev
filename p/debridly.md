# Debridly

> debridly.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debridly/ | JSON https://fshy.ajam.dev/api/v1/entity/debridly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debridly

- `debrid/debridly` | qualifies-with-caveat | evidence documented | binding volume-quota | category multi-hoster (premium link generator) | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:39:03.000Z (live) | stale on 2026-11-23
- url https://debridly.com/premium
- price USD 49.99/year (USD 4.17/month) or USD 7.99/30 days | parsed USD 4.17/mo
- free tier: Create a free account to start generating direct premium download links from Rapidgator, Nitroflare, 1Fichier, Mega, and dozens of other file hosts. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1] | note: A free account exists but no free allowance is published anywhere on the pages read. The step list says 'Your account status, email verification, host availability, and daily bandwidth limits are checked before a premium link is delivered', so a free account has some daily limit; the number is not stated. Premium is what the per-host caps on the hosts page belong to ('Debridly Premium includes up to 200 GB of 1Fichier downloads per 24 hours').
- per-object cap: not applicable: a URL is unlocked and a direct link returned; nothing is stored by Debridly | source: [1]
- retention: Direct links are valid for 24 hours on Premium ('24h link validity'). | days: 1 | source: [2]
- egress: Direct CDN links from the host's own servers with 'no throttling added by Debridly'. Counted per host per 24 hours, reset at 00:00 UTC. | metered: yes | free allowance: unpublished free allowance; Premium caps per host, e.g. 200 GB/24h on 1Fichier | source: [3]
- identity: email | detail: A free account needs only an email, and the generator checks 'email verification' before issuing a link. Premium is a one-time Stripe-style purchase; no card is needed for the free account.
- interface: rest
- limits:
  - volume-quota (binding): per-host daily cap, e.g. 200 GB per 24 h on 1Fichier, 100 GB on 4Share and FileBlade, 50 GB on Alfafile/DepositFiles/FileFactory, 20 GB on Ddownload/ClickUpload, 5 GB on Emload/FileAxa, 3 GB on DaoFile, 2 GB on FileDot [4]
  - retention-clamped: generated links live 24 hours [2]
  - per-ip-shaping: no published concurrency number; the generator checks 'email verification, host availability, and daily bandwidth limits' before delivering a link [1]
  - pull-count: generated links expire after 24 hours [2]
- limits note: Some hosts are marked Offline in the list (daofile.com 'Offline Daily cap 3 GB' on the read date). The premium page warns that hosts such as Rapidgator and Tezfiles sell a separate premium package for 'exclusive' content that Debridly cannot unlock.
- binding note: At 1 TiB/month the per-host daily cap is the constraint that binds: 200 GB/day on 1Fichier is 6 TB/month, but a month spread over the 2-5 GB hosts (FileDot, Emload, DaoFile) hits their caps at tens of GB, so host mix decides whether 100 GiB is reachable at all.
- interface detail: Web generator that returns a direct URL; the page lists file name, size, host and expiry. No public API documented on the pages read.
- tooling: Any HTTP client on the returned direct URL; the site says 'No browser extensions or software required', which is also a note that no CLI exists.
- composes with: The published per-host caps make it the only provider among debrid providers where a reader can plan a month: 200 GB/day on 1Fichier alone is 6 TB/month, far past the 1 TiB monthly volume, so the annual USD 49.99 is the cheapest documented route over 100 GiB.
- reliability: Per-host caps are enforced at generation time and nothing is deducted when a link fails with LINK_D0WN; hosts listed Offline return nothing; premium cannot unlock hosts' own 'exclusive' tiers.
- notes: The only provider among debrid providers that publishes a numeric per-host daily cap instead of an 'unlimited' adjective. The annual term is sub-USD-5 per month; the 30-day term is not. Free tier exists but its allowance is unpublished, which is why the record is priced at the premium tier. The hosts page count differs between the page text ('90+ hosts') and the premium page ('70+ supported hosts'), so the true count is between the two. The newest service in the set and the only one with no archive footprint whatsoever, so it is a price with no history rather than a stable price. Its 365-day term at USD 49.99 is the second-cheapest annual in the set after OffCloud's EUR 40.
- evidence note: Prices and the per-host caps are quoted from the vendor's own pages. The free tier's allowance is unstated, so the free half of the record is unverified.
- extras:
  - host_caps_sampled.1fichier: 200 GB/24h
  - host_caps_sampled.4share.vn: 100 GB/24h
  - host_caps_sampled.fileblade: 100 GB/24h
  - host_caps_sampled.filecat: 100 GB/24h
  - host_caps_sampled.alfafile: 50 GB/24h
  - host_caps_sampled.ddownload: 20 GB/24h
  - host_caps_sampled.emload: 5 GB/24h
  - host_caps_sampled.filedot: 2 GB/24h
  - hosts_claimed: 70+ on the premium page, 90+ on the home page
  - price_history[0].date: 2026-10-23
  - price_history[0].price: USD 1.89 / 2 days
  - price_history[0].plan: 2 Days
  - price_history[0].source_url: https://debridly.com/premium
  - price_history[1].date: 2026-10-23
  - price_history[1].price: USD 7.99 / 30 days
  - price_history[1].plan: 30 Days
  - price_history[1].source_url: https://debridly.com/premium
  - price_history[2].date: 2026-10-23
  - price_history[2].price: USD 18.99 / 90 days
  - price_history[2].plan: 90 Days
  - price_history[2].source_url: https://debridly.com/premium
  - price_history[3].date: 2026-10-23
  - price_history[3].price: USD 49.99 / 365 days
  - price_history[3].plan: 365 Days
  - price_history[3].source_url: https://debridly.com/premium
  - price_history_status: unread
  - price_history_note: No capture of the domain exists at any date.
  - change_36m: unknown
  - currency: USD
  - usenet: no
- evidence:
  - [2] 2026-10-23: USD 1.89 / 2 days, USD 3.99 / 7 days, USD 7.99 / 30 days, USD 18.99 / 90 days, USD 49.99 / 365 days, each 'All 70+ supported hosts', 'Maximum daily caps per host', '24h link validity'
  - [4] 2026-10-23: per-host daily caps: '1Fichier 1fichier.com Online Daily cap 200 GB', '4Share 4share.vn Online Daily cap 100 GB', 'DDownload ddownload.com Online Daily cap 20 GB', 'Emload emload.com Online Daily cap 5 GB', 'FileDot filedot.xyz Online Daily cap 2 GB', 'DaoFile daofile.com Offline Daily cap 3 GB'
  - [3] 2026-10-23: 'Debridly Premium includes up to 200 GB of 1Fichier downloads per 24 hours. The counter resets at 00:00 UTC' and that a failed link deducts nothing
  - [1] 2026-10-23: 90+ hosts claimed, free account offered, and the pre-generation check of 'account status, email verification, host availability, and daily bandwidth limits'
  - [2] 2026-10-23: 2/7/30/90/365 days at USD 1.89/3.99/7.99/18.99/49.99, 'All 70+ supported hosts', 'Maximum daily caps per host', '24h link validity'
  - [5] 2026-10-23: the archive holds no capture of this domain, so no earlier price can be established
- sources:
  - [1] https://debridly.com/
  - [2] https://debridly.com/premium
  - [3] https://debridly.com/premium-link-generator/1fichier
  - [4] https://debridly.com/hosts
  - [5] https://web.archive.org/cdx/search/cdx?url=debridly.com&output=json&fl=timestamp&limit=3
