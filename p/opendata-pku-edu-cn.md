# peking university open research data platform

> opendata.pku.edu.cn | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opendata-pku-edu-cn/ | JSON https://fshy.ajam.dev/api/v1/entity/opendata-pku-edu-cn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## peking university open research data platform (opendata.pku.edu.cn)

- `storage/peking-university-open-research-data-platform` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:56.425Z (live) | stale on 2026-12-04
- url https://opendata.pku.edu.cn/api/info/version
- free tier: none reachable: A Harvard-Dataverse fork ('基于哈佛大学 Dataverse 框架二次开发') with a real deposit flow, but the API and handbook both return 403 to a foreign client and the platform is aimed at PKU and Chinese… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Beta stage: only authenticated Peking University users may create and publish data; access to other data may require real identity information and manager approval.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: A Harvard-Dataverse fork ('基于哈佛大学 Dataverse 框架二次开发') with a real deposit flow, but the API and handbook both return 403 to a foreign client and the platform is aimed at PKU and Chinese…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A Harvard-Dataverse fork ('基于哈佛大学 Dataverse 框架二次开发') with a real deposit flow, but the API and handbook both return 403 to a foreign client and the platform is aimed at PKU and Chinese…
  - [2] 2026-10-21: cited as the basis of the rejection: A Harvard-Dataverse fork ('基于哈佛大学 Dataverse 框架二次开发') with a real deposit flow, but the API and handbook both return 403 to a foreign client and the platform is aimed at PKU and Chinese resea
  - [1] 2026-11-19: first-party handbook states only authenticated PKU users may create and publish data in the beta stage | capture: sha256:5a8e32daa886f0e138def2d8ecc7ae00a99f2ee433a8e83f6419797a2916e857 | quote: 【Beta 测试阶段】 北大数据平台暂时只支持本校的认证用户创建和发布数据。
  - [1] 2026-11-19: the platform is a Harvard Dataverse fork | capture: sha256:5a8e32daa886f0e138def2d8ecc7ae00a99f2ee433a8e83f6419797a2916e857 | quote: 北大数据平台基于哈佛大学 Dataverse 框架二次开发而成。
  - probe:https://opendata.pku.edu.cn/api/info/version 2026-11-19: the API endpoint answered HTTP 403 on 2026-11-19 | capture: sha256:baa9ee94556e150aaeb66a766a867b14b38f5103b50239011cbfe32b677b7cdd | quote: "status": 403
- sources:
  - [1] https://opendata.pku.edu.cn/api/info/version
  - [2] https://opendata.pku.edu.cn/handbook.xhtml
