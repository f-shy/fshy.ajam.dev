# UCLouvain Dataverse

> uclouvain.be | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uclouvain/ | JSON https://fshy.ajam.dev/api/v1/entity/uclouvain.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UCLouvain Dataverse (Open Data @ UCLouvain)

- `storage/uclouvain-dataverse` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.x
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:20.587Z (live) | stale on 2026-12-04
- url https://dataverse.uclouvain.be
- free tier: Each research Institute that requests it has 1 Tb free of charge. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1] | note: Each research Institute that requests it has 1 Tb free of charge.
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - volume-quota: 1 Tb free of charge per research institute that requests it [2]
- limits note: For larger datasets > 1Tb a financial contribution will be requested : you will have to pay 33.3 euros/TB/year (500 euros/TB for a period of 15 years).
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Another open-signup, no-quota national instance.
- reliability: Login page advertises both institutional and native login.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200
  - [4] 2026-10-21: offers institutional login plus builtin
  - [2] 2026-11-09: the university's UCLouvain Dataverse page states each research institute that requests it has 1 Tb free of charge | capture: sha256:ca1032174d36a387ca426288889e8b657b8af034e777b9b08982e92bd7c28376 | quote: Each research Institute that requests it has 1 Tb free of charge.
  - [2] 2026-11-09: the page states that datasets above 1 Tb are charged EUR 33.3 per TB per year, or EUR 500 per TB for 15 years | capture: sha256:ca1032174d36a387ca426288889e8b657b8af034e777b9b08982e92bd7c28376 | quote: For larger datasets > 1Tb a financial contribution will be requested : you will have to pay 33.3 euros/TB/year (500 euros/TB for a period of 15 years).
  - [1] 2026-11-09: the root collection's quota endpoint reports no quota object | capture: sha256:7a2577d46ff3e397d4decb37ee9587e2f94e062ea3d5d3443d18e5c5208acfe0 | quote: No quota defined for this collection
  - [2] 2026-11-19: the 1 Tb free allowance per research institute is unchanged | capture: sha256:ca1032174d36a387ca426288889e8b657b8af034e777b9b08982e92bd7c28376 | quote: Each research Institute that requests it has 1 Tb free of charge.
  - [2] 2026-11-19: the over-quota charge remains 33.3 EUR/TB/year | capture: sha256:ca1032174d36a387ca426288889e8b657b8af034e777b9b08982e92bd7c28376 | quote: For larger datasets > 1Tb a financial contribution will be requested : you will have to pay 33.3 euros/TB/year (500 euros/TB for a period of 15 years).
- sources:
  - [1] https://dataverse.uclouvain.be/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://uclouvain.be/en/university-libraries/uclouvain-dataverse
  - [3] https://dataverse.uclouvain.be/dataverseuser.xhtml?editMode=CREATE
  - [4] https://dataverse.uclouvain.be/loginpage.xhtml
