# ipapi.com

> ipapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipapi-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ipapi-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipapi.com (APILayer)

- `data-apis/ipapi-com` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://ipapi.com/pricing
- free tier: Free plan, USD 0.00 a month: 100 lookups a month with location data and HTTPS and no support | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Standard is USD 12.99 a month (USD 11.99 billed yearly) for 50,000 lookups, then USD 0.0010392 each; Business USD 59.99 for 500,000 with Bulk Lookups; Business Pro USD 99.99 for 2,000,000. An answer that errors is not counted.
- per-object cap: one IP per request on the Free plan; Bulk Lookups are listed from the Business plan | source: [1]
- retention: not applicable: a lookup API | source: [1]
- egress: not applicable: JSON or XML answers, not metered in bytes | metered: no | source: [1]
- identity: email | detail: a sign-up with first name, last name, email, password and a billing address (address, postal code, country, city); no card number is asked on the free sign-up form
- interface: rest
- limits:
  - volume-quota (binding): 100 lookups a month on the Free plan [1]
- binding note: 100 lookups a month is exhausted first; no rate is stated.
- interface detail: GET http(s)://api.ipapi.com/api/{ip}?access_key={key} answers JSON or XML; a call without a key answers HTTP 401 with error code 101 missing_access_key
- endpoint: https://api.ipapi.com/api/{ip}
- tooling: any HTTP client
- composes with: 100 lookups a month is a test allowance only; the paid plans from USD 12.99 a month are the working route. Bulk path: Bulk Lookups on Business, USD 59.99 a month, and above; none free. APILayer, the vendor, also sells ipstack, which has its own record.
- reliability: usage notices are sent at 75%, 90% and 100% of the monthly allowance; a call without a key answers HTTP 401 with error code 101
- notes: Free requests: 100 a month. Rate limit: not stated. Bulk path: Bulk Lookups from the Business plan; none free.
- evidence note: The pricing, FAQ, home and sign-up pages were quoted on 2026-11-02 and a keyless call answered HTTP 401; no keyed lookup was made, so the answers and any rate limit on the Free plan are unverified.
- extras:
  - bulk_path: Bulk Lookups from Business, USD 59.99 a month; none free
  - free_requests: 100 a month
- evidence:
  - [1] 2026-11-02: the Free plan lists 100 lookups | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: 100 Lookups
  - [1] 2026-11-02: the Free plan costs USD 0.00 a month | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: $0.00 per month
  - [1] 2026-11-02: the Free plan lists 100 lookups, no support, location data and HTTPS encryption | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: 100 Lookups * No Support * Location Data * HTTPS Encryption
  - [2] 2026-11-02: the vendor is APILayer | capture: sha256:cd5d241d763172401af8dfc1b2aff92db8471cb7a1db987b523e94860cc028f7 | quote: ipapi is a product built and maintained by apilayer, a software company based in London, United Kingdom and Vienna, Austria.
  - [3] 2026-11-02: the free allowance is 100 requests a month and Standard starts at USD 12.99 | capture: sha256:3c5c09d1d737919232655929d08bf0307d3175414b46da29de49767751bde8d9 | quote: Make 100 requests a month for free — need more? Standard plans start at just $12.99
  - [2] 2026-11-02: the Free plan allows up to 100 API requests | capture: sha256:cd5d241d763172401af8dfc1b2aff92db8471cb7a1db987b523e94860cc028f7 | quote: The ipapi Free Plan is a great way to explore the API and see how it fits your use case, with up to 100 API requests.
  - [1] 2026-11-02: Standard is USD 12.99 a month or USD 11.99 billed yearly | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: $12.99 per month or $11.99 if billed yearly
  - [1] 2026-11-02: Standard allows 50,000 lookups | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: 50,000 Lookups
  - [1] 2026-11-02: Standard overage is USD 0.0010392 a lookup | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: + 0.0010392 each
  - [1] 2026-11-02: Business is USD 59.99 a month | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: $59.99 per month or $52.99 if billed yearly
  - [1] 2026-11-02: Business allows 500,000 lookups | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: 500,000 Lookups
  - [1] 2026-11-02: Bulk Lookups are listed on the higher plans | capture: sha256:ba567cfd57d42dee800e8552eb485340e3b5aac21752fa047108aed137f9e3d7 | quote: Bulk Lookups
  - [2] 2026-11-02: bulk lookups depend on the plan | capture: sha256:cd5d241d763172401af8dfc1b2aff92db8471cb7a1db987b523e94860cc028f7 | quote: Other factors include HTTPS encryption, advanced IP data modules and the ability to make bulk IP lookups.
  - [1] 2026-11-02: an answer that errors is not counted | capture: sha256:3c631d852cdf876ff6ade3841620a5ede384486708addbe5f05eab763c89537d | quote: In the event that an error should occur, your request does not count towards the monthly volume.
  - [1] 2026-11-02: usage notices at 75%, 90% and 100% | capture: sha256:3c631d852cdf876ff6ade3841620a5ede384486708addbe5f05eab763c89537d | quote: Users will be automatically notified via email and in their account dashboard as soon as at least 75%, 90%, and 100% of their monthly API quota has been reached.
  - [4] 2026-11-02: the sign-up form asks for a first name | capture: sha256:fa4348ab38dd0ee86c6335e85fc037b4810f0d4d1b5ef4904e46f17ecd85b2bc | quote: First Name\*
  - [4] 2026-11-02: the sign-up form asks for a last name | capture: sha256:fa4348ab38dd0ee86c6335e85fc037b4810f0d4d1b5ef4904e46f17ecd85b2bc | quote: Last Name\*
  - [4] 2026-11-02: the sign-up form asks for an email | capture: sha256:fa4348ab38dd0ee86c6335e85fc037b4810f0d4d1b5ef4904e46f17ecd85b2bc | quote: Email\*
  - [4] 2026-11-02: the sign-up form asks for a postal code | capture: sha256:fa4348ab38dd0ee86c6335e85fc037b4810f0d4d1b5ef4904e46f17ecd85b2bc | quote: Postal Code\*
  - [4] 2026-11-02: the sign-up form asks for an address | capture: sha256:fa4348ab38dd0ee86c6335e85fc037b4810f0d4d1b5ef4904e46f17ecd85b2bc | quote: Address\*
  - probe:https://api.ipapi.com/api/8.8.8.8 2026-11-02: a keyless GET of api.ipapi.com answered HTTP 401 | capture: sha256:32a07018f3fad6162751622556b88f1ad05437f79f2d8ab8e1c3504ea67f4649 | quote: "status": 401
  - probe:https://api.ipapi.com/api/8.8.8.8 2026-11-02: the keyless answer is error code 101 missing_access_key | capture: sha256:9c6236715bb8db4001544e79d9e830eddd952f053ab9d565a3847de65e6bdf83 | quote: "type": "missing_access_key"
- sources:
  - [1] https://ipapi.com/pricing
  - [2] https://ipapi.com/faq
  - [3] https://ipapi.com/
  - [4] https://ipapi.com/signup
