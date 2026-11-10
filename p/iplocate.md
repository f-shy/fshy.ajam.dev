# IPLocate

> iplocate.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iplocate/ | JSON https://fshy.ajam.dev/api/v1/entity/iplocate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPLocate

- `data-apis/iplocate` | qualifies | evidence documented | binding volume-quota | category IP geolocation API and database download | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.116Z (live) | stale on 2026-12-04
- url https://www.iplocate.io/pricing
- free tier: 1,000 requests a day free forever with an API key, no credit card, the same data as paid plans; free IP to Country and IP to ASN databases (CSV, MMDB) on GitHub, updated daily, no sign-up | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: a keyless request answered with x-ratelimit-limit 50
- per-object cap: the free ip-to-country.mmdb is 17,278,592 bytes; the batch API (1,000 IPs at once) needs paid credits | bytes: 17278592 | source: [2]
- retention: storage of API results is not stated | source: [2]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: email address and password, or GitHub or Google sign-in; no credit card; the databases need no sign-up
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a day with a free key [1]
  - volume-quota (binding): 50 requests a day per IP address without an API key; the day resets at 00:00:00 UTC [3]
  - request-rate: 100 requests per second from a single IP address, within the plan limits [3]
- interface detail: GET iplocate.io/api/lookup/{ip} with a key (keyless calls answered with a 50-request limit header); database files in the GitHub repository iplocate/ip-address-databases, served through Git LFS
- endpoint: https://iplocate.io/api/lookup/
- tooling: any HTTP client; any MMDB reader (GeoLite-compatible format)
- composes with: 1,000 keyed lookups a day with privacy, hosting, company and abuse data, plus daily country and ASN files for local lookups with no account. Bulk path: the free GitHub databases; the batch API needs paid credits
- reliability: a rate of up to 100 requests per second per IP address applies within the plan limits, and a request past a quota answers HTTP 429
- notes: Free requests: 1,000 a day with a key; a keyless call carried a 50-request limit. Rate limit: none stated within the quota. Bulk path: free daily IP to Country and IP to ASN files on GitHub.
- evidence note: the pricing page, the free-database docs, the GitHub repository and the signup page were quoted on 2026-10-30; a keyless lookup answered HTTP 200 with x-ratelimit-limit 50 and a ranged read of the MMDB on GitHub answered HTTP 206.
- extras:
  - bulk_path: free IP to Country and IP to ASN databases (CSV, MMDB) on GitHub, daily, no sign-up
  - free_requests: 1,000 a day with a key
- evidence:
  - [1] 2026-10-30: 1,000 requests a day free, no card | capture: sha256:ff139336e5abff66a6b9bc6b4712f5148f586654dd09c9959c068744befebb13 | quote: 1,000 requests per day, free forever. No credit card required. No other limits — the same data, same accuracy, same API.
  - [1] 2026-10-30: the free quota is 1,000 a day | capture: sha256:ff139336e5abff66a6b9bc6b4712f5148f586654dd09c9959c068744befebb13 | quote: | API request quota | 1,000/day Top-up with credits any time | From 100,000/month Up to millions of requests per month |
  - [1] 2026-10-30: the batch API takes 1,000 IPs | capture: sha256:ff139336e5abff66a6b9bc6b4712f5148f586654dd09c9959c068744befebb13 | quote: Batch API Enrich up to 1,000 IPs at once
  - [1] 2026-10-30: the batch API needs paid credits on the free tier | capture: sha256:ff139336e5abff66a6b9bc6b4712f5148f586654dd09c9959c068744befebb13 | quote: Available with paid credits
  - [4] 2026-10-30: the free country database is updated daily | capture: sha256:c862c514b96d8886ca1995667d509f4f23fe204edaa694e369785a91549a3873 | quote: It's updated daily and uses the same high-quality data that powers our production API, ensuring you get reliable results.
  - [4] 2026-10-30: the free database downloads with no sign-up | capture: sha256:c862c514b96d8886ca1995667d509f4f23fe204edaa694e369785a91549a3873 | quote: | Download with no sign-up | Sign-up required | Sign-up required | Sign-up required | ✅ Available on GitHub |
  - [2] 2026-10-30:  | capture: sha256:b89baf425cb81ad35db5c1e1abf83b76572ac2fbace4a2a4450445b1e8bcf2ae
  - [2] 2026-10-30: the databases come as CSV and MMDB | capture: sha256:b89baf425cb81ad35db5c1e1abf83b76572ac2fbace4a2a4450445b1e8bcf2ae | quote: The database is available in CSV and MMDB formats in the
  - [5] 2026-10-31: the signup page restates 1,000 a day | capture: sha256:404ce45a4ffdafbb63f7985c94dc1cf37b85d2c82c966739376d3e93b3b9c2f8 | quote: Get started with 1,000 free API requests per day.
  - [5] 2026-10-31: GitHub and Google sign-in are offered | capture: sha256:404ce45a4ffdafbb63f7985c94dc1cf37b85d2c82c966739376d3e93b3b9c2f8 | quote: Sign up with GitHubSign up with Google
  - [5] 2026-10-31: the signup form asks an email address | capture: sha256:404ce45a4ffdafbb63f7985c94dc1cf37b85d2c82c966739376d3e93b3b9c2f8 | quote: Email address
  - probe:https://github.com/iplocate/ip-address-databases/raw/main/ip-to-country/ip-to-country.mmdb 2026-10-31: the free MMDB is 17,278,592 bytes and downloads with no account | capture: sha256:e81086d3059e99e855793d1bc68184f73c246fb83d5c7c86deff09785d01d42d | quote: "content-range": "bytes 0-1023/17278592"
  - probe:https://iplocate.io/api/lookup/8.8.8.8 2026-10-31: a keyless call carried a limit of 50 | capture: sha256:bee673ede8f1d64c181e8df53f9c46f99215cabdcf1eab431e8910d656845336 | quote: "x-ratelimit-limit": "50"
  - probe:https://iplocate.io/api/lookup/8.8.8.8 2026-10-30: a keyless call answered with privacy fields | capture: sha256:82bec9db539bd6b0ae53e2c728f37d80f97ac42e993a716b6e20d4f609d5e248 | quote: "is_vpn":false
  - [3] 2026-11-02: the quota with no API key is 50 requests per day by IP address, and the daily quota resets at 00:00:00 UTC each day | capture: sha256:e4be64a9877dac975282c7e89b151a659bfcf0f69b389e29de2241df7186d102 | quote: | With no API key | 50 requests per day by IP address |
  - [3] 2026-11-02: a single IP address may send up to 100 requests per second within the plan limits | capture: sha256:e4be64a9877dac975282c7e89b151a659bfcf0f69b389e29de2241df7186d102 | quote: You can make up to 100 requests per second from a single IP address (within your plan limits).
  - [3] 2026-11-02: a single IP address may send up to 100 requests per second within the plan limits, and a request past a quota gets a 429 error | capture: sha256:e4be64a9877dac975282c7e89b151a659bfcf0f69b389e29de2241df7186d102 | quote: You can make up to 100 requests per second from a single IP address (within your plan limits).
  - [6] 2026-11-02: a keyless lookup sent x-ratelimit-limit 50 and x-ratelimit-reset 1793664000, which is 2026-11-03T00:00:00Z, the next UTC midnight | capture: sha256:08a019beeb253d042ac03d3732ae3add7519ae8bb48ff63e9c29be256148a5fa | quote: x-ratelimit-reset: 1793664000
  - [1] 2026-11-02: the free plan is 1,000 requests per day with no credit card | capture: sha256:b2c26e1c5dea34e105838810e6e08a6446ed459e1e080eaa0763a51a6caf7ea8 | quote: 1,000 requests per day, free forever. No credit card required.
- sources:
  - [1] https://www.iplocate.io/pricing
  - [2] https://github.com/iplocate/ip-address-databases/
  - [3] https://www.iplocate.io/docs/getting-started/quota-rate-limits
  - [4] https://www.iplocate.io/docs/data-feeds/free-ip-to-country-database
  - [5] https://www.iplocate.io/signup
  - [6] https://iplocate.io/api/lookup/8.8.8.8
