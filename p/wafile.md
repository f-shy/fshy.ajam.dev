# Wafile

> wafile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wafile/ | JSON https://fshy.ajam.dev/api/v1/entity/wafile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wafile

- `debrid/wafile` | qualifies | evidence documented | binding none | category file search engine (Mega.nz index) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://wafile.com/
- price USD 0
- free tier: 'Search Mega.nz with speed, clarity, and confidence.' Free index of Mega links with size, type and context shown before opening. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: No query cap is published on the page read.
- per-object cap: not applicable: an index of links | source: [1]
- retention: not applicable: results point at Mega.nz files under Mega's own retention | source: [1]
- egress: Nothing is transferred by Wafile; a result downloads from Mega, which applies its own free-tier transfer quota. | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: No account or login on the search form.
- interface: unknown
- limits:
  - request-rate: unstated; '24/7 Index refresh' and '4h Status recheck' are the only cadence figures [1]
- binding note: An index transfers nothing, so no byte constraint binds. The first real limit is Mega's own transfer quota on the download.
- interface detail: Web search form. No API is published on the page read.
- tooling: Browser only as read.
- composes with: A Mega-only index, so it pairs with Mega-download tooling (megatools, MEGAcmd) rather than with a debrid: debrids generally refuse Mega links or resolve them slowly. The site claims a 24-hour index refresh and a 4-hour status recheck.
- reliability: The 4-hour status recheck means a dead Mega link can still be listed as alive for most of a day.
- notes: SearchFiles is the general index; this is the single-host one.
- evidence note: The Mega focus and the refresh cadence are read from the vendor page. No query was run, so coverage is unmeasured.
- extras:
  - host_indexed: mega.nz
  - refresh: index 24/7, status 4h
- evidence:
  - [1] 2026-10-23: 'Search Mega.nz with speed, clarity, and confidence', '24/7 Index refresh', '4h Status recheck', and the promise to show 'file size, type, and context before opening'
- sources:
  - [1] https://wafile.com/
