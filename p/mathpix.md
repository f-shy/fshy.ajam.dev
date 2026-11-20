# Mathpix OCR API

> mathpix.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mathpix/ | JSON https://fshy.ajam.dev/api/v1/entity/mathpix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mathpix OCR API

- `inference/mathpix-ocr-api` | paid-only | evidence documented | binding volume-quota | category OCR and document parsing API, paid with a testing credit | tier Pay as you go
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:34:02.658Z (live) | stale on 2026-12-04
- url https://mathpix.com/pricing/api
- free tier: no free tier and no free trial for the OCR API: a one-time USD 19.99 non-refundable setup fee activates the first API key and applies a USD 29 testing credit to the account; a credit or debit card is required to activate a key. Billing is per use after the credit: image OCR USD 0.002 per image, documents (PDF, DOCX, PPTX) USD 0.005 per page, batch documents USD 0.0015 per page | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the testing credit is denominated in USD (USD 29); the metered unit is images for v3/text and pages for v3/pdf and the Files API, for which the vocabulary has no term
- per-object cap: unverified: no per-file size or per-document page cap read on the pricing, billing or limits pages; the Files API accepts a job of up to 200,000 documents
- retention: images are stored for quality assurance for 30 days by default; a retention opt-out deletes images within 24 hours | days: 30 | source: [2]
- egress: the response is the payload; no separate egress term is published; the Files API can write results to a customer-owned S3, GCS or Azure bucket | metered: no
- identity: card | detail: a Mathpix account with a verified email, then an API organization on the Pay as you go plan with a credit or debit card added and a one-time non-refundable setup fee paid before a key is issued
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 29 testing credit applied after the one-time USD 19.99 setup fee; the default page limit is 20,000 pages per month for v3/pdf and files/v1 together, per API key [3]
  - request-rate: 200 requests per minute per API key on synchronous image requests (v3/text, v3/latex); asynchronous and batch requests are not subject to the per-minute limit [3]
- binding note: a card and a USD 19.99 setup fee gate the key before any quota exists; the USD 29 testing credit then runs out first
- interface detail: REST endpoints v3/text (image), v3/pdf (documents), v3/strokes (digital ink) and files/v1 (asynchronous batch); the open-source Mathpix CLI (mpx) drives the hosted API
- endpoint: https://api.mathpix.com/v3/text
- tooling: any HTTP client with app_id and app_key headers; the Mathpix CLI (mpx) handles uploads, status polling and downloads
- composes with: a paid OCR lane for printed and handwritten STEM content (math, tables, chemistry diagrams); the USD 29 testing credit costs a USD 19.99 setup fee and a card, so the no-card hosted OCR offers come before it
- reliability: no reliability event recorded; the page limit and rate limit are per key and can be raised from the console Requests tab
- evidence note: the card requirement, the setup fee, the testing credit, the prices and the default limits are quoted from vendor pages read on 2026-11-03; no request was made, because a key needs a paid setup. The per-file size cap is unverified.
- evidence:
  - [2] 2026-11-03: an API key is activated by a one-time USD 19.99 setup fee | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: A one-time $19.99 setup fee activates your first API key.
  - [2] 2026-11-03: the Pay as you go plan includes a USD 29 credit for testing | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: - $29 credit for testing endpoints
  - [1] 2026-11-03: the API has no free trial; the setup fee buys the USD 29 testing credit | capture: sha256:ed5ab5539d801f280c687b5c4ce02636c8e3f0347be593a1f6164387a70f65a6 | quote: We don’t give a free trial for Mathpix OCR API. But you can create an account for a $19.99 one-time non-refundable setup fee and you’ll get $29 applied to your account for testing any of our endpoints.
  - [4] 2026-11-03: a credit or debit card is required to activate an API key | capture: sha256:dd7db80b0243a28a24e8dd9d0097f61898e01ce7acd002d61f0d85dd30f69a5b | quote: You will be required to add a credit or debit card in order to activate an API key.
  - [4] 2026-11-03: the REST endpoint and its app_id and app_key header authentication | capture: sha256:dd7db80b0243a28a24e8dd9d0097f61898e01ce7acd002d61f0d85dd30f69a5b | quote: curl -X POST https://api.mathpix.com/v3/text
  - [2] 2026-11-03: v3/text accepts images and returns LaTeX, Markdown or MathML | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: Printed or handwritten text, math, tables, and diagrams from one image, to LaTeX, Markdown, or MathML.
  - [2] 2026-11-03: v3/pdf accepts PDF, DOCX and PPTX and is billed per page | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: PDFs, DOCX, and PPTX to Mathpix Markdown, LaTeX, DOCX, HTML, or line-level JSON. Billed per page.
  - [3] 2026-11-03: the default monthly page limit per key, shared by v3/pdf and files/v1 | capture: sha256:5ee19fbbf2d05c6f1b2efd96625fd01fcabc919eb8b53f6dd2621cd9bd710d78 | quote: | Page limit | 20,000 pages / month | `v3/pdf` and `files/v1`, which share one allotment |
  - [3] 2026-11-03: the default synchronous rate limit per key | capture: sha256:5ee19fbbf2d05c6f1b2efd96625fd01fcabc919eb8b53f6dd2621cd9bd710d78 | quote: | Rate limit | 200 requests / minute | Synchronous image requests - `v3/text`, `v3/latex` |
  - [2] 2026-11-03: default image retention is 30 days with an opt-out that deletes within 24 hours | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: Default retention is 30 days. You can opt out, and images are deleted within 24 hours.
  - [2] 2026-11-03: the Files API takes a job of up to 200,000 documents and can write results to the customer's own bucket | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: One file, a source URI, or a job of up to 200,000 documents. Results land in your own S3, GCS, or Azure bucket.
  - [2] 2026-11-03: image OCR is billed at USD 0.002 per image | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: $0.002/ image
  - [2] 2026-11-03: document pages through v3/pdf are billed at USD 0.005 per page | capture: sha256:cb734277e13844a7698836976121696e9f73d5303dbc1d888fa2d19a9031defc | quote: $0.005/ page
  - [5] 2026-11-03: the service recognises printed and handwritten STEM content from images, stroke data or PDF files | capture: sha256:4ea3e2739e9c92a53dbf768a57451e7efecec5d824f96b8e861d0cc6bb149113 | quote: Mathpix OCR recognizes printed and handwritten STEM document content, including math, text, tables, and chemistry diagrams, from images, stroke data, or PDF files.
  - [5] 2026-11-03: a command-line client drives the hosted API | capture: sha256:4ea3e2739e9c92a53dbf768a57451e7efecec5d824f96b8e861d0cc6bb149113 | quote: It handles uploads, status polling, and downloads for the hosted API or your Private Cloud OCR deployment.
  - [3] 2026-11-03: asynchronous requests are exempt from the per-minute rate limit | capture: sha256:5ee19fbbf2d05c6f1b2efd96625fd01fcabc919eb8b53f6dd2621cd9bd710d78 | quote: - Sending `async: true`, or supplying a `callback`, on `v3/text` exempts that request.
  - [3] 2026-11-03: limit increases are self-service from the console | capture: sha256:5ee19fbbf2d05c6f1b2efd96625fd01fcabc919eb8b53f6dd2621cd9bd710d78 | quote: Limit increases are self-service.
  - [4] 2026-11-03: the account needs a verified email before the organization and billing steps | capture: sha256:dd7db80b0243a28a24e8dd9d0097f61898e01ce7acd002d61f0d85dd30f69a5b | quote: Once you have verified your email
- sources:
  - [1] https://mathpix.com/docs/convert/billing
  - [2] https://mathpix.com/pricing/api
  - [3] https://mathpix.com/docs/convert/limits
  - [4] https://mathpix.com/docs/convert/creating-an-api-key
  - [5] https://docs.mathpix.com/
