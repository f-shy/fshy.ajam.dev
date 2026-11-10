# IP Vigilante

> ipvigilante.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipvigilante/ | JSON https://fshy.ajam.dev/api/v1/entity/ipvigilante.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP Vigilante

- `data-apis/ip-vigilante` | dead | evidence measured | binding none | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://www.ipvigilante.com/
- free tier: none: ipvigilante.com now redirects (HTTP 301 three times) via two other domains to an unrelated site; an archived copy of 2022-11-30 described a free geographical IP locator API answering JSON and CSV | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the archived copy states no quota, rate limit or key.
- per-object cap: not applicable: the API is gone | source: [1]
- retention: not applicable: the API is gone | source: [1]
- egress: not applicable: the API is gone | metered: no | source: [1]
- identity: anonymous | detail: the former API was a plain GET of /{ip} with no key in the archived example
- interface: rest
- binding note: the host no longer serves the API.
- interface detail: former form GET https://ipvigilante.com/{ip} answering JSON (archived 2022-11-30); the host now answers HTTP 301 redirects to other domains
- endpoint: part of interface detail
- tooling: none that works
- composes with: No working route: any free or paid IP geolocation API of this topic replaces it. Bulk path: none.
- reliability: https://www.ipvigilante.com/json/8.8.8.8 and the root both redirect (HTTP 301 three times) through groundingspace.net and asopran.org to an unrelated site, on 2026-11-02
- notes: Free requests: none; the former free API is gone. Rate limit: not applicable. Bulk path: none.
- evidence note: The redirect chain of the host was probed on 2026-11-02 and the last archived copy (2022-11-30) was read; the former quota was never stated on a page that could be read.
- extras:
  - bulk_path: none
  - free_requests: none
- evidence:
  - [1] 2026-11-02: the archived page describes a free geographical IP locator API with JSON and CSV answers | capture: sha256:58f045b31f02d4c53f97c7fd2bd08dc6cde32ffb1d6755f784ef9c849f156b2d | quote: IP Vigilante provides a free geographical IP locator API, so the developers can obtain geographical information of an IP in various formats: JSON and CSV.
  - [1] 2026-11-02: the archived example is a plain GET of /{ip} with no key | capture: sha256:58f045b31f02d4c53f97c7fd2bd08dc6cde32ffb1d6755f784ef9c849f156b2d | quote: https://ipvigilante.com/8.8.8.8
  - probe:https://www.ipvigilante.com/json/8.8.8.8 2026-11-02: the former API path redirects to another domain | capture: sha256:fa858a13b647899868dbf5c0d28f0923fc1f3e3cd2211a804cc0c7c9e643d188 | quote: "location": "https://groundingspace.net/",
  - probe:https://www.ipvigilante.com/json/8.8.8.8 2026-11-02: the redirect chain ends on an unrelated domain | capture: sha256:fa858a13b647899868dbf5c0d28f0923fc1f3e3cd2211a804cc0c7c9e643d188 | quote: "final_url": "https://lugnutscarreviews.com/",
- sources:
  - [1] https://web.archive.org/web/20221130105431/https://www.ipvigilante.com/
