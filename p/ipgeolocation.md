# IPGeolocation.io

> ipgeolocation.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipgeolocation/ | JSON https://fshy.ajam.dev/api/v1/entity/ipgeolocation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPGeolocation.io

- `data-apis/ipgeolocation-io` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Developer (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:33.117Z (live) | stale on 2026-12-04
- url https://ipgeolocation.io/pricing.html
- free tier: Developer plan: 1,000 API credits a day for life, no credit card; a standard IP lookup costs 1 credit; no overages and no bulk lookup on the free plan | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: single lookups; bulk lookup is not available on the free plan | source: [1]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: full name, email address and a password of 12 or more characters, or GitHub (Google sign-in is offered); no credit card
- interface: rest
- limits:
  - volume-quota (binding): 1,000 credits a day; a standard lookup is 1 credit [1]
- limits note: unverified: behind a sign-up: the full set of response headers of a keyed lookup
- interface detail: every successful response carries an X-Credits-Charged header with the credits billed; a request with no API key answers HTTP 401 and costs nothing
- tooling: any HTTP client
- composes with: 1,000 single lookups a day with location, country metadata, currency, ASN and time zone; security, company and bulk need a paid plan (Pro USD 79 a month for 1,000,000 credits). Bulk path: none free
- reliability: the free plan has no overage: past 1,000 API credits a day the API answers HTTP 429 until the allowance resets at 00:00 UTC, and no rate limit applies per second or per minute
- notes: Free requests: 1,000 credits a day, 1 per standard lookup. Rate limit: none published; requests past the credits are refused. Bulk path: none on the free plan.
- evidence note: the pricing page and the signup form were quoted on 2026-10-30; no keyed lookup was made, so no value is measured.
- extras:
  - bulk_path: none on the free plan
  - free_requests: 1,000 a day
- evidence:
  - [1] 2026-10-30: the free plan needs no card | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: No credit card required for the free plan
  - [1] 2026-10-30: the Developer plan gives 1000 credits | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: 1000 API Credits
  - [1] 2026-10-30: the credits are per day, for life | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: Per day for life
  - [1] 2026-10-30: the free plan has no overage | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: No overages on the free plan
  - [1] 2026-10-30: a lookup costs 1 credit | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: A standard unified IP lookup uses 1 credit.
  - [1] 2026-10-30: bulk lookup is not on the free plan | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: | Bulk Lookup | Not available in Free plan | Available in Paid plan | Available in Enterprise plan |
  - [1] 2026-10-30: Pro is USD 79 a month | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: $79/month
  - [1] 2026-10-30: Pro gives 1,000,000 credits a month | capture: sha256:4ce6c49e1ca7c11e100173976fe4d2ecb95f626394e9450902ba1fce89ac4776 | quote: 1000000 API Credits
  - [2] 2026-10-31: the signup page restates 1,000 free credits a day | capture: sha256:3e739383d5560628fe16b7e0ef68403dcdd95fb3c000d77c85a340109d8bca1a | quote: 1,000 free API credits per day. No credit card required.
  - [2] 2026-10-31: GitHub sign-in is offered | capture: sha256:3e739383d5560628fe16b7e0ef68403dcdd95fb3c000d77c85a340109d8bca1a | quote: Continue with GitHub
  - [2] 2026-10-31: the signup form asks a full name | capture: sha256:3e739383d5560628fe16b7e0ef68403dcdd95fb3c000d77c85a340109d8bca1a | quote: Full name
  - [2] 2026-10-31: the password is 12 to 64 characters | capture: sha256:3e739383d5560628fe16b7e0ef68403dcdd95fb3c000d77c85a340109d8bca1a | quote: Use 12–64 characters.
  - [3] 2026-11-02: the free plan resets its 1,000 daily API credits at 00:00 UTC, has no limit per second or per minute, and answers HTTP 429 until the reset with no overage | capture: sha256:18555bb83c54d58c2775b4361c7f55ce510a836d2b1694788801cb9e1e900dc6 | quote: | When credits run out | HTTP 429 Too Many Requests until the reset; no overage charges |
  - [4] 2026-11-02: every successful response carries an X-Credits-Charged header, and a request with no API key answers HTTP 401 and uses no credits | capture: sha256:5cb6acfc61570713df000bd354e5322a3dcc7a8f3212b6cc12a323539301fee4 | quote: Every successful response includes an `X-Credits-Charged` header showing the number of credits deducted.
  - probe:https://api.ipgeolocation.io/v3/ipgeo?ip=8.8.8.8 2026-11-02: a lookup with no API key answered HTTP 401 with a JSON message, so a keyed answer and its headers show only after sign-up | capture: sha256:5a142872ba31aa814bf27943bc0aafe88bf6dea4015bb4bc4c09ddd390916950 | quote: "status": 401
  - [1] 2026-11-02: the Developer plan gives 1,000 credits a day for life with no credit card and no overage, and a standard IP lookup uses 1 credit | capture: sha256:ad742a06a99766ebf955a97aa9fe8ddc2da594b535a367996ef6e79c3f000264 | quote: The free Developer plan gives you 1,000 credits a day for life, with no credit card.
- sources:
  - [1] https://ipgeolocation.io/pricing.html
  - [2] https://app.ipgeolocation.io/signup
  - [3] https://ipgeolocation.io/help/whats-in-the-free-plan
  - [4] https://ipgeolocation.io/help/how-ipgeolocation-io-credits-work
