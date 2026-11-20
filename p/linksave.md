# Linksave

> linksave.in | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linksave/ | JSON https://fshy.ajam.dev/api/v1/entity/linksave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linksave (linksave.in / linkcrypt.ws)

- `debrid/linksave` | dead | evidence measured | binding none | category link container / link protector (dead) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://linksave.in/
- free tier: Historical: a free link protector whose API took a username and password and returned a folder URL. 'URL: http://linksave.in/protect?api=[username]:[Password]' with fields for links, mirrors, captcha on/off and container types rsdf/ccf/dlc. Nothing of the service answers today. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The 2011 API description is third-party. No current page on the domain exists to confirm or price anything.
- per-object cap: not applicable: it held links, not bytes. | source: [2]
- retention: unknown and now moot: the service is unreachable, so nothing is retained. | source: [2]
- egress: none: dead. | metered: no | free allowance: none | source: [2]
- identity: anonymous | detail: Historical API used a username:password pair embedded in the URL; whether registration was open is not verifiable now.
- interface: rest
- limits:
  - request-rate: no service: the wildcard host ww17.linksave.in fails name resolution probe:https://linksave.in/
- limits note: The 302 target is the same wildcard pattern that linkcrypt.ws now uses, which suggests one operator or one parking setup for both domains.
- binding note: Nothing binds because nothing answers: at any volume the first failure is DNS.
- interface detail: Historical HTTP API only: POST to /protect?api=user:pass with *save, *links and optional container/captcha fields. Today the domain issues a 302 to a wildcard host that does not resolve in DNS.
- tooling: JDownloader used to ship a linksave decrypter plugin. Nothing to drive now.
- composes with: none: a dead container service removes an indirection layer, it does not add one.
- reliability: Dead as of 2026-10-23: 302 to ww17.linksave.in, then getaddrinfo failure (errno 11004). The proxy also returned 504 on the plain read. Last known live capture is the Wayback snapshot of 2025-05-24, HTTP 200.
- notes: linkcrypt.ws is the same case and is documented here rather than as a second file: both 302 to the identical ww17.<domain> wildcard and both fail DNS. Requirements names both; one dead service with two domains is one fact.
- evidence note: The death is measured twice (probe redirect + DNS failure, proxy 504). The description of what it was rests on a 2011 forum post and the archive capture, and is marked reported.
- probe:
  - url: https://linksave.in/
  - final_url: https://linksave.in/
  - method: GET
  - status: 302
  - bytes: 0
  - content_type: text/html
  - elapsed_ms: 1921.8
  - redirects[0].status: 302
  - redirects[0].location: https://ww17.linksave.in/
  - redirects[0].raw_location: https://ww17.linksave.in/
  - redirects[0].from: https://linksave.in/
  - headers_subset.server: Apache
  - headers_subset.location: https://ww17.linksave.in/
  - headers_subset.content-length: 0
  - headers_subset.content-type: text/html; charset=UTF-8
  - challenge.detected: no
  - error: dns
  - probed_at: 2026-10-23T01:47:06.978Z
  - probe_version: 1.0.0
  - usable: no
  - declared_bytes: 0
  - truncated: no
  - sha256_scope: none
  - attempts: 2
  - urls_tried: https://linksave.in/; https://ww17.linksave.in/
  - tls.insecure: no
  - false_200.detected: no
  - error_detail: URLError: <urlopen error [Errno 11004] getaddrinfo failed>
- extras:
  - sibling_domain: linkcrypt.ws (302 to ww17.linkcrypt.ws, DNS failure)
  - last_live_capture: 2025-05-24T06:39:44Z (Wayback, HTTP 200)
- evidence:
  - probe:https://linksave.in/ 2026-10-23: HTTP 302 to https://ww17.linksave.in/, then 'getaddrinfo failed' errno 11004; 0 bytes; no hash
  - probe:https://linkcrypt.ws/ 2026-10-23: the sibling domain fails identically: 302 to https://ww17.linkcrypt.ws/, then DNS failure
  - [3] 2026-10-23: Wayback capture 2025-05-24 06:39:44 of the root: HTTP 200, text/html, 1122 bytes recorded
  - [1] 2026-10-23: reported, 2011: the protect API signature and the rsdf/ccf/dlc container options
- sources:
  - [1] https://www.autoitscript.com/forum/topic/129784-help-using-winhttp-to-send-data-using-linksave-api/
  - [2] https://linksave.in/
  - [3] https://web.archive.org/web/20250524063944/http://linksave.in/
