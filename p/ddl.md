# DDL.to

> ddl.to | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ddl/ | JSON https://fshy.ajam.dev/api/v1/entity/ddl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DDL.to

- `debrid/ddl-to` | dead | evidence documented | binding none | category former premium file host, now a redirect to DDownload | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:43.324Z (live) | stale on 2026-12-26
- url https://ddl.to/
- free tier: Not applicable: ddl.to serves no offer of its own. The domain redirects to ddownload.com. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The successor's terms belong to storage/ddownload and are not restated here.
- per-object cap: Not applicable: the brand no longer hosts. | source: [1]
- retention: Not applicable. | source: [1]
- egress: None from this domain; every request is forwarded to ddownload.com. | metered: no | source: [1]
- identity: anonymous | detail: Nothing is asked for at ddl.to; whatever the redirect target asks for is DDownload's policy.
- interface: unknown
- limits note: No constraint applies to a redirect.
- binding note: Nothing transfers from this domain, so nothing can bind.
- interface detail: An HTTP redirect. There is no endpoint to call.
- tooling: Nothing to tool against. A client that still holds a ddl.to link is handed to DDownload's own page.
- composes with: A dead link in old index posts. Its only use now is to know that a DDL.to URL still resolves, to DDownload, rather than 404ing - so a link checker will report it alive when the host behind it is a different company.
- reliability: A link checker sees HTTP 200 and a live host, which is exactly the failure these records warns about: the host answering is not the host the link names. Any inventory that still counts DDL.to as a separate provider is double-counting DDownload.
- notes: Kept as a dead record rather than deleted so the subsequent audit does not re-open the name and so the DDownload redirect is documented once. Successor: storage/ddownload.
- evidence note: The redirect and its landing page were read. That is all this record claims.
- extras:
  - successor_record: storage/ddownload
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-23: ddl.to resolves to https://ddownload.com/ and serves the DDownload homepage ('Ultimate Cloud Storage - DDownload'), so the brand is retired and the domain forwards
  - [1] 2026-11-25: ddl.to serves the DDownload transfer service, so the old brand hosts nothing of its own | capture: sha256:f4b3f19870489a26e1ab758724833b94d18181c14833d5d8874b617f7d5f0c1a | quote: Drop your files into the window, wait a moment and send the link. Whoever gets it does not need an account.
  - [1] 2026-11-25: the page at the old domain is DDownload's service, not DDL.to | capture: sha256:f4b3f19870489a26e1ab758724833b94d18181c14833d5d8874b617f7d5f0c1a | quote: Drop your files into the window, wait a moment and send the link. Whoever gets it does not need an account.
- sources:
  - [1] https://ddl.to/
