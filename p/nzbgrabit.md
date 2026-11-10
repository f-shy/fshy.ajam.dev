# NZBGrabit

> nzbgrabit.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbgrabit/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbgrabit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBGrabit

- `debrid/nzbgrabit` | qualifies-with-caveat | evidence reported | binding retention-clamped | category Usenet NZB index (vBulletin forum) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://nzbgrabit.org/
- free tier: Reported as 10 days retention and 5 NZBs per day on a free account, with no API because it is a forum. The site's own page lists an 'API Key Info' link, so the no-API claim was not confirmed. | unit: objects | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The free allowance is third-party and undated; the paid tiers are GBP 14 per year (Supporter) and GBP 15.50 per year (Super Supporter) in the same listing.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [2]
- retention: Reported as 10 days of retention on the free account. | days: 10 | source: [1] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [2]
- identity: email | detail: unverified: the sign-up form was not readable; a third-party listing calls registration open and the site is a forum that takes a credit card only for the paid tiers.
- interface: unknown
- limits:
  - retention-clamped (binding): reported: 10 days retention and 5 NZBs per day on a free account [1]
- binding note: Ten days of retention is the shortest horizon named, and it is third-party.
- interface detail: A vBulletin forum; the front page links Welcome Page, API Key Info and Donate / Upgrade.
- endpoint: https://nzbgrabit.org/
- tooling: The page lists an API Key Info link; whether a Newznab-style API exists was not read. Otherwise a wrapper has to drive the forum pages. That is a tooling note, not a verdict.
- composes with: A manual fallback; 10 days of retention on the free account makes it a recent-release grab only.
- reliability: The origin answers a bot wall (HTTP 403) with only the forum footer and menu text; the footer shows 2012 to 2025.
- evidence note: The allowance, the retention and the prices are third-party; only the menu entries come from the site, and a bot wall limited the read to them.
- extras:
  - price: USD 0 (free); GBP 14 per year Supporter (reported)
- evidence:
  - [1] 2026-11-03: third-party: free account retention is 10 days with 5 NZBs per day | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 10 days retention, 5 NZBs/day (Forum, so there is no API)
  - [1] 2026-11-03: third-party: the Supporter tier is GBP 14 per year or GBP 17 for 3 years | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: £14 /1 year or £17 /3 year (Supporter)
  - [2] 2026-11-03: the site page lists an API Key Info entry | capture: sha256:5498f5e037ae44fc08f8f05b93d77c56693079197012c5920f142d4769f23b90 | quote: - API Key Info
  - [2] 2026-11-03: the site is a vBulletin forum dated 2012 to 2025 | capture: sha256:5498f5e037ae44fc08f8f05b93d77c56693079197012c5920f142d4769f23b90 | quote: NZBGrabit 2012 - 2025 Powered by vBulletin® Version 4.2.5
- sources:
  - [1] https://github.com/openlemmy/reddit-backups/wiki/Indexers
  - [2] https://nzbgrabit.org/
