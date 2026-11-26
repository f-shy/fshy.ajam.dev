# Zlion

> zlion.top | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zlion/ | JSON https://fshy.ajam.dev/api/v1/entity/zlion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zlion, a film and anime instance whose WebDAV was withdrawn for excess use (alist.zlion.top)

- `netdisk-pan/alist-zlion-top` | dead | evidence measured | binding retention-clamped | category public-instance
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:58:42.229Z (live) | stale on 2026-12-18
- url https://alist.zlion.top/
- free tier: nothing reachable: the host does not serve an anonymous mount list | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; nothing is readable | source: [1]
- retention: the host is gone; no TCP service | days: 0 | source: [1]
- egress: nothing to serve | metered: no | source: [1]
- identity: anonymous | detail: no account would have helped
- interface: unknown
- limits:
  - retention-clamped (binding): 若发现下载行为过多，将直接关停本站 probe:https://alist.zlion.top/api/public/settings
- binding note: The host is not slow or capped, it is gone; the constraint is that it stopped.
- tooling: none: no client reaches it
- composes with: excluded
- reliability: Anonymous JSON listing of 5 root directories returned by the AList API on a fresh probe; guest session with permission 0; the earlier no-TCP-service state is not observed at this check.
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
  - probe:https://alist.zlion.top/api/fs/list 2026-11-19: an anonymous GET /api/fs/list returns a success JSON body with five root directory entries | capture: sha256:f83a2b41538ad56169e22b473c563154efc582ab733fca2f07335534d4c38c61 | quote: "total":5
  - probe:https://alist.zlion.top/api/fs/list 2026-11-19: the read path now returns an anonymous listing of five root directories | capture: sha256:f83a2b41538ad56169e22b473c563154efc582ab733fca2f07335534d4c38c61 | quote: "total":5
  - probe:https://alist.zlion.top/api/me 2026-11-19: the session is anonymous: /api/me returns a guest user with permission 0 and no account requirement | capture: sha256:7ff3ac9d0c289a36e4ea6bc73e4cec8b627c6d6738ee1e86ef31971bfa3dd40d | quote: "username":"guest"
  - probe:https://alist.zlion.top/api/public/settings 2026-11-19: the host answers the AList settings API with title Zlion and version v4.2.9 | capture: sha256:ceec46d0e235b0c6f9d72d15a9c1cb6b2e8979850e37eb34adb282ce6be43dff | quote: "site_title":"Zlion"
  - probe:https://alist.zlion.top/api/fs/list 2026-11-26: the saved anonymous fs/list body carries this notice | capture: sha256:f83a2b41538ad56169e22b473c563154efc582ab733fca2f07335534d4c38c61 | quote: 若发现下载行为过多，将直接关停本站
  - probe:https://alist.zlion.top/api/fs/list 2026-11-26: the readme field of the anonymous fs/list body contains this exact sentence | capture: sha256:f83a2b41538ad56169e22b473c563154efc582ab733fca2f07335534d4c38c61 | quote: 若发现下载行为过多，将直接关停本站
- sources:
  - [1] https://alist.zlion.top/
