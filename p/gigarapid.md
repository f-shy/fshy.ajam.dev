# GigaRapid

> gigarapid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gigarapid/ | JSON https://fshy.ajam.dev/api/v1/entity/gigarapid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GigaRapid

- `debrid/gigarapid` | dead | evidence measured | binding none | category former seedbox host (domain for sale) | tier none
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:00:08.862Z (live) | stale on 2026-12-26
- url https://gigarapid.com/
- free tier: none: gigarapid.com is a GoDaddy for-sale page - 'gigarapid.com is for sale — Get a price in 24 hours | GoDaddy'. No seedbox plan is purchasable. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no service | source: [1]
- retention: not applicable: no service | source: [1]
- egress: no service to assess | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: not applicable; nothing can be registered | country: None
- interface: unknown
- binding note: no constraint applies to a parked for-sale domain
- interface detail: no interface: the domain is listed for sale
- tooling: part of the free tier
- composes with: removed from the candidate set; the cheapest plan any index reports for this name cannot be bought
- reliability: The domain is parked for sale on GoDaddy with a price request, so any price index that still lists a EUR 0.99 plan is stale and would send a buyer to a dead checkout
- notes: This is the clearest case in the sector of a price index outliving its provider. The index is useful for breadth and must never be the evidence for a number; the parked page is the evidence here.
- evidence note: Measured by probe on 2026-10-23: https://gigarapid.com/ returned 200 and redirected to forsale.godaddy.com with the text 'GigaRapid.com is for sale!' and the price USD 2,695 (lease USD 450/month). Two price indexes still quote GigaRapid Eco AF10 at EUR 0.99, which is how a stale index costs a session.
- extras:
  - death_evidence: GoDaddy for-sale landing page at USD 2,695
  - index_that_still_lists_it: seedboxcompare.com/en/cheapest-seedbox
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - probe:https://gigarapid.com 2026-10-23: redirect to forsale.godaddy.com; page text 'GigaRapid.com is for sale! ... Own it today for $2,695, or select Lease to Own ... USD$450 / month'
  - [2] 2026-10-23: third-party index still lists 'GigaRapid Eco AF10 at EUR 0.99 per month' as the cheapest plan, which the parked domain disproves
  - probe:https://gigarapid.com/lander 2026-11-25: the domain is parked for sale on GoDaddy with no seedbox service | capture: sha256:a09e7acdc4d576878c6119f9d94fb804e3c4b7edd1506cb7f845759985eff02d | quote: gigarapid.com is for sale — Get a price in 24 hours | GoDaddy
  - probe:https://gigarapid.com/lander 2026-11-25: the domain name is the one listed for sale, so no seedbox service is served | capture: sha256:a09e7acdc4d576878c6119f9d94fb804e3c4b7edd1506cb7f845759985eff02d | quote: GigaRapid.com
  - probe:https://gigarapid.com/lander 2026-11-25: the domain is for sale, so no seedbox service remains | capture: sha256:a09e7acdc4d576878c6119f9d94fb804e3c4b7edd1506cb7f845759985eff02d | quote: gigarapid.com is for sale — Get a price in 24 hours | GoDaddy
  - probe:https://gigarapid.com/lander 2026-11-25: a direct GET of gigarapid.com/lander follows a 307 to the GoDaddy for-sale page whose title is a price-request listing for the domain | capture: sha256:b0fcc2501fa56035e97d55b90d4ae3c73581fbb24ffa1e190582ecfa6b48f5a4 | quote: gigarapid.com is for sale — Get a price in 24 hours | GoDaddy
  - [1] 2026-11-25: the first-party lander at the domain states that GigaRapid.com is for sale, so no seedbox checkout is available | capture: sha256:9265f796fdeb033fb9d9fbdbf845b611c0adb0c040f71907c7adc5686d5bf0a9 | quote: The domain name GigaRapid.com is for sale!
  - probe:https://gigarapid.com/ 2026-11-25: a direct GET of the domain answers 200 with only a 114-byte HTML redirect stub, so a client that trusts the status code sees no service | capture: sha256:a7a7232f783d69147468479843c3319aaa333a13713d8de6f893ac5da2f38975 | quote: "false_200": {
- sources:
  - [1] https://gigarapid.com/
  - [2] https://seedboxcompare.com/en/cheapest-seedbox
