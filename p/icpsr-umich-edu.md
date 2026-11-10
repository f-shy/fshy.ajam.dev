# ICPSR Consortium Archive

> icpsr.umich.edu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/icpsr-umich-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/icpsr-umich-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ICPSR Consortium Archive (curated deposit path)

- `storage/icpsr-consortium-archive` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.icpsr.umich.edu
- free tier: No published byte cap on the curated path; ICPSR states 'Anyone can deposit data into ICPSR's Consortium Archive at no cost' and covers curation from membership fees. Size is negotiated per study rather than metered. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free to users at member institutions; fee-gated for non-members unless the depositor buys five years of open access. That asymmetry is why this ranks below openICPSR. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: s3, rest, webdav
- limits note: Human curation gate before release (weeks to months), plus the read-side membership paywall. Not self-service and not usable as working storage.
- interface detail: rest
- tooling: Deposit via ICPSR's submission pipeline and the openICPSR front end; DOIs via DataCite; long-term preservation with redundant backups and format migration. No S3/WebDAV surface.
- composes with: Unlimited studies per depositor, each negotiated for size; curation is the throttle, not quota.
- reliability: The most durable option in this space (60+ years, DOI maintenance guaranteed), but the slowest to write to and the read path can be paywalled.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Anyone can deposit data into ICPSR's Consortium Archive at no cost. ICPSR covers curation costs with membership fees.'
  - [2] 2026-10-21: DOI, usage reports, long-term preservation commitments
- sources:
  - [1] https://www.icpsr.umich.edu/sites/shared/posts/deposit-options
  - [2] https://www.icpsr.umich.edu/sites/icpsr/manage-data/deposit
