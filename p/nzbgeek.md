# NZBGeek

> nzbgeek.info | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbgeek/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbgeek.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBGeek

- `debrid/nzbgeek` | fails-quota | evidence reported | binding request-rate | category Usenet indexer (Newznab API, paid membership) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:59.770Z (live) | stale on 2026-11-18
- url https://nzbgeek.info/
- free tier: No free tier is documented: a third-party review checked in October 2026 states that search and downloads require an active subscription, and a comparison table lists NZBGeek's free tier as 'None (subscription required)'. An unkeyed search is refused with an empty-API-key error and caps declares registration available=no. Earlier third-party readings of a free trial and of a few downloads a day are not found on the pages read now. The public site lists no prices. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The conservative reading is the one the vendor's own API supports: an unkeyed call is refused, and no reading of the free tier describes an API allowance enough to drive an arr stack. The 5-calls-a-day figure is unsourced, not contradicted.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: not stated on the API surface. A third-party listing claims 'NZBs from 8 years ago available, 500,000+ indexed NZBs' (nzbhydra.com, 2026-10-23). | source: [2] | note: reported
- egress: No byte metering: the API returns XML pointers. The payload is served by whichever news provider is paid for. | metered: no | source: [1]
- identity: email | detail: Registration is contradictory at the vendor: the login page links 'register account?' and register.php serves a Registration Agreement with an 'agree' submit, while /api?t=caps declares <registration available="no" open="no"/>; a third-party review checked in October 2026 states that registration was open. The fields a signup demands are unverified: behind a sign-up.
- interface: rest
- limits:
  - request-rate (binding): no free API allowance that a stack can use; paid membership USD 12/year [2]
  - request-rate (binding): 100 results per request maximum (caps <limits max="100"/>) [1]
- limits note: The 100 is a per-request result ceiling and applies to every tier; it is not the paid allowance.
- binding note: The API call allowance is what fails first: without a key the first automated search is refused outright (error 102), and the readings of the free tier that describe an allowance put it at 5 calls a day, which is one search every five hours.
- interface detail: Newznab API on a separate host, api.nzbgeek.info/api, not nzbgeek.info/api (the apex returns HTML). caps declares <limits max="100" default="100"/> and <registration available="no" open="no"/>. An unkeyed search returns error code 102.
- endpoint: https://api.nzbgeek.info/api?t=caps ; https://api.nzbgeek.info/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab: Prowlarr, NZBHydra2, Sonarr, Radarr, Lidarr and Mylar all add it with URL plus key. No wrapper needed. The API host is different from the site host, which is the first mistake a hand-rolled config makes.
- composes with: A broad, well-populated index that a paid arr stack reaches with no wrapper; on the free tier it contributes nothing to automation, because no reading of the free tier gives an API allowance that could drive a stack.
- reliability: The membership is what keeps the index alive; a lapsed membership drops the account back to the capped tier and automation stops with no partial service.
- notes: Two vendor signals contradict each other on registration: a served agreement form says open, caps says available=no. The conservative reading is recorded on the record and not resolved, because resolving it needs an account. The verdict rests on the API allowance, which is independent of that question.
- evidence note: The caps and the unkeyed error were measured. Creating one free account and reading its API page would move this to documented.
- extras:
  - price: USD 12/year (reported by a third-party index; the vendor's public site lists no prices; another third party says plans start at USD 6 for six months)
  - nzb_is_newznab: yes
  - caps_limits: 100
  - api_host: api.nzbgeek.info
  - unkeyed_error: 102 Empty API Key
- evidence:
  - probe:https://api.nzbgeek.info/api?t=caps&x=1 2026-10-23: caps returned 200 and 3,927 bytes: NZBgeek, <limits max="100" default="100"/>, <registration available="no" open="no"/>
  - probe:https://api.nzbgeek.info/api?t=search&q=linux&x=1 2026-10-23: unkeyed search returned 200 with 47 bytes: <error code="102" description="Empty API Key"/>, so the API is closed to a free, unauthenticated caller
  - probe:https://nzbgeek.info/api?t=caps 2026-10-23: the apex host serves HTML for /api, 91,943 bytes; the API lives only on api.nzbgeek.info
  - probe:https://nzbgeek.info/register.php 2026-10-23: an anonymous GET receives the Registration Agreement plus an 'agree' submit, which contradicts the caps registration flag; no POST was made
  - [2] 2026-10-23: third-party: NZBGeek 'USD 12/year VIP', free tier '0 calls'
  - [3] 2026-10-23: third-party: the paid tier 'removes download caps and unlocks full API integration'
  - [4] 2026-10-23: third-party: 'NZBgeek used to have a free level, but now you need a paid membership to search and download.'
  - [3] 2026-11-03: a 2026 third-party review: search and downloads require an active subscription | capture: sha256:353a2166e05f491ace74bf1619e192b82dad43b8a67665de8788ab3b3a15771b | quote: Registration was open when we checked in October 2026, but search and downloads require an active subscription and the policy states there are no refunds, so choose a plan length you are comfortable with before paying.
  - probe:https://nzbgeek.info/register.php 2026-11-03: an anonymous GET of register.php still serves the Registration Agreement with an 'agree' submit | capture: sha256:0035bbdc45a6c9b1cc2809ed47a685db20bf09c8d2a67e891bf71467d1711207 | quote: <input class="login_button" tabindex="2" type="submit" name="terms" value="agree" id="terms">
  - [4] 2026-11-03: third party: no free level, a paid membership is needed to search and download | capture: sha256:4fb8969be035c81787b5758be09ea61789f17486b6dbcfc3a8ca52620769032d | quote: NZBgeek used to have a free level, but now you need a paid membership to search and download.
  - [1] 2026-11-03: caps still declares a 100-result ceiling and registration available=no | capture: sha256:5e6abdb0ee09ae266514c935c0d9701417027c1a5dfe5fb9c3e5e865c3eef1fb | quote: <limits max="100" default="100"/><registration available="no" open="no"/>
  - [5] 2026-11-03: third-party table: NZBGeek's free tier is 'None (subscription required)' | capture: sha256:292540c8bb826f676e1f6fc436f8f09f10148d74423d0b32ce6b38e5f6b2f0af | quote: | Free Tier | 5 NZBs, 100 API hits/day | None (subscription required) |
  - probe:https://api.nzbgeek.info/api?t=search&q=linux&x=2 2026-11-03: an unkeyed search is refused with error 102 (probe 2026-11-03) | capture: sha256:afb41bce94e8ab6613b7b561b5b1e4ed12c50e02174efa8f1f8bd6d16a0cfd44 | quote: <error code="102" description="Empty API Key"/>
  - [2] 2026-11-03: third-party index: USD 12/year VIP with 6-month, 1-year, 2-year and lifetime options | quote: $12/year VIP (flexible options: 6 months, 1 year, 2 years, lifetime)
  - [3] 2026-11-03: third-party review: plan prices are not on the public site | capture: sha256:353a2166e05f491ace74bf1619e192b82dad43b8a67665de8788ab3b3a15771b | quote: NZBgeek does not list its prices on the public site.
- sources:
  - [1] https://api.nzbgeek.info/api?t=caps
  - [2] https://nzbhydra.com/indexers/
  - [3] https://datahoarder.io/nzbgeek-review/
  - [4] https://www.usenet.com/free-nzb-sites/
  - [5] https://datahoarder.io/drunkenslug-vs-nzbgeek/
