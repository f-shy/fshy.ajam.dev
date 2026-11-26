# Rage4

> rage4.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rage4/ | JSON https://fshy.ajam.dev/api/v1/entity/rage4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rage4

- `domains-dns/rage4` | qualifies-with-caveat | evidence documented | binding none | category managed authoritative DNS, anycast, GeoDNS | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T01:34:15.559Z (live) | stale on 2026-12-20
- url https://rage4.com/
- free tier: Included free of charge for each domain: dual-stack anycast network, DNSSEC and DANE/TLSA, vanity NS, failover support, unlimited records and requests, 60 sec. TTL, REST API access | unit: unlimited | metered on: none | read on: 2026-11-19 | source: [1]
- per-object cap: no per-object or record-size cap is stated on the first-party pages read; the free tier states unlimited records and requests | source: [1] | note: the word unlimited is the vendor's claim, not a measured value
- retention: unverified: the first-party pages read state no retention period or automatic deletion rule for zones or records; DNS records persist until the owner changes them | source: [1] | note: no zone-inactivity or expiry statement was found on the pages read
- egress: the free tier states unlimited DNS requests; paid plans are priced per zone and the pricing page carries no per-query or per-GB line | metered: no | free allowance: unlimited requests | source: [1]
- identity: email | detail: it has no phone, card or identity-document field. The live URL answered HTTP 404 when read on 2026-11-19, so the form was read from a 2026-09-30 Wayback capture of the same first-party page (https://web.archive.org/web/20260930075401/https://rage4.com/secure/register). A card is used only on paid upgrades, where the first-party billing guide names Stripe as the sole payment provider, supporting cards and PayPal.
- interface: rest
- limits:
  - request-rate: unlimited records and requests stated on the free tier [1]
- limits note: the only other numeric value on the free-feature list is a 60-second TTL, which is a DNS caching value and not a storage, retention or request quota
- binding note: the first-party free-feature list states unlimited records and requests, so no documented quota binds at a typical single-domain scale; the 60-second TTL is a design value, not a quota
- interface detail: a REST API is included free of charge for each domain; the API uses HTTP Basic authentication, with the account email address sent as the user and an API key as the password, base64 encoded; the Swagger document is at https://rage4.com/swagger/index.html?urls.primaryName=dns-legacy; API keys are created under Profile/API keys with an optional IP ACL, and the control panel is at rage4.com/dnsmanager. Delegation uses ns1.r4ns.com and ns2.r4ns.net.
- endpoint: part of interface detail
- tooling: curl or any HTTP client against the REST API with HTTP Basic auth (email address as user, API key as password); the web control panel for manual edits
- composes with: an authoritative anycast DNS service with GeoDNS, DNSSEC/DANE, vanity nameservers, failover and a 60-second TTL; it can act as primary with secondary DNS elsewhere, and the vendor sells a separate AnycastIP service for content, not DNS
- reliability: no outage was measured here; the vendor SLA, which excludes service during a trial period and accounts with overdue invoices, states 99.99 percent monthly availability, sub-300 ms responses in 95 percent of cases each month, and a service-plan extension as the only remedy, with claims by email within 120 hours
- notes: The free feature list states unlimited records and requests. Older third-party reviews cite a 250,000-query cap and per-million query overage fees, but no query cap appears on the first-party pages read; those reports are not used for any number here. No public read path was probed, which is the named caveat. The signup form was read from a 2026-09-30 Wayback capture of the first-party page because the live address answered 404 on 2026-11-19.
- evidence note: the pricing and free-feature page, the API and API-key guides, the nameserver guide, the SLA and the billing guide were captured and quoted from first-party pages. The signup form was read from a Wayback capture of the first-party page because the live address answered 404. No live DNS probe was run, so the rung stays documented.
- evidence:
  - [1] 2026-11-19: a free set of DNS features exists for each domain | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Included free of charge for each domain:
  - [1] 2026-11-19: the free tier states no record or request cap | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Unlimited records and requests
  - [1] 2026-11-19: the free tier sets a 60-second TTL | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: 60 sec. TTL
  - [1] 2026-11-19: the REST API is included on the free tier | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: REST API access
  - [1] 2026-11-19: DNSSEC and DANE/TLSA are on the free feature list | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: DNSSEC and DANE/TLSA
  - [1] 2026-11-19: failover is on the free feature list | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Failover support
  - [1] 2026-11-19: the paid Premium plan price | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Premium €5/m or €55/y
  - [1] 2026-11-19: paid plans are priced per zone with no setup fee | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Price per zone. No setup fee.
  - [1] 2026-11-19: the paid Professional plan price | capture: sha256:0fbfa5059ea225505855926d9136dca0d7f9b92aac86825fa7f6600a20b87282 | quote: Professional €50/m or €550/y
  - [2] 2026-11-19: the REST API authenticates by HTTP Basic with email and API key | capture: sha256:914c55f9c5419103b41137cc412ee00619f179e8043814bae206608d74644fd0 | quote: The Rage4 API use BASIC authentication. To receive authorization, the client sends the email address and API key as a password, separated by a single colon (":") character, within a base64 encoded string in the credentials.
  - [3] 2026-11-19: there is no stated cap on API keys | capture: sha256:2cb80999df1a7124ac4a41be38a2ae6d25d849d0dd2af2127905b737473eed57 | quote: Currently, there is no limit to the number of API keys you can create.
  - [3] 2026-11-19: API keys can be restricted by IP ACL | capture: sha256:2cb80999df1a7124ac4a41be38a2ae6d25d849d0dd2af2127905b737473eed57 | quote: API keys support Access Control List (ACL), which allows you to restrict a specific API key to certain IP addresses and subnets.
  - [4] 2026-11-19: the delegation nameservers for Rage4 DNS | capture: sha256:361bb6f68e33b6eff67ddee56867b91dd68be3d24ca0fbd648fb70d5cbbe0139 | quote: ns1.r4ns.com ns2.r4ns.net
  - [5] 2026-11-19: the signup form asks for an email address and a password only | capture: sha256:ced783d4f4d6d56b553047cec6b22e744c8bbfda33f236c291257cb0b84ca217 | quote: Email address ... Password ... Create new account
  - [5] 2026-11-19:  | capture: sha256:ced783d4f4d6d56b553047cec6b22e744c8bbfda33f236c291257cb0b84ca217 | quote: By clicking button below you accept our
  - [6] 2026-11-19: the SLA excludes trial-period service | capture: sha256:2551f3378672f8ab49c0cd5ac8bf90f39013883068c809d7c9d0de7e32d80d34 | quote: The Agreement does not cover services provided during the trial period; service plans that do not have Service Level Agreements; user accounts with overdue invoices and/or a negative payment history.
  - [6] 2026-11-19: the stated monthly availability target | capture: sha256:2551f3378672f8ab49c0cd5ac8bf90f39013883068c809d7c9d0de7e32d80d34 | quote: guaranteeing the availability of its Authoritative DNS servers to users at 99.99% per month
  - [7] 2026-11-19: a card is used only through Stripe for paid plans | capture: sha256:7fd8ded39d34d32d9f4f23b48fe0a1b639e8079937ee1c5adac6c1dd8c588b76 | quote: Stripe is our sole payment provider; it supports multiple currencies and channels, including cards and PayPal.
- sources:
  - [1] https://rage4.com/
  - [2] https://support.rage4.net/helpdesk/KB/View/74085153-developers-api
  - [3] https://support.rage4.net/KB/View/100783042-general-setup-api-keys
  - [4] https://support.rage4.net/KB/View/74004849-how-to-update-my-domain-with-rage4-dns-name-servers-
  - [5] https://web.archive.org/web/20260930075401/https://rage4.com/secure/register
  - [6] https://blog.rage4.com/files/sla.pdf
  - [7] https://support.rage4.net/KB/View/100831943-general-setup-billing-and-subscriptions
