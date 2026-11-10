# News69

> keagaming.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keagaming/ | JSON https://fshy.ajam.dev/api/v1/entity/keagaming.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## News69

- `debrid/news69` | dead | evidence measured | binding none | category Usenet indexer (Newznab; no longer resolves) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://newz69.keagaming.com/
- free tier: none reachable: the host newz69.keagaming.com has no address record. A third-party listing describes a free Newznab-based service. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the index is unreachable | source: [1]
- egress: none: the host does not resolve to an address | metered: no | source: [1]
- identity: email | detail: unverified: the register page cannot be reached; a third-party listing called registration open.
- interface: unknown
- limits:
  - request-rate: none applicable: the host has no A record probe:https://cloudflare-dns.com/dns-query?name=newz69.keagaming.com&type=A
- binding note: The host does not resolve, so no limit is reachable.
- interface detail: none reachable: a DNS-over-HTTPS query for the A record answered NOERROR with only the parent zone's SOA row.
- endpoint: https://newz69.keagaming.com/
- tooling: none: a client cannot connect to a host with no address.
- composes with: none: replace it with a reachable indexer.
- reliability: The host returns no A record from a public resolver, while the parent zone keagaming.com still answers.
- evidence note: The absence of the A record is a DNS answer read; only name resolution was checked, and a later return of the record would revive the offer.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://cloudflare-dns.com/dns-query?name=newz69.keagaming.com&type=A 2026-11-03: an A query returned an Authority SOA row for keagaming.com and no Answer row, so the host has no A record | capture: sha256:397656cf409e1028aef0711a1dafc6280530527e0169b78eb82ea343491a2c36 | quote: "Question":[{"name":"newz69.keagaming.com","type":1}],"Authority":[{"name":"keagaming.com","type":6
  - [2] 2026-11-03: third-party: the listing described a free Newznab-based service | quote: Surprisingly free service. Newznab-based.
- sources:
  - [1] https://newz69.keagaming.com/
  - [2] https://nzbhydra.com/indexers/
