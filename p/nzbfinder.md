# NZBFinder

> nzbfinder.ws | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbfinder/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbfinder.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBFinder

- `debrid/nzbfinder` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (Newznab API, tiered membership) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:50.405Z (live) | stale on 2026-11-18
- url https://nzbfinder.ws/
- free tier: Free tier reported as 5 NZB downloads and 25 API hits per day, no XXX access; Basic EUR 10/year gives 5,000 API hits and unlimited downloads, Pro EUR 20/year 20,000, Elite EUR 35/year unlimited plus Spotweb. The vendor's own caps declares <limits max="100" default="100"/> and <registration available="yes" open="yes"/>. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: Two 2026 third-party tables agree on 5 downloads / 25 API per day; a 2013 vendor forum post said 10 API and 5 downloads, and a March 2020 promotion raised it temporarily to 250 API and 100 downloads. The conservative 25 is kept.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: '18+ years of posts in our DB' (login page strapline); a third-party listing claims 'over 3,600 days of binary content, 500,000+ NZBs indexed'. | source: [2] | note: The vendor states a span in years, not a day count; the day figure is third-party.
- egress: No byte metering; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: Registration declares itself open in caps and /register serves an email field with the warning 'Temporary e-mail domains are banned', plus a verification link. Spam-blocking is the gate, not an invite.
- interface: rest
- limits:
  - request-rate (binding): 25 API hits per day and 5 NZB downloads per day on the free tier [3]
  - request-rate (binding): 100 results per request maximum [1]
- limits note: Registration is declared open, which is the one difference that matters against every other invite-only indexer among debrid providers.
- binding note: At a 1 TiB/month habit the daily counter is what stops a caller: 25 API hits a day is roughly one search per hour, and the 5-grab cap allows about 50 GB a day at a 10 GB average NZB, which is 1.5 TB a month only if nothing retries.
- interface detail: Newznab API on the same host at /api. caps advertises 100 results per request and open registration. The site lists Sonarr, Radarr, Prowlarr, NZBHydra 2, SickChill/SickGear, Chaptarr, Mylar, Lazylibrarian and Lidarr as compatible.
- endpoint: https://nzbfinder.ws/api?t=caps ; https://nzbfinder.ws/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab, no wrapper: Prowlarr, NZBHydra2 and every arr app add it with URL plus key.
- composes with: An open-registration indexer with a real API key on the free tier, so it can carry an arr stack at 25 searches and 5 grabs a day before EUR 10/year lifts the ceiling.
- reliability: Free accounts have been re-capped before without notice (the 2013 status post reverted a temporary lift), so a free allowance is a policy number that can change under a running stack.
- notes: The open-registration flag in caps is the strongest single fact on this record, and it is what separates NZBFinder from DrunkenSlug, NZBPlanet, Tabula Rasa and NinjaCentral today.
- evidence note: caps and the open-registration flag were measured on 2026-11-03; the free allowance that decides the verdict is third-party. One free account confirms the threshold and would move the record to documented.
- extras:
  - price: EUR 10/year Basic (reported); FREE = 5 downloads + 25 API hits/day
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: yes
- evidence:
  - probe:https://nzbfinder.ws/api?t=caps&x=1 2026-10-23: caps returned 200 and 2,425 bytes: title NZBFinder, <limits max="100" default="100"/>, <registration available="yes" open="yes"/>
  - probe:https://nzbfinder.ws/api?t=search&q=linux&x=1 2026-10-23: an unkeyed search did not reach the API: the origin answered a Cloudflare page (4,553 bytes), so the key requirement is inferred from the Newznab contract and caps, not from an error…
  - [2] 2026-10-23: vendor strapline '18+ years of posts in our DB', 'Newznab-compatible API', and the client list
  - [3] 2026-10-23: third-party 2026 table: Free 5 NZBs / 25 APIs; Basic 10 EUR / 5,000; Pro 20 EUR / 20,000; Elite 35 EUR / unlimited + Spotweb
  - [4] 2026-10-23: second third-party 2026 table with the same free row, and the note that 'Free' figures are daily
  - [5] 2026-11-03: the registration form asks for an email and bans temporary-email domains | capture: sha256:c428e5853ddc11b9395504b65640e8164ab02080f8d35fe56658098cfb09b7c9 | quote: Temporary e-mail domains are banned and cannot be used.
  - [5] 2026-11-03: a verification link is sent by email after registering | capture: sha256:c428e5853ddc11b9395504b65640e8164ab02080f8d35fe56658098cfb09b7c9 | quote: You'll get a verification link by email after registering.
  - [2] 2026-11-03: the login page still carries the 18+ years strapline | capture: sha256:912aeb630d8b3e1e39be7f0c51d79c00d4d9c09ab46dcb3163adc7388805ccee | quote: 18+ years of posts in our DB
  - probe:https://nzbfinder.ws/api?t=caps 2026-11-03: the unkeyed caps endpoint answered 200 with registration open | capture: sha256:0d4e1b62209c032c14136e215978961bcb0ab6993e1657baab0f753ef76e004b | quote: <registration available="yes" open="yes"/>
  - probe:https://nzbfinder.ws/api?t=caps 2026-11-03: the caps endpoint declares 100 results per request | capture: sha256:0d4e1b62209c032c14136e215978961bcb0ab6993e1657baab0f753ef76e004b | quote: <limits max="100" default="100"/>
  - [4] 2026-11-03: a second third-party 2026 table agrees on the free row: 5 NZB downloads and 25 API calls | capture: sha256:9c2bfa5d7026364275d16aca383dca947fb64a1725eaa2e8e8cf275b183497cd | quote: | Free | €0 | 5 | 25 | No |
  - [3] 2026-11-03: a third-party review last updated 2026-03-04 lists the free tier as 5 NZBs and 25 API calls | capture: sha256:d5e15485fb93ff392c1d3da460e5587de40998f6000f87896d1cf513613b4558 | quote: Free 5 NZBs & 25 API Calls
- sources:
  - [1] https://nzbfinder.ws/api?t=caps
  - [2] https://nzbfinder.ws/login
  - [3] https://usenetreviewz.com/nzbfinder-review/
  - [4] https://www.toolsurf.com/nzbfinder-price-2026/
  - [5] https://nzbfinder.ws/register
