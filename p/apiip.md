# Apiip

> apiip.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apiip/ | JSON https://fshy.ajam.dev/api/v1/entity/apiip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apiip

- `data-apis/apiip` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://apiip.net/get-started
- free tier: Free plan, EUR 0.00: 1,000 requests a month, no hidden fees and no credit card; an access key is issued after an account is created | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Basic is EUR 9.99 a month (EUR 7.99 billed yearly) for 100,000 requests and Professional EUR 49.99 (EUR 39.99) for 1,000,000. Past the monthly allowance the API answers HTTP 403 usage_limit_reached.
- per-object cap: a bulk lookup takes up to 50 IPs as a comma-separated list; a single lookup takes one | source: [2]
- retention: not applicable: a lookup API | source: [2]
- egress: not applicable: JSON or XML answers, not metered in bytes | metered: no | source: [2]
- identity: email | detail: an account is needed for the access key; the sign-up form has account details, billing details with a country selector and company details; no credit card is asked on the Free plan
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a month on the Free plan; HTTP 403 usage_limit_reached past it [1]
  - request-rate: 100 requests per second from a single IP address; HTTP 429 too_many_requests past it [3]
  - per-object-cap: up to 50 IPs per bulk lookup request [2]
- binding note: 1,000 requests a month is met long before the 100 requests a second rate.
- interface detail: GET https://apiip.net/api/check?ip={ip}&accessKey={key} answers JSON or XML; a comma-separated list of up to 50 IPs does a bulk lookup on plans that include it; check without an ip parameter looks up the caller
- endpoint: part of interface detail
- tooling: any HTTP client or the vendor's client packages for JavaScript, Python and PHP
- composes with: 1,000 lookups a month with location, currency, language, time zone and security modules is a test allowance; the paid plans are the working route. Bulk path: bulk lookup of up to 50 IPs on plans that include it; whether Free includes it is unverified.
- reliability: past the monthly allowance the API answers HTTP 403 usage_limit_reached and past the per-second rate HTTP 429 too_many_requests; a keyless call answered HTTP 401 missing_access_key
- notes: Free requests: 1,000 a month. Rate limit: 100 requests a second from one IP address. Bulk path: bulk lookup of up to 50 IPs on plans that include it; whether Free includes it is unverified.
- evidence note: The plan list, documentation, FAQ and sign-up page were quoted on 2026-11-02 and a keyless call answered HTTP 401; no keyed lookup was made. The plan list as rendered does not show which modules the Free plan excludes, and the account-detail fields of the sign-up form are rendered by script, so whether Free includes bulk lookup and which account fields are required are unverified.
- extras:
  - bulk_path: comma-separated list of up to 50 IPs on plans with Bulk Lookup
  - free_requests: 1,000 a month
- evidence:
  - [1] 2026-11-02: the free plan has no hidden fees and needs no credit card | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: No hidden fees No credit card required
  - [1] 2026-11-02: the EUR 0.00 plan lists 1,000 requests a month | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: - 1,000 req / mo
  - [1] 2026-11-02: the free plan is priced EUR 0.00 | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: #### €0.00
  - [1] 2026-11-02: Basic is EUR 9.99 a month | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: €9.99
  - [1] 2026-11-02: Basic allows 100,000 requests a month | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: - 100,000 req / mo
  - [1] 2026-11-02: Professional is EUR 49.99 a month | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: €49.99
  - [1] 2026-11-02: Professional allows 1,000,000 requests a month | capture: sha256:4c805a719e10099f04683b59a74179408ba0859ad88ea12669e3c8a055f8140b | quote: - 1,000,000 req / mo
  - [2] 2026-11-02: an account is created first and an access key is assigned | capture: sha256:fa273506d36a0d77eec8871836ca5a7f664f7f4ee104379695ff64a8023892bc | quote: After creating an account, you will be assigned a API access key, a unique hash consisting of 36 characters that will allow you to authenticate with the API interface.
  - [2] 2026-11-02: a bulk lookup takes up to 50 IPs | capture: sha256:fa273506d36a0d77eec8871836ca5a7f664f7f4ee104379695ff64a8023892bc | quote: | `ip` | [Required] A comma-separated list of IPv4 or IPv6 addresses of your choice.(Limit: 50 values) |
  - [2] 2026-11-02: bulk lookup depends on the plan | capture: sha256:fa273506d36a0d77eec8871836ca5a7f664f7f4ee104379695ff64a8023892bc | quote: | `403` | `bulk_not_supported` | Your current subscription plan does not include Bulk Lookup. |
  - [2] 2026-11-02: past the monthly limit the API answers HTTP 403 usage_limit_reached | capture: sha256:fa273506d36a0d77eec8871836ca5a7f664f7f4ee104379695ff64a8023892bc | quote: | `403` | `usage_limit_reached` | Your API usage limit has been reached. Please upgrade your plan. |
  - [2] 2026-11-02: past the per-second rate the API answers HTTP 429 | capture: sha256:fa273506d36a0d77eec8871836ca5a7f664f7f4ee104379695ff64a8023892bc | quote: | `429` | `too_many_requests` | You exceeded the allowed number of requests per second, if you need more, please send us a message on www.apiip.net/contact |
  - [3] 2026-11-02: the per-second limit is 100 requests from a single IP address | capture: sha256:f931cdcee738913b7bf45d57078850ddddf828925d2931b1abc57a0646aca6e5 | quote: To ensure stability, API requests are limited to 100 requests per second from a single IP address.
  - [4] 2026-11-02: the sign-up form asks for a billing country | capture: sha256:4c1219fdf393b425d7988903e517b13f9ff6f9d6d99fff37c3bbd9e67c01c3d3 | quote: Choose your country \*
  - [4] 2026-11-02: the sign-up form has an account details section | capture: sha256:4c1219fdf393b425d7988903e517b13f9ff6f9d6d99fff37c3bbd9e67c01c3d3 | quote: ACCOUNT DETAILS
  - [4] 2026-11-02: the sign-up form has a company details section | capture: sha256:4c1219fdf393b425d7988903e517b13f9ff6f9d6d99fff37c3bbd9e67c01c3d3 | quote: COMPANY DETAILS
  - [4] 2026-11-02: the sign-up form ends with an agreement checkbox and a Signup button | capture: sha256:4c1219fdf393b425d7988903e517b13f9ff6f9d6d99fff37c3bbd9e67c01c3d3 | quote: I have read and agree to the
  - [5] 2026-11-02: a keyless call answers HTTP 401 missing_access_key | capture: sha256:d5f74679db9ad18ad3d178fb9375ef77dfd6f47f0a1b04772cf9ee7607b32c6b | quote: {"success":false,"message":{"code":401,"type":"missing_access_key","info":"Api access key is required!"}}
- sources:
  - [1] https://apiip.net/get-started
  - [2] https://apiip.net/documentation
  - [3] https://apiip.net/faq
  - [4] https://apiip.net/signup
  - [5] https://apiip.net/api/check?ip=8.8.8.8
