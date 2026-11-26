# SearchFiles

> searchfiles.de | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/searchfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/searchfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SearchFiles

- `debrid/searchfiles-de` | qualifies | evidence documented | binding none | category file search engine (multi-host index) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:41.783Z (live) | stale on 2026-12-26
- url https://searchfiles.de/
- price USD 0
- free tier: Free search across file hosts: 'SearchFiles file search engine is a search tool which can search for information in files', with named engines for Mediafire, Keep2share/K2s, MediaFire and Mega.nz. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: No query cap is published on the page read.
- per-object cap: not applicable: an index of links, not a store of bytes | source: [1]
- retention: not applicable: the index lists links that live on the hosts | source: [1]
- egress: Downloads are served by the host behind each result, so the host's limits apply. SearchFiles itself transfers nothing. | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: No account or login on the search form.
- interface: browser
- limits:
  - request-rate: unstated [1]
- limits note: No rate limit, result cap or query budget is printed on the page read.
- binding note: SearchFiles stores and transfers nothing, so no byte constraint can bind. The first real limit is on the host a result points to.
- interface detail: Web search form with per-host engines. No API is published on the page read.
- tooling: Browser only as read; a wrapper would have to scrape the result page.
- composes with: The step before a debrid: find the link, then unrestrict it. Its value is the per-host engines (K2s, MediaFire, Mega) rather than a general web search, because each one indexes inside that host's file metadata.
- reliability: An index of other people's links inherits their rot: a result can point at a deleted file, and the index does not re-check on the way out.
- notes: File search engine indexing links across multiple file hosts. Does not provide debrid link unlocking. No programmatic path found: Web search form with per-host engines. No API is published on the page read.
- evidence note: The per-host engines and the free claim are read from the vendor page. No query was run, so the index's real coverage is unmeasured.
- extras:
  - engines_named: Mediafire, Keep2share/K2s, MediaFire, Mega.nz
- evidence:
  - [1] 2026-10-23: the per-host engines it advertises (Mediafire, Keep2share/K2s, MediaFire, Mega.nz) and the file-content search claim
  - [1] 2026-11-25: the site is still a file search tool rather than a file host | capture: sha256:7998a1a09af66bc7d1a4a6a176f0577a31367358d867360aa68af00f56ad1488 | quote: SearchFiles file search engine is a search tool which can search for information in files.
  - [1] 2026-11-25: the per-host Mega.nz engine is still advertised | capture: sha256:7998a1a09af66bc7d1a4a6a176f0577a31367358d867360aa68af00f56ad1488 | quote: Mega.nz is a file hoster for music, movies, software and documents.
- sources:
  - [1] https://searchfiles.de/
