# Unstructured Transform

> unstructured.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unstructured/ | JSON https://fshy.ajam.dev/api/v1/entity/unstructured.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unstructured Transform

- `inference/unstructured-transform-free` | trial-only | evidence documented | binding volume-quota | category document parsing API, one-time free pages | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:34:02.658Z (live) | stale on 2026-12-04
- url https://unstructured.io/pricing
- free tier: 10,000 free pages once per account, no card required, all features included; after the first 10,000 pages the API refuses further page processing unless the account is upgraded to Pay-As-You-Go at USD 0.015 a page | unit: mixed | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the unit is pages (a page, slide or image for .pdf, .pptx and .tiff; the file size divided by 100 KB for other types; the vocabulary has no page term). The 10,000-page credit is applied once per account and does not renew
- per-object cap: 100 MB (104,857,600 bytes) per document on upload, parse or direct extract; one document per request; 50 MB per file through the MCP server | bytes: 104857600 | source: [2]
- retention: unverified: no retention period for uploaded documents or results read on the Transform pages captured
- egress: metered: no
- identity: email | detail: a Transform account: the login page at transform.unstructured.io offers registration with an email address or Continue with Google; the pricing page states no card is required for the 10,000 free pages and a card is entered only to upgrade to Pay-As-You-Go; unverified: whether registration is open or approval-gated, since the quickstart says 'If you do not have access, contact your account team'
- interface: rest
- limits:
  - volume-quota (binding): 10,000 pages once per account; further page requests fail until the account is upgraded to Pay-As-You-Go at USD 0.015 a page [1]
  - per-object-cap: 100 MB (104,857,600 bytes) per document; extensions .bmp, .docx, .heic, .jpeg, .jpg, .pdf, .png, .pptx, .tiff; one document per request [2]
  - request-rate: unverified: the limits page states 'No public values are specified for result size, request rate, or concurrent jobs' [2]
- binding note: the 10,000 pages are a one-time credit that runs out before the 100 MB per-document cap matters
- interface detail: REST (POST https://transform.unstructured.io/api/v2/parse with an unstructured-api-key header), a Python SDK, and an MCP server
- endpoint: part of interface detail
- tooling: plain REST with an API key from the Transform console, the Python SDK, or the Transform MCP server in an MCP client; the endpoint takes one local file per request, with no URL ingestion
- composes with: 10,000 pages with no card, once, for the file types .bmp, .docx, .heic, .jpeg, .jpg, .pdf, .png, .pptx and .tiff; the next page costs USD 0.015, so it is a one-time trial lane rather than a monthly one
- reliability: no reliability event recorded; no request was made because an API key needs a signed-in account
- notes: the Transform MCP server limits files to 50 MB and accepts a broader file-type list than the web app and API
- evidence note: the 10,000 free pages, their one-time application, the missing card requirement, the per-page price, the 100 MB cap and the nine accepted extensions are quoted from vendor pages read on 2026-11-03; whether registration is open to anyone is unverified, and no request was made.
- evidence:
  - [3] 2026-11-03: the Free plan is 10,000 free pages | capture: sha256:6540e1daa072e99c2f3d3b03f99ef7402c367334f79809b43b680981f9b1ef05 | quote: Start processing your data with 10,000 free pages.
  - [3] 2026-11-03: the Free plan needs no card | capture: sha256:6540e1daa072e99c2f3d3b03f99ef7402c367334f79809b43b680981f9b1ef05 | quote: - No card required.
  - [3] 2026-11-03: the next page after the first 10,000 costs USD 0.015 | capture: sha256:6540e1daa072e99c2f3d3b03f99ef7402c367334f79809b43b680981f9b1ef05 | quote: Pay only $0.015 a page after your first 10,000 free pages.
  - [3] 2026-11-03: the Free plan includes all features | capture: sha256:6540e1daa072e99c2f3d3b03f99ef7402c367334f79809b43b680981f9b1ef05 | quote: - All features included.
  - [2] 2026-11-03: the MCP server has a separate 50 MB per-file limit | capture: sha256:296da417d7a95707b5d4fd860cad91c13bdd666c0ea09b7438f345a7f4d687e7 | quote: MCP clients have a separate documented limit of 50 MB per file.
  - [4] 2026-11-03: a Python SDK client exists for the Transform API | capture: sha256:f2f1e3225576936424b23cc07303b35d28074d829231295f12657af06531bb5d | quote: from unstructured_transform_client import TransformClient
  - [1] 2026-11-03: the 10,000-page credit is applied once per account | capture: sha256:ee77e8d2a588e09ba04c70df6850a0dd19545181af9b71d6634bb7e9e9e430ae | quote: Unstructured applies this 10,000-page credit once per account.
  - [1] 2026-11-03: page requests fail after the first 10,000 pages unless the account is upgraded | capture: sha256:ee77e8d2a588e09ba04c70df6850a0dd19545181af9b71d6634bb7e9e9e430ae | quote: After the first 10,000 pages, future page processing requests will begin failing unless you have upgraded to a Pay-As-You-Go plan.
  - [1] 2026-11-03: a credit card is entered only when upgrading to Pay-As-You-Go | capture: sha256:ee77e8d2a588e09ba04c70df6850a0dd19545181af9b71d6634bb7e9e9e430ae | quote: Follow the on-screen directions to enter your credit card information.
  - [1] 2026-11-03: how a page is counted for file types other than PDF, PPTX, TIFF and DOCX with page metadata | capture: sha256:ee77e8d2a588e09ba04c70df6850a0dd19545181af9b71d6634bb7e9e9e430ae | quote: For all other file types, Unstructured calculates the number of pages as the file's size divided by 100 KB.
  - [2] 2026-11-03: the per-document size cap | capture: sha256:296da417d7a95707b5d4fd860cad91c13bdd666c0ea09b7438f345a7f4d687e7 | quote: | Document upload | 100 MB (104,857,600 bytes) per document on Upload, Parse, or direct Extract. |
  - [2] 2026-11-03: the accepted file extensions | capture: sha256:296da417d7a95707b5d4fd860cad91c13bdd666c0ea09b7438f345a7f4d687e7 | quote: | Supported extensions | `.bmp`, `.docx`, `.heic`, `.jpeg`, `.jpg`, `.pdf`, `.png`, `.pptx`, `.tiff` |
  - [2] 2026-11-03: the request rate and concurrency limits are unpublished | capture: sha256:296da417d7a95707b5d4fd860cad91c13bdd666c0ea09b7438f345a7f4d687e7 | quote: No public values are specified for result size, request rate, or concurrent jobs.
  - [2] 2026-11-03: the API takes one local document per request and has no URL ingestion | capture: sha256:296da417d7a95707b5d4fd860cad91c13bdd666c0ea09b7438f345a7f4d687e7 | quote: The Transform API does not currently support URL ingestion, presigned uploads, or multi-document uploads.
  - [5] 2026-11-03: requests authenticate with an API key header | capture: sha256:2c3e1a62338eb91bed0bf1908f061c69adca29ff4cb92d31115150d135a37b29 | quote: Transform API requests use an API key in the `unstructured-api-key` header.
  - [6] 2026-11-03: the parse endpoint of the Transform API | capture: sha256:9aff47c7a26da7d06f9118febb305b6b7d49b3507d492e70d5e9eda4eaec5239 | quote: curl -i https://transform.unstructured.io/api/v2/parse \
  - [6] 2026-11-03: the quickstart says users without access contact an account team, so open registration is not confirmed by it | capture: sha256:9aff47c7a26da7d06f9118febb305b6b7d49b3507d492e70d5e9eda4eaec5239 | quote: If you do not have access, contact your account team.
  - [7] 2026-11-03: the Transform login page has a registration link for new users | capture: sha256:67e72d1beb05a53281289db06d44426e97b4242f05f96ce5ce5da45f54d14954 | quote: # Get access to Transform
  - [7] 2026-11-03: the Transform login page offers Google sign-in beside an email field | capture: sha256:67e72d1beb05a53281289db06d44426e97b4242f05f96ce5ce5da45f54d14954 | quote: Continue with Google
  - probe:https://transform.unstructured.io/api/v2/parse 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 401 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:dfe56215d11653cfbf9638b5fa5c8463efeb80b18f9e496c70a5f427106e9cef | quote: "status": 401
- sources:
  - [1] https://docs.unstructured.io/transform/billing
  - [2] https://docs.unstructured.io/transform/limits
  - [3] https://unstructured.io/pricing
  - [4] https://docs.unstructured.io/transform/parse
  - [5] https://docs.unstructured.io/transform/authentication
  - [6] https://docs.unstructured.io/
  - [7] https://transform.unstructured.io/
