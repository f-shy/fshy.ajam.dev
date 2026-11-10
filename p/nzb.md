# NZB.life

> nzb.life | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzb/ | JSON https://fshy.ajam.dev/api/v1/entity/nzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZB.life

- `debrid/nzb-life` | qualifies-with-caveat | evidence documented | binding none | category Usenet indexer (Newznab API, successor to NZB.su) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.nzb.life/
- free tier: Not stated on the pages reachable. caps declares <limits max="100" default="100"/> and <registration available="yes" open="yes"/>; /register serves a Create Account form with password rules and no invite field. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: unit is recorded as none because no allowance is published; A third-party table claims the old NZB.su free tier gave '0 calls' and that VIP was USD 9 for 180 days and USD 15 for 360 days.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not published on the pages read; a third-party table claims 'over 2,000 days of binary retention, 50 newsgroups indexed' for the old name. | source: [2] | note: reported
- egress: No byte metering observed; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Open registration: /register serves Create Account with a 10-character password policy and no invite or card field.
- interface: rest
- limits:
  - request-rate: 100 results per request maximum [1]
  - write-gated: registration open, but the allowance is only visible after login [3]
- binding note: No counter could be read without an account, so naming one would be a guess. The 100-result cap is real and measured in caps; it is a per-request result ceiling, not a rate.
- interface detail: Newznab API at /api (caps title still reads 'NZB.su', so the software was renamed but not the server string), 100 results per request. Registration is a plain form on the site.
- endpoint: https://www.nzb.life/api?t=caps ; https://www.nzb.life/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab: change the host in an existing NZB.su entry and the key keeps working, per the vendor's own error message. Prowlarr and NZBHydra2 need nothing else.
- composes with: The live successor under the old NZB.su key, so an existing stack recovers by editing one URL.
- reliability: The capabilities response still identifies as 'NZB.su', referencing the legacy service domain.
- evidence note: caps and the registration form were read. The allowance is unstated, which is why the verdict is a caveat.
- extras:
  - price: USD 15/360 days (reported, under the old name)
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: yes
  - predecessor: nzb-su
- evidence:
  - probe:https://www.nzb.life/api?t=caps&x=1 2026-10-23: caps returned 200 and 226,097 bytes: title 'NZB.su', <limits max="100" default="100"/>, <registration available="yes" open="yes"/>
  - probe:https://www.nzb.life/register 2026-10-23: Create Account form with password rules (10+ characters, one uppercase, one number, one special), no invite field
  - [2] 2026-10-23: third-party for the old name: 'VIP 180-day USD 9, 360-day USD 15', free tier '0 calls'
- sources:
  - [1] https://www.nzb.life/api?t=caps
  - [2] https://nzbhydra.com/indexers/
  - [3] https://www.nzb.life/register
