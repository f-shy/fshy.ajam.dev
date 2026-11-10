# YDNS

> ydns.io | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ydns/ | JSON https://fshy.ajam.dev/api/v1/entity/ydns.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## YDNS

- `domains-dns/ydns` | qualifies-with-caveat | evidence documented | binding none | category free dynamic subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://ydns.io/
- free tier: unlimited hosts per user on a fair-use model, as dynamic DNS names such as example.ydns.io, plus full DNS hosting for the user's own domains | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: no number is published: unlimited hosts per user under a fair-use model, whose limit is not stated
- retention: unverified: no expiry, inactivity or confirmation rule for a free host is stated on the pages read; the introduction says the service is guaranteed to be free for its entire lifetime | source: [2]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: no phone and no card field on the register page
- interface: rest
- limits:
  - per-object-cap: unlimited hosts per user on a fair-use model; the fair-use limit is not stated [1]
- binding note: no count, expiry or review is published; the fair-use model is the one unstated bound; the zone is the vendor's
- interface detail: a lightweight API that works with most DynDNS implementations; DNSSEC is not available for all zones
- tooling: any DynDNS-compatible client or router, or curl against the vendor's API
- composes with: a free name for a changing address; the vendor also hosts the DNS of the user's own domain for free, which is the way to a zone the user controls
- reliability: the fair-use limit behind 'unlimited' is not stated, and the introduction promises a free service for its entire lifetime; the suffix was not found in the captured Public Suffix List, which is an inference from absence, so a TLS limit may be shared across users of the suffix
- notes: Nothing published binds except an unstated fair-use bound. The zone is the vendor's for ydns.io names; hosting the user's own domain there is the free route to an own zone. The TLS limit is unverified: the suffix has no entry in the captured Public Suffix List, so the Let's Encrypt count for the suffix is shared by inference.
- evidence note: the features page, the introduction and the register page were read and quoted; no fair-use figure, expiry rule or suffix list was read; the Public Suffix List statement is an inference from the absence of an entry and cannot be quoted
- evidence:
  - [1] 2026-11-03: unlimited hosts per user | capture: sha256:d73388a6914bc0e20adf5aa609a156ad7229038478800d5f08a4e35ff0d1c566 | quote: Unlimited hosts1 per user
  - [1] 2026-11-03: the unlimited figure rests on a fair-use model | capture: sha256:d73388a6914bc0e20adf5aa609a156ad7229038478800d5f08a4e35ff0d1c566 | quote: based on fair-use model
  - [1] 2026-11-03: full DNS hosting of the user's own domains is part of the service | capture: sha256:d73388a6914bc0e20adf5aa609a156ad7229038478800d5f08a4e35ff0d1c566 | quote: Full DNS hosting for your own domains
  - [2] 2026-11-03: the vendor promises the service stays free for its lifetime | capture: sha256:747f4bffaf040509c8b9c2233d32237be7b724a0fa3488f89093a0368a6833c9 | quote: The service is guaranteed to be free for its entire lifetime. Without exceptions.
  - [3] 2026-11-03: an account needs only an email address | capture: sha256:64cf3cfd413f6894b3966d38560567f3ad7f7cd528edb7494552d676e300ec66 | quote: Create your YDNS account by providing your email address below.
  - [4] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://ydns.io/features
  - [2] https://docs.ydns.io/introduction.html
  - [3] https://ydns.io/user/register
  - [4] https://letsencrypt.org/docs/rate-limits/
