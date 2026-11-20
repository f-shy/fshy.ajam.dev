# EpikHost

> epikhost.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/epikhost/ | JSON https://fshy.ajam.dev/api/v1/entity/epikhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EpikHost

- `debrid/epikhost` | dead | evidence measured | binding none | category former host (zone has no reachable authority) | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://epikhost.com/
- free tier: none: epikhost.com does not answer. DNS over HTTPS returns SERVFAIL with 'No Reachable Authority at delegation epikhost.com' and the delegated server 87.117.238.51 refusing the query. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no service | source: [1]
- retention: not applicable: no service | source: [1]
- egress: no service to assess | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: not applicable; nothing can be registered | country: None
- interface: unknown
- binding note: no constraint applies to an unresolvable zone
- interface detail: no interface: the zone is not answering
- tooling: part of the free tier
- composes with: removed from the candidate set; a zone with no reachable authority serves no bytes
- reliability: SERVFAIL at delegation: the registry points at nameservers that refuse queries, which is a worse state than NXDOMAIN because the name still appears delegated
- notes: The name appears in seedbox briefs but resolves to nothing. epikhost.org is a live but unrelated hosting company with a different name and no seedbox plans; treating them as one provider would be a false match. Re-probe before reuse.
- evidence note: Measured by probe on 2026-10-23: Cloudflare DoH returned Status 2 (SERVFAIL) with EDE(22) 'No Reachable Authority at delegation epikhost.com' and EDE(23) 'Network Error 87.117.238.51:53 returned REFUSED'; curl returned 'Could not resolve host'. A separate epikhost.org belongs to a different company and was not treated as the same provider.
- extras:
  - death_evidence: SERVFAIL, no reachable authority at delegation
  - probe_commands: curl 'https://cloudflare-dns.com/dns-query?name=epikhost.com&type=A' -H 'accept: application/dns-json'; curl -sS -o /dev/null -w '%{http_code}' https://epikhost.com/
- evidence:
  - probe:https://epikhost.com 2026-10-23: DoH Status 2 SERVFAIL, EDE 'No Reachable Authority at delegation epikhost.com', delegated NS 87.117.238.51 returned REFUSED; curl exit 6 for epikhost.com and www.epikhost.net
- sources:
  - [1] https://epikhost.com/
