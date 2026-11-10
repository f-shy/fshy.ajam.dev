# ipfind.io

> ipfind.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipfind/ | JSON https://fshy.ajam.dev/api/v1/entity/ipfind.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipfind.io

- `data-apis/ipfind-io` | dead | evidence measured | binding none | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://ipfind.io/ip-location-api-pricing
- free tier: none that can be reached: the pricing page lists a Free plan of 15000 API calls priced $0.0 a month with a free API key, but the API host app.ipfind.io named in the documentation has no DNS record (NXDOMAIN at two public resolvers) and the sign-in and sign-up links of archived pages lead to ipgeolocation.io | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the listed plans are Free (15000 API calls), PRO at $49.90 a month (1M API calls) and Enterprise (unlimited); the period of the free calls is not stated beyond the plan being priced per month.
- per-object cap: one IP address or domain name per request (the ip parameter) | source: [2]
- retention: not applicable: the API host does not resolve | source: [2]
- egress: not applicable: the API host does not resolve | metered: no | source: [2]
- identity: email | detail: the archived sign-up form asked for a name, email, country and password and said no credit card was required; its links lead to ipgeolocation.io
- interface: rest
- limits:
  - volume-quota: 15000 API calls on the Free plan, as listed; the API host does not resolve [1]
- binding note: the documented API host does not resolve, so no quota can be reached.
- interface detail: documented form GET https://app.ipfind.io/api/iplocation?apikey={key}&ip={ip}; the host app.ipfind.io has no DNS record
- endpoint: part of interface detail
- tooling: none that works
- composes with: No working route as documented. The archived sign-in and sign-up links lead to ipgeolocation.io, which has its own record. Bulk path: none.
- reliability: app.ipfind.io, api.ipfind.io, dashboard.ipfind.io and my.ipfind.io have no DNS record while ipfind.io and www.ipfind.io resolve; the site answers a Cloudflare managed challenge (HTTP 403) to a plain HTTP client
- notes: Free requests: none that can be reached; the listed 15000 API calls cannot be used because the documented API host does not resolve. Rate limit: not applicable. Bulk path: none.
- evidence note: The API host was resolved through two public DNS-over-HTTPS resolvers on 2026-11-02 and both answered NXDOMAIN; the pricing and documentation pages were read from stored copies and the sign-up pages from archived copies of 2024 and 2025.
- extras:
  - bulk_path: none
  - free_requests: none reachable
- evidence:
  - [1] 2026-11-02: the Free plan lists 15000 API calls | capture: sha256:3d21eaa94bca27285e99dc9d335b37ae2d9b753f545610c7d63f937ff823e7d6 | quote: 15000API calls
  - [1] 2026-11-02: the Free plan is priced $0.0 a month | capture: sha256:3d21eaa94bca27285e99dc9d335b37ae2d9b753f545610c7d63f937ff823e7d6 | quote: $0.0/Month
  - [3] 2026-11-02: the archived pricing page lists the same 15000 API calls | capture: sha256:c2290c821adead2b6cb8fed4789e6dc33d87f79230ad0e2765934698b6a3b261 | quote: - 15000 API calls
  - [3] 2026-11-02: the Get Started button of the Free plan leads to ipgeolocation.io | capture: sha256:c2290c821adead2b6cb8fed4789e6dc33d87f79230ad0e2765934698b6a3b261 | quote: [Get Started](https://ipgeolocation.io/signup.html)
  - [4] 2026-11-02: the archived sign-up page says no credit card is required | capture: sha256:71efd945085196282521f4d49feddf72fcb5386fd93bb6cf66bd52cc24dc5c19 | quote: Simple registration method just signup and get your dashboard & access APIKEY. No credit card required.
  - [4] 2026-11-02: the archived sign-up form asked for a name, email, country and password | capture: sha256:71efd945085196282521f4d49feddf72fcb5386fd93bb6cf66bd52cc24dc5c19 | quote: Your Name Email Country Name Password
  - [4] 2026-11-02: the archived sign-up link leads to ipgeolocation.io | capture: sha256:71efd945085196282521f4d49feddf72fcb5386fd93bb6cf66bd52cc24dc5c19 | quote: - [Sign Up](https://ipgeolocation.io/signup.html)
  - [5] 2026-11-02: a free API key comes with sign-up and no credit card | capture: sha256:ab2c45c08dc3ced98302c846aafe51dd54d4a8e5d0ee293f3782c8619a7c2e7b | quote: To get our free IP location API just simply Signup, no credit card required & get your free dashboard with free API Key access.
  - [2] 2026-11-02: the documented endpoint host is app.ipfind.io | capture: sha256:00acda556bb85d6898d5ce36e83b6499be14052120a9295dfc537175cae43bb7 | quote: https://app.ipfind.io/api/iplocation?apikey=YOUR\_APIKEY
  - probe:https://ipfind.io/ 2026-11-02: a plain GET of the home page answered HTTP 403 | capture: sha256:b46d5c17e04401b866f700265d4e706a1f6c861c8fe75db27d9fd46e56c29e33 | quote: "status": 403
  - probe:https://ipfind.io/ 2026-11-02: the 403 is a Cloudflare managed challenge | capture: sha256:b46d5c17e04401b866f700265d4e706a1f6c861c8fe75db27d9fd46e56c29e33 | quote: "signature": "cloudflare-challenge:title:just a moment..."
  - probe:https://cloudflare-dns.com/dns-query?name=app.ipfind.io&type=A 2026-11-02: the public DNS-over-HTTPS query for app.ipfind.io was answered | capture: sha256:82db8d631cbcb5e048309ba8c04b44e01c1bcf29d691a95138bfa3e422ecf61d | quote: "status": 200
  - probe:https://cloudflare-dns.com/dns-query?name=app.ipfind.io&type=A 2026-11-02: Cloudflare's resolver answered NXDOMAIN for app.ipfind.io | capture: sha256:de9fc61a5b64022fd0fbae84300cda532409d6482af333f58cf73835d5db9633 | quote: "Status":3
  - probe:https://dns.google/resolve?name=app.ipfind.io&type=A 2026-11-02: a second public resolver query for app.ipfind.io was answered | capture: sha256:c304563cc083a67899ff427860cb112d278cd0bfe2f647fc90d578b1dafd8450 | quote: "status": 200
  - probe:https://dns.google/resolve?name=app.ipfind.io&type=A 2026-11-02: Google's resolver answered NXDOMAIN for app.ipfind.io | capture: sha256:0fb79147eea88ee043b090764311b60a03075ec05da7fb55ccf2ad5ceeef9aa7 | quote: "Status":3
- sources:
  - [1] https://ipfind.io/ip-location-api-pricing
  - [2] https://ipfind.io/documentation
  - [3] https://web.archive.org/web/20250918022524/https://ipfind.io/ip-location-api-pricing
  - [4] https://web.archive.org/web/20250514202754/https://ipfind.io/signup
  - [5] https://web.archive.org/web/20240716040735/https://ipfind.io/iplocator
