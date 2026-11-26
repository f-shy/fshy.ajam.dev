# EPrints 3.x platform class

> eprints.whiterose.ac.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eprints-whiterose-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/eprints-whiterose-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EPrints 3.x platform class (White Rose, QUT, Southampton)

- `storage/eprints-3-x-platform-class` | fails-identity | evidence reported | binding none | category academic repository / EPrints 3.3–3.4
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.790Z (live) | stale on 2026-12-04
- url https://eprints.whiterose.ac.uk
- free tier: No quota model. EPrints has no per-user or per-collection byte accounting; the only constraints are the JavaScript max on the upload widget and Apache's LimitRequestBody. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Accounts not used for deposit remain live for 12 months from last recorded activity, then the account and its personal data are deleted. | source: [1] | note: not stated
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
  - [2] 2026-11-19: registration page states accounts unused for deposit are deleted after 12 months of inactivity | capture: sha256:69ef0a49ffc6460a57ac349670d8ed01208452159538073bd28c0c1b9eca1b43 | quote: Should you not use your account to deposit content, the account will remain live for 12 months from last recorded activity. After this period, the account, along with any personal data it contains, will be deleted.
  - [2] 2026-11-19: registration page routes depositors through institutional systems (Symplectic, myPublications, PURE) | capture: sha256:69ef0a49ffc6460a57ac349670d8ed01208452159538073bd28c0c1b9eca1b43 | quote: To deposit an item you do not normally need to register here. Instead, please follow the appropriate link from the list below:
  - [1] 2026-11-19: EPrints document upload configuration exposes per-archive file-count settings | capture: sha256:2471bcaa70c36dd5e1847bd5bb492dcfd2b3dd9c8e222a820a8168caca6d71ab | quote: $c->{archive_max_files} - Maximum files in an archive (e.g. zip file) that can be expanded and stored on EPrints. (Commented out by default, 100 is the maximum unless uncommented).
  - [3] 2026-11-19: practitioners report successful uploads of files up to 50GB | capture: sha256:56179d3d141dbed898348d9dc62dfd394fef8769285907f42920639076417c35 | quote: We have had successful uploads of files of up to 50GB in the past,
  - [4] 2026-11-19: practitioners advise against files larger than 10GB because there is no in-built failure recovery | capture: sha256:2c0f3a3fc48225803be808970da8588857b056fb2896ed6d5979e78288c3fdcb | quote: I would normally advise against using EPrints for files larger than 10GB, as the time to upload can be quite long and as they is no in-built failure recovery,
- sources:
  - [1] https://wiki.eprints.org/w/Document_upload.pl
  - [2] https://eprints.whiterose.ac.uk/cgi/register
  - [3] https://www.eprints.org/eptech/msg08776.html
  - [4] https://www.eprints.org/eptech/msg08775.html
  - [5] https://eprints.soton.ac.uk/cgi/register
