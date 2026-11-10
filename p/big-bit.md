# Big-bit

> big-bit.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/big-bit/ | JSON https://fshy.ajam.dev/api/v1/entity/big-bit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Big-bit

- `debrid/big-bit-org` | dead | evidence measured | binding none | category Usenet NZB index forum (domain parked for sale) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://big-bit.org/
- free tier: none: the domain serves a for-sale page instead of the index. A third-party listing described an English and Dutch forum with open registration and voluntary donations. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the index is gone | source: [1]
- egress: none: the domain serves a for-sale page | metered: no | source: [1]
- identity: email | detail: unverified: the register page is gone; a third-party listing called registration open.
- interface: unknown
- limits:
  - request-rate: none applicable: the domain is parked for sale probe:https://big-bit.org/
- binding note: The domain no longer serves the index, so no limit is reachable.
- interface detail: none: HTTP 200 with a script-built page whose text offers the domain for sale.
- endpoint: https://big-bit.org/
- tooling: none: nothing to automate.
- composes with: none: replace it with a reachable index.
- reliability: The page returns HTTP 200 with a for-sale notice, so a client that trusts the status code would take it for a live site.
- evidence note: The for-sale text is in the response body read.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://big-bit.org/ 2026-11-03: the response body of the domain offers it for sale | capture: sha256:914062afb404cdcb0e4fd2b0d9c9cfcd4c8df29536f2b6af52a2cb9eed128968 | quote: domain is for sale
  - [2] 2026-11-03: third-party: the listing described an English and Dutch forum | quote: 30,000+ monthly visitors. English and Dutch.
- sources:
  - [1] https://big-bit.org/
  - [2] https://nzbhydra.com/indexers/
