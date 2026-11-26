# NZBScout

> nzbscout.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbscout/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbscout.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBScout

- `debrid/nzbscout` | qualifies-with-caveat | evidence reported | binding none | category Usenet indexer (NZB search and download) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-26T01:59:17.873Z (live) | stale on 2026-12-11
- url https://nzbscout.com/
- free tier: This domain name may be for sale. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1] | note: Not exercised: a direct request timed out on the read date, so no search or NZB download was run.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [2]
- retention: A third-party listing claims 'files available dating back approximately 10 years'. The home page lists posts dated between 2013 and 2021. | source: [1] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [2]
- identity: email | detail: unverified: a third-party listing says 'Open registration' and 'Completely free'; the register page returned no readable content and the home page shows no login field in the text read.
- interface: browser
- limits:
  - request-rate: reported: no usage limits; none published on the pages read [1]
- binding note: No numeric limit is named by any source read.
- interface detail: Web search and download pages; no API was described on the pages read.
- endpoint: https://nzbscout.com/
- tooling: No Newznab API was found on the pages read, so Prowlarr and NZBHydra2 may not add it; a wrapper would parse the pages. That is a tooling note, not a verdict.
- composes with: A fallback for older releases; the newest post dates on the home page are from 2021, so it does not replace a current indexer.
- reliability: A direct request timed out; the home page text was read from another route.
- notes: No programmatic path found: Web search and download pages; no API was described on the pages read.
- evidence note: The free claim and the registration claim are third-party; the home page text is first-party and shows the post dates. No search or download was run.
- extras:
  - price: USD 0
- evidence:
  - [1] 2026-11-03: third-party: the indexer is completely free with no usage limits | capture: sha256:3125b505eca26d74096a6985446593dbb6eb97637bbd1d4543eaa49be6387223 | quote: Completely free with no usage limits.
  - [1] 2026-11-03: third-party: files date back about 10 years | capture: sha256:3125b505eca26d74096a6985446593dbb6eb97637bbd1d4543eaa49be6387223 | quote: files available dating back approximately 10 years
  - [2] 2026-11-03: the home page lists a post dated 2021-08-14, so entries are indexed with post dates | capture: sha256:d6b5795aaf2f7215c3ab054a3b61507cacfd3d9d0020f4f45b3b45ff8ec367a5 | quote: Posted: 2021-08-14 12:45:55
  - [2] 2026-11-26: the captured page states that the domain may be for sale | capture: sha256:1e29e1157ae2349e7855e530a7742ca9a17a8597f2c45513c3c100939c5d130a | quote: This domain name may be for sale.
- sources:
  - [1] https://nzbhydra.com/indexers/
  - [2] https://nzbscout.com/
