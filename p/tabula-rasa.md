# Tabula Rasa

> tabula-rasa.pw | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tabula-rasa/ | JSON https://fshy.ajam.dev/api/v1/entity/tabula-rasa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tabula Rasa

- `debrid/tabula-rasa` | fails-identity | evidence documented | binding write-gated | category Usenet indexer (Newznab API, closed registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.tabula-rasa.pw/
- free tier: Free accounts are view-only as of March 2026: 'all new user accounts are view only ... you cannot use the API or download NZBs, just view the releases'. caps declares <registration available="no" open="no"/> and <limits max="500" default="250"/>. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Older reviews still say '10 downloads and 100 API queries daily' for free; that reading is contradicted by the March 2026 admin statement and is not used.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not published on any page reachable today; a third-party listing claims 'up to 100 days for binary files, 50+ indexed groups'. | source: [2] | note: reported
- egress: No byte metering; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Closed. caps declares registration available=no; a third-party status tracker records 'Registration closed / site offline' as of 2026-10-06.
- interface: rest
- limits:
  - request-rate: 0 API hits and 0 NZB downloads on a free account (view only) [3]
  - write-gated (binding): registration unavailable; new accounts are created view-only when the door opens [1]
  - request-rate: 500 results per request maximum [1]
- binding note: Registration fails first: available=no in the vendor's own caps, so a client cannot reach a quota to be limited by.
- interface detail: Newznab API at /api, 500 results per request (the highest cap among debrid providers). The HTML site answers a Cloudflare 'Just a moment' interstitial to network requests on every path tried.
- endpoint: https://www.tabula-rasa.pw/api?t=caps ; https://www.tabula-rasa.pw/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab and the reference testbed for the NNTmux software other indexers run, so its API shape matches what Prowlarr and NZBHydra2 expect. The account is the obstacle, not the user.
- composes with: Nothing on the free side; it becomes a broad index only on a paid supporter tier, which cannot be obtained while registration is shut.
- reliability: New free accounts receive no API key and no download right even when registration opens, so an account created on a good day still cannot be used by an arr stack.
- evidence note: caps and the registration state were measured; the view-only free tier is a dated third-party quote of an admin statement and is labelled as such.
- extras:
  - price: USD 15/year supporter (reported)
  - nzb_is_newznab: yes
  - caps_limits: 500
  - registration_open: no
- evidence:
  - probe:https://www.tabula-rasa.pw/api?t=caps&x=1 2026-10-23: caps returned 200 and 125,232 bytes: title Tabula Rasa, <limits max="500" default="250"/>, <registration available="no" open="no"/>
  - probe:https://www.tabula-rasa.pw/ 2026-10-23: the HTML site answered a Cloudflare 'Just a moment...' interstitial (5,821 bytes, 403), so no page text was readable directly
  - [3] 2026-10-23: third-party, dated Mar 2026: 'all new user accounts are view only ... you cannot use the API or download NZBs'
  - [4] 2026-10-23: third-party status, checked 2026-10-06: 'Registration closed / site offline'
- sources:
  - [1] https://www.tabula-rasa.pw/api?t=caps
  - [2] https://nzbhydra.com/indexers/
  - [3] https://usenetalmanac.com/indexer/tabula-rasa/
  - [4] https://www.bestnzbsites.com/sites/tabula-rasa/
