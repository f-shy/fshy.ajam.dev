# DNS Made Easy

> dnsmadeeasy.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dnsmadeeasy/ | JSON https://fshy.ajam.dev/api/v1/entity/dnsmadeeasy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DNS Made Easy

- `domains-dns/dnsmadeeasy` | trial-only | evidence documented | binding retention-clamped | category managed authoritative DNS | tier Free 30-day trial (no perpetual free tier)
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T01:33:39.433Z (live) | stale on 2026-12-20
- url https://support.dnsmadeeasy.com/hc/en-us/articles/34327085326107-How-to-Sign-Up-With-DNS-Made-Easy-Free-Trial
- free tier: A free 30-day trial with 3 domains, 900 records, unlimited queries during the trial, 1 failover record, 5 query logs, 2FA, DNS analytics and a 100% SLA; there is no perpetual free tier and paid plans start at USD 6.25 per month | unit: seconds | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: the trial is time-boxed at 30 days rather than capacity-boxed; the 30-day length is the head-line allowance, so the unit names wall-clock time
- per-object cap: 900 records across 3 domains on the trial and 7,500 records across 25 domains on the cheapest paid Business plan; no single-record size cap is stated | source: [2] | note: the cap is a record count, not a byte size
- retention: the trial ends after 30 days, after which a paid plan is required to keep the zones active; no separate retention window for zones on a paid plan was read | days: 30 | source: [1] | note: 30 days is the trial length, which is the clock that decides access to the offer
- egress: unlimited DNS queries during the 30-day trial; on the paid Business plan 10M queries per month are included and overages are invoiced | metered: yes | free allowance: unlimited queries during the 30-day trial | source: [2]
- identity: email | detail: the trial signup guide lists username, password, confirm password, email, first name and last name, then company name, address, city, state, country, zip, phone, an optional fax, a secret question and secret answer, and an optional charity; no card is listed on the Create an Account page and Prerequisites is None, so no payment card is asked for at trial signup (https://support.dnsmadeeasy.com/hc/en-us/articles/34327085326107-How-to-Sign-Up-With-DNS-Made-Easy-Free-Trial). A phone number is requested as account information for the business
- interface: rest
- limits:
  - retention-clamped (binding): the free offer is a 30-day trial; a paid plan is required afterwards [1]
  - per-object-cap: 3 domains and 900 records on the trial; 25 domains and 7,500 records on the paid Business plan [2]
  - request-rate: 150 REST API requests per 5 minute scrolling window per API key [3]
  - write-gated: REST API keys are available only on Business / DNS-25 memberships or above; DNS-5 members must upgrade [4]
- binding note: the free offer is only a 30-day trial, so the clock ends access before the record count, API rate or API-key gate binds for a free user; API access is also gated to paid tiers
- interface detail: a REST API at https://api.dnsmadeeasy.com/V2.0/ using x-dnsme-apiKey, x-dnsme-requestDate and an HMAC-SHA1 x-dnsme-hmac header; a separate dynamic DNS update servlet at https://cp.dnsmadeeasy.com/servlet/updateip takes username, password, record id and ip. The API reference documents full record and domain CRUD, secondary DNS, failover and query-usage calls
- endpoint: part of interface detail
- tooling: curl with the x-dnsme-* HMAC headers, the sample dnsmeapi.pl Perl wrapper, and dynamic DNS clients such as ddclient; public SDKs and terraform providers exist from third parties
- composes with: a managed authoritative DNS service that can serve as a primary or secondary zone and can be paired with another DNS provider for redundancy; dynamic DNS clients update A records through the update servlet
- reliability: REST API calls with invalid credentials or an invalid request-date header receive HTTP 403, and calls arriving more than 30 seconds after the request-date and HMAC are generated are denied
- notes: The free offer is a 30-day trial and no perpetual free tier was found. DNS Made Easy is a DigiCert brand; the dnsmadeeasy.com marketing and free-trial pages now answer 404 or serve a DigiCert UltraDNS page, while the support articles, API reference and the first-party DigiCert pricing blog remain live. The blog and the signup guide disagree on the trial record count (900 versus 1,500), so the lower guide figure is used.
- evidence note: the free-trial signup guide, the DigiCert first-party pricing blog, the API reference, the API-key article, the add-ons article and the dynamic DNS article were read and quoted; no signup form was submitted, so the exact fields are as documented rather than measured. The marketing pricing and free-trial pages at dnsmadeeasy.com now answer 404 or serve a DigiCert UltraDNS page, so the trial terms come from the support guide and the first-party DigiCert blog
- self hosted: no
- evidence:
  - [2] 2026-11-19: the free offer is a 30-day trial | capture: sha256:8748bc724bc33be38b2650dc7f69fa4a8e4023c3056fca51267d6946deffdac7 | quote: DNS Made Easy provides users with a free 30-day trial that includes our most popular features.
  - [2] 2026-11-19: trial allowance of 3 domains, 900 records, unlimited queries, 1 failover record and 5 query logs | capture: sha256:8748bc724bc33be38b2650dc7f69fa4a8e4023c3056fca51267d6946deffdac7 | quote: - 3 domains - 900 records - Unlimited queries during the trial period - 1 Failover record - 5 query logs - 2FA - DNS analytics - 100% SLA-backed
  - [1] 2026-11-19: the trial is free for 30 days | capture: sha256:c6fcaeab0947b4fb7fd6cedcf754c8ed6902e677a7646fe7bcf77ae87a973b7b | quote: Cost: Free for 30 days
  - [1] 2026-11-19: the cheapest paid plan after the trial is USD 6.25 per month | capture: sha256:c6fcaeab0947b4fb7fd6cedcf754c8ed6902e677a7646fe7bcf77ae87a973b7b | quote: Cost: $6.25 mo / $75 billed annually
  - [1] 2026-11-19: the paid Business tier counts | capture: sha256:c6fcaeab0947b4fb7fd6cedcf754c8ed6902e677a7646fe7bcf77ae87a973b7b | quote: - 25 Domains - 7,500 Records - 10M Queries /month
  - [2] 2026-11-19: the trial signup asks for email and a name | capture: sha256:8748bc724bc33be38b2650dc7f69fa4a8e4023c3056fca51267d6946deffdac7 | quote: - Username - Password - Confirm Password - Email - First Name - Last Name
  - [2] 2026-11-19: the signup also asks for company details and a phone number | capture: sha256:8748bc724bc33be38b2650dc7f69fa4a8e4023c3056fca51267d6946deffdac7 | quote: Next, enter the account information for your business: - Company name - Address/City/State/Country/Zip - Phone - Fax (optional) - Secret question - Secret answer - Charity (optional)
  - [2] 2026-11-19: no prerequisite such as a card is stated for the trial | capture: sha256:8748bc724bc33be38b2650dc7f69fa4a8e4023c3056fca51267d6946deffdac7 | quote: Prerequisites - None
  - [4] 2026-11-19: REST API keys are gated to paid memberships | capture: sha256:ce7bf5f8f7dc810d1e59d5a131cf8a891dd25226a30529de38be965be2730ff0 | quote: Only Business / DNS-25 memberships or above have access to API Keys. Small Business / DNS-5 members will need to upgrade to [Business / DNS-25](https://dnsmadeeasy.com/pricing)to take advantage of our API service.
  - [3] 2026-11-19: the REST API is rate limited to 150 requests per 5 minute window per API key | capture: sha256:ad63eb397cbf261b07758536bb37f4eb7d47e4604743dba0a5dd5729d8479cde | quote: This limit is 150 requests per 5 minute scrolling window.
  - [3] 2026-11-19: the REST API endpoint | capture: sha256:ad63eb397cbf261b07758536bb37f4eb7d47e4604743dba0a5dd5729d8479cde | quote: The current endpoint for API V2.0 is available at: http\[s\]://api.dnsmadeeasy.com/V2.0/
  - [3] 2026-11-19: bad credentials or request date are refused with HTTP 403 | capture: sha256:ad63eb397cbf261b07758536bb37f4eb7d47e4604743dba0a5dd5729d8479cde
  - [3] 2026-11-19: a skewed request date causes denial | capture: sha256:ad63eb397cbf261b07758536bb37f4eb7d47e4604743dba0a5dd5729d8479cde | quote: If too much time has passed between when the _x-dnsme-requestDate_ and _x-dnsme-hmac_ strings were created and when the request is received by the DNS Made Easy API servers, then the request will be denied.
  - [5] 2026-11-19: a programmatic dynamic DNS update endpoint exists | capture: sha256:46acabc25245f661b6492a2ebcedfa4cc611c0e39888be89ad374d4a1676fdfd | quote: The servlet is: [https://cp.dnsmadeeasy.com/servlet/updateip](https://cp.dnsmadeeasy.com/servlet/updateip)?
  - [5] 2026-11-19: dynamic DNS updates use username, password, record id and ip | capture: sha256:46acabc25245f661b6492a2ebcedfa4cc611c0e39888be89ad374d4a1676fdfd | quote: The four parameters are: "username", "password", "id", and "ip".
  - [6] 2026-11-19: extra API call capacity is a paid add-on | capture: sha256:ccebf393316edf80a877464cce657bd668823e82b4b160fa49b102128fa0ee32 | quote: If additional API calls are needed for your account or a sub-user’s account, you can purchase an extra 150 API calls per 300 seconds (per user).
- sources:
  - [1] https://www.digicert.com/blog/how-much-does-dns-cost
  - [2] https://support.dnsmadeeasy.com/hc/en-us/articles/34327085326107-How-to-Sign-Up-With-DNS-Made-Easy-Free-Trial
  - [3] https://api-docs.dnsmadeeasy.com/
  - [4] https://support.dnsmadeeasy.com/hc/en-us/articles/34326955127451-Finding-or-Generating-API-Keys-In-DNS-Made-Easy
  - [5] https://support.dnsmadeeasy.com/hc/en-us/articles/34327262173723-Dynamic-DNS
  - [6] https://support.dnsmadeeasy.com/hc/en-us/articles/34327053801627-How-to-Purchase-Additional-DNS-Services-and-Add-ons
