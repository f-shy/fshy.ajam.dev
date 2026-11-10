# a media

> advanced360.top | Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/advanced360/ | JSON https://fshy.ajam.dev/api/v1/entity/advanced360.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## a media instance behind a JavaScript cookie gate (alist.advanced360.top)

- `netdisk-pan/alist-advanced360-top` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://alist.advanced360.top/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; JS-cookie interstitial | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): the host stopped serving: JS-cookie interstitial probe:https://alist.advanced360.top/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Death mode: JS-cookie interstitial.
- notes: a media instance behind a JavaScript cookie gate. JS-cookie interstitial
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - death_mode: JS-cookie interstitial
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
  - first_seen: 2024-01-20
- evidence:
  - probe:https://alist.advanced360.top/api/public/settings 2026-10-22: HTTP 200 with a 502-byte body: <title>Loading...</title> and window.location.replace() to the same URL carrying ch=1&js=<JWT>; it is neither JSON nor a page, and the SHA-256 of the body is 770fedcf5d7b62a606978c08b3753fb6ed3c90e6fcae1cb9ecd45fc8e5b88992
- sources:
  - [1] https://alist.advanced360.top/

## media.advanced360.top

- `netdisk-pan/media-advanced360-top` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://media.advanced360.top/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; 302 to a host whose TLS fails | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): the host stopped serving: 302 to a host whose TLS fails probe:https://media.advanced360.top/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Death mode: 302 to a host whose TLS fails.
- notes: A media mirror. 302 to a host whose TLS fails
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - death_mode: 302 to a host whose TLS fails
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
  - first_seen: 2024-01-20
- evidence:
  - probe:https://media.advanced360.top/api/public/settings 2026-10-22: HTTP 302 to ww547.advanced360.top, whose TLS handshake then fails; the pinned notice about excess use and this redirect are the two ends of the same shutdown
- sources:
  - [1] https://media.advanced360.top/
