# UsenetNow

> usenetnow.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetnow/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetnow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetNow

- `debrid/usenetnow` | paid-only | evidence documented | binding none | category Usenet provider (seven server regions) - no free trial | tier monthly
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:22.000Z (live) | stale on 2026-11-23
- url https://usenetnow.net/
- free tier: None on the page read: "$3.99 per week", "$7.99 per month", "$19.99 per quarter". No trial, free account or free allowance is offered. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: No per-object cap is published. The unit of retrieval is a Usenet article, roughly 750 KB by convention. | source: [1]
- retention: "Industry leading retention and continuously increasing day by day" - no day count is published on the page read. | source: [1] | note: The page names no retention figure at all, which is unusual for the market and is documented as null rather than guessed.
- egress: No byte counter or traffic price is published; the product is sold by time (week, month, quarter) with "FREE SSL encryption". | metered: no | free allowance: none | source: [1]
- identity: card | detail: The page's only call to action is pricing; no free path exists. The instrument at checkout was not read.
- interface: unknown
- limits:
  - request-rate: not stated on the page read [1]
- limits note: Connection count and speed are not published on the home page.
- binding note: Nothing in the vocabulary can be shown to fail at 1 TiB/month because the vendor publishes no counter, no connection cap and no speed on the page read; the price per week is the real constraint.
- interface detail: NNTP over SSL. The schema has no nntp token, so the array says unknown.
- tooling: any NNTP client
- composes with: The $3.99 week is the shortest paid unit in the set, useful when a job needs four days of access and no monthly subscription is wanted.
- reliability: No suspension report was read. The absence of a published retention or connection figure makes this provider hard to compare on anything but price.
- notes: Repeatability: not applicable. Abandonment: if the price page stops rendering, the record needs a re-read before it is cited.
- evidence note: The three prices are quoted from the vendor page on 2026-10-23. Retention and connections are documented as unpublised rather than filled in from a comparison site.
- extras:
  - repeatable: not-applicable
  - repeat_basis: no free trial
- evidence:
  - [1] 2026-10-23: "$3.99 per week", "$7.99 per month", "$19.99 per quarter", "We have SEVEN reliable Usenet systems strategically located in the USA & Europe", "FREE SSL encryption"
- sources:
  - [1] https://usenetnow.net/
