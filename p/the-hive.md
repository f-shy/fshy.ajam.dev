# The Hive

> the-hive.be | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/the-hive/ | JSON https://fshy.ajam.dev/api/v1/entity/the-hive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## The Hive

- `debrid/the-hive` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet NZB index (vBulletin forum, no API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://www.the-hive.be/forum/
- free tier: Registration is free. Reported allowance on a free account: 1 NZB per day and limited forum access; no API because it is a forum. | unit: objects | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The allowance is third-party; the forum pages do not state a number.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [2]
- retention: not stated on the forum pages read. A third-party listing claims 'Approximately 500 days retention, 50+ newsgroups indexed'. | source: [3] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [2]
- identity: email | detail: Registration needs an email address that can receive mail (the rules ban several mail providers because password reset would not work) and the member's statement of being at least 18 years old; no card is asked.
- interface: unknown
- limits:
  - request-rate (binding): reported: 1 NZB per day on a free account [1]
- binding note: The one NZB a day is the only numeric limit named, and it is third-party.
- interface detail: A forum: NZBs are downloaded through the web UI after login. A third-party listing states there is no API and no integrations.
- endpoint: https://www.the-hive.be/forum/
- tooling: A wrapper has to log in and drive the forum pages; Prowlarr and NZBHydra2 cannot add a forum as a Newznab indexer. That is a tooling note, not a verdict.
- composes with: A manual fallback for a name when the API indexers have failed; 1 NZB a day makes it a last-resort grab, not a bulk path.
- reliability: A third-party listing records 95.5% uptime; the forum answered with 2,079 active users.
- evidence note: The free registration and the email requirement are first-party text; the 1 NZB a day figure is third-party and undated.
- extras:
  - price: USD 0 (free); GBP 12.20 per year paid (reported)
- evidence:
  - [2] 2026-11-03: registration is free | capture: sha256:0290f499d524635940b223a83993dd2ab92c61f17b607360555b184dfed43e62 | quote: Registration to this forum is free!
  - [2] 2026-11-03: an email address that can receive mail is needed for an account | capture: sha256:0290f499d524635940b223a83993dd2ab92c61f17b607360555b184dfed43e62 | quote: otherwise simple things like password reset would not be possible
  - [4] 2026-11-03: the forum is live and busy on the read date | capture: sha256:0aaea468ec66d8a201d30ba03aad2f612ce99ad4e1a366389bc0fc04a589ddae | quote: Most users ever online was 48,322, 22nd-October-2026 at 02:46:41 PM.
  - [1] 2026-11-03: third-party: a free account gets 1 NZB per day and the site has no API | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 1 NZB /day (Forum, so there is no API)
  - [3] 2026-11-03: third-party: the free tier is 1 NZB per day with limited forum access | quote: Free: 1 NZB/day, limited forum access.
  - [3] 2026-11-03: third-party: the listing claims about 500 days of retention and 50+ newsgroups | quote: Approximately 500 days retention, 50+ newsgroups indexed
  - [3] 2026-11-03: third-party: the listing reports 95.5% uptime | quote: 95.5% uptime, 350ms response time
- sources:
  - [1] https://github.com/openlemmy/reddit-backups/wiki/Indexers
  - [2] https://www.the-hive.be/forum/register.php
  - [3] https://nzbhydra.com/indexers/
  - [4] https://www.the-hive.be/forum/index.php
