# isroot

> isroot.in | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/isroot/ | JSON https://fshy.ajam.dev/api/v1/entity/isroot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## isroot

- `domains-dns/isroot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category free registrable subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://docs.isroot.in/
- free tier: a free <name>.isroot.in subdomain registered in a dashboard after a GitHub sign-in, 1 subdomain by default and up to 5 total after starring a repository; each registration lasts 365 days | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: 1 subdomain on a default account and up to 5 in total when GitHub star verified; one registration per hour
- retention: a registration lasts 365 days; renewal opens 60 days before expiry and adds 365 days; an expired registration can still be renewed during a 7-day grace period | days: 365 | source: [2]
- egress: no query cap published | metered: no | source: [3]
- identity: email | detail: a GitHub account, through the only sign-in the application supports, and a CAPTCHA on sign-up and on each registration; no phone and no card are named in the guide
- interface: unknown
- limits:
  - per-object-cap (binding): 1 subdomain on a default account, up to 5 in total after GitHub star verification [1]
  - retention-clamped: a registration lasts 365 days and must be renewed in the final 60 days, with a 7-day grace period after expiry [2]
  - request-rate: after a successful registration the user waits one hour before creating another subdomain [1]
- binding note: the allowance of 1 subdomain, or 5 after a star, binds first; the 365-day renewal is the clock; the zone is delegable but the suffix is not on the Public Suffix List, so providers and the Let's Encrypt count treat all isroot names as one site
- interface detail: a web dashboard for registration, DNS records, nameservers, renewal and deletion; no API was read
- tooling: the isroot dashboard, then a host that takes a DNS record
- composes with: the dashboard has an Edit Nameservers action, so the name can be delegated to an external DNS provider that accepts the exact zone; isroot.in is not on the Public Suffix List, so some providers refuse the zone and the TLS limit is shared with every other isroot subdomain
- reliability: a name expires after 365 days unless renewed; the suffix is not on the Public Suffix List, so some DNS providers or hosts may refuse the zone and sibling registrations share a site boundary
- notes: Binds: 1 subdomain (5 with a star) and a 365-day renewal, with a 7-day grace period. The zone is delegable, but the suffix is not listed, so some DNS providers refuse the zone, and every isroot name draws on one Let's Encrypt count of 50 certificates in 7 days for isroot.in. The listing status is stated by the vendor's guide; the shared count is an inference.
- evidence note: the getting-started, limits, manage-domains and provider-compatibility pages were read and quoted; the terms and the dashboard were not read; the shared TLS count is an inference from the vendor's Public Suffix List status and the Let's Encrypt registered-domain rule
- evidence:
  - [4] 2026-11-03: sign-up is through GitHub authorization | capture: sha256:70ee0f02046aec3060074b212e464e80543afbe45f25254bd2d641883607c1f8 | quote: Choose Signup with GitHub and complete the GitHub authorization flow.
  - [4] 2026-11-03: GitHub is the only supported sign-in | capture: sha256:70ee0f02046aec3060074b212e464e80543afbe45f25254bd2d641883607c1f8 | quote: GitHub is the sign-in method supported by the current application.
  - [4] 2026-11-03: sign-up carries a CAPTCHA | capture: sha256:70ee0f02046aec3060074b212e464e80543afbe45f25254bd2d641883607c1f8 | quote: Enter your name if prompted and complete the CAPTCHA.
  - [1] 2026-11-03: a default account has 1 subdomain | capture: sha256:5a3ec62741509d4ecd7312f346e2aff1f5e15cd7f387560c63408d0a3666610a | quote: | Default account | 1 |
  - [1] 2026-11-03: a GitHub star raises the allowance to 5 in total | capture: sha256:5a3ec62741509d4ecd7312f346e2aff1f5e15cd7f387560c63408d0a3666610a | quote: | GitHub star verified | Up to 5 total |
  - [1] 2026-11-03: registrations are spaced one hour apart | capture: sha256:5a3ec62741509d4ecd7312f346e2aff1f5e15cd7f387560c63408d0a3666610a | quote: After a successful registration, wait one hour before creating another subdomain.
  - [1] 2026-11-03: a registration lasts 365 days and renewal opens 60 days before expiry | capture: sha256:5a3ec62741509d4ecd7312f346e2aff1f5e15cd7f387560c63408d0a3666610a | quote: Registrations last 365 days. Renewal opens 60 days before expiry.
  - [2] 2026-11-03: renewal adds 365 days | capture: sha256:f0c550a6649bd89f222499defbe5294294e5ee4132c3276a2f3ebcc5d7bef78f | quote: Renewal becomes available during the final 60 days before expiry. A successful renewal adds 365 days to the previous expiry date.
  - [5] 2026-11-03: the operator states the suffix is not on the Public Suffix List | capture: sha256:e7152e5100830dfab311e6d796dd8b5eb9fff26a5809fd556e43a6062366fc62 | quote: As checked on October 29, 2026, `isroot.in` is not listed in the [Public Suffix List]
  - [5] 2026-11-03: an external DNS provider must accept the exact delegated zone without parent ownership | capture: sha256:e7152e5100830dfab311e6d796dd8b5eb9fff26a5809fd556e43a6062366fc62 | quote: For an external provider, first confirm that it can create the exact zone `myproject.isroot.in`, without requiring ownership of `isroot.in`.
  - [6] 2026-11-03: Let's Encrypt counts 50 certificates per registered domain in 7 days, and finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: Up to 50 certificates can be issued per registered domain (or IPv4 address, or IPv6 /64 range) every 7 days.
- sources:
  - [1] https://docs.isroot.in/limits
  - [2] https://docs.isroot.in/manage-domains
  - [3] https://docs.isroot.in/
  - [4] https://docs.isroot.in/getting-started
  - [5] https://docs.isroot.in/provider-compatibility
  - [6] https://letsencrypt.org/docs/rate-limits/
