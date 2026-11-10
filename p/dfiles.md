# DFiles

> dfiles.eu | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/dfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DFiles (DepositFiles)

- `debrid/dfiles` | qualifies-with-caveat | evidence documented | binding write-gated | category file host (account required, premium upgrade) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://dfiles.eu/
- price unverified: no premium price page was readable
- free tier: Unlimited file storage time and space; maximum upload file size 10 GB; account required. | unit: unlimited | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The homepage prints these as what the service offers; whether they bind free or paid accounts is not separated on the page.
- per-object cap: Maximum upload file size – 10 GB | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3.
- retention: unverified: the homepage says unlimited file storage time and does not separate free from premium retention | source: [1]
- egress: unverified: no download allowance printed on the homepage; the premium and FAQ pages tried (premium.php, faq.php) answered HTTP 404. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: 'All you need is to create an account and upload files.' The sign-up form fields were not read, so email is the minimum assumed and is unverified.
- interface: unknown
- limits:
  - per-object-cap: 10 GB per file [1]
  - write-gated (binding): an account must be created before upload [1]
- binding note: The homepage says an account is the first step to upload; the cap and retention are second.
- interface detail: Files upload from remote HTTP or FTP servers; web upload.
- tooling: Browser only as read; remote HTTP and FTP URL import is listed.
- composes with: 10 GB per file, but a sign-up is the first step.
- reliability: The premium and FAQ URLs guessed (premium.php, faq.php) answered 404 on 2026-11-03, so the paid price is unverified.
- evidence note: Homepage read on 2026-11-03; price, retention by tier and identity fields unverified.
- evidence:
  - [1] 2026-11-03: the per-file upload cap is 10 GB | capture: sha256:cba7a96888cda78c80cc094aa12663efdceb48627da1ad5a22f20fa229366103 | quote: Maximum upload file size – 10 GB
  - [1] 2026-11-03: the homepage advertises unlimited storage time and space | capture: sha256:cba7a96888cda78c80cc094aa12663efdceb48627da1ad5a22f20fa229366103 | quote: Unlimited file storage time and space
  - [1] 2026-11-03: an account is needed to upload | capture: sha256:cba7a96888cda78c80cc094aa12663efdceb48627da1ad5a22f20fa229366103 | quote: All you need is to create an account and upload files.
- sources:
  - [1] https://dfiles.eu/
