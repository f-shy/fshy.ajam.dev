# NZBServer.com

> nzbserver.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzbserver/ | JSON https://fshy.ajam.dev/api/v1/entity/nzbserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZBServer.com (public Spotweb)

- `debrid/nzbserver-com` | qualifies | evidence measured | binding none | category Public Spotweb instance exposing a Newznab API | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://www.nzbserver.com/
- free tier: No account, no key, nothing to register. /api?t=caps returned 2,140 bytes declaring <registration available="no" open="no"/> and <limits max="500" default="50"/>; /api?t=search&q=linux returned 41,868 bytes of RSS with 50 items; /api?t=g&id=... returned a 7,346-byte NZB. The site is 'Entirely free, no upgrade options' per a third-party listing (nzbhydra.com, 2026-10-23). | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No per-day counter is declared in caps or published on the page. 10 rapid searches produced no 429.
- per-object cap: not applicable per object, but the request accepts at most 500 results: <limits max="500" default="50"/> in caps | source: [1] | note: The 500 is results per request, not a byte cap.
- retention: not stated in caps or on the page. The index is Spotnet-derived, so its depth follows the Spotnet post history rather than a vendor commitment. | source: [1] | note: unverified: no retention figure is published anywhere reachable.
- egress: No metering and no account. The API returns RSS with NZB enclosures; each NZB measured 7,346 bytes. | metered: no | source: [1]
- identity: anonymous | detail: Nothing: no account route (caps says registration unavailable), no key, no cookie needed for caps, search or get.
- interface: rest
- limits:
  - request-rate: none observed: 10 consecutive searches in one session, all 200 probe:https://www.nzbserver.com/api?t=search&q=test1..test10
  - request-rate: 500 results per request maximum; a limit above 500 silently returns the 50-result default probe:https://www.nzbserver.com/api?t=search&q=linux&limit=501
- limits note: The clamp is the only ceiling that behaved like a quota. Measured: limit=500 returned 178 items (all matches for 'linux'), limit=200 returned 178, limit=100 returned 100, limit=501 returned 50, limit=999 returned 50, limit=1000 returned 50. The three clamped responses are byte-identical to the default one (sha256 964a100b...), so the server is not truncating a larger answer: it is ignoring the parameter and serving the default page. A client that asks for 1000 gets fewer results than one that asks for 200, with HTTP 200 and no error element.
- binding note: There is no daily counter and no byte quota, so nothing in the vocabulary fails at a 1 TiB/month habit. The first thing a client actually meets is the results-per-request clamp above 500, which the vocabulary has no kind for.
- interface detail: A Newznab-shaped API on /api. caps advertises <server type="Spotweb" version="0.1"> with search, tv-search and an NZB endpoint at /api?t=g&id=<message-id>. No apikey parameter was required for caps, search or get.
- endpoint: https://www.nzbserver.com/api?t=caps ; https://www.nzbserver.com/api?t=search&q=<query> ; https://www.nzbserver.com/api?t=g&id=<message-id>
- tooling: Any Newznab client can use it: Prowlarr and NZBHydra2 both accept a generic Newznab indexer with a URL and a key, and this endpoint ignores the key. Sonarr, Radarr, Lidarr and Mylar therefore work without a wrapper. There is also a Spotweb web UI at /?page=index with per-post NZB links.
- composes with: The only indexer among debrid providers that needs neither an account nor a key, so it is the zero-identity default for an arr stack; its Dutch Spotnet catalogue is the gap that a second indexer fills.
- reliability: A stock Spotweb install (caps still carries the default placeholder email 'john@example.com (Jane Doe)') run by a volunteer; a third-party listing records 'inconsistent uptime, 4.6s response time when operational', so a client should not make it the only indexer.
- notes: The 7,346-byte NZB has the same sha256 as the one spotnzb.com served for the same message-id, so the two instances share a Spotnet backend or mirror the same database; the search feeds differ slightly in size (41,868 vs 41,244 bytes) but start with the same item. Treat them as one catalogue reachable at two hostnames, not as two independent indexers.
- evidence note: caps, search and NZB download were all run today with status, bytes and digest. The retention and uptime figures are third-party and are labelled as such.
- extras:
  - price: USD 0
  - measurements[0].url: https://www.nzbserver.com/api?t=caps&x=1
  - measurements[0].status: 200
  - measurements[0].bytes: 2140
  - measurements[0].sha256: 229536ac73e0d2a4c7f6a594ce2b4b8ec50141350ee3fd9f7004ea96a00fd051
  - measurements[1].url: https://www.nzbserver.com/api?t=search&q=linux&x=1
  - measurements[1].status: 200
  - measurements[1].bytes: 41868
  - measurements[1].sha256: 964a100b65980145cff530bb4b70523356bd815a1fe2d4a434de3d7798daf181
  - measurements[2].url: https://www.nzbserver.com/api?t=g&id=19XKJ8pokN4BLjUagNmQp@spot.net&x=1
  - measurements[2].status: 200
  - measurements[2].bytes: 7346
  - measurements[2].sha256: ac230711afeb760dee32b4ef20a83f42c339d7bfaa8a2bdafa46b482f3e0c6bc
  - measurements[3].url: https://www.nzbserver.com/api?t=search&q=linux&limit=500
  - measurements[3].status: 200
  - measurements[3].bytes: 147360
  - measurements[3].sha256: 4923fd0a54fc804f32704a8365f2d4eabf919a14ead630a27e33cc0cafef3918
  - measurements[3].note: limit=500 returned 178 items
  - measurements[4].url: https://www.nzbserver.com/api?t=search&q=linux&limit=501
  - measurements[4].status: 200
  - measurements[4].bytes: 41868
  - measurements[4].sha256: 964a100b65980145cff530bb4b70523356bd815a1fe2d4a434de3d7798daf181
  - measurements[4].note: limit=501 returned 50 items, byte-identical to the default response, not 178
  - nzb_is_newznab: yes
  - caps_type: Spotweb
  - content_language: predominantly Dutch (NL subs, Flemish series in the default index)
  - burst: 10 sequential searches, all 200
- evidence:
  - probe:https://www.nzbserver.com/api?t=caps&x=1 2026-10-23: caps returned 200 and 2,140 bytes: type Spotweb, <limits max="500" default="50"/>, <registration available="no" open="no"/>
  - probe:https://www.nzbserver.com/api?t=search&q=linux&x=1 2026-10-23: anonymous Newznab search returned 200 and 41,868 bytes of RSS with 50 items and NZB enclosures (sha256 964a100b...)
  - probe:https://www.nzbserver.com/api?t=g&id=19XKJ8pokN4BLjUagNmQp@spot.net&x=1 2026-10-23: anonymous NZB download returned 200, application/x-nzb, 7,346 bytes, 10 <file> elements (sha256 ac230711...)
  - probe:https://www.nzbserver.com/api?t=search&q=linux&limit=501 2026-10-23: the clamp: 501 returned 50 items while 500 returned 178, with HTTP 200 and no error body
  - [2] 2026-10-23: third-party: 'Spotweb-based technology. No login or registration required. Entirely free, no upgrade options. Inconsistent uptime, 4.6s response time when operational.'
- sources:
  - [1] https://www.nzbserver.com/api?t=caps
  - [2] https://nzbhydra.com/indexers/
