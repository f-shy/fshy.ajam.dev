# Internet Archive Wayback Machine

> Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/internet-archive-wayback-machine/ | JSON https://fshy.ajam.dev/api/v1/entity/internet-archive-wayback-machine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Internet Archive Wayback Machine

- `crawler-scraper/wayback` | qualifies | evidence measured | binding per-object-cap | category archive
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-22
- url https://web.archive.org/
- free tier: keyless listing, closest and replay of existing captures; Save Page Now needs keys | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a capture | source: [1]
- retention: captures are held indefinitely; a listing row's record_length is the compressed WARC size, not the body | source: [1]
- egress: Retrieval bandwidth is unmetered. Direct replay throughput for large binary objects is unmeasured. | metered: no | source: [1]
- identity: anonymous | detail: listing, closest and replay need nothing; Save Page Now needs Internet Archive API keys
- interface: rest
- limits:
  - request-rate: Save Page Now is held after 5 saves of one URL a day on this deployment; the listing and replay are keyless
  - per-object-cap (binding): A listing pages by a CDX resume key, where responses containing boundary captures specify a cursor for subsequent requests.
- interface detail: CDX server, Availability API and raw replay with an id_ suffix
- tooling: not established
- composes with: Rung four of the escalation ladder; the copy that survives the origin changing, as hostloc.com did
- reliability: No failure observed across five sample requests executed on 2026-10-22.
- notes: The single most useful service in this topic and the only one that answered within 4 s on every call. A short at= is the start of its period, so at=2024-06 asks 20240601000000.
- evidence:
  - [2] 2026-10-22: 200 in 3.2 s; capture 20240530023233, status 200, mimetype text/html, record_length 7402, compared[] names a distance of 163647 s
  - [3] 2026-10-22: 200, 26,000 bytes, x-web-origin-status 200, x-web-body archived: a 2024 copy of a forum that no longer serves its forums
  - [4] 2026-10-22: 3 captures then 3 more by next, no timestamp repeated, more true on both pages
- sources:
  - [1] https://web.archive.org/
  - [2] https://web.archive.org/web/202406/hostloc.com/forum.php
  - [3] https://web.archive.org/web/20240530023233/https://hostloc.com/forum.php?provider=wayback
  - [4] https://web.archive.org/web/*/example.com
