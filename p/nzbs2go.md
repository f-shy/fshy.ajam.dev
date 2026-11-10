# NZBs2GO

> nzbs2go.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbs2go/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbs2go.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBs2GO

- `debrid/nzbs2go` | dead | evidence measured | binding none | category Usenet indexer (Spotnet-based; no longer resolves) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://nzbs2go.com/
- free tier: none: the name nzbs2go.com has no address record, so no free tier can be reached. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the index is unreachable | source: [1]
- egress: none: the name does not resolve to an address | metered: no | source: [1]
- identity: email | detail: unverified: the register page cannot be reached.
- interface: unknown
- limits:
  - request-rate: none applicable: the host has no A record probe:https://cloudflare-dns.com/dns-query?name=nzbs2go.com&type=A
- binding note: The name does not resolve, so no limit is reachable.
- interface detail: none reachable: a DNS-over-HTTPS query for the A record answered NOERROR with only the zone's SOA row.
- endpoint: https://nzbs2go.com/
- tooling: none: a client cannot connect to a name with no address.
- composes with: none: replace it with a reachable indexer.
- reliability: The apex name returns no A record from a public resolver; the zone itself still answers, so the address record was removed or never set rather than the zone lapsing.
- evidence note: The absence of the A record is a DNS answer read; only name resolution was checked, and a later return of the record would revive the offer.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://cloudflare-dns.com/dns-query?name=nzbs2go.com&type=A 2026-11-03: an A query returned an Authority SOA row and no Answer row, so the name has no A record | capture: sha256:949a0e164c2249d5e1eb40baacf1f98cb654a27255b671164e3dbaa4dd94b4c1 | quote: "Question":[{"name":"nzbs2go.com","type":1}],"Authority":[{"name":"nzbs2go.com","type":6
  - [2] 2026-11-03: third-party: the listing described a Spotnet-based index of 300,000+ NZB files | quote: 300,000+ NZB files indexed. Spotnet-based.
- sources:
  - [1] https://nzbs2go.com/
  - [2] https://nzbhydra.com/indexers/
