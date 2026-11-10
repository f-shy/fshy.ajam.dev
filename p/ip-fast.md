# ip-fast.com

> ip-fast.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip-fast/ | JSON https://fshy.ajam.dev/api/v1/entity/ip-fast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ip-fast.com

- `data-apis/ip-fast-com` | dead | evidence measured | binding none | category IP address, country and city API | tier Free
- identity a placeholder: card and phone unknown | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://ip-fast.com/docs/
- free tier: none: ip-fast.com and its documentation URL serve a domain-parking page with advertising links, and the home page redirects to an advertising feed | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: unverified: the former offer; the public-apis listing described IP address, country and city with no key, and no archived copy could be read.
- per-object cap: not applicable: the API is gone | source: [1]
- retention: not applicable: the API is gone | source: [1]
- egress: not applicable: the API is gone | metered: no | source: [1]
- identity: anonymous | detail: unverified: the former offer; the public-apis listing described no key
- interface: rest
- binding note: the domain is parked, so no API limit exists.
- interface detail: unverified: the former request form; /api/ip/?format=json and /api/country/?ip={ip} no longer serve an API
- endpoint: https://ip-fast.com/
- tooling: none that works
- composes with: No working route: any free keyless IP geolocation API of this topic replaces it. Bulk path: none.
- reliability: ip-fast.com answers an HTTP 302 redirect to an advertising feed and /docs/ serves a parking page of search-ad links, on 2026-11-02
- notes: Free requests: none; the domain is parked. Rate limit: not applicable. Bulk path: none.
- evidence note: The home page redirect was probed and the documentation URL was read on 2026-11-02; the former offer could not be established because no archived copy is readable.
- extras:
  - bulk_path: none
  - free_requests: none
- evidence:
  - [1] 2026-11-02: the documentation URL serves a parking page of related searches | capture: sha256:5a66098a62683ca63e6f1e7a8024ccf75c78c7b060e6cb8ca9fb23d54dcbe444 | quote: Related Searches:
  - [1] 2026-11-02: the parking page links to an advertising click host | capture: sha256:5a66098a62683ca63e6f1e7a8024ccf75c78c7b060e6cb8ca9fb23d54dcbe444 | quote: - [internet speed test](http://ww547.ip-fast.com/kw-click)
  - probe:https://ip-fast.com/ 2026-11-02: the home page answers a redirect | capture: sha256:4f72b48811385671c005b32ee909b3c85c8b53bab69f684706dd133d01666a80 | quote: "from": "https://ip-fast.com/"
  - probe:https://ip-fast.com/ 2026-11-02: the home page redirect is an HTTP 302 to an advertising feed | capture: sha256:4f72b48811385671c005b32ee909b3c85c8b53bab69f684706dd133d01666a80 | quote: "status": 302,
- sources:
  - [1] https://ip-fast.com/docs/
