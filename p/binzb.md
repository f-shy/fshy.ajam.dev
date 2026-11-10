# Binzb

> binzb.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/binzb/ | JSON https://fshy.ajam.dev/api/v1/entity/binzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Binzb

- `debrid/binzb` | dead | evidence documented | binding none | category Usenet search engine (domain now serves an unrelated gambling site) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://binzb.com/
- free tier: none: the domain serves an unrelated gambling site, branded LAMTOTO, in place of the search engine. A third-party listing described a free search engine with no registration. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the search engine is gone | source: [1]
- egress: none: the domain serves an unrelated site | metered: no | source: [1]
- identity: anonymous | detail: A third-party listing said no registration was required; the original service is gone.
- interface: unknown
- limits:
  - request-rate: none applicable: the domain serves an unrelated site [1]
- binding note: The domain no longer serves the search engine, so no limit is reachable.
- interface detail: none: HTTP 200 with the page of an unrelated gambling site whose login and sign-up links point to another host.
- endpoint: https://binzb.com/
- tooling: none: nothing to automate.
- composes with: none: replace it with a reachable index.
- reliability: The page returns HTTP 200, so a client that trusts the status code would take the unrelated site for a live index.
- evidence note: The page text read names another brand and links its login and sign-up elsewhere; no search request was made.
- extras:
  - price: unverified: unreachable
- evidence:
  - [1] 2026-11-03: the page is branded LAMTOTO, an unrelated site, not a Usenet search engine | capture: sha256:21a934818d118f556305b11e0b10c071e0b0e073e6384cd79444bc2a965dc0ac | quote: Powered By: [LAMTOTO](https://binzb.com/)
  - [2] 2026-11-03: third-party: the listing described a free, automated search engine with no registration | quote: No registration required. Completely free. Automated, not manually curated.
- sources:
  - [1] https://binzb.com/
  - [2] https://nzbhydra.com/indexers/
