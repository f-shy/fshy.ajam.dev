# FileShot

> fileshot.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileshot/ | JSON https://fshy.ajam.dev/api/v1/entity/fileshot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileShot

- `debrid/fileshot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file transfer service (freemium, zero-knowledge encryption) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://fileshot.io/pricing
- price USD 9.99 per month starting paid plan; storage volume of that plan not read | parsed USD 9.99/mo
- free tier: Free: max file size 10 GB, total storage 50 GB, file expiry 90 days, no signup required. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1] | note: Read from the vendor's own comparison table against other transfer services.
- per-object cap: | Max file size | 10 GB | 2 GB | 50 GB | Unlimited* | 5 GB | Unlimited | | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3; the first column is FileShot Free.
- retention: | File expiry | 90 days | 3 days | 30 days | Auto-deleted | 7 days | Until sender closes | | days: 90 | source: [1] | note: The first column is FileShot Free.
- egress: Unlimited downloads are stated on the homepage; no byte cap is printed. | metered: no | free allowance: unstated | source: [2]
- identity: anonymous | detail: The homepage states 'No account needed.' and the comparison table marks no signup required.
- interface: rest
- limits:
  - per-object-cap (binding): 10 GB per file on the free plan [1]
  - volume-quota: 50 GB total storage on the free plan [1]
  - retention-clamped: files expire after up to 90 days [1]
- binding note: 10 GB per file is the first limit; total storage of 50 GB is second.
- interface detail: The comparison table lists API access for the Creator plan and above; the free tier has none.
- tooling: Browser only on the free tier; API on a paid tier.
- composes with: Decryption keys live only in the URL fragment, so a shared link works only with the full link.
- reliability: Free chat attachments are 10 MB and chat history is kept 30 days.
- evidence note: Pricing and homepage read on 2026-11-03. The paid plan names and prices were loaded dynamically and are not on the captured page beyond the 'starting paid price' row.
- evidence:
  - [1] 2026-11-03: the free per-file cap is 10 GB | capture: sha256:a97b5a3f3e5d67adbd0aa996eac48e78628bd324521b331629d3db866e5af2de | quote: | Max file size | 10 GB | 2 GB | 50 GB | Unlimited* | 5 GB | Unlimited |
  - [1] 2026-11-03: the free plan includes 50 GB total storage | capture: sha256:a97b5a3f3e5d67adbd0aa996eac48e78628bd324521b331629d3db866e5af2de | quote: | Total storage | 50 GB | — | — | — | — | — |
  - [1] 2026-11-03: free file expiry is 90 days | capture: sha256:a97b5a3f3e5d67adbd0aa996eac48e78628bd324521b331629d3db866e5af2de | quote: | File expiry | 90 days | 3 days | 30 days | Auto-deleted | 7 days | Until sender closes |
  - [1] 2026-11-03: the cheapest paid plan starts at $9.99 a month | capture: sha256:a97b5a3f3e5d67adbd0aa996eac48e78628bd324521b331629d3db866e5af2de | quote: | Starting paid price | $9.99/mo | $12/mo | — | ~$9.99/mo | — | — |
- sources:
  - [1] https://fileshot.io/pricing
  - [2] https://fileshot.io/
