# seeding.io

> seeding.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seeding/ | JSON https://fshy.ajam.dev/api/v1/entity/seeding.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## seeding.io

- `debrid/seeding-io` | dead | evidence measured | binding none | category former seedbox host (domain parked) | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://seeding.io/
- free tier: none: the domain no longer serves a seedbox service. seeding.io is a CNAME to park.io and an HTTP request redirects to whoisbroker.com. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no service | source: [1]
- retention: not applicable: no service | source: [1]
- egress: no service to assess; the host serves a domain-sale page | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: not applicable; nothing can be registered | country: None
- interface: unknown
- binding note: no constraint applies to a domain that serves no service
- interface detail: no interface: the domain is parked
- tooling: part of the free tier
- composes with: removed from the candidate set; a parked domain cannot hold bytes or serve a retrieval path
- reliability: parked domain: HTTPS presents a certificate for a different principal name, and HTTP 302-redirects to whoisbroker.com
- notes: Documented as dead rather than omitted so the subsequent audit does not spend a pass on it. If the domain is bought by a new operator, the record must be rechecked rather than trusted; a parked name proves nothing about a future service.
- evidence note: Measured by probe on 2026-10-23: DNS over HTTPS returned 'seeding.io CNAME park.io' and A 184.196.180.154; curl followed http://seeding.io/ to https://whoisbroker.com/ with 200; https://seeding.io/ failed TLS with SEC_E_WRONG_PRINCIPAL. The instrument was curl and Cloudflare DoH, not probe.
- extras:
  - death_evidence: CNAME park.io + redirect to whoisbroker.com
  - probe_commands: DoH: curl 'https://cloudflare-dns.com/dns-query?name=seeding.io&type=A' -H 'accept: application/dns-json'; HTTP: curl -sSL -o /dev/null -w '%{url_effective} %{http_code}' http://seeding.io/
- evidence:
  - probe:https://seeding.io 2026-10-23: DNS answer 'seeding.io. 60 IN CNAME park.io.'; HTTP 302 to https://whoisbroker.com/; TLS certificate name mismatch on the apex
- sources:
  - [1] https://seeding.io/
