# SimplyNZBs

> simplynzbs.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simplynzbs/ | JSON https://fshy.ajam.dev/api/v1/entity/simplynzbs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SimplyNZBs

- `debrid/simply-nzbs` | dead | evidence reported | binding write-gated | category Usenet indexer (Newznab API, closed) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:59.772Z (live) | stale on 2026-11-18
- url https://simplynzbs.com/
- free tier: None: the domain no longer hosts the indexer. A request for https://simplynzbs.com/ answers a redirect to http://ww80.simplynzbs.com/?subid1=<uuid> - the shape of a lapsed domain on a parking service - and that host name no longer resolves on 2026-11-03. A review states the service is 'no longer operational as of 2024-2025'. The last published free tier was invite-gated. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an NZB pointer file | source: [1]
- retention: last claimed 'up to 2,145 days retention' while operating; no longer served | source: [2] | note: reported, historical
- egress: none: every request is answered by a redirect to a parking host that does not respond | metered: no | source: [1]
- identity: email | detail: Was invite-only: 'weekly 50 users get 10 invites each' plus a paid bypass. Today no registration path answers.
- interface: rest
- limits:
  - request-rate: 10 API hits and 5 NZB downloads per day (historical, invite-gated) [3]
- binding note: The service is gone, so the binding constraint is the one that killed it: no reachable write path at all. Documented as write-gated because the vocabulary has no 'offline' kind and the verdict field carries that fact.
- interface detail: Was Newznab-compatible ('The SimplyNZBs API is compatible with ...' in its own invite page). Today the host redirects to a parking subdomain and /api?t=caps is answered by the same non-API redirect.
- endpoint: https://simplynzbs.com/api
- tooling: Nothing to configure: Prowlarr and NZBHydra2 cannot reach an indexer that does not answer.
- composes with: Nothing: removed from the stack.
- reliability: Dead: the name redirects to a parking host that no longer resolves; a rendered read of the domain through a pinned provider ends on a human-verification page that offers a software installer download. A client that still has it configured follows the redirect and gets no result, not an auth error.
- notes: The verdict changed while the record was being written: the first two probes returned a 504, which reads as 'down', and a later probe returned 200 on the first hop, which looked like 'up'. Reading the redirect target settled it - the 200 was a redirect to a parking service. A session that stopped at the first probe would have written a different and wrong reason.
- evidence note: The redirect to a parking subdomain was observed today, and that is strong evidence of a lapsed domain. The rung stays reported because the authoritative statement of death ('no longer operational as of 2024-2025') is third-party; the redirect alone does not date it.
- extras:
  - price: GBP 5 lifetime VIP (historical)
  - nzb_is_newznab: yes
  - death_signal: domain redirects (HTTP 302) to a parking host, ww80.simplynzbs.com, whose name no longer resolves
  - probe_sequence: an earlier request returned a 504; the later one showed the redirect. Both were kept rather than the first one reported as the truth.
- evidence:
  - probe:https://simplynzbs.com/ 2026-10-23: the request redirects to http://ww80.simplynzbs.com/?subid1=ba516fd4-ce86-11f1-9da0-c6ff21bde0c4, a parking host, which then fails with Cloudflare 520 'origin returned an unknown or empty response'
  - probe:https://simplynzbs.com/api?t=caps 2026-10-23: no Newznab document: the same redirect applies, so no API is served
  - [4] 2026-10-23: third-party: 'SimplyNZB is no longer operational as of 2024-2025'
  - [2] 2026-10-23: third-party, still listing it: 'registration closed', 'VIP GBP 5 donation', '10 hits'
  - probe:https://simplynzbs.com/ 2026-11-03: the redirect target ww80.simplynzbs.com no longer resolves (DNS failure on 2026-11-03) | capture: sha256:1fe8436a26150d4001b0cdc6f7038211fbbd9a52e7714e129d2736a4f609383d | quote: "error": "dns"
  - [1] 2026-11-03: a rendered read of simplynzbs.com ends on a page that instructs the visitor to open a downloaded installer file | capture: sha256:cb2c22e6658be21f1d8238fcd4c28e6102b326975bd142856c7d8ccc2f17a62c | quote: Then click the PrivacyKeeper.msix file
  - [4] 2026-11-03: third-party: the indexer is no longer operational as of 2024-2025 | capture: sha256:dee381f82e212e5c2c8ef0d640aebbaedf61e738cffd538a7308e042a7e701e9 | quote: Editor’s Note: SimplyNZB is no longer operational as of 2024-2025.
  - [1] 2026-11-03: the rendered read of the domain is a bot-check page that precedes an installer download, not an indexer | capture: sha256:cb2c22e6658be21f1d8238fcd4c28e6102b326975bd142856c7d8ccc2f17a62c | quote: Please verify you're not a robot
  - [4] 2026-11-03: third-party review still states the indexer is no longer operational | capture: sha256:dee381f82e212e5c2c8ef0d640aebbaedf61e738cffd538a7308e042a7e701e9 | quote: Editor’s Note: SimplyNZB is no longer operational as of 2024-2025.
- sources:
  - [1] https://simplynzbs.com/
  - [2] https://nzbhydra.com/indexers/
  - [3] https://www.cabalcartel.net/phpbb/viewtopic.php?p=15679
  - [4] https://usenetreviewz.com/simplynzb-review/
