# Kevin Service Registry

> kevsrv.me | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kevsrv/ | JSON https://fshy.ajam.dev/api/v1/entity/kevsrv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kevin Service Registry

- `domains-dns/kevin-service-registry` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://docs.kevsrv.me/guides/getting-started
- free tier: free subdomains under 5 public domains including ae.kg, delegated by NS records to the user's own DNS provider; invite-based registration, a maximum of 3 domains per user | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: a maximum of 3 domains per user in total: at most 1 under ae.kg and 2 others, or 3 other than ae.kg
- retention: no expiry or renewal term is stated on the pages read; the introduction says there are free renewals and that availability is not guaranteed | source: [2]
- egress: no query cap published; the registry holds only the delegation | metered: no | source: [2]
- identity: email | detail: an invite code and an account through a login method the page does not name; a written reason of at least 50 words for each domain; the login methods are unverified because the sign-in page was not read
- interface: unknown
- limits:
  - write-gated (binding): registration is limited by an invite code, and a new domain needs approval by registry staff after a written reason of at least 50 words [1]
  - per-object-cap: a maximum of 3 domains per user in total, at most 1 of them under ae.kg [1]
- binding note: the zone is the registrant's through delegation
- interface detail: a web dashboard at registry.kevsrv.me; the registration form asks for the nameservers of the user's DNS provider, and the registry offers NS management only; no API was read
- tooling: the registry dashboard, then a DNS provider of the user's choice that can host the zone
- composes with: the delegation can point at an external DNS provider such as Hurricane Electric or deSEC or ClouDNS, which makes the name a zone of the registrant's; ae.kg is on the Public Suffix List, so each name has its own TLS limit
- reliability: a domain may be suspended without prior notice, registration is invite-only, and the operator states one account per person
- notes: The gate is an invite code plus staff approval, and the operator can suspend a name without notice. The zone is the registrant's through NS delegation. The TLS limit does not bind for ae.kg, because it is listed; the other 4 suffixes were not checked against the list.
- evidence note: the introduction and the get-started guide were read and quoted; the sign-in page, the terms and the management guide were not read; the ae.kg listing is an entry of the captured Public Suffix List, and the TLS statement is an inference from it and the Let's Encrypt registered-domain rule
- evidence:
  - [1] 2026-11-03: registration is limited by an invite system | capture: sha256:e97c1f849781131a69a5d163aaf6f8f214301d523b18f5c4049784e24759c637 | quote: Registrations are limited through an invite system to control abuse and platform load.
  - [1] 2026-11-03: 5 domains are offered for registration | capture: sha256:e97c1f849781131a69a5d163aaf6f8f214301d523b18f5c4049784e24759c637 | quote: We currently offer 5 domains you can register under
  - [1] 2026-11-03: each domain needs staff approval | capture: sha256:e97c1f849781131a69a5d163aaf6f8f214301d523b18f5c4049784e24759c637 | quote: Wait for one of our Kevin Service Registry staff to approve your domain.
  - [1] 2026-11-03: the reason for a domain must be at least 50 words | capture: sha256:e97c1f849781131a69a5d163aaf6f8f214301d523b18f5c4049784e24759c637 | quote: At least 50 words
  - [2] 2026-11-03: the registry offers nameserver management only, so the user brings a DNS provider | capture: sha256:2d428439f4a94ccca72366990e63ee705c59a653da4c3d39b59c6c4eec24ce02 | quote: Nameserver (NS) management only
  - [2] 2026-11-03: a domain can be suspended without prior notice | capture: sha256:2d428439f4a94ccca72366990e63ee705c59a653da4c3d39b59c6c4eec24ce02 | quote: may be suspended without prior notice
  - [2] 2026-11-03: one account per person | capture: sha256:2d428439f4a94ccca72366990e63ee705c59a653da4c3d39b59c6c4eec24ce02 | quote: strict one-person-one-account policy
  - [3] 2026-11-03: Kevin Service's suffix ae.kg is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // Kevin Service : https://kevsrv.me
  - [4] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://docs.kevsrv.me/guides/getting-started/get-started.md
  - [2] https://docs.kevsrv.me/guides/getting-started
  - [3] https://publicsuffix.org/list/public_suffix_list.dat
  - [4] https://letsencrypt.org/docs/rate-limits/
