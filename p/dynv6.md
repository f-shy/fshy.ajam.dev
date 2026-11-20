# dynv6

> dynv6.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dynv6/ | JSON https://fshy.ajam.dev/api/v1/entity/dynv6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dynv6

- `domains-dns/dynv6` | qualifies-with-caveat | evidence documented | binding none | category free dynamic subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:05:09.544Z (live) | stale on 2026-12-05
- url https://dynv6.com/
- free tier: a free hostname for dynamic IPv4 and IPv6 addresses, or delegation of the user's own domain to dynv6, free for everyone; no zone or hostname count is published | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: no hostname, zone or record count is published on the pages read
- retention: unverified: no expiry, inactivity or confirmation rule is stated on the pages read | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: the sign-up form has an email, a password of at least 8 characters and a password confirmation; no phone and no card field
- interface: rest
- binding note: no count, expiry or review is published, so no limit binds on the pages read; the stated exposure is that the service has no enterprise DDoS protection and no SLA
- interface detail: five ways to update a zone: a REST API, an update API, a DynDNS-compatible API, SSH with public key authentication, and DNS updates signed with TSIG keys; the DynDNS-style API updates the IPv4 address only; webhooks fire when the address changes
- tooling: curl, nsupdate or any software that speaks RFC 2136 with a TSIG key, a router's DynDNS client, or lego for certificate challenges
- composes with: a free name with a full update API; a zone under the vendor's suffix is not the registrant's, and the user's own domain can instead be delegated to dynv6
- reliability: the vendor says it offers no enterprise-grade DDoS protection and no SLA and asks that it not be used for critical services; the suffix is on the Public Suffix List, so the TLS limit counts per name
- notes: Nothing published binds: no count, expiry or review. The unknowns are the withdrawal rule and the count, and the vendor disclaims an SLA. The zone is the vendor's; delegating the user's own domain is the other offer. The TLS limit does not bind, because dynv6.net is listed.
- evidence note: the home page, the API page and the sign-up form were read and quoted; no count, expiry or suffix list was read; the TLS statement is an inference from the Let's Encrypt registered-domain rule and the Public Suffix List entry
- evidence:
  - [1] 2026-11-03: a free hostname, or delegation of the user's own domain, is free for everyone | capture: sha256:3d0298cc8d0804d419bca31f685117bb0b5467a5fa858ceb9ec6a1359e66d553 | quote: Just choose a free hostname to start, or delegate your own domain to dynv6.
  - [1] 2026-11-03: no enterprise DDoS protection or SLA, and not for critical services | capture: sha256:3d0298cc8d0804d419bca31f685117bb0b5467a5fa858ceb9ec6a1359e66d553 | quote: Please be aware that we don't offer enterprise-grade DDoS protection and SLAs yet. Don't use it for critical services.
  - [1] 2026-11-03: several update interfaces exist (REST, update API, DynDNS, SSH, TSIG DNS updates) | capture: sha256:3d0298cc8d0804d419bca31f685117bb0b5467a5fa858ceb9ec6a1359e66d553 | quote: dynv6 offers many ways to update your zones:
  - [2] 2026-11-03: the sign-up form asks for an email, a password and its confirmation | capture: sha256:c313e4fc79613b28bed0b7489761dd2f4d7a01951e8a2bb7fd3ea3c1d3efbba7 | quote: Email Password at least 8 characters Password confirmation
  - [3] 2026-11-03: dynv6.net is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // dynv6 : https://dynv6.com
  - [4] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
  - [1] 2026-11-04: a free hostname or delegation is offered; the page states no count or quota, so 'unlimited' is not stated | capture: sha256:3d0298cc8d0804d419bca31f685117bb0b5467a5fa858ceb9ec6a1359e66d553 | quote: Just choose a free hostname to start, or delegate your own domain to dynv6.
- sources:
  - [1] https://dynv6.com/
  - [2] https://dynv6.com/users/sign_up
  - [3] https://publicsuffix.org/list/public_suffix_list.dat
  - [4] https://letsencrypt.org/docs/rate-limits/
