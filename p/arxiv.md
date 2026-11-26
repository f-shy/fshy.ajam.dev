# arxiv

> arxiv.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/arxiv/ | JSON https://fshy.ajam.dev/api/v1/entity/arxiv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## arxiv

- `storage/arxiv` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:56.063Z (live) | stale on 2026-12-04
- url https://info.arxiv.org/help/submit/index.html
- free tier: none reachable: Endorsement-gated and paper-shaped: 'We only accept submissions from registered authors. If you are a new user or are submitting to a new category, you may be required to find… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on https://info.arxiv.org/help/submit/index.html | source: [1] | note: not applicable
- retention: not stated on https://info.arxiv.org/help/submit/index.html | source: [1]
- egress: not stated on https://info.arxiv.org/help/submit/index.html | metered: no
- identity: email
- interface: browser
- interface detail: Submission is through the arXiv website; files are uploaded in the browser on the Prepare Files page.
- tooling: not documented
- composes with: Ancillary data files accompany an article and are downloaded from its abstract page; arXiv is an archive and distribution service for research articles.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Endorsement-gated and paper-shaped: 'We only accept submissions from registered authors. If you are a new user or are submitting to a new category, you may be required to find…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Endorsement-gated and paper-shaped: 'We only accept submissions from registered authors. If you are a new user or are submitting to a new category, you may be required to find endorsements'
  - [1] 2026-11-19: arxiv submissions are restricted to registered authors and may require endorsement | capture: sha256:c3d04ae1fea8dfa803172491859935dad65b4e031cd7e17005b10100baace737 | quote: - We only accept submissions from [registered authors](https://info.arxiv.org/help/registerhelp.html). If you are a new user or are submitting to a new category, you may be required to find [endorsements](https://info.arxiv.org/help/endorsement.html).
  - [1] 2026-11-19: the submission page describes uploading files in the browser | capture: sha256:c3d04ae1fea8dfa803172491859935dad65b4e031cd7e17005b10100baace737 | quote: Please note: The option to drag files from your computer into the submission window in the browser is not currently available.
  - [1] 2026-11-19: the page states a storage goal but no fixed retention period | capture: sha256:c3d04ae1fea8dfa803172491859935dad65b4e031cd7e17005b10100baace737 | quote: Our goal is to store articles in formats that are highly portable and stable over time.
  - [1] 2026-11-19: the page describes multi-file upload but no per-object byte cap | capture: sha256:c3d04ae1fea8dfa803172491859935dad65b4e031cd7e17005b10100baace737 | quote: You can use zip or tar.gz to upload multiple files, uploading source that uses subfolders, and source that includes ancillary files.
  - [2] 2026-11-19: the ancillary-file page describes how data files accompany an article | capture: sha256:f605c1a219306e752428c7eb863ce923b58c600690afd7812114f25481449016 | quote: arXiv is primarily an [archive and distribution service for research articles](https://info.arxiv.org/about/index.html).
  - [2] 2026-11-19: the ancillary page states no egress price or traffic quota | capture: sha256:f605c1a219306e752428c7eb863ce923b58c600690afd7812114f25481449016 | quote: There are limited facilities for including ancillary files with articles.
- sources:
  - [1] https://info.arxiv.org/help/submit/index.html
  - [2] https://info.arxiv.org/help/ancillary_files.html
