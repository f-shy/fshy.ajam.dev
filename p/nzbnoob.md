# NzbNoob

> nzbnoob.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbnoob/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbnoob.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NzbNoob

- `debrid/nzbnoob` | qualifies-with-caveat | evidence documented | binding request-rate | category Usenet indexer (Newznab, open registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://nzbnoob.com/
- free tier: Free registration: 1 download and 100 API hits per day, XXX access included, USD 0. The VIP Donor tier is 200 downloads and 2,000 API hits for USD 12. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The page states the counters reset daily and that VIP Donor benefits reset annually.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: not stated on the pages read. A third-party listing claims '1,500 days of binary retention'. | source: [2] | note: unverified
- egress: No byte metering; the answer is an NZB pointer file and the payload comes from the news provider. | metered: no | source: [1]
- identity: email | detail: The register form asks for a user name, a password, a password confirmation and an email address; no card and no invite code is requested (the invite field is hidden and empty).
- interface: rest
- limits:
  - request-rate (binding): free registration: 1 download and 100 API hits per day; VIP Donor: 200 downloads and 2,000 API hits [1]
- limits note: The two counters reset daily on the free tier.
- binding note: One download a day fails first for any bulk workload, before the 100 API hits do.
- interface detail: Newznab-style indexer with an API counter on the account. The API path itself was not read.
- endpoint: https://nzbnoob.com/
- tooling: A third-party listing names it Newznab-based, so Prowlarr and NZBHydra2 add it with URL plus key; the key sits behind a sign-up and was not read.
- composes with: At 100 API hits a day the free account is enough for automated search; 1 download a day is the part that forces a paid tier or another indexer for the grab.
- reliability: unverified: no outage or throttle was observed; one read of the home page and the register form only.
- evidence note: Both the counters and the register form fields are first-party text read; the free account was not created, so the counters were not exercised.
- extras:
  - price: USD 0 (free registration); USD 12 VIP Donor
- evidence:
  - [1] 2026-11-03: the free registration row: 1 download, 100 API hits, XXX access, USD 0 | capture: sha256:f0033aa1380f36ded0311f1c534b66c7036355d34186bc7fd9a3ac2c94815ffd | quote: | Free reg | 1 | 100 | Yes | 0 | $0 |
  - [1] 2026-11-03: the paid tier: 200 downloads, 2,000 API hits and 5 invites for USD 12 | capture: sha256:f0033aa1380f36ded0311f1c534b66c7036355d34186bc7fd9a3ac2c94815ffd | quote: | VIP Donor | 200 | 2000 | Yes | 5 | $12 |
  - probe:https://nzbnoob.com/register 2026-11-03: the register form asks for an email address | capture: sha256:5fbdf16901d7a2922a7b98dff3465fbc19066895b804ea6ab3f54007af8824a9 | quote: placeholder="Your email address"
  - [2] 2026-11-03: third-party: the listing claims 1,500 days of binary retention | quote: 1,500 days of binary retention
- sources:
  - [1] https://nzbnoob.com/
  - [2] https://nzbhydra.com/indexers/
