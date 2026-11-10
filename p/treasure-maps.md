# Treasure Maps

> treasure-maps.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/treasure-maps/ | JSON https://fshy.ajam.dev/api/v1/entity/treasure-maps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Treasure Maps

- `debrid/treasure-maps` | qualifies-with-caveat | evidence documented | binding none | category Usenet indexer (Newznab API, renamed from SceneNZBs) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://treasure-maps.com/
- free tier: Not stated on the login or caps surface. caps declares <limits max="500" default="250"/> and <registration available="yes" open="yes"/>; the login page offers 'No account yet? Register'. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: unit is recorded as none because the vendor publishes no allowance at all.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not published anywhere reachable; the caps carries no retention figure | source: [1] | note: unverified
- egress: No byte metering observed; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Registration is offered from the login page ('No account yet? Register') and caps declares it open; an existing SceneNZBs account carries over.
- interface: rest
- limits:
  - request-rate: 500 results per request maximum [1]
  - write-gated: registration is open per caps but the allowance is only visible after login [1]
- binding note: No counter could be read without an account, so naming one would be a guess. The 500-result cap is real and measured in caps; it is a per-request result ceiling, not a rate.
- interface detail: Newznab API at /api (caps appversion 1.0.0-snzb, 500 results per request). Site login supports a passkey or username plus password, with two-factor.
- endpoint: https://treasure-maps.com/api?t=caps ; https://treasure-maps.com/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab, so Prowlarr, NZBHydra2 and the arr apps add it with URL plus key. An existing SceneNZBs entry must have its URL edited to this host.
- composes with: The live name for a SceneNZBs account; nothing changes in the stack except the host.
- reliability: A rename that kept accounts but moved hosts; the risk is a stale host in a client, which reads as an empty index rather than an error.
- notes: The 458 KB caps is the largest among debrid providers, which means a very wide category list; nothing else could be learned without an account.
- evidence note: caps and the login page were read. The free allowance is unstated, so the verdict is a caveat rather than a qualification.
- extras:
  - price: unstated
  - nzb_is_newznab: yes
  - caps_limits: 500
  - registration_open: yes
  - predecessor: scenenzbs
- evidence:
  - probe:https://treasure-maps.com/api?t=caps&x=1 2026-10-23: caps returned 200 and 458,697 bytes: title 'Treasure Maps', appversion 1.0.0-snzb, <limits max="500" default="250"/>, registration available and open
  - [2] 2026-10-23: vendor text: 'SceneNZBs now sails under a new flag - Treasure Maps. Your access still works.' plus 'No account yet? Register'
- sources:
  - [1] https://treasure-maps.com/api?t=caps
  - [2] https://treasure-maps.com/
