# abNZB

> abnzb.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/abnzb/ | JSON https://fshy.ajam.dev/api/v1/entity/abnzb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## abNZB

- `debrid/abnzb` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (Newznab, open registration) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://abnzb.com/
- free tier: Reported, and the two listings disagree: '25 NZBs monthly, 10 API calls monthly' in one, '50 NZBs/day, 25 API, No BluRay/4K Movie sections' in the other. The site's own pages were walled and not read. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: unverified: the allowance is third-party and conflicting; the pricing page was behind a bot challenge.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [1]
- retention: A third-party listing claims 'Exceeds 500 days, 25+ newsgroups indexed'. | source: [1] | note: reported
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [1]
- identity: email | detail: unverified: the sign-up form was behind a bot challenge. A listing names the registration as open and says payment accepts cards, Bitcoin and gift cards.
- interface: rest
- limits:
  - request-rate (binding): reported: 25 NZBs and 10 API calls monthly (one listing) or 50 NZBs and 25 API per day (another) [1]
- binding note: The free counters are the only numeric limit named, and they are third-party and conflicting.
- interface detail: Newznab-based indexer per the listings; the API path was not read.
- endpoint: https://abnzb.com/
- tooling: Listings call it Newznab with an API counter on the free tier, so Prowlarr and NZBHydra2 would add it with URL plus key; the key sits behind a sign-up.
- composes with: A paid Supporter step at USD 12 to 15 per year is the reported way past a free allowance of a few dozen calls.
- reliability: Every direct request on the read date was answered with HTTP 403 and a redirect to the login page; a listing reports 98% uptime.
- evidence note: Every value is third-party; the site answered a bot challenge (HTTP 403) to a direct request.
- extras:
  - price: USD 0 (free); USD 12 per year Supporter (reported)
- evidence:
  - [1] 2026-11-03: third-party: free tier of 25 NZBs and 10 API calls monthly | quote: Generous free tier: 25 NZBs monthly, 10 API calls monthly.
  - [1] 2026-11-03: third-party: paid tiers are Supporter USD 12 per year and VIP USD 25 per year | quote: Supporter $12/year, VIP $25/year
  - [2] 2026-11-03: third-party: an older listing gives the free allowance as 50 NZBs and 25 API per day | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 50 NZBs/day, 25 API, No BluRay/4K Movie sections
  - probe:https://abnzb.com/ 2026-11-03: a direct request was answered HTTP 403 with a bot challenge | capture: sha256:fc5e9f014a39a0f3316e7b4cf6433f539859f5327409028192731ed0492a9f2d | quote: "status": 403
- sources:
  - [1] https://nzbhydra.com/indexers/
  - [2] https://github.com/openlemmy/reddit-backups/wiki/Indexers
