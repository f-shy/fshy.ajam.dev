# pdfcoffee

> pdfcoffee.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pdfcoffee/ | JSON https://fshy.ajam.dev/api/v1/entity/pdfcoffee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pdfcoffee / dokumen.pub / idoc.pub (unlimited-PDF dump network)

- `storage/pdfcoffee-dokumen-pub-idoc-pub` | fails-quota | evidence reported | binding write-gated | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:22:32.524Z (live) | stale on 2026-11-19
- url https://pdfcoffee.com
- free tier: pdfcoffee.com states 'Upload as much as you need! Unlimited volume of uploaded files.' with any number of documents in PDF, Microsoft Word and PowerPoint format; no document count or account quota is stated on the page. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: the dokument.pub FAQ that stated 200 MB per PDF now serves a domain-for-sale page, and no current page of the three sites states a per-file cap | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public HTTP: every document has a permanent public page and a download endpoint (idoc.pub: /download-file-partner/<slug>?hash=<md5-like>); no auth, no metering, no expiry documented. | metered: no
- identity: anonymous | detail: unverified: the pdfcoffee.com sign-in page offers only Login with Google and no upload was attempted; the earlier anonymous kind rests on page text, not on an executed upload
- interface: rclone
- limits:
  - write-gated (binding): dokumen.pub answers HTTP 403 with a Cloudflare challenge page to a plain GET [2]
- limits note: pdfcoffee.com states no document count, account quota or per-file cap; the 200 MB per-file figure of the dokument.pub FAQ can no longer be read because that address serves a domain-for-sale page. dokumen.pub sits behind a Cloudflare challenge. File types are PDF, Microsoft Word and PowerPoint.
- binding note: the site behind the upload form answers a bot challenge (HTTP 403 to a plain GET), so bulk ingest is bounded by that gate rather than by a quota
- interface detail: wrapper-only
- tooling: No API. Upload is a browser form behind Cloudflare/nginx bot filtering; download is a plain GET. No rclone backend, no known maintained client.
- composes with: Per-record unlimited means the chain is just 'keep uploading': 200 MB/PDF x unlimited PDFs. But every unit needs a form POST, so throughput is bounded by bot defences, not quota.
- reliability: On 2026-11-03 idoc.pub and dokument.pub serve a domain-for-sale page, dokumen.pub answers HTTP 403 with a Cloudflare challenge, and pdfcoffee.com serves its pages and offers sign-in only with a Google account. Documents are public pages, and sibling sites share templates.
- notes: "Upload as much as you need! Unlimited volume of uploaded files". No document count or account quota; dokument.pub FAQ caps a single PDF at 200 MB and states "No limitation" on number of pages/uploads. Per-record unlimited x unlimited records.
- evidence note: reported: the pages read on 2026-11-03 are https://pdfcoffee.com/about (states unlimited volume of uploaded files and publication of any number of documents in PDF, Microsoft Word and PowerPoint format), https://pdfcoffee.com/login (sign-in offers only Login with Google), https://dokument.pub/faqs and https://idoc.pub/faqs (both now serve a domain-for-sale page with no FAQ content) and a plain-GET probe of https://dokumen.pub/ that was refused with a Cloudflare challenge. The write-gated binding rests on that probe, and no per-file cap or sign-up route is stated on any page read, so the rung stays reported.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: "Upload as much as you need! Unlimited volume of uploaded files" — no document count or account quota; dokument.pub FAQ caps a single PDF at 200 MB and states "No limitation" on number of pages/uploads. Per-record unlimited x unlimited records.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The max PDF file size is 200 MB'; 'Is there a limitation on the number of ... uploads? No limitation.'
  - [3] 2026-10-21: 'Upload as much as you need! Unlimited volume of uploaded files. You may publish any number of documents in PDF, Microsoft Word and PowerPoint format.'
  - [4] 2026-10-21: POST https://dokumen.pub/upload -F file=@t.pdf -> 403 Cloudflare 'Just a moment...'
  - [5] 2026-10-21: probe: GET -> login wall (/login?redirect_url=...); GET https://idoc.pub/download-file-partner/anonymous-presentacion-vlr0vrvwjzlz?hash=e2e0... -> 302 to /404 (hash is per-document, not reusable)
  - [6] 2026-10-21: probe: GET -> 200 but Content-Type text/html (viewer page, not the original bytes)
  - [7] 2026-11-03: pdfcoffee.com states unlimited volume of uploaded files | capture: sha256:0839458b818160fa2484e8c25c24b7d701abf55a4469eb65ad2603d2c56f460f | quote: Upload as much as you need! Unlimited volume of uploaded files.
  - [1] 2026-11-03: the dokument.pub FAQ address now serves a domain-for-sale page | capture: sha256:7c7044dafee22ec7e0beb53d4b1b97e65bbac1d5a853a1cddec801b607860946 | quote: is for sale!
  - probe:dokumen.pub 2026-11-03: a plain GET of dokumen.pub answered HTTP 403 | capture: sha256:1dbfd488265741defbaf338345085f5cd95d751ecb3f8a9c764a6610b14a429f | quote: "status": 403
  - [7] 2026-11-03: pdfcoffee.com lists PDF, Word and PowerPoint documents | capture: sha256:0839458b818160fa2484e8c25c24b7d701abf55a4469eb65ad2603d2c56f460f | quote: Upload as much as you need! Unlimited volume of uploaded files.
  - [8] 2026-11-03: idoc.pub serves a domain-for-sale page | capture: sha256:11ed843e6602840535c5f0a3a10c64fbaa85feb7b782932a80488e55d92c906b | quote: is for sale!
  - [1] 2026-11-03: dokument.pub serves a domain-for-sale page | capture: sha256:7c7044dafee22ec7e0beb53d4b1b97e65bbac1d5a853a1cddec801b607860946 | quote: is for sale!
  - [9] 2026-11-03: the pdfcoffee.com sign-in page offers only Login with Google | capture: sha256:5ff44c4950eb91ab7b52b2205bf173036f9fff2debb4b3ee31d23dc41d8dfd56 | quote: [Login with Google](https://pdfcoffee.com/login/google)
  - [9] 2026-11-03: the sign-in page offers only Login with Google | capture: sha256:5ff44c4950eb91ab7b52b2205bf173036f9fff2debb4b3ee31d23dc41d8dfd56 | quote: [Login with Google](https://pdfcoffee.com/login/google)
  - [7] 2026-11-03: pdfcoffee.com still states unlimited volume of uploaded files | capture: sha256:0839458b818160fa2484e8c25c24b7d701abf55a4469eb65ad2603d2c56f460f | quote: Upload as much as you need! Unlimited volume of uploaded files.
  - [7] 2026-11-04: pdfcoffee.com states unlimited volume of uploaded files | capture: sha256:0839458b818160fa2484e8c25c24b7d701abf55a4469eb65ad2603d2c56f460f | quote: Upload as much as you need! Unlimited volume of uploaded files.
- sources:
  - [1] https://dokument.pub/faqs
  - [2] https://dokumen.pub/
  - [3] https://dokumen.pub/about
  - [4] https://pdfcoffee.com/upload
  - [5] https://idoc.pub/upload
  - [6] https://pdfcoffee.com/download/upload-10-pdf-free.html
  - [7] https://pdfcoffee.com/about
  - [8] https://idoc.pub/faqs
  - [9] https://pdfcoffee.com/login
