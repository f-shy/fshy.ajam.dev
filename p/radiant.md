# Ori Global Cloud

> radiant.co | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/radiant/ | JSON https://fshy.ajam.dev/api/v1/entity/radiant.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ori Global Cloud

- `compute/ori-global-cloud` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T08:50:29.745Z (live) | stale on 2026-12-04
- url https://radiant.co/ori
- free tier: no free lane and no self-serve signup. The merged company sells powered-land AI factories from 10,000 to 100,000+ GPUs with Brookfield capital behind it; the site carries no price and no trial. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): there is no price page and no signup: capacity is sold through a sales conversation about powered land and clusters, which a single person cannot enter. [1]
- limits note: there is no price page and no signup: capacity is sold through a sales conversation about powered land and clusters, which a single person cannot enter.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: none: nothing here is reachable without a sales relationship.
- reliability: no reliability event recorded
- notes: Ori appears on every stale GPU-cloud list as an independent vendor with hourly rates. The rebrand is the finding that stops the next reader chasing it: the old ori.co domain now redirects to radiant.co/ori, and no pricing page exists. Recorded paid-only rather than dead because the platform still operates for customers under the new brand.
- extras:
  - facets.class: rebrand
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 'Radiant is the new company formed through the merger of Ori Industries and Brookfield's AI infrastructure capabilities. Ori's technology, team, and cloud platform all continue under the Radiant brand'; 'scaling from 10K to 100K+ GPUs', quoted
  - [2] 2026-10-22: 404: 'The page you're looking for hasn't been deployed to this cluster', measured
  - [3] 2026-10-22: quoted: 'H100 SXM5 at $2.90/hr on Ori', described as the cheapest current secure on-demand SXM5 price in that tracker's summary
  - [4] 2026-10-22: 
  - [5] 2026-10-22: HTTP 404 with the tracker's own not-found page, which is the observation behind the third bullet above
  - [1] 2026-11-03: the Ori page is the merged company's page, still without a GPU price | capture: sha256:2595ec0c3da2742afd530a09dcad4146a271725866a64d2b28651a0695ba8469 | quote: Radiant is the new company formed through the merger of Ori Industries and Brookfield's AI infrastructure capabilities.
  - [3] 2026-11-03: a third-party tracker lists an H100 SXM5 at USD 2.90 per hour on Ori; no first-party page lists it | capture: sha256:8cf1b54169a04c2d073b5b81b5f1f41f4f0fb355d8d19ce9f0a5979729835769 | quote: | [H100 SXM5](https://gpuperhour.com/rent/h100-sxm-80gb) [all H100](https://gpuperhour.com/rent/h100) | $2.90/hr | Ori | $2.22/hr (30 days) | 5 |
- sources:
  - [1] https://radiant.co/ori
  - [2] https://radiant.co/pricing
  - [3] https://gpuperhour.com/
  - [4] https://gpurentalprices.com/
  - [5] https://gpurentalprices.com/providers/ori
