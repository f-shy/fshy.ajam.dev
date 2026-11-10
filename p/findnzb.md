# FindNZB

> findnzb.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/findnzb/ | JSON https://fshy.ajam.dev/api/v1/entity/findnzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FindNZB

- `debrid/findnzb` | qualifies-with-caveat | evidence reported | binding none | category Usenet binary search engine (HTML search, anonymous) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://findnzb.net/
- free tier: Reported as no registration required. The site offers search by filename, subject or author, a newsgroup browser and an RSS feed, and 'integrated Usenet downloading services to provide direct NZB download'. No daily counter is published. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1] | note: A direct request answered HTTP 522 from the edge.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: The search form offers an age filter up to 750 days; a third-party listing claims 'Up to 750 days, 2,000 newsgroups accessible'. | days: 750 | source: [1] | note: documented as the longest age filter offered, not measured
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [1]
- identity: anonymous | detail: Reported 'No registration required'; the search form and the page text show no login field. A download was not run.
- interface: rest
- limits:
  - request-rate: none published: no counter on the pages read [1]
- limits note: No request counter or byte counter is published. The origin timing out (HTTP 522 on the read date) is an availability problem that no vocabulary kind names; see reliability_note.
- binding note: No numeric limit is named on any page read; availability of the origin is what fails first and it is recorded in reliability_note.
- interface detail: HTML search form with an RSS feed advertised by the page; no Newznab API was found on the pages read.
- endpoint: https://findnzb.net/
- tooling: No Newznab API is described, so Prowlarr and NZBHydra2 cannot add it; a wrapper would parse the search page. That is a tooling note, not a verdict.
- composes with: A fallback search for a name that the API indexers lack; the origin timing out makes it unreliable as a first choice.
- reliability: A third-party listing says 'Almost always having downtime issues'; a direct request on the read date got HTTP 522 from the edge.
- evidence note: The no-registration claim and the downtime claim are third-party; the page text is first-party and the 522 is a probe. No search or NZB download was completed.
- extras:
  - price: USD 0
- evidence:
  - [1] 2026-11-03: the site says it offers direct NZB download through integrated downloading services | capture: sha256:2d91be56ccb748a40aec352f3d3e566c2eb340326ca7984b1a81fade3d448388 | quote: FindNZB integrated Usenet downloading services to provide direct NZB download.
  - [1] 2026-11-03: the longest age filter on the search form is 750 days | capture: sha256:2d91be56ccb748a40aec352f3d3e566c2eb340326ca7984b1a81fade3d448388 | quote: | Age of posts: | -- show all -- 24 hours 1 week 2 week 3 week 50 days 70 days 100 days 120 days 365 days 600 days 750 days |
  - [2] 2026-11-03: third-party: no registration is required | quote: No registration required.
  - [2] 2026-11-03: third-party: the site is almost always having downtime issues | quote: Almost always having downtime issues.
  - probe:https://findnzb.net/ 2026-11-03: a direct request answered HTTP 522 from the edge, so the origin timed out | capture: sha256:c70868864008b185194ffcffa5fa248266eaaa7472cd94f7ec2e6c7c60b34b1c | quote: "status": 522
- sources:
  - [1] https://findnzb.net/
  - [2] https://nzbhydra.com/indexers/
