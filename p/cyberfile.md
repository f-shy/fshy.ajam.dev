# CyberFile

> cyberfile.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyberfile/ | JSON https://fshy.ajam.dev/api/v1/entity/cyberfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CyberFile

- `debrid/cyberfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (freemium, anonymous uploads) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://cyberfile.me/faq
- price unverified: the premium price page was not readable
- free tier: Upload files up-to 10 GB anonymously; free/non-account files kept for 14 days. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ says uploading and downloading is free for all users; no total storage or download byte allowance is printed.
- per-object cap: Each file you upload must be less than 10 GB in size for free/non accounts or less than 100 GB in size for premium accounts. | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3 for free and non-account uploads; premium is 100 GB.
- retention: Free/non accounts files are kept for 14 days. Premium accounts files are kept for unlimited days. | days: 14 | source: [1]
- egress: No download byte allowance or speed figure is printed on the pages read. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The homepage says 'Upload files up-to 10 GB anonymously' and offers an optional Register to link uploads to an account.
- interface: unknown
- limits:
  - per-object-cap: 10 GB free and non-account, 100 GB premium [1]
  - retention-clamped (binding): 14 days free and non-account, unlimited premium [1]
- binding note: 14-day deletion on the free tier bounds how long a file can be fetched; the 10 GB cap is second.
- interface detail: Web upload with a register_non_user route; no API page was read.
- tooling: Browser only as read. No rclone backend found.
- composes with: 10 GB anonymous files kept 14 days: a hand-off point for one large file, not storage.
- reliability: The /upgrade page answered with the homepage, so no premium price was readable.
- evidence note: FAQ and homepage read on the vendor site on 2026-11-03. Premium price unverified: the upgrade page redirected to the homepage.
- evidence:
  - [1] 2026-11-03: the per-file caps are 10 GB free and 100 GB premium | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Each file you upload must be less than 10 GB in size for free/non accounts or less than 100 GB in size for premium accounts.
  - [1] 2026-11-03: free retention is 14 days | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Free/non accounts files are kept for 14 days. Premium accounts files are kept for unlimited days.
  - [2] 2026-11-03: anonymous upload is offered up to 10 GB | capture: sha256:c708a7fd4a02be751ae8b002a025ffc90b3b522eea0b87481105337162cb6af6 | quote: Upload files up-to 10 GB anonymously.
- sources:
  - [1] https://cyberfile.me/faq
  - [2] https://cyberfile.me/
