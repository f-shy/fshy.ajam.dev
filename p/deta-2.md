# Deta

> Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deta-2/ | JSON https://fshy.ajam.dev/api/v1/entity/deta-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deta

- `egress/deta` | dead | evidence reported | binding volume-quota | category paas l4 port | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://news.ycombinator.com/item?id=41426388
- price USD 0
- free tier: Deta Space is shutting down and will be sunset on 17 October 2024. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No service; Deta Space was sunset on 2024-10-17.; ingress: none | metered: yes | free allowance: No service; Deta Space was sunset on 2024-10-17. | source: [1]
- identity: email | detail: Not applicable; the hosting product no longer exists. | country: None
- interface: unknown
- limits:
  - volume-quota (binding): service sunset 2024-10-17 [1]
- binding note: No service, so no constraint applies.
- interface detail: No live interface.
- tooling: None.
- composes with: Not available.
- reliability: Service withdrawn; data deleted after sunset.
- notes: Deta Cloud and Space cloud runtime services are discontinued. Successor products focus on personal computing environments rather than application hosting.
- evidence note: Discontinuation documented in vendor communications and repository issues. Deta endpoints returned HTTP 530 during verification.
- extras:
  - wg_path: none
  - wg_detail: No service remains to expose a port. Both deta.space and deta.sh returned HTTP 530.
  - ingress: none
  - volume_tib_month: 0
  - volume_stated: No service; Deta Space was sunset on 2024-10-17.
  - bytes_transit: no
  - transit_note: No service.
- evidence:
  - [1] 2026-10-23: "Deta Space is shutting down and will be sunset on 17 October 2024"
  - [2] 2026-10-23: quotes Deta: login for 45 days until sunset on October 17, 2024, then deletion of Horizons, apps and data
  - [3] 2026-10-23: HTTP 530
- sources:
  - [1] https://news.ycombinator.com/item?id=41426388
  - [2] https://github.com/withastro/docs/pull/9345
  - [3] https://deta.space/
