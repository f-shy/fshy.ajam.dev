# Zlion

> zlion.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zlion/ | JSON https://fshy.ajam.dev/api/v1/entity/zlion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zlion, a film and anime instance whose WebDAV was withdrawn for excess use (alist.zlion.top)

- `netdisk-pan/alist-zlion-top` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://alist.zlion.top/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; no TCP service | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): the host stopped serving: no TCP service probe:https://alist.zlion.top/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Death mode: no TCP service.
- notes: Zlion instance with media collections where WebDAV access is inactive due to excessive bandwidth utilization. TCP service is offline.
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - death_mode: no TCP service
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
  - first_seen: 2024-01-20
- evidence:
  - probe:https://alist.zlion.top/api/public/settings 2026-10-22: curl returned 000 with a TLS handshake failure, so nothing is listening on 443; the community index records that its WebDAV was closed before the host itself went away
- sources:
  - [1] https://alist.zlion.top/
