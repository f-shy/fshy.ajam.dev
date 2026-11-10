# Miatrix

> miatrix.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/miatrix/ | JSON https://fshy.ajam.dev/api/v1/entity/miatrix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Miatrix

- `debrid/miatrix` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (own Newznab fork, open registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://www.miatrix.com/
- free tier: Reported as 10 NZBs and 40 API hits per day with no XXX access on a free account; a second third-party listing says '2 requests/day'. The site states registration is open and shows no allowance of its own on the pages read. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The two third-party figures disagree and neither is dated; the plans page behind the sign-up was not read.
- per-object cap: not applicable: an NZB pointer file, never the payload | source: [2]
- retention: The home page states '3000+ Days Of NZB Retention' and '13+ Million Releases'. | days: 3000 | source: [2] | note: documented as a vendor claim, not measured
- egress: No byte metering; the answer is an NZB pointer file. | metered: no | source: [2]
- identity: email | detail: The register form has username, password, confirm password and email fields, all marked mandatory; no card and no invite field is shown.
- interface: rest
- limits:
  - request-rate (binding): reported: 10 NZBs and 40 API hits per day on a free account; a second listing reports 2 requests per day [1]
- binding note: The daily counters are the only numeric limit named, and they are third-party.
- interface detail: Newznab-based indexer with a web UI; the API surface itself was not read.
- endpoint: https://www.miatrix.com/
- tooling: A third-party listing calls it Newznab-based, so Prowlarr and NZBHydra2 add it with URL plus key; the key sits behind a sign-up.
- composes with: A paid Member tier at USD 10 per year is the cheapest step up from a free allowance of a few dozen API hits a day.
- reliability: The home page reports a database server that failed to reboot in September 2025 and a move to new servers in November 2023; recent news posts were dated up to December 2025.
- evidence note: Registration state, retention claim and form fields are first-party; the free allowance and the prices are third-party and disagree with each other, so the record is at the third-party rung.
- extras:
  - price: USD 0 (free account); USD 10 per year Member (reported)
- evidence:
  - [2] 2026-11-03: registration is open | capture: sha256:2c6133bccdf6ce4fd809f589ea4109a40041d73357368658060707ebda819de9 | quote: Registration is currently OPEN
  - [2] 2026-11-03: the site claims 3000+ days of NZB retention | capture: sha256:2c6133bccdf6ce4fd809f589ea4109a40041d73357368658060707ebda819de9 | quote: 3000+ Days Of NZB Retention
  - [3] 2026-11-03: the register form has mandatory fields (username, password, confirm password, email) | capture: sha256:db57d6eeaba1fbe150cd0b1e4b3ba33781385ae3526d4f9030e57addd59d0e71 | quote: Indicates mandatory field.
  - [1] 2026-11-03: third-party: the free account allows 10 NZBs and 40 API hits per day | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 10 NZBs, 40 API hits/day, No XXX
  - [4] 2026-11-03: third-party: the paid tiers are Member USD 10 per year, VIP USD 20 per year and Lifetime USD 50 | quote: Member $10/year, VIP $20/year, Lifetime $50
  - [4] 2026-11-03: third-party: a second listing gives the free allowance as 2 requests per day | quote: 2 requests/day
  - [5] 2026-11-03: the news page records a database server reboot problem in September 2025 | capture: sha256:9c30d69bdefb7e43d0555baabf4a6a45b2aaab12037dcfbe4bf35be6618df3da | quote: We upgraded the software on our database server. This required a reboot.
- sources:
  - [1] https://github.com/openlemmy/reddit-backups/wiki/Indexers
  - [2] https://www.miatrix.com/
  - [3] https://www.miatrix.com/register
  - [4] https://nzbhydra.com/indexers/
  - [5] https://www.miatrix.com/content/6/News/
