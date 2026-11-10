# EPrints 3.x platform class

> eprints.whiterose.ac.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eprints-whiterose-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/eprints-whiterose-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EPrints 3.x platform class (White Rose, QUT, Southampton)

- `storage/eprints-3-x-platform-class` | fails-identity | evidence reported | binding none | category academic repository / EPrints 3.3–3.4
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://eprints.whiterose.ac.uk
- free tier: No quota model. EPrints has no per-user or per-collection byte accounting; the only constraints are the JavaScript max on the upload widget and Apache's LimitRequestBody. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Direct, no CDN in front on the instances checked. | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits note: Per-file only, set by Apache LimitRequestBody or the form's JS; practitioners on the EPrints list cite successful 50 GB uploads and advise against >10 GB because there is no resumable upload.
- interface detail: SWORD, OAI-PMH, cgi/ HTTP forms
- tooling: SWORD client / curl POST to cgi/
- composes with: Structurally unbounded, but the write gate is deposit-medated: White Rose's own registration page tells depositors to go through their university's CRIS (Symplectic, PURE, myPublications) instead of registering.
- reliability: No resumable upload and no failure recovery. A >10 GB POST that drops must restart from zero.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No quota model. EPrints has no per-user or per-collection byte accounting; the only constraints are the JavaScript max on the upload widget and Apache's LimitRequestBody.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 200; 'To deposit an item you do not normally need to register here. Instead, please follow the appropriate link from the list below: University of Leeds staff via Symplectic Elements ... Sheffield ... myPublications ... York ... PURE'
  - [3] 2026-10-21: 'We have had successful uploads of files of up to 50GB in the past'
  - [4] 2026-10-21: 'I would normally advise against using EPrints for files larger than 10GB ... there is no in-built failure recovery'
  - [5] 2026-10-21: https://eprints.soton.ac.uk/cgi/register — 403
- sources:
  - [1] https://wiki.eprints.org/w/Document_upload.pl
  - [2] https://eprints.whiterose.ac.uk/cgi/register
  - [3] https://www.eprints.org/eptech/msg08776.html
  - [4] https://www.eprints.org/eptech/msg08775.html
  - [5] https://eprints.soton.ac.uk/cgi/register
