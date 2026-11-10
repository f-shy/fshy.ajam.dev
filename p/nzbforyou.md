# NZBforyou

> nzbforyou.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbforyou/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbforyou.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBforyou

- `debrid/nzbforyou` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet NZB index (forum-style, no API) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://www.nzbforyou.com/
- free tier: Reported as 2 NZB grabs per day and no API support on the free account; the other listing says 2 NZBs per 24 to 36 hours. The site's own pages were walled and not read. | unit: objects | metered on: request-count | read on: 2026-11-03 | source: [1] | note: unverified: the allowance is third-party; the site answered a bot challenge.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: not stated by any source read | source: [1] | note: unverified
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up form was behind a bot challenge; listings call registration open and the paid donation USD 12 to 13 per year.
- interface: unknown
- limits:
  - request-rate (binding): reported: 2 NZB grabs per day, no API (one listing); 2 NZBs per 24 to 36 hours (another) [1]
- binding note: The free grab counter is the only numeric limit named, and it is third-party.
- interface detail: A web index with a custom newznab-style interface per a listing; the same listing says there is no API.
- endpoint: https://www.nzbforyou.com/
- tooling: No API is reported, so Prowlarr and NZBHydra2 cannot add it; a wrapper would drive the web pages. That is a tooling note, not a verdict.
- composes with: A manual fallback; 2 NZBs per day, or one per day and a half, makes it a last-resort grab.
- reliability: A third-party listing says 'Recent data loss of NZB files reported'; a direct request on the read date was answered with HTTP 403.
- evidence note: Every value is third-party; the site answered a bot challenge (HTTP 403) to a direct request.
- extras:
  - price: USD 0 (free); USD 13 per year donation (reported)
- evidence:
  - [1] 2026-11-03: third-party: the free account gets 2 NZB grabs per day and no API | quote: Free: 2 NZB grabs/day. No API support.
  - [1] 2026-11-03: third-party: the paid donation is USD 13 per year | quote: $13/year donation for full features
  - [2] 2026-11-03: third-party: an older listing gives the free allowance as 2 NZBs per 24 to 36 hours | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 2 NZBs/24-36 hours
  - probe:https://www.nzbforyou.com/ 2026-11-03: a direct request was answered HTTP 403 with a bot challenge | capture: sha256:4928c2b5418af9bc04aa5017c78d10e2787eb1cd72619003b80b1fc7cc225bf0 | quote: "status": 403
- sources:
  - [1] https://nzbhydra.com/indexers/
  - [2] https://github.com/openlemmy/reddit-backups/wiki/Indexers
