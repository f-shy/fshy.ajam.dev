# Gandi

> gandi.net | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gandi/ | JSON https://fshy.ajam.dev/api/v1/entity/gandi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gandi

- `domains-dns/gandi` | paid-only | evidence documented | binding write-gated | category domain registrar with bundled managed authoritative DNS (LiveDNS)
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T00:19:24.696Z (live) | stale on 2026-12-20
- url https://www.gandi.net/en-US/domain/dns
- free tier: Free Anycast LiveDNS hosting and a REST API are included with each domain registered at Gandi; the domain registration itself is paid (USD 11.71 per year for .com, USD 8.00 for .fr) | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: No free-standing DNS tier: the free DNS servers and the API require a paid domain registered at Gandi. A free DNS zone for a domain registered elsewhere is not documented on the pages read. The 'none' unit records the absence of a free-standing offer; a 'bundled-with-paid-domain' unit would name it more exactly.
- per-object cap: no per-object cap is stated on the pages read; the LiveDNS API accepts DNS record sets and its record-type list has no stated size cap | source: [2]
- retention: zones persist while the domain is registered; no automatic expiry of DNS zones is stated on the pages read | source: [1]
- egress: Anycast DNS query traffic is included with the domain and is not metered or priced on the pages read | metered: no | source: [1]
- identity: card | detail: Account creation at id.gandi.net asks an email address, first name, last name, username and password, an affirmation of being older than 18, and acceptance of the terms; no card is asked at account creation, and a confirmation link must be clicked to activate the account. An identity document may be requested if ownership verification proves necessary. The paid domain that unlocks the free DNS and API needs a payment method.
- interface: rest, browser
- limits:
  - write-gated (binding): a paid domain registered at Gandi is required before LiveDNS hosting and the API can be used [1]
  - request-rate: a maximum of 1000 requests per minute from the same IP address [3]
- limits note: DNS record TTL values must be between 300 and 2592000 seconds, as stated in the LiveDNS API reference.
- binding note: The paid domain registration is the gate that fails first, since no free-standing DNS zone is offered; once a domain is held, the 1000 requests per minute per IP rate limit is the next constraint.
- interface detail: A REST API at https://api.gandi.net/v5/ for domains, records, zones and snapshots, plus a browser dashboard; TSIG keys support AXFR zone transfer to BIND, Knot, NSD and PowerDNS
- endpoint: part of interface detail
- tooling: the Gandi LiveDNS v5 REST API with a Personal Access Token in the Authorization header; curl or any HTTPS/JSON client; the browser dashboard
- composes with: Free DNS and a REST API bundled with a paid domain, with DNSSEC, zone snapshots and a domain-ownership verification record endpoint for ACME DNS-01 challenges
- reliability: A read-only probe of the documented unauthenticated generic nameservers route returned HTTP 401, so keyless programmatic DNS read is unverified. The product page states DNS changes propagate in less than 250 ms, while full resolver visibility can take a few hours.
- notes: The free DNS and REST API are bundled with a paid domain, which is why the verdict is paid-only rather than the qualifies given to a free-standing DNS host. A read-only probe of the LiveDNS generic nameservers route returned HTTP 401 even though the API docs call it unauthenticated; the docs may be stale.
- evidence note: All verdict-deciding values come from first-party Gandi pages that were captured and quoted. A read-only probe of the generic nameservers route returned HTTP 401, so no keyless programmatic read was established; that does not raise the rung.
- self hosted: no
- evidence:
  - [1] 2026-11-19: free DNS servers are included with each domain registered at Gandi | capture: sha256:921f9171cd66f4d0abbbc3658e348ae1404b3af27b71cfa0abd8de9e3b55fc13 | quote: Each [domain name](https://www.gandi.net/en-US/domain) registered at Gandi gets access to free DNS servers, linked to our developed technologies and features.
  - [1] 2026-11-19: Gandi states a propagation time below 250 ms for DNS changes | capture: sha256:921f9171cd66f4d0abbbc3658e348ae1404b3af27b71cfa0abd8de9e3b55fc13 | quote: Thanks to LiveDNS, our DNS management service, each modification is propagated in less than 250 ms.
  - [3] 2026-11-19: the API is limited to 1000 requests per minute per source IP | capture: sha256:10a87d2c74b1cb36b878ffea6e83815f5fc71f638f2eef0ab3a535d1848cfacf | quote: Gandi's API is rate limited; you can perform a maximum of 1000 requests per minute from the same IP address.
  - [3] 2026-11-19: the management interface is a REST API over HTTPS | capture: sha256:10a87d2c74b1cb36b878ffea6e83815f5fc71f638f2eef0ab3a535d1848cfacf | quote: Gandi provides remote RESTful APIs over HTTPS, making it easy to manage your products and build third-party applications.
  - [4] 2026-11-19: account creation asks a username, email address and password | capture: sha256:0beb6a2ff88645ebab43753daa414aaf35e185a8c31ffbe53c4ce4ef99a2e9de | quote: When on the creation page, you will have to choose a username, an email address and a password.
  - [4] 2026-11-19: an identity document may be requested for account ownership verification | capture: sha256:0beb6a2ff88645ebab43753daa414aaf35e185a8c31ffbe53c4ce4ef99a2e9de | quote: If it proves necessary to verify the ownership of the account via an identity document, it will be simpler to do so via this data.
  - [5] 2026-11-19: the sign-up form requires an age affirmation and acceptance of the terms | capture: sha256:911b375f8256a1611a5dcbcb5206ec8c602353ec1c952381df8f8f1a2feadcf7
  - [6] 2026-11-19: a .com domain costs USD 11.71 to register and USD 38.38 to renew | capture: sha256:54c3821cd2bc3d510493a6f4b3d7153706787548e4e2ea77fd2c6553556d9bc9 | quote: | [.com](https://www.gandi.net/en-US/domain/tld/com) | $11.71 | $38.38 | $11.71 |
  - [6] 2026-11-19: DNS is free, secure and anycast with DNSSEC when bought with a domain | capture: sha256:54c3821cd2bc3d510493a6f4b3d7153706787548e4e2ea77fd2c6553556d9bc9 | quote: Your domain's DNS (domain name system) is free, secure, and available with DNSSEC, high quality anycast DNS servers
  - [7] 2026-11-19: API calls require a Personal Access Token or API key | capture: sha256:7ca64f9bff030ef0d3598dbda0cc8000dfc41932dd2c5b842dc10de914dc3fb6 | quote: Every request to Gandi's API requires authentication.
  - [2] 2026-11-19: the API docs describe a generic nameservers route as unauthenticated | capture: sha256:095617cb894668383f9f22f40cfd61362e1e581a5764dc35c9e851e2b639b5a2 | quote: This is a generic route for hashing any domain and thus is not authenticated.
  - probe:https://api.gandi.net/v5/livedns/nameservers/example.com 2026-11-19: a read-only probe of the documented unauthenticated generic nameservers route returned HTTP 401, so keyless programmatic read was not established | capture: sha256:f66a9fd680a1ca6f508754cf72459b1b6103aeb980966cdb3918133c35b08a6c | quote: "status": 401
- sources:
  - [1] https://www.gandi.net/en-US/domain/dns
  - [2] https://api.gandi.net/docs/livedns/
  - [3] https://api.gandi.net/docs/reference
  - [4] https://docs.gandi.net/en/account_management/activate_account/account_creation.html
  - [5] https://id.gandi.net/en/login
  - [6] https://www.gandi.net/en-US/domain
  - [7] https://api.gandi.net/docs/authentication
