# Usenet Crawler

> usenet-crawler.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenet-crawler/ | JSON https://fshy.ajam.dev/api/v1/entity/usenet-crawler.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Usenet Crawler

- `debrid/usenet-crawler` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet indexer (Newznab API, open registration) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:53.664Z (live) | stale on 2026-11-18
- url https://www.usenet-crawler.com/
- free tier: Free tier reported at 10,000 API calls and 1,000 NZB downloads per user per day, with a USD 20 lifetime VIP; caps declares <registration available="yes" open="yes"/> and <limits max="100" default="100"/>. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The 10,000 figure appears in two independent third-party sources but neither is dated on the page, so it is kept as reported and flagged as the number to check first with an account.
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: Free tier 2,700 days across 500+ indexed newsgroups; VIP 3,900 days (nzbhydra.com, 2026-10-23). | source: [2] | note: reported; a second third-party review states 'Retention is currently at five years and still growing', which differs from the figure in the retention field
- egress: No byte metering; the API returns pointers. | metered: no | source: [1]
- identity: email | detail: The register form asks for username, email, password and a Google reCAPTCHA; its invitecode input is type="hidden", so no invite code is asked in the form. The API documents a register function that 'Does not require any credentials'. Whether the server enforces an invite was not tested: submitting the form creates an account.
- interface: rest
- limits:
  - request-rate (binding): 10,000 API calls per day free (reported) [2]
  - pull-count: 1,000 NZB downloads per day free (reported) [3]
  - request-rate (binding): 100 results per request maximum [1]
- limits note: At 10,000 calls a day the request rate stops being the constraint and the 100-result page becomes it: a client that wants a whole season must paginate.
- binding note: If the reported allowance holds, nothing in the vocabulary binds at 1 TiB/month; the record still names request-rate because that is the only counter the vendor is documented to run, and it is the one to verify first.
- interface detail: Newznab API at /api. /api with no parameters returns <error code="200" description="Missing parameter"/>, which is the Newznab key check, so the endpoint is live and keyed.
- endpoint: https://www.usenet-crawler.com/api?t=caps ; https://www.usenet-crawler.com/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab, listed as integrating with NZBVortex and SabNZBD, so Prowlarr and NZBHydra2 add it with URL plus key.
- composes with: The only open-registration indexer among debrid providers claiming a five-figure daily API allowance, which is what an arr stack actually needs; the caveat is that the claim is third-party and undated.
- reliability: The public pages of the domain now sell Usenet block accounts and advertise 'Pay Only ONCE', so the indexer and a news provider share one brand; a report of a database outage and fake releases in September 2026 exists in a third-party status tracker.
- notes: Registering confirms both open questions at once (is the invite mandatory, what is the real daily counter) and is the single highest-value follow-up among debrid providers.
- evidence note: caps, the keyed error and the registration form were observed today; the allowance that decides the verdict is third-party. One free account moves this to documented.
- extras:
  - price: USD 20 lifetime VIP (reported)
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: yes
- evidence:
  - probe:https://www.usenet-crawler.com/api?t=caps&x=1 2026-10-23: caps returned 200 and 40,803 bytes: title usenet-crawler, <limits max="100" default="100"/>, <registration available="yes" open="yes"/>
  - probe:https://www.usenet-crawler.com/api?t=search&q=linux&x=1 2026-10-23: unkeyed search returned <error code="200" description="Missing parameter"/>, 91 bytes
  - probe:https://www.usenet-crawler.com/register 2026-10-23: the register form carries username, password, confirmpassword, email and an empty invitecode field
  - [2] 2026-10-23: third-party: 'Open registration', 'USD 20 lifetime membership VIP', '10,000 calls/day', free tier 2,700 days
  - [3] 2026-10-23: third-party: 'the limits are set to 10k API and 1k NZB downloads per user per day'
  - [4] 2026-11-03: the API documentation lists a register function that needs no credentials | capture: sha256:c6d71db862fcafd467681bb81e35265b43b63387ecfdef4957292e31500e8233 | quote: Registers a new user account. Does not require any credentials in order to be ran.
  - [3] 2026-11-03: third-party review: 10k API and 1k NZB downloads per day, retention five years | capture: sha256:63578792bbf694a30c671b2e4ab45e7e6ea559794bfc98ac26bdc48357c88883 | quote: Currently the limits are set to 10k API and 1k NZB downloads per user per day. Retention is currently at five years and still growing.
  - probe:https://www.usenet-crawler.com/register 2026-11-03: the register form's invitecode input is type hidden | capture: sha256:53438a74b5f13a06f6b96d17eb6f0f7778d0cbad3067f0ac288b176b8083508d | quote: <input id="invitecode" name="invitecode" type="hidden" value="" />
  - [2] 2026-11-03: third-party listing: 10,000 calls/day | quote: - 10,000 calls/day
  - [1] 2026-11-03: the caps document declares open registration | capture: sha256:6ab0f3cc87cae334f4a94699da35c06465365d32adbc5fdda461fa62d30891c4 | quote: <registration available="yes" open="yes" />
  - [1] 2026-11-03: the caps document declares 100 results per request | capture: sha256:6ab0f3cc87cae334f4a94699da35c06465365d32adbc5fdda461fa62d30891c4 | quote: <limits max="100" default="100"/>
- sources:
  - [1] https://www.usenet-crawler.com/api?t=caps
  - [2] https://nzbhydra.com/indexers/
  - [3] https://www.newsgroupreviews.com/usenet-crawler-review.html
  - [4] https://www.usenet-crawler.com/apihelp
