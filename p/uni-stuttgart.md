# DaRUS

> uni-stuttgart.de | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uni-stuttgart/ | JSON https://fshy.ajam.dev/api/v1/entity/uni-stuttgart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DaRUS (Universität Stuttgart)

- `storage/darus` | fails-identity | evidence reported | binding none | category academic repository / Dataverse 6.12.1
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:30.233Z (live) | stale on 2026-12-04
- url https://darus.uni-stuttgart.de
- disagrees on identity_kind: `storage/darus` says institution, `storage/darus-2` says email
- disagrees on verdict: `storage/darus` says fails-identity, `storage/darus-2` says fails-quota
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted, 1.58 s. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits note: the same as the free tier
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Unlimited-by-default at 2,529 datasets and 1,007 collections, but the write path is Shibboleth-only.
- reliability: 302 to Shibboleth on account creation.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No quota defined at root.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: https://darus.uni-stuttgart.de/api/info/version — 6.12.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 302 (no native form)
  - [4] 2026-10-21: 2,529 datasets; type=dataverse — 1,007
  - [1] 2026-11-09: the root collection's storage quota endpoint states that no quota is defined for this collection | capture: sha256:b3694e9fc81b6efacb0a70fd92449689512b2cd318252e827eac5a389a458312 | quote: No quota defined for this collection
  - [1] 2026-11-19: the root collection's storage quota endpoint still states no quota is defined | capture: sha256:f13d7f2bf7b4e7486a2ad8a9ae13f48f0692d280f1317b4cfc76a459e1fb739e | quote: No quota defined for this collection
- sources:
  - [1] https://darus.uni-stuttgart.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://darus.uni-stuttgart.de/api/info/version
  - [3] https://darus.uni-stuttgart.de/dataverseuser.xhtml?editMode=CREATE
  - [4] https://darus.uni-stuttgart.de/api/search?q=*&type=dataset&per_page=1

## darus (university of stuttgart, dataverse)

- `storage/darus-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.378Z (live) | stale on 2026-12-04
- url https://www.izus.uni-stuttgart.de/fokus/darus
- disagrees on identity_kind: `storage/darus` says institution, `storage/darus-2` says email
- disagrees on verdict: `storage/darus` says fails-identity, `storage/darus-2` says fails-quota
- free tier: None reachable: Explicitly restricted to 'Mitglieder und Partner der Universität Stuttgart' (Stuttgart members and partners) and to completed research results. Not a general depositor. Technically capable. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Explicitly restricted to 'Mitglieder und Partner der Universität Stuttgart' (Stuttgart members and partners) and to completed research results — not a general depositor. Technically capable
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly restricted to 'Mitglieder und Partner der Universität Stuttgart' (Stuttgart members and partners) and to completed research results — not a general depositor. Technically capable
  - [2] 2026-10-21: cited as the basis of the rejection: Explicitly restricted to 'Mitglieder und Partner der Universität Stuttgart' (Stuttgart members and partners) and to completed research results — not a general depositor. Technically capable
  - [3] 2026-10-21: cited as the basis of the rejection: Explicitly restricted to 'Mitglieder und Partner der Universität Stuttgart' (Stuttgart members and partners) and to completed research results — not a general depositor. Technically capable
  - [1] 2026-11-19: DaRUS is restricted to Stuttgart University members and partners and to completed research results | capture: sha256:ae142b6726540618d7499d47ee03d388b89249ad085126b5bdf56bd78a6335c9 | quote: DaRUS ist der Ort für alle Mitglieder und Partner der Universität Stuttgart, um abgeschlossene Forschungsergebnisse in Form von Daten und/oder Software zu teilen, zu veröffentlichen oder zu archivieren.
- sources:
  - [1] https://www.izus.uni-stuttgart.de/fokus/darus
  - [2] https://www.izus.uni-stuttgart.de/fokus/darus/bigdata/
  - [3] https://darus.uni-stuttgart.de/api/info/version
