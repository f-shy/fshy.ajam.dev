# OpenAIRE Graph API

> openaire.eu | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openaire/ | JSON https://fshy.ajam.dev/api/v1/entity/openaire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenAIRE Graph API

- `debrid/openaire` | qualifies | evidence measured | binding request-rate | category scholarly graph aggregator (publications, datasets, software, projects) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://graph.openaire.eu/docs/
- price USD 0
- free tier: Public REST APIs over 'one of the largest open scholarly record collections worldwide', with no registration described on the documentation landing page. The Graph itself is 'openly available and can be used by third-parties to create added value services'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No key and no numeric rate limit appear on the docs landing page.
- per-object cap: not applicable: XML or JSON per query. size=100 returned 8,384,696 bytes in one response here, so a page is megabytes rather than kilobytes. | source: [2]
- retention: the graph is rebuilt from source repositories and deduplicated; records reflect the last harvest, not a fixed snapshot | source: [1]
- egress: Free and unmetered for the public API endpoints. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No key, no account: both calls answered 200 anonymously. Nothing on the docs page asks for registration.
- interface: rest, cli
- limits:
  - request-rate (binding): none published on the docs landing page; two calls here (size=1 and size=100) both returned 200 with no throttling header [3]
- binding note: At 8.38 MB per call and 4.2 s per call, one connection moves about 2 MB/s; with no published cap the unknown is how many calls the service tolerates before a 429, which is what decides the day.
- interface detail: GET https://api.openaire.eu/search/publications?title=...&size=N (XML by default, format=json available); the newer Graph API sits under https://api.openaire.eu/graph/.
- endpoint: part of interface detail
- tooling: curl/python-requests; the openaire python client exists but the endpoints are plain HTTP.
- composes with: The widest single metadata source among debrid providers per call: 8.4 MB per size=100 page means a few thousand calls moves tens of GB of linked records, which is a different order from Crossref's 0.77 MB pages.
- reliability: Responses are large XML by default, so a client that forgets format=json spends bandwidth on tags; the search endpoint and the newer graph endpoint are different APIs with different shapes.
- notes: The highest bytes-per-call of any metadata API among debrid providers by an order of magnitude, which makes it the best candidate for filling a day with metadata when the file hosts are the bottleneck.
- evidence note: Two calls were made and their byte counts recorded, one of them 8.4 MB. The absence of a rate limit is an absence of evidence: no sustained run was attempted.
- extras:
  - size_1_bytes: 24711
  - size_100_bytes: 8384696
  - size_100_ms: 4166.8
- evidence:
  - [1] 2026-10-23: 'one of the largest open scholarly record collections worldwide' and that the graph data are 'openly available' through public APIs
  - probe:https://api.openaire.eu/search/publications?title=cancer&size=1 2026-10-23: 200, 24,711 bytes of application/xml, anonymous
  - probe:https://api.openaire.eu/search/publications?title=cancer&size=100 2026-10-23: 200, 8,384,696 bytes in 4,166.8 ms - one anonymous call returns 8.4 MB
- sources:
  - [1] https://graph.openaire.eu/docs/
  - [2] https://api.openaire.eu/search/publications
  - [3] https://api.openaire.eu/search/publications?title=cancer&size=100
