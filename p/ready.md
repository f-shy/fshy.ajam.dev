# Ready

> ready.bd | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ready/ | JSON https://fshy.ajam.dev/api/v1/entity/ready.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ready (ready.bd)

- `domains-dns/ready-bd` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T01:33:35.379Z (live) | stale on 2026-12-05
- url https://ready.bd/
- free tier: a free name under .pro.bd, .ami.bd, .iam.bd and other .bd and Bengali suffixes, with A, CNAME, TXT and MX records, a REST API and free SSL/TLS certificates; no credit card | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the page read gives no count of domains per user
- retention: a domain left unused after being claimed, or inactive for 30 days, may be reclaimed; a domain is kept free for as long as it is used | days: 30 | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: an account: the sign-up form asks Full Name, Phone Number, Email and Password, or sign-up with Google, Facebook or GitHub; a 'Verify Identity' step of about 1 minute follows, and its method (email code, phone code, ID document) is unverified: behind a sign-up; no credit card is required
- interface: rest
- limits:
  - write-gated (binding): new domains are reviewed by the operator before the user can manage DNS records, configure nameservers or claim offers [1]
  - retention-clamped: a domain left unused after being claimed, or inactive for 30 days, may be reclaimed [1]
- binding note: a review sits before any DNS control and the operator can reclaim an inactive name after 30 days; the zone is the operator's unless the suffix supports delegation
- interface detail: a dashboard for A, CNAME, TXT and MX records, and a REST API for automation whose reference was not read; where a suffix supports delegation, the domain can point at the user's own nameservers
- tooling: the ready.bd dashboard and its REST API
- composes with: a name with its own records and a REST API; delegation to the user's own nameservers is offered only where the suffix supports it, and the suffixes were not found in the captured Public Suffix List, so each suffix shares one Let's Encrypt count across its users
- reliability: an inactive name may be reclaimed after 30 days and a new name waits for review; the suffixes are not on the Public Suffix List, which is an inference from absence
- notes: Binds: a review before any DNS control and a 30-day inactivity reclaim, so the operator can withdraw the name. The zone is the operator's unless the suffix supports delegation. The TLS limit is a risk: the .bd suffixes have no entry in the captured Public Suffix List, so each suffix is one registered domain for Let's Encrypt, an inference from absence.
- evidence note: the landing page and its FAQ were read and quoted; the verification method, the per-user count and the API were not read; the Public Suffix List statement is an inference from the absence of an entry and cannot be quoted
- evidence:
  - [1] 2026-11-03: the service is free | capture: sha256:dfb250c9c00c908a704408d0bf4e0671bdb89604e0278cb667724097ad399759 | quote: Yes, 100% free.
  - [1] 2026-11-03: a new domain is reviewed before any DNS control | capture: sha256:dfb250c9c00c908a704408d0bf4e0671bdb89604e0278cb667724097ad399759 | quote: Yes. New domains go under review by our team before you can manage DNS records, configure nameservers, or claim offers.
  - [1] 2026-11-03: an unused or 30-day inactive domain may be reclaimed | capture: sha256:dfb250c9c00c908a704408d0bf4e0671bdb89604e0278cb667724097ad399759 | quote: We may reclaim domains that are left unused after being claimed, that stay inactive for 30 days, or that violate our terms.
  - [1] 2026-11-03: A, CNAME, TXT and MX records are managed in the dashboard and delegation is offered where the suffix supports it | capture: sha256:dfb250c9c00c908a704408d0bf4e0671bdb89604e0278cb667724097ad399759 | quote: You can manage A, CNAME, TXT, and MX records from your dashboard. Where the suffix supports delegation, you can also point your domain at your own nameservers.
  - [1] 2026-11-03: registration has a verification step whose method is not named | capture: sha256:dfb250c9c00c908a704408d0bf4e0671bdb89604e0278cb667724097ad399759
  - [2] 2026-11-03: Let's Encrypt counts 50 certificates per registered domain in 7 days, and finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: Up to 50 certificates can be issued per registered domain (or IPv4 address, or IPv6 /64 range) every 7 days.
  - [3] 2026-11-04: the sign-up form has a Phone Number field beside Full Name, Email and Password, with Google, Facebook and GitHub sign-up | capture: sha256:98e642827a8fd5162683dd6fbc57fd15939f07f366a6767dfa74c08cea8c1b0a | quote: Phone Number
- sources:
  - [1] https://ready.bd/
  - [2] https://letsencrypt.org/docs/rate-limits/
  - [3] https://ready.bd/register
