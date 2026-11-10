# OkDebrid

> okdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/okdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/okdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OkDebrid

- `debrid/okdebrid` | qualifies-with-caveat | evidence documented | binding pull-count | category premium-link generator (free, no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://okdebrid.com/
- price USD 0
- free tier: Free premium link generator; the FAQ says 'Right now, you can to unrestrict almost 8 files per day.' | unit: objects | metered on: object-count | read on: 2026-10-23 | source: [1] | note: 'almost 8' is the vendor's hedge, so the cap is soft.
- per-object cap: 'We don't bother you with annoying file size limits.' | source: [1] | note: Stated only. The upstream host's own per-file cap still applies.
- retention: 'We will remove your premium link once you finish downloading the file.' | days: 0 | source: [1]
- egress: Served from OkDebrid's servers at '100% full download speed'. No byte allowance, no price. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: No registration. The generator runs against the caller's IP.
- interface: unknown
- limits:
  - pull-count (binding): about 8 files per day [1]
  - per-ip-shaping: 'The generated premium link is locked and only accessible to the user that initiated the link generator' [1]
- limits note: Claims to support 'about +100 cloud hosters' without publishing the list on the page read.
- binding note: The daily file count is the only stated ceiling. No byte figure exists to bind against.
- interface detail: Web form only: 'Enter your link', 'Get Premium Link', download. No API or CLI published.
- tooling: browser only.
- composes with: Same slot as DebridHub: a zero-identity leecher for a few files a day. Eight files is below any real batch, so it is a spot tool.
- reliability: IP-locked links break on an egress change. The vendor advertises antivirus scanning of processed files, which is a scan of somebody else's file and not a guarantee about content.
- notes: Copy matches DebridHub's page almost word for word, including the eight-links cap and the IP-lock sentence. Treat them as one product with two domains until someone compares their generated output.
- evidence note: Cap read on the vendor's FAQ. One completed download would raise it to measured.
- extras:
  - hosts_claimed: 100+
  - twin: debridhub.com
- evidence:
  - [1] 2026-10-23: 'you can to unrestrict almost 8 files per day', the IP-locked link sentence, and the +100-host claim
- sources:
  - [1] https://okdebrid.com/
