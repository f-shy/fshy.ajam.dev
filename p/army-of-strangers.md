# Army of Strangers

> army-of-strangers.biz | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/army-of-strangers/ | JSON https://fshy.ajam.dev/api/v1/entity/army-of-strangers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Army of Strangers

- `debrid/army-of-strangers` | dead | evidence measured | binding none | category Usenet NZB link forum (redirects to a parking host) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://army-of-strangers.biz/
- free tier: none: the domain redirects to a parking host that does not resolve. A third-party listing described a community forum sharing NZB links with open registration. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: nothing is served | source: [1]
- retention: not applicable: the forum is unreachable | source: [1]
- egress: none: the domain redirects to a parking host that does not resolve | metered: no | source: [1]
- identity: email | detail: unverified: the register page cannot be reached; a third-party listing called registration open and said a VPN must be disabled at signup.
- interface: unknown
- limits:
  - request-rate: none applicable: the domain redirects to a parking host probe:https://army-of-strangers.biz/
- binding note: The domain no longer serves the forum, so no limit is reachable.
- interface detail: none reachable: a request answered HTTP 302 to a parking host (ww80 subdomain of the same domain) whose name then failed to resolve.
- endpoint: https://army-of-strangers.biz/
- tooling: none: a client cannot reach the forum.
- composes with: none: replace it with a reachable index.
- reliability: The domain answers HTTP 302 to a parking host whose name does not resolve, and a public resolver returns SERVFAIL for the domain itself.
- evidence note: The redirect and the resolver failure were read; that the redirect target is a parking page is inferred from its name and the failed resolution, not read.
- extras:
  - price: unverified: unreachable
- evidence:
  - probe:https://army-of-strangers.biz/ 2026-11-03: the domain answered HTTP 302 to a ww80 host of the same domain, a parking pattern, and that host then failed to resolve | capture: sha256:e5cec32170a527547cbc09a815e568d9103dbf6e771ff16d28ae88a9f78dd885 | quote: "location": "http://ww80.army-of-strangers.biz/
  - probe:https://cloudflare-dns.com/dns-query?name=army-of-strangers.biz&type=A 2026-11-03: a public resolver answered SERVFAIL (Status 2) for the domain | capture: sha256:5713d7366bcdc97e8f5e103f5ccd9d03331e6740ba6dc9b8af56af86a525901f | quote: {"Status":2,"TC":false,"RD":true,"RA":true,"AD":false,"CD":false,"Question":[{"name":"army-of-strangers.biz","type":1}]
  - [2] 2026-11-03: third-party: the listing described a community forum sharing NZB links | quote: Community-driven forum sharing NZB links, not hosting files directly.
- sources:
  - [1] https://army-of-strangers.biz/
  - [2] https://nzbhydra.com/indexers/
