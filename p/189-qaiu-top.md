# 189.qaiu.top

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/189-qaiu-top/ | JSON https://fshy.ajam.dev/api/v1/entity/189-qaiu-top.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 189.qaiu.top — netdisk-fast-download '专业版' (baidu/xunlei/quark/uc/139/189/w

- `storage/189-qaiu-top-netdisk-fast-download-baidu-xunlei-quark-uc` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:46.270Z (inherited) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/189-qaiu-top.md
- free tier: None reachable: a direct probe of /parser now answers HTTP 401 '未提供API Key（请在请求头X-API-Key或URL参数token中提供）' - an API key in the X-API-Key header or a token URL parameter is required on every call. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party HTTP endpoint does not state a per-object cap; it answered HTTP 500 on the settings path | note: not applicable
- retention: stated-absent: the first-party HTTP endpoint does not state a retention period; it answered HTTP 500 on the settings path
- egress: stated-absent: the first-party HTTP endpoint does not state egress terms; its settings path answered HTTP 500 | metered: no
- identity: email
- interface: rest
- interface detail: stated-absent: the first-party host exposes an HTTP API path but the settings endpoint answered HTTP 500, so no client interface is documented
- tooling: not documented
- composes with: stated-absent: the first-party HTTP endpoint does not state how it chains with other services; its settings path answered HTTP 500
- reliability: AUTH-REQUIRED and paid. This is the tier that actually covers Baidu Pan, Quark, UC, 139, 189 and Unicom. Precisely the pans the free tier omits. Every /parser call returns HTTP 401 '未提供API.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: AUTH-REQUIRED and paid. This is the tier that actually covers Baidu Pan, Quark, UC, 139, 189 and Unicom — precisely the pans the free tier omits. Every /parser call returns HTTP 401 '未提供API
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: AUTH-REQUIRED and paid. This is the tier that actually covers Baidu Pan, Quark, UC, 139, 189 and Unicom — precisely the pans the free tier omits. Every /parser call returns HTTP 401 '未提供API
  - probe:https://189.qaiu.top/parser?url=https%3A%2F%2Fpan.baidu.com%2Fs%2Fabc 2026-11-19: every /parser call is now refused with HTTP 401 unless an API key is supplied | capture: sha256:ad3526a3fea3768666f57238ad152d74a41879cca82bf815caf1200875d7101f | quote: 未提供API Key（请在请求头X-API-Key或URL参数token中提供）
  - probe:https://189.qaiu.top/api/public/settings 2026-11-19: the first-party host exposes an HTTP API path, but the probed endpoint returned no usable interface documentation | capture: sha256:da5c938b74b82adccf9234e3f478878a0e28dd6f6e951b7f5ae7b69489d9bfc5 | quote: "status": 500
