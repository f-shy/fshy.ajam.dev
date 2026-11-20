# SwiftSeedbox

> swiftseedbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swiftseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/swiftseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SwiftSeedbox

- `debrid/swiftseedbox` | dead | evidence measured | binding none | category former seedbox host (domain does not resolve) | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://www.swiftseedbox.com/
- free tier: none: swiftseedbox.com does not resolve. DNS over HTTPS returns NXDOMAIN (Status 3) and a local lookup returns 'Could not resolve host'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no service | source: [1]
- retention: not applicable: no service | source: [1]
- egress: no service to assess | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: not applicable; nothing can be registered | country: None
- interface: unknown
- binding note: no constraint applies to a name that does not resolve
- interface detail: no interface: the name has no DNS record
- tooling: part of the free tier
- composes with: removed from the candidate set; nothing resolves, so nothing can be ordered or retrieved
- reliability: NXDOMAIN at the registry level, not a blocked fetch: the name is not delegated
- notes: A brief that names SwiftSeedbox should treat it as gone. The check is cheap to repeat: one DoH query. If the name is re-registered, this record is stale rather than wrong, and must be re-probed before use.
- evidence note: Measured by probe on 2026-10-23: Cloudflare DoH for swiftseedbox.com returned Status 3 (NXDOMAIN) with the .com authority section and no answer; curl returned 'Could not resolve host'. swiftseedbox.ch was tried too and also did not resolve.
- extras:
  - death_evidence: NXDOMAIN at the .com registry
  - probe_commands: curl 'https://cloudflare-dns.com/dns-query?name=swiftseedbox.com&type=A' -H 'accept: application/dns-json'; curl -sS -o /dev/null -w '%{http_code}' https://www.swiftseedbox.com/
- evidence:
  - probe:https://www.swiftseedbox.com 2026-10-23: DoH 'Status: 3' (NXDOMAIN) for swiftseedbox.com, A query; curl exit 6 'Could not resolve host' for www.swiftseedbox.com and for swiftseedbox.ch
- sources:
  - [1] https://www.swiftseedbox.com/
