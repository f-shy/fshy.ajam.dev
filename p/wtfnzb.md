# WtfNZB

> wtfnzb.pw | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wtfnzb/ | JSON https://fshy.ajam.dev/api/v1/entity/wtfnzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WtfNZB

- `debrid/wtfnzb` | qualifies-with-caveat | evidence reported | binding none | category Usenet indexer (web only, no Newznab API found) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:53.665Z (live) | stale on 2026-11-18
- url https://wtfnzb.pw/
- free tier: Reported as no registration and unlimited NZB downloads for free users, with donors getting more API access. No Newznab API answered: every /api variant tried returned the HTML home page. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not stated on any page reachable | source: [1] | note: unverified
- egress: No byte metering reported; the site serves pointers. | metered: no | source: [1]
- identity: anonymous | detail: Reported 'No registration required' by a third-party listing. The site's /register and /login paths answer HTTP 403 behind a Cloudflare 'Just a moment...' challenge on 2026-11-03, so whether an account is needed is unverified.
- interface: rest
- limits:
  - request-rate: reported unlimited NZB downloads for free users; donors get more API access [2]
- binding note: Nothing measured could bind: no API, no account and no published counter. Naming a kind here would be invention.
- interface detail: HTML site only. /api?t=caps and /api.php return 200 with text/html and the site's own page (7,571 bytes on 2026-11-03), so no Newznab surface is exposed at the addresses a client would try.
- endpoint: https://wtfnzb.pw/
- tooling: A wrapper has to drive the web UI; Prowlarr and NZBHydra2 cannot add it as a Newznab indexer. The absence of an API is a tooling note, not a verdict.
- composes with: A manual fallback for a name when every API indexer has failed; not automatable without a scraper.
- reliability: A third-party listing records it as 'in heavy development with frequent downtime', so a scraper should expect intermittent failure.
- notes: Four API paths returning the home page is the shape of a single-page app with a catch-all route, not of a retired API. A client that needs automation should look for an API on a subdomain before concluding there is none.
- evidence note: The absence of a Newznab endpoint was measured across four candidate paths; the free, unlimited, no-registration claim and the reliability note are third-party.
- extras:
  - price: USD 0 (donation model)
  - nzb_is_newznab: no
- evidence:
  - probe:https://wtfnzb.pw/api?t=caps 2026-10-23: returned 200 with text/html and the site front page, 6,457 bytes, not a caps document
  - probe:https://wtfnzb.pw/api.php?t=caps 2026-10-23: same: 200, text/html, front page
  - [2] 2026-10-23: third-party: 'No registration required. Unlimited NZB downloads for free users. Donors get more API access.' and 'in heavy development with frequent downtime'
  - probe:https://wtfnzb.pw/register 2026-11-03: the /register path answers HTTP 403 behind a Cloudflare 'Just a moment...' challenge | capture: sha256:00082065ddf583dd77c51cad5f714f6d7267d5092996e789c8663cbb72663127 | quote: "status": 403
  - probe:https://wtfnzb.pw/api?t=caps 2026-11-03: the api caps path answers 200 with a 7,571 byte text/html page, not a caps document | capture: sha256:d019f012c5624ca1de6f2afb527594a226a812d6e60aa7fefa7e59f2ae132dd7 | quote: "bytes": 7571
  - probe:https://wtfnzb.pw/login 2026-11-03: the /login path answers HTTP 403 behind a Cloudflare 'Just a moment...' challenge | capture: sha256:c867ce5479ba3c7c27c1f55d5aee8bf7b5e4d856f8b825866ab0f3f138a27bb5 | quote: "status": 403
  - [1] 2026-11-03: the front page identifies the site as a usenet indexing community site | capture: sha256:889b25e60b7dc3cac231d12d37f7fe74acccbf51991c13eb4250949da91e0c39 | quote: A usenet indexing community site.
- sources:
  - [1] https://wtfnzb.pw/
  - [2] https://nzbhydra.com/indexers/
