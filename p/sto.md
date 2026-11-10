# sto.care

> sto.care | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sto/ | JSON https://fshy.ajam.dev/api/v1/entity/sto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sto.care (ul.sto.care)

- `debrid/sto-care` | qualifies-with-caveat | evidence measured | binding pull-count | category anonymous transfer.sh-shaped upload (PUT a body, get a JSON link) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:30:47.000Z (live) | stale on 2026-11-23
- url https://ul.sto.care/
- price USD 0
- free tier: 3-day expiry and a JSON link from a single PUT, no account. The site advertises 'a retention period that depends on file size' and the upload reply carried expiresAt three days out. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The upload host is ul.sto.care and the download host is trystocare.com; the brand and both domains disagree.
- per-object cap: unverified: no size cap is stated on the pages read; 1 MiB was accepted | source: [2] | note: A 100 MB cap is mentioned by a third-party blog for a different product on the same site, so it was not carried over.
- retention: expiresAt 2026-10-26T02:22:40.454Z for an upload at 2026-10-23T02:22:40Z, so 72 hours | days: 3 | source: [2] | note: Measured from the reply field, not from the page.
- egress: Downloads are served from trystocare.com. The site advertises a 10-download limit per link, which makes the link a distribution budget rather than a store. | metered: no | free allowance: none published | source: [3]
- identity: anonymous | detail: A bare PUT with no cookie, no account and no email returned a link.
- interface: rest, cli
- limits:
  - retention-clamped: 72 hours measured: expiresAt in the upload reply
  - pull-count (binding): 10 downloads per link (vendor claim) [3]
- limits note: The download limit was not exercised: 10 fetches of one link confirms the threshold, and the second fetch is the interesting one because the first may not count.
- binding note: At 1 TiB a month no published byte cap was hit, but a 10-download link means a re-fetch of the same object fails once ten readers have had it, and 72 hours bounds it again; the pull count is the first of the two that a busy object meets.
- interface detail: curl -T file https://ul.sto.care/<name> returns JSON {url, expiresAt}, with the download URL on a different host.
- endpoint: part of interface detail
- tooling: Any HTTP client that can PUT a file; the transfer.sh one-liner works with the hostname swapped
- composes with: A transfer.sh-shaped PUT is the cheapest thing to wire into a script that already speaks that idiom, and the JSON reply makes the link parseable, but 3 days and a per-link download count make it a hand-off, not a mirror.
- reliability: The upload host and the download host are different domains, so a client that allow-lists the upload domain breaks at retrieval.
- notes: A credible transfer.sh replacement that actually answers, and the only measured relay that returns a machine-readable expiry. The caveat is that its own documentation lives in blog posts rather than a docs page.
- evidence note: Upload and read-back at 1 MiB with a matching SHA-256; the cap and the 10-download limit are vendor claims and were not pushed.
- probe:
  - upload_bytes: 1048576
  - download_bytes: 1048576
  - match: yes
  - status: 200
- extras:
  - download_host: trystocare.com
  - expires_at: 2026-10-26T02:22:40.454Z
- evidence:
  - probe:https://ul.sto.care/ 2026-10-23: PUT of 1 048 576 bytes -> HTTP 200 body {'url':'https://trystocare.com/c8aujwob94','expiresAt':'2026-10-26T02:22:40.454Z'}
  - probe:https://trystocare.com/c8aujwob94 2026-10-23: read-back 1 048 576 bytes, sha256 da0099c231f1182a5d411c8ac5149dfb7a2e3578a3970928490cb78ba92aecc9, full-body hash matched
  - [3] 2026-10-23: 'You get a JSON link that allows 10 downloads over 72 hours' - the vendor's own blog, which is the only place either number is stated
  - [1] 2026-10-23: the service positions itself as a 0x0.st and transfer.sh replacement with a curl one-liner
- sources:
  - [1] https://sto.care/blog/0x0-st-alternative/
  - [2] https://ul.sto.care/
  - [3] https://sto.care/blog/file-io-alternative/
