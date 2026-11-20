# anubis

> dataverse.nl | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-2/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseNL

- `storage/dataversenl` | fails-identity | evidence reported | binding none | category national Dataverse consortium (DANS)
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.166Z (live) | stale on 2026-12-04
- url https://dataverse.nl
- free tier: No quota defined for this collection; effectiveDatasetFileCountLimit=10000. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free | metered: no
- identity: institution | detail: Institution. 'The institutions using DataverseNL are responsible for assigning permissions to user accounts'; users 'log in with their institutional account'. Prospective depositors without a partner institution are told to 'contact your institution' or find another repository.
- interface: rest
- limits note: part of the free tier
- interface detail: REST (works even though the HTML front end is behind Anubis proof-of-work)
- tooling: REST; note the HTML UI returns an Anubis 'Making sure you're not a bot' PoW page to non-browser clients
- composes with: None. Account provisioning is manual per institution.
- reliability: API fully usable anonymously for read; the wall is account provisioning, not transport.
- notes: part of the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no quota defined (API); effectiveDatasetFileCountLimit=10000 — the highest file-count ceiling seen in the sweep
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: {"message":"No quota defined for this collection"}
  - [2] 2026-10-21: 'effectiveDatasetFileCountLimit':10000
  - [2] 2026-10-21: (description) — 'contact your institution directly ... If your institution is not in this list, and you are looking for a repository to publish research data, please contact [DANS]'
  - [3] 2026-10-21: (search snippet) — 'The institutions using DataverseNL are responsible for assigning permissions to user accounts'
  - [4] 2026-10-21: Anubis proof-of-work interstitial to non-browser clients
  - [1] 2026-11-09: the repository's quota endpoint states no quota is defined, so no numeric quota is published | capture: sha256:1e6dfdf28ff847f18a0c1fc65076c2d999e44bd819fbcf230a0889d37ae9d3c2 | quote: No quota defined for this collection
  - [1] 2026-11-19: the repository's quota API states no quota is defined | capture: sha256:1da0cd7092bf31c48c131c11004fd8244a01cf3207935d53fa7b5c01a825aef4 | quote: No quota defined for this collection
  - [2] 2026-11-19: the repository states an effective dataset file count limit of 10000 | capture: sha256:ac896ae1672e783f2340798d1324d5152279a37294af081e36f4ed1630d2f2be | quote: effectiveDatasetFileCountLimit":10000
- sources:
  - [1] https://dataverse.nl/api/dataverses/1/storage/quota?showInherited=true
  - [2] https://dataverse.nl/api/dataverses/1
  - [3] https://dans.knaw.nl/en/data-services/dataversenl/user-guide/
  - [4] https://dataverse.nl/

## anubis / techaro botstopper walls (dans, dataverse.nl, bonndata, uni-bonn,

- `storage/anubis-techaro-botstopper-walls-dans-dataverse-nl-bonnda` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:46.271Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/dataverse-2.md
- free tier: none reachable: Proof-of-work interstitial served with HTTP 200 on every HTML route. It inflates naive status-code probes: 10 hosts looked like they had an open signup form when the body was actually… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the Anubis product page states no per-object size cap | note: not applicable
- retention: stated-absent: the Anubis product page describes bot protection and states no retention period for stored bytes
- egress: stated-absent: the Anubis product page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: Anubis is a proof-of-work bot-protection layer placed in front of web applications and states no storage client interface
- tooling: not documented
- composes with: stated-absent: the Anubis product page states no way to chain byte storage with other services; it also warns that API clients and RSS readers cannot pass its proof-of-work challenge
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Proof-of-work interstitial served with HTTP 200 on every HTML route. It inflates naive status-code probes: 10 hosts looked like they had an open signup form when the body was actually…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Proof-of-work interstitial served with HTTP 200 on every HTML route. It inflates naive status-code probes: 10 hosts looked like they had an open signup form when the body was actually…
  - [1] 2026-11-19: a named host from the record is still behind the Anubis/BotStopper proof-of-work wall | capture: sha256:2268e1066fddb21b1f1fae7557beed557b5c3992d5f489fb5b5882ba128d8758 | quote: Protected by BotStopper
  - [2] 2026-11-19: Anubis is a proof-of-work bot-protection layer, not a storage service; it states no storage client interface | capture: sha256:9a899da31a68bac12485c012976913ec9f5941f107727d1a6c337cadac8b52ed | quote: Anubis uses proof-of-work challenges to stop automated abuse while letting real users through.
  - [2] 2026-11-19: the product page notes that clients unable to run JavaScript cannot pass the challenge, limiting programmatic chaining | capture: sha256:9a899da31a68bac12485c012976913ec9f5941f107727d1a6c337cadac8b52ed | quote: Use neither for network-level volumetric DDoS, or for endpoints whose clients cannot run JavaScript
- sources:
  - [1] https://dataverse.nl/
  - [2] https://techaro.lol/products.md
