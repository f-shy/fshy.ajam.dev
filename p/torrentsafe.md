# TorrentSafe

> torrentsafe.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torrentsafe/ | JSON https://fshy.ajam.dev/api/v1/entity/torrentsafe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TorrentSafe

- `debrid/torrentsafe` | fails-quota | evidence documented | binding per-object-cap | category torrent-to-cloud fetcher | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:55:00.000Z (live) | stale on 2026-11-23
- url https://www.torrentsafe.com/
- price free under 1 GB per file; premium reported at about USD 4.95/month | parsed USD 4.95/mo
- free tier: 'Free users can download unlimited files per month under 1GB at full speed.' No registration is required; an email is used only to send a licence key. | unit: requests | metered on: object-count | read on: 2026-10-23 | source: [1] | note: unlimited count, 1 GB per file - the mirror image of TorBox's 10 files at 10 GB
- per-object cap: 'under 1GB' per file on the free tier. Paid is described as unlimited file size; a third-party review puts the premium single-file ceiling near 1.1 TB. | bytes: 1000000000 | source: [1] | note: the 1 GB figure is the only hard number on the vendor page
- retention: Not stated on the vendor page. Third-party reviews report a two-day file lifetime on free accounts and seven days on paid. | days: 2 | source: [2] | note: reported, not vendor-documented
- egress: Free files are downloaded 'at full speed'; no byte allowance is published. Premium is advertised as having no storage or transfer rate limits. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: no registration to download: 'Am I required to provide my information or register to use TorrentSafe? No, your E-mail address is only used to send your license key.'
- interface: rest
- limits:
  - per-object-cap (binding): 1 GB per file on free [1]
  - request-rate: reported 5 downloads per month on free accounts (Chrome Web Store listing); the vendor FAQ says unlimited [3]
- limits note: the vendor FAQ and the vendor's own Chrome listing disagree on the free download count. The conservative reading is the smaller number, but the FAQ sentence is the one on the homepage.
- binding note: A 20 GiB torrent is 21 times the 1 GB free cap, so size fails before the disputed monthly count matters.
- interface detail: browser only: 'There is no software. Our service works directly through this webpage.' Downloads arrive as HTTPS links from the My Downloads page; no API is documented.
- tooling: browser, plus a Chrome extension that posts magnets; Dropbox upload is supported with a user-supplied app token. No API, no CLI.
- composes with: the account-free fetch hop: a torrent under 1 GB is fetched and returned as an HTTPS link without signup, which makes it the cheapest way to test whether a tracker or a magnet resolves at all.
- reliability: third-party tests report slow transfers and a media player that fails on common formats; the site runs on plain Apache without a CDN and its pricing URL is a 404.
- notes: Included because it is the only service here that returns a fetched file without any account and without a published byte quota - useful as a resolver test even though the 1 GB cap rules out the 20 GiB case.
- evidence note: the free-tier sentence and the no-registration claim are from the vendor homepage today. Retention and the monthly count are third-party, and the vendor's own pages contradict each other on the count.
- extras:
  - registration: none for free
  - pricing_url: 404 at /pricing
- evidence:
  - [1] 2026-10-23: 'Free users can download unlimited files per month under 1GB at full speed', and 'No, your E-mail address is only used to send your license key'
  - [2] 2026-10-23: reported: free lifetime 2 days, premium 7 days, premium from $4.95/month
  - [3] 2026-10-23: the extension listing states 'Free users limited to 5 downloads per month', contradicting the homepage
- sources:
  - [1] https://www.torrentsafe.com/
  - [2] https://vpnetic.com/blog/torrent-safe/
  - [3] https://chromewebstore.google.com/detail/torrentsafe/lokbhemjpeifblfhlmbbojahimbmdmai
