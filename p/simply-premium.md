# Simply-Premium

> simply-premium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simply-premium/ | JSON https://fshy.ajam.dev/api/v1/entity/simply-premium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Simply-Premium

- `debrid/simply-premium` | qualifies-with-caveat | evidence reported | binding volume-quota | category German multi-hoster debrid with usenet and torrent | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-07
- url https://www.simply-premium.com/
- price EUR 10.00 per 30 days (reported), capped at 1000 GB | parsed USD 11.19/mo
- free tier: None published. The home page offers 'over 20 sharehosters with the advantages of premium accounts' and lists Usenet and P2P as features; no free plan, trial or credit is mentioned on the home page or the hoster page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not stated; the vendor publishes per-host daily traffic caps instead (2 GB for hitfile.net up to 250 GB for 1fichier, ddownload, filestore.to, mega.co.nz and YouTube) | source: [2]
- retention: not applicable: a link generator, nothing is stored after the transfer | source: [1]
- egress: No speed limit is applied ('We do not limit the download speed'), but a monthly account cap of 1000 GB is reported by a third-party comparison. | metered: yes | price per TB: EUR 10.00 per 30 days up to 1000 GB (reported, not vendor-stated) | source: [3]
- identity: email | detail: An account is needed to buy and to generate links; the fields were not read because the checkout was not entered. Email is the minimum such a site implies.
- interface: unknown
- limits:
  - volume-quota (binding): max 1000 GB per month (reported) [3]
  - volume-quota (binding): per-host daily caps from 2 GB (hitfile.net) to 250 GB (1fichier, ddownload, filestore.to, mega.co.nz, youtube.com) [2]
- limits note: Hosts carry a 'Factor' (1.0 to 5.0) that multiplies the traffic counted against the account; k2s.cc and turbobit.net are the 5.0 hosts, so a gigabyte there costs five.
- binding note: The daily per-host cap binds before the monthly 1000 GB does: one 250 GB day on 1fichier is a quarter of the month, and a 5.0-factor host turns 200 GB of real traffic into the whole monthly allowance.
- interface detail: Web interface plus 'Multiple download managers supported' and 'Many One Click Hoster are supported'; no documented API and no protocol endpoint is named on the site.
- tooling: Download-manager integration is claimed generically; no JDownloader plugin name, CLI or API is documented.
- composes with: The usenet and torrent support means one German account can replace both a usenet provider and a debrid subscription for a client who only needs host links plus the occasional NZB.
- reliability: Per-host traffic factors up to 5.0 mean the advertised monthly volume is not the usable volume on premium hosts; the site publishes no status page.
- notes: The vendor's own price is not on any page reachable today: /premium and /preise both 404, so the EUR 10/30 days figure is third-party and a reader should re-check at checkout. The factor column is the part a comparison site omits: EUR 10 buys 1000 GB of counted traffic, which on k2s.cc (factor 5.0) is 200 GB of files.
- evidence note: The host list, factors and daily caps are vendor pages read; the price and the 1000 GB monthly cap come from a third-party German comparison (multio.ch) because the vendor's own pricing page returned 404 at /premium and /preise. A vendor-stated price would raise this to documented.
- evidence:
  - [2] 2026-10-23: 19 hosts with a traffic factor (1.0-5.0) and a daily traffic cap each, from 2 GB (hitfile.net) to 250 GB (1fichier, ddownload, filestore.to, mega.co.nz, youtube.com)
  - [1] 2026-10-23: 'over 20 sharehosters', 'We do not limit the download speed', and the Usenet and P2P feature blocks
  - [3] 2026-10-23: third-party price of '10 € / 30 Tage, 70 € / 360 Tage' and 'Max. 1000 GB pro Monat, Tageslimits je Hoster'
- sources:
  - [1] https://www.simply-premium.com/
  - [2] https://www.simply-premium.com/hoster
  - [3] https://multio.ch/
