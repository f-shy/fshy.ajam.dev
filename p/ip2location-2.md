# IP2Location.io

> ip2location.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip2location-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ip2location-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP2Location.io

- `data-apis/ip2location-io` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://www.ip2location.io/pricing
- free tier: Free plan: 50K IP geolocation queries a month with an API key (plus 500 Domain WHOIS and 50 Hosted Domain queries), 11 IP attributes; keyless: 1,000 queries a day with no registration | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the keyless quota resets at 00:00 UTC daily and is served from the US East region only
- per-object cap: not stated: single-IP lookups
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: name, work email and password with an arithmetic question; one plan per email address; the keyless route needs nothing
- interface: rest
- limits:
  - volume-quota (binding): 50K queries a month with a free key; 1,000 a day keyless, reset at 00:00 UTC; the free plan stops when queries run out [1]
- interface detail: GET api.ip2location.io/?ip=IP&format=json, keyless or with key=KEY; JSON answer with country, region, city, coordinates, ZIP, time zone, ASN and a public-proxy flag
- endpoint: https://api.ip2location.io/
- tooling: any HTTP client; vendor SDKs for PHP, Python, .NET and others
- composes with: 1,000 keyless lookups a day with no account, or 50K a month with a free key; the LITE database (separate record) covers unmetered local lookups. Bulk path: none on the free API plan
- reliability: the free plan stops answering when its queries run out (no overage); the keyless route is served from one US East region
- notes: Free requests: 50K a month with a free key, or 1,000 a day keyless. Rate limit: none published beyond the quotas. Bulk path: none on the free API; the separate IP2Location LITE download is the bulk route.
- evidence note: the pricing page and the signup form were quoted on 2026-10-30, and a keyless lookup answered HTTP 200 naming its 1,000-a-day limit. No account was opened, so the 50K keyed quota is documented only.
- extras:
  - bulk_path: none on the free API plan
  - free_requests: 50K a month with a key; 1,000 a day keyless
- evidence:
  - [1] 2026-10-30: the Free plan gives 50K geolocation queries a month | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: 50K IP Geolocation API queries/month
  - [1] 2026-10-30:  | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5
  - [1] 2026-10-30: the Free plan returns 11 IP attributes | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: 11 IP Attributes
  - [1] 2026-10-30: the free plan stops when its queries run out | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: If you are subscribed to a free plan, the web service will be stopped once you have run out of queries.
  - [1] 2026-10-30: keyless use gives 1,000 queries a day | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: You can perform up to 1,000 queries daily using the api.ip2location.io endpoint without the need for an API key to obtain geolocation information instantly.
  - [1] 2026-10-30: keyless 1,000 a day against 50,000 a month with a free key | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: | Query Limit | 1,000 queries per day | 50,000 queries per month |
  - [1] 2026-10-30: the keyless route is served from US East | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: | Infrastructure | Hosted in the US East Region | Global Load Balancers spread across more than 10 strategic regions worldwide |
  - [1] 2026-10-30: the keyless limit resets at 00:00 UTC | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: Query limit will be reset at 00:00 UTC daily.
  - [1] 2026-10-30: one plan per email address | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: No. You can only subscribe to one plan using one email address.
  - [1] 2026-10-30: the keyless endpoint | capture: sha256:20ea4f3b83e30b8b7e4b3132cc48a84442ed8a883cbba1b1813cfb39ce2ad5f5 | quote: curl "https://api.ip2location.io/?ip=8.8.8.8&format=json"
  - [2] 2026-10-30: the signup form asks a work email | capture: sha256:42beac289e79f9f79b530ff947ea6c2229e888b94900605f0bc15765cb65f728 | quote: Work Email
  - [2] 2026-10-30: the signup form has an arithmetic check | capture: sha256:42beac289e79f9f79b530ff947ea6c2229e888b94900605f0bc15765cb65f728 | quote: Please resolve the question below:
  - probe:https://api.ip2location.io/?ip=8.8.8.8 2026-10-30: a keyless lookup answered and named its 1,000-a-day limit | capture: sha256:a87fb97a4ec7836ce9400647f05817390cccc4aadc996e91aa7478f01d63c460 | quote: Limit to 1,000 queries per day.
- sources:
  - [1] https://www.ip2location.io/pricing
  - [2] https://www.ip2location.io/sign-up
