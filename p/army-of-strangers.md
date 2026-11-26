# Army of Strangers

> army-of-strangers.biz | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/army-of-strangers/ | JSON https://fshy.ajam.dev/api/v1/entity/army-of-strangers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Army of Strangers

- `debrid/army-of-strangers` | dead | evidence measured | binding none | category Usenet NZB link forum (redirects to a parking host) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-25T12:00:07.720Z (live) | stale on 2026-12-26
- url https://army-of-strangers.biz/
- free tier: none: the former NZB link forum is gone; the domain now redirects to a third-party online casino (casino, sports betting, poker and lotteries) with no NZB index or free tier. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the forum is unreachable | source: [1]
- egress: none: the domain redirects to a parking host that does not resolve | metered: no | source: [1]
- identity: email | detail: unverified: the register page cannot be reached; a third-party listing called registration open and said a VPN must be disabled at signup.
- interface: unknown
- limits:
  - request-rate: none applicable: a probe read a client-side redirect page at the domain, and no NZB index is served probe:https://army-of-strangers.biz/
- binding note: The domain no longer serves the forum, so no limit is reachable.
- interface detail: None reachable for an NZB index: a first-party read of the domain now redirects to a third-party online casino site
- endpoint: https://army-of-strangers.biz/
- tooling: none: a client cannot reach the forum.
- composes with: none: replace it with a reachable index.
- reliability: The domain answers HTTP 302 to a parking host whose name does not resolve, and a public resolver returns SERVFAIL for the domain itself.
- evidence note: The client-side redirect at the domain was read by a probe on 2026-11-25; a pinned first-party read that day landed on a third-party casino registration page.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://army-of-strangers.biz/ 2026-11-03: the domain answered HTTP 302 to a ww80 host of the same domain, a parking pattern, and that host then failed to resolve | capture: sha256:e5cec32170a527547cbc09a815e568d9103dbf6e771ff16d28ae88a9f78dd885 | quote: "location": "http://ww80.army-of-strangers.biz/
  - probe:https://cloudflare-dns.com/dns-query?name=army-of-strangers.biz&type=A 2026-11-03: a public resolver answered SERVFAIL (Status 2) for the domain | capture: sha256:5713d7366bcdc97e8f5e103f5ccd9d03331e6740ba6dc9b8af56af86a525901f | quote: {"Status":2,"TC":false,"RD":true,"RA":true,"AD":false,"CD":false,"Question":[{"name":"army-of-strangers.biz","type":1}]
  - [2] 2026-11-03: third-party: the listing described a community forum sharing NZB links | capture: sha256:3125b505eca26d74096a6985446593dbb6eb97637bbd1d4543eaa49be6387223 | quote: Community-driven forum sharing NZB links, not hosting files directly.
  - probe:https://army-of-strangers.biz/ 2026-11-25: the domain answered a JavaScript redirect page on 2026-11-25, so no NZB index is served at the domain | capture: sha256:9c72f337789c39cb448db477cde41afa3ee9030a3c7459a5429d3797c496e83f | quote: window.location.replace
  - probe:https://army-of-strangers.biz/ 2026-11-25: the domain answered a client-side redirect page, with no NZB interface at the URL | capture: sha256:9c72f337789c39cb448db477cde41afa3ee9030a3c7459a5429d3797c496e83f | quote: window.location.replace
  - probe:https://army-of-strangers.biz/ 2026-11-25: a probe read a client-side redirect at the domain on 2026-11-25 | capture: sha256:9c72f337789c39cb448db477cde41afa3ee9030a3c7459a5429d3797c496e83f | quote: window.location.replace
  - probe:https://army-of-strangers.biz/ 2026-11-25: the domain served a redirect page with no NZB index on 2026-11-25 | capture: sha256:9c72f337789c39cb448db477cde41afa3ee9030a3c7459a5429d3797c496e83f | quote: window.location.replace
  - probe:https://army-of-strangers.biz/ 2026-11-25: a probe read a client-side redirect at the domain on 2026-11-25, so no NZB index is served | capture: sha256:9c72f337789c39cb448db477cde41afa3ee9030a3c7459a5429d3797c496e83f | quote: window.location.replace
  - [1] 2026-11-25: a first-party read of the domain landed on a third-party online casino with no NZB index | capture: sha256:823486495af4bdae2f8839f563e1d4c9542e30488a057595669343937b34ca8e | quote: Dive into our in-house games, live casino and slots
  - [1] 2026-11-25: the page reached at the domain offers sports betting, not an NZB index | capture: sha256:823486495af4bdae2f8839f563e1d4c9542e30488a057595669343937b34ca8e | quote: Bet on Football, Cricket, NFL, eSports
- sources:
  - [1] https://army-of-strangers.biz/
  - [2] https://nzbhydra.com/indexers/
