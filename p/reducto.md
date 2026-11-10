# Reducto

> reducto.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/reducto/ | JSON https://fshy.ajam.dev/api/v1/entity/reducto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Reducto

- `inference/reducto-standard` | trial-only | evidence documented | binding volume-quota | category document parsing API, one-time free credit | tier Standard
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:34:02.658Z (live) | stale on 2026-12-04
- url https://reducto.ai/pricing
- free tier: USD 150 of free usage on the Standard plan, then list rates apply: Parse (r-1) USD 10 per 1,000 pages, Extract USD 20 per 1,000 pages | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the credit is denominated in USD; at the USD 10 per 1,000 pages r-1 Parse list rate, USD 150 / USD 10 per 1,000 pages = 15,000 pages. A third-party list prints '15k free credits' for the same free tier. Whether the USD 150 renews is unverified: the pricing page says 'your free $150' and names no period
- per-object cap: 100 MB per file through direct upload; 5 GB through a presigned-URL upload | source: [2]
- retention: uploaded files expire 24 hours after upload | source: [2]
- egress: metered: no
- identity: email | detail: a free account created at studio.reducto.ai ('sign up for a free account'), then an API key from Studio; unverified: the sign-up form's fields and whether a card is asked, since studio.reducto.ai answers a login wall to every reader route tried
- interface: rest, cli
- limits:
  - volume-quota (binding): USD 150 of free usage on the Standard plan; r-1 Parse is USD 10 per 1,000 pages at list rates effective 2026-09-01; unverified whether the credit renews [1]
  - per-object-cap: 100 MB per file by direct upload, 5 GB by presigned URL; 30+ file types including PDFs, images, spreadsheets, presentations and scanned documents [2]
  - request-rate: 1,000 requests per second sustained per API key on all endpoints at the API edge, returning HTTP 429 above it; parallel parse work is separately queued by a concurrency throttle [3]
- binding note: the USD 150 credit runs out at about 15,000 r-1 Parse pages, long before the 100 MB per-file cap matters
- interface detail: REST (POST https://platform.reducto.ai/parse with a Bearer API key), SDKs, a CLI (reducto-cli) and an MCP server
- endpoint: part of interface detail
- tooling: the Reducto Python, Node.js and Go SDKs, the reducto-cli command line, the MCP server, or plain REST with an API key created in Reducto Studio
- composes with: a one-time USD 150 credit worth about 15,000 r-1 Parse pages, with the Standard plan's 'No Page Limits' meaning pay-as-you-go afterwards; useful for a single bulk job rather than a recurring free lane
- reliability: no reliability event recorded; the list prices changed on 2026-09-01 and legacy credit rates were retired, and no request was made because a key needs a signed-in account
- evidence note: the USD 150 free usage, the page prices, the upload caps and the edge rate limit are quoted from vendor pages read on 2026-11-03; the sign-up fields, any card requirement and the renewal of the credit are unverified, and no request was made.
- evidence:
  - [1] 2026-11-03: the Standard plan includes a free USD 150 before standard rates apply | capture: sha256:83fbbf989fff70fba7c0b87433178c19194c92912b14f2d595c40277789c61eb | quote: After your free $150, standard rates apply.
  - [1] 2026-11-03: the Standard plan includes USD 150 of free usage, then list rates | capture: sha256:83fbbf989fff70fba7c0b87433178c19194c92912b14f2d595c40277789c61eb | quote: Standard includes $150 of free usage, then list rates apply.
  - [1] 2026-11-03: r-1 Parse is USD 10 per 1,000 pages | capture: sha256:83fbbf989fff70fba7c0b87433178c19194c92912b14f2d595c40277789c61eb | quote: | r-1 Parse | $10 | Custom | Custom |
  - [1] 2026-11-03: the pricing page lists no page limit on the plan | capture: sha256:4416e23c01dcf680de68f98aa8473d1c7efd99150297a68f2f2acb30426c9f1d | quote: - No Page Limits
  - [4] 2026-11-03: the Parse r-1 list price in the usage documentation | capture: sha256:092017e7cc6305a1cedcae99380476cdfdef2e7f468da5f8dd51ea3b795c6d90 | quote: | Parse, r-1 | \$10 / 1,000 pages | |
  - [4] 2026-11-03: the list prices took effect on 2026-09-01 | capture: sha256:092017e7cc6305a1cedcae99380476cdfdef2e7f468da5f8dd51ea3b795c6d90 | quote: These listed prices go into effect on September 1, 2026.
  - [2] 2026-11-03: direct upload is limited to 100 MB | capture: sha256:28c24fb8c432a2fc7676eefdd8ccc6899554c13ef1e71772b2cbdae0727b4a0f | quote: > | Direct upload (this page) | 100MB |
  - [2] 2026-11-03: uploaded files expire 24 hours after upload | capture: sha256:28c24fb8c432a2fc7676eefdd8ccc6899554c13ef1e71772b2cbdae0727b4a0f | quote: Files expire 24 hours after upload.
  - [3] 2026-11-03: the per-API-key request cap at the edge | capture: sha256:dae34f35cb2bbe5847ee45be3422d814d5f10a4ab69f69d8c7e97821517764a1 | quote: | All endpoints | 1,000 req/s sustained |
  - [5] 2026-11-03: an account is created at studio.reducto.ai as a free account | capture: sha256:6c49a07c2b6700dad752820c1f981bd781c2f89456750a5cc5f43593a822b3b1 | quote: Go to [studio.reducto.ai](https://studio.reducto.ai/) and sign up for a free account.
  - [5] 2026-11-03: the REST parse endpoint | capture: sha256:6c49a07c2b6700dad752820c1f981bd781c2f89456750a5cc5f43593a822b3b1 | quote: curl -X POST "https://platform.reducto.ai/parse" \
  - [5] 2026-11-03: a CLI package exists | capture: sha256:6c49a07c2b6700dad752820c1f981bd781c2f89456750a5cc5f43593a822b3b1 | quote: pip install reducto-cli
  - [6] 2026-11-03: the platform reads PDFs, images, spreadsheets, presentations and scanned documents | capture: sha256:7dffd1af058d44406d1d7f8d0fd8e1228fd36fbe316ed8ad6e18045522ccd09c | quote: including PDFs, images, spreadsheets, presentations, and scanned documents.
  - [7] 2026-11-03: a third-party list gives the free tier as 15k free credits plus pay-as-you-go | capture: sha256:7eb9f38d0d00b2e6c616bfcd2b507b785e6c1c89fd625d2766a4d0856cfbe450 | quote: Reducto - Turn any unstructured documents (PDF, XLSX, JPG, PPTX, etc.) into structured JSON data. Parse, extract data, and edit PDF forms. Free tier with 15k free credits and pay-as-you-go.
  - probe:https://platform.reducto.ai/parse 2026-11-10: a keyless POST on 2026-11-10 answered HTTP 403 with the vendor's own gate message, so the tier is gated on a key | capture: sha256:ed9e473c1af35794d0d00f1d47d89b281e5c3679682764476c0a1fa6f291922f | quote: "status": 403
- sources:
  - [1] https://reducto.ai/pricing
  - [2] https://docs.reducto.ai/upload/overview
  - [3] https://docs.reducto.ai/reference/rate-limits
  - [4] https://docs.reducto.ai/reference/credit-usage
  - [5] https://docs.reducto.ai/quickstart
  - [6] https://docs.reducto.ai/
  - [7] https://free-for.dev/
