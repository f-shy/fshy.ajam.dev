# FilePursuit

> filepursuit.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filepursuit/ | JSON https://fshy.ajam.dev/api/v1/entity/filepursuit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FilePursuit

- `debrid/filepursuit` | dead | evidence unverified | binding request-rate | category file-host search engine (index over public file links) + metered JSON API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:12.551Z (live) | stale on 2026-11-19
- url https://filepursuit.com/
- price USD 0
- free tier: The site was not readable today. The API is documented on RapidAPI as a Basic plan at $0.00/month with 3,000 requests per day and 500 requests per hour. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The website returned HTTP 530; API numbers reflect the vendor's published marketplace tier.
- per-object cap: not applicable: a search result, not a stored object. | source: [2]
- retention: unknown: the index's own retention was not readable, and the API terms say nothing about how long a link stays in the index | source: [2]
- egress: the API returns links, not bytes; bytes come from whichever host the link names | metered: yes | free allowance: 3,000 requests/day on the free RapidAPI plan | source: [1]
- identity: email | detail: The API needs a RapidAPI account and key, which is an email signup; the amount of identity RapidAPI demands beyond that was not established because the signup flow was not entered.
- interface: rest
- limits:
  - request-rate (binding): 500 requests per hour on the free RapidAPI plan, with a hard cap of 3,000 requests per day [1]
- limits note: The free plan also meters bandwidth at 10,240 MB/month plus $0.001 per 1 MB over. A third-party scraper reports that flooding the site triggers a captcha, which is the HTML path's limit rather than the API's.
- binding note: 500/hour is 0.14 req/s, so enumeration stops long before any byte quota does; and the API additionally requires an account, which is recorded under identity_cost.
- interface detail: RapidAPI JSON endpoint with an X-RapidAPI-Key header; the site itself is HTML. The API is also offered through third-party clients (filepursuit-cli, go-filepursuit, a PyPI scraper).
- endpoint: rapidapi.com/azharxes/api/filepursuit
- tooling: The PyPI 'filepursuit' scraper and a Go client exist. Both drive the site rather than the paid API, and the scraper's own documentation says the site answers a flood of requests with a captcha.
- composes with: Query the index for a filename, then hand the file-host URL to a debrid service. The value is discovery: the index is what tells you which public link exists.
- reliability: On 2026-11-03 the .com registry lists filepursuit.com with status client hold and the domain has no DNS answer (NXDOMAIN); the site answered an origin failure on 2026-10-23. Whether a datacenter address is accepted: not published.
- notes: The index domain no longer resolves, so the service is recorded dead. The RapidAPI listing remains, showing a 0% service level, and its machine interface needs a RapidAPI key.
- evidence note: The domain's DNS answer (NXDOMAIN) and registry status (client hold) were read on 2026-11-03 and the RapidAPI listing shows a 0% service level; the API plan figures come from the RapidAPI pricing page and nothing was executed against the API.
- extras:
  - http_status_observed: 530
  - attempts: 4
  - api_marketplace: RapidAPI
  - anonymous_api: no
  - death.on: 2026-11-03
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: Basic $0.00/mo, 'Requests 3,000 / Day Hard Limit', 'Rate Limit 500 requests per hour', 10240 MB/month bandwidth
  - [2] 2026-10-23: nothing was established about the live site
  - [3] 2026-10-23: a third-party scraper's README says FilePursuit answers flooding with a captcha
  - probe:https://dns.google/resolve?name=filepursuit.com&type=A 2026-11-03: the public resolver answers NXDOMAIN (status 3) for filepursuit.com | capture: sha256:1f30409690b9ee0a9b7e3d70344ac0fd14d00e2902c9cd79d492d115077fed04 | quote: "Status":3
  - probe:https://rdap.verisign.com/com/v1/domain/filepursuit.com 2026-11-03: the registry shows the domain on client hold, which removes it from DNS | capture: sha256:1083a20c561f0b7b5b054f6cdd4f2d4e5b5834c985d59c1988bd68092bbfb28f
  - [4] 2026-11-03: the marketplace listing for the API shows 0% service level | capture: sha256:e613edf56bb83b9cc0a6cbe81a4f5533e3e3af2e973e8fe63f7483e8095b4b83 | quote: 0% Service Level
  - [1] 2026-11-04: the free plan rate limit is 500 requests per hour | capture: sha256:3253f5e94a075f4e3f07c4f361500dc3388e2379e0c69ffc3ddf4e2e9242575f | quote: Rate Limit 500 requests per hour
  - probe:filepursuit.com 2026-11-04: the site does not resolve in DNS | capture: sha256:f7f461ec5aadb18fb1643c3a9e5a2008801d63c40a5108bf3cde394f7b71f270 | quote: "error": "dns"
  - probe:https://dns.google/resolve?name=filepursuit.com&type=A 2026-11-04: the public resolver answers NXDOMAIN for filepursuit.com | capture: sha256:71bc9d726284fe22542819f6d440cb71dffc664879fe20b93d4c03f7a3a82308 | quote: "Status":3
- sources:
  - [1] https://rapidapi.com/azharxes/api/filepursuit/pricing
  - [2] https://filepursuit.com/
  - [3] https://pypi.org/project/filepursuit/
  - [4] https://rapidapi.com/azharxes/api/filepursuit
