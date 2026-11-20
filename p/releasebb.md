# ReleaseBB

> releasebb.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/releasebb/ | JSON https://fshy.ajam.dev/api/v1/entity/releasebb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ReleaseBB

- `debrid/releasebb` | dead | evidence documented | binding none | category DDL release index (defunct; domain now a parking router) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
- url https://releasebb.net/
- price USD 0
- free tier: none: the domain no longer serves an index. The root returned 5,591 bytes titled 'Redirecting...' whose script posts browser fingerprints to https://router.parklogic.com/ | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no content served | source: [1]
- retention: not applicable: no posts | source: [1]
- egress: none: there is no content to serve | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: No signup path exists on the served page.
- interface: unknown
- limits:
  - request-rate: the interstitial gates on ad-blocking detection, iframe and webdriver flags, GPU vendor and timezone before answering [1]
- binding note: There is nothing to meter and no rate to observe; the domain serves a parking page rather than an index.
- interface detail: The only interface is a JavaScript interstitial that either replaces the document with a parklogic routing answer or runs an ad-blocking and webdriver check first.
- tooling: A browser gets redirected; there is no feed, no API and no host link. A command-line client receives the same 5,591-byte interstitial.
- composes with: None. ReleaseBB cannot sit in the stack. The live DDL feeds measured among debrid providers are scnlog.me, ddlbase.com and rlsbb.cc.
- reliability: Parked domain: the served page carries no release data, so a client pointed at it receives an ad or a redirect rather than a post.
- notes: Distinct from rlsbb.cc, which is still alive and whose feed channel is also titled 'ReleaseBB'. The two names are the same brand on different domains; only rlsbb.cc serves posts today. Not deleted, because a name this common will be searched again.
- evidence note: The root was fetched raw on 2026-10-23 and the interstitial's own base64 parameters were decoded: they name domainApex 'releasebb.net' and tenant 'seth3'. A second capture on another day would show whether the parking is permanent.
- extras:
  - parking_router: router.parklogic.com
  - bytes: 5591
- evidence:
  - [1] 2026-10-23: raw root is 5,591 bytes titled 'Redirecting...' and POSTs fingerprints to https://router.parklogic.com/ with domainApex 'releasebb.net'
  - [1] 2026-10-23: the reader's extractor found 1 word in the page and refused it as 'no content', consistent with an interstitial rather than an index
- sources:
  - [1] https://releasebb.net/
