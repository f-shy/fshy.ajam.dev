# an instance from the 2024 cohort

> t-satoru.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-satoru/ | JSON https://fshy.ajam.dev/api/v1/entity/t-satoru.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## an instance from the 2024 cohort (pan.t-satoru.top)

- `netdisk-pan/pan-t-satoru-top` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-13
- url https://pan.t-satoru.top/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; challenge page | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): the host stopped serving: challenge page probe:https://pan.t-satoru.top/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Death mode: challenge page.
- notes: an instance from the 2024 cohort. challenge page
- extras:
  - access_mode: public-instance
  - read_capability: none
  - write_capability: not-tested
  - death_mode: challenge page
  - last_verified_dead: 2026-10-22T03:37:00.574Z
  - consecutive_failures: 1
  - first_seen: 2024-01-20
- evidence:
  - probe:https://pan.t-satoru.top/api/public/settings 2026-10-22: HTTP 403 with an interstitial body from an automated-traffic filter; the host is behind a challenge that no fetch path passed, so its capability is unestablished and it is unusable as a substrate
- sources:
  - [1] https://pan.t-satoru.top/
