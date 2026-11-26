# DocumentCloud

> documentcloud.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/documentcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/documentcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DocumentCloud (MuckRock)

- `storage/documentcloud` | fails-quota | evidence reported | binding none | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:34.672Z (live) | stale on 2026-12-04
- url https://www.documentcloud.org
- free tier: 500 MB per PDF (25 MB for non-PDF, converted via LibreOffice); no published account storage cap, but uploads require a manually verified account. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public document pages and a full REST API; funded by Knight Foundation so no egress billing, but it is journalism-only. | metered: no
- identity: email | detail: real name and valid email address; upload requires a requested account verification
- interface: rest
- limits note: 500 MB/PDF (25 MB for Office formats); upload permission requires request + verification as a journalism organization; free because of grant funding, which the FAQ says is being replaced by 'a paid model'.
- interface detail: rest
- tooling: Full REST API at https://api.www.documentcloud.org/api plus python-documentcloud and a batch uploader github.com/MuckRock/dc_batch_upload.
- composes with: Gated at the identity layer: upload rights require 'account verification', so the account multiplier (the usual escape hatch) is closed here.
- reliability: Upload is not self-serve; verification can be refused, and the funding model is explicitly in transition to paid.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 500 MB per PDF (25 MB for non-PDF, converted via LibreOffice); no published account storage cap, but uploads require a manually verified account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'PDF files have a much larger size limit of 500 MB'; non-PDF 'up to 25 MB'
  - [2] 2026-10-21: (redirects to help.muckrock.com) — 'if you are seeking to upload documents, you need to request account verification'; 'We are currently developing a paid model'
  - [3] 2026-10-21: 'All APIs ... are served from https://api.www.documentcloud.org/api'
  - [2] 2026-11-19: an account needs a real name and a valid email address, and upload additionally needs verification | capture: sha256:2bb86973a0ae2641b4af867eeecdaf1082eddc16064f26c8a950d7cc7a6cc2e1
  - [2] 2026-11-19: the upload cap is 500 MB for a single file | capture: sha256:2bb86973a0ae2641b4af867eeecdaf1082eddc16064f26c8a950d7cc7a6cc2e1 | quote: Yes, 500 MB is the largest file you can upload.
  - [1] 2026-11-19: non-PDF uploads are capped at 25 MB and PDFs at 500 MB | capture: sha256:e594fcc445b2f9eb78170534cb504f934a2da70713328bad851122d4f1a34c93 | quote: Each non-PDF document can be up to 25 MB (PDF files have a much larger size limit of 500 MB).
  - [2] 2026-11-19: free use is restricted to verified journalism organizations and a paid model is being developed | capture: sha256:2bb86973a0ae2641b4af867eeecdaf1082eddc16064f26c8a950d7cc7a6cc2e1 | quote: Thanks to generous funding from the Knight Foundation, DocumentCloud since its launch in 2010 has been offered for free exclusively to verified journalism organizations. We are currently developing a paid model to ensure the DocumentCloud platform’s sustainability.
- sources:
  - [1] https://www.muckrock.com/news/archives/2020/nov/10/release-notes-beta-document-types/
  - [2] https://www.documentcloud.org/help/faq/
  - [3] https://www.documentcloud.org/help/api/
