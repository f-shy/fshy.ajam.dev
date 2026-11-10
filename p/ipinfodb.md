# IPInfoDB

> ipinfodb.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipinfodb/ | JSON https://fshy.ajam.dev/api/v1/entity/ipinfodb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPInfoDB

- `data-apis/ipinfodb` | dead | evidence documented | binding none | category IP geolocation API | tier Free key
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://www.ipinfodb.com/api
- free tier: none for a new user: the register page says no new sign-ups are accepted for the API and points to a free IP2Location.io API; a key issued earlier was limited to 2 queries a second | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the page says a faster key from IP2Location.io offers 30K IP geolocation queries a month; that offer has its own record.
- per-object cap: one IP address per request (the ip parameter, default the caller) | source: [2]
- retention: not stated; the page suggests keeping the geolocation in a cookie instead of querying on every page view | source: [2]
- egress: not applicable: raw, XML or JSON answers, not metered in bytes | metered: no | source: [2]
- identity: email | detail: the former sign-up gave a free key; the register page now says no new sign-ups are accepted
- interface: rest
- limits:
  - request-rate: 2 queries per second; a faster IP is temporarily blocked and then permanently banned [2]
- binding note: no new key can be created, so no limit can be reached by a new user.
- interface detail: GET https://api.ipinfodb.com/v3/ip-country/ and /v3/ip-city/ with the key, ip and format parameters (raw, xml or json)
- endpoint: https://api.ipinfodb.com/v3/ip-city/
- tooling: any HTTP client; PHP, Ruby, Python, C#, VB.NET and Java examples are on the page
- composes with: No new key can be created; the register page names the IP2Location.io free API as the replacement. Bulk path: none.
- reliability: past 2 queries a second an IP address is temporarily blocked by a firewall and then permanently banned; the origin answers HTTP 403 to a plain client and the pages were read from stored copies
- notes: Free requests: none for new users; sign-ups are closed. Rate limit: 2 queries a second, blocked then banned past it. Bulk path: none. The replacement named on the register page is IP2Location.io, which has its own record.
- evidence note: The API page and the register page were quoted on 2026-11-02 from stored copies, because the origin answers HTTP 403 to direct reads; whether keys issued earlier still answer was not tested.
- extras:
  - bulk_path: none
  - free_requests: none for new users
- evidence:
  - [1] 2026-11-02: new sign-ups for the API are closed | capture: sha256:21a0d9eb95438d1ed0d23b055af884eb146bc92caa59aa43e973cacac64be0d7 | quote: We are no longer accepting new sign ups for the IPInfoDB API.
  - [1] 2026-11-02: the page points to a free IP2Location.io API | capture: sha256:21a0d9eb95438d1ed0d23b055af884eb146bc92caa59aa43e973cacac64be0d7 | quote: Instead, please sign up for a free IP2Location.io IP Geolocation API, which offers a faster API with more geolocation data points.
  - [2] 2026-11-02: the API page answers HTTP 403 to a plain client | capture: sha256:39d1caae31592fd311c79e5885cc9f239d885eba7ca24017c1eccac175a1f12c
  - [2] 2026-11-02: the 403 is a Cloudflare managed challenge | capture: sha256:39d1caae31592fd311c79e5885cc9f239d885eba7ca24017c1eccac175a1f12c | quote: cf-mitigated: challenge
  - [2] 2026-11-02: the free service is limited to 2 queries a second | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: To remain the stabilities of free service, a rate limit of 2 queries per second applied to our API servers.
  - [2] 2026-11-02: a faster IP is temporarily blocked | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: Any IP querying the API faster than this rate will be temporarily blocked by our firewall.
  - [2] 2026-11-02: a request takes one IP address, defaulting to the caller | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: | ip | No | Client IP | IPv4 or IPv6 address. |
  - [2] 2026-11-02: a key from a free account is required | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: | key | Yes | API key provided with your free account. |
  - [2] 2026-11-02: the city-precision request form | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: https://api.ipinfodb.com/v3/ip-city/?key=YOUR_API_KEY&ip=IPV4_OR_IPV6_ADDRESS&format=json
  - [2] 2026-11-02: the page suggests storing the geolocation in a cookie | capture: sha256:4f5bd071ac9cb30b94e8c43445a1bfbb69bb80576f1dd0cbe00f7bed907dad25 | quote: - If you track your visitors, avoid querying our API for all your page views (you can store the geolocation in a cookie, see below for an example).
- sources:
  - [1] https://www.ipinfodb.com/register
  - [2] https://www.ipinfodb.com/api
