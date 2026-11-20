# No-IP

> noip.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/noip/ | JSON https://fshy.ajam.dev/api/v1/entity/noip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## No-IP

- `domains-dns/no-ip-free` | qualifies-with-caveat | evidence documented | binding retention-clamped | category free dynamic DNS hostname | tier Free Dynamic DNS
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:07.606Z (live) | stale on 2026-12-04
- url https://www.noip.com/free
- free tier: 1 hostname on a No-IP shared domain, no credit card; the hostname must be confirmed every 30 days or it is deleted | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: 1 hostname on the free plan, on one of 30+ No-IP shared domains; the zone belongs to No-IP, so the user holds no record count of its own; hostnames may be type A, AAAA or Port 80 Redirect | source: [1]
- retention: a free hostname is active for 23 days, may be confirmed in the next 7 days, stops resolving when it expires, sits 14 more days in redemption and is then deleted and open to anyone; an update from a client does not confirm it | days: 30 | source: [2] | note: confirmation is a web login or an e-mailed link
- egress: no DNS query cap published on the pages read | metered: no | source: [1]
- identity: email | detail: the sign-up form asks for an e-mail address and a password and a terms checkbox that states one free account; the free page says no credit card is required (https://www.noip.com/sign-up, https://www.noip.com/free); no phone field in the captured form text
- interface: rest
- limits:
  - retention-clamped (binding): confirm every 30 days: active 23 days, 7-day confirmation window, 14-day redemption, then deletion [2]
  - per-object-cap: 1 hostname on the free plan [1]
- binding note: the 30-day manual confirmation is what decides; an update client keeps the address current but does not renew the hostname
- interface detail: a dyndns2-style HTTP update request, GET https://dynupdate.no-ip.com/nic/update?hostname=HOST&myip=IP with HTTP Basic auth (the account e-mail address and password), on port 443 over HTTPS or on ports 80 and 8245 over HTTP; the response is a text code such as good, nochg or badauth; the pages read list a RESTful API only under the contact-sales Branded Remote Access plan
- tooling: the free No-IP Dynamic Update Client for Windows, macOS and Linux, any dyndns2-compatible client or router, and curl from cron; confirmation itself is a web or e-mail action with no documented API
- composes with: a name for a changing address and nothing else on the free plan; the domains are No-IP's, so the name cannot be a zone of its own, and the 30-day confirmation has to be done by hand
- reliability: a free hostname silently stops resolving if the 30-day confirmation is missed; the update endpoint answers HTTP 401 with the body badauth for a request without credentials; a client without an approved User-Agent can be rate-limited or blocked, and the badagent and abuse codes tell a client to stop updating
- notes: Free confirmation interval: 30 days (23 active, 7 to confirm, then 14 in redemption). The paid Enhanced plan, USD 2.50 a month billed annually for 5 hostnames, lists hostnames that never expire.
- evidence note: the free-plan page, the confirmation knowledge-base page, the FAQ, the sign-up page and the update protocol pages were read and quoted; the unauthenticated update endpoint was probed once and answered 401 badauth
- evidence:
  - [1] 2026-11-03: the free plan lists 1 hostname | capture: sha256:b831197726766f7013fae7ea2a4e76a584182eef9bb06ad3822c877a22d55d15 | quote: 1 Hostname
  - [1] 2026-11-03: no credit card is required for the free plan | capture: sha256:b831197726766f7013fae7ea2a4e76a584182eef9bb06ad3822c877a22d55d15 | quote: When we say free, we actually mean free - no credit card required, ever.
  - [2] 2026-11-03: a free hostname must be confirmed every 30 days | capture: sha256:e5404f7962279e4a7449a46276e2cc110f9c88105734202368b48db80e7ed82a | quote: Free hostnames require confirmation every 30 days to remain active in your account.
  - [2] 2026-11-03: the confirmation window opens after 23 days and lasts 7 days | capture: sha256:e5404f7962279e4a7449a46276e2cc110f9c88105734202368b48db80e7ed82a | quote: After 23 days the hostname will enter a “Confirmation” period where it will be eligible to be confirmed for the next 7 days.
  - [2] 2026-11-03: after the 14-day redemption the hostname is deleted and anyone can claim it | capture: sha256:e5404f7962279e4a7449a46276e2cc110f9c88105734202368b48db80e7ed82a | quote: After 14 days the hostname will be deleted and be available for you or anyone else to claim.
  - [3] 2026-11-03: an IP update does not confirm a free hostname | capture: sha256:43d2e9475228f17a9425cfb4c6ab7a7e19cf7d0f318bf46b040fbbd8fec3cfb6 | quote: Please note that updates on your hostname do not confirm them.
  - [4] 2026-11-03: free hostnames are created on 30+ shared domains | capture: sha256:af457843929cd2d33892e1ae674898e7625d604785d20f4e1a7f76f1828dd520 | quote: Hostname creation is available on 30+ domains with Free Dynamic DNS and 50+ premium domains with Enhanced or Pro plans.
  - [4] 2026-11-03: free plans offer limited hostname and domain options | capture: sha256:af457843929cd2d33892e1ae674898e7625d604785d20f4e1a7f76f1828dd520 | quote: Offer limited hostname and domain options
  - [5] 2026-11-03: the update is an HTTP request to dynupdate.no-ip.com/nic/update | capture: sha256:8b968a0058e7095b13513e5229f7853539af1936680650f20d420286f3ec1a10 | quote: Dynamic updates are performed by making an HTTP request to one of the following URLs:
  - [5] 2026-11-03: the hostnames updated may be A, AAAA or Port 80 Redirect | capture: sha256:8b968a0058e7095b13513e5229f7853539af1936680650f20d420286f3ec1a10 | quote: Hostnames may be of type A, AAAA, or Port 80 Redirect.
  - [5] 2026-11-03: the update credential is the account e-mail address and password | capture: sha256:8b968a0058e7095b13513e5229f7853539af1936680650f20d420286f3ec1a10 | quote: No-IP uses an email address as the username.
  - [5] 2026-11-03: a client without an approved User-Agent risks being rate-limited or blocked | capture: sha256:8b968a0058e7095b13513e5229f7853539af1936680650f20d420286f3ec1a10 | quote: Clients that do not supply a certified and approved User-Agent risk being rate-limited or blocked from the system.
  - [6] 2026-11-03: badauth is the response code for a bad username and password | capture: sha256:bfb7cc79ee06ccd2afdb211ac1a002503dc2fbf9a37b9a2245fb628778271a2b | quote: | badauth | Error | Invalid username password combination. |
  - [7] 2026-11-03: the sign-up form carries a terms checkbox stating one free account | capture: sha256:af49673549b447a8fcb35add31d9df93136df52b3858357f256490dfc420975e | quote: I also agree that I will only create one free account.
  - probe:https://dynupdate.no-ip.com/nic/update 2026-11-03: the update endpoint is live and answers HTTP 401 without credentials | capture: sha256:5491abcb5accaf340650a7888be0b591dddf0787af7380a4e9e4d69c5ffdc1c2 | quote: "status": 401
  - probe:body-noip 2026-11-03: the body of that unauthenticated answer is the text code badauth | capture: sha256:129513079a33740dc75b859502965c7aa2c05cdcf016d9228b96fe6dfdbbe796 | quote: badauth
  - [8] 2026-11-03: the paid Enhanced Dynamic DNS plan with 5 hostnames is USD 2.50 a month billed annually | capture: sha256:7df75a9349531442c8e24c73014591e4deb52f885b915e762f3da7d283fc697a | quote: $2.50/mo When billed annually
  - [8] 2026-11-03: the paid Enhanced plan lists hostnames that never expire | capture: sha256:7df75a9349531442c8e24c73014591e4deb52f885b915e762f3da7d283fc697a | quote: Hostnames Never Expire
  - [9] 2026-11-03: a RESTful API is listed under the contact-sales Branded Remote Access plan | capture: sha256:00ac13442ed927e701f01c793e6794656a59a2c75b943c5dc2640d5889cc8aab | quote: RESTful API
  - [1] 2026-11-03: free dynamic DNS is the entry level service on names such as yourname.no-ip.info | capture: sha256:b831197726766f7013fae7ea2a4e76a584182eef9bb06ad3822c877a22d55d15 | quote: No-IP Free Dynamic DNS is our entry level service.
  - [1] 2026-11-03: no card is required for the free plan | capture: sha256:b831197726766f7013fae7ea2a4e76a584182eef9bb06ad3822c877a22d55d15 | quote: When we say free, we actually mean free - no credit card required, ever.
  - [10] 2026-11-03: a free account has 1 hostname | capture: sha256:5ead6eccd54641c34e130d412a3c4b24aba4a78e66279a535e20d2c536696e2d | quote: 1 Hostname
  - [2] 2026-11-03: free hostnames need confirmation every 30 days | capture: sha256:e5404f7962279e4a7449a46276e2cc110f9c88105734202368b48db80e7ed82a | quote: Free hostnames require confirmation every 30 days to remain active in your account.
  - [2] 2026-11-03: an unconfirmed hostname is deleted after the Redemption period and anyone can claim it | capture: sha256:e5404f7962279e4a7449a46276e2cc110f9c88105734202368b48db80e7ed82a | quote: After 14 days the hostname will be deleted and be available for you or anyone else to claim.
  - [11] 2026-11-03: No-IP.com's suffixes (no-ip.info, no-ip.org and others) are entries of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // No-IP.com : https://noip.com/
  - [12] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://www.noip.com/free
  - [2] https://www.noip.com/support/knowledgebase/confirm-my-hostname-free-account-support-question-day
  - [3] https://www.noip.com/support/knowledgebase/i-installed-your-update-client-but-my-hostnames-are-not-being-kept-up-to-date-with-my-current-ip-address
  - [4] https://www.noip.com/faqs
  - [5] https://www.noip.com/integrate/request
  - [6] https://www.noip.com/integrate/response
  - [7] https://www.noip.com/sign-up
  - [8] https://www.noip.com/pricing
  - [9] https://www.noip.com/remote-access
  - [10] https://www.noip.com/support/knowledgebase/how-many-hostnames-can-i-have
  - [11] https://publicsuffix.org/list/public_suffix_list.dat
  - [12] https://letsencrypt.org/docs/rate-limits/
