# AUSSDA Dataverse

> aussda.at | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aussda/ | JSON https://fshy.ajam.dev/api/v1/entity/aussda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AUSSDA Dataverse (Austrian Social Science Data Archive, University of Vienna)

- `storage/aussda-dataverse` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.aussda.at
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted, 1.92 s. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published per-file cap; no quota number returned.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Same open pattern as Borealis, smaller corpus, same lack of a bound.
- reliability: No published SLA; app-tier /api/admin/settings/ returned 403 rather than 404 here, i.e. admin surface is firewalled but the app is not.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://data.aussda.at/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
- sources:
  - [1] https://data.aussda.at/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://data.aussda.at/api/info/version
  - [3] https://data.aussda.at/dataverseuser.xhtml?editMode=CREATE

## aussda (austria)

- `storage/aussda` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true
- free tier: none reachable: Self-deposit is limited to researchers at partner universities (Vienna, Graz, Linz, Innsbruck, Salzburg, Krems, WU, OeAW) who sign an archive contract. Not an open door despite 'no quota… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
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
- sources:
  - [1] https://data.aussda.at/api/dataverses/1/storage/quota?showInherited=true
  - [2] https://www.aussda.at/en/deposit-data/
  - [3] https://www.aussda.at/en/news-details/news/university-of-klagenfurt-joins-aussda-consortium/
