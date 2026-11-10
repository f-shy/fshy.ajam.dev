# BinnewZ

> binnews.ninja | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/binnews/ | JSON https://fshy.ajam.dev/api/v1/entity/binnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BinnewZ

- `debrid/binnewz` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (French-language, open registration) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://binnews.ninja/
- free tier: Reported as free membership with 3 NZB grabs per day and forum access. The site did not answer on the read date, so nothing first-party was read. | unit: objects | metered on: request-count | read on: 2026-11-03 | source: [1] | note: unverified: the allowance is third-party; a direct request was closed by the origin without a response.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: A third-party listing claims 'Approximately 300 days of retention, 300 newsgroups indexed'. | source: [1] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up form could not be read; a listing calls registration open with optional donations of EUR 5 to 50 through PayPal.
- interface: unknown
- limits:
  - request-rate (binding): reported: 3 NZB grabs per day on free membership [1]
- binding note: The free grab counter is the only numeric limit named, and it is third-party.
- interface detail: A web index with a forum; no API was described by the source read.
- endpoint: https://binnews.ninja/
- tooling: Nothing about an API was read, so Prowlarr and NZBHydra2 support is unknown; the site was unreachable to every reader tried on the read date.
- composes with: A French-language fallback; 3 NZB grabs a day makes it a last-resort path.
- reliability: A direct request was closed by the origin without a response; a listing says it was 'Recently revived' with 97% uptime.
- evidence note: Every value is third-party; no first-party page could be read.
- extras:
  - price: USD 0 (free); donations EUR 5 to 50 (reported)
- evidence:
  - [1] 2026-11-03: third-party: free membership allows 3 NZB grabs per day | quote: Free membership includes 3 NZB grabs/day and forum access.
  - [1] 2026-11-03: third-party: about 300 days of retention and 300 newsgroups | quote: Approximately 300 days of retention, 300 newsgroups indexed
  - probe:https://binnews.ninja/ 2026-11-03: a direct request was closed by the origin without a response | capture: sha256:147508c4303270593971c12420fbeeb3a92e98ac649735ca2df4de2c99830ef4 | quote: "error": "reset"
- sources:
  - [1] https://nzbhydra.com/indexers/
