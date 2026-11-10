# ipapi.is

> ipapi.is | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipapi-3/ | JSON https://fshy.ajam.dev/api/v1/entity/ipapi-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipapi.is

- `data-apis/ipapi-is` | qualifies | evidence documented | binding volume-quota | category IP geolocation API and database download | tier Free account
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.115Z (live) | stale on 2026-12-04
- url https://ipapi.is/free-tier.html
- free tier: 1,000 requests a day with a free account and key, full response, no payment details, not a trial; 30 lookups a day per client IP without a key (ownership and location fields only); a free geolocation database in CSV for IPv4 and IPv6 | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: one-time credits beyond the free tier cost USD 1 per 30,000 requests and never expire
- per-object cap: the free IPv4 geolocation database zip is 65,954,248 bytes | bytes: 65954248 | source: [2]
- retention: storage of API results is not stated | source: [2]
- egress: not applicable | metered: no | source: [3]
- identity: email | detail: a free account: the sign-up form requires an email address, a password and a country, and has an optional how-did-you-hear field and no payment field; GitHub or Google sign-in is offered
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a day with a free key; 30 a day per client IP without a key [3]
- limits note: keyless requests past the 30th lookup of a UTC day get HTTP 429 ERR_FREE_TIER_EXHAUSTED for the next 10 requests, with a Retry-After header holding the seconds until UTC midnight; the response headers of a keyed answer are unverified: behind a sign-up
- interface detail: GET api.ipapi.is/?q=IP&key=KEY, or POST a JSON body with q and key; without a key the answer carries 11 keys and a docs link, and bulk and ASN queries answer 403 ERR_FORBIDDEN_API_KEY_REQUIRED; free files at ipapi.is/data/geolocationDatabaseIPv4.csv.zip and geolocationDatabaseIPv6.csv.zip with no account
- endpoint: https://api.ipapi.is/
- tooling: any HTTP client; any CSV tool for the database
- composes with: 1,000 keyed lookups a day with VPN, proxy, datacenter and abuse fields, plus a free WHOIS-sourced geolocation file for local lookups; one-time credits at USD 1 per 30,000 requests extend it without a subscription. Bulk path: the free CSV database download; bulk API queries need a key
- reliability: keyless callers get HTTP 429 after 30 lookups a day and a 24-hour firewall block if they keep sending; the free database has fewer entries and reduced accuracy
- notes: Free requests: 1,000 a day with a free key; 30 a day per IP without. Rate limit: HTTP 429 past the daily budget, 24-hour block on persistent overrun. Bulk path: free IPv4 and IPv6 geolocation CSV downloads, no account.
- evidence note: the free-tier, pricing, geolocation-database and signup pages were quoted on 2026-10-30; a keyless lookup answered HTTP 200 with the short response and a ranged read of the free IPv4 zip answered HTTP 206 with no account.
- extras:
  - bulk_path: free IPv4 and IPv6 geolocation database CSV zips, no account
  - free_requests: 1,000 a day with a key; 30 a day keyless
- evidence:
  - [3] 2026-10-30: keyless use is 30 lookups per IP per UTC day | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: Anonymous use is capped at 30 lookups per client IP per UTC day.
  - [3] 2026-10-30: ignoring the 429 notices brings a 24-hour block | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: A client that ignores those notices and keeps sending is blocked at the firewall for 24 hours
  - [3] 2026-10-30: a free account gives 1,000 lookups a day | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: A free account raises you to 1,000 lookups a day and returns the complete response.
  - [3] 2026-10-30: the free account needs no payment details | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: It takes a minute and needs no payment details
  - [3] 2026-10-30: the free tier is not a trial | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: The account tier is free, and it is not a trial: if 1,000 a day is enough, you never pay.
  - [3] 2026-10-30: bulk and ASN queries need a key | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: which the anonymous tier refuses outright with `403 ERR_FORBIDDEN_API_KEY_REQUIRED`
  - [1] 2026-10-30: the pricing page states 1,000 a day free | capture: sha256:aa6cdcedd4ba6899997cd3a043d237e207a8cb59f122fef3bce317ce32edf80f | quote: With a free account and API key, 1,000 requests per day, every day, with the full response.
  - [1] 2026-10-30: one-time credits are 30,000 requests per USD 1 | capture: sha256:aa6cdcedd4ba6899997cd3a043d237e207a8cb59f122fef3bce317ce32edf80f | quote: pay once, 30,000 requests per dollar, any amount from $1
  - [2] 2026-10-30: a free geolocation database is downloadable as CSV | capture: sha256:29d28580225107c7064273a279e4bd60e3a3ed24bff940d819e0dade7b0195d3 | quote: The free version is available for download in CSV format.
  - [2] 2026-10-30:  | capture: sha256:29d28580225107c7064273a279e4bd60e3a3ed24bff940d819e0dade7b0195d3 | quote: You may use it for any purpose, including commercial ones, as long as you credit ipapi.is with a link wherever you show data from it
  - [2] 2026-10-30: the free database is partial | capture: sha256:29d28580225107c7064273a279e4bd60e3a3ed24bff940d819e0dade7b0195d3 | quote: The free database has fewer entries and does not cover the full IPv4 and IPv6 address space
  - [2] 2026-10-30: a free IPv4 geolocation database is offered as CSV | capture: sha256:29d28580225107c7064273a279e4bd60e3a3ed24bff940d819e0dade7b0195d3 | quote: The free geolocation database for IPv4 addresses in CSV format
  - [4] 2026-10-30: the signup form asks an email | capture: sha256:a8335e29c9e9cd5f9a357697c8785c7c0091196aef023c2e9ce7d6c3b2b45485 | quote: type="email" name="email" placeholder="you@example.com"
  - [4] 2026-10-30: the signup form asks how the user heard of the service | capture: sha256:a8335e29c9e9cd5f9a357697c8785c7c0091196aef023c2e9ce7d6c3b2b45485 | quote: name="heardAbout" maxlength="160" placeholder="In a few words"
  - [4] 2026-10-30: GitHub sign-in is offered | capture: sha256:a8335e29c9e9cd5f9a357697c8785c7c0091196aef023c2e9ce7d6c3b2b45485 | quote: Continue with GitHub
  - probe:https://api.ipapi.is/?q=8.8.8.8 2026-10-30: a keyless lookup answered with the short anonymous response | capture: sha256:ae7b174106a070ab6b1c6daf553ce75826b99334fcf4742f4b241a060a58e011 | quote: "docs":"https://ipapi.is/free-tier.html?ref=api"
  - probe:https://ipapi.is/data/geolocationDatabaseIPv4.csv.zip 2026-10-31: the free IPv4 zip is 65,954,248 bytes and downloads with no account | capture: sha256:9eb16f8d09255672d0f00848e132a0a093f29ed9cc580108942150e1e0cc5838 | quote: "content-range": "bytes 0-1023/65954248"
  - [4] 2026-11-02: the sign-up form requires email address, password and country, has an optional how-did-you-hear field and no payment field, and offers GitHub and Google sign-in | capture: sha256:3dabd7c005f4beca491b7ce0d81c9d1d835b9563bbc4d3cb7a5321a29b611e2a | quote: name="country" required id="country-list"
  - [5] 2026-11-02: a keyless 429 carries a Retry-After header with the seconds until UTC midnight; the documentation names no header for a keyed answer | capture: sha256:238929769adc853764ed05dffc6e7ba181afc1db4fdb5a47d550f3fb36a7f8ae | quote: After the 30th lookup, the next 10 requests are answered with `429 ERR_FREE_TIER_EXHAUSTED` and a `Retry-After` header holding the seconds until UTC midnight.
  - [6] 2026-11-02: a keyless lookup answered HTTP 200 with the short anonymous response of eleven keys and a docs link | capture: sha256:7a1e88e04bd02a1daa56ba3631ab6fd1b7bb9f3444a5678e5b605c89f9b62298 | quote: "docs": "https://ipapi.is/free-tier.html?ref=api"
  - [7] 2026-11-02: a ranged read of the free IPv4 zip with no account answered HTTP 206 and the file is 65954248 bytes, last modified 30 Oct 2026 | capture: sha256:a1c03bf7c894fda1d859d5bf514578dbf61317b324014da4aa771450ec4602c8 | quote: Content-Range: bytes 0-1023/65954248
  - [3] 2026-11-02: keyless use is 30 lookups per client IP per UTC day, and a free account raises it to 1,000 lookups a day | capture: sha256:4ace7fef36d34d1e4711c915a9a456b85563ce642e85a99803a6fef70782cde4 | quote: Anonymous use is capped at 30 lookups per client IP per UTC day.
- sources:
  - [1] https://ipapi.is/pricing.html
  - [2] https://ipapi.is/geolocation.html
  - [3] https://ipapi.is/free-tier.html
  - [4] https://ipapi.is/app/signup
  - [5] https://ipapi.is/developers.html
  - [6] https://api.ipapi.is/?q=8.8.8.8
  - [7] https://ipapi.is/data/geolocationDatabaseIPv4.csv.zip
