# NZBPlanet

> nzbplanet.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbplanet/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbplanet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBPlanet

- `debrid/nzbplanet` | fails-quota | evidence documented | binding request-rate | category Usenet indexer (Newznab API, free browse only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://nzbplanet.net/
- free tier: A free account is browse-only. The register page says 'Join NzbPlanet - free to browse, premium to download', and a vendor page cached in search results says 'The site is free to look around, you only need to pay for premium if you want to download nzb's'. caps declares <registration available="yes" open="no"/> and <limits max="100" default="100"/>. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an NZB pointer file | source: [2]
- retention: Free tier reported as 200 days, VIP or Platinum 2,500 days (nzbhydra.com, 2026-10-23). Not stated on the pages read from the vendor. | source: [3] | note: reported
- egress: No byte metering; the API returns pointers. | metered: no | source: [2]
- identity: email | detail: Email plus an invitation. caps says open=no, and the register page's invitecode field rejects an invented code; premium signup is the documented bypass.
- interface: rest
- limits:
  - request-rate (binding): 0 NZB downloads on the free tier; premium required for any download [1]
  - write-gated: invite code required at registration; a stale code is rejected [4]
  - request-rate (binding): 100 results per request maximum [2]
- binding note: The first thing that fails is the download allowance, which is zero on free: not a counter that runs out but one that never starts. The invite gate sits in front of it and would bind first only if registration were open.
- interface detail: Newznab API at /api, capped at 100 results per request. Registration is invitation-gated: the register page accepts an invitecode and rejects a bad one with 'Bad or invite code older than 7 days'.
- endpoint: https://nzbplanet.net/api?t=caps ; https://nzbplanet.net/api?t=search&q=<query>&apikey=<key>
- tooling: Native Newznab on paper; in practice the key belongs to an account that cannot download without a paid tier, so Prowlarr and NZBHydra2 can add it and still get nothing useful on free.
- composes with: A paid-only index: nothing on the free side contributes to a 1 TiB/month habit.
- reliability: Free accounts keep full search and zero grabs, so a misconfigured arr stack sees results and fails every download rather than failing at search time.
- notes: The registerpremium page that search engines still hold returned 404 to a direct request, so its wording is cited as a snippet and not as a page read.
- evidence note: The browse-only free tier and the invite gate are quoted from the vendor's own register pages read. Prices are third-party.
- extras:
  - price: USD 10/year VIP (reported)
  - nzb_is_newznab: yes
  - caps_limits: 100
  - registration_open: no
  - free_downloads: 0
- evidence:
  - [1] 2026-10-23: vendor text read: 'Join NzbPlanet - free to browse, premium to download', plus the email and password rules
  - probe:https://nzbplanet.net/api?t=caps&x=1 2026-10-23: caps returned 200 and 7,128 bytes: title 'Nzb Planet - NZB', <limits max="100" default="100"/>, <registration available="yes" open="no"/>
  - probe:https://nzbplanet.net/api?t=search&q=linux&x=1 2026-10-23: unkeyed search returned <error code="200" description="Missing parameter"/>, 91 bytes, so the API needs a key
  - [4] 2026-10-23: vendor page (search snippet): 'Bad or invite code older than 7 days'
  - [3] 2026-10-23: third-party: VIP USD 10/year, Platinum USD 24/year, free 200 days retention, free tier '0 calls'
- sources:
  - [1] https://nzbplanet.net/register
  - [2] https://nzbplanet.net/api?t=caps
  - [3] https://nzbhydra.com/indexers/
  - [4] https://nzbplanet.net/register?invitecode=INVITECODEHERE
