# DrunkenSlug

> drunkenslug.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/drunkenslug/ | JSON https://fshy.ajam.dev/api/v1/entity/drunkenslug.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DrunkenSlug

- `debrid/drunkenslug` | fails-identity | evidence documented | binding write-gated | category Usenet indexer (Newznab API, invite-only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://drunkenslug.com/
- free tier: Reported as 5 NZB downloads and 25 API hits per day on the free 'Water' tier; Lager EUR 5/year gives 25 downloads and 250 API calls a day, Ale EUR 10/year 100 and 1,000, Wine EUR 20/year 200 and 2,000. The vendor's caps declares <limits max="100" default="100"/> and <registration available="yes" open="no"/>. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: Free API allowance is disputed: usenetreviews.org and bestnzbsites say 100 hits/day, a 2023 registration thread says 25, and usenet.com says 'a small number'. The conservative 25 is kept.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not stated by the vendor on any page reachable today; a third-party listing claims '3000+ days for binary'. | source: [2] | note: reported
- egress: No byte metering; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Invite only. The register page says 'Sorry! The Bar is closed. Please don't contact us asking for invites.' caps agrees: <registration available="yes" open="no"/>.
- interface: rest
- limits:
  - request-rate: 5 NZB downloads and 25 API hits per day on the free tier [3]
  - request-rate: 100 results per request maximum [1]
- limits note: The hard gate is registration, not the counter: nobody without an invite reaches the counter.
- binding note: The invite gate is what fails first, before any quota is reached: without an account the 5 grabs cannot be spent at all. If an account existed, the daily counter would bind instead.
- interface detail: Newznab API at /api; caps answers anonymously with 100 results per request. The HTML site is behind Cloudflare and returns 403 to automated request egress on every path tried (/, /register, /plans, /faq, /help, /support, /donate, /subscribe, /store), while /api answers normally.
- endpoint: https://drunkenslug.com/api?t=caps ; https://drunkenslug.com/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab: Prowlarr, NZBHydra2, Sonarr and Radarr add it with URL plus key once an account exists.
- composes with: A depth index for older and rarer material behind a 5-grab-a-day free cap; it complements a broad index rather than replacing one.
- reliability: Registration opens for short windows and closes again, so an account is an asset that cannot be recreated on demand if lost.
- notes: The /api path answering while every HTML path is challenged is itself the useful finding: an indexer the browser cannot open still exposes caps, so registration state and result limits are readable without an account.
- evidence note: Registration closure is documented from the vendor's own register page and caps. The free allowance is third-party, and the record's verdict does not depend on it.
- extras:
  - price: EUR 5/year Lager; free tier 5 downloads/day
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: no
- evidence:
  - probe:https://drunkenslug.com/api?t=caps&x=1 2026-10-23: caps returned 200 and 3,247 bytes: title DS, <limits max="100" default="100"/>, <registration available="yes" open="no"/>
  - [4] 2026-10-23: vendor text via search snippet: 'Sorry! The Bar is closed. Please don't contact us asking for invites.' The direct fetch of the page returned a Cloudflare 403.
  - probe:https://drunkenslug.com/ 2026-10-23: HTML site returns 403 with a Cloudflare 'Attention Required' body (4,556 bytes); /api is unaffected
  - [5] 2026-10-23: third-party tier table: Water free 5 NZBs; Lager 25/250 at EUR 5; Ale 100/1,000 at EUR 10; Wine 200/2,000 at EUR 20
- sources:
  - [1] https://drunkenslug.com/api?t=caps
  - [2] https://bestnzbsites.com/item/drunkenslug
  - [3] https://forums.redflagdeals.com/drunkenslug-registration-open-2644891/
  - [4] https://drunkenslug.com/register
  - [5] https://www.usenet.com/drunkenslug-nzb-review/
