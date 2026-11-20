# Let's Encrypt

> letsencrypt.org | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/letsencrypt/ | JSON https://fshy.ajam.dev/api/v1/entity/letsencrypt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Let's Encrypt

- `domains-dns/lets-encrypt` | qualifies | evidence measured | binding request-rate | category certificate authority
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2027-01-21
- url https://letsencrypt.org/docs/rate-limits/
- free tier: free 90-day certificates including wildcards over DNS-01, with automated issuance and renewal | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: no certificate size cap; the binding limits are rate limits and not object caps
- retention: a certificate is valid 90 days and must be renewed; ARI lets a client renew early | days: 90 | source: [1]
- egress: no charge | metered: no | source: [2]
- identity: anonymous | detail: no account is required to obtain a certificate; an ACME account key is generated locally and is not a registration
- interface: rest
- limits:
  - request-rate (binding): 50 certificates per registered domain per 7 days, global across all accounts, refilling at 1 per 202 minutes [2]
  - request-rate (binding): 5 certificates per exact set of identifiers per 7 days [2]
  - request-rate (binding): 300 new orders per account per 3 hours [2]
  - request-rate (binding): 10 new accounts per IP per 3 hours [2]
  - request-rate (binding): 5 failed authorizations per identifier per account per hour; 1,152 consecutive failures then the identifier pauses [2]
  - retention-clamped: a certificate is valid 90 days; the requesting client performs the renewal and no automatic extension exists [1]
- interface detail: the ACME v2 protocol at acme-v02.api.letsencrypt.org, with a staging endpoint for testing
- tooling: certbot, acme.sh, lego, Caddy, Traefik, any ACME client
- composes with: free TLS on any name you control, including a wildcard, which is what makes the free-DNS plus free-tunnel chain terminate in a valid certificate
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: The per-registered-domain limit is the one that binds a multi-tenant scheme: 50 certificates a week for every name under one registered domain, whoever requests them. The exact-identifier limit is the one that binds a retry loop, and 5 an hour is reachable in a bad afternoon.
- evidence note: the production and staging directories were fetched and answered 200 with the profile list; the rate limits are a first-party page. The 90-day validity is on the FAQ page, not on the rate-limits page it was attributed to.
- evidence:
  - probe:https://acme-v02.api.letsencrypt.org/directory 2026-10-22: 200, 961 bytes, sha256 ee1bfe324dcd5aff6e67ba25ea98397494d5b6ebf6c7f16e98348254636190e0, listing keyChange, the classic, shortlived and tlsserver profiles, and the current subscriber agreement URL
  - probe:https://acme-staging-v02.api.letsencrypt.org/directory 2026-10-22: 200, 1,035 bytes; the staging endpoint is live, so an issuance test costs nothing against the production limits
  - [2] 2026-10-22: 50 certificates per registered domain per 7 days; 5 per exact set of identifiers per 7 days; 300 new orders per account per 3 hours; 10 accounts per IP per 3 hours; 5 failed authorizations per identifier per hour; 1,152 consecutive failures; ARI renewals are exempt from the order and per-domain limits
  - [1] 2026-10-22: 'Our default certificates are valid for 90 days'; the same FAQ points at the published rationale
- sources:
  - [1] https://letsencrypt.org/docs/faq/
  - [2] https://letsencrypt.org/docs/rate-limits/
