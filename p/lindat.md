# LINDAT/CLARIAH-CZ

> lindat.cz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lindat/ | JSON https://fshy.ajam.dev/api/v1/entity/lindat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LINDAT/CLARIAH-CZ (Charles University, UFAL) — DSpace language-data repository

- `storage/lindat-clariah-cz-dspace-language-data-repository` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T21:21:13.742Z (live) | stale on 2026-12-10
- url https://lindat.cz
- free tier: It is free and safe. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: the FAQ states the repository is free and safe but states no per-object cap on this page
- retention: We keep at least three copies, one of them off-site, at all times | source: [1] | note: The FAQ states the repository keeps at least three copies, one of them off-site, at all times.
- egress: You can download data and tools with a license that allows free sharing without any obstacles. | metered: no
- identity: institution | detail: a local account on request
- interface: rest
- limits:
  - write-gated (binding): Only authenticated users can deposit items. [1]
- limits note: Account is the gate, not bytes: you need an eduGAIN institutional login, a CLARIN account, or a manually granted local account. Files >2 GB need help-desk handling. Every deposit signs a Distribution License Agreement and must carry adequate metadata, so bulk dumping of undocumented blobs will be rejected.
- interface detail: rest
- tooling: DSpace REST/OAI-PMH plus a documented submission workflow (repository/mydspace); handles as PIDs; SWORD-style deposit contract per collection ('Distribution License Agreement'). CLARIN SPF / eduGAIN SSO, and a local account on request.
- composes with: Unlimited items per depositor x no per-item byte cap. Multiple CLARIN centres (LINDAT, CLARIN.SI, CLARIN-D, plus 20+ national nodes) each run their own DSpace with the same open door, so the chain is 'one account per centre'.
- reliability: Run by UFAL with an explicit preservation policy since 2010; stable, but the metadata/contract review and the >2 GB manual step make it a scripted-assisted path rather than a fire-and-forget API.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'It is free and safe'; 'If you don't have an academic account that works with us, let us know. We will make you a local account.'
  - [2] 2026-10-21: institutional login via eduGAIN, or CLARIN account, or local account via Help Desk
  - [3] 2026-10-21: live Deposit link to lindat.mff.cuni.cz/repository/mydspace
  - [1] 2026-11-09: the repository FAQ states that deposit is free | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: It is free and safe.
  - [1] 2026-11-09: the FAQ states the write gate is authentication | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: Only authenticated users can deposit items.
  - [1] 2026-11-09: the FAQ states downloads carry a free-sharing licence | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: You can download data and tools with a license that allows free sharing without any obstacles.
  - [1] 2026-11-09: the FAQ states a local account can be made on request | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: If you don't have an academic account that works with us, let us know. We will make you a local account.
  - [1] 2026-11-09: the FAQ states the copy and off-site policy | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: We keep at least three copies, one of them off-site, at all times
  - [1] 2026-11-09: the FAQ states institutional login is the preferred route | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: the preferred and more convenient for both you and us is logging with an institutional account
  - [1] 2026-11-19: the first-party FAQ confirms deposit is free | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: It is free and safe.
  - [1] 2026-11-19: the FAQ confirms the write gate is authentication | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: Only authenticated users can deposit items.
  - [1] 2026-11-19: the FAQ states the copy and off-site preservation policy | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: We keep at least three copies, one of them off-site, at all times
  - [1] 2026-11-19: the FAQ confirms downloads carry a free-sharing licence | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: You can download data and tools with a license that allows free sharing without any obstacles.
  - [1] 2026-11-19: the FAQ confirms institutional login is the preferred route | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: the preferred and more convenient for both you and us is logging with an institutional account
  - [1] 2026-11-25: the FAQ states the repository is free and safe | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: It is free and safe.
  - [1] 2026-11-25: the FAQ states only authenticated users can deposit items | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: Only authenticated users can deposit items. If you cannot find your home organisation in the Login dialog list of organisations then register at [clarin.eu](https://user.clarin.eu/user/register) and authenticate using "clarin.eu website account". In case you cannot use any authentication method above or if you encounter a problem, do not hesitate to contact our [Help Desk](mailto:[address removed]) and we can create a local account for you.
  - [1] 2026-11-25: the FAQ states the service is free and safe; no per-object cap is stated on this page | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: It is free and safe.
  - [1] 2026-11-25: the FAQ states three copies are kept with one off-site | capture: sha256:df96465862436fb188dc508f4abef17f6795ccf276b443ae359b1f4042f1b065 | quote: We keep at least three copies, one of them off-site, at all times
- sources:
  - [1] https://lindat.cz/faq-repository
  - [2] https://lindat.cz/faq-repository#sign-up
  - [3] https://lindat.cz
