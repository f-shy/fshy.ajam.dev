# altHUB

> althub.co.za | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/althub/ | JSON https://fshy.ajam.dev/api/v1/entity/althub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## altHUB

- `debrid/althub` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (Newznab API, open registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.166Z (live) | stale on 2026-11-18
- url https://althub.co.za/
- free tier: A new account starts on a 14-day Trial (500 API requests and 100 NZB downloads per day) and then moves to a Free tier with no expiry (100 API requests and 25 NZB downloads per day); Premium is USD 10 for 1 year. Vendor home page: 'Register and use altHUB without paying first. Upgrade later if you want higher limits.' | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The vendor promises a free start without a number. The daily caps are third-party figures from a review dated 2026-10-08 (Trial 500 API requests and 100 NZB downloads per day for 14 days, then Free 100 and 25 per day with no expiry); the vendor plans page redirects to the sign-in page.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not published on the pages reachable today; a third-party table claims '900,000+ NZBs from 80 newsgroups indexed'. | source: [2] | note: reported
- egress: No byte metering; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Registration is open: /register asks for a username, an email address that must be confirmed before sign-in, a password and a password confirmation, with no invite field and no card.
- interface: rest
- limits:
  - request-rate (binding): Free tier with no expiry: 100 API requests and 25 NZB downloads per day; 14-day Trial: 500 API requests and 100 NZB downloads per day [3]
  - write-gated: the vendor plans page redirects to the sign-in page (final URL /login?redirect=%2Fplans), so the Free and Trial caps are third-party figures [4]
- binding note: A daily counter is the limit: the Free tier has no expiry and allows 100 API requests and 25 NZB downloads per day, so request-rate binds on any automated use.
- interface detail: Newznab API. The site's own pages advertise 'Fast API', 'Works with SABnzbd and NZBGet, using the same API your client already speaks' and a response-time claim. An unauthenticated /api?t=caps returned 403 with text/plain, so the API refuses anonymous callers.
- endpoint: https://althub.co.za/api
- tooling: Native Newznab, explicitly built for SABnzbd and NZBGet; Prowlarr and NZBHydra2 add it with URL plus key.
- composes with: Premium is USD 10 for 1 year (USD 25 for 3 years, USD 40 for 5 years) and lifts the daily caps of the Free tier; the Trial and the Free tier make it worth trying before paying.
- reliability: The domain moved from althub.ovh, which now returns a Cloudflare 530 to every request; a saved config pointing at the old host fails at DNS, not at auth.
- notes: The old spelling altHUB.ovh is still circulating in lists; it answers 530, which reads like a dead service and is not one.
- evidence note: The registration form was observed on 2026-10-23 and again on 2026-11-03, and the unauthenticated API request was refused on 2026-10-23. The allowances are third-party (a review dated 2026-10-08) because the plans page redirects to the sign-in page. One free account would show the first-party caps.
- extras:
  - price: USD 10/year Premium (reported)
  - nzb_is_newznab: yes
  - old_host: althub.ovh returns Cloudflare 530
  - registration_open: yes
  - relaunched: site relaunched on September 15, 2026 with registration reopened two days later (third-party review)
- evidence:
  - probe:https://althub.co.za/ 2026-10-23: vendor text read: 'Fast API', 'Free to start - Register and use altHUB without paying first. Upgrade later if you want higher limits.'
  - probe:https://althub.co.za/register 2026-10-23: registration form with username, password, confirm and email; no invitecode field
  - probe:https://althub.co.za/api?t=caps 2026-10-23: unauthenticated caps returned 403 with text/plain, so the API rejects anonymous callers
  - probe:https://althub.co.za/plans 2026-10-23: the plans page returned a Cloudflare 'Just a moment' interstitial (403); a pinned browserless retry also failed
  - [2] 2026-10-23: third-party: 'Open registration', 'AltPRO USD 5/year, AltUNLIMITED USD 10/year', '14-day trial: 5,000 downloads and 5,000 API calls'
  - [3] 2026-11-03: a review that read the plans page on 2026-10-08 lists the Free tier as 100 API requests and 25 NZB downloads per day with no expiry | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Free (free, no expiry): 100 API requests and 25 NZB downloads per day. No requests or invites.
  - [3] 2026-11-03: the Trial tier is free for 14 days at 500 API requests and 100 NZB downloads per day and then moves to Free | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Trial (free, 14 days): 500 API requests and 100 NZB downloads per day. No requests or invites. Moves to Free automatically.
  - [3] 2026-11-03: the Free tier caps are 100 API requests and 25 NZB downloads per day | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Free (free, no expiry): 100 API requests and 25 NZB downloads per day. No requests or invites.
  - [3] 2026-11-03: the review is the source of the Free tier caps | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Free (free, no expiry): 100 API requests and 25 NZB downloads per day. No requests or invites.
  - [4] 2026-11-03: a read of /plans through a pinned provider ended on the sign-in page with a redirect back to /plans | capture: sha256:3afbf4a09b1324f80c8b53bb3751dc5a8660c647960c340cfc35b091ba55804a | quote: x-web-final-url: https://althub.co.za/login?redirect=%2Fplans
  - [4] 2026-11-03: the row cites the plans page itself | capture: sha256:3afbf4a09b1324f80c8b53bb3751dc5a8660c647960c340cfc35b091ba55804a | quote: x-web-final-url: https://althub.co.za/login?redirect=%2Fplans
  - [3] 2026-11-03: Premium costs $10 for 1 year, $25 for 3 years and $40 for 5 years, with unlimited API requests and NZB downloads | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Premium ($10 for 1 year, $25 for 3 years, $40 for 5 years): unlimited API requests, NZB downloads and requests, plus 10 invites. Returns to Free when the term ends.
  - [3] 2026-11-03: Premium is $10 for 1 year | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Premium ($10 for 1 year, $25 for 3 years, $40 for 5 years): unlimited API requests, NZB downloads and requests, plus 10 invites. Returns to Free when the term ends.
  - [3] 2026-11-03: the Free tier is a daily counter of 100 API requests and 25 NZB downloads | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Free (free, no expiry): 100 API requests and 25 NZB downloads per day. No requests or invites.
  - [5] 2026-11-03: the registration form is served and asks for an email address that must be confirmed | capture: sha256:c27344a32799374be24560ca3cc29c1018fd298d7f0f809bdbf8a412dbb032a4 | quote: Email addressUse an address you can access. You'll need to confirm it before you can sign in.
  - [5] 2026-11-03: the form asks for an email address that is confirmed before sign-in | capture: sha256:c27344a32799374be24560ca3cc29c1018fd298d7f0f809bdbf8a412dbb032a4 | quote: Email addressUse an address you can access. You'll need to confirm it before you can sign in.
  - [3] 2026-11-03: the site relaunched on 2026-09-15 and reopened registration two days later | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: altHUB relaunched its site on September 15, 2026, and reopened registration two days later.
  - [1] 2026-11-03: the vendor home page still promises a free start and gives no number | capture: sha256:5715167c5582bea48e0db2045bbb8133eff22495c1b76ad212397a907826996d | quote: Register and use altHUB without paying first. Upgrade later if you want higher limits.
  - [3] 2026-11-03: a third-party review states that the vendor publishes no retention figure and no index size | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: altHUB does not publish retention or index size
  - [3] 2026-11-03: the Free tier is 100 API requests and 25 NZB downloads per day with no expiry | capture: sha256:c2d35fe2d7d04ce47653d43bfa16716b859efe80ccb97cc869d742dbb8460ee5 | quote: Free (free, no expiry): 100 API requests and 25 NZB downloads per day. No requests or invites.
- sources:
  - [1] https://althub.co.za/
  - [2] https://nzbhydra.com/indexers/
  - [3] https://usenetreviewz.com/althub-review/
  - [4] https://althub.co.za/plans
  - [5] https://althub.co.za/register
