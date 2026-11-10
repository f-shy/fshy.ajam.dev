# Namecheap FreeDNS

> namecheap.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/namecheap/ | JSON https://fshy.ajam.dev/api/v1/entity/namecheap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Namecheap FreeDNS

- `domains-dns/namecheap-freedns` | qualifies | evidence reported | binding write-gated | category managed authoritative DNS
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2026-11-06
- url https://www.namecheap.com/domains/freedns/
- free tier: free DNS hosting for domains registered elsewhere, with dynamic DNS | unit: unlimited | metered on: object-count | read on: 2026-10-22 | source: [1]
- per-object cap: no record count is published on Namecheap's own page; comparison sites state about 150 host records, which is a third-party figure | source: [1] | note: the record is reported on this field, and the 150 comes from comparison sites rather than from the page named here; the page named here is the one that is silent
- retention: the zone persists while it is configured; verification of nameserver changes takes up to 16 hours and the registrar gives 10 days to make the change | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: email signup; the domain must be registered elsewhere
- interface: rest
- limits:
  - per-object-cap: no published record count; comparison sites state about 150 host records, which is reported and not documented [1]
  - write-gated (binding): third-party domains only, and nameserver verification takes up to 16 hours [1]
- interface detail: a web panel; an API exists for registered domains and is not documented for FreeDNS
- tooling: the web panel; dynamic DNS by URL
- composes with: a backup DNS for a domain whose primary is elsewhere, which is the use Namecheap itself names
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: The 150-record figure cannot be promoted to documented until a zone is created and counted, and creating one needs a domain registered elsewhere.
- evidence note: Namecheap's page proves the service and the third-party-domain rule but not the record count, which is a comparison-page figure. A record count from a comparison page is not a quota.
- evidence:
  - [1] 2026-10-22: 'Free 3rd-party domains support only'; nameserver verification within 16 hours; 10 days to change nameservers at the current registrar. No record count is stated
- sources:
  - [1] https://www.namecheap.com/domains/freedns/
