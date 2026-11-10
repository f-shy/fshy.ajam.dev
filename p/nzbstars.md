# NZBStars

> nzbstars.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbstars/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbstars.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBStars

- `debrid/nzbstars` | qualifies-with-caveat | evidence reported | binding none | category Usenet indexer (Spotnet-based, web and API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://www.nzbstars.com/
- free tier: Reported as 'Completely free', no registration required, with unlimited API calls and no RSS feeds. The page shows a search form, a category tree and a donate prompt, and also Login and Add user links. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1] | note: The third-party 'no registration' claim and the page's Login and Add user links were not reconciled; no search or download was run.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [2]
- retention: A third-party listing claims 'Approximately 1,400 days of retention'. | source: [1] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [2]
- identity: anonymous | detail: Reported 'No registration required'; the page also exposes Login and Add user links, so whether a search or an NZB needs an account was not confirmed.
- interface: rest
- limits:
  - request-rate: reported: unlimited API calls; none published on the page read [1]
- binding note: No numeric limit is named by any source read.
- interface detail: Web search with a Spotnet-style category tree; a third-party listing says it provides an API with unlimited calls. The API path was not read.
- endpoint: https://www.nzbstars.com/
- tooling: Third-party listings call it Spotnet-based with an API; whether Prowlarr or NZBHydra2 can add it was not tested. The origin answered a direct request with a bot challenge (HTTP 403) and the page was readable only through a pinned reader.
- composes with: A free fallback search for Dutch-oriented Spotnet releases when the paid indexers lack a name.
- reliability: A direct request on the read date was answered with a bot challenge (HTTP 403); a third-party listing reports 98% uptime.
- evidence note: The free, unlimited and no-registration claims are third-party; the page text shows the Login and Add user links. Nothing was exercised.
- extras:
  - price: USD 0 (donations optional)
- evidence:
  - [1] 2026-11-03: third-party: no registration, completely free, unlimited API calls | quote: No registration required. Completely free. Unlimited API calls, no RSS feeds.
  - [1] 2026-11-03: third-party: the listing claims about 1,400 days of retention | quote: Approximately 1,400 days of retention
  - [2] 2026-11-03: the live page asks for donations and has no paid tier on it | capture: sha256:8d7e10ccc4e64a077e37d9a3fec8478d3a6d88f1cb3480e527da74ad59e8555e | quote: Please support us,Donate, keep the server running!
  - [2] 2026-11-03: the page exposes an Add user link next to Login | capture: sha256:8d7e10ccc4e64a077e37d9a3fec8478d3a6d88f1cb3480e527da74ad59e8555e | quote: - [Add user](https://www.nzbstars.com/)
- sources:
  - [1] https://nzbhydra.com/indexers/
  - [2] https://www.nzbstars.com/
