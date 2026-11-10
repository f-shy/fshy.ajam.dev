# Dynu

> dynu.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dynu/ | JSON https://fshy.ajam.dev/api/v1/entity/dynu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dynu

- `domains-dns/dynu-free` | qualifies-with-caveat | evidence documented | binding per-object-cap | category free dynamic DNS and managed DNS | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:07.606Z (live) | stale on 2026-12-04
- url https://www.dynu.com/en-US/DynamicDNS
- free tier: 4 hostnames free (third-level names under Dynu domains, or your own domain), no expiry for an unused free account, REST API free for all users | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: 4 hostnames and up to 4 subdomains on the free plan per the FAQ; the membership page says members can have more than 3 third level domain names and 200 custom records, and no page read gives a free custom-record count (unverified) | source: [1]
- retention: Dynu accounts never expire; a free dynamic DNS service stays fully functional until the user deletes it | source: [2]
- egress: no DNS query cap published on the pages read | metered: no | source: [2]
- identity: email | detail: the sign-up form asks for a first name, a last name, a username, a password and an e-mail address entered twice, or a sign-up with GitHub or Google; no phone or card field in the captured form text (https://www.dynu.com/en-US/ControlPanel/CreateAccount)
- interface: rest
- limits:
  - per-object-cap (binding): 4 hostnames and 4 subdomains free; the membership page's own figure is more than 3 third level domain names for members [1]
  - per-object-cap (binding): up to 20 hostnames in one update request (numhost above 20) [3]
  - write-gated: several record types are member-only, among them CAA on a third-level Dynu name and on the user's own domain; A, AAAA, CNAME, MX, SRV, TXT and PTR are free [1]
- binding note: the hostname cap of 4 decides for a free account; the record-type gate matters only for CAA-class records
- interface detail: three update paths: a dyndns2-style HTTP update, GET https://api.dynu.com/nic/update?hostname=HOST&myip=IP&myipv6=IPV6&password=PASSWORD (the password may be sent as is or as an MD5 or SHA256 hash, and a separate IP update password can be set), up to 20 hostnames per request; HTTP and TCP GnuDIP at gnudip.dynu.com; and a REST API at https://api.dynu.com/v2/ with an API-Key header that manages hostnames and DNS records
- tooling: the free Dynu IP update clients for Windows, macOS and Linux, ddclient with protocol dyndns2, routers with a Dynu or Custom provider, GnuDIP clients, and curl against the REST API
- composes with: a free name that can also carry MX, TXT, SRV and CNAME records and a wildcard, on a Dynu domain or on a domain the user already owns that is served by Dynu name servers
- reliability: a failed update authentication returns HTTP 200 with the body badauth, so a status-only check reports success on a failed update; an unknown domain name can also return badauth
- notes: Confirmation interval: none; the dynamic DNS page states that accounts never expire. The free hostname count is 4 in the FAQ and the membership page implies 3, so the figure needs a re-read.
- evidence note: the dynamic DNS page, the FAQ, the membership page, the REST API page and the IP update protocol page were read and quoted; the update endpoint was probed once with a wrong password and answered 200 badauth. The free hostname count is 4 in the FAQ and implied as 3 by the membership page, so the figure is unreconciled
- evidence:
  - [1] 2026-11-03: the free plan allows 4 hostnames | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: You can have 4 hostnames for free
  - [1] 2026-11-03: the free plan allows up to 4 subdomains | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: You are allowed to have up to 4 subdomains for free.
  - [4] 2026-11-03: the membership page gives its own figures for members: more than 3 third level domain names and 200 custom records | capture: sha256:ca6c8b1db08b5203acd1ae07191316791e6c275fa763ec590585a784d4fba8bc | quote: members can have more than 3 third level domain names, 200 custom records
  - [1] 2026-11-03: A records are free on both a Dynu third-level name and an own domain | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: | A - IPv4 | Supported | Supported | Free |
  - [1] 2026-11-03: TXT records are free on both a Dynu third-level name and an own domain | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: | TXT - Text | Supported | Supported | Free |
  - [1] 2026-11-03: CAA is a member-only record type | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: | CAA - Certification Authority Authorization | Supported | Supported | [Member-Only](https://www.dynu.com/Membership) |
  - [2] 2026-11-03: accounts never expire, free users included, and the service works until deleted | capture: sha256:3caea35bfd1d76c719e8d05a09576547600918adb9a11f41fadf435260625330 | quote: Dynu accounts never expire! Even if you are a free user, your dynamic DNS service will remain fully functional until you delete it.
  - [2] 2026-11-03: the service works with a top level domain name the user already owns | capture: sha256:3caea35bfd1d76c719e8d05a09576547600918adb9a11f41fadf435260625330 | quote: Our Dynamic DNS service works with all top level domain names regardless of country of origin.
  - [5] 2026-11-03: the advanced REST API is free for all users | capture: sha256:371b0571443d1afc82ec89ac63c7cddc98f84e64150082b8dbb234a2b2055a73 | quote: Advanced API is free for all users.
  - [5] 2026-11-03: the REST API manages hostnames and DNS records | capture: sha256:371b0571443d1afc82ec89ac63c7cddc98f84e64150082b8dbb234a2b2055a73 | quote: Our fully-featured REST API gives you access to manage hostnames, DNS records and more without having to access the control panel.
  - [3] 2026-11-03: the HTTPS update URL on api.dynu.com with hostname, myip, myipv6 and password | capture: sha256:a3a8ea8b32c085023144818f7ff1a17f08083cbdd9fa16bd27310fc2501f435a | quote: https://api.dynu.com/nic/update?hostname=[HOSTNAME]&myip=[IP ADDRESS]&myipv6=[IPv6 ADDRESS]&password=
  - [3] 2026-11-03: an update with more than 20 hostnames returns numhost | capture: sha256:a3a8ea8b32c085023144818f7ff1a17f08083cbdd9fa16bd27310fc2501f435a | quote: numhost This response code is returned in cases where too many hostnames(more than 20) are specified for the update process.
  - [3] 2026-11-03: badauth is the response code for a failed authentication of the request | capture: sha256:a3a8ea8b32c085023144818f7ff1a17f08083cbdd9fa16bd27310fc2501f435a | quote: badauth This response code is returned in case of a failed authentication for the 'request'.
  - [3] 2026-11-03: an unknown domain name sent as a parameter can also return badauth | capture: sha256:a3a8ea8b32c085023144818f7ff1a17f08083cbdd9fa16bd27310fc2501f435a | quote: Please note that sending across an invalid parameter such as an unknown domain name can also result in this 'response code'.
  - [1] 2026-11-03: MX records are free on both a Dynu third-level name and an own domain | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: | MX - Mail Exchange | Supported | Supported | Free |
  - [1] 2026-11-03: wildcard DNS records are supported on Dynu third-level names and customer-owned domains | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: Yes, wildcard DNS records are supported.
  - [3] 2026-11-03: GnuDIP over TCP and HTTP is supported | capture: sha256:a3a8ea8b32c085023144818f7ff1a17f08083cbdd9fa16bd27310fc2501f435a | quote: Both TCP and HTTP based GnuDIP is fully supported.
  - [6] 2026-11-03: the sign-up form asks for the e-mail address twice | capture: sha256:7e52a7067eca40a055b06d85d8021ac2417db1b7991214b6216e4b2b7c905745 | quote: Confirm Email Address
  - [6] 2026-11-03: the sign-up form offers a sign-up through Google | capture: sha256:7e52a7067eca40a055b06d85d8021ac2417db1b7991214b6216e4b2b7c905745 | quote: Sign up with Google
  - probe:https://api.dynu.com/nic/update 2026-11-03: the update endpoint is live and answers HTTP 200 to a request with a wrong password | capture: sha256:344c15fe3afee2fc117d0336227e933730f30fac98593453f177a0cf3a641b77 | quote: "status": 200
  - probe:body-dynu 2026-11-03: the body of that failed update is the text code badauth, under HTTP 200 | capture: sha256:b4c8d643f204c090b4e1ddc5b9f8f0bf35d031651ad9e64eca94f12ecb6c5a0d | quote: badauth
  - [1] 2026-11-03: 4 hostnames free, up to 500 for a member | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: You can have 4 hostnames for free or you can become a member to have up to 500 hostnames.
  - [1] 2026-11-03: up to 4 subdomains are free | capture: sha256:55b6133465be90d0bdd7128ee31bc6342f7f0632cdc582e793b51cb7e62d8b7c | quote: You are allowed to have up to 4 subdomains for free.
  - [7] 2026-11-03: the membership page counts a different number of third level domain names for members | capture: sha256:ca6c8b1db08b5203acd1ae07191316791e6c275fa763ec590585a784d4fba8bc | quote: members can have more than 3 third level domain names
  - [8] 2026-11-03: the dynamic DNS service is free | capture: sha256:04a7eb9706d978b5f2d5e77bc324ea22a19c8c71b14529a0676b2ed170080831 | quote: 100% free
  - [8] 2026-11-03: a free account comes with a free third level domain name or the user's own domain | capture: sha256:04a7eb9706d978b5f2d5e77bc324ea22a19c8c71b14529a0676b2ed170080831 | quote: Create a free account
  - [9] 2026-11-03: Dynu's suffixes (dynu.net, dynuddns.net) are entries of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // Dynu.com : https://www.dynu.com/
  - [10] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://www.dynu.com/FAQ/Dynamic-DNS-Service
  - [2] https://www.dynu.com/en-US/DynamicDNS
  - [3] https://www.dynu.com/en-US/DynamicDNS/IP-Update-Protocol
  - [4] https://www.dynu.com/en-US/Membership
  - [5] https://www.dynu.com/en-US/Resources/API
  - [6] https://www.dynu.com/en-US/ControlPanel/CreateAccount
  - [7] https://www.dynu.com/Membership
  - [8] https://www.dynu.com/
  - [9] https://publicsuffix.org/list/public_suffix_list.dat
  - [10] https://letsencrypt.org/docs/rate-limits/
