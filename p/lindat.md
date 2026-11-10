# LINDAT/CLARIAH-CZ

> lindat.cz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lindat/ | JSON https://fshy.ajam.dev/api/v1/entity/lindat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LINDAT/CLARIAH-CZ (Charles University, UFAL) — DSpace language-data repository

- `storage/lindat-clariah-cz-dspace-language-data-repository` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://lindat.cz
- free tier: Deposit is free with no published byte ceiling ('It is free and safe'); the only stated object limit is operational. CLARIN-family DSpace instances handle files above 2 GB by special arrangement rather than refusing them. Individual deposited corpora routinely run to tens of GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Public items download without login; licence-gated items need an account and an e-signed licence. No metering, no egress pricing. This is a national research-infrastructure node. | metered: no
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): review and the >2 GB manual step make it a scripted-assisted path rather than a fire-a [1]
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
- sources:
  - [1] https://lindat.cz/faq-repository
  - [2] https://lindat.cz/faq-repository#sign-up
  - [3] https://lindat.cz
