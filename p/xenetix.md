# Spots.xenetix.nl

> xenetix.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xenetix/ | JSON https://fshy.ajam.dev/api/v1/entity/xenetix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Spots.xenetix.nl

- `debrid/spots-xenetix-nl` | dead | evidence measured | binding none | category Usenet index (Spotweb, anonymous; no longer resolves) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://spots.xenetix.nl/
- free tier: none reachable: the host spots.xenetix.nl has no address record. A third-party listing describes it as a Spotweb index with no login, entirely free. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the index is unreachable | source: [1]
- egress: none: the host does not resolve to an address | metered: no | source: [1]
- identity: anonymous | detail: A third-party listing said no login or registration was required; the host cannot be reached to confirm.
- interface: unknown
- limits:
  - request-rate: none applicable: the host has no A record probe:https://cloudflare-dns.com/dns-query?name=spots.xenetix.nl&type=A
- binding note: The host does not resolve, so no limit is reachable.
- interface detail: none reachable: a DNS-over-HTTPS query for the A record answered NOERROR with only the parent zone's SOA row.
- endpoint: https://spots.xenetix.nl/
- tooling: none: a client cannot connect to a host with no address.
- composes with: none: replace it with a reachable index.
- reliability: The host returns no A record from a public resolver, while the parent zone xenetix.nl still answers.
- evidence note: The absence of the A record is a DNS answer read; only name resolution was checked, and a later return of the record would revive the offer.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://cloudflare-dns.com/dns-query?name=spots.xenetix.nl&type=A 2026-11-03: an A query returned an Authority SOA row for xenetix.nl and no Answer row, so the host has no A record | capture: sha256:e910b5354c58b941816f969b523d2aee03ccec363f036ff803b67668b913b955 | quote: "Question":[{"name":"spots.xenetix.nl","type":1}],"Authority":[{"name":"xenetix.nl","type":6
  - [2] 2026-11-03: third-party: the listing described a Spotweb index with no login, entirely free | quote: Spotweb-based. No login or registration required. Entirely free.
- sources:
  - [1] https://spots.xenetix.nl/
  - [2] https://nzbhydra.com/indexers/
