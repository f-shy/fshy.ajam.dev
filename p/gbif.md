# GBIF IPT

> gbif.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gbif/ | JSON https://fshy.ajam.dev/api/v1/entity/gbif.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GBIF IPT via a data-hosting centre - free email account, but the payload must be biodiversity occurrences

- `storage/gbif-ipt-via-a-data-hosting-centre-free-email-account-bu` | qualifies-with-caveat | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gbif.org/data-hosting-centres
- free tier: No quota published anywhere: a data-hosting centre gives you an account on its IPT installation, and your dataset lives in that IPT's data directory. Capacity is whatever the centre provisioned; there is no per-user byte figure to quote. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public download as DwC-A; GBIF also mirrors a full monthly snapshot to AWS Open Data, Azure Planetary Computer and a public S3 bucket. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: Scope restricted to occurrence, checklist, and sampling-event data in Darwin Core format. Registration is coordinated by contacting the data centre or GBIF helpdesk. No explicit byte cap is stated in published documentation.
- interface detail: rest
- tooling: IPT web UI plus its REST resource endpoints; publishing to GBIF mints a DOI. VertNet (vertebrates), VLIZ/EurOBIS (marine, 20+ IPT instances), BioFresh (freshwater) are the listed centres.
- composes with: Per dataset within a centre's IPT; multiple datasets are allowed, but reviewers police relevance, so this does not shard.
- reliability: Long-lived EU-funded centres with backed-up IPT data directories; the IPT is a metadata+archive publisher, not an object store, and it re-packages rather than serving your original bytes.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'A data-hosting centre (DHC) can provide users with an account on their IPT installation'; requirements list includes 'Ensuring the IPT data directory is regularly backed up'
  - [1] 2026-10-21: 'request a free account on a trusted data hosting centre'; demo IPT account by email to [address removed]
  - [3] 2026-10-21: live list of 20+ hosted IPT instances (EurOBIS, OBIS nodes, ISA, IBSS, ILVO)
  - [4] 2026-10-21: 200, live VertNet IPT resource table
- sources:
  - [1] https://ipt.gbif.org/manual/en/ipt/latest/
  - [2] https://www.gbif.org/data-hosting-centres
  - [3] https://ipt.vliz.be/
  - [4] https://ipt.vertnet.org/

## gbif

- `storage/gbif` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://api.gbif.org/v1/occurrence/download/request
- free tier: none reachable: Publishes Darwin Core occurrences and derived download archives, not arbitrary blobs. Anonymous download requests are refused (403), and the synchronous API caps at 100,000 records. The… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Publishes Darwin Core occurrences and derived download archives, not arbitrary blobs. Anonymous download requests are refused (403), and the synchronous API caps at 100,000 records. The…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Publishes Darwin Core occurrences and derived download archives, not arbitrary blobs. Anonymous download requests are refused (403), and the synchronous API caps at 100,000 records. The IP
  - [2] 2026-10-21: cited as the basis of the rejection: Publishes Darwin Core occurrences and derived download archives, not arbitrary blobs. Anonymous download requests are refused (403), and the synchronous API caps at 100,000 records. The IP
  - [3] 2026-10-21: cited as the basis of the rejection: Publishes Darwin Core occurrences and derived download archives, not arbitrary blobs. Anonymous download requests are refused (403), and the synchronous API caps at 100,000 records. The IP
- sources:
  - [1] https://api.gbif.org/v1/occurrence/download/request
  - [2] https://www.gbif.org/faq
  - [3] https://www.gbif.org/ipt
