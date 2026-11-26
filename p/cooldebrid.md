# CoolDebrid

> cooldebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cooldebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/cooldebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoolDebrid

- `debrid/cooldebrid` | dead | evidence documented | binding none | category multi-hoster debrid with torrent streaming (closed) | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:55.563Z (live) | stale on 2026-12-26
- url https://cooldebrid.com/
- free tier: None surviving: the site returns 404 on every path tried, so no current offer exists to quote. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the service is gone | source: [1]
- retention: not applicable: the service is gone | source: [1]
- egress: No terms reachable: the origin answers 404. | metered: no | source: [1]
- identity: email | detail: As archived: 'Log in to your account', so an account existed. Not reachable today.
- interface: unknown
- limits note: not applicable
- binding note: A dead service binds nothing; the record exists to carry the date of death.
- interface detail: As archived in 2024: a login-based download manager with torrent streaming ('Stream Torrents with cooldebrid'). Nothing is served today.
- tooling: none: the domain serves a 404
- composes with: Nothing to chain: preserved so the subsequent audit does not spend a wave re-finding it, and so a comparison site that still lists it can be discounted.
- reliability: Dead: the root returns HTTP 404 as of today. The Wayback capture of 2024-06-01 shows it live and selling a 'Premium Download Manager' with torrent streaming.
- notes: Found through an Italian-language query ('servizio debrid'), which is why the English lists never carried it. The 404 is the whole finding: no parked page, no redirect, no explanation.
- evidence note: Two dated observations: the 404 today and the 2024-06-01 capture. The date of closure is not established - only that it was alive in June 2024 and is 404 in October 2026.
- evidence:
  - probe:https://cooldebrid.com/ 2026-10-23: HTTP 404 with 'The document has no body element to read'; a HEAD request also returned 404
  - [2] 2026-10-23: the service was alive on 2024-06-01: title 'Log in to your account', description 'cooldebrid is a Premium Download Manager. Get files at premium speeds from all filehosts. Stream Torrents with cooldebrid.'
  - probe:https://cooldebrid.com/ 2026-11-25: an anonymous GET of the root on 2026-11-25 answered 200 with 45102 bytes and no challenge, so the previously recorded 404 is no longer the current state | capture: sha256:a8a71faab8972d51ecc0407082ed91b0da43b2ce3bac433161aa79b5ab76bfa2 | quote: "status": 200,
  - [1] 2026-11-25: the root now serves a live premium link generator page advertising 63 supported filehosts | capture: sha256:606df2097cadc0773ef67e088d5dd3c2a2212a8d718b4cc6e5a4227b09e298ba | quote: CoolDebrid Premium Link Generator — 63 Supported Filehosts
- sources:
  - [1] https://cooldebrid.com/
  - [2] https://web.archive.org/web/20240601173729/https://cooldebrid.com/?provider=wayback
