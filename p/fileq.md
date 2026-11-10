# FileQ

> fileq.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileq/ | JSON https://fshy.ajam.dev/api/v1/entity/fileq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileQ

- `debrid/fileq` | qualifies-with-caveat | evidence documented | binding write-gated | category premium file host with a webmaster-gated free tier and pay-per-download programme | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:42:02.709Z (live) | stale on 2026-11-23
- url https://fileq.net/
- price USD 20 per TB-month of additional storage | parsed USD 20/TB-mo
- free tier: "Deleted after 3 days. Sign up to store longer." The free path accepts uploads but keeps them three days; the site also says file upload privileges are for verified webmasters. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Three days is the shortest free retention met among debrid providers.
- per-object cap: "Upload Large Files 110GB" - the headline figure, 110 GB per file. | bytes: 118111600640 | source: [1] | note: 110 GB taken in the site's own decimal-free phrasing; stored above as 110 x 1024^3. The page does not say whether the 110 GB applies to the free path or to Premium.
- retention: Anonymous uploads: 'Deleted after 3 days'. Registered accounts 'store longer' - the number is not printed. | days: 3 | source: [1]
- egress: Downloads are served from a CDN: 'Multi-region with CDN for fast global delivery'. Premium advertises 'unlimited bandwidth'. No allowance is printed for the free path. | metered: no | source: [2]
- identity: email | detail: Registration is free, but the upload right needs a review of the applicant's website: 'FileQ provides file upload privileges exclusively to verified webmasters with established websites and significant traffic'.
- interface: unknown
- limits:
  - write-gated (binding): upload privileges are for 'verified webmasters with established websites and significant traffic', by application [2]
  - retention-clamped: 3 days for anonymous uploads [1]
  - volume-quota: additional storage at USD 20 per TB per month for non-webmaster accounts [2]
- limits note: Two gates stack: the upload right is reviewed, and the free retention is three days. A client that is not a webmaster cannot use this as storage at any price below USD 20/TB-month.
- binding note: Before any byte or day can bind, the account has to be approved as a webmaster. At 1 TiB a month an unapproved account never reaches a quota question, and an approved one hits the 3-day retention on the free path.
- interface detail: A web upload form at /upload with no documented API on the pages read. A referral URL pattern exists (/api/ref/<code>) which is a marketing link, not an endpoint.
- tooling: Browser upload only as read. Here that is a tooling note, not a verdict: the form is a POST and could be driven by a script.
- composes with: Not a storage answer at three days. Its place in published records is as a price reference: EUR/USD 20 per TB-month for storage is the shape of a host that sells capacity, against hosts here that give it away and monetise the player instead.
- reliability: A hosting service whose free tier deletes in three days and whose upload right is discretionary: both are account decisions, so both can change without a pricing page changing. The 110 GB figure is a headline with no stated tier attached.
- notes: Live host resolves at fileq.net. Three days free file retention.
- evidence note: The 3-day retention, the 110 GB headline, the webmaster gate and the USD 20/TB price were read on the vendor's pages. Not established: whether 110 GB applies to free or paid, and what an account's retention actually is.
- extras:
  - referral_pattern: /api/ref/<code> is a referral link, not an API endpoint
- evidence:
  - [1] 2026-10-23: 'Upload Large Files 110GB', 'Deleted after 3 days. Sign up to store longer.', and the webmaster-oriented pitch
  - [2] 2026-10-23: 'Additional Storage: $20 per TB monthly for non-webmaster accounts', the webmaster-only upload policy, 'unlimited bandwidth' on premium, and PPD on Pro and Team
- sources:
  - [1] https://fileq.net/
  - [2] https://fileq.net/premium
