# NinjaCentral

> ninjacentral.co.za | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ninjacentral/ | JSON https://fshy.ajam.dev/api/v1/entity/ninjacentral.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NinjaCentral

- `debrid/ninjacentral` | fails-identity | evidence documented | binding write-gated | category Usenet indexer (Newznab API, closed registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://ninjacentral.co.za/
- free tier: Reported free allowance of 20 API hits and 5 downloads a day, raised temporarily to 300 and 50 by the admin. caps declares <limits max="100" default="100"/> and <registration available="yes" open="no"/>. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not published on the pages reachable; a third-party tracker records the site as closed or offline as of 2026-10-06. | source: [2] | note: reported
- egress: No byte metering; the API returns pointers. The HTML site answered with 14 words of text, which is a login shell, not content. | metered: no | source: [1]
- identity: email | detail: Closed. caps declares available=yes but open=no, which is the invite-only shape; a third-party tracker records 'Registration closed / site offline' checked 2026-10-06.
- interface: rest
- limits:
  - request-rate: 20 API hits and 5 downloads per day free (reported), raised temporarily to 300 and 50 [3]
  - write-gated (binding): registration closed; caps open=no [1]
  - request-rate: 100 results per request maximum [1]
- binding note: Registration fails first; caps says open=no and a third-party tracker says the site is closed, so no quota is reachable.
- interface detail: Newznab API at /api, 100 results per request. The web front end serves almost no server-rendered text (14 words to an extractor), so the caps endpoint is the only readable surface.
- endpoint: https://ninjacentral.co.za/api?t=caps ; https://ninjacentral.co.za/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab, so Prowlarr and NZBHydra2 can hold an entry, but only a key obtained during a registration window makes it work.
- composes with: Nothing without an account; it is a membership to watch for a registration window rather than a usable index today.
- reliability: Third-party reports describe the site as offline while its API still answers caps, so reachability of the API is not evidence that the index is alive.
- evidence note: Registration closure is documented from the vendor's caps read. Allowance and pricing are third-party.
- extras:
  - price: EUR 15/year (reported)
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: no
- evidence:
  - probe:https://ninjacentral.co.za/api?t=caps&x=1 2026-10-23: caps returned 200 and 2,898 bytes: title NinjaCentral, <limits max="100" default="100"/>, <registration available="yes" open="no"/>
  - probe:https://ninjacentral.co.za/ 2026-10-23: the front end gave an extractor 14 words, under the 20-word threshold, so no page content was readable
  - [3] 2026-10-23: third-party: 'dan 0 1 year, 2,000 API hits, 450 downloads EUR 15'; free limits once raised to 300 API hits and 50 downloads
  - [2] 2026-10-23: third-party, checked 2026-10-06: 'Registration closed / site offline'
- sources:
  - [1] https://ninjacentral.co.za/api?t=caps
  - [2] https://www.bestnzbsites.com/sites/ninjacentral/
  - [3] https://usenetalmanac.com/indexer/ninjacentral/
