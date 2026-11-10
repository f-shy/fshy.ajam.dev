# SpotNZB.com

> spotnzb.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/spotnzb/ | JSON https://fshy.ajam.dev/api/v1/entity/spotnzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SpotNZB.com (public Spotweb)

- `debrid/spotnzb-com` | qualifies | evidence measured | binding none | category Public Spotweb instance exposing a Newznab API | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://spotnzb.com/
- free tier: No account and no key. /api?t=caps returned 2,128 bytes with <limits max="500" default="50"/> and <registration available="no" open="no"/>; /api?t=search&q=linux returned 41,244 bytes with 50 items; /api?t=g&id=... returned a 7,346-byte NZB. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable per object; at most 500 results per request per caps | source: [1]
- retention: not published. Spotnet-derived catalogue; depth follows the Spotnet post history. | source: [1] | note: unverified
- egress: No metering and no account. | metered: no | source: [1]
- identity: anonymous | detail: Nothing: registration is declared unavailable and no key was needed for caps, search or get.
- interface: rest
- limits:
  - request-rate: none observed: 3 requests in one session, all 200 probe:https://spotnzb.com/api?t=search&q=linux
  - request-rate: 500 results per request maximum per caps [1]
- limits note: The 500/50 clamp was measured on the twin instance nzbserver.com, where limit=501 returns the 50-result default; the same code is running here (identical caps shape).
- binding note: No counter to hit; the same result-clamp caveat as nzbserver.com.
- interface detail: Newznab-shaped API at /api, caps type Spotweb version 0.1, with search, tv-search and get. No apikey was required.
- endpoint: https://spotnzb.com/api?t=search&q=<query> ; https://spotnzb.com/api?t=g&id=<message-id>
- tooling: Works as a generic Newznab indexer in Prowlarr and NZBHydra2, and therefore in Sonarr, Radarr and Lidarr, with no wrapper and no key. Same Spotweb surface as nzbserver.com.
- composes with: A second hostname for the same anonymous Spotnet index; useful as failover for nzbserver.com, not as extra coverage.
- reliability: Volunteer-run Spotweb instance with a stock placeholder email in caps; the NZB it served was byte-identical to nzbserver.com's, so the two go down together only if the shared backend does.
- notes: Listed in a community index of Usenet indexers as 'No accounts, Free'. Its caps is a stock Spotweb default, so it is a second front end rather than a separately curated index.
- evidence note: caps, search and download measured. The clamp detail is carried from the twin instance and is labelled as such rather than claimed as measured here.
- extras:
  - price: USD 0
  - measurements[0].url: https://spotnzb.com/api?t=caps&x=1
  - measurements[0].status: 200
  - measurements[0].bytes: 2128
  - measurements[0].sha256: 1ccee9cf5780092eee656be49d656aa5a0ed1c383ef8f0c8a9a492d2b6879751
  - measurements[1].url: https://spotnzb.com/api?t=search&q=linux&x=1
  - measurements[1].status: 200
  - measurements[1].bytes: 41244
  - measurements[1].sha256: 3ca43b75ce2773b715f082d11ca0049493ea211f3c6fd024d13aebef14dfa7d9
  - measurements[2].url: https://spotnzb.com/api?t=g&id=19XKJ8pokN4BLjUagNmQp@spot.net&x=1
  - measurements[2].status: 200
  - measurements[2].bytes: 7346
  - measurements[2].sha256: ac230711afeb760dee32b4ef20a83f42c339d7bfaa8a2bdafa46b482f3e0c6bc
  - nzb_is_newznab: yes
  - same_backend_as: nzbserver-com
- evidence:
  - probe:https://spotnzb.com/api?t=caps&x=1 2026-10-23: caps returned 200 and 2,128 bytes: type Spotweb, limits max 500 default 50, registration unavailable
  - probe:https://spotnzb.com/api?t=search&q=linux&x=1 2026-10-23: anonymous Newznab search returned 200 and 41,244 bytes with 50 items (sha256 3ca43b75...)
  - probe:https://spotnzb.com/api?t=g&id=19XKJ8pokN4BLjUagNmQp@spot.net&x=1 2026-10-23: anonymous NZB download returned 200, 7,346 bytes, 10 files, sha256 ac230711... identical to nzbserver.com's
- sources:
  - [1] https://spotnzb.com/api?t=caps
