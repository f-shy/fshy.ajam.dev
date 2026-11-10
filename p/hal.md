# HAL

> hal.science | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hal/ | JSON https://fshy.ajam.dev/api/v1/entity/hal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HAL (Hyper Articles en Ligne, CCSD / CNRS)

- `storage/hal` | fails-quota | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hal.science
- free tier: 200 MB maximum per file in the deposit UI, plus a 5 GB per-account FTP staging space that is provisional only: 'pour une durée provisoire pouvant aller jusqu'à 31 jours maximum'. No aggregate storage quota is published. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 200 MB maximum per file | bytes: 200000000 | source: [1] | note: not stated
- retention: | Very stable national infrastructure (CCSD/CNRS) with permanent URLs, but the per-file 200 MB cap and the bibliographic-record model make it useless for bulk blobs; the 5 GB FTP space decays in 31 days. | days: 31 | source: [1] | note: not stated
- egress: Free public PDF/fulltext download, no metering; metadata is harvested by OpenAIRE, BASE, Google Scholar. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, ftp
- limits:
  - per-ip-shaping: transfer is limited to 3 MB/file and 10 MB total [1]
  - per-object-cap (binding): 3 MB/file [1]
  - per-object-cap (binding): 200 MB cap [1]
- limits note: Per-object-cap 200 MB (soft, varies with traffic); FTP staging 5 GB / 31 days; the deposit must be a scholarly document with a document type, so raw data blobs are out of scope. arXiv transfer is limited to 3 MB/file and 10 MB total.
- interface detail: rest
- tooling: Deposit API + SWORD for programmatic submission (api.archives-ouvertes.fr/docs), FTP staging at ftp.ccsd.cnrs.fr with explicit TLS (FileZilla), OAI-PMH, and a TripleStore. This is a genuinely automatable write path.
- composes with: Unlimited deposits x 200 MB/file. 2,500 files for 500 GB, but each deposit is a bibliographic notice, so the multiplier is records not blobs. 5 GB FTP staging expires in 31 days.
- reliability: Very stable national infrastructure (CCSD/CNRS) with permanent URLs, but the per-file 200 MB cap and the bibliographic-record model make it useless for bulk blobs; the 5 GB FTP space decays in 31 days.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200 MB maximum per file in the deposit UI, plus a 5 GB per-account FTP staging space that is provisional only: 'pour une durée provisoire pouvant aller jusqu'à 31 jours maximum'. No aggregate storage quota is published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'La taille maximum d'un fichier est de 200Mo'; mentions the FTP staging space as the alternative route for larger sets
  - [2] 2026-10-21: 'Chaque compte utilisateur dispose d'un espace de 5 Go sur le serveur FTP du CCSD... pour une durée provisoire pouvant aller jusqu'à 31 jours maximum'
  - [1] 2026-10-21: arXiv transfer capped at 3 MB per file / 10 MB total
- sources:
  - [1] https://doc.hal.science/en/faq/
  - [2] https://doc.hal.science/en/gerer-ses-depots/espace-de-stockage-ftp/
