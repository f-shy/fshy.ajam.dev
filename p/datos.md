# datos.gob.es

> datos.gob.es | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datos/ | JSON https://fshy.ajam.dev/api/v1/entity/datos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## datos.gob.es (Spain)

- `storage/datos-gob-es` | fails-quota | evidence inferred | binding none | category gov-ckan-portal
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://datos.gob.es/
- free tier: Not machine-readable from here. CKAN action API returns 403 behind the WAF; the public catalogue is harvested from ministry and regional nodes. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: public. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: The registration form renders (HTTP 200, 'Crear nueva cuenta'), but datos.gob.es is an aggregator of Aporta-harvested regional/state nodes, not a host: the file always lives on the publishing body's own server. Even a successful account would not hold bytes.
- interface detail: CKAN-derived but API blocked.
- tooling: curl (blocked).
- composes with: n/a.
- reliability: unverified on quota: API 403 to this IP. Aggregator architecture is documented, so the hosting verdict stands regardless.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Not machine-readable from here — CKAN action API returns 403 behind the WAF; the public catalogue is harvested from ministry and regional nodes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: HTTP 403
  - [3] 2026-10-21: HTTP 200, form title 'Crear nueva cuenta'
- sources:
  - [1] https://datos.gob.es/
  - [2] https://datos.gob.es/api/3/action/package_search?rows=0
  - [3] https://datos.gob.es/user/register
