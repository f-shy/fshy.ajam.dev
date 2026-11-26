# AUSSDA Dataverse

> aussda.at | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aussda/ | JSON https://fshy.ajam.dev/api/v1/entity/aussda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AUSSDA Dataverse (Austrian Social Science Data Archive, University of Vienna)

- `storage/aussda-dataverse` | qualifies-with-caveat | evidence reported | binding none | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-11-25T03:33:12.195Z (live) | stale on 2026-12-10
- url https://data.aussda.at
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: The re-read root-collection quota endpoint states only a quota value and publishes no per-object size cap; a per-object cap is unverified.
- retention: source: [1] | note: The first-party quota endpoint was re-read on 2026-11-25 and states only a root-collection quota; it publishes no retention period. Retention is unverified beyond the absence of a published clause.
- egress: Cloudflare-fronted, 1.92 s. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published per-file cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Same open pattern as Borealis, smaller corpus, same lack of a bound.
- reliability: No published SLA; app-tier /api/admin/settings/ returned 403 rather than 404 here, i.e. admin surface is firewalled but the app is not.
- notes: The quota endpoint states "No quota defined for this collection".
- evidence:
  - [2] 2026-10-21: https://data.aussda.at/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
  - [1] 2026-11-09: the repository's own quota endpoint states that no quota is defined for the root collection | capture: sha256:28e17c84f0519becfb637fe69a951313ba5c1eb6027ac2bc9aaeabcaa90f2535 | quote: No quota defined for this collection
  - [1] 2026-11-09: the repository's quota endpoint states that no quota is defined for the collection | capture: sha256:2f1211ab7fcbb3cd55eafde7ee550a9181347f409c77254b1cfcd68f1ee71e59
  - [1] 2026-11-19: the root collection has no storage quota defined | capture: sha256:8830c7ceefb9a4c090d0b7015fbbe74e200abb25f3032bf4a17d85ecccc049f9
  - [1] 2026-11-25: the quota endpoint reports the root collection's quota and states no retention period | capture: sha256:53ab62027431170ca359185c334ea294f526f85778cc13d3487764b7d5c11d88
  - [1] 2026-11-25: the quota endpoint reports the root collection's quota and states no per-object size cap | capture: sha256:53ab62027431170ca359185c334ea294f526f85778cc13d3487764b7d5c11d88
  - [1] 2026-11-25: the root collection has no storage quota defined, still after this re-read | capture: sha256:53ab62027431170ca359185c334ea294f526f85778cc13d3487764b7d5c11d88
- sources:
  - [1] https://data.aussda.at/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://data.aussda.at/api/info/version
  - [3] https://data.aussda.at/dataverseuser.xhtml?editMode=CREATE

## aussda (austria)

- `storage/aussda` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:56.064Z (live) | stale on 2026-12-04
- url https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true
- free tier: none reachable: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true | source: [1] | note: not applicable
- retention: not stated on https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true | source: [1]
- egress: not stated on https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true | metered: no
- identity: email
- interface: unknown
- interface detail: not stated on https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true
- tooling: not documented
- composes with: the same as interface detail
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota…
  - [2] 2026-10-21: cited as the basis of the rejection: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota def
  - [3] 2026-10-21: cited as the basis of the rejection: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota def
  - [1] 2026-11-19: the endpoint body contains only a quota message and states no client interface | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the endpoint body states no client interface | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the endpoint returns only a quota message and states no retention period | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the endpoint returns only a quota message and states no per-object cap | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the endpoint returns only a quota message and states no chaining mechanism | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the endpoint returns only a quota message and states no egress price or traffic quota | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
  - [1] 2026-11-19: the first-party quota endpoint was re-read and returned only the quota message | capture: sha256:63b9470d2727c6e321adf3f1da21a3e898b9f42f93fc0aff2befa141258a62c7
- sources:
  - [1] https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true
  - [2] https://www.aussda.at/en/deposit-data/
  - [3] https://www.aussda.at/en/news-details/news/university-of-klagenfurt-joins-aussda-consortium/
