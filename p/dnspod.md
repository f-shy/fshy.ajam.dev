# DNSPod

> dnspod.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dnspod/ | JSON https://fshy.ajam.dev/api/v1/entity/dnspod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DNSPod

- `domains-dns/dnspod-free` | qualifies-with-caveat | evidence documented | binding per-object-cap | category managed authoritative DNS | tier Free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T16:43:07.606Z (live) | stale on 2026-12-04
- url https://docs.dnspod.com/dns/help-diff-plan/
- free tier: the Free DNS plan: unlimited records, 5 subdomain levels, 2 URL forwards, round-robin DNS of up to 10 records per host, API supported, minimum TTL 600 s; it is activated by default once a domain is added | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: no record cap on the Free plan (records unlimited); 5 subdomain levels, 2 URL forwards and up to 10 round-robin records per host | source: [1]
- retention: unverified: the plan, overview and API pages read state no inactivity, renewal or confirmation rule for a Free zone | source: [1]
- egress: no DNS query cap published on the pages read | metered: no | source: [1]
- identity: any-phone | detail: the international site uses a Tencent Cloud account: an e-mail address with a code sent to it, then a mobile number of the registration location with an SMS code, at most 5 accounts per number; the +86 area code is not supported on the international site; no card is asked on the pages read (https://www.tencentcloud.com/document/product/378/17985, https://docs.dnspod.com/account/accountupgrade/)
- interface: rest
- limits:
  - per-object-cap (binding): 5 subdomain levels, 2 URL forwards, up to 10 round-robin records per host, minimum TTL 600 s on the Free plan [1]
- binding note: the 600 s TTL floor decides for a dynamic record; the identity gate is a phone number with an SMS code
- interface detail: a dynamic-DNS update call on the international API, POST https://api.dnspod.com/Record.Ddns with a login_token and the parameters domain_id, record_id, record_line and sub_domain; the pages read give no rate limit for it
- tooling: curl or any HTTP client against the DNSPod API, and the DNSPod console; an update must name the domain_id and the record_id
- composes with: a free zone for a domain the user already owns, with A, CNAME and subdomain records pointed at any address; it can hold a dynamic record but the 600 s minimum TTL slows how quickly an address change reaches resolvers
- reliability: unverified: the pages read state no inactivity rule and no SLA for the Free plan
- notes: Confirmation interval: none stated. The mainland-China site dnspod.cn has its own e-mail registration that also binds and verifies a mobile number.
- evidence note: the plan overview, the dynamic-DNS API page, the Tencent Cloud sign-up page and the account-upgrade page were read and quoted; no sign-up form was submitted and the update call was not probed because it needs a token
- evidence:
  - [1] 2026-11-03: DNSPod has four DNS plans, the first of them Free | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: DNSPod provides 4 DNS plans: Free, Professional, Enterprise, and Ultimate.
  - [1] 2026-11-03: the Free plan is activated by default after a domain is registered, with no separate application | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: After a domain name is successfully registered, the Free plan will be activated by default
  - [1] 2026-11-03: the Free plan has unlimited records | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | Free | Records | Unlimited |
  - [1] 2026-11-03: the Free plan supports 5 subdomain levels | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | Subdomain levels | 5 | |
  - [1] 2026-11-03: the Free plan includes 2 URL forwards | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | URL forwards | 2 | |
  - [1] 2026-11-03: the Free plan allows round-robin DNS of up to 10 records per host | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | Round-Robin DNS records | Up to 10 records per host |
  - [2] 2026-11-03: the update is a POST to api.dnspod.com/Record.Ddns carrying a login_token | capture: sha256:d6f884c821b70b3f6debac575ed6fcc852e20aca714acd99d328c84e4067b7d0 | quote: curl -X POST https://api.dnspod.com/Record.Ddns -d 'login_token=
  - [2] 2026-11-03: the update names the record by its record id | capture: sha256:d6f884c821b70b3f6debac575ed6fcc852e20aca714acd99d328c84e4067b7d0 | quote: | record_id | yes | The record id. Mandatory parameter. |
  - [3] 2026-11-03: the mainland-China site's e-mail registration binds and verifies a mobile number | capture: sha256:302d07f663d2f9dc352f1a7dc77444c1d32174efac5a65b63a52a93061ff5764 | quote: 绑定手机号码并验证
  - [1] 2026-11-03: the Free plan supports the API | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | API | Supported | |
  - [1] 2026-11-03: the Free plan minimum TTL is 600 seconds | capture: sha256:cb9aca1933e13459fb64d467c212a97072d2af84ca13fa192c72af8cddad8c89 | quote: | Minimum TTL value | 600s | |
  - [4] 2026-11-03: the Free plan lets a user add domains in the console and set records such as A and CNAME | capture: sha256:8da8c37c7b09cf803feb7d497ebb95ec39616360472092cc4759bd8aa92e9c52 | quote: The Free DNS plan supports adding domains in the DNSPod console and setting up DNS records such as A and CNAME.
  - [2] 2026-11-03: the Record.Ddns API updates a dynamic DNS record | capture: sha256:d6f884c821b70b3f6debac575ed6fcc852e20aca714acd99d328c84e4067b7d0 | quote: This API (Record.Ddns) is used to update the dynamic DNS rcord.
  - [2] 2026-11-03: the update is an HTTP POST | capture: sha256:d6f884c821b70b3f6debac575ed6fcc852e20aca714acd99d328c84e4067b7d0 | quote: HTTP request method: POST
  - [5] 2026-11-03: sign-up needs an e-mail address and a verification code sent to it | capture: sha256:232f60ab6a2eb2da37ab77d8fd40993e43d05aaa02b485a440e465a7361160ad | quote: 4. Click Send code, then enter the verification code received by your registered email address.
  - [5] 2026-11-03: account completion asks for a mobile number of the registration location | capture: sha256:232f60ab6a2eb2da37ab77d8fd40993e43d05aaa02b485a440e465a7361160ad | quote: 4. Enter the mobile number of the registration location.
  - [5] 2026-11-03: an SMS verification code is sent to that mobile number | capture: sha256:232f60ab6a2eb2da37ab77d8fd40993e43d05aaa02b485a440e465a7361160ad | quote: 5. Obtain and enter the verification code sent to your mobile number.
  - [5] 2026-11-03: one mobile number serves at most 5 accounts | capture: sha256:232f60ab6a2eb2da37ab77d8fd40993e43d05aaa02b485a440e465a7361160ad | quote: Each mobile number can be used for at most 5 Tencent Cloud accounts.
  - [6] 2026-11-03: the international DNSPod site runs on the Tencent Cloud account system | capture: sha256:acfd15322037686046fa81010b172c0924e53752448f4590d3577854b1293497 | quote: the new website will use the Tencent Cloud account system
  - [6] 2026-11-03: the +86 area code is not accepted for the recovery mobile number on the international site | capture: sha256:acfd15322037686046fa81010b172c0924e53752448f4590d3577854b1293497 | quote: the +86 area code is not supported
- sources:
  - [1] https://docs.dnspod.com/dns/help-diff-plan/
  - [2] https://docs.dnspod.com/api/update-the-dynamic-dns-record/
  - [3] https://docs.dnspod.cn/account/register-dnspod/
  - [4] https://docs.dnspod.com/dns/dns-overview/
  - [5] https://www.tencentcloud.com/document/product/378/17985
  - [6] https://docs.dnspod.com/account/accountupgrade/
